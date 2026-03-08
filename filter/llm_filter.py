from typing import List
from models.tweet_models import Reply
from llm.client import LLMClient
from llm.prompts import build_filter_prompt

llm = LLMClient()

def llm_is_insightful(reply_text: str) -> bool:
    prompt = build_filter_prompt(reply_text)
    response = llm.generate(prompt)
    answer = response.choices[0].message.content.strip()
    return "TRUE" in answer.upper()


def llm_filter(replies: List[Reply]) -> List[Reply]:
    filtered = []
    for r in replies:
        try:
            if llm_is_insightful(r.text):
                filtered.append(r)
        except Exception:
            # if LLM fails, keep reply
            filtered.append(r)

    return filtered