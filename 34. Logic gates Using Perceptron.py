def perceptron(inputs, weights, threshold):
    weighted_sum = sum(i * w for i, w in zip(inputs, weights))    
    return 1 if weighted_sum >= threshold else 0

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ['0', '1']:
            return int(user_input)
        else:
            print("Invalid input. Please enter 0 or 1.")

def OR_gate(inputs):
    weights = [1, 1]
    threshold = 1
    return perceptron(inputs, weights, threshold)

def AND_gate(inputs):
    weights = [1, 1]
    threshold = 2
    return perceptron(inputs, weights, threshold)

x1 = get_valid_input("Enter first input (0 or 1): ")
x2 = get_valid_input("Enter second input (0 or 1): ")
    
inputs = [x1, x2]
        
print("Testing the OR gate with your input pairs:", OR_gate(inputs))
print("Testing the AND gate with your input pairs:", AND_gate(inputs))