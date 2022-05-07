# -*- coding: utf-8 -*-
"""flight ticket price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F9rQX45iiolTWgz7UmGgNs9rBYZFtSjQ
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
data = pd.read_excel("/content/drive/MyDrive/Dataset.xlsx")

data

"""**PRE-PROCESSING**"""

data.info()

data.isnull().sum()

data.dropna(inplace = True)

data.isnull().sum()

"""DATA VISUALISATION"""

import seaborn as sns

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.countplot(data['Airline'])
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.countplot(data['Source'])
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.countplot(data['Destination'])
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.countplot(data['Additional_Info'])
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.countplot(data['Total_Stops'])
plt.show()

"""Comparing price with different attributes"""

sns.catplot(y = "Price", x = "Airline", data = data.sort_values("Price", ascending = False), kind="boxen", height = 8, aspect = 3)
plt.show()

sns.catplot(y = "Price", x = "Source", data = data.sort_values("Price", ascending = False), kind="boxen", height = 8, aspect = 3)
plt.show()

sns.catplot(y = "Price", x = "Destination", data = data.sort_values("Price", ascending = False), kind="boxen", height = 8, aspect = 3)
plt.show()

data[data.duplicated()].head()

data.drop_duplicates(keep='first',inplace=True)
data.head()

data.Total_Stops.unique()

data = data.replace({"non-stop":0,"1 stop":1,"2 stops":2,"3 stops":3,"4 stops":4})

data.Route.unique()

"""we see that number of stops and route are interrelated so we can drop one of them and it will be easy if we drop the route column."""

data["Additional_Info"].value_counts()

df = data.drop(columns =['Route'])

df['journey_day']=pd.to_datetime(df.Date_of_Journey, format='%d/%m/%Y').dt.day
df['journey_month']=pd.to_datetime(df.Date_of_Journey, format='%d/%m/%Y').dt.month

df

df.drop(['Date_of_Journey'],axis=1,inplace=True)

df['dep_hour']=pd.to_datetime(df.Dep_Time).dt.hour
df['dep_min']=pd.to_datetime(df.Dep_Time).dt.minute
df.drop(['Dep_Time'],axis=1,inplace=True)

df

df['arr_hour']=pd.to_datetime(df.Arrival_Time).dt.hour
df['arr_min']=pd.to_datetime(df.Arrival_Time).dt.minute
df.drop(['Arrival_Time'],axis=1,inplace=True)

df

data["Duration"].value_counts()

df['Duration'] = df['Duration'].str.replace("h", '*60').str.replace(' ','+').str.replace('m','*1').apply(eval)

df

df['Duration(min)']=df['Duration']

df.drop(['Duration'],axis=1,inplace=True)

df

data["Airline"].value_counts()

data["Source"].value_counts()

data["Destination"].value_counts()

df = df.replace({"Jet Airways":1,"IndiGo":2,"Air India":3,"Multiple carriers":4,"SpiceJet":5,"Vistara":6,"Air Asia":7,"GoAir":8,"Jet Airways Business":10,"Multiple carriers Premium economy":9,"Vistara Premium economy":11,"Trujet":12})

df

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df['Source']= label_encoder.fit_transform(df['Source']) 
df['Destination']= label_encoder.fit_transform(df['Destination']) 
df['Additional_Info']= label_encoder.fit_transform(df['Additional_Info'])

df

plt.figure(figsize=(4,4))
sns.distplot(df.journey_day)

plt.figure(figsize=(4,4))
sns.distplot(df.journey_month)

plt.figure(figsize=(4,4))
sns.distplot(df.dep_hour)

plt.figure(figsize=(4,4))
sns.distplot(df.dep_min)

plt.figure(figsize=(4,4))
sns.distplot(df.arr_hour)

plt.figure(figsize=(4,4))
sns.distplot(df.arr_min)

plt.figure(figsize=(4,4))
sns.distplot(df.Price)

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['Airline'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['Source'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['Destination'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['Total_Stops'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['Additional_Info'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['journey_day'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['journey_month'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['dep_hour'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['dep_min'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['arr_hour'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['arr_min'],y=df.Price)
plt.show()

plt.figure(figsize=(20,50))
plt.subplot(6,3,1)
sns.scatterplot(x=df['Duration(min)'],y=df.Price)
plt.show()





from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# col_names = ['Total_Stops', 'journey_day', 'journey_month','dep_hour','dep_min','arr_hour','arr_min','Duration(min)','Additional_Info']
# features = df[col_names]
# features = scaler.fit_transform(features.values)

Y = df.loc[:,'Price']

d_X = df.loc[:,['Airline','Source','Destination','Total_Stops','Additional_Info','journey_day','journey_month','dep_hour','dep_min','arr_hour','arr_min','Duration(min)']]

X = scaler.fit_transform(d_X)

X

Y

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3)

x_train

y_test

from sklearn.ensemble import RandomForestRegressor as rsr

model1 = rsr()
model1.fit(x_train,y_train)

y_pred1 = model1.predict(x_test)

from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error

print("r2_score:", r2_score(y_test,y_pred1))
print("mean_absolute_error:",mean_absolute_error(y_test,y_pred1) )
print("mean_squared_error:",mean_squared_error(y_test,y_pred1))

from sklearn.tree import DecisionTreeRegressor as dtr

model2 = dtr()
model2.fit(x_train,y_train)
y_pred2 = model2.predict(x_test)

print("r2_score:", r2_score(y_test,y_pred2))
print("mean_absolute_error:",mean_absolute_error(y_test,y_pred2) )
print("mean_squared_error:",mean_squared_error(y_test,y_pred2))

from sklearn.neighbors import KNeighborsRegressor as knr

model3 = knr()
model3.fit(x_train,y_train)
y_pred3 = model3.predict(x_test)

print("r2_score:", r2_score(y_test,y_pred3))
print("mean_absolute_error:",mean_absolute_error(y_test,y_pred3) )
print("mean_squared_error:",mean_squared_error(y_test,y_pred3))

from sklearn.ensemble import GradientBoostingRegressor as gdr

model4 = gdr()
model4.fit(x_train,y_train)
y_pred4 = model4.predict(x_test)

print("r2_score:", r2_score(y_test,y_pred4))
print("mean_absolute_error:",mean_absolute_error(y_test,y_pred4) )
print("mean_squared_error:",mean_squared_error(y_test,y_pred4))

"""**Hyper parameter tuning using randomizedSearchCV**"""

from sklearn.model_selection import RandomizedSearchCV as rcr

param1 = {'n_estimators':[10,30,50,70,90,100,120,140],'max_depth':[None,2,4,6,8,10],'max_samples':[20,50,100,120,150,200,250],'min_samples_split':[None,2,4,6,8,10]}

class1= rsr()

rfr1 = rcr(class1,param1,cv=5)

x_train

res1 = rfr1.fit(x_train,y_train)

res1.best_params_

params3 = {'max_depth': [None,1,2,3,4,5,6], 'min_samples_split':[2,4,6,8,10], 'min_samples_leaf':[1,2,3,4,5,6], 'max_leaf_nodes': [None,1,2,3,4,5]}

class2= dtr()

rfr2 = rcr(class2,params3,cv=5)

res2 = rfr2.fit(x_train,y_train)

res2.best_params_

params4 = {'n_estimators':[10,50,100,150,200],'alpha':[0.09,0.1,0.5,0.9],'learning_rate':[0.01,0.1,0.2],'max_depth':[2,3,4,5],'min_samples_leaf':[1,2,3,4,5],'min_samples_split':[2,3]}

from sklearn.model_selection import GridSearchCV as gcr

class3 = gdr()
rfr3 = rcr(class3,params4,cv=5)

res3 = rfr3.fit(x_train,y_train)
res3.best_params_

"""Fitting model using the new best parameters."""

model4_new = gdr(alpha=0.09,learning_rate=0.1,max_depth=5,min_samples_leaf=4,min_samples_split=3,n_estimators=200)

model4_new.fit(x_train,y_train)

pre = model4_new.predict(x_test)

print("r2_score:", r2_score(y_test,pre))
print("mean_absolute_error:",mean_absolute_error(y_test,pre) )
print("mean_squared_error:",mean_squared_error(y_test,pre))