# neu

1. a. Consider finding the root of f(x) = (e^-x) (3.2 sin(x) - 0.5 cos(x)) on the interval [3, 4], this time with Estep = 0.001, Eabs = 0.001. Show also the result in tabular format and plot the solution using graphicalłły using Bisection method.

```
import math

# Function
def f(x):
    return math.exp(-x) * (3.2 * math.sin(x) - 0.5 * math.cos(x))

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
    print("Root is:", round(c, 6))

# Fixed values
a = 3
b = 4
tol = 0.001

bisection(a, b, tol)
```
