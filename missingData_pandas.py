#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


d={
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3]
}


# In[4]:


d


# In[5]:


df=pd.DataFrame(d)


# In[6]:


df


# In[9]:


df.dropna(axis=0)


# In[8]:


df.dropna(axis=1)


# In[10]:


df.dropna(thresh=2)


# In[11]:


df.fillna(value='Fill Value')


# In[12]:


df['A']


# In[13]:


df['A'].fillna(value=df['A'].mean())


# In[ ]:




