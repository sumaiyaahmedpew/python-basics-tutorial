# Matrix operations using NumPy
import numpy as np
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
sum_mat = mat1 + mat2
prod_mat = mat1 @ mat2
print("Matrix 1:\n", mat1)
print("Matrix 2:\n", mat2)
print("Sum:\n", sum_mat)
print("Product:\n", prod_mat)
