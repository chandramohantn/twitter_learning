import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from models.tweet_models import TweetData
from .file_utils import generate_filename, save_markdown
from generator.concept_pages import create_concept_pages
from dotenv import load_dotenv

load_dotenv()

TEMPLATE_DIR = os.getenv("TEMPLATE_DIR", "templates")
VAULT_POSTS = os.getenv("VAULT_POSTS", "vault/twitter_posts")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("tweet_template.md")

def render_markdown(tweet: TweetData):
    markdown = template.render(
        url=tweet.url,
        author=tweet.author,
        date=tweet.date,
        tweet_text=tweet.text,
        core_idea=tweet.core_idea,
        insights=tweet.insights,
        concepts=tweet.concepts,
        tags=tweet.tags,
        simplified_explanation=tweet.simplified_explanation,
        analogy=tweet.analogy,
        related_topics=tweet.related_topics,
        replies=tweet.replies
    )
    return markdown


def generate_markdown(tweet: TweetData):
    markdown = render_markdown(tweet)
    create_concept_pages(tweet.concepts)
    filename = generate_filename(tweet)
    save_markdown(filename, markdown)
    return filename