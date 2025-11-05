n = 3
a = [
    [2, -2, 3, 2],   # Equation 1
    [1,  2, -1, 3],  # Equation 2
    [3, -1, 2, 1]    # Equation 3
]
# Gauss-Jordan Elimination
for i in range(n):
    factor = a[i][i]
    for j in range(i, n+1):
        a[i][j] /= factor
        
    for k in range(n):
        if k != i:
            factor = a[k][i]
            for j in range(i, n+1):
                a[k][j] -= factor * a[i][j]


print("x1 =", round(a[0][n], 4))
print("x2 =", round(a[1][n], 4))
print("x3 =", round(a[2][n], 4))



