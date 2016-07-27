import cv2
import cv
import wx
import numpy as np
import time

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title, capture, fps=15):
        # initialize screen capture
        self.capture = capture

        # determine window size and init wx.Frame
        ret,frame = self.capture.read()
        self.imgHeight,self.imgWidth = frame.shape[:2]
        buffer = np.zeros((self.imgWidth,self.imgHeight,3),np.uint8)
        self.bmp = wx.BitmapFromBuffer(self.imgWidth, self.imgHeight, buffer)
        wx.Frame.__init__(self, parent, id, title, size=(self.imgWidth, self.imgHeight))
        
        # counteract flicker
        def disable_event(*pargs,**kwargs):
            pass
        self.Bind(wx.EVT_ERASE_BACKGROUND, disable_event)

        self.CreateLayout()
        self.InitializeAlgorithm()

        # set up periodic screen capture
        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)
        self.Bind(wx.EVT_TIMER, self.NextFrame)


    def OnCloseFrame(self, event):
        """ executed whenever close button is pressed """
        self.Destroy()

    def InitializeAlgorithm(self):
        # setting chessboard size
        self.chessboard_size = (9,6)
        
        # prepare object points
        self.objp = np.zeros((np.prod(self.chessboard_size),3), dtype=np.float32)
        self.objp[:,:2] = np.mgrid[0:self.chessboard_size[0],0:self.chessboard_size[1]].T.reshape(-1,2)

        # prepare recording
        self.recording = False
        self.recordMinNumFrames = 20
        self.ResetRecording()


    def OnButtonCalibrate(self, event):
        """ whenever calibrate button is pressed, we start looking for the chessboard
            in the image and collecting data """
        self.button_calibrate.Disable()
        self.recording = True
        self.ResetRecording()

    def ResetRecording(self):
        """ unset recording mode and reset list of collected points """
        self.recordCnt = 0
        self.obj_points = []
        self.img_points = []

    def CreateLayout(self):
        """ create frame/button layout """
        self.pnl1 = wx.Panel(self, -1, size=(self.imgWidth,self.imgHeight))
        self.pnl1.SetBackgroundColour(wx.BLACK)

        # create a horizontal layout with a single button
        pnl2 = wx.Panel(self, -1 )
        self.button_calibrate = wx.Button(pnl2, label='Calibrate Camera')
        self.Bind(wx.EVT_BUTTON, self.OnButtonCalibrate)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.button_calibrate)
        pnl2.SetSizer(hbox)

        # display the button layout beneath the video stream
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pnl1, 1, flag=wx.EXPAND)
        sizer.Add(pnl2, flag=wx.EXPAND | wx.BOTTOM | wx.TOP, border=1)

        self.SetMinSize((self.imgWidth, self.imgHeight))
        self.SetSizer(sizer)
        self.Centre()

    def NextFrame(self, event):
        # acquire new frame, ignore timestamp
        ret,frame = self.capture.read()
        if ret:

            processedFrame = self.ProcessFrame(frame)
            processedFrame = cv2.cvtColor(processedFrame, cv2.COLOR_BGR2RGB)

            # update buffer and paint
            self.bmp.CopyFromBuffer(processedFrame)
            deviceContext = wx.BufferedPaintDC(self.pnl1)

            deviceContext.DrawBitmap(self.bmp, 0, 0)
            del deviceContext


    def ProcessFrame(self, frame):
        """ process each frame """

        # if we are not recording, just display the frame
        if not self.recording:
            return frame

        # else we're recording
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.uint8)

        if self.recordCnt < self.recordMinNumFrames:
            # need at least some number of chessboard samples before we can calculate
            # the intrinsic matrix
            ret,corners = cv2.findChessboardCorners(frameGray, self.chessboard_size, None)

            if ret:
                cv2.drawChessboardCorners(frame, self.chessboard_size, corners, ret)

                # refine found corners
                criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.01)
                cv2.cornerSubPix(frameGray, corners, (9,9), (-1,-1), criteria)

                self.obj_points.append(self.objp)
                self.img_points.append(corners)
                self.recordCnt += 1

        else:
            # we have already collected enough frames, so now we want to calculate the
            # intrinsic camera matrix (K) and the distortion vector (dist)
            print "Calibrating..."
            ret,K,dist,rvecs,tvecs = cv2.calibrateCamera(self.obj_points, self.img_points,
                (self.imgHeight,self.imgWidth), None, None)

            print "K=", K
            print "dist=", dist

            # double-check reconstruction error (should be as close to zero as possible)
            mean_error = 0
            for i in xrange(len(self.obj_points)):
                img_points2,_ = cv2.projectPoints(self.obj_points[i], rvecs[i], tvecs[i], K, dist)
                error = cv2.norm(self.img_points[i], img_points2, cv2.NORM_L2)/len(img_points2)
                mean_error += error

            print "mean error=",mean_error

            self.recording = False
            self.ResetRecording()
            self.button_calibrate.Enable()

        
        return frame


def main():
    capture = cv2.VideoCapture(0)
    if not(capture.isOpened()):
        capture.open()

    capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    app = wx.App()
    frame = MyFrame(None, -1, 'calibrate.py', capture, fps=5)
    frame.Show(True)
    app.MainLoop()

    # When everything done, release the capture
    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()