import numpy as np
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

x=2*np.random.randn(100,1)
print(x.shape)
print(x)
y = 3 * x + np.random.randn(100, 1)
print("y",y)
'''print(x)
print(y)'''
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)#splitting our data
#here we need to create our model
model=LinearRegression()
#Train the model
model.fit(xtrain,ytrain)
#make predictions
ypred=model.predict(xtest)
#Evaluating our model
mse=mean_squared_error(xtest,ypred)
print(mse)
