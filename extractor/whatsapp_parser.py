from pathlib import Path
from typing import List
from .url_extractor import extract_tweet_urls


def parse_whatsapp_export(file_path: str) -> List[str]:
    """
    Parse WhatsApp exported chat file and extract tweet URLs.
    """
    text = Path(file_path).read_text(encoding="utf-8")
    urls = extract_tweet_urls(text)
    return urls