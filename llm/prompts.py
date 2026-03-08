def build_structured_knowledge_prompt(tweet_text, replies):
    replies_text = "\n\n".join(
        [f"{r.author}: {r.text}" for r in replies]
    )
    prompt = f"""
        You are analyzing a Twitter discussion and converting it into structured knowledge.

        Tweet:
        {tweet_text}

        Important replies:
        {replies_text}

        Extract the following information.

        Return the result in JSON format.

        Fields required:

        core_idea:
        Short description of the main idea.

        key_insights:
        List of 3-6 important insights.

        technical_concepts:
        Important technical terms mentioned.

        tags:
        3-6 tags in kebab-case.

        simplified_explanation:
        Explain the concept in simple terms.

        analogy:
        Provide a helpful analogy if possible.

        related_topics:
        Topics someone should explore next.

        Return JSON only.
        """

    return prompt

def build_filter_prompt(reply_text):
    prompt = f"""
        Evaluate whether the following reply adds meaningful knowledge
        to a discussion.

        Useful replies include:
        - technical explanations
        - examples
        - counterarguments
        - corrections
        - deeper insights

        Reply with only TRUE or FALSE.
        Reply:
        {reply_text}
    """
    return prompt
