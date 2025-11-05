def f(x, y):
    return x + y  # dy/dx = x + y

# Initial values (from RK4 or given)
x = [0, 0.1, 0.2, 0.3]
y = [1.0, 1.1103, 1.2428, 1.3997]
h = 0.1

# Calculate f(x, y)
f0 = f(x[0], y[0])
f1 = f(x[1], y[1])
f2 = f(x[2], y[2])
f3 = f(x[3], y[3])

# Predictor
y4_pred = y[0] + (4*h/3)*(2*f1 - f2 + 2*f3)

# Corrector
f4_pred = f(x[3] + h, y4_pred)
y4_corr = y[2] + (h/3)*(f2 + 4*f3 + f4_pred)

print("Predicted y4 =", round(y4_pred, 5))
print("Corrected y4 =", round(y4_corr, 5))
