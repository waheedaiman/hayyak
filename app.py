"""Hayyak quiz app.

Run with:
    streamlit run app.py
"""

import streamlit as st

from src.ai_helper import generate_ai_explanation
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

st.markdown(
    """
    <style>
    .top-navbar {
        position: sticky;
        top: 0;
        z-index: 999;
        margin: -1rem auto 2rem auto;
        padding: 0.75rem 1rem;
        max-width: 950px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.10);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.18);
    }

    .top-navbar-inner {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        flex-wrap: wrap;
    }

    .brand {
        font-weight: 800;
        font-size: 1.05rem;
        letter-spacing: 0.02em;
        color: #ffffff;
        white-space: nowrap;
    }

    .nav-links {
        display: flex;
        align-items: center;
        gap: 0.35rem;
        flex-wrap: wrap;
    }

    .nav-link {
        text-decoration: none !important;
        color: rgba(255, 255, 255, 0.86) !important;
        font-size: 0.88rem;
        padding: 0.45rem 0.75rem;
        border-radius: 999px;
        transition: all 0.2s ease;
    }

    .nav-link:hover {
        background: rgba(255, 255, 255, 0.16);
        color: #ffffff !important;
    }

    .nav-cta {
        background: linear-gradient(135deg, #ff9f43, #ff7a45);
        color: #ffffff !important;
        font-weight: 700;
    }

    .nav-cta:hover {
        background: linear-gradient(135deg, #ffb366, #ff8c5a);
    }

    @media (max-width: 700px) {
        .top-navbar {
            border-radius: 24px;
        }

        .top-navbar-inner {
            align-items: flex-start;
        }

        .nav-links {
            width: 100%;
        }
    }
    </style>

    <div class="top-navbar">
        <div class="top-navbar-inner">
            <div class="brand">Hayyak</div>
            <div class="nav-links">
                <a class="nav-link" href="#home-profile">Home / Profile</a>
                <a class="nav-link" href="#quiz">Quiz</a>
                <a class="nav-link" href="#ai-chatbot">AI Chatbot</a>
                <a class="nav-link" href="#utilities">Utilities</a>
                <a class="nav-link" href="#checklist">Checklist</a>
                <a class="nav-link nav-cta" href="#dubai-guide">Dubai Guide</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div id="home-profile"></div>', unsafe_allow_html=True)
st.title("Hayyak")
st.subheader("Dubai relocation assistant")

st.markdown('<div id="quiz"></div>', unsafe_allow_html=True)
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
    st.markdown('<div id="ai-chatbot"></div>', unsafe_allow_html=True)
    st.subheader("AI Relocation Explanation")    st.caption(
        "Generate a more natural explanation and checklist using Groq. "
        "This requires GROQ_API_KEY to be set in your environment."
    )

    if st.button("Generate AI Explanation"):
        with st.spinner("Hayyak is preparing your relocation explanation..."):
            ai_response = generate_ai_explanation(profile, recommendations)

        if ai_response["ok"]:
            st.success(
                f"AI explanation generated with Groq in "
                f"{ai_response['latency_seconds']} seconds."
            )
        else:
            st.warning("Using fallback explanation because the Groq API response was unavailable.")

        st.write(ai_response["message"])

        st.markdown("**Was this explanation useful?**")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("👍 Useful"):
                st.session_state["ai_feedback"] = "useful"
                st.success("Thanks for the feedback.")

        with col2:
            if st.button("👎 Needs improvement"):
                st.session_state["ai_feedback"] = "needs_improvement"
                st.info("Thanks. This will help improve Hayyak's recommendations.")

    st.divider()
    st.subheader("Developer output for the future Groq prompt")
    st.caption(
        "This text can later be passed to the Groq API so the chatbot can explain the results more naturally."
    )
    st.code(build_llm_context(profile, recommendations), language="markdown")

else:
    st.info("Complete the quiz above to generate your first recommendation results.")

st.divider()

st.markdown('<div id="utilities"></div>', unsafe_allow_html=True)
st.subheader("Utilities")
st.write("Coming next: DEWA, Ejari, e&, du, internet setup, and move-in service guidance.")

st.markdown('<div id="checklist"></div>', unsafe_allow_html=True)
st.subheader("Checklist")
st.write("Coming next: a personalised relocation checklist based on your quiz answers.")

st.markdown('<div id="dubai-guide"></div>', unsafe_allow_html=True)
st.subheader("Dubai Guide")
st.write("Coming next: an A–Z guide for moving to Dubai, from pre-arrival planning to first-month setup.")
