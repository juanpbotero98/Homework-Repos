#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


# Part A

# In[ ]:


def plot_vect2(vect_matrix):
    rows,columns = np.shape(vect_matrix) 
    if rows == 2: 
        origin = np.zeros((columns,rows))
        fig, ax = plt.subplots(figsize=(10,6))
        plt.quiver(*origin,vect_matrix[:,0], vect_matrix[:,1], angles='xy', scale_units='xy', scale=1)
        plt.xlim((-1,1))
        plt.ylim((-1,1))

    else: 
        print('vector not 2-dimensional')
        


# In[ ]:


test_matrix = np.random.rand(2,2)
plot_vect2(test_matrix)


# Part B

# In[ ]:


def vecLenAngle(a,b):
    
    norm_a = la.norm(a,2)
    norm_b = la.norm(b,2)
    if norm_a == 0 or norm_b == 0:
        print('A vector has length = 0, cannot compute')
    else:
        theta = np.arccos((np.dot(a,b))/(norm_a*norm_b))
    
        return norm_a,norm_b,theta
        
        
    # # c- Get the angle theta between ~c and ~a. Get the unit vector of ~c in two ways (by shrinking
    # # the vector; by using the angle theta). Then create vectors that has the same length as ~c but
    # # with the angle that is 3,4 times of theta.

    


# In[ ]:


a = np.array([1,1])
b = np.array([1,2])

vecLenAngle(a,b)


# Part C

# In[ ]:


M = np.random.rand(2,2)
u,s,v = la.svd(M, full_matrices=True, compute_uv=True, hermitian=False)

s = np.diag(s)
e1 = np.array([1,0])
e2 = np.array([0,1])

e1_1 = v.T@e1
e1_2 = s@e1_1
e1_3 = u@e1_2

e2_1 = v.T@e2
e2_2 = s@e2_1
e2_3 = u@e2_2


# In[105]:


E1 = np.array([e1_1,e1_2,e1_3]).T
E2 = np.array([e2_1,e2_2,e2_3]).T

plot_vect2(E1)
plot_vect2(E2)


# In[108]:





# In[ ]:


np.shape(E1)


# Part D

# In[ ]:


n = 64
u = np.arange(0,n).T
thetan = (u(2*np.pi/n))
x = np.array([np.cos(thetan), np.sin(thetan)])

