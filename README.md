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


1. c. You are working for "COMPANY" that makes floats for ABC commodes. The floating ball has a specific gravity of 0.6 and has a radius of 5.5cm. You are asked to find the depth to which the ball is submerged when floating in water. The equation that gives the depth x to which the ball is submerged under water is given by X^4 - 0.165*X^2 + 3.993x10^(-2) = 0 Use the false-position method of finding roots of equations to find the depth x to which the ball is submerged under water. Conduct three iterations to estimate the root of the above equation. Find the absolute relative approximate error at the end of each iteration, and the number of significant digits at least correct at the end of third iteration.

```

# Function definition
def f(x):
    return x**4 - 0.165*x**2 + 3.993e-2

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
    print("Approximate root is:", round(c, 6))

# Fixed values
a = 0
b = 1
tol = 0.001

# Call the method
falsi(a, b, tol)


```


<img width="1752" height="410" alt="image" src="https://github.com/user-attachments/assets/6fa5233d-60a3-4334-a561-e38ee760436f" />

```
import math

def f(t):
    return 200 * math.log(140000 / (140000 - 2100 * t)) - 9.8 * t

# Input values
a = 8       # lower limit
b = 30      # upper limit
n = 6       # number of subintervals (must be multiple of 3)

h = (b - a) / n  # step size

# Simpson's 3/8 Rule formula
sum = f(a) + f(b)

for i in range(1, n):
    x = a + i * h
    if i % 3 == 0:
        sum += 2 * f(x)
    else:
        sum += 3 * f(x)

area = (3 * h / 8) * sum
print("Approximate vertical distance =", round(area, 4), "meters")

```
