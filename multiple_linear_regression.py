import numpy as np

print("---- Multiple Linear Regression (Manual Formula) ----")

n = int(input("Enter number of data points: "))
m = int(input("Enter number of features (x1, x2, ..., xm): "))

X = []
y = []

print("\nEnter values for each data point:")
for i in range(n):
    row = []
    print(f"\n--- Data Point {i+1} ---")
    for j in range(m):
        val = float(input(f"Enter x{j+1}: "))
        row.append(val)
    X.append(row)

    target = float(input("Enter y value: "))
    y.append(target)

X = np.array(X)
y = np.array(y)

# Add bias term
X_b = np.c_[np.ones((n, 1)), X]

# Normal Equation
beta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

# Prediction input
print("\n===== PREDICTION =====")
new_x = []
print("\nEnter feature values to predict y:")
for j in range(m):
    val = float(input(f"Enter x{j+1}: "))
    new_x.append(val)

new_x = np.array([1] + new_x)
predicted_y = new_x @ beta

# WRITE OUTPUT TO FILE
with open("mlr_output.txt", "w") as f:
    f.write("===== MULTIPLE LINEAR REGRESSION OUTPUT =====\n\n")
    f.write(f"Number of data points: {n}\n")
    f.write(f"Number of features: {m}\n\n")

    f.write("Model Parameters:\n")
    f.write(f"Intercept (β0): {beta[0]}\n")
    for i in range(1, len(beta)):
        f.write(f"Coefficient β{i} (for x{i}): {beta[i]}\n")

    f.write("\nPrediction Result:\n")
    f.write(f"Predicted y = {predicted_y}\n")

print("Output saved in mlr_output.txt")
