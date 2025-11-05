# Picard's Method দিয়ে dy/dx = x + y সমাধান
# Step size h = 0.1, Initial y(0) = 1

# Step 1: ফাংশন সংজ্ঞায়িত করি
def f(x, y):
    return x + y

# Step 2: প্রাথমিক মান
x0 = 0
y0 = 1
h = 0.1

# Step 3: প্রথম অনুমান (y0(x) = y0)
def y0_func(x):
    return y0

# Step 4: প্রথম iteration (y1(x))
def y1_func(x):
    return y0 + (x**2)/2 + x  # Integration of x + y0

# Step 5: দ্বিতীয় iteration (y2(x))
# এখানে y1(x) = 1 + x + x^2/2 ব্যবহার করে f(x, y1(x)) = x + y1(x)
# তারপর integrate করি: ∫(x + y1(x)) dx

def y2_func(x):
    # f(x, y1) = x + (1 + x + x^2/2) = 1 + 2x + x^2/2
    # Integration: ∫(1 + 2x + x^2/2) dx = x + x^2 + x^3/6
    return y0 + x + x**2 + x**3/6

# Step 6: ফলাফল দেখাই
x = 0.1
print(f"x = {x}")
print(f"y1(x) = {y1_func(x):.5f}")
print(f"y2(x) = {y2_func(x):.5f}")
