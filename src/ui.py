from pathlib import Path
import base64
import streamlit as st

PALETTE = {
    "deep_brown": "#642A16",
    "sand": "#B59275",
    "olive": "#8C8A67",
    "clay": "#BC8653",
    "terracotta": "#B27960",
    "cream": "#F6EFE5",
    "paper": "#FFF9F0",
    "ink": "#2B1B14",
}

def _image_to_data_uri(path):
    image_path = Path(path)
    if not image_path.exists():
        return None
    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    suffix = image_path.suffix.lower().replace(".", "")
    if suffix == "jpg":
        suffix = "jpeg"
    return f"data:image/{suffix};base64,{encoded}"

def get_image_data_uri(path):
    return _image_to_data_uri(path)

def apply_hayyak_theme():
    st.markdown(
        f"""
        <style>
        :root {{
            --deep-brown: #642A16;
            --olive: #8C8A67;
            --paper: #FFF9F0;
            --ink: #2B1B14;
        }}

        html, body, [data-testid="stAppViewContainer"] {{
            background: #F6EFE5 !important;
            color: var(--ink) !important;
        }}

        [data-testid="stSidebar"] {{ display: none !important; }}

        .block-container {{
            max-width: 1120px;
            padding-top: 1rem;
            padding-bottom: 2.5rem;
        }}

        /* NAVBAR */
        .hayyak-navbar {{
            position: sticky;
            top: 0.75rem;
            z-index: 999;
            width: 100%;
            margin-bottom: 0.85rem;
            padding: 0.52rem 0.7rem;
            border: 1px solid rgba(140, 138, 103, 0.28);
            border-radius: 999px;
            background: rgba(255, 249, 240, 0.90);
            box-shadow: 0 12px 28px rgba(100, 42, 22, 0.09);
            backdrop-filter: blur(12px);
        }}
        .hayyak-navbar-inner {{ display: flex; align-items: center; justify-content: space-between; gap: 1rem; }}
        .hayyak-brand {{ display: flex; align-items: center; min-width: 72px; }}
        .hayyak-logo {{ width: 54px; height: 54px; object-fit: contain; }}
        .hayyak-links {{ display: flex; align-items: center; gap: 0.35rem; flex-wrap: wrap; }}
        .hayyak-links a {{
            color: var(--deep-brown) !important;
            text-decoration: none !important;
            font-size: 0.88rem;
            padding: 0.46rem 0.78rem;
            border-radius: 999px;
            transition: 0.18s ease;
        }}
        .hayyak-links a:hover {{ background: rgba(140, 138, 103, 0.14); }}
        .hayyak-links a.active {{ background: var(--olive); color: white !important; }}

        /* HERO IMAGE – no shadow, no border */
        .hero-image-container {{
            width: 100%;
            max-width: 980px;
            margin: 0 auto 1.2rem auto;
            text-align: center;
            animation: fadeIn 1s ease-out both;
        }}
        .hero-image-container img {{
            width: 100%;
            height: auto;
            max-height: 400px;
            object-fit: contain;
            display: block;
            box-shadow: none !important;   /* removed */
            border-radius: 0 !important;    /* removed */
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(8px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* SECTION CARDS */
        .section-card {{
            border: 1px solid rgba(140, 138, 103, 0.24);
            border-radius: 28px;
            background: rgba(255, 249, 240, 0.91);
            box-shadow: 0 16px 38px rgba(100, 42, 22, 0.075);
            padding: 1.25rem;
            margin: 0.45rem 0 1rem 0;
        }}
        .section-heading {{ display: flex; justify-content: space-between; gap: 1rem; align-items: flex-end; margin-bottom: 0.85rem; }}
        .section-heading h2 {{ margin: 0; font-size: 1.55rem; color: var(--deep-brown); }}
        .section-heading p {{ margin: 0.3rem 0 0 0; color: #735A4C; }}

        .result-card {{
            border: 1px solid rgba(140, 138, 103, 0.24);
            background: #FFF9F0;
            border-radius: 22px;
            padding: 1rem;
            margin-bottom: 0.8rem;
        }}
        .result-topline {{ display: flex; justify-content: space-between; align-items: center; gap: 1rem; }}
        .result-title {{ color: var(--deep-brown); font-size: 1.15rem; font-weight: 800; margin: 0; }}
        .match-pill {{
            background: rgba(140, 138, 103, 0.14);
            color: var(--olive);
            border: 1px solid rgba(140, 138, 103, 0.36);
            border-radius: 999px;
            padding: 0.35rem 0.65rem;
            font-size: 0.82rem;
            font-weight: 800;
            white-space: nowrap;
        }}
        .muted-text {{ color: #735A4C; }}

        /* CUSTOM SLIDER WRAPPER */
        .custom-slider-wrapper {{
            background: rgba(255, 249, 240, 0.76);
            border: 1px solid rgba(140, 138, 103, 0.18);
            border-radius: 18px;
            padding: 0.85rem 0.9rem;
            margin-bottom: 0.75rem;
        }}
        .custom-slider-wrapper label {{
            color: var(--deep-brown) !important;
            font-weight: 800 !important;
            display: block;
            margin-bottom: 0.4rem;
        }}
        .custom-slider-wrapper input[type="range"] {{
            width: 100%;
            height: 6px;
            background: var(--olive);
            border-radius: 3px;
            outline: none;
            -webkit-appearance: none;
        }}
        .custom-slider-wrapper input[type="range"]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--deep-brown);
            cursor: pointer;
            border: 2px solid var(--paper);
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }}
        .custom-slider-wrapper input[type="range"]::-moz-range-thumb {{
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--deep-brown);
            cursor: pointer;
            border: 2px solid var(--paper);
        }}
        /* Hide the Streamlit text input for the slider value */
        div[data-testid="stTextInput"] {{
            display: none !important;
        }}

        /* OTHER WIDGETS (select, radio, buttons) – same as before */
        div[data-testid="stSelectbox"],
        div[data-testid="stRadio"] {{
            background: rgba(255, 249, 240, 0.76) !important;
            border: 1px solid rgba(140, 138, 103, 0.18) !important;
            border-radius: 18px !important;
            padding: 0.85rem 0.9rem !important;
            margin-bottom: 0.75rem !important;
        }}

        div[data-testid="stSelectbox"] label,
        div[data-testid="stRadio"] label {{
            color: var(--deep-brown) !important;
            font-weight: 800 !important;
        }}

        input[type="radio"] {{
            accent-color: var(--olive) !important;
        }}
        div[role="radiogroup"] label {{
            background: rgba(140, 138, 103, 0.09) !important;
            border: 1px solid rgba(140, 138, 103, 0.18) !important;
            border-radius: 999px !important;
            padding: 0.38rem 0.68rem !important;
            margin-right: 0.25rem !important;
            color: var(--ink) !important;
        }}
        div[role="radiogroup"] label:hover {{
            background: rgba(140, 138, 103, 0.16) !important;
        }}

        /* SELECTBOX */
        div[data-baseweb="select"] > div {{
            background-color: #FFF9F0 !important;
            border-color: rgba(140, 138, 103, 0.35) !important;
            border-radius: 999px !important;
            color: var(--ink) !important;
            box-shadow: none !important;
        }}
        div[data-baseweb="select"] span {{ color: var(--ink) !important; }}
        div[data-baseweb="popover"] div[role="listbox"] {{
            background-color: #FFF9F0 !important;
            border: 1px solid rgba(140, 138, 103, 0.24) !important;
            border-radius: 16px !important;
        }}
        div[data-baseweb="popover"] div[role="option"] {{
            background-color: #FFF9F0 !important;
            color: var(--ink) !important;
        }}
        div[data-baseweb="popover"] div[role="option"]:hover {{
            background-color: rgba(140, 138, 103, 0.14) !important;
        }}

        /* BUTTONS */
        div[data-testid="stButton"] > button,
        div[data-testid="stFormSubmitButton"] > button {{
            background: var(--olive) !important;
            color: white !important;
            border: 1px solid var(--olive) !important;
            border-radius: 999px !important;
            padding: 0.65rem 1.15rem !important;
            font-weight: 800 !important;
            transition: 0.18s ease !important;
        }}
        div[data-testid="stButton"] > button:hover,
        div[data-testid="stFormSubmitButton"] > button:hover {{
            background: #6F7A52 !important;
            border-color: #6F7A52 !important;
            transform: translateY(-1px);
        }}

        /* MODAL */
        [data-testid="stDialog"] {{
            z-index: 1000 !important;
        }}
        [data-testid="stDialog"]::backdrop {{
            background: rgba(0, 0, 0, 0.4) !important;
        }}
        [data-testid="stDialog"] > div {{
            background: rgba(255, 249, 240, 0.98) !important;
            backdrop-filter: blur(4px);
            border-radius: 28px !important;
            border: 1px solid rgba(140, 138, 103, 0.24) !important;
            box-shadow: 0 20px 48px rgba(100, 42, 22, 0.15) !important;
            color: var(--ink) !important;
        }}
        [data-testid="stDialog"] * {{
            color: var(--ink) !important;
        }}
        [data-testid="stDialog"] h1,
        [data-testid="stDialog"] h2,
        [data-testid="stDialog"] h3,
        [data-testid="stDialog"] h4,
        [data-testid="stDialog"] h5,
        [data-testid="stDialog"] h6 {{
            color: var(--deep-brown) !important;
        }}
        [data-testid="stDialog"] p {{
            color: var(--ink) !important;
        }}
        [data-testid="stDialog"] [data-testid="stCaption"] {{
            color: #735A4C !important;
        }}
        [data-testid="stDialog"] [data-testid="stSuccess"] {{
            background: rgba(140, 138, 103, 0.12) !important;
            border: 1px solid rgba(140, 138, 103, 0.24) !important;
            color: var(--deep-brown) !important;
        }}
        [data-testid="stDialog"] [data-testid="stWarning"] {{
            background: rgba(178, 121, 96, 0.12) !important;
            border: 1px solid rgba(178, 121, 96, 0.24) !important;
            color: var(--deep-brown) !important;
        }}

        /* ALERTS */
        div[data-testid="stAlert"] {{
            background: rgba(140, 138, 103, 0.12) !important;
            border: 1px solid rgba(140, 138, 103, 0.24) !important;
            color: var(--deep-brown) !important;
        }}

        @media (max-width: 820px) {{
            .hayyak-navbar {{ border-radius: 24px; position: relative; top: 0; }}
            .hayyak-navbar-inner {{ flex-direction: column; align-items: flex-start; }}
            .hero-image-container img {{ max-height: 250px; }}
            .section-card {{ padding: 1rem; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

def render_nav(active="home"):
    logo_uri = _image_to_data_uri("assets/hayyak-logo.png")
    if logo_uri:
        brand_html = f'<img class="hayyak-logo" src="{logo_uri}" alt="Hayyak logo" />'
    else:
        brand_html = '<div class="hayyak-logo-fallback">H</div>'

    links = [
        ("home", "Home / Quiz", "/"),
        ("utilities", "Utilities", "/Utilities"),
        ("checklist", "Dubai Checklist", "/Checklist"),
        ("guide", "Dubai Guide", "/Dubai_Guide"),
    ]

    link_html = "".join(
        f'<a class="{"active" if active == key else ""}" href="{href}">{label}</a>'
        for key, label, href in links
    )

    st.markdown(
        f"""
        <div class="hayyak-navbar">
            <div class="hayyak-navbar-inner">
                <div class="hayyak-brand">{brand_html}</div>
                <div class="hayyak-links">{link_html}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def arabic_divider():
    st.markdown('<div class="arabic-divider"></div>', unsafe_allow_html=True)
