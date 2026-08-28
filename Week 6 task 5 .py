# Install PyTorch if needed:
# pip install torch

import torch
import torch.nn as nn
import torch.optim as optim

# -----------------------------
# 1. Toy Dataset
# -----------------------------
# Features: [Study Hours, Attendance]
X = torch.tensor([
    [1.0, 50.0],
    [2.0, 55.0],
    [3.0, 60.0],
    [4.0, 65.0],
    [5.0, 70.0],
    [6.0, 75.0],
    [7.0, 80.0],
    [8.0, 85.0]
])

# Labels: 0 = Fail, 1 = Pass
y = torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [0.0],
    [1.0],
    [1.0],
    [1.0],
    [1.0]
])

# Normalize the input data
X[:, 0] = X[:, 0] / 8.0       # Study hours
X[:, 1] = X[:, 1] / 100.0    # Attendance


# -----------------------------
# 2. Define Neural Network
# -----------------------------
class FeedForwardNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(2, 8),      # Input layer -> Hidden layer
            nn.ReLU(),
            nn.Linear(8, 4),      # Hidden layer
            nn.ReLU(),
            nn.Linear(4, 1),      # Output layer
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)


# Create model
model = FeedForwardNN()


# -----------------------------
# 3. Loss Function & Optimizer
# -----------------------------
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)


# -----------------------------
# 4. Train the Model
# -----------------------------
epochs = 1000

for epoch in range(epochs):

    # Forward pass
    predictions = model(X)

    # Calculate loss
    loss = criterion(predictions, y)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()

    # Update weights
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")


# -----------------------------
# 5. Test the Model
# -----------------------------
with torch.no_grad():

    predictions = model(X)

    predicted_classes = (predictions >= 0.5).float()

    accuracy = (predicted_classes == y).float().mean()

    print("\nPredicted Probabilities:")
    print(predictions)

    print("\nPredicted Classes:")
    print(predicted_classes)

    print("\nActual Classes:")
    print(y)

    print(f"\nAccuracy: {accuracy.item() * 100:.2f}%")
