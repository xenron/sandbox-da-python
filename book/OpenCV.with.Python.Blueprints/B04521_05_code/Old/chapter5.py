# chapter5.py

import cv2 as cv3
import numpy as np

from saliency import Saliency
from multipleobjectstracker import MultipleObjectsTracker

def main():
    # open video file
    video = cv3.VideoCapture("soccer.avi")

    # initialize tracker
    mot = MultipleObjectsTracker()

    while True:
        # grab next frame
        ret,img = video.read()
        if ret:
            # original video is too big: grab some meaningful ROI
            img = img[140:500,100:600]

            img = cv3.imread("IMG_1688.JPG")

            # generate saliency map
            sal = Saliency(img, useNumpyFFT=False, gaussKernel=(3,3))

            cv3.imwrite("magn.jpg",sal.PlotMagnitudeSpectrum())

            cv3.imshow("original",img)
            cv3.imshow("saliency",sal.GetSaliencyMap())
            cv3.imshow("objects",sal.GetProtoObjectsMap(useOtsu=False))
            cv3.imshow("tracker",mot.AdvanceFrame(img, sal.GetProtoObjectsMap(useOtsu=False)))

            if cv3.waitKey(100) & 0xFF == ord('q'):
                cv3.imwrite("tracker.jpg",tracker)
                break
        else:
            break

    video.release()
    cv3.destroyAllWindows()

if __name__ == '__main__':
    main()