# chapter7.py

import time
import wx
from os import path
import cPickle as pickle

import cv2 as cv3
import numpy as np

from datasets import homebrew
from classifiers import MultiLayerPerceptron

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title, capture,
        saveTrainingFile='datasets/faces_training.pkl',
        loadPreprocessedData='datasets/faces_preprocessed.pkl',
        loadMLP='params/mlp.xml',
        faceCasc='params/haarcascade_frontalface_default.xml',
        leftEyeCasc='params/haarcascade_lefteye_2splits.xml',
        rightEyeCasc='params/haarcascade_righteye_2splits.xml',
        fps=10):

        # initialize screen capture
        self.capture = capture
        ret,frame = self.capture.read()

        # determine window size and init wx.Frame
        self.imgHeight,self.imgWidth = frame.shape[:2]
        self.bmp = wx.BitmapFromBuffer(self.imgWidth, self.imgHeight, frame)
        wx.Frame.__init__(self, parent, id, title, size=(self.imgWidth, self.imgHeight+60))

        # set up periodic screen capture
        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)
        self.Bind(wx.EVT_TIMER, self.NextFrame)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        # counteract flicker
        def disable_event(*pargs,**kwargs):
            pass
        self.Bind(wx.EVT_ERASE_BACKGROUND, disable_event)

        # initialize data structure
        self.dataFile = saveTrainingFile
        self.samples = []
        self.labels = []

        # call method to save data upon exiting
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        # create the layout, which draws all buttons and
        # connects events to class methods
        self.CreateLayout()

        self.InitAlgorithm(faceCasc, leftEyeCasc, rightEyeCasc, loadPreprocessedData, loadMLP)

    def InitAlgorithm(self, faceCasc, leftEyeCasc, rightEyeCasc, loadPreprocessedData, loadMLP):
        # load pre-trained cascades
        self.faceCasc = cv3.CascadeClassifier(faceCasc)
        if self.faceCasc.empty():
            print 'Warning: Could not load face cascade:', faceCasc
            raise SystemExit
        self.leftEyeCasc = cv3.CascadeClassifier(leftEyeCasc)
        if self.leftEyeCasc.empty():
            print 'Warning: Could not load left eye cascade:', leftEyeCasc
            raise SystemExit
        self.rightEyeCasc = cv3.CascadeClassifier(rightEyeCasc)
        if self.rightEyeCasc.empty():
            print 'Warning: Could not load right eye cascade:', rightEyeCasc
            raise SystemExit

        # load preprocessed dataset to access labels and PCA params
        if path.isfile(loadPreprocessedData):
            (_,y_train),(_,y_test),self.pca_V,self.pca_m = homebrew.load_from_file(loadPreprocessedData)
            self.allLabels = np.unique(np.hstack((y_train,y_test)))

            # load pre-trained multi-layer perceptron
            if path.isfile(loadMLP):
                self.MLP = MultiLayerPerceptron(np.array([self.pca_V.shape[1], len(self.allLabels)]),
                    self.allLabels)
                self.MLP.load(loadMLP)
            else:
                print "Warning: Testing is disabled"
                print "Could not find pre-trained MLP file ", loadMLP
                self.testing.Disable()
        else:
            print "Warning: Testing is disabled"
            print "Could not find preprocessed data file ", loadPreprocessedData
            self.testing.Disable()

    def CreateLayout(self):
        self.pnl1 = wx.Panel(self, -1, size=(self.imgWidth,self.imgHeight))
        self.pnl1.SetBackgroundColour(wx.BLACK)

        # create horizontal layout with train/test buttons
        pnl2 = wx.Panel(self, -1)
        self.training = wx.RadioButton(pnl2, -1, 'Train', (10, 10), style=wx.RB_GROUP)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnTraining, self.training)
        self.testing = wx.RadioButton(pnl2, -1, 'Test')
        self.Bind(wx.EVT_RADIOBUTTON, self.OnTesting, self.testing)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.training, 1)
        hbox2.Add(self.testing, 1)
        pnl2.SetSizer(hbox2)

        # create a horizontal layout with all buttons
        pnl3 = wx.Panel(self, -1 )
        self.neutral = wx.RadioButton(pnl3, -1, 'neutral', (10, 10), style=wx.RB_GROUP)
        self.happy = wx.RadioButton(pnl3, -1, 'happy')
        self.sad = wx.RadioButton(pnl3, -1, 'sad')
        self.surprised = wx.RadioButton(pnl3, -1, 'surprised')
        self.angry = wx.RadioButton(pnl3, -1, 'angry')
        self.disgusted = wx.RadioButton(pnl3, -1, 'disgusted')
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.neutral, 1)
        hbox3.Add(self.happy, 1)
        hbox3.Add(self.sad, 1)
        hbox3.Add(self.surprised, 1)
        hbox3.Add(self.angry, 1)
        hbox3.Add(self.disgusted, 1)
        pnl3.SetSizer(hbox3)

        # create horizontal layout with single snapshot button
        pnl4 = wx.Panel(self, -1)
        self.snapshot = wx.Button(pnl4, -1, 'Take Snapshot')
        self.Bind(wx.EVT_BUTTON, self.OnSnapshot, self.snapshot)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.snapshot, 1)
        pnl4.SetSizer(hbox4)

        # arrange all horizontal layouts vertically
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pnl1, 1, flag=wx.EXPAND)
        sizer.Add(pnl2, flag=wx.EXPAND | wx.TOP, border=1)
        sizer.Add(pnl3, flag=wx.EXPAND | wx.BOTTOM, border=1)
        sizer.Add(pnl4, flag=wx.EXPAND | wx.BOTTOM, border=1)

        self.SetMinSize((self.imgWidth, self.imgHeight))
        self.SetSizer(sizer)
        self.Centre()

    def NextFrame(self, event):
        """ called whenever new frame is received, prepares frame for display """
        ret, self.thisFrame = self.capture.read()
        if ret:
            # process frame
            frame = cv3.cvtColor(self.thisFrame, cv3.COLOR_BGR2RGB)
            frame = self.ProcessFrame(frame)

            # update buffer and paint (EVT_PAINT triggered by Refresh)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh(eraseBackground=False)

    def ProcessFrame(self, frame):
        """ detects face, predicts face label in testing mode """
        # detect face
        scale = 4
        frameCasc = cv3.cvtColor(cv3.resize(frame, (0,0), fx=1./scale, fy=1./scale), cv3.COLOR_RGB2GRAY)
        faces = self.faceCasc.detectMultiScale(frameCasc, scaleFactor=1.1, minNeighbors=3,
            flags=cv3.cv.CV_HAAR_FIND_BIGGEST_OBJECT) * scale

        # if face is found
        for (x,y,w,h) in faces:
            # extract head region from bounding box
            cv3.rectangle(frame, (x, y), (x+w, y+h), (100, 255, 0), 2)
            self.head = cv3.cvtColor(frame[y:y+h, x:x+w], cv3.COLOR_RGB2GRAY)

            # in testing mode: predict label of facial expression
            if self.testing.GetValue()==True:
                # preprocess face: align
                ret,head = self.AlignHead(self.head)
                if ret:
                    # extract features using PCA (loaded from file)
                    X,_,_ = homebrew.extract_features([head.flatten()], self.pca_V, self.pca_m)

                    # predict label with pre-trained MLP
                    label = self.MLP.predict(np.array(X))[0]

                    # draw label above bounding box
                    cv3.putText(frame, str(label), (x,y-20), cv3.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            break # need only look at first, largest face

        return frame

    def AlignHead(self, head):
        """ aligns a head region using affine transformations (rotation, scaling) """
        height,width = head.shape[:2]

        # detect left eye
        leftEyeRegion = head[0.2*height:0.5*height, 0.1*width:0.5*width]
        leftEye = self.leftEyeCasc.detectMultiScale(leftEyeRegion, scaleFactor=1.1, minNeighbors=3,
            flags=cv3.cv.CV_HAAR_FIND_BIGGEST_OBJECT)
        leftEyeCenter = None
        for (xl,yl,wl,hl) in leftEye:
            # find the center of the detected eye region
            leftEyeCenter = np.array([0.1*width+xl+wl/2, 0.2*height+yl+hl/2])
            break # need only look at first, largest eye

        # detect right eye
        rightEyeRegion = head[0.2*height:0.5*height, 0.5*width:0.9*width]
        rightEye = self.rightEyeCasc.detectMultiScale(rightEyeRegion, scaleFactor=1.1, minNeighbors=3,
            flags=cv3.cv.CV_HAAR_FIND_BIGGEST_OBJECT)
        rightEyeCenter = None
        for (xr,yr,wr,hr) in rightEye:
            # find the center of the detected eye region
            rightEyeCenter = np.array([0.5*width+xr+wr/2, 0.2*height+yr+hr/2])
            break # need only look at first, largest eye

        # need both eyes in order to align face
        # else break here and report failure (False)
        if leftEyeCenter is None or rightEyeCenter is None:
            return (False, head)

        # we want the eye to be at 25% of the width, and 20% of the height
        # resulting image should be square (desiredImgWidth,desiredImgHeight)
        desiredEyeX = 0.25
        desiredEyeY = 0.2
        desiredImgWidth = 200
        desiredImgHeight = desiredImgWidth

        # get center point between the two eyes and calculate angle
        eyeCenter = (leftEyeCenter+rightEyeCenter)/2
        eyeAngleDeg = np.arctan2(rightEyeCenter[1]-leftEyeCenter[1],
            rightEyeCenter[0]-leftEyeCenter[0])*180.0/cv3.cv.CV_PI

        # scale distance between eyes to desired length
        eyeSizeScale = (1.0-desiredEyeX*2)*desiredImgWidth/np.linalg.norm(rightEyeCenter-leftEyeCenter)

        # get rotation matrix
        rotMat = cv3.getRotationMatrix2D(tuple(eyeCenter), eyeAngleDeg, eyeSizeScale)

        # shift center of the eyes to be centered in the image
        rotMat[0,2] += desiredImgWidth*0.5 - eyeCenter[0]
        rotMat[1,2] += desiredEyeY*desiredImgHeight - eyeCenter[1]

        # warp perspective to make eyes aligned on horizontal line and scaled to right size
        res = cv3.warpAffine(head, rotMat, (desiredImgWidth,desiredImgWidth))

        # return success
        return (True,res)

    def OnTraining(self, evt):
        """ whenever training mode is selected, enable all training-related buttons """
        self.neutral.Enable()
        self.happy.Enable()
        self.sad.Enable()
        self.surprised.Enable()
        self.angry.Enable()
        self.disgusted.Enable()
        self.snapshot.Enable()

    def OnTesting(self, evt):
        """ whenever testing mode is selected, disable all training-related buttons """
        self.neutral.Disable()
        self.happy.Disable()
        self.sad.Disable()
        self.surprised.Disable()
        self.angry.Disable()
        self.disgusted.Disable()
        self.snapshot.Disable()

    def OnPaint(self, evt):
        """ called whenever new frame needs to be drawn """
        # read and draw buffered bitmap
        deviceContext = wx.BufferedPaintDC(self.pnl1)
        deviceContext.DrawBitmap(self.bmp, 0, 0)
        del deviceContext

    def OnSnapshot(self, evt):
        """ called whenever Take Snapshot button is clicked """
        if self.neutral.GetValue()==True:
            label = 'neutral'
        elif self.happy.GetValue()==True:
            label = 'happy'
        elif self.sad.GetValue()==True:
            label = 'sad'
        elif self.surprised.GetValue()==True:
            label = 'surprised'
        elif self.angry.GetValue()==True:
            label = 'angry'
        elif self.disgusted.GetValue()==True:
            label = 'disgusted'

        ret,head = self.AlignHead(self.head)
        if ret:
            self.samples.append(head.flatten())
            self.labels.append(label)
        else:
            print "Could not align head (eye detection failed?)"

    def OnExit(self, evt):
        """ called whenever window is closed """
        # if we have collected some samples, dump them to file
        if len(self.samples) > 0:
            # make sure we don't overwrite an existing file
            if path.isfile(self.dataFile):
                # file already exists, construct new load_from_file
                load_from_file,fileext = path.splitext(self.dataFile)
                offset = 0
                while True:
                    file = load_from_file + "-" + str(offset) + fileext
                    if path.isfile(file):
                        offset += 1
                    else:
                        break
                self.dataFile = file

            # dump samples and labels to file
            f = open(self.dataFile,'wb')
            pickle.dump(self.samples, f)
            pickle.dump(self.labels, f)
            f.close()

            # inform user that file was created
            print "Saved", len(self.samples), "samples to",self.dataFile

        # deallocate
        self.Destroy()


def main():
    capture = cv3.VideoCapture(0)
    if not(capture.isOpened()):
        capture.open()

    capture.set(cv3.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv3.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    app = wx.App()
    frame = MyFrame(None, -1, 'chapter7.py', capture)
    frame.Show(True)
    app.MainLoop()

    # When everything done, release the capture
    capture.release()
    cv3.destroyAllWindows()


if __name__ == '__main__':
    main()