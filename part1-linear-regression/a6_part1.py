import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values


# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)
model = LinearRegression().fit(x, y)
# Create the model
plt.figure(figsize=(6,4))
# Find the coefficient, bias, and r squared values. 
coef = round(float(model.coef_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)
print(intercept)
# Each should be a float and rounded to two decimal places. 
plt.scatter(x, y)
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Age vs Blood Pressure")
# Print out the linear equation and r squared value
print("the Linear Regression equation is " + str(2))
print("the R squared value is " + str(r_squared))
# Predict the the blood pressure of someone who is 43 years old.
x_predict = 43
prediction = model.predict([[x_predict]])
# Print out the prediction
print("My prediction is " + str(prediction))
plt.plot(x, coef*x + intercept, c="r", label = "line of best fit")
# Create the model in matplotlib and include the line of best fit
plt.show()

