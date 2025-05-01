# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:20:36 2022

@author: Anjan Payra
"""
import pandas as pd
from sklearn import preprocessing
#from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


class Ensemble:
    def __init__(self):
        self.x_train = None
        self.x_test = None
        self.y_train = None
        self.y_test = None

    def load_data(self):
        fileIn = 'D:\\remma\\New_ECC\\ML\\KNN.csv'
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
       
        x = list(zip( itemAt1, itemAt2, itemAt3))
        y = list(itemAt4)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.5, random_state=23)

    @staticmethod
    def __Classifiers__(name=None):
        # See for reproducibility
        random_state = 23

        if name == 'decision_tree':
            return DecisionTreeClassifier(random_state=random_state)
        if name == 'kneighbors':
            return KNeighborsClassifier()
        if name == 'logistic_regression':
            return LogisticRegression(random_state=random_state, solver='liblinear')

    def __DecisionTreeClassifier__(self):

        # Decision Tree Classifier
        decision_tree = Ensemble.__Classifiers__(name='decision_tree')

        # Train Decision Tree
        decision_tree.fit(self.x_train, self.y_train)

    def __KNearestNeighborsClassifier__(self):

        # K-Nearest Neighbors Classifier
        knn = Ensemble.__Classifiers__(name='kneighbors')

        # Train K-Nearest Neighbos
        knn.fit(self.x_train, self.y_train)

    def __LogisticRegression__(self):

        # Decision Tree Classifier
        logistic_regression = Ensemble.__Classifiers__(name='logistic_regression')

        # Init Grid Search
        logistic_regression.fit(self.x_train, self.y_train)

    def __VotingClassifier__(self):

        # Instantiate classifiers
        decision_tree = Ensemble.__Classifiers__(name='decision_tree')
        knn = Ensemble.__Classifiers__(name='kneighbors')
        logistic_regression = Ensemble.__Classifiers__(name='logistic_regression')

        # Voting Classifier initialization
        vc = VotingClassifier(estimators=[('decision_tree', decision_tree),
                                          ('knn', knn), ('logistic_regression',
                                                         logistic_regression)], voting='soft')

        # Fitting the vc model
        vc.fit(self.x_train, self.y_train)

        # Getting train and test accuracies from meta_model
        y_pred_train = vc.predict(self.x_train)
        y_pred = vc.predict(self.x_test)
        

        print(f"Train accuracy: {accuracy_score(self.y_train, y_pred_train)}")
        print(f"Test accuracy: {accuracy_score(self.y_test, y_pred)}")
        print(f"Test error: {mean_squared_error(self.y_test, y_pred)}")


if __name__ == "__main__":
    ensemble = Ensemble()
    ensemble.load_data()
    ensemble.__VotingClassifier__()