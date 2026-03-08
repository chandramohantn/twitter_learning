import os
from pathlib import Path
import re
from dotenv import load_dotenv

load_dotenv()
VAULT_POSTS = os.getenv("VAULT_POSTS", "vault/twitter_posts")

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text[:80]

def generate_filename(tweet):
    title = slugify(tweet.core_idea or "twitter-post")
    filename = f"{title}.md"
    return filename

def save_markdown(filename, content):
    path = Path(VAULT_POSTS)
    path.mkdir(parents=True, exist_ok=True)
    file_path = path / filename
    file_path.write_text(content, encoding="utf-8")