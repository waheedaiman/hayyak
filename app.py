"""Hayyak quiz app.

Run with:
    streamlit run app.py
"""

import streamlit as st

from src.recommender import (
    COMMUTE_OPTIONS,
    HOUSEHOLD_OPTIONS,
    LIFESTYLE_OPTIONS,
    METRO_OPTIONS,
    PRIORITY_OPTIONS,
    build_llm_context,
    score_neighbourhoods,
)


st.set_page_config(
    page_title="Hayyak - Dubai relocation quiz",
    page_icon="🏙️",
    layout="centered",
)

st.title("Hayyak")
st.subheader("Dubai relocation quiz")
st.write(
    "Answer a few questions and Hayyak will suggest the top 3 neighbourhoods "
    "to consider for your move."
)

with st.form("hayyak_quiz"):
    monthly_budget_aed = st.slider(
        "Monthly rent budget in AED",
        min_value=3000,
        max_value=25000,
        value=7500,
        step=500,
        help="Use an approximate monthly rent budget. This is only for early matching logic.",
    )

    commute_target = st.selectbox(
        "Where will you commute most often?",
        COMMUTE_OPTIONS,
    )

    lifestyle = st.radio(
        "What kind of area do you prefer?",
        LIFESTYLE_OPTIONS,
        horizontal=True,
    )

    household_type = st.selectbox(
        "Who are you moving as?",
        HOUSEHOLD_OPTIONS,
    )

    needs_metro = st.radio(
        "Do you need metro access?",
        METRO_OPTIONS,
        index=1,
        horizontal=True,
    )

    priority = st.selectbox(
        "What matters most to you?",
        PRIORITY_OPTIONS,
    )

    submitted = st.form_submit_button("Find my top 3 neighbourhoods")

if submitted:
    user_profile = {
        "monthly_budget_aed": monthly_budget_aed,
        "commute_target": commute_target,
        "lifestyle": lifestyle,
        "household_type": household_type,
        "needs_metro": needs_metro,
        "priority": priority,
    }

    st.session_state["user_profile"] = user_profile
    st.session_state["recommendations"] = score_neighbourhoods(user_profile)

if "recommendations" in st.session_state:
    profile = st.session_state["user_profile"]
    recommendations = st.session_state["recommendations"]

    st.divider()
    st.subheader("Your top 3 neighbourhood matches")

    for rank, rec in enumerate(recommendations, start=1):
        with st.expander(
            f"{rank}. {rec['name']} - {rec['match_percent']}% match",
            expanded=True,
        ):
            st.progress(rec["match_percent"] / 100)
            st.write(rec["summary"])

            st.markdown("**Why it fits:**")
            if rec["reasons"]:
                for reason in rec["reasons"]:
                    st.markdown(f"- {reason.capitalize()}.")
            else:
                st.markdown("- This area is a possible match, but it needs more user details.")

            if rec["cautions"]:
                st.markdown("**Cautions:**")
                for caution in rec["cautions"]:
                    st.markdown(f"- {caution.capitalize()}.")

            st.markdown(f"**Possible downside:** {rec['downside']}")

            st.markdown("**First move-in steps:**")
            for step in rec["first_steps"]:
                st.markdown(f"- {step}")

    st.divider()
    st.subheader("Developer output for the future Groq prompt")
    st.caption(
        "This text can later be passed to the Groq API so the chatbot can explain the results more naturally."
    )
    st.code(build_llm_context(profile, recommendations), language="markdown")
else:
    st.info("Complete the quiz above to generate your first recommendation results.")
