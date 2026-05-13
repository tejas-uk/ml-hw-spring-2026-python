import numpy as np


class KNNRegressor:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.points = np.empty((n, 2), dtype=float)

    def add_point(self, i, x, y):
        self.points[i] = [x, y]

    def predict(self, x_query):
        distances = np.abs(self.points[:, 0] - x_query)
        nearest_idx = np.argsort(distances)[: self.k]
        return np.mean(self.points[nearest_idx, 1])


if __name__ == "__main__":
    n = int(input("Enter N: "))
    k = int(input("Enter k: "))

    if k > n:
        print("Error: k must be less than or equal to N.")
    else:
        regressor = KNNRegressor(n, k)
        for i in range(n):
            x = float(input(f"Enter x for point {i + 1}: "))
            y = float(input(f"Enter y for point {i + 1}: "))
            regressor.add_point(i, x, y)

        x_query = float(input("Enter X to predict Y: "))
        print(f"Y = {regressor.predict(x_query)}")
