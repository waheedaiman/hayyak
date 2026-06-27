import streamlit as st
from src.ui import apply_hayyak_theme, render_nav, arabic_divider

st.set_page_config(
    page_title="Hayyak | Your Dubai Checklist",
    page_icon="",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="checklist")

# ---------- helper: build personalised checklist (unchanged) ----------
def build_personalised_checklist(profile, top_recs):
    budget = profile.get("monthly_budget_aed", 8000)
    commute = profile.get("commute_target", "")
    lifestyle = profile.get("lifestyle", "")
    household = profile.get("household_type", "")
    needs_metro = profile.get("needs_metro", "Metro helpful")
    priority = profile.get("priority", "")

    first_steps_all = []
    for rec in top_recs:
        first_steps_all.extend(rec.get("first_steps", []))

    before = [
        "Shortlist 35 neighbourhoods based on your budget & commute",
        "Prepare identity documents (passport, visa, Emirates ID if applicable)",
        "Estimate total movein costs (rent + deposit + agency fee + DEWA + internet)",
    ]

    if needs_metro.lower().startswith("metro"):
        before.append("Research metro routes and Nol card options")
    else:
        before.append("Compare car ownership costs vs. taxi / ridehail budgets")

    if "family" in household.lower():
        before.append("Check school and nursery catchments in shortlisted areas")
        before.append("Look up familyfriendly community facilities (parks, clinics)")

    if "professional" in household.lower() or "couple" in household.lower():
        before.append("Confirm rental budget allows for a second bedroom / home office")

    if budget <= 6000:
        before.append("Explore studio / sharedapartment options to stay within budget")
    elif budget >= 12000:
        before.append("Research premium buildings with gym, pool, and covered parking")

    if "work" in priority.lower() or "commute" in priority.lower():
        before.append("Test commute time on Google Maps during peak hours")

    first_week = [
        "Inspect apartment in person before signing any contract",
        "Confirm Ejari registration process with landlord / agent",
        "Start DEWA connection (electricity & water)",
        "Arrange home internet & mobile plan (Du / Etisalat)",
    ]

    if "metro" in needs_metro.lower():
        first_week.append("Buy a Nol card and test the nearest metro station")

    if "family" in household.lower():
        first_week.append("Locate nearest supermarket, pharmacy, and clinic")
        first_week.append("Find out about community play areas and family groups")

    if "professional" in household.lower():
        first_week.append("Set up a temporary workspace and test commute timing")

    for step in first_steps_all[:3]:
        if step not in first_week:
            first_week.append(step)

    first_month = [
        "Review commute routine and adjust if needed",
        "Update your Emirates ID, bank, and tenancy contract details",
        "Register with a local GP / clinic",
        "Explore nearby restaurants, gyms, and leisure spots",
    ]

    if "metro" in needs_metro.lower():
        first_month.append("Evaluate metro convenience vs. alternative transport")

    if "family" in household.lower():
        first_month.append("Attend a community event or join a local parenting group")
    else:
        first_month.append("Check out social meetups or sports clubs in the area")

    if "budget" in priority.lower():
        first_month.append("Track monthly expenses against your projected budget")

    first_month.append("Save emergency numbers and building management contacts")

    def unique_ordered(items):
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    return {
        "before_arrival": unique_ordered(before),
        "first_week": unique_ordered(first_week),
        "first_month": unique_ordered(first_month),
    }

# ---------- pagewide styling (inspired by Utilities) ----------
st.markdown(
    f"""
    <style>
    /* hero  same as before */
    .checklist-hero {{
        position: relative;
        padding: 2.5rem 1.5rem 2rem 1.5rem;
        margin-bottom: 1.5rem;
        border-radius: 32px;
        background: linear-gradient(135deg, #F6EFE5 0%, #E8D9C8 100%);
        text-align: center;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(100,42,22,0.06);
    }}
    .hero-pattern {{
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: radial-gradient(circle at 20% 30%, rgba(140,138,103,0.08) 0%, transparent 50%),
                          radial-gradient(circle at 80% 70%, rgba(140,138,103,0.06) 0%, transparent 50%);
        pointer-events: none;
    }}
    .hero-content {{
        position: relative; z-index: 1;
        max-width: 640px; margin: 0 auto;
        animation: fadeUp 0.8s ease-out both;
    }}
    .hero-icon {{ font-size: 3.2rem; line-height: 1; margin-bottom: 0.2rem; }}
    .hero-content h1 {{
        font-size: 2.8rem; margin: 0.2rem 0 0.2rem 0;
        color: #642A16; font-weight: 700; letter-spacing: -0.03em;
    }}
    .hero-content p {{
        font-size: 1.1rem; color: #735A4C;
        max-width: 460px; margin: 0 auto; line-height: 1.5;
    }}
    .hero-underline {{
        width: 50px; height: 3px; background: #8C8A67;
        border-radius: 2px; margin: 0.7rem auto 0 auto;
    }}

    /* tip card */
    .tip-card {{
        display: flex; align-items: center; gap: 1rem;
        background: rgba(255,249,240,0.7); backdrop-filter: blur(4px);
        border: 1px solid rgba(140,138,103,0.18); border-radius: 20px;
        padding: 0.8rem 1.2rem; margin: 0 0 1.5rem 0;
        box-shadow: 0 4px 12px rgba(100,42,22,0.04);
        animation: fadeUp 0.9s ease-out 0.15s both;
    }}
    .tip-icon {{ font-size: 2rem; line-height: 1; flex-shrink: 0; }}
    .tip-text {{ color: #2B1B14; font-size: 0.95rem; }}

    /* tabs */
    div[data-testid="stTabs"] button[data-baseweb="tab"] {{
        background: transparent; border: none;
        color: #735A4C; font-weight: 600;
        padding: 0.6rem 1.2rem; border-radius: 999px;
        margin-right: 0.3rem; transition: all 0.2s ease;
    }}
    div[data-testid="stTabs"] button[data-baseweb="tab"]:hover {{
        background: rgba(140, 138, 103, 0.12); color: #642A16;
    }}
    div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {{
        background: #8C8A67; color: white;
    }}

    /* checklist card anchor - invisible positioning marker */
    .checklist-card {{
        display: none;  /* Don't render empty div */
    }}

    /* Apply card styling to first/only checkbox - top border and rounded corners */
    .checklist-card + div[data-testid="stCheckbox"] {{
        background: #FFF9F0;
        border: 1px solid rgba(140, 138, 103, 0.18);
        border-radius: 24px 24px 0 0;
        padding: 1.2rem 2rem !important;
        margin: 1rem 0 0 0 !important;
        box-shadow: 0 8px 18px rgba(100, 42, 22, 0.05);
    }}

    /* If there's only one checkbox, round the bottom too */
    .checklist-card + div[data-testid="stCheckbox"]:only-of-type {{
        border-radius: 24px;
        border-bottom: 1px solid rgba(140, 138, 103, 0.18);
    }}

    /* Checkboxes between first and last - straight edges */
    .checklist-card + div[data-testid="stCheckbox"] ~ div[data-testid="stCheckbox"]:not(:last-of-type) {{
        background: #FFF9F0;
        border: 1px solid rgba(140, 138, 103, 0.18);
        border-top: none;
        border-radius: 0;
        padding: 0.9rem 2rem !important;
        margin: 0 !important;
        border-bottom: 1px dashed rgba(140,138,103,0.12);
    }}

    /* Last checkbox - bottom border and rounded corners */
    .checklist-card + div[data-testid="stCheckbox"] ~ div[data-testid="stCheckbox"]:last-of-type {{
        background: #FFF9F0;
        border: 1px solid rgba(140, 138, 103, 0.18);
        border-top: none;
        border-radius: 0 0 24px 24px;
        padding: 0.9rem 2rem !important;
        margin: 0 !important;
        border-bottom: 1px solid rgba(140, 138, 103, 0.18);
        box-shadow: 0 8px 18px rgba(100, 42, 22, 0.05);
    }}

    /* task label styling */
    div[data-testid="stCheckbox"] label {{
        font-size: 1.05rem !important;
        line-height: 1.55 !important;
        color: #2B1B14 !important;
        font-weight: 450 !important;
        padding-left: 0.4rem !important;
    }}

    /* checkbox itself */
    div[data-testid="stCheckbox"] input[type="checkbox"] {{
        accent-color: #8C8A67 !important;
        transform: scale(1.3);
        margin-right: 0.7rem;
        cursor: pointer;
    }}

    /* progress bar color */
    div[data-testid="stProgress"] > div > div {{
        background-color: #8C8A67;
    }}

    @keyframes fadeUp {{
        from {{ opacity: 0; transform: translateY(12px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    @media (max-width: 820px) {{
        .hero-content h1 {{ font-size: 2.2rem; }}
        .tip-card {{ flex-direction: column; text-align: center; gap: 0.3rem; }}
        .checklist-card label {{ font-size: 0.98rem; }}
    }}
    @media (max-width: 480px) {{
        .hero-content h1 {{ font-size: 1.8rem; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- hero ----------
st.markdown(
    """
    <div class="checklist-hero">
        <div class="hero-pattern"></div>
        <div class="hero-content">
            <div class="hero-icon"></div>
            <h1>Dubai Checklist</h1>
            <p>Your personalised movein timeline, built from your quiz. Tick things off as you go  each step brings you closer to home.</p>
            <div class="hero-underline"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- tip ---------- 
st.markdown( 
    """ 
    <div class="tip-card"> 
    <div class="tip-icon">💡</div> 
    <div class="tip-text"> 
    <strong>Tip:</strong> This checklist adapts to your quiz profile. Update your answers on the Home page and return here to see your latest action plan. 
    </div> 
    </div> 
    """, 
    unsafe_allow_html=True, 
    )

arabic_divider()

# ---------- personalised checklist ----------
if "user_profile" in st.session_state and "recommendations" in st.session_state:
    profile = st.session_state.user_profile
    recs = st.session_state.recommendations
    checklist = build_personalised_checklist(profile, recs)

    st.markdown(
        '<div style="margin-bottom:0.5rem;"><span style="font-size:0.72rem; font-weight:800; letter-spacing:0.3em; text-transform:uppercase; color:#8C8A67;">Your Movein Timeline</span></div>',
        unsafe_allow_html=True,
    )

    tabs = st.tabs([" Before arrival", " First week", " First month"])
    phase_keys = ["before_arrival", "first_week", "first_month"]

    for idx, tab in enumerate(tabs):
        with tab:
            tasks = checklist[phase_keys[idx]]
            total = len(tasks)
            checked_count = 0

            # progress bar at top
            st.markdown(
                f'<p style="margin:0 0 0.5rem 0; color:#642A16; font-weight:700;">{total} tasks</p>',
                unsafe_allow_html=True,
            )

            # Anchor element for CSS targeting of checklist card
            st.markdown('<div class="checklist-card"></div>', unsafe_allow_html=True)

            # Render checkboxes - they will be visually styled as a card via CSS sibling selectors
            for task in tasks:
                key = f"{phase_keys[idx]}_{hash(task)}"
                checked = st.checkbox(task, key=key)
                if checked:
                    checked_count += 1

            # progress bar below the card
            progress = checked_count / total if total else 0
            st.progress(progress)
            st.caption(f"{checked_count} of {total} completed")

else:
    # fallback (no quiz completed)
    st.info(
        """
         **Your checklist is waiting.**  
        Complete the quiz on the **Home** page and come back  we'll build a stepbystep timeline just for you.
        """
    )
    # static sample (optional)
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Sample checklist (not personalised)")
    sample_tabs = st.tabs(["Before arrival", "First week", "First month"])
    with sample_tabs[0]:
        st.checkbox("Shortlist neighbourhoods")
        st.checkbox("Estimate rent and deposit budget")
        st.checkbox("Prepare identity and visa documents")
        st.checkbox("Research commute options")
    with sample_tabs[1]:
        st.checkbox("Inspect apartment before signing")
        st.checkbox("Confirm Ejari process")
        st.checkbox("Start DEWA setup")
        st.checkbox("Arrange mobile and internet")
    with sample_tabs[2]:
        st.checkbox("Explore local supermarkets and clinics")
        st.checkbox("Save emergency and building contacts")
        st.checkbox("Review commute routine")
        st.checkbox("Update documents and account details")
    st.markdown("</div>", unsafe_allow_html=True)