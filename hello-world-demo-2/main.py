"This script fetches a random cat fact from a public API using requests:"
# main.py
import requests

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        fact = response.json().get("fact", "No fact found!")
        print(f"🐱 Cat Fact: {fact}")
    else:
        print("Failed to fetch cat fact. Try again later!")

if __name__ == "__main__":
    print("👋 Welcome to Hello World Demo 2!")
    get_cat_fact()
