# Handwritten Digit Classifier
# Using a small MNIST subset and a basic neural network

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. Use a small subset
x_train = x_train[:10000]
y_train = y_train[:10000]

x_test = x_test[:2000]
y_test = y_test[:2000]

# 3. Normalize pixel values (0-255 -> 0-1)
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# 4. Build a basic neural network
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

# 5. Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# 6. Train the model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# 7. Evaluate the model
test_loss, test_accuracy = model.evaluate(
    x_test, y_test, verbose=0
)

print("\nEvaluation Report")
print("------------------")
print("Test Loss:", round(test_loss, 4))
print("Test Accuracy:", round(test_accuracy * 100, 2), "%")

# 8. Make predictions
predictions = model.predict(x_test, verbose=0)
predicted_labels = np.argmax(predictions, axis=1)

# 9. Find misclassified examples
misclassified = np.where(predicted_labels != y_test)[0]

print("\nNumber of misclassified images:", len(misclassified))

# 10. Display a few misclassified examples
plt.figure(figsize=(10, 6))

for i, index in enumerate(misclassified[:6]):
    plt.subplot(2, 3, i + 1)
    plt.imshow(x_test[index], cmap="gray")
    plt.title(
        f"True: {y_test[index]}, "
        f"Predicted: {predicted_labels[index]}"
    )
    plt.axis("off")

plt.tight_layout()
plt.show()
