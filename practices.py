import numpy as np

A=np.array([[ 2,3,1],
            [4,1,2],
            [3,2,3]])

D=np.linalg.det(A)

Dx=np.array([[ 1,3,1],
            [2,1,2],
            [3,2,3]])

Dy=np.array([[ 2,1,1],
            [4,2,2],
            [3,3,3]])

Dz=np.array([[ 2,3,1],
            [4,1,2],
            [3,2,3]])

Dx[:,0]=[1,2,3]
Dy[:,1]=[1,2,3]
Dz[:,2]=[1,2,3]

det_Dx=np.linalg.det(Dx)
det_Dy=np.linalg.det(Dy)
det_Dz=np.linalg.det(Dz)

x=det_Dx/D                                  
y=det_Dy/D
z=det_Dz/D

print(x)
print(y)
print(z)


    

