import numpy as np
def gauss_jordan(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    M = np.hstack([A, b.reshape(-1,1)])

    for i in range(n):
        M[i] = M[i]/M[i][i]
        for j in range(n):
            if i != j:
                M[j] = M[j] - M[j][i] * M[i]
    return M[:,-1]

A = np.array([[2,3,-1], [4,4,-3], [-2,3,-2]], float)
b = np.array([5,3,1], float)
solution = gauss_jordan(A,b)
print("solution = ", solution)