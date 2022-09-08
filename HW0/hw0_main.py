import numpy as np
from numpy.linalg import norm 

## 1) Basics Try the following quick exercises
## a- Using Pythagoras' theorem, calculate the length of a hypotenuse of a right triangle given the length of the other two sides is 1 and 1.
h = np.sqrt(2)
## b- NO FUTHER DEVELOPED 

## 2) Vectors and plotting
## a- Create two vectors that represent the two sides of right triangle with the length of 1 and
## 1 (~a and ~b).Then get the vector ~c for the hypotenuse. Calculate the length of ~c. Check if 
## it agrees with the previous calculation.
a = np.array([1,0])
b = np.array([0,1])
c = a - b 
norm_c = norm(c,2)
print(norm_c==h)

# # c- Get the angle theta between ~c and ~a. Get the unit vector of ~c in two ways (by shrinking
# # the vector; by using the angle theta). Then create vectors that has the same length as ~c but
# # with the angle that is 3,4 times of theta.
theta = np.acos((np.dot(c,a))/norm_c)
c_unit = c/norm_c


## 3) PhD financial life in NYC - modeling your financial life as a first year phd student.
## a- Income from NYU: since you will have a steady income, create a column vector of 12 elements each with same amount of 3000.
income = np.ones(12)*3000
## b- Assuming you decide to TA from the second semester, therefore receiving an income of
## 4000 on the 7th month. Incorporate that to your income vector.
income[6] = income[6] + 4000
# # c- Life expense: create a matrix of expenses with again 12 rows and each column repre-
# # senting a category (rent, grocery, clothing, fun). You can start with a constant expense
# # as a first approximation.
outcome = np.concatenate(((np.ones((12,1))*1500),(np.ones((12,1))*600),(np.ones((12,1))*150),(np.ones((12,1))*150)),axis = 1) #(rent, grocery, clothing, fun)
# # d- Get your saving vector for each month and calculate how much money you've got left
# # after the whole year.
outcome_month = outcome.sum(axis=1)
savings = income - outcome_month
savings_year = savings.sum()
# # e- Grocery and clothing will hopefully get cheaper after you gradually finding out the
# # best options around. Suppose by the end of year your grocery expense will be only
# # 80 percent as of the first month. And in between your expense is linearly decreasing.
# # Using linspace(1,0.8,12) to create a "discount vector" and apply to the grocery and
# # clothing columns of the expense matrix.
discount = np.linspace(1,.8,12)
outcome[:,1] = outcome[:,1] * discount
outcome[:,2] = outcome[:,2] * discount


