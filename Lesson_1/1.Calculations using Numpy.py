#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Задание 1
import numpy as np


# In[44]:


a = np.array([[1, 6], [2, 8], [3, 11], [3, 10], [1, 7]])
print(a)


# In[8]:


a.shape


# In[11]:


mean_a = a.mean(axis=0)


# In[45]:


print(mean_a)


# In[ ]:


### Задание 2


# In[15]:


a_centered = a - mean_a


# In[46]:


print(a_centered)


# In[ ]:


### Задание 3


# In[79]:


a_cent_1 = a_centered[0:, :1].reshape(5,)
a_cent_2 = a_centered[0:, 1:].reshape(5,)
a_centered_sp = a_cent_1 @ a_cent_2
print(a_centered_sp)


# In[80]:


print(np.dot(a_cent_1, a_cent_2))


# In[88]:


a_centered_shape = a_centered.shape
res = a_centered_sp / (a_centered_shape[0] - 1)
print(res)


# In[ ]:


### Задание 4


# In[89]:


print(np.cov(a.T))

