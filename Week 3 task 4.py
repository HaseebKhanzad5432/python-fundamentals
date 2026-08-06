import requests
import matplotlib.pyplot as plt
from collections import Counter

# Public REST API
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Fetch data from API
    response = requests.get(url)
    response.raise_for_status()

    # Parse JSON response
    posts = response.json()

    # Count posts per user
    user_posts = Counter(post["userId"] for post in posts)

    # Prepare data for chart
    users = list(user_posts.keys())
    counts = list(user_posts.values())

    # Create bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(users, counts)
    plt.title("Number of Posts by User")
    plt.xlabel("User ID")
    plt.ylabel("Number of Posts")

    # Save chart
    plt.savefig("posts_chart.png")

    # Display chart
    plt.show()

    print("Chart saved as 'posts_chart.png'")

except requests.exceptions.RequestException as e:
    print("Error:", e)
