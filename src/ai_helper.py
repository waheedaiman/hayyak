import os
import time

from groq import Groq


def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    return Groq(api_key=api_key)


def build_relocation_prompt(user_profile, top_recommendations):
    profile_text = f"""
Monthly budget: AED {user_profile.get("monthly_budget_aed")}
Commute target: {user_profile.get("commute_target")}
Lifestyle preference: {user_profile.get("lifestyle")}
Household type: {user_profile.get("household_type")}
Needs metro access: {user_profile.get("needs_metro")}
Main priority: {user_profile.get("priority")}
"""

    recommendations_text = ""

    for index, area in enumerate(top_recommendations, start=1):
        reasons = area.get("reasons", [])
        cautions = area.get("cautions", [])
        first_steps = area.get("first_steps", [])

        reasons_text = "\n".join([f"- {reason}" for reason in reasons]) or "- No specific reasons listed."
        cautions_text = "\n".join([f"- {caution}" for caution in cautions]) or "- No cautions listed."
        steps_text = "\n".join([f"- {step}" for step in first_steps]) or "- No first steps listed."

        recommendations_text += f"""
{index}. {area.get("name", "Unknown area")}
Match percentage: {area.get("match_percent", "N/A")}%
Summary: {area.get("summary", "No summary provided.")}
Why it fits:
{reasons_text}
Cautions:
{cautions_text}
Possible downside: {area.get("downside", "No downside listed.")}
First move-in steps:
{steps_text}
"""

    prompt = f"""
You are Hayyak, an AI relocation assistant for people moving to Dubai.

Your job is to explain neighbourhood recommendations in a practical, beginner-friendly way.

Use only the user's profile and the scored neighbourhood results provided below.
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


def build_fallback_explanation(user_profile, top_recommendations):
    lines = []

    lines.append("Hayyak could not reach the AI explanation service right now, so here is a basic fallback summary.\n")
    lines.append(
        f"Your profile suggests a budget of around AED {user_profile.get('monthly_budget_aed')} "
        f"with commute focus around {user_profile.get('commute_target')}."
    )

    lines.append("\nTop neighbourhood matches:")

    for index, area in enumerate(top_recommendations, start=1):
        lines.append(f"\n{index}. {area.get('name', 'Unknown area')} - {area.get('match_percent', 'N/A')}% match")
        lines.append(area.get("summary", "No summary available."))

        reasons = area.get("reasons", [])
        if reasons:
            lines.append("Why it fits:")
            for reason in reasons[:3]:
                lines.append(f"- {reason.capitalize()}.")

        lines.append(f"Possible downside: {area.get('downside', 'No downside listed.')}")

    lines.append("\nFirst-week checklist:")
    lines.append("- Confirm your rental budget and shortlisted neighbourhoods.")
    lines.append("- Check commute time during peak hours.")
    lines.append("- Prepare documents for tenancy and Ejari.")
    lines.append("- Plan DEWA, internet, and mobile setup.")
    lines.append("- Visit shortlisted areas before signing.")

    return "\n".join(lines)


def generate_ai_explanation(user_profile, top_recommendations, max_retries=2):
    client = get_groq_client()

    if client is None:
        return {
            "ok": False,
            "source": "fallback",
            "message": (
                "Groq API key is not configured yet. "
                "Set GROQ_API_KEY as an environment variable to enable AI explanations."
            ),
        }

    prompt = build_relocation_prompt(user_profile, top_recommendations)

    last_error = None

    for attempt in range(max_retries + 1):
        try:
            start_time = time.time()

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

            latency = round(time.time() - start_time, 2)

            return {
                "ok": True,
                "source": "groq",
                "latency_seconds": latency,
                "message": response.choices[0].message.content,
            }

        except Exception as error:
            last_error = error
            time.sleep(1)

    fallback_message = build_fallback_explanation(user_profile, top_recommendations)

    return {
        "ok": False,
        "source": "fallback",
        "error": str(last_error),
        "message": fallback_message,
    }
