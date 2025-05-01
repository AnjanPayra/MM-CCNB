# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 20:51:45 2022

@author: Anjan Payra
"""

import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import pickle
import csv
from sklearn import svm
from sklearn import metrics

#Opening Message
print("Hello, you will find instructions for building your model in the README.md file.")

#User selects a .csv file from the data folder
fileIn = 'D:\\remma\\Ortho_Sim_loc\\YMIPS_centrality.csv'

data = pd.read_csv(fileIn)

namesInCsv = pd.read_csv(fileIn, nrows=0)
namesClassified = []

for name in namesInCsv:
	namesClassified.append(name)

#Empty numpy array to replace empty columns
emptyColumn = []
emptyArray = np.asarray(emptyColumn)

#Future Update: This section will be of variable length
le = preprocessing.LabelEncoder()
#Five Data Points:
if len(data[namesClassified[0]]) != 0:
	itemAt0 = le.fit_transform((data[namesClassified[0]]))
else:
	itemAt0 = emptyArray
if len(data[namesClassified[1]]) != 0:
	itemAt1 = le.fit_transform((data[namesClassified[1]]))
else:
	itemAt1 = emptyArray
if len(data[namesClassified[2]]) != 0:
	itemAt2 = le.fit_transform((data[namesClassified[2]]))
else:
	itemAt2 = emptyArray
if len(data[namesClassified[3]]) != 0:
	itemAt3 = le.fit_transform((data[namesClassified[3]]))
else:
	itemAt3 = emptyArray
if len(data[namesClassified[4]]) != 0:
	itemAt4 = le.fit_transform((data[namesClassified[4]]))
else:
	itemAt4 = emptyArray
if len(data[namesClassified[5]]) != 0:
	itemAt5 = le.fit_transform((data[namesClassified[5]]))
else:
	itemAt5 = emptyArray
#Mandatory Prediction Column 7:
if len(data[namesClassified[6]]) != 0:
	itemAt6 = le.fit_transform((data[namesClassified[6]]))

predict = itemAt6

x = list(zip(itemAt0, itemAt1, itemAt2, itemAt3, itemAt4, itemAt5))
y = list(itemAt6)

#Allows user to partition the test group
testSize = input("Enter your test size: ")
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=float(testSize))

#Allows the user to specify the number of neighbors in the model
#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(x_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))