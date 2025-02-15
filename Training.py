import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder

# Load dataset
data = pd.read_csv("data.csv") 

# Inputs: Angle & Distance
X = data.iloc[:, :-1].values  

# Labels: Action
y = data.iloc[:, -1].values  

# Convert actions to numbers
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# Build AI Model
model = Sequential([
    Dense(8, activation='relu', input_shape=(2,)),  # Angle, Distance
    Dense(8, activation='relu'),
    Dense(len(set(y)), activation='softmax')
])

# Compile & Train
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=50, batch_size=8)

# Save Model
model.save("car_ai.h5")
print("✅ AI Model trained and saved!")
