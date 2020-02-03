#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data={
    'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
    'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
    'Sales':[200,120,340,124,243,350]
}


# In[3]:


df=pd.DataFrame(data)


# In[4]:


df


# In[7]:


byComp=df.groupby('Company')


# In[9]:


byComp.mean()


# In[10]:


byComp.sum()


# In[11]:


byComp.std()


# In[13]:


byComp.sum().loc['FB']


# In[14]:


df.groupby('Company').sum().loc['FB']


# In[15]:


df.groupby('Company').max()


# In[18]:


df.groupby('Company').describe()


# In[19]:


df.groupby('Company').describe().transpose()


# In[20]:


df.groupby('Company').describe().transpose()['FB']


# In[ ]:




