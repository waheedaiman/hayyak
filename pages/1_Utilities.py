import streamlit as st

from src.ui import apply_hayyak_theme, arabic_divider, render_nav


st.set_page_config(
    page_title="Hayyak | Utilities",
    page_icon="🔌",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="utilities")


UTILITIES = {
    "DEWA": {
        "number": "01",
        "tag": "Electricity & Water",
        "description": "Power and water activation for your new Dubai home — the essential first step.",
        "steps": [
            "Prepare tenancy contract and Emirates ID once available.",
            "Confirm the premises number or property details.",
            "Submit activation request through the official DEWA channel.",
            "Pay deposit and activation fees where applicable.",
            "Save confirmation details for your landlord or building management.",
        ],
        "accent": "#BC8653",
        "motif": "M 0,20 Q 30,0 60,20 Q 90,40 120,20",
    },
    "Ejari": {
        "number": "02",
        "tag": "Rental Registration",
        "description": "Your tenancy contract, made official — required before almost everything else.",
        "steps": [
            "Confirm your signed tenancy contract.",
            "Prepare landlord and tenant documents.",
            "Register the contract through the approved Ejari process.",
            "Download or save your Ejari certificate.",
            "Use the certificate for utilities and other move-in requirements.",
        ],
        "accent": "#8C8A67",
        "motif": "M 0,10 L 20,30 L 40,10 L 60,30 L 80,10 L 100,30 L 120,10",
    },
    "du / e&": {
        "number": "03",
        "tag": "Mobile & SIM",
        "description": "Stay connected from day one — your first local number sets everything else in motion.",
        "steps": [
            "Compare prepaid and postpaid plans.",
            "Prepare passport, Emirates ID, or valid identification.",
            "Choose mobile data based on commute and daily usage.",
            "Activate SIM or eSIM where supported.",
            "Save customer support details in case activation fails.",
        ],
        "accent": "#B27960",
        "motif": "M 0,15 C 20,0 40,30 60,15 C 80,0 100,30 120,15",
    },
    "Internet": {
        "number": "04",
        "tag": "Home Broadband",
        "description": "Fast, reliable internet — book early, because installation takes time.",
        "steps": [
            "Check which providers are available in the building.",
            "Compare speed, contract length, and installation time.",
            "Book installation after tenancy confirmation.",
            "Keep router and account details safely stored.",
            "Test speed after installation.",
        ],
        "accent": "#B59275",
        "motif": "M 0,20 L 30,5 L 60,20 L 90,5 L 120,20",
    },
    "Move-in Documents": {
        "number": "05",
        "tag": "Document Checklist",
        "description": "The paperwork that underpins everything — keep these within reach at all times.",
        "steps": [
            "Passport copy.",
            "Visa or entry permit where applicable.",
            "Emirates ID or application details.",
            "Tenancy contract.",
            "Payment receipts and confirmation emails.",
        ],
        "accent": "#642A16",
        "motif": "M 10,25 A 20,20 0 0 1 50,5 A 20,20 0 0 1 90,25 A 20,20 0 0 1 50,45 A 20,20 0 0 1 10,25",
    },
}


@st.dialog("Utility setup guide")
def show_utility_modal(name, item):
    st.markdown(
        f"""
        <div style="margin-bottom:0.25rem;">
            <span style="
                font-size:0.72rem;
                font-weight:800;
                letter-spacing:0.22em;
                text-transform:uppercase;
                color:{item['accent']};
            ">{item['tag']}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader(name)
    st.caption(item["description"])
    arabic_divider()

    st.markdown("**Setup checklist**")
    for i, step in enumerate(item["steps"], 1):
        st.markdown(
            f"""
            <div style="
                display:flex;
                align-items:flex-start;
                gap:0.75rem;
                padding:0.6rem 0;
                border-bottom:1px solid rgba(140,138,103,0.14);
            ">
                <span style="
                    min-width:24px;
                    height:24px;
                    border-radius:50%;
                    background:rgba(140,138,103,0.14);
                    border:1px solid rgba(140,138,103,0.28);
                    display:inline-flex;
                    align-items:center;
                    justify-content:center;
                    font-size:0.72rem;
                    font-weight:800;
                    color:{item['accent']};
                ">{i}</span>
                <span style="color:#2B1B14;line-height:1.55;">{step}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <p style="margin-top:1.1rem;font-size:0.8rem;color:#735A4C;">
            Official links will be added as inline references within each step as the guide develops.
        </p>
        """,
        unsafe_allow_html=True,
    )


# ── ADDITIONAL PAGE-LEVEL CSS ──────────────────────────────────────────────

st.markdown(
    """
    <style>
    .util-hero {
        position: relative;
        overflow: hidden;
        border-radius: 32px;
        background: linear-gradient(135deg, #2B1B14 0%, #642A16 55%, #BC8653 100%);
        padding: 4rem 3.5rem;
        margin-bottom: 2.5rem;
        display: flex;
        align-items: flex-end;
        min-height: 320px;
    }

    .util-hero-svg {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        opacity: 0.13;
        pointer-events: none;
    }

    .util-hero-content {
        position: relative;
        z-index: 2;
        max-width: 560px;
    }

    .util-hero-eyebrow {
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.32em;
        text-transform: uppercase;
        color: #BC8653;
        margin-bottom: 0.85rem;
        display: block;
    }

    .util-hero-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(3rem, 7vw, 5.2rem);
        font-weight: 700;
        line-height: 0.92;
        letter-spacing: -0.04em;
        color: #FFF9F0 !important;
        margin: 0 0 1.1rem 0;
    }

    .util-hero-copy {
        font-size: 1.05rem;
        line-height: 1.65;
        color: rgba(246, 239, 229, 0.78);
        max-width: 440px;
        margin: 0;
    }

    .util-hero-badge {
        position: absolute;
        top: 2.2rem;
        right: 2.5rem;
        z-index: 3;
        width: 90px;
        height: 90px;
        border-radius: 50%;
        border: 1px solid rgba(181, 146, 117, 0.38);
        background: rgba(255, 249, 240, 0.07);
        backdrop-filter: blur(4px);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 0;
    }

    .util-hero-badge-num {
        font-family: Georgia, serif;
        font-size: 1.9rem;
        font-weight: 700;
        color: #F6EFE5;
        line-height: 1;
    }

    .util-hero-badge-label {
        font-size: 0.6rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #B59275;
        font-weight: 700;
    }

    /* ── SECTION LABEL ── */
    .util-section-label {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.75rem;
    }

    .util-section-label-line {
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, rgba(100,42,22,0.18), transparent);
    }

    .util-section-label-text {
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.3em;
        text-transform: uppercase;
        color: #8C8A67;
        white-space: nowrap;
    }

    /* ── PINTEREST CARD ── */
    .util-pin-card {
        background: #FFF9F0;
        border: 1px solid rgba(140, 138, 103, 0.20);
        border-radius: 24px;
        overflow: hidden;
        transition: transform 0.22s ease, box-shadow 0.22s ease;
        cursor: pointer;
        box-shadow: 0 4px 18px rgba(100, 42, 22, 0.06);
        margin-bottom: 0.85rem;
    }

    .util-pin-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 44px rgba(100, 42, 22, 0.13);
    }

    .util-pin-top {
        padding: 1.5rem 1.5rem 0.6rem 1.5rem;
        position: relative;
    }

    .util-pin-number {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 4.2rem;
        font-weight: 700;
        line-height: 0.85;
        letter-spacing: -0.06em;
        opacity: 0.08;
        position: absolute;
        bottom: -0.1rem;
        right: 1.1rem;
        pointer-events: none;
        color: #642A16;
    }

    .util-pin-tag {
        display: inline-block;
        font-size: 0.66rem;
        font-weight: 800;
        letter-spacing: 0.24em;
        text-transform: uppercase;
        padding: 0.28rem 0.7rem;
        border-radius: 999px;
        background: rgba(140, 138, 103, 0.12);
        border: 1px solid rgba(140, 138, 103, 0.22);
        color: #8C8A67;
        margin-bottom: 0.9rem;
    }

    .util-pin-title {
        font-family: Georgia, "Times New Roman", serif;
        font-size: 1.38rem;
        font-weight: 700;
        color: #642A16 !important;
        line-height: 1.15;
        letter-spacing: -0.03em;
        margin: 0 0 0.6rem 0;
    }

    .util-pin-desc {
        font-size: 0.88rem;
        line-height: 1.6;
        color: #735A4C;
        margin: 0;
    }

    .util-pin-motif {
        width: 100%;
        height: 36px;
        display: block;
        margin-top: 1rem;
        opacity: 0.45;
    }

    .util-pin-footer {
        padding: 0.85rem 1.5rem 1.25rem 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-top: 1px solid rgba(140, 138, 103, 0.12);
    }

    .util-pin-count {
        font-size: 0.75rem;
        color: #8C8A67;
        font-weight: 700;
        letter-spacing: 0.04em;
    }

    .util-pin-arrow {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: rgba(140, 138, 103, 0.1);
        border: 1px solid rgba(140, 138, 103, 0.22);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #642A16;
        font-size: 0.9rem;
        transition: background 0.18s;
    }

    .util-pin-card:hover .util-pin-arrow {
        background: #642A16;
        border-color: #642A16;
        color: #FFF9F0;
    }

    /* hide streamlit buttons inside card columns — they show below the HTML card */
    div[data-testid="stButton"] > button {
        width: 100%;
        margin-top: -0.4rem;
        margin-bottom: 0.5rem;
        border-radius: 18px !important;
        font-size: 0.83rem !important;
        padding: 0.55rem 1rem !important;
        letter-spacing: 0.03em;
    }

    @media (max-width: 820px) {
        .util-hero {
            padding: 2.5rem 1.75rem;
            min-height: 240px;
        }
        .util-hero-badge {
            display: none;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ── HERO ──────────────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="util-hero">
        <!-- Geometric tile SVG background -->
        <svg class="util-hero-svg" viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg">
            <!-- Islamic-inspired geometric repeat -->
            <defs>
                <pattern id="tile" x="0" y="0" width="80" height="80" patternUnits="userSpaceOnUse">
                    <rect width="80" height="80" fill="none"/>
                    <!-- outer diamond -->
                    <polygon points="40,2 78,40 40,78 2,40" fill="none" stroke="#F6EFE5" stroke-width="0.8"/>
                    <!-- inner octagon -->
                    <polygon points="40,14 54,26 66,40 54,54 40,66 26,54 14,40 26,26" fill="none" stroke="#B59275" stroke-width="0.6"/>
                    <!-- center star cross -->
                    <line x1="40" y1="2" x2="40" y2="78" stroke="#F6EFE5" stroke-width="0.4"/>
                    <line x1="2" y1="40" x2="78" y2="40" stroke="#F6EFE5" stroke-width="0.4"/>
                    <line x1="14" y1="14" x2="66" y2="66" stroke="#F6EFE5" stroke-width="0.3"/>
                    <line x1="66" y1="14" x2="14" y2="66" stroke="#F6EFE5" stroke-width="0.3"/>
                    <!-- corner roses -->
                    <circle cx="0" cy="0" r="5" fill="none" stroke="#BC8653" stroke-width="0.7"/>
                    <circle cx="80" cy="0" r="5" fill="none" stroke="#BC8653" stroke-width="0.7"/>
                    <circle cx="0" cy="80" r="5" fill="none" stroke="#BC8653" stroke-width="0.7"/>
                    <circle cx="80" cy="80" r="5" fill="none" stroke="#BC8653" stroke-width="0.7"/>
                </pattern>
            </defs>
            <rect width="800" height="320" fill="url(#tile)"/>
        </svg>

        <div class="util-hero-badge">
            <span class="util-hero-badge-num">05</span>
            <span class="util-hero-badge-label">Guides</span>
        </div>

        <div class="util-hero-content">
            <span class="util-hero-eyebrow">Move-in setup · Dubai</span>
            <h1 class="util-hero-title">Utilities</h1>
            <p class="util-hero-copy">
                Everything you need to activate before you feel at home — electricity,
                contracts, connectivity, and the documents that tie it all together.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ── SECTION LABEL ────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="util-section-label">
        <span class="util-section-label-text">Choose a setup area</span>
        <div class="util-section-label-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ── PINTEREST CARD GRID ───────────────────────────────────────────────────

items = list(UTILITIES.items())

# 3-column layout — first two cards are taller (more prominent)
col1, col2, col3 = st.columns([1, 1, 1], gap="medium")
columns = [col1, col2, col3]

for index, (name, item) in enumerate(items):
    with columns[index % 3]:
        step_count = len(item["steps"])
        motif_d = item["motif"]
        accent = item["accent"]

        st.markdown(
            f"""
            <div class="util-pin-card">
                <div class="util-pin-top">
                    <span class="util-pin-tag">{item["tag"]}</span>
                    <p class="util-pin-number">{item["number"]}</p>
                    <h3 class="util-pin-title">{name}</h3>
                    <p class="util-pin-desc">{item["description"]}</p>
                    <svg class="util-pin-motif" viewBox="0 0 120 36" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
                        <path d="{motif_d}" fill="none" stroke="{accent}" stroke-width="1.5" stroke-linecap="round"/>
                        <circle cx="0" cy="20" r="2.5" fill="{accent}" opacity="0.6"/>
                        <circle cx="120" cy="20" r="2.5" fill="{accent}" opacity="0.6"/>
                    </svg>
                </div>
                <div class="util-pin-footer">
                    <span class="util-pin-count">{step_count} steps</span>
                    <div class="util-pin-arrow">→</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(f"Open {name} guide", key=f"utility_{name}"):
            show_utility_modal(name, item)
