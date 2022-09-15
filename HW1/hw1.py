import numpy as np 
import matplotlib.pyplot as plt
## 1) Testing Linearity 
## System 1 --> Doesn't obey scalability when input is scaled by 2.5 output is not.
## System 2 --> 

## 3) 

def plot_vect2(vect_matrix):
    rows,columns = np.shape(vect_matrix) 
    if rows == 2: 
        origin = np.zeros((rows,columns))
        # fig, ax = plt.subplots(figsize=(10,6))
        plt.quiver(*origin,vect_matrix[:,0], vect_matrix[:,1], angles='xy', scale_units='xy', scale=1)
        plt.xlim((-1,1))
        plt.ylim((-1,1))
        plt.imshow()
    else: 
        print('vector not 2-dimensional')

test_matrix = np.random.rand(2,2)
plot_vect2(test_matrix)
print('done')