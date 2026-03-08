import os
import asyncio
from extractor.whatsapp_parser import parse_whatsapp_export
from extractor.deduplicator import (
    filter_new_urls,
    load_processed_urls,
    save_processed_urls,
)

from scraper.twitter_scraper import scrape_tweet
from filter.reply_filter import filter_replies
from processor.knowledge_extractor import extract_knowledge
from generator.markdown_generator import generate_markdown
from generator.tag_index import build_tag_index
from generator.knowledge_links import build_knowledge_links
from dotenv import load_dotenv

load_dotenv()

CHAT_FILE = os.getenv("CHAT_FILE", "chat.txt")

async def process_tweet(url):
    loop = asyncio.get_event_loop()

    print(f"\nProcessing tweet: {url}")
    tweet = await loop.run_in_executor(None, scrape_tweet, url)
    tweet = await loop.run_in_executor(None, filter_replies, tweet)
    tweet = await loop.run_in_executor(None, extract_knowledge, tweet)
    filename = await loop.run_in_executor(None, generate_markdown, tweet)
    print(f"Markdown created: {filename}")


async def run_pipeline():
    print("\nStarting Twitter Knowledge Pipeline\n")

    urls = parse_whatsapp_export(CHAT_FILE)
    new_urls = filter_new_urls(urls)
    processed = load_processed_urls()

    tasks = []
    for url in new_urls:
        task = asyncio.create_task(process_tweet(url))
        tasks.append(task)
        processed.add(url)

    await asyncio.gather(*tasks)
    save_processed_urls(processed)
    print("\nPipeline completed.\n")
    build_tag_index()
    print("Tag index updated.")
    build_knowledge_links()
    print("Knowledge links updated.")