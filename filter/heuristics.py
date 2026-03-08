import re
from typing import List
from models.tweet_models import Reply

MIN_TEXT_LENGTH = 20
LOW_SIGNAL_PATTERNS = [
    r"^great post",
    r"^awesome",
    r"^lol",
    r"^nice",
    r"^🔥+$",
]

def is_low_signal(text: str) -> bool:
    """
    Detect obvious junk replies.
    """
    text_lower = text.lower().strip()
    if len(text_lower) < MIN_TEXT_LENGTH:
        return True

    for pattern in LOW_SIGNAL_PATTERNS:
        if re.match(pattern, text_lower):
            return True

    return False

def heuristic_filter(replies: List[Reply]) -> List[Reply]:
    """
    Remove obvious low-value replies.
    """
    filtered = []
    for r in replies:
        if is_low_signal(r.text):
            continue

        filtered.append(r)
    return filtered

def deduplicate_replies(replies: List[Reply]) -> List[Reply]:
    seen = set()
    unique = []
    for r in replies:
        key = r.text.strip().lower()
        if key in seen:
            continue

        seen.add(key)
        unique.append(r)
    return unique
