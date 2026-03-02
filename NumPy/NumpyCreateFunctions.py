'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''
import numpy as np
from numpy.ma.core import identity

# 1D array
# This function creates a numpy array filled with zeros
# By this default, the data type is float64
a = np.zeros(4)
print(a)

# 2D array
a_2D = np.zeros((4,2))
print(a_2D)

#  Using numpy.ones() Function
a = np.ones(4)
print(a)

# 2D array of ones
a_2D = np.ones((4,2))
print(a_2D)

# Using numpy.arange() Function
# The numpy.arange() function creates an array by generating a sequence of numbers based on start,step and stop values
# it is similar to pythons built-in range() function

a = np.arange(4,10)
print(a)

# providing the start, stop and step values
a = np.arange(2,10,4)
print(a)

# Using numpy.linspace() Function
# linspace() is used to generate evenly spaced numbers over a specified interval
# endpoint is true last number is included


a = np.linspace(0,8,4,endpoint=True)
print(a)

# exclude the last number
a = np.linspace(2,12,6,endpoint=False)
print(a)

# Using numpy.random.rand() Function
# generates an array of the specified shape with random values between 0 and 1
# if no argument is provided, it returns a single random float value

a = np.random.rand(4)
print(a)

# 2D
a = np.random.rand(4,6)
print(a)

# 3D
a = np.random.rand(4,6,8)
print(a)

#  Using numpy.empty() Function
# 2D
# This function initializes an array without initializing its elements
# The content of the array is arbitrary and may vary

a = np.empty((3,4))
print(a)

# Using numpy.full() Function
# In the following example, we are using the numpy.full() function to create a 2D array
# filled entirely with the value 8

a = np.full((5,6), 8)
print(a)

# numpy.eye()
# the numpy eye function is used to
# create a 2D array with ones on the diagonal and zeros in all other positions

identity_matrix = np.eye((5))
print(identity_matrix)

# numpy identity - function is used generate a square identity matrix
identity_matrix = np.identity((4))
print(identity_matrix)

# numpy.diagonal
# in case of 2D array the function extracts the diagonal elements of the array
# in case of 1D array the function creates a square diagonal matrix with the elements of the diagonal values and zeros in remaining positions

Matrix = np.array([[10,20,30], [40,60,80], [110,140,170]])
print("Original matrix", Matrix)
Diagonal_elements = np.diag(Matrix)
print("Diagonal elements", Diagonal_elements)
