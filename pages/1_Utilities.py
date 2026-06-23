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
        "icon": "D",
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
        "icon": "E",
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
        "icon": "M",
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
        "icon": "I",
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
        "icon": "M",
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
    st.subheader(name)
    st.caption(item["description"])
    arabic_divider()

    st.markdown("**Setup checklist**")
    for step in item["steps"]:
        st.markdown(f"- {step}")

    st.caption(
        "Official links can be added here later as natural inline links inside the setup text."
    )


st.markdown(
    """
    <section class="hero-shell">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">Move-in setup</div>
                <h1 class="hero-title">Utilities</h1>
                <p class="hero-copy">
                    A calm, structured place to understand the essential services
                    newcomers usually need when settling into a Dubai home.
                </p>
            </div>
            <div class="brand-card">
                <h3 style="color:#642A16;margin-bottom:.5rem;">Setup without the overwhelm</h3>
                <p class="muted-text">
                    Each card will open a focused guide instead of forcing users
                    through a long page of information.
                </p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="section-card">
        <div class="section-heading">
            <div>
                <h2>Choose a setup area</h2>
                <p>Select a utility to view its move-in checklist.</p>
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
        st.markdown(
            f"""
            <div class="utility-card">
                <div class="utility-icon">{item["icon"]}</div>
                <h3 style="margin:.2rem 0;color:#642A16;">{name}</h3>
                <p class="muted-text">{item["description"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(f"View {name} steps", key=f"utility_{name}"):
            show_utility_modal(name, item)

st.markdown("</div></div>", unsafe_allow_html=True)
