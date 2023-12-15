import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import numpy 
#imports data and sepperates it into sepperate values
data = pd.read_csv("final-project/apartment_data.csv")
x = data["bedrooms"].values
y = data["price"].values
#reshape data to be in 2d arrays
x = x.reshape(-1, 1)
#print(x)
model = LinearRegression().fit(x, y)