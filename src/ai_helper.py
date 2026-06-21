import os
from groq import Groq


def get_groq_client():
    """
    Creates a Groq client using the GROQ_API_KEY environment variable.
    The API key should never be hardcoded in the code.
    """
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    return Groq(api_key=api_key)


def build_relocation_prompt(user_profile, top_recommendations):
    """
    Builds the prompt that will be sent to Groq.
    """

    profile_text = f"""
Budget: AED {user_profile.get("budget")}
Workplace/University Area: {user_profile.get("workplace")}
Lifestyle Preference: {user_profile.get("lifestyle")}
Household Type: {user_profile.get("household_type")}
Needs Metro Access: {user_profile.get("needs_metro")}
Main Priority: {user_profile.get("priority")}
"""

    recommendations_text = ""

    for index, area in enumerate(top_recommendations, start=1):
        recommendations_text += f"""
{index}. {area["name"]}
Match Score: {area["score"]}
Why it matched: {area["match_reason"]}
Possible downside: {area["downside"]}
"""

    prompt = f"""
You are Hayyak, an AI relocation assistant for people moving to Dubai.

Your job is to explain neighbourhood recommendations in a practical, beginner-friendly way.

Use the user's profile and the scored neighbourhood results provided below.
Do not invent official legal, visa, rent, or government information.
If something requires official confirmation, tell the user to verify it with the relevant official Dubai/UAE source.

User profile:
{profile_text}

Top neighbourhood recommendations:
{recommendations_text}

Generate:
1. A short summary of the user's relocation profile
2. A clear explanation of the top 3 neighbourhoods
3. Why each area fits
4. One possible downside for each area
5. A personalised first-week move-in checklist
6. One follow-up question that would improve the recommendation

Keep the tone helpful, clear, and concise.
"""

    return prompt


def generate_ai_explanation(user_profile, top_recommendations):
    """
    Sends the relocation prompt to Groq and returns the AI-generated explanation.
    """

    client = get_groq_client()

    if client is None:
        return (
            "Groq API key is not configured yet. "
            "Set GROQ_API_KEY as an environment variable to enable AI explanations."
        )

    prompt = build_relocation_prompt(user_profile, top_recommendations)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are Hayyak, a Dubai relocation assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.4,
        max_tokens=900,
    )

    return response.choices[0].message.content
