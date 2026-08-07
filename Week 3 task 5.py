import matplotlib.pyplot as plt


# 1. Reusable Bar Chart Function
def plot_bar(categories, values, title="Bar Chart", xlabel="Category", ylabel="Value"):
    plt.figure(figsize=(8, 5))
    plt.bar(categories, values)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# 2. Reusable Line Chart Function
def plot_line(x, y, title="Line Chart", xlabel="X", ylabel="Y"):
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker="o")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# 3. Reusable Pie Chart Function
def plot_pie(labels, values, title="Pie Chart"):
    plt.figure(figsize=(7, 7))
    plt.pie(values, labels=labels, autopct="%1.1f%%")

    plt.title(title)
    plt.tight_layout()
    plt.show()


# -------------------------
# Example Usage
# -------------------------

subjects = ["AI", "ML", "Python", "NLP", "CV"]
marks = [85, 78, 92, 80, 88]

plot_bar(
    subjects,
    marks,
    title="Student Marks",
    xlabel="Subjects",
    ylabel="Marks"
)


months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 160, 210]

plot_line(
    months,
    sales,
    title="Monthly Sales",
    xlabel="Month",
    ylabel="Sales"
)


skills = ["Python", "AI", "ML", "NLP"]
hours = [30, 25, 20, 15]

plot_pie(
    skills,
    hours,
    title="Learning Time Distribution"
)
