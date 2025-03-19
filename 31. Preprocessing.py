import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# Load dataset
data = load_iris(as_frame=True)
df = data.frame

# Handle missing values
imputer = SimpleImputer(strategy='mean')
df.iloc[:, :] = imputer.fit_transform(df)

# Encode categorical values (if any, here we assume the target is categorical)
encoder = OneHotEncoder()
y_encoded = encoder.fit_transform(df[['target']]).toarray()

# Normalize numeric features
scaler = StandardScaler()
X_normalized = scaler.fit_transform(df.drop(columns=['target']))

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y_encoded, test_size=0.3, random_state=42)

# Verify shapes
print("Train shapes:", X_train.shape, y_train.shape)
print("Test shapes:", X_test.shape, y_test.shape)
