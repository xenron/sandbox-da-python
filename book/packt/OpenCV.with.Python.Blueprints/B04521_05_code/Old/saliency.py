import cv2 as cv3
import numpy as np
from matplotlib import pyplot as plt


class Saliency:
    """
        Calculates a saliency map from a grayscale or RGB image
    """
    def __init__(self, img, useNumpyFFT=True, gaussKernel=(5,5)):
        """ constructor """
        self.useNumpyFFT = useNumpyFFT
        self.gaussKernel = gaussKernel
        self.frameOrig = img

        # downsample image for processing
        self.smallShape = (64,64)
        self.frameSmall = cv3.resize(img, self.smallShape[1::-1])

        # whether we need to do the math (True) or it has already
        # been done (False)
        self.needToCalcSaliencyMap = True

    def GetSaliencyMap(self):
        if self.needToCalcSaliencyMap:
            # haven't calculated saliency map for this frame yet
            num_channels = 1
            if len(self.frameOrig.shape)==2:
                # single channel
                sal = self.__GetChannelSalMagn(self.frameSmall)
            else:
                # multiple channels: consider each channel independently
                sal = np.zeros_like(self.frameSmall).astype(np.float32)
                for c in xrange(self.frameSmall.shape[2]):
                    sal[:,:,c] = self.__GetChannelSalMagn(self.frameSmall[:,:,c])

                # overall saliency: channel mean
                sal = np.mean(sal,2)

            # postprocess: blur, square, and normalize
            if self.gaussKernel is not None:
                sal = cv3.GaussianBlur(sal, self.gaussKernel, sigmaX=8, sigmaY=0)
            sal = sal**2
            sal = np.float32(sal)/np.max(sal)

            # scale up
            sal = cv3.resize(sal, self.frameOrig.shape[1::-1])

            # store a copy so we do the work only once per frame
            self.saliencyMap = sal
            self.needToCalcSaliencyMap = False

        return self.saliencyMap


    def __GetChannelSalMagn(self, channel):
        # do FFT and get log-spectrum
        if self.useNumpyFFT:
            imgDFT = np.fft.fft2(channel)
            magnitude,angle = cv3.cartToPolar(np.real(imgDFT), np.imag(imgDFT))
        else:
            imgDFT = cv3.dft(np.float32(channel), flags=cv3.DFT_COMPLEX_OUTPUT)
            magnitude,angle = cv3.cartToPolar(imgDFT[:,:,0], imgDFT[:,:,1])

        # get log amplitude
        logAmpl = np.log10(magnitude.clip(min=1e-9))

        # blur log amplitude with avg filter
        logAmplBlur = cv3.blur(logAmpl, (3,3))

        # residual
        residual = np.exp(logAmpl - logAmplBlur)

        # back to cartesian frequency domain
        if self.useNumpyFFT:
            realPart,imagPart = cv3.polarToCart(residual, angle)
            imgCombined = np.fft.ifft2(realPart + 1j*imagPart)
            magnitude,_ = cv3.cartToPolar(np.real(imgCombined), np.imag(imgCombined))
        else:
            imgDFT[:,:,0],imgDFT[:,:,1] = cv3.polarToCart(residual, angle)
            imgCombined = cv3.idft(imgDFT)
            magnitude,_ = cv3.cartToPolar(imgCombined[:,:,0], imgCombined[:,:,1])

        # magnitude = magnitude - np.mean(magnitude)

        # if self.gaussKernel is not None:
        #     magnitude = cv3.GaussianBlur(np.float32(magnitude), self.gaussKernel, sigmaX=8, sigmaY=0)

        # magnitude = magnitude**2
        # magnitude = np.float32(magnitude)/np.max(magnitude)

        return magnitude

    def PlotMagnitudeSpectrum(self):
        # convert the frame to grayscale if necessary
        if len(self.frameOrig.shape)>2:
            frame = cv3.cvtColor(self.frameOrig, cv3.COLOR_BGR2GRAY)
        else:
            frame = self.frameOrig

        # expand the image to an optimal size for FFT
        rows,cols = self.frameOrig.shape[:2]
        nrows = cv3.getOptimalDFTSize(rows)
        ncols = cv3.getOptimalDFTSize(cols)
        frame = cv3.copyMakeBorder(frame, 0, ncols-cols, 0, nrows-rows, 
            cv3.BORDER_CONSTANT, value = 0)

        # do FFT and get log-spectrum
        imgDFT = np.fft.fft2(frame)
        spectrum = np.log10(np.abs(np.fft.fftshift(imgDFT)))

        # return for plotting
        return 255*spectrum/np.max(spectrum)

    def PlotPowerSpectrum(self):
        # convert the frame to grayscale if necessary
        if len(self.frameOrig.shape)>2:
            frame = cv3.cvtColor(self.frameOrig, cv3.COLOR_BGR2GRAY)
        else:
            frame = self.frameOrig

        # expand the image to an optimal size for FFT
        rows,cols = self.frameOrig.shape[:2]
        nrows = cv3.getOptimalDFTSize(rows)
        ncols = cv3.getOptimalDFTSize(cols)
        frame = cv3.copyMakeBorder(frame, 0, ncols-cols, 0, nrows-rows, 
            cv3.BORDER_CONSTANT, value = 0)

        # do FFT and get log-spectrum
        if self.useNumpyFFT:
            imgDFT = np.fft.fft2(frame)
            spectrum = np.log10(np.real(np.abs(imgDFT))**2)
        else:
            imgDFT = cv3.dft(np.float32(frame), flags=cv3.DFT_COMPLEX_OUTPUT)
            spectrum = np.log10(imgDFT[:,:,0]**2+imgDFT[:,:,1]**2)

        # radial average
        L = max(frame.shape)
        freqs = np.fft.fftfreq(L)[:L/2]
        dists = np.sqrt(np.fft.fftfreq(frame.shape[0])[:,None]**2
            + np.fft.fftfreq(frame.shape[1])**2)
        dcount = np.histogram(dists.ravel(), bins=freqs)[0]
        histo,bins = np.histogram(dists.ravel(), bins=freqs, weights=spectrum.ravel())

        centers = (bins[:-1] + bins[1:]) / 2
        plt.plot(centers, histo/dcount)
        plt.xlabel('frequency')
        plt.ylabel('log-spectrum')
        plt.show()

    def GetProtoObjectsMap(self, useOtsu=True):
        saliency = self.GetSaliencyMap()

        if useOtsu:
            _,imgObjects = cv3.threshold(np.uint8(saliency*255), 0, 255, cv3.THRESH_BINARY + cv3.THRESH_OTSU)
        else:
            thresh = np.mean(saliency)*255*3
            _,imgObjects = cv3.threshold(np.uint8(saliency*255), thresh, 255, cv3.THRESH_BINARY)
        return imgObjects