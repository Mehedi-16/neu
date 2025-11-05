import numpy as np

# Coefficients of the equations
# Equation 1: 2x + 3y + z = 1
# Equation 2: 4x + y  + 2z = 2
# Equation 3: 3x + 2y + 3z = 3

A = np.array([[2, 3, 1],
              [4, 1, 2],
              [3, 2, 3]])

D = np.linalg.det(A)  # Main determinant

# Replace columns with constants to get Dx, Dy, Dz
Dx = np.array([[1, 3, 1],
               [2, 1, 2],
               [3, 2, 3]])

Dy = np.array([[2, 1, 1],
               [4, 2, 2],
               [3, 3, 3]])

Dz = np.array([[2, 3, 1],
               [4, 1, 2],
               [3, 2, 3]])

Dx[:,0] = [1,2,3]  # Replace 1st column with constants
Dy[:,1] = [1,2,3]  # Replace 2nd column with constants
Dz[:,2] = [1,2,3]  # Replace 3rd column with constants

# Determinants
det_Dx = np.linalg.det(Dx)
det_Dy = np.linalg.det(Dy)
det_Dz = np.linalg.det(Dz)

# Solutions
x = det_Dx / D
y = det_Dy / D
z = det_Dz / D

print("x =", round(x, 4))
print("y =", round(y, 4))
print("z =", round(z, 4))


