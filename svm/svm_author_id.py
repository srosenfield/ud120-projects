#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#clf = SVC(kernel="linear")
clf = SVC(kernel="rbf", C=10000)

#code to limit the data by a factor of 100 in order to train it faster
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

t0 = time() #time the fit classifier
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s" #print the training time

t1 = time() #time the prediction
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s" #print the prediction time

accuracy = accuracy_score(labels_test, pred)
print(accuracy)

#What class does your SVM (0 or 1, corresponding to Sara and Chris respectively)
#predict for element 10 of the test set?

#prints out the corresponding name of the value
def who(number):
    if number == 1:
        return "Chris"
    else:
        return "Sara"

print "element 10 is predicted to be class = ", who(pred[10])
print "element 26 is predicted to be class = ", who(pred[26])
print "element 50 is predicted to be class = ", who(pred[50])

#There are over 1700 test events--how many are predicted to be
#in the Chris (1) class?

print "the number of events predicted to be from Chris = ", (pred == 1).sum()


#########################################################
