import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create toy dataset
X, y = make_classification(
    n_samples=1000,
    n_features=4,
    n_classes=2,
    random_state=42
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)


# Neural Network
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(4, 16),
            nn.ReLU(),
            nn.Linear(16, 2)
        )

    def forward(self, x):
        return self.model(x)


# Function to train and evaluate
def train_model(learning_rate, epochs):

    model = NeuralNetwork()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        optimizer.zero_grad()

        output = model(X_train)
        loss = criterion(output, y_train)

        loss.backward()
        optimizer.step()

    # Test accuracy
    with torch.no_grad():
        predictions = model(X_test).argmax(dim=1)
        accuracy = (predictions == y_test).float().mean().item()

    return accuracy


# Try different learning rates and epochs
settings = [
    (0.001, 50),
    (0.001, 100),
    (0.01, 50),
    (0.01, 100),
    (0.1, 50),
    (0.1, 100)
]

print("Learning Rate | Epochs | Accuracy")
print("----------------------------------")

for lr, epochs in settings:
    accuracy = train_model(lr, epochs)

    print(
        f"{lr:<14} | {epochs:<6} | "
        f"{accuracy * 100:.2f}%"
      )
