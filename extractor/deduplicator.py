import os
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
STORAGE_FILE = os.getenv("STORAGE_FILE", "storage/processed_urls.json")

def load_processed_urls():
    path = Path(STORAGE_FILE)
    if not path.exists():
        return set()
    return set(json.loads(path.read_text()))

def save_processed_urls(urls):
    Path(STORAGE_FILE).write_text(json.dumps(list(urls), indent=2))

def filter_new_urls(urls):
    processed = load_processed_urls()
    new_urls = [u for u in urls if u not in processed]
    return new_urls