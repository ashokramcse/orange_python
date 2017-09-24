# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:08:35 2017

@author: BALASUBRAMANIAM
"""


import pandas as pd
#cultivator does labelling. Three class labels 1,2 and 3
iris = pd.read_csv('Iris_5cols.csv', names = ["SepalLength ", "SepalWidth ", "PetalLength ", "PetalWidth ", "Class"])

#takes first 5 rows
print(iris.head())

print(iris.describe().transpose())


print(iris.shape)
#print(wine["Malic_Acid"])
'''
tempdata=[]
for macid in wine["Malic_Acid"]:
    macid=macid/4
    tempdata.append(macid)
  
wine["Malic_Acid"] = tempdata
    
print(wine["Malic_Acid"])
'''
from sklearn.model_selection import train_test_split
X = iris.drop('Class',axis=1)
#X = wine.drop('Malic_Acid',axis=1)
#X = wine.drop('Alchol',axis=1)
y = iris['Class']

#data=iris.iloc[0:3, 4:]
#print(data)
#deciding data by slice
#Purely integer-location based indexing 
'''
X_train=iris.iloc[0:50, 0:4]
print(X_train)
X_test=iris.iloc[51:100, 0:4]
print(X_test)
y_train=iris.iloc[0:50, 4:]
print(y_train)
y_test=iris.iloc[51:100, 4:]
'''
X_train, X_test, y_train, y_test = train_test_split(X, y)

#data normalization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
#fit the training data
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
#Multi layer perceptron created with 3 hidden layer and each hidden layer has
#13 neurons and 500 iterations
mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
#view the model generated
print(mlp.fit(X_train,y_train))
predictions = mlp.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
#confusion matrix gives result for each class 
#Diagonal elements shows the number of correct classifications
#off diagonal gives number of misclassified data
#F1 = 2 * (precision * recall) / (precision + recall)
#Recall is the proportion of cases correctly identified as belonging to class c among all cases that truly belong to class c.
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
print(len(mlp.coefs_))
print(len(mlp.coefs_[0]))
print(len(mlp.intercepts_[0]))
