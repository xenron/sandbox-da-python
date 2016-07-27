import numpy as np
import cv2 as cv3
import copy

class MultipleObjectsTracker:
    def __init__(self, minArea=400, minShift2=5):
        """ constructor """
        self.object_roi = []
        self.object_box = []

        self.min_cnt_area = minArea
        self.min_shift2 = minShift2

        # Setup the termination criteria, either 100 iteration or move by at least 1 pt
        self.term_crit = ( cv3.TERM_CRITERIA_EPS | cv3.TERM_CRITERIA_COUNT, 100, 1 )

    def AdvanceFrame(self, frame, protoObjectsMap):
        """
            tracks all objects via the following steps:
             - adds all bounding boxes from saliency map as potential
               targets
             - finds bounding boxes from previous frame in current frame
               via mean-shift tracking
             - combines the two lists by removing duplicates

            certain targets are discarded:
             - targets that are too small
             - targets that don't move
        """
        self.tracker = copy.deepcopy(frame)

        # build a list of all bounding boxes
        box_all = []

        # append to the list all bounding boxes found from the
        # current proto-objects map
        box_all = self.__AppendBoxesFromSaliency(protoObjectsMap, box_all)

        # find all bounding boxes extrapolated from last frame
        # via mean-shift tracking
        box_all = self.__AppendBoxesFromMeanShift(frame, box_all)

        # only keep those that are both salient and in mean shift
        if len(self.object_roi)==0:
            group_thresh = 0 # no previous frame: keep all form saliency
        else:
            group_thresh = 1 # previous frame + saliency
        box_grouped,_ = cv3.groupRectangles(box_all, group_thresh, 0.1)

        # update mean-shift bookkeeping for remaining boxes
        self.__UpdateMeanShiftBookkeeping(frame, box_grouped)

        # draw remaining boxes
        for (x,y,w,h) in box_grouped:
            cv3.rectangle(self.tracker,(x,y),(x+w,y+h),(0,255,0),2)

        return self.tracker


    def __AppendBoxesFromSaliency(self, protoObjectsMap, box_all):
        # find all bounding boxes in new saliency map
        box_sal = []
        cnt_sal,_ = cv3.findContours(protoObjectsMap, 1, 2)
        for cnt in cnt_sal:
            # discard small contours
            if cv3.contourArea(cnt) < self.min_cnt_area:
                continue

            # otherwise add to list of boxes found from saliency map
            box = cv3.boundingRect(cnt)
            box_all.append(box)

        return box_all

    def __AppendBoxesFromMeanShift(self, frame, box_all):
        hsv = cv3.cvtColor(frame, cv3.COLOR_BGR2HSV)

        for i in xrange(len(self.object_roi)):
            roi_hist = copy.deepcopy(self.object_roi[i])
            box_old = copy.deepcopy(self.object_box[i])

            dst = cv3.calcBackProject([hsv],[0],roi_hist,[0,180],1)
            ret,box_new = cv3.meanShift(dst, tuple(box_old), self.term_crit)
            self.object_box[i] = copy.deepcopy(box_new)

            # discard boxes that don't move
            (xo,yo,wo,ho) = box_old
            (xn,yn,wn,hn) = box_new

            co = [xo+wo/2,yo+ho/2]
            cn = [xn+wn/2,yn+hn/2]
            if (co[0]-cn[0])**2 + (co[1]-cn[1])**2 >= self.min_shift2:
                box_all.append(box_new)

        return box_all

    def __UpdateMeanShiftBookkeeping(self, frame, box_grouped):
        hsv = cv3.cvtColor(frame, cv3.COLOR_BGR2HSV)

        self.object_roi = []
        self.object_box = []
        for box in box_grouped:
            (x,y,w,h) = box
            hsv_roi = hsv[y:y+h, x:x+w]
            mask = cv3.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
            roi_hist = cv3.calcHist([hsv_roi],[0],mask,[180],[0,180])
            cv3.normalize(roi_hist,roi_hist,0,255,cv3.NORM_MINMAX)

            self.object_roi.append(roi_hist)
            self.object_box.append(box)