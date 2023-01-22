#!/usr/bin/env python
# coding: utf-8

# # Weather Data Analysis Project Using Python
# 

# <img src= "860_main_weather_and_prediction.png" >

# # The Weather Dataset

# Here, The weather dataset is a time series dataset with per-hour information about the weather conditions at a particular locations. It records Temperature, Dew Point Temperature, Relative Humidity, Wind Speed, Visibility, Pressure and conditions. 

# # Problem Statements:-
# Q. 1)  Find all the unique 'Wind Speed' values in the data.
# Q. 2) Find the number of times when the 'Weather is exactly Clear'.
# Q. 3) Find the number of times when the 'Wind Speed was exactly 4 km/h'.
# Q. 4) Find out all the Null Values in the data.
# Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.
# Q. 6) What is the mean 'Visibility' ?
# Q. 7) What is the Standard Deviation of 'Pressure'  in this data?
# Q. 8) What is the Variance of 'Relative Humidity' in this data ?
# Q. 9) Find all instances when 'Snow' was recorded.
# Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.
# Q. 11) What is the Mean value of each column against each 'Weather Condition ?
# Q. 12) What is the Minimum & Maximum value of each column against each 'Weather Condition ?
# Q. 13) Show all the Records where Weather Condition is Fog.
# Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
# Q. 15) Find all instances when :
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# or
# B. 'Visibility is above 40'
# 

# ##  This data is available as a CSV file and this dataset is analyzed using the Pandas DataFrame.

# In[12]:


import pandas as pd


# In[13]:


data = pd.read_csv(r"F:\Projects\Weather Data Analysis Using Python\Weather Data.csv")


# In[4]:


data


# # Data Exploration
# Before analysing the data we have to explore the data using following commands.

# # (1) .head()
# It shows the first N rows in the data (by default, N=5)

# In[5]:


data.head()


# # (2) .shape()
# It shows the total no. of rows and columns of the dataframe

# In[7]:


data.shape


# # (3) .index
# This attributes provides the index of the dataframe.

# In[9]:


data.index


# # (4) .columns
# It shows the names of each column

# In[10]:


data.columns


# # (5) .dtypes
# It shows the data-type of each column

# In[11]:


data.dtypes


# # (6) .unique()
# In a column, it shows all the unique values.It can be applied on a single column only,not on the whole dataframe.

# In[13]:


data['Weather'].unique()


# # (7) .nunique()
# It shows the total no. of unique values in each column.it can be applied on a single column as well as on whole dataframe. 

# In[14]:


data.nunique()


# # (8) .count
# It shows the total no. of non null in each column. it can be applied on single column as well as on whole dataframe.

# In[15]:


data.count()


# # (9) .value_counts
# In a column,it shows all the unique values with their count.it can be applied on single column only.

# In[16]:


data['Weather'].value_counts()


# # (10) .info()
# Provides the basic information about the dataframe.

# In[21]:


data.info()


# # Q.1) Find all the unique 'Wind Speed' values in the data?

# In[23]:


data.head(4)


# In[25]:


data.nunique()


# In[26]:


data['Wind Speed_km/h'].nunique()


# In[27]:


data['Wind Speed_km/h'].unique() #Answer of the Question


# # Q.2) Find the number of times when the 'Weather is exactly Clear'?

# In[28]:


data.head(5)


# ## We can solve this problem using 3 commands.

# In[31]:


# A) value_counts()
data.Weather.value_counts()


# In[33]:


# B) Filtering
#data.head(2)
data[data.Weather == 'Clear']


# In[35]:


# C) groupby()
#data.head(2)
data.groupby('Weather').get_group('Clear')


# # Q.3) Find the number of times when the 'Wind Speed was exactly 4 km/h'?

# In[36]:


data.head(2)


# In[41]:


# By filtering Command
data[data['Wind Speed_km/h'] == 4]


# # Q.4) Find out all the Null Values in the data?

# In[5]:


data.isnull().sum()


# In[6]:


data.notnull().sum()


# # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[7]:


data.head(2)


# In[9]:


#data.rename(columns= {'Weather' : 'Weather Condition'})
# abovecommand will rename column for this condition only.for rename in actual data we have to rename it as follows.
data.rename(columns= {'Weather' : 'Weather Condition'}, inplace = True)


# In[10]:


data.head(2)


# # Q.6) What is the mean 'Visibility' ?

# In[11]:


data.head(2)


# In[12]:


data.Visibility_km.mean()


# # Q.7) What is the Standard Deviation of 'Pressure'  in this data?

# In[13]:


data.Press_kPa.std()


# # Q.8) What is the Variance of 'Relative Humidity' in this data ?

# In[15]:


data['Rel Hum_%'].var()
# we use the square bracket when there is a space between letters of column name.


# # Q.9) Find all instances when 'Snow' was recorded.

# In[17]:


# By value_counts()
#data.head(2)
data["Weather Condition"].value_counts()


# In[18]:


# by filtering
data[data['Weather Condition'] == 'Snow']


# In[19]:


# by str.contains
data[data['Weather Condition'].str.contains('Snow')]


# # Q.10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'?

# In[20]:


data.head(2)


# In[21]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# # Q.11) What is the Mean value of each column against each 'Weather Condition ?

# In[22]:


data.head(2)


# In[33]:


data.groupby('Weather Condition').mean()


# # Q.12) What is the Minimum & Maximum value of each column against each 'Weather Condition?

# In[25]:


data.head(2)


# In[26]:


data.groupby('Weather Condition').min()


# In[27]:


data.groupby('Weather Condition').max()


# # Q.13) Show all the Records where Weather Condition is Fog.

# In[28]:


data[data['Weather Condition'] == 'Fog']


# # Q.14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[29]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# # Q.15) Find all instances when :
# 
# A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
# 
# or
# 
# B. 'Visibility is above 40'
# 

# In[30]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]

