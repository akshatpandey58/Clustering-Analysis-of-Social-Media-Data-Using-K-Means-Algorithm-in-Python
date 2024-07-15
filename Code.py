#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df_exam=pd.read_csv(r'C:\Users\Acer\OneDrive\Documents\EnjoySport.csv')


# In[3]:


print(df_exam.head())


# In[4]:


print('Target category wise number of records')
df_exam.groupby('EnjoySport').size()


# In[5]:


input_feat=np.array(df_exam)[:,:-1]
print("The Attributes are: ")
input_feat


# In[6]:


output_feat=np.array(df_exam)[:,-1]
print("The Target is: ")
output_feat


# # Implementing Find-S Algorithm to find the specific hypothesis

# In[7]:


def find_S(c,t):
    for i, val in enumerate(t):
        if val == 1:
            specific_hypothesis=c[i].copy()
            break
        
    for i,val in enumerate(c):
        if t[i]==1:
            for x in range(len(specific_hypothesis)):
                specific_hypothesis[x] = '?' 
                if val[x]!=specific_hypothesis[x]:
                     return specific_hypothesis


# In[8]:


print("The Final Hypothesis is:",find_S(input_feat,output_feat))


# In[ ]:




