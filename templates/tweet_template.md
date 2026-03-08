---
source: twitter
url: {{url}}
author: {{author}}
date: {{date}}

tags:
{% for tag in tags %}
- {{tag}}
{% endfor %}

related_topics:
{% for topic in related_topics %}
- {{topic}}
{% endfor %}
---

# Twitter Post

> {{tweet_text}}

Author: **{{author}}**

Source: {{url}}

---

# Core Idea

{{core_idea}}

---

# Key Insights

{% for insight in insights %}
- {{insight}}
{% endfor %}

---

# Important Replies

{% for reply in replies %}
## Reply — {{reply.author}} ({{reply.likes}} likes)

> {{reply.text}}

{% endfor %}

---

# Extracted Concepts

{% for concept in concepts %}
- [[{{concept}}]]
{% endfor %}

---

# Simplified Explanation

{{simplified_explanation}}

---

# Analogy

{{analogy}}

---

# Related Topics

{% for topic in related_topics %}
- [[{{topic}}]]
{% endfor %}

---

# Learning Session

*(To be filled during teacher-student interaction)*

## Student Questions

Q1:  
A1:

---

## Assessment

Score:

Feedback:

---

# References

- {{url}}