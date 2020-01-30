#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[7]:


labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={
    'a':10,
    'b':20,
    'c':30
}


# In[10]:


pd.Series(data = my_data)


# In[11]:


pd.Series(data=my_data,index=labels)


# In[12]:


pd.Series(my_data,labels)


# In[15]:


pd.Series(arr)


# In[16]:


pd.Series(arr,labels)


# In[17]:


pd.Series(d)


# In[18]:


d


# In[19]:


pd.Series(data=labels)


# In[27]:


ser1=pd.Series([1,2,3,4],['US','Ger','USSR','Japan'])


# In[28]:


ser1


# In[29]:


ser2=pd.Series([1,2,5,4],['US','Ger','Italy','Japan'])


# In[30]:


ser2


# In[31]:


ser1['US']


# In[32]:


ser3=pd.Series(data=labels)


# In[33]:


ser3


# In[34]:


ser3[0]


# In[35]:


ser1+ser2


# In[ ]:




