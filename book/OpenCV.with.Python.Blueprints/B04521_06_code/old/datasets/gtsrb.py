import cv2 as cv3
import numpy as np
import csv
from matplotlib import cm
from matplotlib import pyplot as plt

def load_data(rootpath="datasets", feature="hog", cut_roi=True, test_split=0.2, plot_samples=False, seed=113):
    """ load dataset """

    # hardcode all available class labels
    classes = np.array([0,4,8,12,16,20,24,28,32,36])

    # read all training samples and corresponding class labels
    X = [] # images
    labels = [] # corresponding labels
    for c in xrange(len(classes)):
        prefix = rootpath + '/' + format(classes[c], '05d') + '/' # subdirectory for class
        gtFile = open(prefix + 'GT-'+ format(classes[c], '05d') + '.csv') # annotations file
        gtReader = csv.reader(gtFile, delimiter=';') # csv parser for annotations file
        gtReader.next() # skip header
        # loop over all images in current annotations file
        for row in gtReader:
            # first column is filename
            im = cv3.imread(prefix+row[0])

            if cut_roi:
                im = im[np.int(row[4]):np.int(row[6]),np.int(row[3]):np.int(row[5]),:]

            X.append(im)
            labels.append(c)
        gtFile.close()

    # perform feature extraction
    if feature is not None:
        X = __extract_feature(X, feature)

    np.random.seed(seed)
    np.random.shuffle(X)
    np.random.seed(seed)
    np.random.shuffle(labels)

    if plot_samples:
        numSamples = 15
        sample_idx = np.random.randint(len(X), size=numSamples)
        sp = 1
        for r in xrange(3):
            for c in xrange(5):
                ax = plt.subplot(3,5,sp)
                sample = X[sample_idx[sp-1]]
                ax.imshow(sample.reshape((32,32)), cmap=cm.Greys_r)
                ax.axis('off')
                sp += 1
        plt.show()

    X_train = X[:int(len(X)*(1-test_split))]
    y_train = labels[:int(len(X)*(1-test_split))]

    X_test = X[int(len(X)*(1-test_split)):]
    y_test = labels[int(len(X)*(1-test_split)):]

    return (X_train, y_train), (X_test, y_test)

def __extract_feature(X, feature):
    """ extract features """

    if feature is None:
        # only resize
        for i in xrange(len(X)):
            orig = cv3.resize(X[i], (32,32))
            X[i] = orig.reshape(-1,1)
    elif feature=="gray":
        # grayscale image (0-centered)
        for i in xrange(len(X)):
            gray = cv3.resize(cv3.cvtColor(X[i], cv3.COLOR_BGR2GRAY), (32,32))
            gray = gray.astype(np.float32)/255. - np.mean(gray)
            X[i] = gray.reshape(-1,1)
    elif feature=="rgb":
        # RGB image (0-centered)
        for i in xrange(len(X)):
            rgb = cv3.resize(X[i], (32,32))
            rgb = rgb.astype(np.float32)/255. - np.mean(rgb)
            print rgb.shape
            X[i] = rgb.reshape(-1,1)
    elif feature=="hsv":
        # HSV image (0-centered)
        for i in xrange(len(X)):
            hsv = cv3.resize(cv3.cvtColor(X[i], cv3.COLOR_BGR2HSV), (32,32))
            hsv = hsv.astype(np.float32)/255. - np.mean(hsv)
            X[i] = hsv.reshape(-1,1)
    elif feature=="surf":
        # SURF features
        surf = cv3.SURF()
        dense = cv3.FeatureDetector_create("Dense")
        for i in xrange(len(X)):
            kp = dense.detect(cv3.resize(cv3.cvtColor(X[i], cv3.COLOR_BGR2GRAY), (32,32)))
            kp,des = surf.compute(X[i], kp)
            X[i] = des[:9,:].reshape(-1,1)
    elif feature=="hog":
        # histogram of gradients
        hog = cv3.HOGDescriptor((32,32), (16,16), (8,8), (8,8), 9)
        for i in xrange(len(X)):
            im = cv3.resize(X[i], (32,32))
            X[i] = hog.compute(im)

    return X