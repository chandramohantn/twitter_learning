from models.tweet_models import TweetData
from .heuristics import heuristic_filter, deduplicate_replies
from .llm_filter import llm_filter

MAX_FINAL_REPLIES = 25

def filter_replies(tweet: TweetData) -> TweetData:
    """
    Apply multi-stage filtering to replies.
    """
    replies = tweet.replies

    # stage 1 — heuristic filtering
    replies = heuristic_filter(replies)

    # stage 2 — deduplicate
    replies = deduplicate_replies(replies)

    # stage 3 — llm relevance filter
    replies = llm_filter(replies)

    # limit final replies
    replies = replies[:MAX_FINAL_REPLIES]
    tweet.replies = replies
    return tweet