from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Reply:
    author: str
    text: str
    likes: int
    url: Optional[str] = None


@dataclass
class TweetData:
    url: str
    author: str
    text: str
    date: str

    replies: List[Reply] = field(default_factory=list)

    # Processor outputs
    core_idea: Optional[str] = None
    insights: List[str] = field(default_factory=list)
    concepts: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    simplified_explanation: Optional[str] = None
    analogy: Optional[str] = None
    related_topics: List[str] = field(default_factory=list)