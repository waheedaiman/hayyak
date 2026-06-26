import streamlit as st

from src.ui import apply_hayyak_theme, render_nav


st.set_page_config(
    page_title="Hayyak | Dubai Guide",
    page_icon="🕌",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="guide")


CHECKLISTS = {
    "Before arrival": {
        "emoji": "🌅",
        "tasks": [
            "Shortlist 3–5 neighbourhoods based on your budget & commute",
            "Prepare identity documents (passport, visa, Emirates ID if applicable)",
            "Estimate total move-in costs (rent + deposit + agency fee + DEWA + internet)",
            "Compare car ownership costs vs. taxi / ride-hail budgets",
        ],
    },
    "First week": {
        "emoji": "🏠",
        "tasks": [
            "Complete move-in inspection and document apartment condition",
            "Activate DEWA connection",
            "Set up internet and mobile plan",
            "Register Ejari if required",
        ],
    },
    "First month": {
        "emoji": "🌿",
        "tasks": [
            "Review actual monthly spending against your planned budget",
            "Test commute routes during peak hours",
            "Explore nearby communities, gyms, cafes, and services",
            "Set up recurring rent and utility payment reminders",
        ],
    },
}


if "movein_active_tab" not in st.session_state:
    st.session_state.movein_active_tab = "Before arrival"

for phase, data in CHECKLISTS.items():
    for index, _ in enumerate(data["tasks"]):
        key = f"movein_{phase}_{index}"
        if key not in st.session_state:
            st.session_state[key] = False


st.markdown(
    """
    <style>
        .movein-wrap {
            margin-top: 2.5rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(100, 42, 22, 0.14);
        }

        .movein-eyebrow {
            color: #8F8C68;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.34rem;
            text-transform: uppercase;
            margin-bottom: 1.25rem;
        }

        .task-count {
            color: #642A16;
            font-size: 1.25rem;
            font-weight: 800;
            margin-top: 1.75rem;
            margin-bottom: 1rem;
        }

        .checklist-card {
            background: #FFF9EF;
            border: 1px solid rgba(100, 42, 22, 0.10);
            border-radius: 28px;
            padding: 1.45rem 2rem;
            box-shadow: 0 10px 26px rgba(100, 42, 22, 0.05);
            margin-bottom: 1.4rem;
        }

        .checklist-card [data-testid="stVerticalBlock"] {
            gap: 0rem;
        }

        .checklist-card div[data-testid="stCheckbox"] {
            padding: 1rem 0;
            border-bottom: 1px solid rgba(100, 42, 22, 0.10);
        }

        .checklist-card div[data-testid="stCheckbox"]:last-child {
            border-bottom: none;
        }

        .checklist-card div[data-testid="stCheckbox"] label {
            align-items: center;
            gap: 1rem;
        }

        .checklist-card div[data-testid="stCheckbox"] label p {
            color: #2A1B15 !important;
            font-size: 1.05rem !important;
            font-weight: 500 !important;
            line-height: 1.45 !important;
        }

        .checklist-card div[data-testid="stCheckbox"] input:checked + div {
            background-color: #8F8C68 !important;
            border-color: #8F8C68 !important;
        }

        .progress-shell {
            width: 100%;
            height: 12px;
            background: rgba(143, 140, 104, 0.25);
            border-radius: 999px;
            overflow: hidden;
            margin-top: 1.1rem;
            margin-bottom: 1rem;
        }

        .progress-fill {
            height: 100%;
            background: #8F8C68;
            border-radius: 999px;
        }

        .progress-label {
            color: #786C63;
            font-size: 1rem;
            margin-bottom: 0.5rem;
        }

        div[data-testid="stButton"] > button {
            background: transparent;
            color: #6F5D4F;
            border: none;
            border-radius: 999px;
            padding: 0.85rem 1.3rem;
            font-size: 1.05rem;
            font-weight: 500;
            box-shadow: none;
        }

        div[data-testid="stButton"] > button:hover {
            background: rgba(143, 140, 104, 0.12);
            color: #642A16;
            border: none;
        }

        .active-tab-pill {
            background: #8F8C68;
            color: #FFFDF7;
            border-radius: 999px;
            padding: 0.85rem 1.35rem;
            font-size: 1.05rem;
            font-weight: 700;
            text-align: center;
            box-shadow: inset 0 -3px 0 #FF4D4D;
        }

        .inactive-tab-pill {
            color: #6F5D4F;
            padding: 0.85rem 1.35rem;
            font-size: 1.05rem;
            font-weight: 500;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <section class="hero-shell">
        <div class="hero-grid">
            <div>
                <div class="eyebrow">City guide</div>
                <h1 class="hero-title">Dubai Guide</h1>
                <p class="hero-copy">
                    A future A-Z guide for newcomers moving to Dubai, covering
                    neighbourhoods, commute, documents, utilities, and daily life.
                </p>
            </div>
            <div class="brand-card">
                <h3 style="color:#642A16;">Grounded guidance</h3>
                <p class="muted-text">
                    Designed to feel practical, local, and culturally aware.
                </p>
            </div>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)


st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("Guide structure preview")

st.markdown(
    """
    **1. Choosing where to live**  
    Budget, commute, metro access, lifestyle, and household needs.

    **2. Understanding rental basics**  
    Contracts, deposits, Ejari, and building/community checks.

    **3. Setting up essentials**  
    DEWA, mobile, internet, banking, and local services.

    **4. Settling into daily life**  
    Groceries, clinics, transport, delivery apps, and community routines.
    """
)

st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    """
    <div class="movein-wrap">
        <div class="movein-eyebrow">Your move-in timeline</div>
    </div>
    """,
    unsafe_allow_html=True,
)


tab_cols = st.columns([1.2, 1.2, 1.2, 5])

for i, phase in enumerate(CHECKLISTS.keys()):
    with tab_cols[i]:
        label = f"{CHECKLISTS[phase]['emoji']} {phase}"

        if st.session_state.movein_active_tab == phase:
            st.markdown(
                f'<div class="active-tab-pill">{label}</div>',
                unsafe_allow_html=True,
            )
        else:
            if st.button(label, key=f"movein_tab_{phase}", use_container_width=True):
                st.session_state.movein_active_tab = phase
                st.rerun()


active_phase = st.session_state.movein_active_tab
tasks = CHECKLISTS[active_phase]["tasks"]

completed = sum(
    1
    for i in range(len(tasks))
    if st.session_state.get(f"movein_{active_phase}_{i}", False)
)

total = len(tasks)
progress = completed / total if total else 0


st.markdown(f'<div class="task-count">{total} tasks</div>', unsafe_allow_html=True)

st.markdown('<div class="checklist-card">', unsafe_allow_html=True)

for i, task in enumerate(tasks):
    st.checkbox(
        task,
        key=f"movein_{active_phase}_{i}",
    )

st.markdown("</div>", unsafe_allow_html=True)


st.markdown(
    f"""
    <div class="progress-shell">
        <div class="progress-fill" style="width: {progress * 100}%;"></div>
    </div>
    <div class="progress-label">{completed} of {total} completed</div>
    """,
    unsafe_allow_html=True,
)