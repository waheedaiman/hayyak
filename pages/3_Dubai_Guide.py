import streamlit as st

from src.ui import apply_hayyak_theme, render_nav


st.set_page_config(
    page_title="Hayyak | Dubai Guide",
    page_icon="🕌",
    layout="wide",
)

apply_hayyak_theme()
render_nav(active="guide")


# -----------------------------
# Checklist data
# -----------------------------
CHECKLISTS = {
    "Before arrival": {
        "emoji": "🌅",
        "tasks": [
            "Shortlist 3–5 neighbourhoods based on your budget & commute",
            "Prepare identity documents (passport, visa, Emirates ID if applicable)",
            "Estimate total move-in costs (rent + deposit + agency fee + DEWA + internet)",
            "Compare car ownership costs vs. taxi / ride-hail budgets",
            "Confirm rental budget allows for a second bedroom / home office",
            "Explore studio / shared-apartment options to stay within budget",
        ],
    },
    "First week": {
        "emoji": "🏠",
        "tasks": [
            "Complete move-in inspection and document apartment condition",
            "Activate DEWA connection",
            "Set up internet and mobile plan",
            "Register Ejari if required",
            "Locate nearest supermarket, pharmacy, clinic, and metro/bus stop",
            "Save building security, maintenance, and landlord/broker contacts",
        ],
    },
    "First month": {
        "emoji": "🌿",
        "tasks": [
            "Review your actual monthly spending against your planned budget",
            "Test commute routes during peak hours",
            "Explore nearby communities, gyms, cafes, and services",
            "Set up recurring rent and utility payment reminders",
            "Check if your neighbourhood still matches your lifestyle needs",
            "Update your document folder with tenancy, DEWA, internet, and ID copies",
        ],
    },
}


# -----------------------------
# Session state
# -----------------------------
if "movein_active_tab" not in st.session_state:
    st.session_state.movein_active_tab = "Before arrival"

for phase, data in CHECKLISTS.items():
    for i, _ in enumerate(data["tasks"]):
        key = f"movein_{phase}_{i}"
        if key not in st.session_state:
            st.session_state[key] = False


# -----------------------------
# CSS fix for checklist UI
# -----------------------------
st.markdown(
    """
    <style>
        .movein-section {
            margin-top: 2.25rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(100, 42, 22, 0.16);
        }

        .movein-eyebrow {
            color: #8F8C68;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.32rem;
            text-transform: uppercase;
            margin-bottom: 1.25rem;
        }

        .movein-tabs {
            display: flex;
            align-items: center;
            gap: 2rem;
            margin-bottom: 1.7rem;
            flex-wrap: wrap;
        }

        .movein-tab-button {
            border: 0;
            background: transparent;
            color: #6F5D4F;
            font-size: 1.05rem;
            font-weight: 500;
            padding: 0.9rem 1.35rem;
            border-radius: 999px;
            cursor: pointer;
        }

        .movein-tab-active {
            background: #8F8C68;
            color: #FFFDF7;
            font-weight: 700;
            box-shadow: inset 0 -3px 0 #FF4D4D;
        }

        .task-count {
            color: #642A16;
            font-size: 1.25rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .checklist-card {
            background: #FFF9EF;
            border: 1px solid rgba(100, 42, 22, 0.10);
            border-radius: 28px;
            padding: 1.8rem 2.15rem;
            box-shadow: 0 10px 28px rgba(100, 42, 22, 0.05);
            margin-bottom: 1.5rem;
        }

        .checklist-row {
            display: grid;
            grid-template-columns: 34px minmax(0, 1fr);
            align-items: center;
            column-gap: 1rem;
            padding: 1.05rem 0;
            border-bottom: 1px solid rgba(100, 42, 22, 0.10);
        }

        .checklist-row:last-child {
            border-bottom: none;
        }

        .checklist-box {
            width: 28px;
            height: 28px;
            border-radius: 8px;
            border: 3px solid #8F8C68;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #FFFDF7;
            font-size: 1rem;
            font-weight: 900;
            background: transparent;
        }

        .checklist-box.done {
            background: #8F8C68;
        }

        .checklist-text {
            color: #2A1B15;
            font-size: 1.05rem;
            font-weight: 500;
            line-height: 1.45;
        }

        .checklist-text.done {
            color: #6F5D4F;
            text-decoration: line-through;
            text-decoration-thickness: 2px;
            text-decoration-color: rgba(143, 140, 104, 0.65);
        }

        .progress-shell {
            width: 100%;
            height: 12px;
            background: rgba(143, 140, 104, 0.22);
            border-radius: 999px;
            overflow: hidden;
            margin-top: 1.3rem;
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

        /* Hide Streamlit default checkbox labels from affecting the design */
        div[data-testid="stCheckbox"] label p {
            color: #2A1B15 !important;
        }

        div[data-testid="stCheckbox"] {
            margin-bottom: -0.25rem;
        }

        @media (max-width: 768px) {
            .checklist-card {
                padding: 1.25rem;
                border-radius: 22px;
            }

            .movein-tabs {
                gap: 0.75rem;
            }

            .movein-tab-button {
                font-size: 0.95rem;
                padding: 0.75rem 1rem;
            }

            .checklist-text {
                font-size: 0.95rem;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Hero
# -----------------------------
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


# -----------------------------
# Guide preview
# -----------------------------
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


# -----------------------------
# Move-in checklist section
# -----------------------------
st.markdown(
    """
    <section class="movein-section">
        <div class="movein-eyebrow">Your move-in timeline</div>
    </section>
    """,
    unsafe_allow_html=True,
)

tab_cols = st.columns([1.1, 1.1, 1.1, 5])

for index, phase in enumerate(CHECKLISTS.keys()):
    with tab_cols[index]:
        is_active = st.session_state.movein_active_tab == phase
        label = f"{CHECKLISTS[phase]['emoji']} {phase}"

        if st.button(label, key=f"tab_{phase}", use_container_width=True):
            st.session_state.movein_active_tab = phase
            st.rerun()

        st.markdown(
            f"""
            <script>
            </script>
            """,
            unsafe_allow_html=True,
        )

active_phase = st.session_state.movein_active_tab
active_data = CHECKLISTS[active_phase]
tasks = active_data["tasks"]

completed = sum(
    1 for i in range(len(tasks)) if st.session_state.get(f"movein_{active_phase}_{i}", False)
)
total = len(tasks)
progress = completed / total if total else 0

st.markdown(
    f"""
    <div class="task-count">{total} tasks</div>
    <div class="checklist-card">
    """,
    unsafe_allow_html=True,
)

for i, task in enumerate(tasks):
    key = f"movein_{active_phase}_{i}"
    is_done = st.session_state.get(key, False)

    row_cols = st.columns([0.04, 0.96])

    with row_cols[0]:
        st.checkbox(
            " ",
            key=key,
            label_visibility="collapsed",
        )

    is_done = st.session_state.get(key, False)
    box_class = "checklist-box done" if is_done else "checklist-box"
    text_class = "checklist-text done" if is_done else "checklist-text"
    check_icon = "✓" if is_done else ""

    with row_cols[1]:
        st.markdown(
            f"""
            <div class="checklist-row">
                <div class="{box_class}">{check_icon}</div>
                <div class="{text_class}">{task}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="progress-shell">
        <div class="progress-fill" style="width:{progress * 100}%;"></div>
    </div>
    <div class="progress-label">{completed} of {total} completed</div>
    """,
    unsafe_allow_html=True,
)