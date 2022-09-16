#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import numpy.linalg as la


# Question #1
# 
# For the following systems, determine if each system could be a linear system. If so, provide an example of a matrix that is consistent with the observed input/output pairs and state why if it is unique. If not, explain explain why such a matrix does not exist. 
# 
# Important note: A system is defined as LINEAR if it obeys scalability and superposition. 
#         i.e. af(x) = f(ax) & f(x) + f(y) = f(x + y)
# 
# System 1: [1] --> [4,6]
#           [2.5] --> [10,14]
# 

# In[10]:


x = np.array([[1],[2.5]]) # Input is being scaled by 2.5, IF this system is linear, the output should also scale by 2.5
h = np.array([[4, 6],[10,14]])

output = print(h[0,:]*2.5)

# This output gives [10,15] when scaled by 2.5. As a result, since this system does not follow scalability, this system
# is NOT a linear system.


# In[8]:


h[1,:]


# For the first pair of system 1, it can be seen that multiplying the input by a matrix [4 6] yields an expected output. However, multiplying that same matrix by the second pair yields a result that is different from the expected output. As such, this system does not follow scalability. Since it does not obey scalability  
# 
# System 1 is NOT a linear system

# System 2: [6 3] --> [12 12]
# 
#           [-2 -1] --> [-6 -6]

# In[11]:


x = np.array([[6,3],[-2,-1]])
h = np.array([[12, 12],[-6,-6]])

# Input 1 is scaled down by -1/3 to get [-2,-1] 
output = print(-1/3*h[0,:])


# System 2 does not obey scalability. If it did, we should expect that dividing the first output pair by -1/3 would give an answer of [-4,-4]. Given that this is not the case, system 2 is NOT a linear system.
# 

# System 3: [1,2] --> [5,-1]
#           [1,-1] --> [1,4]
#           [3,0] --> [7,8]

# In[17]:


x = np.array([[1,2], [1, -1], [3,0]])
x3 = print(x[0,:] + 2*x[1,:])

y = np.array([[5,-1],[1,4],[7,8]])
y3 = print(y[0,:] + 2*y[1,:])


# This system does not follow superposition. Y3 = Y1 + Y2. Summing the the first and second input paris (and multiplying input pair 2 by 2), we get the third input. When this same method is applied to the output pairs, a different output is seen. As such, System 3 is NOT a linear system because it does not follow the principles of superposition. 

# System 4: [2,4] --> 0 
#           [-2,1] --> 3
#     # Notice we are going from dimensionality 2 to 1, implying a dot product

# In[12]:


x1 = np.array([2, 4])
h = np.array([-6/5, 3/5])

y = print(np.dot(x1,h)) # Using a transfer function of 1/5[-6 3] we get the desired output

x2 = np.array([-2,1])
y2 = print(np.dot(x2,h))


# System 4 could potentially be a linear system. Using the transfer function h = 1/5[-6 3], it is found that this holds for both input/ouput pairs. This matrix is a unqiue matrix. Further scaling of the transfer function (h) will give a result that can be reduced back down to the original matrix. 

# System 5: 0 --> [1,2]

# Given that the input to the system is 0 and the output are two integers, this implies that no matrix multiplication can be performed, only addition. As such, this system cannot be linear.
# 
# System 5 is NOT a linear system. 
