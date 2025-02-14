'''
Creates a Decision tree classification model
Can be found at https://spark.apache.org/docs/latest/ml-classification-regression.html#decision-tree-classifier
'''
from pyspark.ml.classification import DecisionTreeClassifier


import modelutils

import os

import pickle
train,test,Traindf, Testdf, data = modelutils.getModelData([0.7,0.3])

DecisionTree = DecisionTreeClassifier(labelCol="Label",
                    featuresCol="features")
DecisionTree_model = DecisionTree.fit(Traindf)
Decisioneval = modelutils.getEvaluationMetrics(DecisionTree_model, Testdf)

with open('DecisionTreeModel_pickle', 'wb') as f:
	picke.dump(DecisionTree_model, f)
