# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample numeric dataset
data = {
    'Age': [20, 22, 25, 28, 30, 35, 40],
    'Height': [160, 165, 170, 175, 180, 178, 185],
    'Weight': [55, 60, 65, 70, 75, 78, 85],
    'Salary': [25000, 30000, 35000, 40000, 45000, 50000, 60000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
correlation = df.corr()

# Create heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(
    correlation,
    annot=True,       # Show correlation values
    cmap="coolwarm",  # Color theme
    fmt=".2f",        # Display values with 2 decimal places
    linewidths=0.5
)

# Add title
plt.title("Correlation Heatmap")

# Display heatmap
plt.show()
