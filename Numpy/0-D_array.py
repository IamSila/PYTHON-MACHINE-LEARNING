"""create a 0-D aray with the value of 42"""


import numpy as np
array_0D = np.array(42)


"""create a 1-D aray with the values 1 2 3 4 5"""
array_1D = np.array([1, 2, 3, 4, 5])



"""Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6"""
array_2D = np.array([1, 2, 3], [4, 5, 6])


"""Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6"""
array_3D = np.array([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])
print(array_3D.ndim)

