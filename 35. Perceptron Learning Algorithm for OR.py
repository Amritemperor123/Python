# up until now, we were assigning weights and bias to the perceptrons mannunally, which is not practical to build a neural network
# this time, we will assign some initial values to the weights and bias, and then keep changing them to get the preffered output

import numpy as np

# we create an input dataset X, which contains the sets of input values 
# y is the dataset which has the output values for each input set
# our goal is to get the exact values of weights and bias which will give us the desired outputs when an input set is given
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1]) 

y = np.where(y == 1, 1, -1)

weights = np.zeros(2)
bias = 0

# signum function return 1 if a number if positive, else -1.
def signum(value):
    return 1 if value >= 0 else -1

# the trainning algorithm is where we make changes to the weights and bias
# convergence is a condition where the predicted output and the desired output becomes same
# by changing the weights and bias to reach convergence, we get the exact value we need
def train_perceptron():
    global weights, bias
    converged = False
    while not converged:
        converged = True 
        for i in range(len(X)):
            weighted_sum = np.dot(weights, X[i]) + bias
            
            if y[i] == 1 and weighted_sum < 0: 
                weights += X[i]
                bias += 1
                converged = False  
            elif y[i] == -1 and weighted_sum >= 0:  
                weights -= X[i]
                bias -= 1
                converged = False

train_perceptron()

print("Trained Weights:", weights)
print("Trained Bias:", bias)
for i in range(len(X)):
    weighted_sum = np.dot(weights, X[i]) + bias
    prediction = signum(weighted_sum)
    print(f"Input: {X[i]} -> Predicted Output: {1 if prediction == 1 else 0}")
