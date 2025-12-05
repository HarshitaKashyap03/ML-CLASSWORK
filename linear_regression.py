# Linear Regression with user input

# Taking input
n = int(input("Enter number of data points: "))

X = []
Y = []

print("Enter X values:")
for i in range(n):
    X.append(float(input()))

print("Enter Y values:")
for i in range(n):
    Y.append(float(input()))

# Step 1: Means
mean_x = sum(X) / n
mean_y = sum(Y) / n

# Step 2: Slope (m)
num = 0
den = 0
for i in range(n):
    num += (X[i] - mean_x) * (Y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

m = num / den

# Step 3: Intercept (c)
c = mean_y - m * mean_x

print("\n===== RESULT =====")
print("Slope (m):", m)
print("Intercept (c):", c)

# Prediction
x_new = float(input("\nEnter X value to predict Y: "))
y_pred = m * x_new + c
print("Predicted Y =", y_pred)