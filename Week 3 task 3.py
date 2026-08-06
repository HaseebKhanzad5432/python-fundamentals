import requests
import json

# Public REST API URL
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Send GET request
    response = requests.get(url)

    # Check if request was successful
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Save data to a JSON file
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data fetched successfully!")
    print("Saved to 'users.json'.")

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
