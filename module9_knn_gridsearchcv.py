import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


class KNNClassifierGridSearch:
    def __init__(self, n):
        self.n = n
        self.points = np.empty((n, 2), dtype=float)

    def add_point(self, i, x, y):
        self.points[i] = [x, y]

    def features(self):
        return self.points[:, 0].reshape(-1, 1)

    def labels(self):
        return self.points[:, 1].astype(int)

    def search_best_k(self, k_max=10):
        X_train = self.features()
        y_train = self.labels()

        # cv folds must not exceed the size of the smallest class.
        min_class_count = np.min(np.bincount(y_train))
        cv = min(5, min_class_count)

        if cv < 2:
            # Not enough samples per class for cross-validation; fall back
            # to scoring each k directly on the training set.
            best_k, best_score = 1, -1.0
            for k in range(1, min(k_max, self.n) + 1):
                model = KNeighborsClassifier(n_neighbors=k)
                model.fit(X_train, y_train)
                score = model.score(X_train, y_train)
                if score > best_score:
                    best_k, best_score = k, score
            return best_k

        # During cross-validation each fold trains on fewer samples, so k must
        # not exceed the smallest per-fold training size.
        max_fold_size = int(np.ceil(self.n / cv))
        k_upper = min(k_max, self.n - max_fold_size)
        param_grid = {"n_neighbors": list(range(1, k_upper + 1))}

        search = GridSearchCV(
            KNeighborsClassifier(),
            param_grid,
            cv=cv,
            scoring="accuracy",
        )
        search.fit(X_train, y_train)
        return search.best_params_["n_neighbors"]

    def test_accuracy(self, k, test_set):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(self.features(), self.labels())
        X_test = test_set.features()
        y_test = test_set.labels()
        return model.score(X_test, y_test)


def read_pairs(set_name, count):
    dataset = KNNClassifierGridSearch(count)
    for i in range(count):
        x = float(input(f"Enter x for {set_name} pair {i + 1}: "))
        y = int(input(f"Enter y for {set_name} pair {i + 1}: "))
        dataset.add_point(i, x, y)
    return dataset


if __name__ == "__main__":
    n = int(input("Enter N (size of training set): "))
    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        train_set = read_pairs("training", n)

        m = int(input("Enter M (size of test set): "))
        if m <= 0:
            print("Error: M must be a positive integer.")
        else:
            test_set = read_pairs("test", m)

            best_k = train_set.search_best_k(k_max=10)
            accuracy = train_set.test_accuracy(best_k, test_set)

            print(f"Best k: {best_k}")
            print(f"Test accuracy: {accuracy}")
