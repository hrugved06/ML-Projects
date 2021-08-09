#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install lux-api


# In[2]:


get_ipython().system('pip install --upgrade lux-api')
get_ipython().system('jupyter nbextension install --py luxwidget')
get_ipython().system('jupyter nbextension enable --py luxwidget')


# In[3]:


import lux
import pandas as pd


# In[5]:


data = pd.read_csv('college.csv')


# In[6]:


data

