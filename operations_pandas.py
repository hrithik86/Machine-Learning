#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.DataFrame({
    'col1':[1,2,3,4],
    'col2':[444,555,666,444],
    'col3':['abc','def','ghi','xyz']
})
df.head()


# In[3]:


df['col2'].unique()


# In[4]:


len(df['col2'].unique())


# In[5]:


df['col2'].nunique()


# In[6]:


df['col2'].value_counts()


# In[10]:


df[(df['col1']>2) & (df['col2']==444)]


# In[11]:


def times2(x):
    return x*2


# In[12]:


df['col1'].sum()


# In[13]:


df['col1'].apply(times2)


# In[14]:


df['col3'].apply(len)


# In[15]:


df['col2'].apply(lambda x:x*2)


# In[16]:


df


# In[17]:


df.drop('col1',axis=1)


# In[18]:


df


# In[19]:


df.columns


# In[20]:


df.index


# In[21]:


df.sort_values('col2')


# In[22]:


df.isnull()


# In[24]:


data={
    'A':['foo','foo','foo','bar','bar','bar'],
    'B':['one','one','two','two','one','one'],
    'C':['x','y','x','y','x','y'],
    'D':[1,3,2,5,4,1]
}
df=pd.DataFrame(data)


# In[25]:


df


# In[26]:


df.pivot_table(values='D',index=['A','B'],columns=['C'])


# In[ ]:




