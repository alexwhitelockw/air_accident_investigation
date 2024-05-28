import json
import re
import requests

def load_json(filepath):
    with open(filepath, "r") as file:
        return json.load(file)
    
def load_viewed_links(filepath):
    with open(filepath) as file:
        return [line.strip() for line in file]
    
def save_viewed_link(filepath, link):
    with open(filepath, "a") as file:
        file.write(f"{link}\n")

def sanitise_title(title):
    title = title.strip().lower().split(",")[0]
    return re.sub(r"[^a-zA-Z0-9]+", "_", title)

def download_pdf(filename, pdf_link):
    try:
        response = requests.get(pdf_link)
        response.raise_for_status()
  
        with open(filename, "wb") as file:
            file.write(response.content)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error Downloading {pdf_link}: {e}")
        return False
