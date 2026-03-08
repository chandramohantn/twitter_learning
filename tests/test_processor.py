from scraper.twitter_scraper import scrape_tweet
from filter.reply_filter import filter_replies
from processor.knowledge_extractor import extract_knowledge


url = "https://x.com/.../status/..."
tweet = scrape_tweet(url)
tweet = filter_replies(tweet)
tweet = extract_knowledge(tweet)

print("Core Idea:", tweet.core_idea)
print()

print("Insights:")
for i in tweet.insights:
    print("-", i)
print()

print("Tags:", tweet.tags)
print("Concepts:", tweet.concepts)