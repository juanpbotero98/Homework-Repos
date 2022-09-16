#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# A reinal neuron generates responses that are a weighted sum of intensities of light sensed at 6 regions in the retina
# 
# w_weight = [1,3,8,8,3,1]

# Part A: Is this system linear?
# 
# A system is considered linear if it meets the conditions of scalability and superposition
# 
# This system can be expressed as light intensity (l1) dotted with the weighted sum (w_weight) 
# 
# 

# Part B: What unit-length stimulus vector elicits the largest response in the nueron?
# 
# dot(l1,w_weight) = r, what is the largest r we can expect?
# 
# Geometrically, the largest response is generated when l1 and w_weight are parallel with each other. 
# This implies that their dot product = 1
# 

# In[15]:


w_weight = [1,3,8,8,3,1]
ln = np.array([1,3,8,8,3,1])
l_1 = np.linalg.norm(ln)
l_hat = ln/l_1

np.dot(w_weight,l_hat)


# The largest possible response we can obtain occurs when both vectors are in parallel. Given that intensity values cannot be negative, this implies that the direction of the intensity vector must point in the same direction as the weighted sum vector. By constraining the vector to unit length, we avoid the output going to infinity. As a result, the smallest unit length vector that maximizes the output response is the normalized intensity vector.

# In[16]:


print(l_hat)


# Part C: What is the smallest response in this nueron?
# 
# dot(l1,w_weight) = r, what is the smallest r we can expect?
# 
# Geometrically, the smallest response for r occurs when l1 and w_h are orthogonal to each other
# This implies that their dot product = 0. However, an input to the system must exist. Therefore, l1 must have a single component that is parallel with one of the axes with the length along all other axes being zero.
# 

# In[3]:


w_weight = np.array([1,3,8,8,3,1])

# The minimum light intensity we can have is when a single dimension = 1 and the others are zero
# The solution is the smallest dot product possible between light intensity and the weighted sum
l_1 = np.array([1,0,0,0,0,0])
l_2 = np.array([0,1,0,0,0,0])
l_3 = np.array([0,0,1,0,0,0])
l_4 = np.array([0,0,0,1,0,0])
l_5 = np.array([0,0,0,0,1,0])
l_6 = np.array([0,0,0,0,0,1])

r1 = np.dot(l_1,w_weight)
r2 = np.dot(l_2,w_weight)
r3 = np.dot(l_3,w_weight)
r4 = np.dot(l_4,w_weight)
r5 = np.dot(l_5,w_weight)
r6 = np.dot(l_6,w_weight)


# In[6]:


print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)


# It can be discerned that there are two possible solutions for this problem
# 
# l1 = [1, 0, 0, 0, 0, 0] and [0, 0, 0, 0, 0, 1]
# 
# When dotted with the weighted sum, the angle between both of them is closest to orthogonality without completely removing the input. 

# In[ ]:




