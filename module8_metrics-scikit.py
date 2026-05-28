import numpy as np
from sklearn.metrics import precision_score, recall_score


class BinaryMetricsScikit:
    def __init__(self, n):
        self.n = n
        self.points = np.empty((n, 2), dtype=int)

    def add_point(self, i, x, y):
        self.points[i] = [x, y]

    def precision(self):
        y_true = self.points[:, 0]
        y_pred = self.points[:, 1]
        return precision_score(y_true, y_pred, zero_division=0)

    def recall(self):
        y_true = self.points[:, 0]
        y_pred = self.points[:, 1]
        return recall_score(y_true, y_pred, zero_division=0)


if __name__ == "__main__":
    n = int(input("Enter N: "))

    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        metrics = BinaryMetricsScikit(n)
        for i in range(n):
            x = int(input(f"Enter x (ground truth) for point {i + 1}: "))
            y = int(input(f"Enter y (predicted) for point {i + 1}: "))
            metrics.add_point(i, x, y)

        print(f"Precision = {metrics.precision()}")
        print(f"Recall = {metrics.recall()}")
