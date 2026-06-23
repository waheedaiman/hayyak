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
            --line: rgba(100, 42, 22, 0.18);
        }

        html, body, [data-testid="stAppViewContainer"] {
            background:
                radial-gradient(circle at top left, rgba(188, 134, 83, 0.12), transparent 34%),
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
            padding-top: 1.25rem;
            padding-bottom: 3rem;
        }

        h1, h2, h3 {
            color: var(--deep-brown);
            letter-spacing: -0.03em;
        }

        p, label, span, div {
            color: var(--ink);
        }

        .hayyak-navbar {
            position: sticky;
            top: 0.75rem;
            z-index: 999;
            width: 100%;
            margin-bottom: 1.75rem;
            padding: 0.7rem 0.85rem;
            border: 1px solid rgba(100, 42, 22, 0.14);
            border-radius: 999px;
            background: rgba(255, 249, 240, 0.88);
            box-shadow: 0 12px 28px rgba(100, 42, 22, 0.10);
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
            gap: 0.65rem;
            font-weight: 800;
            color: var(--deep-brown);
            letter-spacing: 0.03em;
        }

        .hayyak-brand-mark {
            width: 34px;
            height: 34px;
            border-radius: 999px;
            background: var(--deep-brown);
            color: var(--paper);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 0.9rem;
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
            padding: 0.48rem 0.78rem;
            border-radius: 999px;
            transition: 0.18s ease;
        }

        .hayyak-links a:hover {
            background: rgba(188, 134, 83, 0.18);
        }

        .hayyak-links a.active {
            background: var(--deep-brown);
            color: var(--paper) !important;
        }

        .hero-shell {
            border: 1px solid var(--line);
            border-radius: 34px;
            background:
                linear-gradient(135deg, rgba(255, 249, 240, 0.95), rgba(239, 225, 209, 0.78));
            box-shadow: 0 24px 60px rgba(100, 42, 22, 0.12);
            padding: 2.1rem;
            margin-bottom: 1.5rem;
            overflow: hidden;
            position: relative;
        }

        .hero-shell:before {
            content: "حيّاك";
            position: absolute;
            right: 2rem;
            top: 0.6rem;
            font-size: 5.5rem;
            color: rgba(100, 42, 22, 0.045);
            font-weight: 800;
            line-height: 1;
        }

        .hero-grid {
            display: grid;
            grid-template-columns: minmax(0, 1.4fr) minmax(260px, 0.7fr);
            gap: 1.5rem;
            align-items: center;
        }

        .eyebrow {
            display: inline-flex;
            width: fit-content;
            align-items: center;
            gap: 0.45rem;
            border: 1px solid rgba(140, 138, 103, 0.35);
            background: rgba(140, 138, 103, 0.10);
            color: var(--olive);
            border-radius: 999px;
            padding: 0.35rem 0.7rem;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.85rem;
        }

        .hero-title {
            font-size: clamp(2.4rem, 6vw, 5rem);
            line-height: 0.95;
            margin: 0 0 1rem 0;
            color: var(--deep-brown);
        }

        .hero-copy {
            max-width: 620px;
            color: var(--muted);
            font-size: 1.05rem;
            line-height: 1.7;
            margin-bottom: 1.25rem;
        }

        .hero-actions {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            align-items: center;
        }

        .soft-note {
            color: var(--muted);
            font-size: 0.9rem;
        }

        .brand-card {
            border: 1px solid rgba(100, 42, 22, 0.16);
            background: rgba(255, 249, 240, 0.72);
            border-radius: 28px;
            padding: 1.1rem;
            text-align: center;
        }

        .brand-card img {
            max-width: 210px;
            width: 100%;
            margin: 0 auto;
            display: block;
        }

        .section-card {
            border: 1px solid var(--line);
            border-radius: 28px;
            background: rgba(255, 249, 240, 0.88);
            box-shadow: 0 18px 42px rgba(100, 42, 22, 0.08);
            padding: 1.45rem;
            margin: 1rem 0;
        }

        .section-heading {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: flex-end;
            margin-bottom: 1rem;
        }

        .section-heading h2 {
            margin: 0;
            font-size: 1.55rem;
        }

        .section-heading p {
            margin: 0.35rem 0 0 0;
            color: var(--muted);
            font-size: 0.95rem;
        }

        .arabic-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(100, 42, 22, 0.28), transparent);
            position: relative;
            margin: 1.1rem 0;
        }

        .arabic-divider:after {
            content: "";
            width: 9px;
            height: 9px;
            background: var(--clay);
            transform: rotate(45deg);
            position: absolute;
            left: 50%;
            top: -4px;
            margin-left: -4px;
        }

        .result-card {
            border: 1px solid rgba(100, 42, 22, 0.14);
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
            background: rgba(188, 134, 83, 0.18);
            color: var(--deep-brown);
            border: 1px solid rgba(188, 134, 83, 0.30);
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

        .utility-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .utility-card {
            border: 1px solid rgba(100, 42, 22, 0.14);
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
            background: rgba(188, 134, 83, 0.20);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--deep-brown);
            font-weight: 900;
            margin-bottom: 0.75rem;
        }

        div[data-testid="stButton"] > button {
            background: var(--deep-brown);
            color: var(--paper);
            border: 1px solid var(--deep-brown);
            border-radius: 999px;
            padding: 0.65rem 1.1rem;
            font-weight: 750;
            transition: 0.18s ease;
        }

        div[data-testid="stButton"] > button:hover {
            background: var(--clay);
            border-color: var(--clay);
            color: var(--paper);
            transform: translateY(-1px);
        }

        div[data-testid="stForm"] {
            border: none;
        }

        div[data-testid="stSlider"] label,
        div[data-testid="stSelectbox"] label,
        div[data-testid="stRadio"] label {
            color: var(--deep-brown) !important;
            font-weight: 700;
        }

        .stSelectbox, .stRadio, .stSlider {
            margin-bottom: 0.35rem;
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

            .hayyak-links {
                width: 100%;
            }

            .hero-shell {
                padding: 1.35rem;
                border-radius: 26px;
            }

            .hero-grid {
                grid-template-columns: 1fr;
            }

            .hero-shell:before {
                font-size: 3.5rem;
                right: 1rem;
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
    links = [
        ("home", "Home / Quiz", "/"),
        ("utilities", "Utilities", "/Utilities"),
        ("checklist", "Dubai Checklist", "/Dubai_Checklist"),
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
                    <div class="hayyak-brand-mark">H</div>
                    <span>Hayyak</span>
                </div>
                <div class="hayyak-links">
                    {link_html}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_card_start():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)


def section_card_end():
    st.markdown("</div>", unsafe_allow_html=True)


def arabic_divider():
    st.markdown('<div class="arabic-divider"></div>', unsafe_allow_html=True)
