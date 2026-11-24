import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
DATA_DIR= os.getenv("DATA_DIR", "./data/")

def  extract(url, filepath):
    try:
        x = requests.get(url)
        with open(filepath, "w") as file:
            json.dump(x.json(), file, indent=4)
    except Exception as e:
        print(str(e))
    
    
    
if __name__ == "__main__":
    extract("https://dst-de.s3.eu-west-3.amazonaws.com/rncp38919/data/data.json", DATA_DIR+"data.json")