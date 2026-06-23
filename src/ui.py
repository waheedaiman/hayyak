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


def apply_hayyak_theme():
    st.markdown(
        """
        <style>
        :root {
            --deep-brown: #642A16;
            --sand: #B59275;
            --olive: #8C8A67;
            --clay: #BC8653;
            --terracotta: #B27960;
            --cream: #F6EFE5;
            --paper: #FFF9F0;
            --ink: #2B1B14;
            --muted: #735A4C;
            --line: rgba(100, 42, 22, 0.16);
            --green-soft: rgba(140, 138, 103, 0.14);
            --green-line: rgba(140, 138, 103, 0.36);
        }

        html, body, [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at top left, rgba(140, 138, 103, 0.16), transparent 30%),
                radial-gradient(circle at top right, rgba(188, 134, 83, 0.11), transparent 28%),
                linear-gradient(180deg, #F6EFE5 0%, #EFE1D1 100%);
            color: var(--ink);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stSidebar"] {
            display: none;
        }

        .block-container {
            max-width: 1120px;
            padding-top: 1.1rem;
            padding-bottom: 2.5rem;
        }

        h1, h2, h3 {
            color: var(--deep-brown);
            letter-spacing: -0.035em;
        }

        p, label, span, div {
            color: var(--ink);
        }

        /* NAVBAR */

        .hayyak-navbar {
            position: sticky;
            top: 0.75rem;
            z-index: 999;
            width: 100%;
            margin-bottom: 1.05rem;
            padding: 0.55rem 0.7rem;
            border: 1px solid rgba(140, 138, 103, 0.28);
            border-radius: 999px;
            background: rgba(255, 249, 240, 0.90);
            box-shadow: 0 12px 28px rgba(100, 42, 22, 0.09);
            backdrop-filter: blur(12px);
        }

        .hayyak-navbar-inner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }

        .hayyak-brand {
            display: flex;
            align-items: center;
            min-width: 72px;
        }

        .hayyak-logo {
            width: 54px;
            height: 54px;
            object-fit: contain;
            display: block;
        }

        .hayyak-logo-fallback {
            width: 42px;
            height: 42px;
            border-radius: 999px;
            background: var(--deep-brown);
            color: var(--paper);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
        }

        .hayyak-links {
            display: flex;
            align-items: center;
            gap: 0.35rem;
            flex-wrap: wrap;
        }

        .hayyak-links a {
            color: var(--deep-brown) !important;
            text-decoration: none !important;
            font-size: 0.88rem;
            padding: 0.46rem 0.78rem;
            border-radius: 999px;
            transition: 0.18s ease;
        }

        .hayyak-links a:hover {
            background: var(--green-soft);
            color: var(--deep-brown) !important;
        }

        .hayyak-links a.active {
            background: var(--olive);
            color: var(--paper) !important;
        }

        /* HERO */

        .hero-shell {
            border: 1px solid rgba(140, 138, 103, 0.25);
            border-radius: 32px;
            background:
                linear-gradient(135deg, rgba(255, 249, 240, 0.96), rgba(239, 225, 209, 0.78));
            box-shadow: 0 22px 52px rgba(100, 42, 22, 0.10);
            padding: 1.65rem;
            margin-bottom: 0.65rem;
            overflow: hidden;
            position: relative;
        }

        .hero-shell:before {
            content: "حيّاك";
            position: absolute;
            right: 1.7rem;
            top: 0.45rem;
            font-size: 5.1rem;
            color: rgba(140, 138, 103, 0.075);
            font-weight: 800;
            line-height: 1;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: minmax(0, 1.15fr) minmax(260px, 0.85fr);
            gap: 1.2rem;
            align-items: center;
        }

        .eyebrow {
            display: inline-flex;
            width: fit-content;
            align-items: center;
            gap: 0.45rem;
            border: 1px solid var(--green-line);
            background: var(--green-soft);
            color: var(--olive);
            border-radius: 999px;
            padding: 0.35rem 0.7rem;
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }

        .hero-title {
            font-size: clamp(2.3rem, 5.5vw, 4.65rem);
            line-height: 0.95;
            margin: 0 0 0.85rem 0;
            color: var(--deep-brown);
        }

        .hero-copy {
            max-width: 620px;
            color: var(--muted);
            font-size: 1.03rem;
            line-height: 1.65;
            margin-bottom: 1rem;
        }

        .soft-note {
            color: var(--olive);
            font-size: 0.92rem;
            font-weight: 650;
        }

        .hero-art-card {
            border: 1px solid rgba(140, 138, 103, 0.28);
            background: rgba(255, 249, 240, 0.70);
            border-radius: 28px;
            padding: 0.85rem;
            text-align: center;
            box-shadow: inset 0 0 0 1px rgba(255, 249, 240, 0.55);
        }

        .hero-art-card img,
        .fade-in-brand img {
            animation: hayyakFadeIn 900ms ease-out both;
        }

        @keyframes hayyakFadeIn {
            from {
                opacity: 0;
                transform: translateY(8px) scale(0.985);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        /* CARDS */

        .section-card {
            border: 1px solid rgba(140, 138, 103, 0.24);
            border-radius: 28px;
            background: rgba(255, 249, 240, 0.91);
            box-shadow: 0 16px 38px rgba(100, 42, 22, 0.075);
            padding: 1.25rem;
            margin: 0.65rem 0 1rem 0;
        }

        .section-heading {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: flex-end;
            margin-bottom: 0.85rem;
        }

        .section-heading h2 {
            margin: 0;
            font-size: 1.55rem;
        }

        .section-heading p {
            margin: 0.3rem 0 0 0;
            color: var(--muted);
            font-size: 0.95rem;
        }

        .arabic-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(140, 138, 103, 0.48), transparent);
            position: relative;
            margin: 1rem 0;
        }

        .arabic-divider:after {
            content: "";
            width: 9px;
            height: 9px;
            background: var(--olive);
            transform: rotate(45deg);
            position: absolute;
            left: 50%;
            top: -4px;
            margin-left: -4px;
        }

        .result-card {
            border: 1px solid rgba(140, 138, 103, 0.24);
            background: #FFF9F0;
            border-radius: 22px;
            padding: 1rem;
            margin-bottom: 0.8rem;
        }

        .result-topline {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
        }

        .result-title {
            color: var(--deep-brown);
            font-size: 1.15rem;
            font-weight: 800;
            margin: 0;
        }

        .match-pill {
            background: var(--green-soft);
            color: var(--olive);
            border: 1px solid var(--green-line);
            border-radius: 999px;
            padding: 0.35rem 0.65rem;
            font-size: 0.82rem;
            font-weight: 800;
            white-space: nowrap;
        }

        .muted-text {
            color: var(--muted);
            line-height: 1.6;
        }

        /* STREAMLIT QUIZ RESTYLE */

        div[data-testid="stForm"] {
            border: 1px solid rgba(140, 138, 103, 0.20);
            background: rgba(246, 239, 229, 0.38);
            border-radius: 24px;
            padding: 1rem 1rem 0.65rem 1rem;
        }

        div[data-testid="stSlider"],
        div[data-testid="stSelectbox"],
        div[data-testid="stRadio"] {
            background: rgba(255, 249, 240, 0.76);
            border: 1px solid rgba(140, 138, 103, 0.18);
            border-radius: 18px;
            padding: 0.85rem 0.9rem;
            margin-bottom: 0.75rem;
        }

        div[data-testid="stSlider"] label,
        div[data-testid="stSelectbox"] label,
        div[data-testid="stRadio"] label {
            color: var(--deep-brown) !important;
            font-weight: 800 !important;
            letter-spacing: -0.01em;
        }

        div[data-baseweb="select"] > div {
            background-color: #FFF9F0 !important;
            border-color: rgba(140, 138, 103, 0.35) !important;
            border-radius: 999px !important;
            color: var(--ink) !important;
            box-shadow: none !important;
        }

        div[data-baseweb="select"] span {
            color: var(--ink) !important;
        }

        div[role="radiogroup"] label {
            background: rgba(140, 138, 103, 0.09);
            border: 1px solid rgba(140, 138, 103, 0.18);
            border-radius: 999px;
            padding: 0.38rem 0.68rem;
            margin-right: 0.25rem;
        }

        div[role="radiogroup"] label:hover {
            background: rgba(140, 138, 103, 0.16);
        }

        input[type="radio"],
        input[type="checkbox"] {
            accent-color: var(--olive);
        }

        input,
        textarea {
            background: #FFF9F0 !important;
            color: var(--ink) !important;
            border-color: rgba(140, 138, 103, 0.35) !important;
            border-radius: 16px !important;
        }

        div[data-testid="stSlider"] [data-baseweb="slider"] {
            color: var(--olive) !important;
        }

        div[data-testid="stButton"] > button,
        div[data-testid="stFormSubmitButton"] > button {
            background: var(--olive);
            color: var(--paper);
            border: 1px solid var(--olive);
            border-radius: 999px;
            padding: 0.65rem 1.15rem;
            font-weight: 800;
            transition: 0.18s ease;
        }

        div[data-testid="stButton"] > button:hover,
        div[data-testid="stFormSubmitButton"] > button:hover {
            background: var(--deep-brown);
            border-color: var(--deep-brown);
            color: var(--paper);
            transform: translateY(-1px);
        }

        div[data-testid="stAlert"] {
            background: rgba(140, 138, 103, 0.12);
            border: 1px solid rgba(140, 138, 103, 0.24);
            color: var(--deep-brown);
        }

        /* UTILITIES */

        .utility-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .utility-card {
            border: 1px solid rgba(140, 138, 103, 0.24);
            background: rgba(255, 249, 240, 0.9);
            border-radius: 24px;
            padding: 1.1rem;
            min-height: 145px;
            box-shadow: 0 14px 34px rgba(100, 42, 22, 0.07);
        }

        .utility-icon {
            width: 42px;
            height: 42px;
            border-radius: 14px;
            background: var(--green-soft);
            border: 1px solid var(--green-line);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--olive);
            font-weight: 900;
            margin-bottom: 0.75rem;
        }

        @media (max-width: 820px) {
            .hayyak-navbar {
                border-radius: 24px;
                position: relative;
                top: 0;
            }

            .hayyak-navbar-inner {
                align-items: flex-start;
                flex-direction: column;
            }

            .hayyak-logo {
                width: 48px;
                height: 48px;
            }

            .hayyak-links {
                width: 100%;
            }

            .hero-shell {
                padding: 1.2rem;
                border-radius: 26px;
                margin-bottom: 0.55rem;
            }

            .hero-grid {
                grid-template-columns: 1fr;
            }

            .hero-shell:before {
                font-size: 3.5rem;
                right: 1rem;
            }

            .section-card {
                padding: 1rem;
            }

            .utility-grid {
                grid-template-columns: 1fr;
            }

            .section-heading {
                align-items: flex-start;
                flex-direction: column;
            }
        }
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

    link_html = ""
    for key, label, href in links:
        active_class = "active" if active == key else ""
        link_html += f'<a class="{active_class}" href="{href}">{label}</a>'

    st.markdown(
        f"""
        <div class="hayyak-navbar">
            <div class="hayyak-navbar-inner">
                <div class="hayyak-brand">
                    {brand_html}
                </div>
                <div class="hayyak-links">
                    {link_html}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def arabic_divider():
    st.markdown('<div class="arabic-divider"></div>', unsafe_allow_html=True)
