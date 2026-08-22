# K-Fold Cross-Validation with Random Forest

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold
import numpy as np

# Load dataset
data = load_iris()

X = data.data
y = data.target

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Create 5-fold cross-validation
kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# Perform cross-validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=kf,
    scoring="accuracy"
)

# Display results
print("Accuracy for each fold:", scores)
print("Average Accuracy:", np.mean(scores))
