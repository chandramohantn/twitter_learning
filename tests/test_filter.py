from scraper.twitter_scraper import scrape_tweet
from filter.reply_filter import filter_replies

url = "https://x.com/.../status/..."
tweet = scrape_tweet(url)
print("Replies before filtering:", len(tweet.replies))
tweet = filter_replies(tweet)
print("Replies after filtering:", len(tweet.replies))

for r in tweet.replies:
    print()
    print(f"@{r.author} ({r.likes} likes)")
    print(r.text)