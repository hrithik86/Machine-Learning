#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# Index Levels
outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_inside=pd.MultiIndex.from_tuples(hier_index)


# In[3]:


outside


# In[4]:


hier_index


# In[5]:


hier_inside


# In[14]:


from numpy.random import randn
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[15]:


df


# In[21]:


df.index.names


# In[22]:


df.index.names=['Groups']


# In[23]:


df


# In[ ]:





# In[ ]:




