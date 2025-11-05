def f(x):
    return x**2  # এখানে আপনি যেকোনো ফাংশন দিতে পারেন

# Input values
a = 0      # lower limit
b = 4      # upper limit
n = 4      # number of subintervals (must be even)

h = (b - a) / n  # step size

# Simpson's 1/3 Rule formula
sum = f(a) + f(b)

for i in range(1, n):
    x = a + i * h
    if i % 2 == 0:
        sum += 2 * f(x)
    else:
        sum += 4 * f(x)

area = (h / 3) * sum
print("Approximate area =", area)
