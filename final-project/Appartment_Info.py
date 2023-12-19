#Made by Lillie and Ari
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
#imports data and sepperates it into sepperate values
data = pd.read_csv("final-project/apartment_data.csv")
y = data["square_feet"].values
x = data["price"].values
#get data for bar graph
y2 = data["latitude"].values
x2 = data["price"].values
#y2 = data["state"].values
#reshape data to be in 2d arrays
x = x.reshape(-1, 1)
#print(x)
model = LinearRegression().fit(x, y)
#find the Co, bias, & rsquared
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)
plt.scatter(x,y)
 #plt.bar(x2, y2)
plt.xlabel("Price")
plt.ylabel("square_feet")
plt.title("Apt Sq ft to Price Ratio")
plt.plot(x, coef*x + intercept, c="purple", label = "line of best fit")
plt.show()

#TRAINING DATA
xtrain, xtest, ytrain, ytest = train_test_split(x, y ,test_size = .2)
xtrain = xtrain.reshape(-1,1)
#prediction
predict = model.predict(xtest)
predict = np.around(predict, 2)
# test the model
for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
#Print out all finished data
print("the accuracy of the line is :", round(r_squared, 4))
print("x value:", float(x_coord), "Predicted Y Value: ", predicted_y, "Actual Y Value: ", actual)
'''
num = [30000]
for i in y2:
    if i > num[0]:
        #num.pop()
        num.append(i)
        '''