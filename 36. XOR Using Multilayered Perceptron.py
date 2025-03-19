import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(0)
input_size, hidden_size, output_size = 2, 2, 1

W1 = np.random.uniform(-1, 1, (input_size, hidden_size))
b1 = np.zeros((1, hidden_size))
W2 = np.random.uniform(-1, 1, (hidden_size, output_size))
b2 = np.zeros((1, output_size))

learning_rate = 0.5
epochs = 10000

def train():
    global W1, b1, W2, b2
    for _ in range(epochs):

        hidden_input = np.dot(X, W1) + b1
        hidden_output = sigmoid(hidden_input)
        output_input = np.dot(hidden_output, W2) + b2
        output = sigmoid(output_input)
        
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)
        
        hidden_error = output_delta.dot(W2.T)
        hidden_delta = hidden_error * sigmoid_derivative(hidden_output)
        
        W2 += hidden_output.T.dot(output_delta) * learning_rate
        b2 += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        W1 += X.T.dot(hidden_delta) * learning_rate
        b1 += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

def predict(x):
    hidden_output = sigmoid(np.dot(x, W1) + b1)
    output = sigmoid(np.dot(hidden_output, W2) + b2)
    return np.round(output)

train()

print("XOR Predictions:")
for i in range(len(X)):
    print(f"Input: {X[i]} -> Predicted Output: {predict(X[i])}")