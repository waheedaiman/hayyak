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
            """Start by confirming your exact property details. Ask the landlord, agent, or building management for the correct unit number, building name, and DEWA premise number. Do not guess the premise number because using the wrong property details can delay activation.""",

            """Prepare your key documents before applying. You may need your signed tenancy contract, Ejari details once available, Emirates ID if available, passport or visa details if requested, and a valid payment method for the security deposit and activation charges.""",

            """Use the official <a href="https://dewa.gov.ae/en/consumer/supply-management/activation-of-electricity-water-move-in" target="_blank">DEWA Move-In service</a>. This is the correct place to activate electricity and water for a new home in Dubai. Avoid relying on unofficial pages for final fees or timelines.""",

            """Submit the move-in request with your property and tenant details. Carefully review the account information, premise number, mobile number, email address, and tenancy details before confirming the request.""",

            """Pay the required DEWA charges through official channels. DEWA’s official page currently lists a refundable security deposit of AED 2,000 for apartments or AED 4,000 for villas, plus a supply activation fee of AED 155. Always confirm the final amount on the official DEWA page at the time of applying.""",

            """Wait for activation and keep the payment confirmation. DEWA notes that if electricity and water supply is not activated within 15 working hours after security deposit payment, the customer should contact DEWA Customer Care.""",

            """After activation, save your DEWA account number, payment receipt, and confirmation email. You will need these for bill payments, move-out, deposit refund, and future service requests.""",
        ],
        "accent": "#BC8653",
        "motif": "M 0,20 Q 30,0 60,20 Q 90,40 120,20",
    },

    "Ejari": {
        "number": "02",
        "tag": "Rental Registration",
        "description": "Your tenancy contract, made official — required before almost everything else.",
        "steps": [
            """First, make sure your tenancy contract is signed and accurate. Check the tenant name, landlord name, property details, rent amount, contract dates, and unit number before starting Ejari registration.""",

            """Prepare the required documents. These may include the signed tenancy contract, tenant Emirates ID if available, passport and visa details if requested, landlord details, property/title deed information, and payment method.""",

            """Choose the official registration route. Dubai Land Department explains that customers can register or renew a tenancy contract through a Real Estate Trustee Centre, property management company if applicable, the Ejari system, or Dubai REST.""",

            """Submit the required information and documents through the selected official channel. Make sure scans or uploaded files are clear, complete, and match the details in the tenancy contract.""",

            """Pay the service fees shown by the official Ejari/Dubai Land Department channel. Do not rely on old screenshots or unofficial fee lists because service fees can change depending on the channel.""",

            """Wait for review and approval. Dubai Land Department states that after the information is submitted, an employee reviews and approves the request through the system.""",

            """Download and save your e-Contract Registration Certificate once issued. Keep a copy in your relocation folder because Ejari is commonly needed for DEWA, telecom setup, housing records, and other move-in processes.""",

            """Official starting point: <a href="https://dubailand.gov.ae/en/eservices/register-renew-ejari-contract/" target="_blank">Dubai Land Department — Register / Renew Ejari Contract</a>.""",
        ],
        "accent": "#8C8A67",
        "motif": "M 0,10 L 20,30 L 40,10 L 60,30 L 80,10 L 100,30 L 120,10",
    },

    "du / e&": {
        "number": "03",
        "tag": "Mobile & SIM",
        "description": "Stay connected from day one — your first local number sets everything else in motion.",
        "steps": [
            """Decide whether you need a tourist/visitor line or a resident mobile plan. If you just arrived, a tourist SIM or eSIM may be enough at first. Once you have Emirates ID, you can move to a regular prepaid or postpaid resident plan.""",

            """Check your phone compatibility before buying an eSIM. Make sure your phone supports eSIM, is unlocked, and can work with UAE mobile networks. If not, choose a physical SIM instead.""",

            """Prepare identification. Visitors usually need passport details. UAE residents usually need Emirates ID for mobile registration or renewal. Keep your documents ready before visiting a store or applying online.""",

            """Compare data needs realistically. If you use Google Maps, WhatsApp calls, food delivery apps, university/work commute apps, or hotspot, choose a package with enough data rather than only the cheapest option.""",

            """Use official provider channels. For e&, start from the official <a href="https://www.eand.ae/en/c/mobile/plans/visitor-line.html" target="_blank">e& Visitor Line</a> page if you are a visitor. For du, start from the official <a href="https://shop.du.ae/en/personal/prepaid/du-tourist-prepaid-plans?view=bundles" target="_blank">du Tourist SIM</a> page.""",

            """Keep your mobile registration updated. The UAE telecom registration process is regulated by TDRA, and providers require valid identity details. You can check TDRA’s <a href="https://tdra.gov.ae/en/initiatives/registration-for-mobile-consumers" target="_blank">Registration for Mobile Consumers</a> page for official context.""",

            """After activation, download the provider app, monitor data usage, check auto-renewal settings, and save customer support details. This helps avoid unexpected balance deductions or service interruptions.""",
        ],
        "accent": "#B27960",
        "motif": "M 0,15 C 20,0 40,30 60,15 C 80,0 100,30 120,15",
    },

    "Internet": {
        "number": "04",
        "tag": "Home Broadband",
        "description": "Fast, reliable internet — book early, because installation takes time.",
        "steps": [
            """Before choosing a provider, ask building management which home internet providers are available in your building. Some buildings may support one provider better than another, so check coverage before signing up.""",

            """Decide whether you are setting up a new home connection or relocating an existing one. If you already have e& home internet, use the official <a href="https://www.eand.ae/en/c/home/home-moving.html" target="_blank">e& Home Move</a> flow. e& describes the process through the e& UAE app: open the eLife Plan tab, tap Manage, then tap Home Move.""",

            """If you already have du Home, use the official <a href="https://www.du.ae/personal/at-home/moving-to-a-new-home" target="_blank">du Home Relocation</a> page. du states that relocation can be done online, and that users may need to upload a tenancy contract or title deed for the new home.""",

            """Prepare your documents. You may need Emirates ID, tenancy contract, title deed if applicable, proof of relationship if the tenancy is not under your name, and your current account details if relocating an existing service.""",

            """Check fees and contract terms before confirming. du currently states that a moving fee of AED 100 will be charged on the next bill for home relocation. For any provider, always confirm final fees, contract length, early cancellation terms, and installation conditions through the official flow.""",

            """Book installation early. Choose a technician appointment when someone can access the apartment, telecom cabinet, router location, and building facilities if needed.""",

            """After installation, test the connection in multiple rooms. Check Wi-Fi speed near your work/study area, bedroom, and living room. If coverage is weak, ask about router placement or mesh options before closing the installation issue.""",
        ],
        "accent": "#B59275",
        "motif": "M 0,20 L 30,5 L 60,20 L 90,5 L 120,20",
    },

    "Move-in Documents": {
        "number": "05",
        "tag": "Document Checklist",
        "description": "The paperwork that underpins everything — keep these within reach at all times.",
        "steps": [
            """Create one digital folder for your move-in documents. Use clear file names such as passport.pdf, tenancy-contract.pdf, ejari.pdf, dewa-receipt.pdf, and internet-installation.pdf so you can find them quickly.""",

            """Keep your passport copy and visa or entry permit ready. These may be requested during early relocation tasks, telecom registration, tenancy steps, or identity verification depending on your status.""",

            """Keep your Emirates ID or Emirates ID application details ready once available. Emirates ID is especially important for resident telecom registration, UAE PASS, banking, and many local services.""",

            """Save your signed tenancy contract and Ejari certificate. These are core housing documents and may be needed for utilities, internet setup, address verification, and other move-in services.""",

            """Save DEWA payment receipts, account number, and activation confirmation. These can help if activation is delayed, billing details need to be checked, or move-out/deposit refund is needed later.""",

            """Save telecom account details, installation appointment confirmations, technician reference numbers, and router/equipment details. This makes troubleshooting easier if internet activation is delayed.""",

            """Avoid storing sensitive documents in random WhatsApp chats only. Use a secure cloud folder, password-protected device, or trusted document storage method. Do not upload passport, Emirates ID, or visa documents into public tools or shared repositories.""",
        ],
        "accent": "#642A16",
        "motif": "M 10,25 A 20,20 0 0 1 50,5 A 20,20 0 0 1 90,25 A 20,20 0 0 1 50,45 A 20,20 0 0 1 10,25",
    },
}
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
    /* ---- HERO (simple, like main page) ---- */
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

    /* ---- TIP CARD (optional, kept) ---- */
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

    /* ---- SECTION LABEL ---- */
    .util-section-label {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.75rem;
        animation: fadeUp 0.9s ease-out 0.2s both;
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

    /* ---- PINTEREST CARD ---- */
    .util-pin-card {
        background: #FFF9F0;
        border: 1px solid rgba(140, 138, 103, 0.20);
        border-radius: 24px;
        overflow: hidden;
        transition: transform 0.22s ease, box-shadow 0.22s ease;
        cursor: pointer;
        box-shadow: 0 4px 18px rgba(100, 42, 22, 0.06);
        margin-bottom: 0.85rem;
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .util-pin-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 44px rgba(100, 42, 22, 0.13);
    }

    .util-pin-top {
        padding: 1.5rem 1.5rem 0.6rem 1.5rem;
        position: relative;
        flex: 1;
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
        margin-top: auto;
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

    /* hide the actual Streamlit button */
    div[data-testid="column"] > div[data-testid="stButton"] {
        display: none !important;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 820px) {
        .hero-content h1 {
            font-size: 2.2rem;
        }
        .tip-card {
            flex-direction: column;
            text-align: center;
            gap: 0.3rem;
        }
        .util-section-label {
            flex-direction: column;
            align-items: flex-start;
        }
    }
    @media (max-width: 480px) {
        .hero-content h1 {
            font-size: 1.8rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)



# ── HERO (simple) ──────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="utilities-hero">
        <div class="hero-pattern"></div>
        <div class="hero-content">
            <div class="hero-icon">⚡</div>
            <h1>Utilities</h1>
            <p>Everything you need to activate before you feel at home – electricity, contracts, connectivity, and the documents that tie it all together.</p>
            <div class="hero-underline"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ── QUICK TIP ──────────────────────────────────────────────────────────────

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


# ── SECTION LABEL ──────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="util-section-label">
        <span class="util-section-label-text">Choose a setup area</span>
        <div class="util-section-label-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ── CARD GRID ──────────────────────────────────────────────────────────────

items = list(UTILITIES.items())
cols = st.columns(3)

for idx, (name, item) in enumerate(items):
    with cols[idx % 3]:
        step_count = len(item["steps"])
        motif_d = item["motif"]
        accent = item["accent"]

        # Unique button ID for this card
        btn_key = f"util_btn_{idx}"

        # Card with onclick that triggers the hidden button
        st.markdown(
            f"""
            <div class="util-pin-card" onclick="document.getElementById('{btn_key}').click();">
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

        # Hidden button – it will be triggered by the card click
        if st.button(" ", key=btn_key):
            show_utility_modal(name, item)
