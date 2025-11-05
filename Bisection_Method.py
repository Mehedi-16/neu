import math

# Function
def f(x):
    return 3*x - math.cos(x) - 1

# Bisection Method
def bisection(a, b, tol):
    while abs(b - a) >= tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("Root is:", c)

# Fixed values
a = 0
b = 1
tol = 0.001

bisection(a, b, tol)
