import numpy as np 

def sigmoid(x): 
    return 1 / (1 + np.exp(-x)) 

def sigmoid_derivative(x): 
    return x * (1 - x) 

class NeuralNetwork: 
    def __init__(self): 
        self.weights = np.random.randn(2, 1)  # Fixed missing parenthesis 

    def forward(self, X): 
        self.input = X 
        self.output = sigmoid(np.dot(self.input, self.weights)) 
        return self.output 

    def backward(self, y, learning_rate=0.1): 
        error = y - self.output 
        delta = error * sigmoid_derivative(self.output) 
        self.weights += np.dot(self.input.T, delta) * learning_rate 

    def train(self, X, y, iterations=10000): 
        for _ in range(iterations): 
            self.forward(X) 
            self.backward(y) 

if __name__ == "__main__": 
    X = np.array([[0, 0], 
                  [0, 1], 
                  [1, 0], 
                  [1, 1]]) 
    y = np.array([[0], 
                  [1], 
                  [1], 
                  [0]]) 
    nn = NeuralNetwork() 
    nn.train(X, y)  
    output = nn.forward(X) 
    print("Predicted output:") 
    print(output) 
