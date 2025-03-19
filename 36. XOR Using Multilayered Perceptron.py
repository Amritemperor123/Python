# upto this point, we were using a single neuron which could compute the AND and OR operations swiftly
# then why should we build a multilayered neural network?
# beacuse these problems we just solved are linearly seperable 
# which means you can draw a line in the graph and the inputs and outputs will take two seperatte sides
# but there are problems which are not as simple as these 
# i.e. you cannot seperate the inputs from outputs by drawing a straight line
# XOR operation is a good example of these kind of problems
# to solve these problems, we need a multilayered nrural network

import numpy as np

# sigmoid function is a type of step function which decides when a neuron/perceptron should fire
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# these are the input and output sets
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(0)

# these are the number of perceptrons in the input layer, hidden layer and the output layer
input_size, hidden_size, output_size = 2, 2, 1

# weights and bias for the hidden layer
W1 = np.random.uniform(-1, 1, (input_size, hidden_size))
b1 = np.zeros((1, hidden_size))

# weights and bias for the output layer
W2 = np.random.uniform(-1, 1, (hidden_size, output_size))
b2 = np.zeros((1, output_size))

# learning rate defines the rate of change of weights and bias 
learning_rate = 0.5

# epochs define the number of times a model train using the same dataset
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
