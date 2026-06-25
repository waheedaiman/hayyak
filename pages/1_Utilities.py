import streamlit as st

from src.ui import apply_hayyak_theme, arabic_divider, render_nav

st.set_page_config(
    page_title="Hayyak | Utilities",
    page_icon="🔌",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="utilities")

# ── UPDATED DATA: all utilities with new structured info ──────────────
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
        "quick_info": {
            "activation": "Up to 15 working hours*",
            "deposit": "AED 2,000 (Apt) / AED 4,000 (Villa)",
        },
        "important_notes": [
            "🕒 <strong>Activation after deposit</strong>: DEWA states up to 15 working hours for supply activation.",
            "💰 <strong>Refundable deposit</strong>: AED 2,000 for apartments, AED 4,000 for villas.",
            "✅ <strong>Keep all receipts safe</strong>: You may need them for move-out or deposit refund.",
            "ℹ️ <strong>Charges may change</strong>: Always confirm the latest amounts on the official DEWA website.",
        ],
        "official_links": [
            {
                "title": "DEWA Move-In Service",
                "url": "https://dewa.gov.ae/en/consumer/supply-management/activation-of-electricity-water-move-in",
            },
            {
                "title": "DEWA Official Website",
                "url": "https://dewa.gov.ae",
            },
        ],
        "footer_note": "* As per DEWA: If supply is not activated within 15 working hours after security deposit payment, please contact DEWA Customer Care.",
    },

    "Ejari": {
        "number": "02",
        "tag": "Rental Registration",
        "description": "Your tenancy contract, made official — required before almost everything else.",
        "steps": [
            """Make sure your tenancy contract is signed and accurate before registration. Check: tenant name, landlord name, property address, unit number, rent amount, contract start and end dates.""",
            """Prepare the documents likely needed for registration: signed tenancy contract, tenant Emirates ID (if available), passport/visa details (if requested), landlord details, property or title deed information (if requested), and a payment method.""",
            """Use an approved Ejari registration route. Dubai Land Department states that registration can be done through channels such as a Real Estate Trustee Centre, a property management company (if the property is managed by one), the Ejari system, or the Dubai REST app.""",
            """Fill in the required information and upload or submit the required documents. Ensure all documents are clear, complete, and match the tenancy contract.""",
            """Proceed to pay the official service fees shown by the approved registration channel. Do not rely on old screenshots or unofficial fee lists because fees can change.""",
            """Dubai Land Department explains that after submission, the request is reviewed and approved through the system.""",
            """Once approved, you receive the **e‑Contract Registration Certificate**. Save it safely because you may need it for DEWA, internet setup, address proof, and other move‑in requirements.""",
        ],
        "accent": "#8C8A67",
        "motif": "M 0,10 L 20,30 L 40,10 L 60,30 L 80,10 L 100,30 L 120,10",
        "quick_info": {
            "Main purpose": "Official tenancy contract registration",
            "Official authority": "Dubai Land Department / Ejari",
        },
        "important_notes": [
            "📄 <strong>Ejari comes before many services</strong> – often needed before or during DEWA, internet, housing documentation, and other move‑in processes.",
            "✅ <strong>Contract details must match</strong> – wrong unit numbers, names, or dates can delay registration.",
            "🏢 <strong>Use approved channels only</strong> – use Dubai Land Department, Dubai REST, Ejari system, Real Estate Trustee Centres, or approved property management channels.",
            "ℹ️ <strong>Fees and requirements may change</strong> – always confirm the latest requirements through Dubai Land Department or the official channel you are using.",
        ],
        "official_links": [
            {
                "title": "Dubai Land Department — Register / Renew Rental Contract",
                "url": "https://dubailand.gov.ae/en/eservices/register-renew-ejari-contract/",
            },
            {
                "title": "Dubai Land Department Official Website",
                "url": "https://dubailand.gov.ae",
            },
        ],
        "footer_note": "Ejari requirements, documents, channels, and fees may change. Always verify the latest details through Dubai Land Department or an authorised Ejari registration channel.",
    },

    "du / e&": {
        "number": "03",
        "tag": "Mobile & SIM",
        "description": "Stay connected from day one — your first local number sets everything else in motion.",
        "steps": [
            """Decide whether you need a temporary visitor line or a resident mobile plan. If you have just arrived, a tourist SIM or visitor line is usually the fastest option. Once your Emirates ID is ready, you can move to regular prepaid or postpaid options.""",
            """Before choosing eSIM, confirm that your phone supports eSIM and is not carrier locked. If your phone does not support eSIM, use a physical SIM.""",
            """Visitors usually need passport details. Residents usually need Emirates ID for mobile registration or renewal. TDRA states that licensed telecom providers must register subscriber data accurately with proper documentation such as Emirates ID.""",
            """Choose your mobile package based on actual daily use. Think about: Google Maps, WhatsApp, ride‑hailing apps, delivery apps, work or university commute, hotspot usage, video calls.""",
            """Use official du or e& channels rather than random third‑party sellers. For visitors, start from the official visitor/tourist plan pages.""",
            """Follow the provider’s activation process. For eSIM, scan the QR code only on the phone you want to activate. Keep Wi‑Fi available during setup in case mobile data is not active yet."""",
            """Download the provider app after activation. Use it to check remaining data, balance, auto‑renewal, add‑ons, Emirates ID registration status, and customer support options.""",
        ],
        "accent": "#B27960",
        "motif": "M 0,15 C 20,0 40,30 60,15 C 80,0 100,30 120,15",
        "quick_info": {
            "Best for arrival": "Tourist SIM / visitor line or prepaid plan",
            "Resident registration": "Usually requires valid identity documentation such as Emirates ID",
        },
        "important_notes": [
            "🪪 <strong>Emirates ID matters</strong> – for resident mobile services, Emirates ID registration is important. e& states that the original Emirates ID is the accepted document through its self‑service registration channels.",
            "📱 <strong>eSIM needs a compatible phone</strong> – not every phone supports eSIM. Check before buying.",
            "🔄 <strong>Watch auto‑renewal</strong> – some bundles renew automatically. Check this in the app to avoid unexpected deductions.",
            "⚠️ <strong>Keep SIMs under your name</strong> – TDRA’s mobile registration initiative aims to protect subscriber rights and reduce misuse, fraud, and scams.",
        ],
        "official_links": [
            {
                "title": "TDRA — Registration for Mobile Consumers",
                "url": "https://tdra.gov.ae/en/initiatives/registration-for-mobile-consumers",
            },
            {
                "title": "e& Visitor Line",
                "url": "https://eand.ae/en/c/mobile/plans/visitor-line.html",
            },
            {
                "title": "du Tourist SIM",
                "url": "https://shop.du.ae/en/personal/prepaid/du-tourist-prepaid-plans",
            },
            {
                "title": "e& Mobile Registration / Emirates ID Guidance",
                "url": "https://eand.ae",
            },
        ],
        "footer_note": "Telecom registration rules, plan prices, tourist SIM validity, and Emirates ID requirements can change. Always check du, e&, and TDRA official channels before choosing a plan.",
    },

    "Internet": {
        "number": "04",
        "tag": "Home Broadband",
        "description": "Fast, reliable internet — book early, because installation takes time.",
        "steps": [
            """Before choosing a package, ask your building management which provider is available or better supported in your building. Some buildings may support du, e&, or both, but coverage and installation experience can vary.""",
            """Choose whether you are setting up a brand‑new home internet connection or moving an existing connection (du Home or e& eLife). Relocation flows and documents can differ.""",
            """For e&, the official Home Move page says the process is done through the **e& UAE app**: download the app, tap **Manage** on the eLife Plan tab, tap **Home Move**, and follow the instructions. For du, the official relocation page allows users to relocate du Home services online.""",
            """Prepare: tenancy contract or title deed, Emirates ID (if requested), new home address and unit number, current account details (if relocating), and proof of relationship if the tenancy is not in your name. du specifically states that you may need to upload the tenancy contract or title deed for the new home.""",
            """Check relocation fees, installation charges, contract duration, early cancellation terms, and outstanding bills before confirming. du currently states that a moving fee of **AED 100** will be charged on the next bill for relocation.""",
            """Choose an installation slot when someone can access the apartment. Make sure the technician can reach the apartment, telecom cabinet, router location, and TV/landline area (if included).""",
            """After installation, test the connection in multiple rooms. Check Wi‑Fi speed near your desk, bedroom signal, living room signal, video call stability, and TV box or landline (if included).""",
        ],
        "accent": "#B59275",
        "motif": "M 0,20 L 30,5 L 60,20 L 90,5 L 120,20",
        "quick_info": {
            "Main providers": "du and e&",
            "Key requirement": "Building coverage and tenancy / title deed documentation",
        },
        "important_notes": [
            "🏢 <strong>Building coverage comes first</strong> – do not choose a plan only by price. First check what your building actually supports.",
            "📄 <strong>Tenancy or title deed may be needed</strong> – for relocation or new setup, providers may ask for proof of address.",
            "💰 <strong>Relocation fees may apply</strong> – du currently lists a moving fee of AED 100 for home relocation, but always confirm final charges during the official request.",
            "🧰 <strong>Keep equipment safe</strong> – do not throw away routers, TV boxes, remotes, cables, or power adapters before confirming provider instructions.",
        ],
        "official_links": [
            {
                "title": "e& Home Move",
                "url": "https://eand.ae/en/c/home/home-moving.html",
            },
            {
                "title": "du Home Relocation",
                "url": "https://du.ae/personal/at-home/moving-to-a-new-home",
            },
            {
                "title": "e& Official Website",
                "url": "https://eand.ae",
            },
            {
                "title": "du Official Website",
                "url": "https://du.ae",
            },
        ],
        "footer_note": "Home internet coverage, installation timelines, relocation fees, and required documents vary by provider and building. Always confirm details directly through du or e& before booking.",
    },

    "Move-in Documents": {
        "number": "05",
        "tag": "Document Checklist",
        "description": "The paperwork that underpins everything — keep these within reach at all times.",
        "steps": [
            """Create a dedicated folder for your move‑in documents. Suggested folder names: “Dubai Move‑in Documents”, “Hayyak Relocation Folder”, or “Apartment Setup Files”. Use clear filenames so you can find documents quickly.""",
            """Keep copies of: passport, visa or entry permit (if applicable), Emirates ID (once available), and Emirates ID application details (if still processing). These may be needed for telecom registration, tenancy tasks, banking, or identity verification.""",
            """Keep your housing documents together: signed tenancy contract, Ejari certificate, landlord/agent contact details, building management contact details, unit number and building name. Ejari and tenancy documents are especially important because they connect to utilities and other move‑in services.""",
            """Keep copies of: DEWA account number, DEWA payment receipt, security deposit receipt, activation confirmation, and any customer care reference numbers. You may need these for billing, service issues, move‑out, or deposit refund.""",
            """Keep copies of: du or e& account number, SIM registration details, internet installation appointment confirmation, router/equipment details, technician reference number, and plan contract/package details.""",
            """Save receipts for: rent payments, security deposit, agency fees (if applicable), DEWA deposit, internet setup or relocation fees, Ejari registration fees. Receipts are useful if there is a dispute, refund, delay, or service issue.""",
            """Do not store passport, visa, Emirates ID, or tenancy documents only in WhatsApp chats. Use a secure cloud folder, password‑protected device, or trusted storage system. Never upload sensitive documents to GitHub, public folders, or public AI tools.""",
        ],
        "accent": "#642A16",
        "motif": "M 10,25 A 20,20 0 0 1 50,5 A 20,20 0 0 1 90,25 A 20,20 0 0 1 50,45 A 20,20 0 0 1 10,25",
        "quick_info": {
            "Main purpose": "Keep housing, identity, and utility documents ready",
            "Safety note": "Do not upload sensitive documents to public repositories or shared links",
        },
        "important_notes": [
            "🔐 <strong>Avoid public uploads</strong> – never upload passport, Emirates ID, visa, tenancy contract, or receipts to public repositories.",
            "📁 <strong>Use clear file names</strong> – bad filenames like `scan123.pdf` are hard to find later. Use names like `ejari-certificate.pdf`.",
            "🧾 <strong>Keep receipts</strong> – receipts can matter for refunds, move‑out, billing disputes, and service delays.",
            "🪪 <strong>Emirates ID becomes increasingly important</strong> – many resident services become easier once your Emirates ID is available.",
        ],
        "official_links": [
            {
                "title": "Dubai Land Department",
                "url": "https://dubailand.gov.ae",
            },
            {
                "title": "DEWA",
                "url": "https://dewa.gov.ae",
            },
            {
                "title": "TDRA",
                "url": "https://tdra.gov.ae",
            },
            {
                "title": "UAE Government Portal — Emirates ID",
                "url": "https://u.ae/en/information-and-services/visa-and-emirates-id/emirates-id",
            },
        ],
        "footer_note": "Move‑in documents often contain sensitive personal information. Store them securely and never commit them to GitHub or share them through public links.",
    },
}

# ── REDESIGNED MODAL: tabs when extra info exists ──────────────────────
@st.dialog("Utility setup guide")
def show_utility_modal(name, item):
    # Header (always visible)
    st.markdown(
        f"""<div style="margin-bottom:0.25rem;">
            <span style="font-size:0.72rem; font-weight:800; letter-spacing:0.22em;
                         text-transform:uppercase; color:{item['accent']};">
                {item['tag']}
            </span>
        </div>""",
        unsafe_allow_html=True,
    )
    st.subheader(name)
    st.caption(item["description"])
    arabic_divider()

    # ---- Check if we have the new detailed structure ----
    has_tabs = any(k in item for k in ("quick_info", "important_notes", "official_links"))

    if has_tabs:
        # Use tabs to organise content without endless scrolling
        tab_labels = ["⚡ Quick Info", "📋 Setup Guide", "❗ Important to Know", "🔗 Official Links"]
        tabs = st.tabs(tab_labels)

        with tabs[0]:  # Quick Info — now generic
            if "quick_info" in item:
                qi = item["quick_info"]
                # Display each key‑value pair in a two‑column layout
                items_list = list(qi.items())
                cols = st.columns(min(2, len(items_list)))
                for idx, (key, value) in enumerate(items_list):
                    with cols[idx % 2]:
                        # Format the key nicely
                        label = key.replace('_', ' ').title()
                        # Choose an emoji based on key
                        emoji = "📌"  # default
                        if "purpose" in key.lower() or "main" in key.lower():
                            emoji = "🎯"
                        elif "authority" in key.lower() or "provider" in key.lower():
                            emoji = "🏛️"
                        elif "requirement" in key.lower():
                            emoji = "🔑"
                        elif "note" in key.lower():
                            emoji = "⚠️"
                        elif "activation" in key.lower():
                            emoji = "🕒"
                        elif "deposit" in key.lower():
                            emoji = "🛡️"
                        elif "arrival" in key.lower():
                            emoji = "✈️"
                        elif "registration" in key.lower():
                            emoji = "🪪"
                        elif "safety" in key.lower():
                            emoji = "🔐"

                        st.markdown(
                            f"""
                            <div style="margin-bottom:0.8rem;">
                                <span style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;
                                             color:{item['accent']}; font-weight:700;">{emoji} {label}</span>
                                <p style="margin:0.2rem 0 0 0; font-size:1.0rem; font-weight:600; color:#2B1B14;">
                                    {value}
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
            else:
                st.info("Quick information will be added soon.")

        with tabs[1]:  # Setup Guide
            st.markdown("**7‑STEP SETUP GUIDE**" if name == "DEWA" else "**Setup checklist**")
            for i, step in enumerate(item["steps"], 1):
                st.markdown(
                    f"""<div style="display:flex; align-items:flex-start; gap:0.75rem;
                                    padding:0.6rem 0; border-bottom:1px solid rgba(140,138,103,0.14);">
                        <span style="min-width:24px; height:24px; border-radius:50%;
                                     background:rgba(140,138,103,0.14);
                                     border:1px solid rgba(140,138,103,0.28);
                                     display:inline-flex; align-items:center; justify-content:center;
                                     font-size:0.72rem; font-weight:800; color:{item['accent']};">
                            {i}
                        </span>
                        <span style="color:#2B1B14; line-height:1.55;">{step}</span>
                    </div>""",
                    unsafe_allow_html=True,
                )

        with tabs[2]:  # Important to Know
            if "important_notes" in item:
                for note in item["important_notes"]:
                    st.markdown(
                        f'<div style="margin-bottom:0.8rem; color:#2B1B14; line-height:1.5;">{note}</div>',
                        unsafe_allow_html=True,
                    )
            else:
                st.info("Important notes will be added soon.")

        with tabs[3]:  # Official Links
            if "official_links" in item:
                for link in item["official_links"]:
                    st.markdown(
                        f'<div style="margin-bottom:0.6rem;">'
                        f'🌐 <a href="{link["url"]}" target="_blank" style="color:{item["accent"]}; '
                        f'text-decoration:none; font-weight:600;">{link["title"]}</a>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )
                # Footer note inside the same tab for convenience
                if "footer_note" in item:
                    st.markdown("---")
                    st.caption(item["footer_note"])
            else:
                st.info("Official links will be added soon.")

    else:
        # Legacy simple checklist (no tabs, just the old layout)
        st.markdown("**Setup checklist**")
        for i, step in enumerate(item["steps"], 1):
            st.markdown(
                f"""<div style="display:flex; align-items:flex-start; gap:0.75rem;
                                padding:0.6rem 0; border-bottom:1px solid rgba(140,138,103,0.14);">
                    <span style="min-width:24px; height:24px; border-radius:50%;
                                 background:rgba(140,138,103,0.14);
                                 border:1px solid rgba(140,138,103,0.28);
                                 display:inline-flex; align-items:center; justify-content:center;
                                 font-size:0.72rem; font-weight:800; color:{item['accent']};">
                        {i}
                    </span>
                    <span style="color:#2B1B14; line-height:1.55;">{step}</span>
                </div>""",
                unsafe_allow_html=True,
            )
        st.markdown(
            """<p style="margin-top:1.1rem; font-size:0.8rem; color:#735A4C;">
                Official links will be added as inline references within each step as the guide develops.
            </p>""",
            unsafe_allow_html=True,
        )

# ── PAGE LAYOUT (including cream background fix for modal) ──────────────
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

    /* ── CREAM BACKGROUND FOR MODAL ── */
    div[data-testid="stDialog"],
    div[data-testid="stDialog"] > div,
    div[data-testid="stDialog"] .stDialogContent,
    div[role="dialog"] {
        background: #FFF9F0 !important;
        border-radius: 24px !important;
    }
    div[data-testid="stDialogOverlay"] {
        background: rgba(255, 249, 240, 0.85) !important;
        backdrop-filter: blur(2px);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── HERO ──────────────────────────────────────────────────────────────────
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

# ── QUICK TIP ─────────────────────────────────────────────────────────────
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

# ── SECTION LABEL ─────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="util-section-label">
        <span class="util-section-label-text">Choose a setup area</span>
        <div class="util-section-label-line"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── CARD GRID ─────────────────────────────────────────────────────────────
items = list(UTILITIES.items())
cols = st.columns(3)

for idx, (name, item) in enumerate(items):
    with cols[idx % 3]:
        step_count = len(item["steps"])
        motif_d = item["motif"]
        accent = item["accent"]

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