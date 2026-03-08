import os
from pathlib import Path
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()
VAULT_POSTS = Path(os.getenv("VAULT_POSTS", "vault/twitter_posts"))
VAULT_TAGS = Path(os.getenv("VAULT_TAGS", "vault/tags"))

def build_tag_index():
    tag_map = defaultdict(list)
    for file in VAULT_POSTS.glob("*.md"):
        content = file.read_text()
        if "tags:" not in content:
            continue

        lines = content.split("\n")
        capture = False
        for line in lines:
            if line.strip() == "tags:":
                capture = True
                continue

            if capture:
                if not line.startswith("-"):
                    break
                tag = line.replace("-", "").strip()
                tag_map[tag].append(file.stem)

    VAULT_TAGS.mkdir(parents=True, exist_ok=True)
    for tag, posts in tag_map.items():
        tag_file = VAULT_TAGS / f"{tag}.md"
        lines = [f"# {tag}\n"]
        for p in posts:
            lines.append(f"- [[{p}]]")
        tag_file.write_text("\n".join(lines))