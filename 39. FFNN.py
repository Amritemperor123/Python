import tensorflow as tf
from tensorflow import keras
import numpy as np

# Sample dataset (XOR problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Create a Feedforward Neural Network model
model = keras.Sequential([
    keras.layers.Dense(4, activation='sigmoid', input_shape=(2,)),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10000, verbose=1)

# Test the network
predictions = model.predict(X)
print("Predictions:")
print(predictions)
