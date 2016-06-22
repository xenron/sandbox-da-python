import logging
logging.basicConfig()

from sknn.mlp import Classifier, Layer

import numpy as np
from sklearn import cross_validation
from sklearn import datasets

 
iris = datasets.load_iris()
# iris.data.shape, iris.target.shape
 
X_train, X_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)
 
nn = Classifier(
 layers=[
 Layer("Rectifier", units=100),
 Layer("Linear")],
 learning_rate=0.02,
 n_iter=10)
nn.fit(X_train, y_train)
 
y_pred = nn.predict(X_test)
 
score = nn.score(X_test, y_test)

# print("y_test", y_test)
# print("y_pred", y_pred)
print("score", score)
