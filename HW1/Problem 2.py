#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# Problem 2: Given an arbirtrary unit vector u_hat and an arbitrary vector v, write expressions for the following
#         a) The component of v lying along the direction of u_hat
#         b) The component of v that is orthogonal to u_hat 
#         c) The distance from v to the component that lies along the direction of u_hat
#         
# 
# Part a) The component lying along the direction of u_hat could be thought of as Vx
# Part b) The component lying perpendicular to along the direction of u_hat could be thought of as Vy
# Part c) seems like it could be found through the distance formula

# Part A

# In[ ]:


projV = np.dot(v,u_hat)*u_hat


# Part B

# In[ ]:


projU = v - projV


# Part C

# In[ ]:


v2u = np.linalg.norm(projU)


# Now convince yourself that the code is working
#     Visually plot a random u vector and a random v vector along with the components found in part A and part B
#     Then test it in higher dimensions to verify the following
#         - Vector in part (a) lies along the same line as u_hat
#         - Vector in part (a) is orthogonal to the vector in (b)
#         - The sum of vectors in part (a) and part (b) is equal to v
#         - The sum of the squared lengths of vectors in part (a) and part (b) is equal to mag(v)**2

# In[2]:


n = 2
u = np.random.randn(n)
u_mag = np.linalg.norm(u)
u_hat = u/u_mag

v = np.random.randn(n)
projV = np.dot(v,u_hat)*u_hat
projU = v - projV


# In[3]:


projU


# In[5]:


c = np.array([0,0])

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
data = np.array([v,u_hat,projV,projU])
origin = np.array([c,c,c,projV])
plt.quiver(*origin.T,data[:,0],data[:,1], scale = 15)
plt.quiver(*origin2,vectors[:,0], vectors[:,1], angles='xy', scale_units='xy', scale=1)


# In[65]:


data[:,1]


# In[66]:


origin[:,1]


# In[ ]:




