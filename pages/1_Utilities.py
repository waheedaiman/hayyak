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

@st.dialog("Utility setup guide")
def show_utility_modal(name, item):
    st.subheader(name)
    st.caption(item["description"])
    arabic_divider()

    st.markdown(item["steps"])

    st.divider()
    st.caption(
        "Hayyak note: official processes, fees, required documents, and timelines can change. "
        "Always confirm details through the linked official service before applying."
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
                    Each card opens a focused guide instead of forcing users
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

st.markdown("</div>", unsafe_allow_html=True)
