#!/usr/bin/env python
# coding: utf-8

# In[59]:


from scipy.io import loadmat
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

mtxN = loadmat('mtxExamples.mat')


# Matrix 1

# In[60]:


mtx1 = mtxN['mtx1']
print(mtx1)


# In[88]:


rank = np.linalg.matrix_rank(mtx1)
U, s, V = np.linalg.svd(mtx1, full_matrices = True)
if rank > len(V):   
    t_U_M = np.transpose(U)
    nrow = t_U_M.shape[0]
    left_null_M1 = t_U_M[rank:nrow,:]
    left_null_M1
    np.dot((left_null_M1[0,:] + left_null_M1[0,:]), mtx1)
else:
    print('Only null space is from the zero vector')


# In[ ]:





# In[82]:


np.shape(V)


# In[ ]:





# Matrix 2

# In[ ]:


mtx2= mtxN['mtx2']
print(mtx2)


# In[ ]:


u,s,v = la.svd(mtx2, full_matrices=True, compute_uv=True, hermitian=False)


# In[ ]:





# Matrix 3

# In[ ]:


mtx3= mtxN['mtx3']
print(mtx3)


# In[ ]:


u,s,v = la.svd(mtx3, full_matrices=True, compute_uv=True, hermitian=False)


# Matrix 4

# In[ ]:


mtx4= mtxN['mtx4']
print(mtx4)


# In[ ]:


u,s,v = la.svd(mtx4, full_matrices=True, compute_uv=True, hermitian=False)

