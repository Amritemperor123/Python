# MP neurones or McCullouch Pits neurons are the building blocks to build a neural network. 
# a single MP neuron has two functions, the first one being aggregation and the second one being the threshold
# the aggregation is done by adding up all the inputs.
# the threshold is set based on various criteria, which decides when a neuron should fire (output = 1) or when it should not (output = 0)
# MP neurons can only process binary data

import matplotlib.pyplot as plt
import numpy as np

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ['0', '1']:
            return int(user_input)
        else:
            print("Invalid input. Please enter 0 or 1.")

# the OR operation returns 1 if any one of the inputs is 1
# the minimum aggregated sum for a OR neuron to fire would be 1
def OR(x1, x2):    
    return 1 if (x1 + x2) >= 1 else 0

# the AND operation returns 1 only if both the inputs are 1
# the minimum aggregated sum for a AND neuron to fire would be 2
def AND(x1, x2):    
    return 1 if (x1 + x2) >= 2 else 0

x1 = get_valid_input("Enter first input (0 or 1): ")
x2 = get_valid_input("Enter second input (0 or 1): ")

print("The output of the OR operation is:", OR(x1, x2))
print("The output of the AND operation is:", AND(x1, x2))

x = np.linspace(0, 2, 400)
y1 = 1 - x
y2 = 2 - x

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='OR (x + y = 1)', color='blue')
plt.plot(x, y2, label='AND (x + y = 2)', color='green')
plt.scatter(x1, x2, color='red', label=f'Point ({x1}, {x2})')
plt.xlim(0, 2.2)
plt.ylim(0, 2.2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of Equations x + y = 1 and x + y = 2 with Point (x1, x2)')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
