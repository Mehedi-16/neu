def f(x):
    return x**2  # এখানে যেকোনো ফাংশন দিতে পারেন

# Input values
a = 0      # lower limit
b = 4      # upper limit
n = 6      # number of subintervals (must be multiple of 3)

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
print("Approximate area =", area)
