import numpy as np
import pandas as pd
import json
from sklearn import datasets
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
# db = json.loads(open('datasets/scm/2025.json', encoding='utf-8'))



boston = datasets.load_boston() ## 加载波士顿房价信息

boston_X = boston.data ## X坐标，房价相关属性：大小，位置等
boston_Y = boston.target  ## 房价

X_train, X_test, Y_train, Y_test = train_test_split(boston_X, boston_Y, test_size=0.3) ##将数据中的70%作为训练数据，30%作为测试数据

model = LinearRegression() ## 使用LinearRegression线性回归模型
model.fit(X_train, Y_train) ## 对模型进行训练
Y_pre = model.predict(X_test) ## 对30%的测试数据进行预测

# plt.scatter(X_test[:,0], Y_test) ## 在图上展示与第一个属性相关图表
# plt.scatter(X_test[:,0], Y_pre)
# plt.show()

# y = model.coef_ * X + model.intercept_
print(model.coef_) ## 得到对于每个属性的斜率
print(model.intercept_) ## 得到在Y坐标的截距
print(model.score(X_test, Y_test)) ## 对该模型中的30%预测结果与真实结果比较，对模型准确度打分