import numpy as np 

def sigmoid(x): 
    return 1 / (1 + np.exp(-x)) 

def sigmoid_derivative(x): 
    return x * (1 - x) 

class NeuralNetwork: 
    def __init__(self, input_size, hidden_size, output_size): 
        self.weights_input_hidden = np.random.randn(input_size, hidden_size) 
        self.weights_hidden_output = np.random.randn(hidden_size, output_size) 

    def forward(self, X): 
        self.hidden_input = np.dot(X, self.weights_input_hidden) 
        self.hidden_output = sigmoid(self.hidden_input) 
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) 
        self.output = sigmoid(self.output_input) 
        return self.output 

    def backward(self, X, y, learning_rate=0.1): 
        output_error = y - self.output 
        output_delta = output_error * sigmoid_derivative(self.output) 
        hidden_error = output_delta.dot(self.weights_hidden_output.T) 
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output) 
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate 
        self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate 

    def train(self, X, y, iterations): 
        for _ in range(iterations): 
            self.forward(X) 
            self.backward(X, y) 

if __name__ == "__main__": 
    X = np.array([[0, 0], 
                  [0, 1], 
                  [1, 0], 
                  [1, 1]]) 
    y = np.array([[0], 
                  [1], 
                  [1], 
                  [0]]) 
    nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1) 
    nn.train(X, y, iterations=10000) 
    output = nn.forward(X) 
    print("Predicted output:") 
    print(output) 
