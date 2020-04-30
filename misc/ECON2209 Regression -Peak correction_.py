#!/usr/bin/env python
# coding: utf-8

# # **Questions being answered in this notebook:**
# I. Construct an Excel spreadsheet with historical data for the 10 year period - from 1 January 2010 to 31 December 2019 in respect of the jurisdiction of New South Wales:
# 1. Daily energy (MWh);
# 2. Daily peak demand (MW);
# 3. Daily average spot price
# 4. Daily maximum and minimum temperatures for each weather station
# 5. Daily 9 am and 3pm relative humidity for each nominated weather stations
#
# II. Undertake a temperature correction analysis for summer peak demand in each year (1 Nov to 31 March excluding week-end days and public holidays) on the basis of a 10 percent probability of exceedence maximum temperature and long term weighted average relative humidity.

# In[52]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from scipy import stats
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[53]:


dataset = pd.read_csv('weather_data.csv')


# In[54]:


dataset.head()


# In[55]:


#this will tell us how many rows, how many columns
dataset.shape


# In[56]:


#descriptive stats of data
dataset.describe(include='all')


# In[ ]:





# In[57]:


#checks if any columns contains NaN values
dataset.isnull().any()


# In[58]:


#if any of the above return True, use below code (commented out)
#dataset = dataset.fillna(method='ffill')


# In[59]:


#this the one
Z = dataset[['Date']]
X = dataset[[ 'Daily av max temp', 'Daily av humidity']]
y = dataset['Peak demand (MW)'].values


# In[60]:


X


# In[10]:


plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['Daily av max temp'])


# In[11]:


plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(dataset['Daily av humidity'])


# In[12]:


#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[13]:


#edit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)


# In[14]:


# copy of above to edit if need be
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[15]:


regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[16]:


#As said earlier, in the case of multivariable linear regression,
#the regression model has to find the most optimal coefficients for all
#the attributes. To see what coefficients our regression model has chosen,
#execute the following script:


# In[17]:


coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=
                        ['Coefficient'])
coeff_df


# In[18]:


y_pred = regressor.predict(X_test)


# In[19]:


df = pd.DataFrame({'Actual': y_test, 'Corrected': y_pred})


# In[20]:


df1 = df.head(25)


# In[21]:


df1.head()


# In[22]:


df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# In[23]:


#df.to_csv(index=False)


# In[24]:


X_test


# In[25]:


humid = X_test.drop(['Daily av max temp'], axis=1)


# In[26]:


humid.head()


# In[27]:


temp = X_test.drop(['Daily av humidity'], axis=1)


# In[28]:


temp.head()


# In[29]:


y_test


# In[30]:


numpy_data = np.array(y_test)
y_test = pd.DataFrame(data=numpy_data)


# In[31]:


y_test = y_test.transpose()


# In[32]:


y_test


# In[33]:


y_test = y_test.transpose()


# In[35]:


y_test


# In[36]:


y_pred


# In[37]:


numpy_data = np.array(y_pred)
y_pred = pd.DataFrame(data=numpy_data)


# In[38]:


y_pred = y_pred.transpose()


# In[39]:


y_pred


# In[40]:


y_pred = y_pred.transpose()


# In[41]:


y_pred


# In[42]:


#just useful thing that turns an array into a matrix
 #y_test = np.asmatrix(y_test)


# In[45]:


plt.scatter(humid, y_test,  color='gray')
plt.show()


# In[46]:


plt.scatter(temp, y_test,  color='gray')
plt.plot(temp, y_pred, color='red', linewidth=2)
plt.show()


# In[47]:


plt.figure(2)
plt.scatter(y_test, X_test.iloc[:,0].values)

plt.figure(3)
plt.scatter(y_test, X_test.iloc[:,1].values)


# In[48]:


#df.to_csv('data2.csv', index=True)


# In[49]:


print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# In[50]:


'''plt.scatter(temp, y_test, color='red')
plt.title('humd v peak demand', fontsize=14)
plt.xlabel('temp', fontsize=14)
plt.ylabel('y_test', fontsize=14)
plt.grid(True)
plt.show()'''


# In[ ]:
