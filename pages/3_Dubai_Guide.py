import streamlit as st

from src.ui import apply_hayyak_theme, render_nav


st.set_page_config(
    page_title="Hayyak | Dubai Guide",
    page_icon="🕌",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="guide")


st.markdown(
    """
    <section class="hero-shell">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">City guide</div>
                <h1 class="hero-title">Dubai Guide</h1>
                <p class="hero-copy">
                    A future A-Z guide for newcomers moving to Dubai, covering
                    neighbourhoods, commute, documents, utilities, and daily life.
                </p>
            </div>
            <div class="brand-card">
                <h3 style="color:#642A16;">Grounded guidance</h3>
                <p class="muted-text">
                    Designed to feel practical, local, and culturally aware.
                </p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("Guide structure preview")

st.markdown(
    """
    **1. Choosing where to live**  
    Budget, commute, metro access, lifestyle, and household needs.

    **2. Understanding rental basics**  
    Contracts, deposits, Ejari, and building/community checks.

    **3. Setting up essentials**  
    DEWA, mobile, internet, banking, and local services.

    **4. Settling into daily life**  
    Groceries, clinics, transport, delivery apps, and community routines.
    """
)

st.markdown("</div>", unsafe_allow_html=True)
