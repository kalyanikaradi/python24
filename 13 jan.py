#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


arr1=np.ones((10,10))


# In[4]:


arr1


# In[6]:


arr1.shape


# In[11]:


arr2d=np.ones((10,10))


# In[12]:


arr2d


# In[14]:


no_of_rows=arr2d.shape[0]
j=0
for i in range (no_of_rows):
    arr2d[i]=np.arange(j+1,j+11)
    j+=10
arr2d


# In[15]:


arr2d[[6,4,3]]


# In[16]:


arr2d[:,[2,3,4]]


# In[17]:


arr2d>50


# In[18]:


arr2d[np.where(arr2d<20)]


# In[19]:


arr2d[np.where(arr2d[0,:]%2==0)]


# In[ ]:




