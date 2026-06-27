"""Hayyak home and quiz page.

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
    score_neighbourhoods,
)
from src.ui import apply_hayyak_theme, arabic_divider, get_image_data_uri, render_nav


st.set_page_config(
    page_title="Hayyak | Dubai neighbourhood matching",
    page_icon="🏡",
    layout="wide",
)

st.set_page_config(
    page_title="Hayyak | Dubai neighbourhood matching",
    page_icon="🏡",
    layout="wide",
)

apply_hayyak_theme()

st.markdown("""
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

/* Pull nav background rectangle down */
.nav-shell,
.nav-container,
.nav-wrap,
.hayyak-nav,
.navbar {
    margin-top: 0 !important;
    transform: translateY(38px) !important;
}

.block-container {
    padding-top: 1rem !important;
}
</style>
""", unsafe_allow_html=True)

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

st.markdown("</div>", unsafe_allow_html=True)


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
            [f"<li>{reason.capitalize()}.</li>" for reason in reasons[:3]]
        ) or "<li>This area is a possible match, but more detail would improve the recommendation.</li>"

        cautions_html = "".join(
            [f"<li>{caution.capitalize()}.</li>" for caution in cautions[:2]]
        )

        caution_block = ""
        if cautions_html:
            caution_block = f"""
            <p style="margin:.7rem 0 .25rem 0;"><strong>Cautions</strong></p>
            <ul>{cautions_html}</ul>
            """

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-topline">
                    <h3 class="result-title">{rank}. {rec.get("name")}</h3>
                    <span class="match-pill">{rec.get("match_percent")}% match</span>
                </div>
                <p class="muted-text">{rec.get("summary")}</p>
                <p style="margin:.7rem 0 .25rem 0;"><strong>Why it fits</strong></p>
                <ul>{reasons_html}</ul>
                {caution_block}
                <p><strong>Possible downside:</strong> {rec.get("downside", "").replace("<p>", "").replace("</p>", "").replace("<strong>Possible downside:</strong>", "").strip()}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    col_a, col_b = st.columns([1, 2])

    with col_a:
        if st.button("Generate relocation brief"):
            with st.spinner("Preparing your Hayyak relocation brief..."):
                ai_response = generate_ai_explanation(profile, recommendations)

            show_ai_result_modal(ai_response)

    with col_b:
        st.caption(
            "The relocation brief opens as a modal so users do not need to scroll away from their results."
        )

else:
    st.info("Complete the quiz to generate your first neighbourhood matches.")
