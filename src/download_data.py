import requests
import os

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
OUTPUT_PATH = "data/raw/titanic.csv"

def main():
    os.makedirs("data/raw", exist_ok=True)
    response = requests.get(URL)
    response.raise_for_status()
    with open(OUTPUT_PATH, "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    main()
