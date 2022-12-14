# -*- coding: utf-8 -*-
"""Pred.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IeB6t55CLQKSZJ8MPkr_G_kHQ0c7T42g
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy  import linalg
from sklearn import metrics
from sklearn import linear_model
from sklearn import preprocessing
import seaborn as sns

from sklearn.datasets import fetch_openml
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF,Matern,DotProduct,WhiteKernel, RationalQuadratic,ExpSineSquared

import sys
import sklearn
print(sys.version)
!python --version
print("numpy: ",np.__version__)
print("sklearn", sklearn.__version__)

df = pd.read_csv("co2.csv")

df.head(100)

X = np.array(df['Decimal']).reshape(-1,1)
Y = np.array(df['Average'])

print(X.shape,Y.shape)

k1=50.0*RBF(length_scale=50.0)
k2= 2.0*2*RBF(length_scale=100.0) *\
        ExpSineSquared(length_scale=1.0,periodicity_bounds='fixed')
k3 = 0.5**2 * RationalQuadratic(length_scale=1.0,alpha =1.0)
k4 = 0.1**2*RBF(length_scale=0.1)+\
        WhiteKernel(noise_level=0.1**2,noise_level_bounds=(1e-5,np.inf))

kernel=k1+k2+k3+k4

gp = GaussianProcessRegressor(kernel=kernel, alpha=0, normalize_y=True)
gp.fit(X,Y)


print("\nLeraned Kernel:",gp.kernel)
print("log_marginal_likelihood: %.3f" % gp.log_marginal_likelihood(gp.kernel_.theta))

X_=np.linspace(X.min(),X.max()+30,1000)[:,np.newaxis]
print(X_.shape,type(X_))

Y_pred,Y_std =gp.predict(X_,return_std=True)

#plot
fig =plt.figure(figsize=(15,5))
plt.scatter(X,Y,c='K',alpha=0.50)
plt.plot(X_,Y_pred)
plt.fill_between(X_[:,0],Y_pred-Y_std,Y_pred+Y_std,alpha=0.5,color='aliceblue')
plt.xlim(X_.min(),X_.max())
plt.xlabel("year")
plt.ylabel("ppm")
plt.title("Carbon Dioxide")
plt.show()

#plot
fig =plt.figure(figsize=(15,5))
plt.scatter(X,Y,c='K',alpha=0.50)
plt.plot(X_,Y_pred)
plt.fill_between(X_[:,0],Y_pred-Y_std,Y_pred+Y_std,alpha=0.5,color='aliceblue')
plt.xlim(2015,2045)
plt.xlabel("year")
plt.ylabel("ppm")
plt.title("Carbon Dioxide")
plt.show()