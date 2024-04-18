#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 建立幾何運算模組 geometry.py

# 計算兩點距離
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# 計算一線段的斜率
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)


# In[7]:



distance(1,1,5,5)

