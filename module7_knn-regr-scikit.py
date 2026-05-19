import numpy as np
from sklearn.neighbors import KNeighborsRegressor

n = int(input("Enter N: "))
k = int(input("Enter k: "))

points = np.empty((n, 2), dtype=float)
for i in range(n):
    points[i, 0] = float(input(f"Enter x for point {i + 1}: "))
    points[i, 1] = float(input(f"Enter y for point {i + 1}: "))

x_query = float(input("Enter X to predict Y: "))

if k > n:
    print("Error: k must be less than or equal to N.")
else:
    X_train = points[:, 0].reshape(-1, 1)
    y_train = points[:, 1]

    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    y_pred = model.predict([[x_query]])
    print(f"Y = {y_pred[0]}")
    print(f"Variance of training labels: {np.var(y_train)}")
