import json
from models.tweet_models import TweetData
from llm.prompts import build_structured_knowledge_prompt
from llm.client import LLMClient

llm = LLMClient()

def extract_knowledge(tweet: TweetData) -> TweetData:
    prompt = build_structured_knowledge_prompt(tweet.text, tweet.replies)
    response = llm.generate(prompt, temperature=0.2)
    try:
        data = json.loads(response)
        tweet.core_idea = data.get("core_idea")
        tweet.insights = data.get("key_insights", [])
        tweet.concepts = data.get("technical_concepts", [])
        tweet.tags = data.get("tags", [])
        tweet.simplified_explanation = data.get("simplified_explanation")
        tweet.analogy = data.get("analogy")
        tweet.related_topics = data.get("related_topics", [])
    except Exception as e:
        print("Failed to parse LLM response:", e)
    return tweet