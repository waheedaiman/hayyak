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
        "icon": "💡",
        "gradient": "linear-gradient(135deg, #F6EFE5 0%, #E8D9C8 100%)",
        "description": "Electricity & water setup for your new home.",
        "steps": [
            "Prepare tenancy contract and Emirates ID.",
            "Confirm premises number and property details.",
            "Submit activation via DEWA official channel.",
            "Pay deposit and activation fees.",
            "Save confirmation for landlord and building management.",
        ],
    },
    "Ejari": {
        "icon": "📝",
        "gradient": "linear-gradient(135deg, #EFE1D1 0%, #DCCBB5 100%)",
        "description": "Rental contract registration – essential for many processes.",
        "steps": [
            "Confirm signed tenancy contract.",
            "Prepare landlord and tenant documents.",
            "Register through the approved Ejari system.",
            "Download your Ejari certificate.",
            "Use it for utilities and other move‑in needs.",
        ],
    },
    "du / e&": {
        "icon": "📱",
        "gradient": "linear-gradient(135deg, #E8D9C8 0%, #D4C0A8 100%)",
        "description": "Mobile connection and SIM setup after arrival.",
        "steps": [
            "Compare prepaid vs postpaid plans.",
            "Have passport, Emirates ID, or visa ready.",
            "Choose data plan based on usage.",
            "Activate SIM or eSIM.",
            "Save customer support contacts.",
        ],
    },
    "Internet": {
        "icon": "🌐",
        "gradient": "linear-gradient(135deg, #DCCBB5 0%, #C8B39A 100%)",
        "description": "Home internet for your apartment or villa.",
        "steps": [
            "Check available providers in your building.",
            "Compare speed, contract length, and installation time.",
            "Book installation after tenancy confirmation.",
            "Keep router and account details safe.",
            "Test speed after installation.",
        ],
    },
    "Move-in Documents": {
        "icon": "📂",
        "gradient": "linear-gradient(135deg, #C8B39A 0%, #B59D82 100%)",
        "description": "Documents needed during early relocation steps.",
        "steps": [
            "Passport copy.",
            "Visa or entry permit.",
            "Emirates ID or application details.",
            "Tenancy contract.",
            "Payment receipts and confirmation emails.",
        ],
    },
}


@st.dialog("Utility setup guide")
def show_utility_modal(name, item):
    # Decorative header
    st.markdown(
        f"""
        <div style="text-align:center; padding:0.5rem 0 0.5rem 0;">
            <span style="font-size:3rem; line-height:1;">{item["icon"]}</span>
            <h2 style="margin:0.2rem 0 0 0; color:#642A16;">{name}</h2>
            <p style="color:#735A4C; margin:0.2rem 0 0 0;">{item["description"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    arabic_divider()

    st.markdown("**✅ Setup checklist**")
    for step in item["steps"]:
        st.markdown(f"- {step}")

    st.caption(
        "Official links can be added here later as natural inline links inside the setup text."
    )


# ---- HERO SECTION (full-width, animated) ----
st.markdown(
    """
    <div class="utilities-hero">
        <div class="hero-pattern"></div>
        <div class="hero-content">
            <div class="hero-icon">⚡</div>
            <h1>Utilities</h1>
            <p>Your essential guide to setting up services in Dubai – clear, calm, and built for newcomers.</p>
            <div class="hero-underline"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---- QUICK TIP CARD (between hero and grid) ----
st.markdown(
    """
    <div class="tip-card">
        <div class="tip-icon">💡</div>
        <div class="tip-text">
            <strong>Pro tip:</strong> Start with DEWA and Ejari – they unlock everything else. Many buildings require these before you can activate internet or move in.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---- UTILITY CARDS (masonry-like grid) ----
st.markdown(
    """
    <div class="utility-grid-container">
        <div class="grid-header">
            <h2>Choose a setup area</h2>
            <span class="grid-badge">5 essentials</span>
        </div>
        <div class="utility-grid">
    """,
    unsafe_allow_html=True,
)

# We'll generate cards using columns but we want a masonry feel – we'll use CSS grid via st.columns and custom classes.
# However, Streamlit columns are easy; we'll use them but style the cells to have variable heights via CSS.
# We'll use 3 columns, but we can add a class to each card to vary height if needed.
# Since we want simplicity, we'll just use 3 columns and let the content define the height.

cols = st.columns(3)
for idx, (name, item) in enumerate(UTILITIES.items()):
    with cols[idx % 3]:
        # Build a card with a gradient background and clickable area
        st.markdown(
            f"""
            <div class="utility-card" style="background: {item['gradient']}; cursor:pointer;" onclick="document.getElementById('util_btn_{idx}').click();">
                <div class="card-icon">{item["icon"]}</div>
                <h3>{name}</h3>
                <p>{item["description"]}</p>
                <div class="card-footer">
                    <span class="card-link">Explore →</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Hidden button to trigger the modal
        if st.button("", key=f"util_btn_{idx}", label_visibility="collapsed"):
            show_utility_modal(name, item)

st.markdown("</div></div>", unsafe_allow_html=True)


# ---- QUOTE FOOTER ----
st.markdown(
    """
    <div class="quote-footer">
        <span class="quote-mark">"</span>
        <p>Moving to a new city is a journey – we're here to make the utility part feel like a gentle step.</p>
        <span class="quote-attribution">– Hayyak</span>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---- CUSTOM STYLES (completely new) ----
st.markdown(
    """
    <style>
    /* ---- HERO ---- */
    .utilities-hero {
        position: relative;
        padding: 2.5rem 1.5rem 2rem 1.5rem;
        margin-bottom: 1.5rem;
        border-radius: 32px;
        background: linear-gradient(135deg, #F6EFE5 0%, #E8D9C8 100%);
        text-align: center;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(100,42,22,0.06);
    }
    .hero-pattern {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: radial-gradient(circle at 20% 30%, rgba(140,138,103,0.08) 0%, transparent 50%),
                          radial-gradient(circle at 80% 70%, rgba(140,138,103,0.06) 0%, transparent 50%);
        pointer-events: none;
    }
    .hero-content {
        position: relative;
        z-index: 1;
        max-width: 640px;
        margin: 0 auto;
        animation: fadeUp 0.8s ease-out both;
    }
    .hero-icon {
        font-size: 3.2rem;
        line-height: 1;
        margin-bottom: 0.2rem;
    }
    .hero-content h1 {
        font-size: 2.8rem;
        margin: 0.2rem 0 0.2rem 0;
        color: #642A16;
        font-weight: 700;
        letter-spacing: -0.03em;
    }
    .hero-content p {
        font-size: 1.1rem;
        color: #735A4C;
        max-width: 460px;
        margin: 0 auto;
        line-height: 1.5;
    }
    .hero-underline {
        width: 50px;
        height: 3px;
        background: #8C8A67;
        border-radius: 2px;
        margin: 0.7rem auto 0 auto;
    }

    /* ---- TIP CARD ---- */
    .tip-card {
        display: flex;
        align-items: center;
        gap: 1rem;
        background: rgba(255,249,240,0.7);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(140,138,103,0.18);
        border-radius: 20px;
        padding: 0.8rem 1.2rem;
        margin: 0 0 1.5rem 0;
        box-shadow: 0 4px 12px rgba(100,42,22,0.04);
        animation: fadeUp 0.9s ease-out 0.15s both;
    }
    .tip-icon {
        font-size: 2rem;
        line-height: 1;
        flex-shrink: 0;
    }
    .tip-text {
        color: #2B1B14;
        font-size: 0.95rem;
    }

    /* ---- GRID ---- */
    .utility-grid-container {
        animation: fadeUp 0.9s ease-out 0.3s both;
        margin: 1rem 0 1.5rem 0;
    }
    .grid-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.2rem;
    }
    .grid-header h2 {
        margin: 0;
        font-size: 1.6rem;
        color: #642A16;
    }
    .grid-badge {
        background: rgba(140,138,103,0.12);
        color: #8C8A67;
        padding: 0.2rem 0.8rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid rgba(140,138,103,0.15);
    }
    .utility-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.2rem;
    }
    /* Streamlit columns will be placed inside the grid, but we'll use the existing column divs */
    /* We need to style the actual column divs to be part of the grid */
    /* We'll use a wrapper div around the columns – we'll inject a class via st.markdown */
    /* We'll just rely on the existing column layout, but we can style the column containers */
    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
    }

    /* ---- CARD ---- */
    .utility-card {
        border-radius: 24px;
        padding: 1.5rem 1.2rem 1rem 1.2rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        transition: all 0.25s ease;
        border: 1px solid rgba(140,138,103,0.12);
        box-shadow: 0 4px 12px rgba(100,42,22,0.04);
        position: relative;
        overflow: hidden;
    }
    .utility-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(180deg, transparent 60%, rgba(255,255,255,0.2) 100%);
        pointer-events: none;
    }
    .utility-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 16px 36px rgba(100,42,22,0.10);
        border-color: rgba(140,138,103,0.3);
    }
    .card-icon {
        font-size: 2.8rem;
        line-height: 1;
        margin-bottom: 0.3rem;
    }
    .utility-card h3 {
        margin: 0 0 0.2rem 0;
        font-size: 1.2rem;
        font-weight: 700;
        color: #642A16;
    }
    .utility-card p {
        margin: 0 0 0.8rem 0;
        color: #735A4C;
        font-size: 0.9rem;
        flex: 1;
    }
    .card-footer {
        text-align: right;
        margin-top: auto;
    }
    .card-link {
        display: inline-block;
        background: rgba(255,255,255,0.4);
        backdrop-filter: blur(4px);
        padding: 0.2rem 1rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #642A16;
        border: 1px solid rgba(140,138,103,0.15);
        transition: 0.2s ease;
    }
    .utility-card:hover .card-link {
        background: #8C8A67;
        color: white;
        border-color: #8C8A67;
    }

    /* ---- QUOTE ---- */
    .quote-footer {
        text-align: center;
        padding: 1.5rem 0 0.5rem 0;
        margin-top: 1.5rem;
        border-top: 1px solid rgba(140,138,103,0.12);
        animation: fadeUp 1s ease-out 0.6s both;
    }
    .quote-mark {
        font-size: 3rem;
        color: rgba(140,138,103,0.25);
        line-height: 1;
        display: block;
        font-family: Georgia, serif;
    }
    .quote-footer p {
        font-size: 1.05rem;
        color: #735A4C;
        max-width: 500px;
        margin: 0.2rem auto 0.3rem auto;
        font-style: italic;
        line-height: 1.5;
    }
    .quote-attribution {
        font-size: 0.85rem;
        color: #8C8A67;
        font-weight: 600;
        letter-spacing: 0.05em;
    }

    /* ---- ANIMATIONS ---- */
    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(12px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* ---- RESPONSIVE ---- */
    @media (max-width: 820px) {
        .utility-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        .hero-content h1 {
            font-size: 2.2rem;
        }
        .tip-card {
            flex-direction: column;
            text-align: center;
            gap: 0.3rem;
        }
        .grid-header {
            flex-direction: column;
            align-items: flex-start;
            gap: 0.3rem;
        }
    }
    @media (max-width: 480px) {
        .utility-grid {
            grid-template-columns: 1fr;
        }
        .hero-content h1 {
            font-size: 1.8rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)
