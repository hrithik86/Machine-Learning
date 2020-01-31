#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from numpy.random import randn


# In[3]:


np.random.seed(101)


# In[4]:


df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[5]:


df


# In[6]:


df['W']


# In[7]:


type(df['W'])


# In[8]:


df['W']['B']


# In[9]:


df[['W','Z']]


# In[10]:


df['new']=df['W']+df['Y']


# In[11]:


df


# In[12]:


df.drop('new',axis=1)


# In[13]:


df


# In[14]:


df.drop('new',axis=1,inplace=True)


# In[15]:


df


# In[16]:


df.drop('E')


# In[17]:


# axis =0 for rows and axis =1 for columns


# In[19]:


df.shape


# In[21]:


df.loc['C']


# In[22]:


df.iloc[2]


# In[23]:


df.loc['B','Y']


# In[24]:


df.loc[['A','B'],['W','Y']]


# In[25]:


df>0


# In[26]:


booldf=df>0


# In[27]:


booldf


# In[28]:


df[booldf]


# In[29]:


df[df>0]


# In[30]:


df['W']>0


# In[33]:


res=df[df['W']>0]


# In[32]:


df[df['Z']<0]


# In[34]:


res


# In[35]:


res['X']


# In[38]:


df[df['W']>0][['Y','X']]


# In[39]:


#we cant use simple and operation because it works on 2 single boolean values
# in this case we get a series of boolean values on which the simple and operation cant work.
df[(df['W']>0) & (df['Y']>1)]


# In[40]:


df[(df['W']>0) | (df['Y']>1)]


# In[41]:


df


# In[42]:


df.reset_index()


# In[44]:


df.reset_index()['index']


# In[45]:


df


# In[46]:


newind='CA NY WY OR CO'.split()


# In[47]:


newind


# In[48]:


df['States']=newind


# In[49]:


df


# In[50]:


df.set_index('States')


# In[51]:


df


# In[ ]:




