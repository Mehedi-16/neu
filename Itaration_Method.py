import math

def f(x):
    return x**3 - x - 1

def g(x):
    return (x + 1)**(1/3)

x0 = 1.5

for i in range(100):
    x1 = g(x0)
    if abs(x1 - x0) < 1e-6:
        break
    x0 = x1

print(f"Approximate root is: {x1:.6f}")
