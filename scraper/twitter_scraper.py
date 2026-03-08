import snscrape.modules.twitter as sntwitter

from typing import List
from models.tweet_models import TweetData, Reply


MAX_REPLIES = 250
MIN_REPLY_LIKES = 1


def fetch_tweet(tweet_url: str):
    """
    Fetch main tweet information.
    """

    scraper = sntwitter.TwitterTweetScraper(tweet_url)
    tweet = next(scraper.get_items())

    return tweet


def fetch_replies(conversation_id: int) -> List[Reply]:
    """
    Fetch replies for a tweet conversation.
    """

    query = f"conversation_id:{conversation_id}"
    replies = []

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):

        # skip the root tweet
        if tweet.inReplyToTweetId is None:
            continue

        if tweet.likeCount < MIN_REPLY_LIKES:
            continue

        reply = Reply(
            author=tweet.user.username,
            text=tweet.content,
            likes=tweet.likeCount,
            url=tweet.url,
        )

        replies.append(reply)

        if len(replies) >= MAX_REPLIES:
            break

    return replies


def scrape_tweet(tweet_url: str) -> TweetData:
    """
    Scrape tweet and conversation replies.
    """

    tweet = fetch_tweet(tweet_url)
    tweet_data = TweetData(
        url=tweet.url,
        author=tweet.user.username,
        text=tweet.content,
        date=str(tweet.date),
    )

    replies = fetch_replies(tweet.id)
    tweet_data.replies = replies

    return tweet_data