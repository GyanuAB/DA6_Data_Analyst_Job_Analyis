#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


data = pd.read_csv("job_analysis.csv")


# In[3]:


data


# In[4]:


data.head(50).T


# In[5]:


data.drop(['Unnamed: 0'], axis=1,inplace=True)


# In[11]:


data['Competitors'].value_counts()


# In[12]:


data['Easy Apply'].value_counts()


# In[13]:


data['Rating'].value_counts()[:5]


# In[14]:


data=data.replace(-1,np.nan)
data=data.replace(-1.0,np.nan)
data=data.replace('-1',np.nan)


# In[25]:


plt.rcParams["figure.figsize"] = (12,9)
#plt.style.use("classic")
color = plt.cm.PuRd(np.linspace(0,1,20))
data["Company Name"].value_counts().sort_values(ascending=False).head(20).plot.bar()
plt.title("Top 20 Company with Highest number of Jobs ",fontsize=20)
plt.xlabel("Company Name",fontsize=15)
plt.ylabel("Count",fontsize=15)
plt.show()


# In[32]:


#   Top 20 Company with highest number of Jobs


# In[33]:


com =data['Company Name'].value_counts()
company = pd.DataFrame({'Company': com.index,'Number of Jobs':com.values})
company.head(60)


# In[34]:


#  Number of Jobs according to Different Company


# In[41]:


data["Job Title"].value_counts().sort_values(ascending=False).head(20).plot.bar()
plt.title("Top 20 Jobs of Data Analyst ",fontsize=20)
plt.xlabel("Job Title",fontsize=15)
plt.ylabel("Count",fontsize=15)


# In[46]:


#    Popular Jobs of Data Analyst


# In[47]:


data["Location"].value_counts().sort_values(ascending=False).head(20).plot.bar()
plt.title("Top 20 locations for Data Analysts Job",fontsize=20)
plt.xlabel("Locations",fontsize=15)
plt.ylabel("Count",fontsize=15)


# In[48]:


#     Top 20 locations for Data Analysts Jobs


# In[49]:


data["Headquarters"].value_counts().sort_values(ascending=False).head(20).plot.bar()
plt.title("Top 20 Head Quarters of Data Analysts Job Holder Company",fontsize=20)
plt.xlabel("Head Quarters",fontsize=15)
plt.ylabel("Count",fontsize=15)


# In[50]:


#   Top 20 Head Quarters of Data Analyst Job Holder Company


# In[51]:


data["Founded"].value_counts().sort_values(ascending=False).head(20).plot.bar()
plt.title("Number of Company's Foundation in a Year",fontsize=20)
plt.xlabel("Company's Foundation Year",fontsize=15)
plt.ylabel("Count",fontsize=15)


# In[52]:


#   Highest number of Company Founded in a Year


# In[53]:


data["Type of ownership"].value_counts().sort_values(ascending=False).head(20).plot.bar()
plt.title("Type of ownership",fontsize=20)
plt.xlabel("Ownership",fontsize=15)
plt.ylabel("Count",fontsize=15)


# In[54]:


#   Above graphs shows the types of Ownership. A higher number of Company's are Private almost 1300 & just 500 company's are Public


# In[55]:


data["Sector"].value_counts().sort_values(ascending=False).head(20).plot.bar()
plt.title("Different types of Sectors for Data Analyst Jobs",fontsize=20)
plt.xlabel("Sectors",fontsize=15)
plt.ylabel("Count",fontsize=15)


# In[56]:


#   Most of the Data Analyst jobs are for the sector of Information Technology


# In[59]:


rating = data.groupby(['Company Name'])[['Company Name','Rating']]
rating.head().nlargest(10,'Rating').style.background_gradient(cmap='Reds')


# In[60]:


#  Above are Company with Highest Number of Rating


# In[62]:


rating.head().nlargest(30,'Rating').plot.bar(x='Company Name',y='Rating')
plt.title("Top 30 Company with highest number of Rating",fontsize=20)
plt.xlabel("Company Name",fontsize=15)
plt.ylabel("Rating",fontsize=15)


# In[63]:


data['Rating'] = data['Rating'].replace(-1,np.NaN)
data['Rating'].value_counts().plot.bar(x='Rating',y='No. of Companies',)
plt.title("Number of Companies with specific Rating",fontsize=20)
plt.xlabel("Rating",fontsize=15)
plt.ylabel("No. of Company",fontsize=15)
plt.show()


# In[ ]:


#   So, this is all about analysis.

