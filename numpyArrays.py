#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list=[1,2,3]


# In[2]:


my_list


# In[3]:


import numpy as np


# In[6]:


arr=np.array(my_list)


# In[7]:


arr


# In[8]:


my_mat=[[1,2,3],[4,5,6],[7,8,9]]
np.array(my_mat)


# In[13]:


np.arange(0,10,2)


# In[15]:


np.zeros(3)


# In[18]:


np.zeros((3,5))


# In[19]:


np.ones(4)


# In[20]:


np.ones((4,2))


# In[22]:


#linspace(start,end,x)
"""it gives x number of equally spaced numbers between start and end(both inclusive)"""
np.linspace(0,5,10)


# In[23]:


#identity matrix
np.eye(4)


# In[24]:


np.random.rand(5)


# In[25]:


np.random.rand(5,5)


# In[26]:


np.random.randn(2)


# In[27]:


np.random.randn(4,4)


# In[30]:


#randint(start,end,x)
#generates x random integers between start to end(start inclusive & end exclusive)
np.random.randint(1,100,10)


# In[32]:


arr=np.arange(25)
arr


# In[33]:


rearr=np.random.randint(0,50,10)
rearr


# In[34]:


arr.reshape(5,5)


# In[37]:


rearr.max()


# In[38]:


rearr.min()


# In[39]:


rearr.argmax()


# In[40]:


rearr.argmin()


# In[44]:


arr=arr.reshape(5,5)


# In[45]:


arr


# In[46]:


arr.shape


# In[48]:


arr.dtype


# In[49]:


from numpy.random import randint


# In[50]:


randint(2,10)

