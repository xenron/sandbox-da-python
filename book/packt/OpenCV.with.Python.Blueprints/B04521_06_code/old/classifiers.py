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


class MultiClassSVM(Classifier):
    """
        Multi-class classification using Support Vector Machines (SVMs)

        This class implements an ensemble of SVMs for multi-class classification.
        Whereas some classifiers naturally permit the use of more than two classes
        (such as neural networks), SVMs are binary in nature.

        However, we can turn SVMs into multinomial classifiers using at least two
        different strategies:
        * one-vs-rest: A single classifier is trained per class, with the samples
                       of that class as positives (label 1) and all others as
                       negatives (label 0).
        * one-vs-one:  For k classes, k*(k-1)/2 classifiers are trained for each
                       pair of classes, with the samples of the one class as
                       positives (label 1) and samples of the other class as
                       negatives (label 0).

        Each classifier then votes for a particular class label, and the final
        decision (classification) is based on a majority vote.
    """

    def __init__(self, numClasses, mode="one-vs-rest", params=None):
        """
            hThe constructor makes sure the correct number of classifiers is
            initialized, depending on the mode ("one-vs-rest" or "one-vs-one").

            :param numClasses: The number of classes in the data.

            :param mode:       Which classification mode to use.
                               "one-vs-rest": single classifier per class
                               "one-vs-one":  single classifier per class pair
                               Default: "one-vs-rest"

            :param params:     SVM training parameters.
                               For now, default values are used for all SVMs.
                               Hyperparameter exploration can be achieved by
                               embedding the MultiClassSVM process flow in a 
                               for-loop that classifies the data with different
                               parameter value, then pick the values that yield
                               the best accuracy.
                               Default: dict()
        """
        self.numClasses = numClasses
        self.mode = mode
        self.params = params or dict()

        # initialize correct number of classifiers
        self.classifiers = []
        if mode == "one-vs-one":
            # k classes: need k*(k-1)/2 classifiers
            for i in xrange(numClasses*(numClasses-1)/2):
                self.classifiers.append(cv3.SVM())
        elif mode == "one-vs-rest":
            # k classes: need k classifiers
            for i in xrange(numClasses):
                self.classifiers.append(cv3.SVM())
        else:
            print "Unknown mode ",mode

    def fit(self, X_train, y_train, params=None):
        """ fit model to data """
        if params is None:
            params = self.params

        if self.mode == "one-vs-one":
            svm_id=0
            for c1 in xrange(self.numClasses):
                for c2 in xrange(c1+1,self.numClasses):
                    y_train_c1 = np.where(y_train==c1)[0]
                    y_train_c2 = np.where(y_train==c2)[0]

                    data_id = np.sort(np.concatenate((y_train_c1,y_train_c2),axis=0))
                    X_train_id = X_train[data_id,:]
                    y_train_id = y_train[data_id]

                    # set class label to 1 where class==c1, else 0
                    y_train_bin = np.where(y_train_id==c1,1,0).reshape(-1,1)

                    self.classifiers[svm_id].train(X_train_id, y_train_bin, params=self.params)
                    svm_id += 1
        elif self.mode == "one-vs-rest":
            for c in xrange(self.numClasses):
                # train c-th SVM on class c vs. all other classes
                # set class label to 1 where class==c, else 0
                y_train_bin = np.where(y_train==c,1,0).reshape(-1,1)

                # train SVM
                self.classifiers[c].train(X_train, y_train_bin, params=self.params)

    def evaluate(self, X_test, y_test, visualize=False):
        """ evaluate model performance """
        # prepare Y_vote: for each sample, count how many times we voted
        # for each class
        Y_vote = np.zeros((len(y_test),self.numClasses))

        if self.mode == "one-vs-one":
            svm_id=0
            for c1 in xrange(self.numClasses):
                for c2 in xrange(c1+1,self.numClasses):
                    data_id = np.where((y_test==c1) + (y_test==c2))[0]
                    X_test_id = X_test[data_id,:]
                    y_test_id = y_test[data_id]

                    # set class label to 1 where class==c1, else 0
                    # y_test_bin = np.where(y_test_id==c1,1,0).reshape(-1,1)

                    # predict labels
                    y_hat = self.classifiers[svm_id].predict_all(X_test_id)

                    # we vote for c1 where y_hat is 1, and for c2 where y_hat is 0
                    # np.where serves as the inner index into the data_id array, which
                    # in turn serves as index into the results array
                    Y_vote[data_id[np.where(y_hat==1)[0]],c1] += 1
                    Y_vote[data_id[np.where(y_hat==0)[0]],c2] += 1
                    svm_id += 1
        elif self.mode == "one-vs-rest":
            for c in xrange(self.numClasses):
                # set class label to 1 where class==c, else 0
                # predict class labels
                # y_test_bin = np.where(y_test==c,1,0).reshape(-1,1)

                # predict labels
                y_hat = self.classifiers[c].predict_all(X_test)
                # print "y_hat",np.unique(y_hat)

                # we vote for c where y_hat is 1
                if np.any(y_hat):
                    Y_vote[np.where(y_hat==1)[0],c] += 1

            # with this voting scheme it's possible to end up with samples that
            # have no label at all...in this case, pick a class at random...
            no_label = np.where(np.sum(Y_vote,axis=1)==0)[0]
            Y_vote[no_label,np.random.randint(self.numClasses, size=len(no_label))] = 1


        accuracy = self.__accuracy(y_test, Y_vote)
        precision = self.__precision(y_test, Y_vote)
        recall = self.__recall(y_test, Y_vote)
        return (accuracy,precision,recall)

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