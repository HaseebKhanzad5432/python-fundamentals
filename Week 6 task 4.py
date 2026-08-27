# Manual Perceptron Implementation

# Step function
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0


# Perceptron class
class Perceptron:
    def __init__(self, learning_rate=0.1):
        self.learning_rate = learning_rate
        self.weights = [0, 0]
        self.bias = 0

    def predict(self, inputs):
        # Weighted sum
        total = (inputs[0] * self.weights[0] +
                 inputs[1] * self.weights[1] +
                 self.bias)

        # Apply step function
        return step_function(total)

    def train(self, X, y, epochs=10):
        for epoch in range(epochs):
            for inputs, target in zip(X, y):

                prediction = self.predict(inputs)

                # Calculate error
                error = target - prediction

                # Update weights
                self.weights[0] += self.learning_rate * error * inputs[0]
                self.weights[1] += self.learning_rate * error * inputs[1]

                # Update bias
                self.bias += self.learning_rate * error


# Simple AND gate dataset
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

y = [0, 0, 0, 1]


# Create and train perceptron
model = Perceptron(learning_rate=0.1)
model.train(X, y, epochs=10)


# Test the perceptron
print("Weights:", model.weights)
print("Bias:", model.bias)

print("\nPredictions:")

for inputs in X:
    prediction = model.predict(inputs)
    print(inputs, "=>", prediction)
