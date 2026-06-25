# checklist.py – now personalised from the quiz
import streamlit as st
from src.ui import apply_hayyak_theme, render_nav

st.set_page_config(
    page_title="Hayyak | Dubai Checklist",
    page_icon="✅",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="checklist")

# ---------- helper: build personalised checklist from quiz results ----------
def build_personalised_checklist(profile, top_recs):
    """
    Returns a dict with keys 'before_arrival', 'first_week', 'first_month'.
    Each value is a list of task strings (will become checkbox labels).
    """
    budget = profile.get("monthly_budget_aed", 8000)
    commute = profile.get("commute_target", "")
    lifestyle = profile.get("lifestyle", "")
    household = profile.get("household_type", "")
    needs_metro = profile.get("needs_metro", "Metro helpful")
    priority = profile.get("priority", "")

    # collect first‑step suggestions from top recommendations
    first_steps_all = []
    for rec in top_recs:
        first_steps_all.extend(rec.get("first_steps", []))

    # ---------- BEFORE ARRIVAL ----------
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

    # ---------- FIRST WEEK ----------
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

    # add unique first‑steps from recommendations
    for step in first_steps_all[:3]:
        if step not in first_week:
            first_week.append(step)

    # ---------- FIRST MONTH ----------
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

    # always append building contacts
    first_month.append("Save emergency numbers and building management contacts")

    # remove duplicates while preserving order
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

# ---------- main page content ----------
st.markdown(
    """
    <section class="hero-shell">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">Relocation planning</div>
                <h1 class="hero-title">Dubai Checklist</h1>
                <p class="hero-copy">
                    A personalised checklist built from your quiz answers – track what you need before, during, and after your move.
                </p>
            </div>
            <div class="brand-card">
                <h3 style="color:#642A16;">Powered by your quiz</h3>
                <p class="muted-text">
                    Update your quiz answers on the home page and return here for fresh recommendations.
                </p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-card">', unsafe_allow_html=True)

# Check if we have quiz results in session state
if "user_profile" in st.session_state and "recommendations" in st.session_state:
    profile = st.session_state.user_profile
    recs = st.session_state.recommendations
    checklist = build_personalised_checklist(profile, recs)

    st.subheader("Your personalised move‑in checklist")

    tabs = st.tabs(["Before arrival", "First week", "First month"])

    with tabs[0]:
        for task in checklist["before_arrival"]:
            st.checkbox(task, key=f"ba_{hash(task)}")

    with tabs[1]:
        for task in checklist["first_week"]:
            st.checkbox(task, key=f"fw_{hash(task)}")

    with tabs[2]:
        for task in checklist["first_month"]:
            st.checkbox(task, key=f"fm_{hash(task)}")

else:
    st.info(
        "Complete the quiz on the **Home** page to unlock your personalised checklist."
    )
    # optional: still show a minimal static version
    st.markdown("### Sample checklist (not personalised)")
    tabs = st.tabs(["Before arrival", "First week", "First month"])
    with tabs[0]:
        st.checkbox("Shortlist neighbourhoods")
        st.checkbox("Estimate rent and deposit budget")
        st.checkbox("Prepare identity and visa documents")
        st.checkbox("Research commute options")
    with tabs[1]:
        st.checkbox("Inspect apartment before signing")
        st.checkbox("Confirm Ejari process")
        st.checkbox("Start DEWA setup")
        st.checkbox("Arrange mobile and internet")
    with tabs[2]:
        st.checkbox("Explore local supermarkets and clinics")
        st.checkbox("Save emergency and building contacts")
        st.checkbox("Review commute routine")
        st.checkbox("Update documents and account details")

st.markdown("</div>", unsafe_allow_html=True)