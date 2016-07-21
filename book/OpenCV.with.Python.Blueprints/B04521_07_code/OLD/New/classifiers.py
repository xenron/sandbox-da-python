import cv2 as cv3
import numpy as np
from abc import ABCMeta, abstractmethod
from matplotlib import pyplot as plt

class Classifier:
    """
        Abstract base class for all classifiers

        A classifier needs to implement at least two methods:
        * fit:       A method to train the classifier by fitting the model to the data.
        * evaluate:  A method to test the classifier by predicting labels of some test
                     data based on the trained model.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def fit(self, X_train, y_train): pass

    @abstractmethod
    def evaluate(self, X_test, y_test, visualize=False): pass


class MultiLayerPerceptron(Classifier):
    """ Multi-Layer Perceptron """
    def __init__(self, layerSizes, classLabels, params=None):
        self.numFeatures = layerSizes[0]
        self.numClasses = layerSizes[-1]
        self.classLabels = classLabels
        self.params = params or dict()
        
        # initialize MLP
        self.model = cv3.ANN_MLP()
        self.model.create(layerSizes)

    def load(self, file):
        """ load a pre-trained MLP from file """
        self.model.load(file)

    def save(self, file):
        """ save a trained MLP to file """
        self.model.save(file)

    def fit(self, X_train, y_train, params=None):
        """ fit model to data """
        if params is None:
            params = self.params

        # need int labels as 1-hot code
        y_train = self.__labels_str_to_num(y_train)
        y_train = self.__one_hot(y_train).reshape(-1, self.numClasses)

        # train model
        self.model.train(X_train, y_train, None, params = params)

    def predict(self, X_test):
        """ predict the labels of test data """
        ret,y_hat = self.model.predict(X_test)

        # find the most active cell in the output layer
        y_hat = np.argmax(y_hat,1)

        # return string labels
        return self.__labels_num_to_str(y_hat)

    def evaluate(self, X_test, y_test, visualize=False):
        """ evaluate model performance """
        # need int labels
        y_test = self.__labels_str_to_num(y_test)

        # predict labels
        ret,Y_vote = self.model.predict(X_test)

        accuracy = self.__accuracy(y_test, Y_vote)
        precision = self.__precision(y_test, Y_vote)
        recall = self.__recall(y_test, Y_vote)

        return (accuracy, precision, recall)

    def __one_hot(self, y_train):
        """ convert a list of labels to a 1 hot code """
        numSamples = len(y_train)
        new_responses = np.zeros(numSamples*self.numClasses, np.float32)
        resp_idx = np.int32(y_train + np.arange(numSamples)*self.numClasses)
        new_responses[resp_idx] = 1
        return new_responses

    def __labels_str_to_num(self, labels):
        """ convert string labels to their corresponding ints """
        return np.array([int(np.where(self.classLabels==l)[0]) for l in labels])

    def __labels_num_to_str(self, labels):
        """ convert integer labels to their corresponding string name """
        return self.classLabels[labels]

    def __accuracy(self, y_test, Y_vote):
        """ Calculates the accuracy based on a vector of ground-truth labels (y_test)
            and a 2D voting matrix (Y_vote) of size (len(y_test),numClasses). """
        # predicted classes
        y_hat = np.argmax(Y_vote, axis=1)

        # all cases where predicted class was correct
        mask = y_hat == y_test
        return np.count_nonzero(mask)*1./len(y_test)

    def __confusion(self, y_test, Y_vote):
        """ Calculates confusion matrix based on a vector of ground-truth labels (y-test)
            and a 2D voting matrix (Y_vote) of size (len(y_test),numClasses).
            Matrix element conf[r,c] will contain the number of samples that were predicted
            to have label r but have ground-truth label c. """
        y_hat = np.argmax(Y_vote, axis=1)
        conf = np.zeros((self.numClasses,self.numClasses)).astype(np.int32)
        for c_true in xrange(self.numClasses):
            # looking at all samples of a given class, c_true
            # how many were classified as c_true? how many as others?
            for c_pred in xrange(self.numClasses):
                y_this = np.where((y_test==c_true) * (y_hat==c_pred))
                conf[c_pred,c_true] = np.count_nonzero(y_this)
        return conf

    def __precision(self, y_test, Y_vote):
        """ precision extended to multi-class classification """
        # predicted classes
        y_hat = np.argmax(Y_vote, axis=1)

        if True or self.mode == "one-vs-one":
            # need confusion matrix
            conf = self.__confusion(y_test, Y_vote)

            # consider each class separately
            prec = np.zeros(self.numClasses)
            for c in xrange(self.numClasses):
                # true positives: label is c, classifier predicted c
                tp = conf[c,c]

                # false positives: label is c, classifier predicted not c
                fp = np.sum(conf[:,c]) - conf[c,c]

                # precision
                prec[c] = tp*1./(tp+fp)
        elif self.mode == "one-vs-rest":
            # consider each class separately
            prec = np.zeros(self.numClasses)
            for c in xrange(self.numClasses):
                # true positives: label is c, classifier predicted c
                tp = np.count_nonzero((y_test==c) * (y_hat==c))

                # false positives: label is c, classifier predicted not c
                fp = np.count_nonzero((y_test==c) * (y_hat!=c))

                prec[c] = tp*1./(tp+fp)
        return prec

    def __recall(self, y_test, Y_vote):
        """ recall extended to multi-class classification """
        # predicted classes
        y_hat = np.argmax(Y_vote, axis=1)

        if True or self.mode == "one-vs-one":
            # need confusion matrix
            conf = self.__confusion(y_test, Y_vote)

            # consider each class separately
            recall = np.zeros(self.numClasses)
            for c in xrange(self.numClasses):
                # true positives: label is c, classifier predicted c
                tp = conf[c,c]

                # false negatives: label is not c, classifier predicted c
                fn = np.sum(conf[c,:]) - conf[c,c]
                if tp>0 and fn>0:
                    recall[c] = tp*1./(tp+fn)
        elif self.mode == "one-vs-rest":
            # consider each class separately
            recall = np.zeros(self.numClasses)
            for c in xrange(self.numClasses):
                # true positives: label is c, classifier predicted c
                tp = np.count_nonzero((y_test==c) * (y_hat==c))

                # false negatives: label is not c, classifier predicted c
                fn = np.count_nonzero((y_test!=c) * (y_hat==c))

                recall[c] = tp*1./(tp+fn)
        return recall