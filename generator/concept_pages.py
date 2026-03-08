import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
VAULT_CONCEPTS = os.getenv("VAULT_CONCEPTS", "vault/concepts")

def create_concept_pages(concepts):
    VAULT_CONCEPTS.mkdir(parents=True, exist_ok=True)
    for concept in concepts:
        filename = concept.replace(" ", "-").lower() + ".md"
        path = VAULT_CONCEPTS / filename
        if path.exists():
            continue

        content = f"""
            # {concept}

            ## Description

            (To be filled later)

            ## Related Posts
        """

        path.write_text(content.strip())