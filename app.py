"""Hayyak home and quiz page.

Run with:
    streamlit run app.py
"""

import re
import html

import streamlit as st

from src.ai_helper import generate_ai_explanation
from src.recommender import (
    COMMUTE_OPTIONS,
    HOUSEHOLD_OPTIONS,
    LIFESTYLE_OPTIONS,
    METRO_OPTIONS,
    PRIORITY_OPTIONS,
    score_neighbourhoods,
)
from src.ui import apply_hayyak_theme, arabic_divider, get_image_data_uri, render_nav


st.set_page_config(
    page_title="Hayyak | Dubai neighbourhood matching",
    page_icon="🏡",
    layout="wide",
)

@st.dialog("Your Hayyak relocation brief")
def show_ai_result_modal(ai_text):
    st.markdown("""
        <style>
        [data-testid="stDialog"] * { color: white !important; }
        [data-testid="stDialog"] { background: #2B1B14 !important; }
        [data-testid="stDialog"] > div { background: #2B1B14 !important; }
        </style>
    """, unsafe_allow_html=True)
    
    st.caption("Based on your quiz preferences and neighbourhood matches.")
    ...

apply_hayyak_theme()

st.markdown(
    """
    <style>
    header[data-testid="stHeader"] {
        display: none !important;
    }
    #MainMenu {
        visibility: hidden !important;
    }
    footer {
        visibility: hidden !important;
    }
    .block-container {
        padding-top: 1rem !important;
    }

/* Give the slider the same boxed look as other inputs */
    div.stSlider {
        border: 1px solid #e0d6c8 !important;
        border-radius: 0.5rem !important;
        padding: 0.75rem 1rem 0.25rem 1rem !important;
        margin-bottom: 1rem !important;
        background: #fff9f0 !important;
    }

    /* Make label and value text match the default color */
    div.stSlider label,
    div.stSlider .stSliderValue {
        color: #333 !important;
    }

    /* Optional: accent color for thumb/track */
    div.stSlider .stSliderTrack {
        background-color: #0066cc !important;
    }
    div.stSlider .stSliderThumb {
        background-color: #0066cc !important;
    }
    /* Force background on the slider's outer container */
    div.stSlider > div {
        background: #fff9f0 !important;
        border-radius: 0.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

render_nav(active="home")


@st.dialog("Your Hayyak relocation brief")
def show_ai_result_modal(ai_text):
    st.caption("Based on your quiz preferences and neighbourhood matches.")
    arabic_divider()

    if isinstance(ai_text, dict):
        if ai_text.get("ok"):
            st.success(
                f"Generated with Groq in {ai_text.get('latency_seconds', 'N/A')} seconds."
            )
        else:
            st.warning("Showing fallback guidance because the AI response was unavailable.")

        st.write(ai_text.get("message", "No explanation was generated."))
    else:
        st.write(ai_text)

    st.caption(
        "Note: Always verify official housing, tenancy, visa, and utility setup details "
        "through the relevant UAE or Dubai authority."
    )


def clean_text(value):
    """Remove accidental HTML tags and keep safe plain text."""
    value = "" if value is None else str(value)
    value = re.sub(r"<[^>]+>", "", value)
    return html.escape(value.strip())


# ---------------- HERO IMAGE ----------------

hero_uri = get_image_data_uri("assets/hayyak-main-trans.png")

if hero_uri:
    st.markdown(
        f"""
        <div class="hero-image-container">
            <img src="{hero_uri}" alt="Hayyak – your neighbourhood, perfectly matched" />
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.warning("Hero image not found. Please ensure assets/hayyak-main-trans.png exists.")


# ---------------- QUIZ ----------------

st.markdown(
    """
    <div class="section-card">
        <div class="section-heading">
            <div>
                <h2>Find your Dubai neighbourhood</h2>
                <p>Answer a few questions so Hayyak can understand your relocation style.</p>
            </div>
        </div>
    """,
    unsafe_allow_html=True,
)

with st.form("hayyak_quiz"):
    col1, col2 = st.columns(2)

    with col1:
        monthly_budget_aed = st.slider(
            "Monthly rent budget in AED",
            min_value=3000,
            max_value=25000,
            value=7500,
            step=500,
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

    with col2:
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

    submitted = st.form_submit_button("Find my neighbourhoods")


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


# ---------------- RESULTS ----------------
# ---------- RESULTS (replace everything from "if 'recommendations' in st.session_state:" onwards) ----------

if "recommendations" in st.session_state:
    profile = st.session_state["user_profile"]
    recommendations = st.session_state["recommendations"]

    st.markdown(
        """
        <div class="section-card">
            <div class="section-heading">
                <div>
                    <h2>Your top neighbourhood matches</h2>
                    <p>These are your strongest matches based on your quiz profile.</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    for rank, rec in enumerate(recommendations, start=1):
        reasons = rec.get("reasons", [])
        cautions = rec.get("cautions", [])

        reasons_html = "".join(
            f"<li>{clean_text(reason).capitalize()}.</li>" for reason in reasons[:3]
        ) or "<li>This area is a possible match, but more detail would improve the recommendation.</li>"

        cautions_html = "".join(
            f"<li>{clean_text(caution).capitalize()}.</li>" for caution in cautions[:2]
        )

        caution_block = ""
        if cautions_html:
            caution_block = f"""
            <p style="margin:.7rem 0 .25rem 0;"><strong>Cautions</strong></p>
            <ul>{cautions_html}</ul>
            """

        raw_downside = rec.get("downside", "")
        downside_text = clean_text(raw_downside)
        downside_text = downside_text.replace("Possible downside:", "").strip()

        card_html = f"""
        <div class="result-card">
            <div class="result-topline">
                <h3 class="result-title">{rank}. {clean_text(rec.get("name", ""))}</h3>
                <span class="match-pill">{clean_text(rec.get("match_percent", ""))}% match</span>
            </div>

            <p class="muted-text">{clean_text(rec.get("summary", ""))}</p>

            <p style="margin:.7rem 0 .25rem 0;"><strong>Why it fits</strong></p>
            <ul>{reasons_html}</ul>

            {caution_block}

            <p><strong>Possible downside:</strong> {downside_text}</p>
        </div>
        """

        # Use st.html if available (Streamlit >= 1.36), otherwise fallback to markdown
        if hasattr(st, "html"):
            st.html(card_html)
        else:
            st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    col_a, col_b = st.columns([1, 2])

    with col_a:
        if st.button("Generate relocation brief", key="generate_relocation_brief"):
            with st.spinner("Preparing your Hayyak relocation brief..."):
                ai_response = generate_ai_explanation(profile, recommendations)

            show_ai_result_modal(ai_response)

else:
    st.info("Complete the quiz to generate your first neighbourhood matches.")
