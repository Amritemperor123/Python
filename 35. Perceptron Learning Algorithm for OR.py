import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 1]) 

y = np.where(y == 1, 1, -1)

weights = np.zeros(2)
bias = 0

def signum(value):
    return 1 if value >= 0 else -1

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