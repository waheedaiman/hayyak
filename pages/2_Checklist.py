import streamlit as st
from src.ui import apply_hayyak_theme, render_nav, arabic_divider

st.set_page_config(
    page_title="Hayyak | Your Dubai Checklist",
    page_icon="✅",
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
        "Shortlist 3–5 neighbourhoods based on your budget & commute",
        "Prepare identity documents (passport, visa, Emirates ID if applicable)",
        "Estimate total move‑in costs (rent + deposit + agency fee + DEWA + internet)",
    ]

    if needs_metro.lower().startswith("metro"):
        before.append("Research metro routes and Nol card options")
    else:
        before.append("Compare car ownership costs vs. taxi / ride‑hail budgets")

    if "family" in household.lower():
        before.append("Check school and nursery catchments in shortlisted areas")
        before.append("Look up family‑friendly community facilities (parks, clinics)")

    if "professional" in household.lower() or "couple" in household.lower():
        before.append("Confirm rental budget allows for a second bedroom / home office")

    if budget <= 6000:
        before.append("Explore studio / shared‑apartment options to stay within budget")
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
        first_month.append("Check out social meet‑ups or sports clubs in the area")

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

# ---------- custom CSS for the checklist ----------
st.markdown(
    """
    <style>
    /* tab styling – olive active tab, cream inactive */
    div[data-testid="stTabs"] button[data-baseweb="tab"] {
        background: transparent;
        border: none;
        color: #735A4C;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        border-radius: 999px;
        margin-right: 0.3rem;
        transition: all 0.2s ease;
    }
    div[data-testid="stTabs"] button[data-baseweb="tab"]:hover {
        background: rgba(140, 138, 103, 0.12);
        color: #642A16;
    }
    div[data-testid="stTabs"] button[data-baseweb="tab"][aria-selected="true"] {
        background: #8C8A67;
        color: white;
    }

    /* checklist card – one card per tab section */
    .checklist-card {
        background: #FFF9F0;
        border: 1px solid rgba(140, 138, 103, 0.18);
        border-radius: 24px;
        padding: 1.5rem 1.8rem;
        margin-top: 0.8rem;
        box-shadow: 0 8px 18px rgba(100, 42, 22, 0.05);
    }

    /* each task row */
    .task-row {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        padding: 0.75rem 0;
        border-bottom: 1px dashed rgba(140, 138, 103, 0.18);
    }
    .task-row:last-child {
        border-bottom: none;
    }

    /* custom styled checkbox to match Hayyak palette */
    .task-row input[type="checkbox"] {
        appearance: none;
        width: 22px;
        height: 22px;
        border: 2px solid #8C8A67;
        border-radius: 6px;
        background: transparent;
        cursor: pointer;
        flex-shrink: 0;
    }
    .task-row input[type="checkbox"]:checked {
        background: #8C8A67;
        border-color: #8C8A67;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white' width='18px' height='18px'%3E%3Cpath d='M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41L9 16.17z'/%3E%3C/svg%3E");
        background-size: 16px;
        background-position: center;
        background-repeat: no-repeat;
    }

    .task-label {
        font-size: 0.95rem;
        color: #2B1B14;
        line-height: 1.4;
    }

    /* progress bar color */
    div[data-testid="stProgress"] > div > div {
        background-color: #8C8A67;
    }

    /* category subtitle */
    .phase-subtitle {
        color: #642A16;
        font-size: 1.1rem;
        font-weight: 700;
        margin-top: 1.2rem;
        margin-bottom: 0.3rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }
    .phase-icon {
        font-size: 1.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- hero section ----------
st.markdown(
    """
    <section class="hero-shell">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">Relocation planning</div>
                <h1 class="hero-title">Dubai Checklist</h1>
                <p class="hero-copy">
                    Your personalised move‑in timeline, built from your quiz answers.
                    Tick things off as you go – each step brings you closer to home.
                </p>
            </div>
            <div class="brand-card" style="background: #F6EFE5; border-radius: 24px; padding: 1.2rem;">
                <p style="color: #642A16; font-weight: 700; margin: 0;">🌴 Your Hayyak journey</p>
                <p style="color: #735A4C; margin: 0.4rem 0 0 0;">
                    Return here anytime after updating your quiz on the Home page.
                </p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

arabic_divider()

# ---------- personalised checklist tabs ----------
if "user_profile" in st.session_state and "recommendations" in st.session_state:
    profile = st.session_state.user_profile
    recs = st.session_state.recommendations
    checklist = build_personalised_checklist(profile, recs)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Your personalised move‑in checklist")

    tabs = st.tabs(["🌅 Before arrival", "🏡 First week", "🌿 First month"])
    phase_keys = ["before_arrival", "first_week", "first_month"]
    phase_icons = ["🌅", "🏡", "🌿"]

    for idx, tab in enumerate(tabs):
        with tab:
            tasks = checklist[phase_keys[idx]]
            total = len(tasks)
            checked_count = 0

            # progress bar
            st.markdown(
                f'<div class="phase-subtitle"><span class="phase-icon">{phase_icons[idx]}</span> {total} tasks</div>',
                unsafe_allow_html=True,
            )

            # build card with custom checkboxes
            card_html = '<div class="checklist-card">'
            for task in tasks:
                # unique key for each checkbox
                key = f"{phase_keys[idx]}_{hash(task)}"
                checkbox_html = f'<input type="checkbox" id="{key}" name="{key}" onchange="this.dispatchEvent(new Event(\'input\', {{ bubbles: true }}))">'
                # We'll wrap the checkbox and label inside a task-row div
                card_html += f'<div class="task-row">'
                card_html += checkbox_html
                card_html += f'<label for="{key}" class="task-label">{task}</label>'
                card_html += '</div>'

                # read Streamlit checkbox state (parallel widget)
                checked = st.checkbox(task, key=key, label_visibility="collapsed")
                if checked:
                    checked_count += 1
            card_html += '</div>'

            st.markdown(card_html, unsafe_allow_html=True)

            # display progress
            progress = checked_count / total if total else 0
            st.progress(progress)
            st.caption(f"{checked_count} of {total} completed")

    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info(
        """
        🧭 **Your checklist is waiting.**  
        Complete the quiz on the **Home** page and come back – we'll build a
        step‑by‑step timeline just for you.
        """
    )
    # fallback static sample
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Sample checklist (not personalised)")
    fallback_tabs = st.tabs(["Before arrival", "First week", "First month"])
    with fallback_tabs[0]:
        st.checkbox("Shortlist neighbourhoods")
        st.checkbox("Estimate rent and deposit budget")
        st.checkbox("Prepare identity and visa documents")
        st.checkbox("Research commute options")
    with fallback_tabs[1]:
        st.checkbox("Inspect apartment before signing")
        st.checkbox("Confirm Ejari process")
        st.checkbox("Start DEWA setup")
        st.checkbox("Arrange mobile and internet")
    with fallback_tabs[2]:
        st.checkbox("Explore local supermarkets and clinics")
        st.checkbox("Save emergency and building contacts")
        st.checkbox("Review commute routine")
        st.checkbox("Update documents and account details")
    st.markdown("</div>", unsafe_allow_html=True)