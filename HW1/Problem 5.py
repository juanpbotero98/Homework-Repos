#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import numpy.linalg as la

def gram_schmidt(N):
    M = np.random.randn(N,N)
    basis = []
    for v in M:
        w = v - np.sum( np.dot(v,b)*b  for b in basis )
        if (w > 1e-10).any():
            basis.append(w/np.linalg.norm(w))
    return np.array(basis)

## We can check if the created matrix is orthonormal if the norm of the vector = 1 and if the dotproduct of each vector = 0
def orthonormal_check(basis):
    n = 0
    for B in basis:
        if np.ceil(la.norm(B)) != 1: # Checks the normality condition
            return False
        n = n + 1
        k = 0
        for x in basis:
            k = k + 1
            if k == n: # A vector dotted with itself does not indicate orthogonality, skip cases when looking at the same vector
                continue
            y = np.dot(B,x)
            if np.floor(np.abs(y)) != 0: # Checks the orthogonality condition in which the dotproduct of to Ortho vectors = 0
                return False
    return True


test = 3 # N = 3 case
test2 = 4 # N = 4 case

basis1 = gram_schmidt(test)
basis2 = gram_schmidt(test2)

ortho1 = orthonormal_check(basis1)
ortho2 = orthonormal_check(basis2)


# In[19]:





# In[9]:


np.shape(basis)

