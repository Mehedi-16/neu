def f(x, y):
    return x + y  # dy/dx = x + y

# Initial values
x0 = 0       # initial x
y0 = 1       # initial y
h = 0.1      # step size
n = 10       # number of steps

# Euler's Method Loop
for i in range(n):
    y0 = y0 + h * f(x0, y0)
    x0 = x0 + h
    
print("Step", i+1, ": x =", round(x0, 2), ", y =", round(y0, 4))
