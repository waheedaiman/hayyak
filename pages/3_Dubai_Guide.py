import os
import streamlit as st
import streamlit.components.v1 as components

from src.ui import apply_hayyak_theme, render_nav


st.set_page_config(
    page_title="Hayyak | Dubai Guide",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_hayyak_theme()

st.markdown(
    """
    <style>
        /* Hide Streamlit default UI */
        [data-testid="stSidebar"]        { display: none !important; }
        [data-testid="stSidebarNav"]     { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        [data-testid="stToolbar"]        { display: none !important; }
        [data-testid="stHeader"]         { display: none !important; }
        #MainMenu                        { visibility: hidden !important; }
        footer                           { display: none !important; }

        /* Keep page clean but allow navbar spacing */
        .block-container {
            max-width: 100% !important;
            padding-top: 1rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            padding-bottom: 0 !important;
        }

        .stApp {
            background: #F7F3EE !important;
        }

        /* Make the embedded guide sit neatly under the nav */
        iframe {
            border: none !important;
            border-radius: 22px !important;
            background: #F7F3EE !important;
        }

        div[data-testid="stIFrame"] {
            margin-top: 0.5rem !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

render_nav(active="guide")

html_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "assets",
    "hayyak_visa_entry.html",
)

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1200, scrolling=True)