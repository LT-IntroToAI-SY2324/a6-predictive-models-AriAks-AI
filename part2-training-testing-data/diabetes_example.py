import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#load the datasets
x, y = datasets.load_diabetes(return_X_y=True)

x = x[:, np.newaxis, 2]
#print(x)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

model = linear_model.LinearRegression().fit(xtrain, ytrain)

coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)

prediction = model.predict(xtest)

print("Coefficient: ", coef)
print("Mean squared Error: ", mean_squared_error(ytest, prediction))

lst = []
#Plot the non-linear line
#creates a list with all x values
'''for i in x:
    lst.append(i)
print(lst)
print(lst.sort())'''
#plot the points
plt.xticks()
plt.yticks()
plt.legend()
plt.scatter(xtest, ytest, c="black")
plt.title("Diabetes Scatter Plot With linear regression line")
plt.plot(xtest, prediction, c="blue", linewidth=1)
#adds in the training data
plt.scatter(xtrain, ytrain, c="green")
plt.show()