def f(x):
    return x**2  # যেটা integrate করতে হবে

a = 0           # lower limit
b = 4           # upper limit
n = 4           # কত ভাগে ভাগ করব

h = (b - a) / n # step size

sum = f(a) + f(b)

for i in range(1, n):
    x = a + i * h
    sum += 2 * f(x)

area = (h / 2) * sum
print("Area =", area)
