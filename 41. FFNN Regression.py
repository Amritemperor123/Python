import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = keras.utils.get_file("auto-mpg.data",
                              "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data",
                              cache_dir='./', cache_subdir='datasets')

column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']

df = pd.read_csv(dataset, names=column_names, na_values="?", comment='\t', sep="\s+", skipinitialspace=True)

df = df.dropna()

X = df.drop(columns=['MPG'])
y = df['MPG']

X = pd.get_dummies(X, columns=['Origin'], prefix='', prefix_sep='')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=16, verbose=1)

loss, mae = model.evaluate(X_test, y_test, verbose=1)
print(f"Test Mean Absolute Error: {mae:.2f} MPG")

predictions = model.predict(X_test)
print("Sample Predictions:")
print(predictions[:10])