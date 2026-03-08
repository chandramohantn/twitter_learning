import os
from pathlib import Path
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()
VAULT_POSTS = Path(os.getenv("VAULT_POSTS", "vault/twitter_posts"))

def extract_concepts(content):
    concepts = []
    lines = content.split("\n")
    capture = False
    for line in lines:
        if line.strip().lower().startswith("# extracted concepts"):
            capture = True
            continue

        if capture:
            if not line.startswith("-"):
                break

            concept = line.replace("-", "").strip()
            concept = concept.replace("[[", "").replace("]]", "")
            concepts.append(concept)
    return concepts


def build_concept_index():
    concept_index = defaultdict(list)
    posts = {}
    for file in VAULT_POSTS.glob("*.md"):
        content = file.read_text()
        concepts = extract_concepts(content)
        posts[file.stem] = concepts
        for c in concepts:
            concept_index[c].append(file.stem)
    return posts, concept_index

def compute_related_posts(posts, concept_index):
    related_map = defaultdict(set)
    for concept, files in concept_index.items():
        for f1 in files:
            for f2 in files:
                if f1 != f2:
                    related_map[f1].add(f2)

    return related_map

def update_related_section(file_path, related_posts):
    content = file_path.read_text()
    lines = content.split("\n")
    new_lines = []
    skip = False
    for line in lines:
        if line.strip() == "# Related Posts":
            skip = True
            new_lines.append("# Related Posts")
            new_lines.append("")
            for post in sorted(related_posts):
                new_lines.append(f"- [[{post}]]")
            new_lines.append("")
            continue

        if skip:
            if line.startswith("#"):
                skip = False
        if not skip:
            new_lines.append(line)

    file_path.write_text("\n".join(new_lines))

def build_knowledge_links():
    posts, concept_index = build_concept_index()
    related_map = compute_related_posts(posts, concept_index)
    for file in VAULT_POSTS.glob("*.md"):
        post_name = file.stem
        related = related_map.get(post_name, [])
        update_related_section(file, related)

