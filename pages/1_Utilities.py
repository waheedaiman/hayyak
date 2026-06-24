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
    <div style="text-align:center; padding:1.5rem 0 0.5rem 0;">
        <div class="eyebrow" style="color:#8C8A67; font-weight:600; letter-spacing:0.15em; text-transform:uppercase; font-size:0.85rem;">
            Move‑in setup
        </div>
        <h1 style="font-size:2.6rem; margin:0.25rem 0 0.2rem 0; color:#642A16; font-weight:700;">
            Utilities
        </h1>
        <p style="font-size:1.1rem; color:#735A4C; max-width:600px; margin:0.5rem auto 0 auto;">
            A calm, structured place to understand the essential services newcomers usually need when settling into a Dubai home.
        </p>
        <div style="margin:1rem auto 0.5rem auto; width:60px; height:2px; background:#8C8A67; border-radius:2px;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---- UTILITY CARDS ----
st.markdown(
    """
    <div class="section-card">
        <div class="section-heading">
            <div>
                <h2>Choose a setup area</h2>
                <p>Select a utility to view its move‑in checklist.</p>
            </div>
        </div>
        <div class="utility-grid">
    """,
    unsafe_allow_html=True,
)

items = list(UTILITIES.items())
cols = st.columns(3)

for index, (name, item) in enumerate(items):
    with cols[index % 3]:
        # We'll use a container to hold the card and the button together
        st.markdown(
            f"""
            <div class="utility-card" style="display:flex; flex-direction:column; height:100%;">
                <div style="flex:1;">
                    <h3 style="margin:0 0 0.3rem 0; color:#642A16;">{name}</h3>
                    <p class="muted-text" style="margin:0;">{item["description"]}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        # Button placed inside the same column, styled to attach to the card
        if st.button("View guide", key=f"utility_{name}", use_container_width=True):
            show_utility_modal(name, item)

st.markdown("</div></div>", unsafe_allow_html=True)


# ---- ADDITIONAL STYLING FOR THE BUTTON INSIDE THE CARD ----
# We'll inject some CSS to make the button look like part of the card.
st.markdown(
    """
    <style>
    /* Style the button to sit flush with the card */
    div[data-testid="column"]:has(div.utility-card) {
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    div[data-testid="column"]:has(div.utility-card) > div[data-testid="stButton"] {
        margin-top: -0.5rem;  /* remove gap */
        padding: 0 0 0.2rem 0;
    }
    div[data-testid="column"]:has(div.utility-card) > div[data-testid="stButton"] button {
        border-radius: 0 0 22px 22px;
        background: rgba(140, 138, 103, 0.08);
        border: 1px solid rgba(140, 138, 103, 0.18);
        border-top: none;
        color: #642A16;
        font-weight: 600;
        padding: 0.5rem 0;
        box-shadow: none;
        transition: 0.2s ease;
    }
    div[data-testid="column"]:has(div.utility-card) > div[data-testid="stButton"] button:hover {
        background: rgba(140, 138, 103, 0.18);
        border-color: rgba(140, 138, 103, 0.3);
        color: #2B1B14;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
