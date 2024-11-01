import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTree:
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
        self.tree = None

    def gini(self, y):
        classes = np.unique(y)
        gini = 1.0
        for c in classes:
            p = np.sum(y == c) / len(y)
            gini -= p ** 2
        return gini

    def split(self, X, y, feature, threshold):
        left_mask = X[:, feature] <= threshold
        right_mask = X[:, feature] > threshold
        return X[left_mask], X[right_mask], y[left_mask], y[right_mask]

    def best_split(self, X, y):
        best_feature, best_threshold, best_gini = None, None, float('inf')
        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                X_left, X_right, y_left, y_right = self.split(X, y, feature, threshold)
                if len(y_left) == 0 or len(y_right) == 0:
                    continue
                gini_left = self.gini(y_left)
                gini_right = self.gini(y_right)
                weighted_gini = (len(y_left) / len(y) * gini_left) + (len(y_right) / len(y) * gini_right)
                if weighted_gini < best_gini:
                    best_feature, best_threshold, best_gini = feature, threshold, weighted_gini
        return best_feature, best_threshold

    def build_tree(self, X, y, depth=0):
        num_samples_per_class = [np.sum(y == c) for c in np.unique(y)]
        most_common_class = np.argmax(num_samples_per_class)
        if depth >= self.max_depth or len(np.unique(y)) == 1:
            return Node(value=most_common_class)
        feature, threshold = self.best_split(X, y)
        if feature is None:
            return Node(value=most_common_class)
        X_left, X_right, y_left, y_right = self.split(X, y, feature, threshold)
        left_child = self.build_tree(X_left, y_left, depth + 1)
        right_child = self.build_tree(X_right, y_right, depth + 1)
        return Node(feature=feature, threshold=threshold, left=left_child, right=right_child)

    def fit(self, X, y):
        self.tree = self.build_tree(X, y)

    def predict_one(self, x, node):
        if node.value is not None:
            return node.value
        if x[node.feature] <= node.threshold:
            return self.predict_one(x, node.left)
        else:
            return self.predict_one(x, node.right)

    def predict(self, X):
        return [self.predict_one(x, self.tree) for x in X]

if __name__ == "__main__":
    X = np.array([[2, 3], [1, 1], [3, 6], [6, 7], [7, 2], [8, 4]])
    y = np.array([0, 0, 1, 1, 0, 1])  # Target labels
    clf = DecisionTree(max_depth=3)
    clf.fit(X, y)
    predictions = clf.predict(X)
    print("Predictions:", predictions)
