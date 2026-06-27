# Hayyak
**AI Relocation Companion for Dubai Newcomers**

Hayyak helps people moving to Dubai choose where to live, avoid relocation mistakes, and complete every setup step — from finding the right neighbourhood to connecting utilities.

---

## Features

- **Onboarding Quiz** — answer questions about your budget, lifestyle, commute destination, and household type
- **Neighbourhood Matchmaker** — ranked recommendations with match percentage, reasons, cautions, and downsides
- **AI Relocation Brief** — personalised summary and first-week checklist generated via Groq API
- **Personalised Move-in Checklist** — three-phase timeline (Before Arrival, First Week, First Month) tailored to your quiz profile
- **Utility Setup Guide** — step-by-step guidance on DEWA, Ejari, internet, and mobile providers (e& and du)
- **Dubai Guide** — area overviews and local tips for newcomers

---

## Tech Stack

| Layer | Technology |
|---|---|
| LLM | Groq API — Llama 3.1 8B Instant (free tier) |
| Frontend | Streamlit |
| Language | Python 3.12 |
| Hosting | Streamlit Community Cloud |

---

## Project Structure

```
hayyak/
├── app.py                  # Main entry point and quiz page
├── pages/
│   ├── 1_Utilities.py      # Utility setup guide
│   ├── 2_Checklist.py      # Personalised move-in checklist
│   └── 3_Dubai_Guide.py    # Dubai area guide
├── src/
│   ├── ai_helper.py        # Groq API integration and prompt building
│   ├── recommender.py      # Neighbourhood scoring logic
│   └── ui.py               # Shared theme, components, and navigation
├── assets/                 # Logo and hero images
├── requirements.txt
└── README.md
```

---

## How It Works

1. User completes the onboarding quiz (budget, commute, lifestyle, household type, metro needs, priority)
2. `recommender.py` scores and ranks Dubai neighbourhoods against the profile
3. Top matches are displayed with reasons, cautions, and a match percentage
4. Optionally, the Groq API generates a personalised relocation brief using Llama 3.1
5. The Checklist page builds a tailored move-in timeline from the same quiz answers

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/hayyak.git
cd hayyak
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

Create a `.streamlit/secrets.toml` file:

```toml
GROQ_API_KEY = "your-groq-api-key-here"
```

Get a free key at [console.groq.com](https://console.groq.com).

### 4. Run the app

```bash
streamlit run app.py
```

---

## Deployment

Hayyak is deployed on **Streamlit Community Cloud**.

To deploy your own instance:
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set `GROQ_API_KEY` under Settings > Secrets
4. Deploy — done

---

## Status

Completed — Built during the **Building AI Application Challenge 2026**

---

## License

MIT
