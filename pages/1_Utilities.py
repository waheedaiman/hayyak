import streamlit as st

from src.ui import apply_hayyak_theme, arabic_divider, render_nav

st.set_page_config(
    page_title="Hayyak | Utilities",
    page_icon="🔌",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="utilities")


# ── ORIGINAL DATA STRUCTURE (exactly as you first provided) ────────────────
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


# ── MODAL WITH TABS – only shows tabs that have content ────────────────────
@st.dialog("Utility setup guide")
def show_utility_modal(name, item):
    accent = item.get("accent", "#8C8A67")
    tag = item.get("tag", "")
    description = item.get("description", "")
    steps = item.get("steps", [])
    quick_info = item.get("quick_info", [])        # not present → empty list
    important_notes = item.get("important_notes", [])
    official_links = item.get("official_links", [])
    footer_note = item.get("footer_note", "")

    # Build a list of (tab_id, label, content_html) only for non‑empty sections
    tabs_to_show = []

    # Quick Info (if data exists)
    if quick_info:
        quick_html = ""
        for info in quick_info:
            if isinstance(info, dict):
                title = info.get("title", info.get("label", ""))
                body = info.get("body", info.get("text", ""))
            else:
                title, body = "", str(info)
            if title or body:
                quick_html += f"""
                <div class="hy-modal-pill">
                    <span class="hy-modal-pill-icon">i</span>
                    <div>
                        <strong>{title}</strong>
                        <p>{body}</p>
                    </div>
                </div>
                """
        if quick_html:
            tabs_to_show.append(("quick", "Quick Info", quick_html))

    # Setup Guide (always present)
    steps_html = ""
    for idx, step in enumerate(steps, 1):
        # step can be a string or a dict with title/body
        if isinstance(step, dict):
            title = step.get("title", f"Step {idx}")
            body = step.get("body", step.get("text", ""))
        else:
            title = f"Step {idx}"
            body = step
        steps_html += f"""
        <div class="hy-step-card">
            <div class="hy-step-number">{idx:02d}</div>
            <h4>{title}</h4>
            <p>{body}</p>
        </div>
        """
    if steps_html:
        tabs_to_show.append(("guide", "Setup Guide", steps_html))

    # Important Notes (if data exists)
    if important_notes:
        notes_html = ""
        for note in important_notes:
            if isinstance(note, dict):
                title = note.get("title", note.get("label", ""))
                body = note.get("body", note.get("text", ""))
            else:
                title, body = "", str(note)
            if title or body:
                notes_html += f"""
                <div class="hy-note-row">
                    <span class="hy-note-icon">!</span>
                    <div>
                        <strong>{title}</strong>
                        <p>{body}</p>
                    </div>
                </div>
                """
        if notes_html:
            tabs_to_show.append(("notes", "Important", notes_html))

    # Official Links (if data exists)
    if official_links:
        links_html = ""
        for link in official_links:
            if isinstance(link, dict):
                label = link.get("title", link.get("label", "Official link"))
                url = link.get("url", link.get("href", "#"))
            else:
                label, url = str(link), "#"
            links_html += f"""
            <a class="hy-official-link" href="{url}" target="_blank">
                <span>↗</span>
                <div>
                    <strong>{label}</strong>
                    <small>{url}</small>
                </div>
            </a>
            """
        if links_html:
            tabs_to_show.append(("links", "Official Links", links_html))

    # Footer note (only shown inside Quick Info tab if no Quick Info tab,
    # otherwise we can put it at the bottom of the modal – optional)
    footer_block = ""
    if footer_note:
        footer_block = f"""
        <div class="hy-footer-note">
            {footer_note}
        </div>
        """

    # Build the HTML radio tabs only if we have >1 tab; otherwise show just the content
    if len(tabs_to_show) > 1:
        # Unique name based on utility name
        safe_name = name.lower().replace(" ", "-").replace("/", "").replace("&", "and")
        radios = ""
        labels = ""
        panels = ""
        for i, (tab_id, tab_label, tab_content) in enumerate(tabs_to_show):
            checked = "checked" if i == 0 else ""
            radios += f'<input class="hy-modal-radio" type="radio" name="utility-tabs-{safe_name}" id="tab-{tab_id}-{safe_name}" {checked}>\n'
            labels += f'<label class="hy-modal-tab-label" for="tab-{tab_id}-{safe_name}">{tab_label}</label>\n'
            panels += f'<div class="hy-modal-panel hy-panel-{tab_id}">{tab_content} {footer_block if tab_id == "quick" and not quick_info else ""}</div>\n'
        # If footer is not placed in a specific panel, add it after panels
        if footer_block and not quick_info:
            footer_block = ""  # we will append it after all panels

        tab_structure = f"""
        <div class="hy-modal-tabs">
            {labels}
        </div>
        <div class="hy-modal-pages">
            {panels}
            {footer_block}
        </div>
        """
    else:
        # Only one tab – just display the content
        if tabs_to_show:
            tab_id, tab_label, content = tabs_to_show[0]
            tab_structure = f"""
            <div class="hy-modal-pages" style="max-height: 58vh; overflow-y: auto;">
                {content}
                {footer_block}
            </div>
            """
        else:
            tab_structure = ""

    # Full modal HTML
    st.markdown(
        f"""
        <style>
        [data-testid="stDialog"] {{
            background: rgba(43, 27, 20, 0.22) !important;
        }}
        [data-testid="stDialog"] > div {{
            background: #FFF9F0 !important;
            border: 1px solid rgba(140, 138, 103, 0.25) !important;
            border-radius: 28px !important;
            box-shadow: 0 28px 80px rgba(43, 27, 20, 0.22) !important;
            color: #2B1B14 !important;
        }}
        [data-testid="stDialog"] * {{
            color: inherit;
        }}
        .hy-modal-shell {{
            background: radial-gradient(circle at top right, rgba(140, 138, 103, 0.13), transparent 28%),
                        linear-gradient(135deg, #FFF9F0 0%, #F6EFE5 100%);
            border-radius: 24px;
            overflow: hidden;
            color: #2B1B14;
            font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }}
        .hy-modal-header {{
            display: grid;
            grid-template-columns: auto 1fr;
            gap: 1rem;
            align-items: center;
            padding: 1.15rem 1.2rem 0.95rem 1.2rem;
            border-bottom: 1px solid rgba(140, 138, 103, 0.18);
        }}
        .hy-modal-mark {{
            width: 72px;
            height: 72px;
            border-radius: 22px;
            background: {accent};
            display: flex;
            align-items: center;
            justify-content: center;
            color: #FFF9F0;
            font-weight: 900;
            font-size: 1.15rem;
            box-shadow: 0 16px 32px rgba(100, 42, 22, 0.14);
        }}
        .hy-modal-kicker {{
            color: {accent};
            font-size: 0.72rem;
            font-weight: 900;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            margin-bottom: 0.2rem;
        }}
        .hy-modal-title {{
            margin: 0;
            color: #642A16;
            font-size: 2rem;
            line-height: 1;
            letter-spacing: -0.04em;
        }}
        .hy-modal-subtitle {{
            margin: 0.35rem 0 0 0;
            color: #735A4C;
            line-height: 1.45;
            font-size: 0.95rem;
        }}
        .hy-modal-body {{
            padding: 1rem 1.2rem 1.15rem 1.2rem;
        }}
        .hy-modal-tabs {{
            display: flex;
            gap: 0.6rem;
            margin-bottom: 1rem;
            border-bottom: 1px solid rgba(140, 138, 103, 0.18);
            padding-bottom: 0.8rem;
            flex-wrap: wrap;
        }}
        .hy-modal-radio {{
            display: none;
        }}
        .hy-modal-tab-label {{
            padding: 0.65rem 1rem;
            border-radius: 999px;
            background: rgba(140, 138, 103, 0.12);
            border: 1px solid rgba(140, 138, 103, 0.22);
            color: #642A16;
            font-size: 0.78rem;
            font-weight: 900;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            cursor: pointer;
            transition: 0.18s ease;
        }}
        .hy-modal-tab-label:hover {{
            background: rgba(140, 138, 103, 0.2);
        }}
        .hy-modal-panel {{
            display: none;
        }}
        .hy-modal-pages {{
            max-height: 58vh;
            overflow-y: auto;
            padding-right: 0.4rem;
        }}
        /* Active tab style – targets the correct radio & label combo */
        {''.join([f'#tab-{tab_id}-{safe_name}:checked ~ .hy-modal-tabs label[for="tab-{tab_id}-{safe_name}"]'
                  for tab_id, _, _ in tabs_to_show]) if len(tabs_to_show) > 1 else ""}
        {{
            background: {accent};
            color: #FFF9F0;
            border-color: {accent};
        }}
        {''.join([f'#tab-{tab_id}-{safe_name}:checked ~ .hy-modal-pages .hy-panel-{tab_id}'
                  for tab_id, _, _ in tabs_to_show]) if len(tabs_to_show) > 1 else ""}
        {{
            display: block;
        }}
        .hy-section-label {{
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin: 0.25rem 0 0.75rem 0;
            color: #642A16;
            font-size: 0.76rem;
            font-weight: 900;
            letter-spacing: 0.16em;
            text-transform: uppercase;
        }}
        .hy-section-label:after {{
            content: "";
            height: 1px;
            flex: 1;
            background: linear-gradient(90deg, rgba(140, 138, 103, 0.42), transparent);
        }}
        .hy-step-grid {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.65rem;
        }}
        .hy-step-card {{
            position: relative;
            min-height: 150px;
            background: rgba(255, 249, 240, 0.90);
            border: 1px solid rgba(188, 134, 83, 0.22);
            border-radius: 18px;
            padding: 0.85rem 0.8rem 0.8rem 0.8rem;
            box-shadow: 0 10px 24px rgba(100, 42, 22, 0.055);
        }}
        .hy-step-card:after {{
            content: "";
            position: absolute;
            left: 0.85rem;
            right: 0.85rem;
            bottom: 0;
            height: 3px;
            border-radius: 999px 999px 0 0;
            background: {accent};
            opacity: 0.86;
        }}
        .hy-step-number {{
            width: 30px;
            height: 30px;
            border-radius: 999px;
            background: {accent};
            color: #FFF9F0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 900;
            font-size: 0.76rem;
            margin-bottom: 0.65rem;
        }}
        .hy-step-card h4 {{
            margin: 0 0 0.35rem 0;
            color: #642A16;
            font-size: 0.95rem;
            line-height: 1.18;
        }}
        .hy-step-card p {{
            margin: 0;
            color: #2B1B14;
            font-size: 0.78rem;
            line-height: 1.45;
        }}
        .hy-step-card a, .hy-official-link {{
            color: #2D5B7C !important;
            font-weight: 800;
            text-decoration: none;
        }}
        .hy-note-row {{
            display: flex;
            gap: 0.65rem;
            padding: 0.65rem 0;
            border-bottom: 1px solid rgba(140, 138, 103, 0.14);
        }}
        .hy-note-row:last-child {{
            border-bottom: 0;
        }}
        .hy-official-link {{
            display: flex;
            gap: 0.65rem;
            align-items: flex-start;
            padding: 0.65rem 0;
            border-bottom: 1px solid rgba(140, 138, 103, 0.14);
        }}
        .hy-official-link:last-child {{
            border-bottom: 0;
        }}
        .hy-official-link span {{
            color: {accent};
            font-weight: 900;
            flex-shrink: 0;
        }}
        .hy-official-link strong {{
            color: #2D5B7C;
            display: block;
            font-size: 0.82rem;
        }}
        .hy-official-link small {{
            color: #735A4C;
            word-break: break-word;
            line-height: 1.25;
        }}
        .hy-footer-note {{
            margin-top: 0.8rem;
            background: rgba(140, 138, 103, 0.12);
            border: 1px solid rgba(140, 138, 103, 0.20);
            border-radius: 16px;
            padding: 0.7rem 0.8rem;
            color: #735A4C;
            font-size: 0.78rem;
            line-height: 1.45;
        }}
        .hy-empty-text {{
            color: #735A4C;
            font-size: 0.8rem;
            margin: 0;
        }}
        @media (max-width: 900px) {{
            .hy-step-grid {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
        }}
        @media (max-width: 560px) {{
            .hy-modal-header {{
                grid-template-columns: 1fr;
            }}
            .hy-step-grid {{
                grid-template-columns: 1fr;
            }}
        }}
        </style>

        <div class="hy-modal-shell">
            <div class="hy-modal-header">
                <div class="hy-modal-mark">{item.get("number", "")}</div>
                <div>
                    <div class="hy-modal-kicker">{tag}</div>
                    <h2 class="hy-modal-title">{name}</h2>
                    <p class="hy-modal-subtitle">{description}</p>
                </div>
            </div>
            <div class="hy-modal-body">
                {radios if len(tabs_to_show) > 1 else ""}
                {tab_structure}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── PAGE LAYOUT (unchanged) ────────────────────────────────────────────────
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

# ── CARD GRID (unchanged) ─────────────────────────────────────────────────
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