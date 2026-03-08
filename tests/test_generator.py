from scraper.twitter_scraper import scrape_tweet
from filter.reply_filter import filter_replies
from processor.knowledge_extractor import extract_knowledge
from generator.markdown_generator import generate_markdown


url = "https://x.com/.../status/..."
tweet = scrape_tweet(url)
tweet = filter_replies(tweet)
tweet = extract_knowledge(tweet)
filename = generate_markdown(tweet)
print("Markdown created:", filename)