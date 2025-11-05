import math

# Function definition
def f(x):
    return 3*x - math.cos(x) - 1

# False Position Method
def falsi(a, b, tol):
    while abs(b - a) >= tol:
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("Approximate root is:", c)

# Fixed values
a = 0
b = 1
tol = 0.001

# Call the method
falsi(a, b, tol)
