import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
        /* Remove the black top header bar */
        [data-testid="stHeader"]   { display: none !important; }
        [data-testid="stToolbar"]  { display: none !important; }
        footer                     { display: none !important; }

        /* Kill all padding around the iframe */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        [data-testid="stAppViewContainer"] > section {
            padding: 0 !important;
        }
        [data-testid="stAppViewContainer"] > section > div {
            padding: 0 !important;
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