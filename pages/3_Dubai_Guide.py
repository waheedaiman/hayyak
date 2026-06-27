import streamlit as st
import streamlit.components.v1 as components
import os

# Hide Streamlit chrome
st.markdown(
    """
    <style>
        [data-testid="stToolbar"]  { display: none !important; }
        footer                     { display: none !important; }
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

# Load HTML — path goes up one level from pages/ to root, then into assets/
html_path = os.path.join(os.path.dirname(__file__), "..", "assets", "hayyak_visa_entry.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=980, scrolling=True)