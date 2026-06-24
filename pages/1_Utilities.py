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
        "description": "Electricity and water setup for your Dubai home.",
        "steps": [
            "Prepare tenancy contract and Emirates ID once available.",
            "Confirm the premises number or property details.",
            "Submit activation request through the official DEWA channel.",
            "Pay deposit and activation fees where applicable.",
            "Save confirmation details for your landlord or building management.",
        ],
    },
    "Ejari": {
        "icon": "📝",
        "description": "Rental contract registration required for many housing processes.",
        "steps": [
            "Confirm your signed tenancy contract.",
            "Prepare landlord and tenant documents.",
            "Register the contract through the approved Ejari process.",
            "Download or save your Ejari certificate.",
            "Use the certificate for utilities and other move-in requirements.",
        ],
    },
    "du / e&": {
        "icon": "📱",
        "description": "Mobile connection and SIM setup after arrival.",
        "steps": [
            "Compare prepaid and postpaid plans.",
            "Prepare passport, Emirates ID, or valid identification.",
            "Choose mobile data based on commute and daily usage.",
            "Activate SIM or eSIM where supported.",
            "Save customer support details in case activation fails.",
        ],
    },
    "Internet": {
        "icon": "🌐",
        "description": "Home internet connection for your apartment or villa.",
        "steps": [
            "Check which providers are available in the building.",
            "Compare speed, contract length, and installation time.",
            "Book installation after tenancy confirmation.",
            "Keep router and account details safely stored.",
            "Test speed after installation.",
        ],
    },
    "Move-in Documents": {
        "icon": "📂",
        "description": "Documents usually needed during early relocation steps.",
        "steps": [
            "Passport copy.",
            "Visa or entry permit where applicable.",
            "Emirates ID or application details.",
            "Tenancy contract.",
            "Payment receipts and confirmation emails.",
        ],
    },
}


@st.dialog("Utility setup guide")
def show_utility_modal(name, item):
    st.markdown(f"## {name}")
    st.caption(item["description"])
    arabic_divider()

    st.markdown("**Setup checklist**")
    for step in item["steps"]:
        st.markdown(f"- {step}")

    st.caption(
        "Official links can be added here later as natural inline links inside the setup text."
    )


# ---- HERO SECTION ----
st.markdown(
    """
    <div class="utilities-hero">
        <div class="utilities-hero-content">
            <div class="eyebrow">Move‑in setup</div>
            <h1>Utilities</h1>
            <p>A calm, structured place to understand the essential services newcomers usually need when settling into a Dubai home.</p>
            <div class="hero-underline"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---- UTILITY CARDS (grid) ----
st.markdown('<div class="section-card" style="margin-top:0.5rem;">', unsafe_allow_html=True)
st.markdown(
    """
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.2rem;">
        <div>
            <h2 style="margin:0;">Choose a setup area</h2>
            <p style="margin:0.2rem 0 0 0; color:#735A4C;">Select a utility to view its move‑in checklist.</p>
        </div>
        <span style="font-size:0.85rem; color:#8C8A67; background:rgba(140,138,103,0.12); padding:0.3rem 0.8rem; border-radius:999px;">5 essentials</span>
    </div>
    """,
    unsafe_allow_html=True,
)

# Grid with 3 columns
cols = st.columns(3)
for idx, (name, item) in enumerate(UTILITIES.items()):
    with cols[idx % 3]:
        # Build a card with an embedded button
        st.markdown(
            f"""
            <div class="utility-card" onclick="document.getElementById('utility_btn_{idx}').click();" style="cursor:pointer;">
                <div class="utility-icon" style="font-size:2.2rem; line-height:1; margin-bottom:0.5rem;">{item["icon"]}</div>
                <h3 style="margin:0 0 0.3rem 0; color:#642A16;">{name}</h3>
                <p class="muted-text" style="margin:0 0 1rem 0; font-size:0.9rem;">{item["description"]}</p>
                <div style="text-align:right; margin-top:auto;">
                    <span class="utility-pill">View guide →</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Hidden button that triggers the modal (invisible, but clickable via the card click)
        # We use a st.button with a unique key but hide it with CSS
        if st.button("View guide", key=f"utility_btn_{idx}", use_container_width=True):
            show_utility_modal(name, item)

st.markdown("</div>", unsafe_allow_html=True)


# ---- EXTRA TIP SECTION TO FILL SPACE ----
st.markdown(
    """
    <div style="margin:2rem 0 0.5rem 0; padding:1.2rem 1.5rem; background:rgba(255,249,240,0.6); border-radius:24px; border:1px solid rgba(140,138,103,0.18);">
        <div style="display:flex; align-items:center; gap:1.2rem; flex-wrap:wrap;">
            <span style="font-size:2rem;">💡</span>
            <div>
                <div style="font-weight:700; color:#642A16;">Relocation tip</div>
                <p style="margin:0.2rem 0 0 0; color:#735A4C;">
                    Start with DEWA and Ejari – they unlock everything else. Many buildings require these before you can activate internet or move in.
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---- CUSTOM STYLES FOR THE NEW LAYOUT ----
st.markdown(
    """
    <style>
    /* Utilities hero */
    .utilities-hero {
        text-align: center;
        padding: 1.5rem 1rem 0.5rem 1rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(180deg, rgba(246,239,229,0.3) 0%, transparent 100%);
        border-radius: 32px;
    }
    .utilities-hero-content {
        max-width: 680px;
        margin: 0 auto;
    }
    .utilities-hero .eyebrow {
        color: #8C8A67;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        font-size: 0.85rem;
    }
    .utilities-hero h1 {
        font-size: 2.8rem;
        margin: 0.2rem 0 0.2rem 0;
        color: #642A16;
        font-weight: 700;
    }
    .utilities-hero p {
        font-size: 1.1rem;
        color: #735A4C;
        max-width: 520px;
        margin: 0 auto;
        line-height: 1.5;
    }
    .hero-underline {
        width: 60px;
        height: 3px;
        background: #8C8A67;
        border-radius: 2px;
        margin: 0.7rem auto 0 auto;
    }

    /* Utility cards */
    .utility-card {
        background: rgba(255,249,240,0.92);
        border: 1px solid rgba(140,138,103,0.18);
        border-radius: 24px;
        padding: 1.25rem 1.25rem 1rem 1.25rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        transition: all 0.2s ease;
        box-shadow: 0 4px 12px rgba(100,42,22,0.04);
    }
    .utility-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(100,42,22,0.10);
        border-color: rgba(140,138,103,0.35);
    }
    .utility-pill {
        display: inline-block;
        background: rgba(140,138,103,0.10);
        color: #642A16;
        padding: 0.25rem 1rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        transition: 0.2s ease;
        border: 1px solid rgba(140,138,103,0.15);
    }
    .utility-card:hover .utility-pill {
        background: #8C8A67;
        color: white;
        border-color: #8C8A67;
    }

    /* Hide the actual Streamlit button we use as a trigger */
    div[data-testid="column"] > div[data-testid="stButton"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
