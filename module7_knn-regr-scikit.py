import numpy as np
from sklearn.neighbors import KNeighborsRegressor


class KNNRegressorScikit:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.points = np.empty((n, 2), dtype=float)
        self.model = KNeighborsRegressor(n_neighbors=k)

    def add_point(self, i, x, y):
        self.points[i] = [x, y]

    def fit(self):
        X_train = self.points[:, 0].reshape(-1, 1)
        y_train = self.points[:, 1]
        self.model.fit(X_train, y_train)

    def predict(self, x_query):
        return self.model.predict([[x_query]])[0]

    def label_variance(self):
        return np.var(self.points[:, 1])


if __name__ == "__main__":
    n = int(input("Enter N: "))
    k = int(input("Enter k: "))

    if k > n:
        print("Error: k must be less than or equal to N.")
    else:
        regressor = KNNRegressorScikit(n, k)
        for i in range(n):
            x = float(input(f"Enter x for point {i + 1}: "))
            y = float(input(f"Enter y for point {i + 1}: "))
            regressor.add_point(i, x, y)

        regressor.fit()

        x_query = float(input("Enter X to predict Y: "))
        print(f"Y = {regressor.predict(x_query)}")
        print(f"Variance of training labels: {regressor.label_variance()}")
