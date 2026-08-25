from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Actual labels
y_actual = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]

# Predicted labels
y_predicted = [1, 1, 0, 0, 0, 1, 1, 0, 0, 0]

# Compute confusion matrix
cm = confusion_matrix(y_actual, y_predicted)

print("Confusion Matrix:")
print(cm)

# Display confusion matrix
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)
disp.plot()
plt.title("Confusion Matrix")
plt.show()
