import sys
import pandas as pd
import matplotlib
import numpy as np
import scipy as sp
import IPython
import sklearn 
import csvTranslator

from sklearn.model_selection import train_test_split

#gender: -1 = male, 0 = female, 1 = other
#age: 1-100
#criminal: 1 = criminal, 0 = not
#family: 1 = has, 0 = doesn't
#rich: 1 = rich, 0 = average, -1 = poor
#important: 1 = important job, 0 = unimportant
#species: 1 = human, -1 = cat, 1 = dog
#count = -1 = 2, 0 = 1, 1 = 3 !!!! potentially shit
#evil = 1 = evil, 0 = not
#story = text describing data
#result: 1 = person one dead, 0 = person two dead

data_set = csvTranslator.load_trolley_short()
print(data_set)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data_set['data'], data_set['target'], random_state=0)

# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors=3) 

# knn.fit(X_train, y_train)

# print("Test set score: {:.2f}". format(knn.score(X_test, y_test)))

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons

X_train, X_test, y_train, y_test = train_test_split(data_set.data, data_set.target, random_state=0)
forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(forest.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(forest.score(X_test, y_test)))