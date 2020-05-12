from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier
from sklearn.svm import SVC
import pandas as pd
import numpy as np

trainData = pd.read_csv('TrainingSet.csv')
trainData.head()
trainX = trainData.iloc[:,0:4].values
trainY = trainData.iloc[:,4].values

testData = pd.read_csv('TestSet1.csv')
testData.head()
testX = testData.iloc[:,0:4].values
testY = testData.iloc[:,4].values

classifier = OneVsOneClassifier(SVC()).fit(trainX, trainY)

prediction = classifier.predict(testX)

h1  = tuple(testData.iloc[:,0:1].values.reshape(1,30)[0])
h2  = tuple(testData.iloc[:,1:2].values.reshape(1,30)[0])
h3  = tuple(testData.iloc[:,2:3].values.reshape(1,30)[0])
h4  = tuple(testData.iloc[:,3:4].values.reshape(1,30)[0])

dataFrame = pd.DataFrame( {'leaf.length' : h1, 'leaf.width' : h2, 'flower.length' : h3, 'flower.length' : h4, 'plant' : tuple(prediction)})

dataFrame.to_csv('Predictions1V1.csv', index= False)