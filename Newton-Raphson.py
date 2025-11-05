def f(x):
    return x**2 - 4

def df(x):
    return 2*x

x = 3  # initial guess
for i in range(5):
    x = x - f(x)/df(x)
    print(f"Iteration {i+1}: x = {round(x, 6)}")
