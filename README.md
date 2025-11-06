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


1. b. For the initial value problem (IVP) y'-y = -(1/2)(e^(t/2)) * sin(5t) + 5(e^(t/2)) + cos(5t), y(0) = 0 Use Euler's Method to find the approximation to the solution at t=1, t=2, t=3, t=4, and t=5. Use h=0.1, h=0.5, h=0.01, h=0.05, h=0.001, and h=0.005 for the approximations. Compare them to the exact values of the solution at these points. Show also the result in tabular format and plot the solution data using graphically.

```
import math

def f(t, y):
    return y + (-0.5 * math.exp(t/2) * math.sin(5*t) + 5 * math.exp(t/2) + math.cos(5*t))

# Initial values
t = 0       # initial t
y = 0       # initial y
h = 0.1     # step size
n = 10      # number of steps

# Euler's Method Loop
for i in range(n):
    y = y + h * f(t, y)
    t = t + h

print("Step", i+1, ": t =", round(t, 2), ", y =", round(y, 4))
```
