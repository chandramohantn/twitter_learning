from scraper.twitter_scraper import scrape_tweet

url = "https://x.com/karpathy/status/..."

tweet = scrape_tweet(url)

print("Author:", tweet.author)
print("Tweet:", tweet.text)
print()

print("Replies:")

for r in tweet.replies:
    print(f"- @{r.author} ({r.likes} likes)")
    print(r.text)
    print()