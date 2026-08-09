# EDA Mini-Dashboard
# Dataset: Iris Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load Public Dataset
# -----------------------------
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

df = pd.read_csv(url)

print("Dataset Loaded Successfully!")
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# 2. Create Dashboard
# -----------------------------
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Chart 1: Species Count
sns.countplot(
    data=df,
    x="species",
    ax=axes[0, 0]
)
axes[0, 0].set_title("Number of Flowers by Species")
axes[0, 0].set_xlabel("Species")
axes[0, 0].set_ylabel("Count")

# Chart 2: Sepal Length Distribution
sns.histplot(
    data=df,
    x="sepal_length",
    kde=True,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Sepal Length Distribution")
axes[0, 1].set_xlabel("Sepal Length")
axes[0, 1].set_ylabel("Frequency")

# Chart 3: Petal Length by Species
sns.boxplot(
    data=df,
    x="species",
    y="petal_length",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Petal Length by Species")
axes[1, 0].set_xlabel("Species")
axes[1, 0].set_ylabel("Petal Length")

# Chart 4: Petal Length vs Petal Width
sns.scatterplot(
    data=df,
    x="petal_length",
    y="petal_width",
    hue="species",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Petal Length vs Petal Width")
axes[1, 1].set_xlabel("Petal Length")
axes[1, 1].set_ylabel("Petal Width")

plt.suptitle("Iris Dataset - EDA Mini Dashboard", fontsize=18)
plt.tight_layout()

# Save dashboard
plt.savefig("eda_dashboard.png", dpi=300)

# Display dashboard
plt.show()

# -----------------------------
# 3. Generate Insights
# -----------------------------

print("\n--- EDA INSIGHTS ---")

# Find average values by species
species_avg = df.groupby("species")[[
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]].mean()

largest_petal = species_avg["petal_length"].idxmax()
smallest_petal = species_avg["petal_length"].idxmin()

correlation = df["petal_length"].corr(df["petal_width"])

print(
    f"1. The dataset contains {len(df)} flower records divided equally "
    f"among the three species."
)

print(
    f"2. {largest_petal} has the largest average petal length, while "
    f"{smallest_petal} has the smallest average petal length."
)

print(
    f"3. Petal length and petal width have a strong positive correlation "
    f"of {correlation:.2f}."
)

print(
    "4. The boxplot and scatterplot show that petal measurements provide "
    "a clear separation between the different Iris species."
)
