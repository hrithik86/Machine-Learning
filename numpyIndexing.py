#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr=np.arange(0,11)


# In[3]:


arr


# In[4]:


arr[3]


# In[5]:


#slice notation
arr[1:5]


# In[6]:


arr[:6]


# In[9]:


arr[5:]


# In[10]:


arr[0:5]=100


# In[11]:


arr


# In[13]:


arr=np.arange(0,11)
#now the changes made in slice_of_arr is reflected back in arr and vice-versa
slice_of_arr=arr[0:6]
slice_of_arr


# In[19]:


slice_of_arr[:]=99
slice_of_arr


# In[16]:


arr


# In[21]:


arr[:]=100


# In[22]:


arr


# In[23]:


slice_of_arr


# In[24]:


arr=np.arange(0,11)
arr_copy=arr.copy()


# In[25]:


arr_copy


# In[28]:


arr_copy[:]=100
print(arr_copy)
print(arr)


# In[29]:


arr_2d=np.array([[5,10,15],[20,25,30],[35,40,45]])
arr_2d


# In[31]:


arr_2d[1][2]


# In[32]:


#same as arr_2d[1][2]
arr_2d[1,2]


# In[33]:


arr_2d[:2,1:]


# In[34]:


arr_2d[1]


# In[36]:


arr=np.arange(0,11)


# In[37]:


arr


# In[38]:


bool_arr=arr>5


# In[39]:


bool_arr


# In[46]:


a=np.arange(0,11)


# In[47]:


a[a>5]


# In[48]:


arr_2d=np.arange(50).reshape(5,10)
arr_2d


# In[50]:


arr_2d[1:3,3:5]

