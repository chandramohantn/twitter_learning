import re
from typing import List

TWITTER_REGEX = r"https://x\.com/.*/status/\d+"

def extract_tweet_urls(text: str) -> List[str]:
    """
    Extract tweet URLs from a block of text.
    """
    matches = re.findall(TWITTER_REGEX, text)
    return list(set(matches))