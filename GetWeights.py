import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("car_ai.h5")

# Extract Weights & Biases from each layer
for i, layer in enumerate(model.layers):
    weights, biases = layer.get_weights()
    print(f"Layer {i} Weights:\n", np.array2string(weights, separator=","))
    print(f"Layer {i} Biases:\n", np.array2string(biases, separator=","))
