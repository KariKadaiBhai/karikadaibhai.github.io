import numpy as np

class KMeans:
    def __init__(self, k=2, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None

    def fit(self, X):
        np.random.seed(42)
        self.centroids = X[np.random.choice(range(len(X)), self.k, replace=False)]
        
        for _ in range(self.max_iters):
            labels = self.assign_clusters(X)
            new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.k)])
            if np.all(new_centroids == self.centroids):
                break
            self.centroids = new_centroids

    def assign_clusters(self, X):
        distances = np.array([np.linalg.norm(X - centroid, axis=1) for centroid in self.centroids])
        return np.argmin(distances, axis=0)

    def predict(self, X):
        return self.assign_clusters(X)

if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [8, 7], [9, 8], [10, 9]])
    kmeans = KMeans(k=2)
    kmeans.fit(X)
    labels = kmeans.predict(X)
    print("Cluster labels:", labels)
    print("Centroids:", kmeans.centroids)
