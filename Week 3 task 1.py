import matplotlib.pyplot as plt

# Sample dataset
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 180, 200, 170]

# -------------------------
# Bar Chart
# -------------------------
plt.figure(figsize=(6, 4))
plt.bar(months, sales)
plt.title("Monthly Sales (Bar Chart)")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# -------------------------
# Line Chart
# -------------------------
plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales (Line Chart)")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# -------------------------
# Pie Chart
# -------------------------
plt.figure(figsize=(6, 6))
plt.pie(
    sales,
    labels=months,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Monthly Sales Distribution (Pie Chart)")
plt.show()
