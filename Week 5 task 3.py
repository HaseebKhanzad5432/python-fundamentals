# Random Forest vs Decision Tree
# Using Python and Scikit-learn

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------------------------------------------
# 1. Load Dataset
# ---------------------------------------------------

iris = load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# ---------------------------------------------------
# 2. Split Dataset
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ---------------------------------------------------
# 3. Train Single Decision Tree
# ---------------------------------------------------

decision_tree = DecisionTreeClassifier(
    random_state=42
)

decision_tree.fit(X_train, y_train)

# Predictions
dt_predictions = decision_tree.predict(X_test)

# Accuracy
dt_accuracy = accuracy_score(y_test, dt_predictions)

print("Decision Tree Accuracy:", dt_accuracy)

# ---------------------------------------------------
# 4. Train Random Forest
# ---------------------------------------------------

random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

random_forest.fit(X_train, y_train)

# Predictions
rf_predictions = random_forest.predict(X_test)

# Accuracy
rf_accuracy = accuracy_score(y_test, rf_predictions)

print("Random Forest Accuracy:", rf_accuracy)

# ---------------------------------------------------
# 5. Compare Accuracy
# ---------------------------------------------------

print("\nAccuracy Comparison")
print("-------------------")
print(f"Decision Tree : {dt_accuracy:.2f}")
print(f"Random Forest : {rf_accuracy:.2f}")

# ---------------------------------------------------
# 6. Feature Importance - Decision Tree
# ---------------------------------------------------

dt_importance = decision_tree.feature_importances_

dt_features = pd.DataFrame({
    "Feature": X.columns,
    "Importance": dt_importance
})

print("\nDecision Tree Feature Importance:")
print(dt_features.sort_values(
    by="Importance",
    ascending=False
))

# ---------------------------------------------------
# 7. Feature Importance - Random Forest
# ---------------------------------------------------

rf_importance = random_forest.feature_importances_

rf_features = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_importance
})

print("\nRandom Forest Feature Importance:")
print(rf_features.sort_values(
    by="Importance",
    ascending=False
))

# ---------------------------------------------------
# 8. Plot Feature Importance Comparison
# ---------------------------------------------------

comparison = pd.DataFrame({
    "Decision Tree": dt_importance,
    "Random Forest": rf_importance
}, index=X.columns)

comparison.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Feature Importance: Decision Tree vs Random Forest")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# 9. Accuracy Comparison Graph
# ---------------------------------------------------

models = ["Decision Tree", "Random Forest"]
accuracies = [dt_accuracy, rf_accuracy]

plt.figure(figsize=(7, 5))
plt.bar(models, accuracies)

plt.title("Accuracy Comparison")
plt.ylabel("Accuracy")
plt.ylim(0, 1)

for i, value in enumerate(accuracies):
    plt.text(i, value + 0.02, f"{value:.2f}", ha="center")

plt.show()
