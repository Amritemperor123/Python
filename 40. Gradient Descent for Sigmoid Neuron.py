import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Gradient Descent for Sigmoid Neuron
def train_sigmoid_neuron(X, y, learning_rate=0.1, epochs=10000):
    # Initialize weights and bias
    weights = np.random.rand(X.shape[1])
    bias = np.random.rand()
    
    for epoch in range(epochs):
        # Forward propagation
        linear_output = np.dot(X, weights) + bias
        predictions = sigmoid(linear_output)
        
        # Compute error
        error = y - predictions
        
        # Backpropagation (gradient computation)
        d_predictions = error * sigmoid_derivative(predictions)
        
        # Update weights and bias using gradient descent
        weights += learning_rate * np.dot(X.T, d_predictions)
        bias += learning_rate * np.sum(d_predictions)
        
        # Print loss every 1000 epochs
        if epoch % 1000 == 0:
            loss = np.mean(np.square(error))
            print(f"Epoch {epoch}, Loss: {loss}")
    
    return weights, bias

# Example usage
if __name__ == "__main__":
    # Sample dataset (XOR problem)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    
    # Train the neuron
    weights, bias = train_sigmoid_neuron(X, y)
    
    # Test the trained neuron
    predictions = sigmoid(np.dot(X, weights) + bias)
    print("Final Predictions:")
    print(predictions)
