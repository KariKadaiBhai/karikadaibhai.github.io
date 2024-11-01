import numpy as np
import pandas as pd

class Node:
    def __init__(self, feature=None, value=None, left=None, right=None, output=None):
        self.feature = feature
        self.value = value
        self.left = left
        self.right = right
        self.output = output

class ID3:
    def __init__(self):
        self.tree = None

    def entropy(self, y):
        """Calculate the entropy of the target variable."""
        value_counts = y.value_counts()
        probabilities = value_counts / len(y)
        return -np.sum(probabilities * np.log2(probabilities + 1e-9))

    def information_gain(self, X, y, feature):
        """Calculate the information gain for a feature."""
        total_entropy = self.entropy(y)
        values = X[feature].unique()
        weighted_entropy = 0
        for value in values:
            subset = y[X[feature] == value]
            weighted_entropy += (len(subset) / len(y)) * self.entropy(subset)
        return total_entropy - weighted_entropy

    def best_feature(self, X, y):
        """Select the best feature to split on based on information gain."""
        gains = {feature: self.information_gain(X, y, feature) for feature in X.columns}
        return max(gains, key=gains.get)

    def build_tree(self, X, y):
        """Recursively build the decision tree."""
        if len(y.unique()) == 1:
            return Node(output=y.iloc[0])
        if X.empty:
            return Node(output=y.mode()[0])
        best_feat = self.best_feature(X, y)
        tree = Node(feature=best_feat)
        for value in X[best_feat].unique():
            subset = X[X[best_feat] == value]
            target_subset = y[X[best_feat] == value]
            subtree = self.build_tree(subset.drop(columns=[best_feat]), target_subset)
            if value == 1:
                tree.right = subtree  # Right branch for 1
            else:
                tree.left = subtree   # Left branch for 0
        return tree

    def fit(self, X, y):
        """Fit the ID3 model to the data."""
        self.tree = self.build_tree(X, y)

    def predict_one(self, node, x):
        """Make a prediction for a single instance."""
        if node.output is not None:
            return node.output
        if x[node.feature] == 1:
            return self.predict_one(node.right, x)
        else:
            return self.predict_one(node.left, x)

    def predict(self, X):
        """Make predictions for a DataFrame."""
        return X.apply(lambda x: self.predict_one(self.tree, x), axis=1)

if __name__ == "__main__":
    data = {
        'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny',   
                    'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Mild', 'Mild', 'Hot', 'Mild', 
                        'Cool', 'Mild', 'Cool', 'Cool'],
        'Humidity': ['High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'High',   
                     'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
        'Windy': [False, True, False, False, False, True, True, False, False, False, True, 
                  True, False, True],
        'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 
                 'No']
    }
    
    df = pd.DataFrame(data)
    X = df[['Outlook', 'Temperature', 'Humidity', 'Windy']]
    y = df['Play']
    X = pd.get_dummies(X, drop_first=True)
    
    id3 = ID3()
    id3.fit(X, y)
    predictions = id3.predict(X)
    print("Predictions:")
    print(predictions.tolist())
