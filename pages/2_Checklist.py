import streamlit as st

from src.ui import apply_hayyak_theme, render_nav


st.set_page_config(
    page_title="Hayyak | Dubai Checklist",
    page_icon="✅",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="checklist")


st.markdown(
    """
    <section class="hero-shell">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">Relocation planning</div>
                <h1 class="hero-title">Dubai Checklist</h1>
                <p class="hero-copy">
                    A simple checklist structure for users to track what they need
                    before arrival, during move-in, and after settling.
                </p>
            </div>
            <div class="brand-card">
                <h3 style="color:#642A16;">Coming soon</h3>
                <p class="muted-text">
                    Later this can become personalised based on the quiz result.
                </p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("Checklist preview")

tabs = st.tabs(["Before arrival", "First week", "First month"])

with tabs[0]:
    st.checkbox("Shortlist neighbourhoods")
    st.checkbox("Estimate rent and deposit budget")
    st.checkbox("Prepare identity and visa documents")
    st.checkbox("Research commute options")

with tabs[1]:
    st.checkbox("Inspect apartment before signing")
    st.checkbox("Confirm Ejari process")
    st.checkbox("Start DEWA setup")
    st.checkbox("Arrange mobile and internet")

with tabs[2]:
    st.checkbox("Explore local supermarkets and clinics")
    st.checkbox("Save emergency and building contacts")
    st.checkbox("Review commute routine")
    st.checkbox("Update documents and account details")

st.markdown("</div>", unsafe_allow_html=True)
