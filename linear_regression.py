import numpy as np

print("---- Multiple Linear Regression (Manual Formula) ----")

# Input
n = int(input("Enter number of data points: "))
m = int(input("Enter number of features: "))

X = []
y = []

print("\nEnter values for each data point:")
for i in range(n):
    row = []
    print(f"\n--- Data Point {i+1} ---")
    for j in range(m):
        row.append(float(input(f"Enter x{j+1}: ")))
    X.append(row)
    y.append(float(input("Enter y value: ")))

X = np.array(X)
y = np.array(y)

# Add bias column
X_b = np.c_[np.ones((n, 1)), X]

# Use pseudo-inverse (safe for singular matrix)
beta = np.linalg.pinv(X_b) @ y

# Model output (terminal)
print("\n===== MODEL OUTPUT =====")
print("Intercept (b0):", beta[0])
for i in range(1, len(beta)):
    print(f"Coefficient b{i}:", beta[i])

# Prediction
print("\n===== PREDICTION =====")
new_x = []
for j in range(m):
    new_x.append(float(input(f"Enter x{j+1}: ")))

new_x = np.array([1] + new_x)
predicted_y = new_x @ beta

print("Predicted y:", predicted_y)

# Write output to file (ASCII safe)
with open("mlr_output.txt", "w") as f:
    f.write("===== MULTIPLE LINEAR REGRESSION OUTPUT =====\n\n")
    f.write(f"Number of data points: {n}\n")
    f.write(f"Number of features: {m}\n\n")

    f.write("Model Parameters:\n")
    f.write(f"Intercept (b0): {beta[0]}\n")
    for i in range(1, len(beta)):
        f.write(f"Coefficient b{i}: {beta[i]}\n")

    f.write("\nPrediction:\n")
    f.write(f"Predicted y: {predicted_y}\n")

print("\nDONE ✔ Output saved in mlr_output.txt")
