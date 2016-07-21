# chapter6.py
import cv2 as cv3
import numpy as np

import matplotlib.pyplot as plt
from datasets import gtsrb
from classifiers import MultiClassSVM

def main():
    strategies = ['one-vs-rest','one-vs-one']
    features = ['gray','rgb','hsv','surf','hog']
    accuracy = np.zeros((2,len(features)))
    precision = np.zeros((2,len(features)))
    recall = np.zeros((2,len(features)))

    for f in xrange(len(features)):
        print "feature",features[f]
        (X_train,y_train), (X_test,y_test) = gtsrb.load_data("datasets/gtsrb_training",
            feature=features[f], test_split=0.2, seed=42)

        # convert to numpy
        X_train = np.squeeze(np.array(X_train)).astype(np.float32)
        y_train = np.array(y_train)
        X_test = np.squeeze(np.array(X_test)).astype(np.float32)
        y_test = np.array(y_test)

        # find all class labels
        labels = np.unique(np.hstack((y_train,y_test)))

        for s in xrange(len(strategies)):
            print "strategy",strategies[s]
            # set up SVMs
            MCS = MultiClassSVM(len(labels),strategies[s])

            # training phase
            MCS.fit(X_train, y_train)

            # test phase
            (acc,prec,rec) = MCS.evaluate(X_test, y_test)
            accuracy[s,f] = acc
            precision[s,f] = np.mean(prec)
            recall[s,f] = np.mean(rec)

    # plot results as stacked bar plot
    f,ax = plt.subplots(2)
    for s in xrange(len(strategies)):
        x = np.arange(len(features))
        ax[s].bar(x-0.2, accuracy[s,:], width=0.2, color='b', align='center')
        ax[s].bar(x, precision[s,:], width=0.2, color='r', align='center')
        ax[s].bar(x+0.2, recall[s,:], width=0.2, color='g', align='center')
        minY = np.min([np.min(accuracy[s,:]),np.min(precision[s,:]),np.min(recall[s,:])])
        ax[s].axis([-0.5, len(features)+0.5, minY, 1.5])
        ax[s].legend(('Accuracy','Precision','Recall'), loc=2, ncol=3, mode="expand")
        ax[s].set_xticks(np.arange(len(features)))
        ax[s].set_xticklabels(features)
        ax[s].set_title(strategies[s])

    plt.show()

if __name__ == '__main__':
    main()