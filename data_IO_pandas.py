#!/usr/bin/env python
# coding: utf-8

# # Data Input and Output
# csv
# ,excel
# ,html
# ,sql

# In[2]:


import pandas as pd


# In[4]:


pd.read_csv('example.csv')


# In[5]:


df=pd.read_csv('example.csv')


# In[6]:


df


# In[7]:


df.to_csv('My_output',index=False)


# In[8]:


pd.read_csv('My_output')


# In[13]:


pd.read_excel('Excel_Sample.xlsx',index_col=0)


# In[15]:


df.to_excel('Excel_Sample2.xlsx',sheet_name='Newsheet')


# In[16]:


data=pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')


# In[17]:


data


# In[18]:


type(data)


# In[20]:


data[0].head()


# In[21]:


from sqlalchemy import create_engine


# In[22]:


engine=create_engine('sqlite:///:memory:')


# In[23]:


df.to_sql('my_table',engine)


# In[24]:


sqldf=pd.read_sql('my_table',con=engine)


# In[25]:


sqldf


# In[ ]:




