#!/usr/bin/env python
# coding: utf-8

# # Explainatory data analysis on fifa 2020 dataset

# In[1]:


# importing libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


# importing dataset
fifa=pd.read_csv("players_20.csv")


# In[3]:


fifa.head()


# In[4]:


# printing columns 
for col in fifa.columns:
    print(col)


# In[5]:


fifa.shape


# In[6]:


# no. of shells
18278*104


# In[7]:


#frequency of players belong to different country
fifa["nationality"].value_counts()


# In[8]:


#top 5
fifa["nationality"].value_counts()[:5]


# In[9]:


# bar plot
plt.figure(figsize=(10,10))
plt.bar(list(fifa["nationality"].value_counts()[:5].keys()),list(fifa["nationality"].value_counts()[:5]),color="g")


# In[10]:


# to see the player salary
player_salary=fifa[["short_name","wage_eur"]]


# In[11]:


player_salary.head()


# In[12]:


# top salary
player_salary=player_salary.sort_values(by=["wage_eur"],ascending=False)


# In[13]:


player_salary.head()


# In[14]:


# BAR PLOT OF TOP 5 highest salary
plt.figure(figsize=(10,10))
sns.barplot(x=list(player_salary["short_name"])[:5],y=list(player_salary["wage_eur"])[:5],data=player_salary)
plt.show()


# In[26]:


#AMALYSING THE COUNTRY GERMANY
germany=fifa[fifa["nationality"]=="Germany"]
germany.head(10)


# In[29]:


# top 5 players with highest height in germany
germany.sort_values(by="height_cm",ascending=False).head()


# In[31]:


# top 5 players with highest weight in germany
germany.sort_values(by="weight_kg",ascending=False).head()


# In[33]:


# top 5 players with highest salary in germany
germany.sort_values(by="wage_eur",ascending=False).head()


# In[38]:


# name + highest salary
germany[["short_name","wage_eur"]].sort_values(by="wage_eur",ascending=False).head()


# In[45]:


# top 5 players who had best shooting in fifa
fifa[["short_name","shooting"]].sort_values(by="shooting",ascending=False).head()


# In[47]:


# top 5 players with best shooting in fifa 2020
fifa[["short_name","defending","nationality"]].sort_values(by="defending",ascending=False).head()


# In[62]:


# analysing the club real madrid
real_madrid=fifa[fifa["club"]=="Real Madrid"]
real_madrid.head()


# In[64]:


# top 5 salary of players who belongs to the real madrid club
real_madrid[["short_name","wage_eur"]].sort_values(by="wage_eur",ascending=False).head()


# In[65]:


# top 5 besht shooting players who belongs to the real madrid club
real_madrid[["short_name","shooting"]].sort_values(by="shooting",ascending=False).head()


# In[68]:


# top 5 best defending players who belong to club real madrid
real_madrid[["short_name","defending"]].sort_values(by="defending",ascending=False).head()


# In[69]:


# counting nationality
real_madrid["nationality"].value_counts()


# In[ ]:




