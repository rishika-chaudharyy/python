import numpy as np
from matplotlib import pylplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

#generate 50 data points in quadrant 1 randomly , Also generate their mirror points in quadrant 3

ds1=np.random.randint(low=1,high=10,size=(50,2))
ds2=ds1

#concatenate
X=np.concatenate((ds1,ds2),axis=0)

#generate class labels
y=np.ones(shape=100)
y[:50]=0

#train test split
X_train , X_test, y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y)

#scatter plot
plt.scatter(x=X_train[:10],y=X_train[:,1],c=y_train)
plt.show()

n_samples=X_train.shape[0]
n_features=X_train.shape[1]


#intial weights and bias are random

w=np.random.uniform(0,1,size=n_features)
b=np.random.uniform(0,1,1)

#Scan number and epochs
n_epoch=int(input("Enter number of epochs"))



