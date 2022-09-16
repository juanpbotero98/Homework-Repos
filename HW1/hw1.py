import numpy as np 
import matplotlib.pyplot as plt
import numpy.linalg as la
## 1) Testing Linearity 
## System 1 --> Doesn't obey scalability when input is scaled by 2.5 output is not.
## System 2 --> 

## 3) 

# def plot_vect2(vect_matrix):
#     rows,columns = np.shape(vect_matrix) 
#     if rows == 2: 
#         origin = np.zeros((rows,columns))
#         # fig, ax = plt.subplots(figsize=(10,6))
#         plt.quiver(*origin,vect_matrix[:,0], vect_matrix[:,1], angles='xy', scale_units='xy', scale=1)
#         plt.xlim((-1,1))
#         plt.ylim((-1,1))
#         # plt.imshow()
#     else: 
#         print('vector not 2-dimensional')

# test_matrix = np.random.rand(2,2)
# plot_vect2(test_matrix)
# print('done')

def gram_schmidt(N):
    M = np.random.randn(N,N)
    basis = []
    for v in M:
        w = v - np.sum( np.dot(v,b)*b  for b in basis )
        if (w > 1e-10).any():
            basis.append(w/np.linalg.norm(w))
    return np.array(basis)

def orthonormal_check(basis):
    n = 0
    for B in basis:
        if np.ceil(la.norm(B)) != 1:
            return False
        n = n + 1
        k = 0
        for x in basis:
            k = k + 1
            if k == n:
                continue
            y = np.dot(B,x)
            if np.floor(np.abs(y)) != 0:
                return False
    return True


test = 3
test2 = 4

basis1 = gram_schmidt(test)
basis2 = gram_schmidt(test2)

ortho1 = orthonormal_check(basis1)
ortho2 = orthonormal_check(basis2)