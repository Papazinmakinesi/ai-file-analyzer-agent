import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def fallback_analyze_text(text):
    """
    Provides a basic local analysis if the API is unavailable.
    """

    words = text.lower().replace(".", "").replace(",", "").split()
    keywords = []

    for word in words:
        if len(word) > 5 and word not in keywords:
            keywords.append(word)

    keywords = keywords[:8]

    sentences = [s.strip() for s in text.split(".") if s.strip()]
    summary = ". ".join(sentences[:3]) + "."

    if "python" in text.lower() or "software" in text.lower() or "api" in text.lower():
        classification = "technical"
    elif "student" in text.lower() or "education" in text.lower() or "learning" in text.lower():
        classification = "educational"
    else:
        classification = "general"

    return f"""Summary:
{summary}

Keywords:
{", ".join(keywords)}

Classification:
{classification}

Note:
This result was generated using the local fallback analyzer because the external AI API was unavailable.
"""


def analyze_text(text):
    """
    Sends text to GPT-4o and returns summary, keywords, and classification.
    If the API is unavailable, it uses a local fallback analyzer.
    """

    if not text or not text.strip():
        raise ValueError("Text cannot be empty.")

    prompt = f"""
Analyze the following text and return the result in this exact format:

Summary:
Write a 3-5 sentence summary.

Keywords:
List 5-8 important keywords separated by commas.

Classification:
Choose only one category: educational, technical, or general.

Text:
{text}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI text analysis assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception:
        return fallback_analyze_text(text)