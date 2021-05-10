#!/usr/bin/env python
# coding: utf-8

# # TASK 4- Exploratory Data Analysis - Terrorism
# 
# # NAME-RISHAV KUMAR SINGH
#    
# PROBLEM STATEMENT:- Perform ‘Exploratory Data Analysis’ on dataset ‘Global Terrorism’.
# 
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[4]:


df=pd.read_csv('globalterrorismdb_0718dist.csv',encoding='latin1') #Reading the dataset
df.describe() #To start with the EDA process and getting familiar with our dataset


# In[3]:


df.head()  #First five observations of our dataset


# In[5]:


df.shape #To know the dimension of our dataset 

The DataFrame has 135 Columns and are named in a very difficult to understand manner
# In[6]:


df.columns #To know the various attributes in our dataset


# In[7]:


df.rename(columns=({'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','provstate':'state','region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed','nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type','weaptype1_txt':'Weapon_type','motive':'Motive'}),inplace=True)
#Proper renaming for easier reuse


# In[8]:


# Only choosing importnant columns
df=df[['Year','Month','Day','Country','state','Region','city','latitude','longitude','AttackType','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]
df.head()


# In[9]:


df.isnull().sum() #To display the null values for each attribute in our dataset


# In[10]:


df.info() #To be known about what type of data in each column we have


# # Visualizations:-

# In[11]:


x_year = df['Year'].unique()
y_count_years = df['Year'].value_counts().sort_index()
plt.figure(figsize = (16,10))
sns.barplot(x = x_year,
           y = y_count_years)
plt.xticks(rotation = 45)
plt.xlabel('Attack Year')
plt.ylabel('Number of Attacks each year')
plt.title('Attack Vs Years')
plt.show()              # To display increasing number of terror activities per year


# In[12]:


plt.figure(figsize=(10,6))
sns.barplot(df['Country'].value_counts()[:15].index,df['Country'].value_counts()[:15].values,palette='Blues_d')
plt.title('Top Countries Affected')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation= 90)
plt.show()                 #Bar Plot - Top 15 countries that are affected


# In[13]:


killData = df.loc[:,'Killed']
print('Number of people killed by terror attack:', int(sum(killData.dropna()))) #Number of people killed in a terror attack


# In[14]:


countryData = df.loc[:,'Country']
countryKillData = pd.concat([countryData, killData], axis=1) #Country wise Death


# In[15]:


countryKillFormatData = countryKillData.pivot_table(columns='Country', values='Killed', aggfunc='sum')
countryKillFormatData #Country wise Death


# In[16]:


plt.figure(figsize=(15, 9))
sns.barplot(
    df["Weapon_type"].value_counts()[:10].index,
    df["Weapon_type"].value_counts()[:10].values,
    palette=("rocket"),
)
plt.title("Weapon types used in attacks")
plt.xlabel("Weapon of choice")
plt.ylabel("Counts")
plt.xticks(rotation=35)
plt.show();       #Bar Plot - Weapon types used in attacks


# # Conclusion & Analyzed Information
# # what i found:-
1- From first visualization we can say that, 2014 is the year which has most number of attacks.
2- From second visualization we can see that, IRAQ is the most affected among the top 15 country. 
3- From third visualization we can see that, total number of people died in the terror attack is 411868.
4- From fourth visualization it could be said that, Afghanistan is the country which has most number of deaths.
5- From fifth visualization it could be said that, 'Explosives' were the most popular weapon among the terrorist groups for carrying out the attacks.
# # Finally, I completed the EDA (Exploratory Data Analysis) on the Global Terrorism Dataset provided and the above mentioned points are my key findings for this particular dataset.
