import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
        /* Hide Streamlit's own sidebar completely */
        [data-testid="stSidebar"]        { display: none !important; }
        [data-testid="stSidebarNav"]     { display: none !important; }
        [data-testid="collapsedControl"] { display: none !important; }
        [data-testid="stToolbar"]        { display: none !important; }
        [data-testid="stHeader"]         { display: none !important; }
        footer                           { display: none !important; }

        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        .stApp { background: #F7F3EE; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = os.path.join(os.path.dirname(__file__), "..", "assets", "hayyak_visa_entry.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1200, scrolling=True)