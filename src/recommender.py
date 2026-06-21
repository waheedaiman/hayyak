"""Rule-based neighbourhood recommender for Hayyak.

This is the first version of the "brain" of the app. It takes a user's
relocation quiz answers and returns the top 3 Dubai neighbourhood matches.
The data below is a starter heuristic dataset and should be improved with
verified sources as the project develops.
"""

from __future__ import annotations

from typing import Any, Dict, List


BUDGET_LEVELS = {
    "budget": 1,
    "mid": 2,
    "premium": 3,
    "luxury": 4,
}

COMMUTE_OPTIONS = [
    "Not sure yet",
    "Dubai Internet City / Media City",
    "JLT / Dubai Marina",
    "DIFC / Downtown",
    "Business Bay",
    "Deira / Old Dubai",
    "Bur Dubai / Oud Metha",
    "Dubai Silicon Oasis / Academic City",
    "Al Barsha / Mall of the Emirates",
    "Dubai Airport / Mirdif",
]

LIFESTYLE_OPTIONS = ["Quiet", "Balanced", "Lively"]
HOUSEHOLD_OPTIONS = ["Student", "Solo professional", "Couple", "Family"]
METRO_OPTIONS = ["Yes", "Flexible", "No"]
PRIORITY_OPTIONS = ["Affordability", "Commute", "Lifestyle", "Family convenience"]


NEIGHBOURHOODS: List[Dict[str, Any]] = [
    {
        "name": "Jumeirah Village Circle (JVC)",
        "budget_level": "mid",
        "commute_tags": [
            "Dubai Internet City / Media City",
            "JLT / Dubai Marina",
            "Al Barsha / Mall of the Emirates",
        ],
        "lifestyle_tags": ["quiet", "balanced"],
        "household_tags": ["solo professional", "couple", "family"],
        "has_metro": False,
        "summary": "A balanced residential option with many apartment choices and a calmer feel than central Dubai.",
        "strengths": [
            "good value for many newcomers",
            "popular with young professionals and small families",
            "many supermarkets, gyms, and cafes nearby",
        ],
        "downside": "Metro access is limited, so commuting often depends on car, taxi, or bus connections.",
        "first_steps": [
            "Compare commute time during peak hours.",
            "Check building chiller and maintenance fees before signing.",
            "Shortlist buildings near daily shops or bus routes.",
        ],
    },
    {
        "name": "Jumeirah Lake Towers (JLT)",
        "budget_level": "mid",
        "commute_tags": [
            "Dubai Internet City / Media City",
            "JLT / Dubai Marina",
            "Al Barsha / Mall of the Emirates",
        ],
        "lifestyle_tags": ["balanced", "lively"],
        "household_tags": ["student", "solo professional", "couple", "family"],
        "has_metro": True,
        "summary": "A practical high-rise community with metro access, restaurants, offices, and quick access to Marina.",
        "strengths": [
            "strong metro connectivity",
            "good mix of work, food, and residential towers",
            "walkable clusters around the lakes",
        ],
        "downside": "Traffic and parking can be frustrating around busy clusters.",
        "first_steps": [
            "Choose a cluster close to the metro if you will not drive.",
            "Check parking availability in the building.",
            "Compare tower quality because buildings vary a lot.",
        ],
    },
    {
        "name": "Dubai Marina",
        "budget_level": "premium",
        "commute_tags": [
            "Dubai Internet City / Media City",
            "JLT / Dubai Marina",
        ],
        "lifestyle_tags": ["lively", "balanced"],
        "household_tags": ["solo professional", "couple", "family"],
        "has_metro": True,
        "summary": "A lively waterfront area suited to people who want restaurants, gyms, nightlife, and walkability.",
        "strengths": [
            "very active lifestyle and social scene",
            "metro and tram options in many parts",
            "close to JBR, Bluewaters, JLT, and Media City",
        ],
        "downside": "It can be more expensive and traffic can be heavy during evenings and weekends.",
        "first_steps": [
            "Check whether the building is closer to metro, tram, or Marina Walk.",
            "Compare noise levels if you prefer quiet evenings.",
            "Confirm parking and guest parking rules.",
        ],
    },
    {
        "name": "Business Bay",
        "budget_level": "premium",
        "commute_tags": [
            "DIFC / Downtown",
            "Business Bay",
        ],
        "lifestyle_tags": ["lively", "balanced"],
        "household_tags": ["solo professional", "couple"],
        "has_metro": True,
        "summary": "A central option for professionals who want to stay close to Downtown, DIFC, and office hubs.",
        "strengths": [
            "central location",
            "good for Downtown and DIFC commutes",
            "many newer apartments and serviced buildings",
        ],
        "downside": "Rent and traffic can be high, especially near the canal and Downtown side.",
        "first_steps": [
            "Test commute time to work during morning rush hour.",
            "Check whether the building is actually walkable to the metro.",
            "Compare included facilities and cooling charges.",
        ],
    },
    {
        "name": "Deira",
        "budget_level": "budget",
        "commute_tags": [
            "Deira / Old Dubai",
            "Dubai Airport / Mirdif",
            "Bur Dubai / Oud Metha",
        ],
        "lifestyle_tags": ["lively", "balanced"],
        "household_tags": ["student", "solo professional", "family"],
        "has_metro": True,
        "summary": "A more affordable and established area with strong metro access and many daily conveniences.",
        "strengths": [
            "usually more budget-friendly",
            "excellent access to older commercial areas",
            "many shops, restaurants, and services nearby",
        ],
        "downside": "Some buildings are older and streets can feel crowded at peak times.",
        "first_steps": [
            "Check building age, maintenance, and lift condition.",
            "Visit the street at night to understand noise and crowding.",
            "Confirm metro station walking distance.",
        ],
    },
    {
        "name": "Bur Dubai / Oud Metha",
        "budget_level": "budget",
        "commute_tags": [
            "Bur Dubai / Oud Metha",
            "Deira / Old Dubai",
            "DIFC / Downtown",
        ],
        "lifestyle_tags": ["balanced", "lively"],
        "household_tags": ["student", "solo professional", "family"],
        "has_metro": True,
        "summary": "An established community with transport access, schools, clinics, restaurants, and older residential options.",
        "strengths": [
            "good everyday convenience",
            "metro access in many parts",
            "useful for families who want schools and clinics nearby",
        ],
        "downside": "Traffic and parking can be difficult in some streets.",
        "first_steps": [
            "Check parking availability carefully.",
            "Compare buildings near metro lines if you do not drive.",
            "Look at noise levels around main roads.",
        ],
    },
    {
        "name": "Dubai Silicon Oasis (DSO)",
        "budget_level": "budget",
        "commute_tags": [
            "Dubai Silicon Oasis / Academic City",
        ],
        "lifestyle_tags": ["quiet", "balanced"],
        "household_tags": ["student", "solo professional", "couple", "family"],
        "has_metro": False,
        "summary": "A practical and quieter option for students, tech workers, and families near Academic City or DSO.",
        "strengths": [
            "good value compared with central areas",
            "useful for Academic City and Silicon Oasis commutes",
            "calmer residential feel",
        ],
        "downside": "It is not ideal if you need daily metro access or frequent trips to Marina/Downtown.",
        "first_steps": [
            "Check bus or car commute before choosing the building.",
            "Look for buildings close to supermarkets and daily services.",
            "Compare commute cost if you will use taxis often.",
        ],
    },
    {
        "name": "Mirdif",
        "budget_level": "mid",
        "commute_tags": [
            "Dubai Airport / Mirdif",
            "Deira / Old Dubai",
        ],
        "lifestyle_tags": ["quiet", "balanced"],
        "household_tags": ["family", "couple", "solo professional"],
        "has_metro": False,
        "summary": "A quieter family-friendly area with malls, villas, apartments, and strong access to the airport side of Dubai.",
        "strengths": [
            "good for families",
            "calmer than central apartment districts",
            "close to airport-side work locations",
        ],
        "downside": "It is less convenient for Marina, JLT, and some central business commutes without a car.",
        "first_steps": [
            "Confirm daily drive time to work or school.",
            "Check proximity to Mirdif City Centre or daily shops.",
            "Compare villa vs apartment maintenance responsibilities.",
        ],
    },
    {
        "name": "Al Barsha",
        "budget_level": "mid",
        "commute_tags": [
            "Al Barsha / Mall of the Emirates",
            "Dubai Internet City / Media City",
            "JLT / Dubai Marina",
        ],
        "lifestyle_tags": ["balanced", "quiet"],
        "household_tags": ["student", "solo professional", "couple", "family"],
        "has_metro": True,
        "summary": "A central and practical area with access to Mall of the Emirates, metro, schools, and mixed housing.",
        "strengths": [
            "good midpoint between Marina side and central Dubai",
            "metro access in parts of the area",
            "useful mix of apartments, villas, shops, and services",
        ],
        "downside": "Traffic can build up around Mall of the Emirates and main roads.",
        "first_steps": [
            "Check whether the exact building is walkable to metro.",
            "Compare Al Barsha 1 with quieter sub-areas.",
            "Review traffic around school and mall timings.",
        ],
    },
    {
        "name": "Dubai Hills",
        "budget_level": "premium",
        "commute_tags": [
            "DIFC / Downtown",
            "Business Bay",
            "Al Barsha / Mall of the Emirates",
        ],
        "lifestyle_tags": ["quiet", "balanced"],
        "household_tags": ["family", "couple", "solo professional"],
        "has_metro": False,
        "summary": "A newer, quieter, family-oriented community with parks, malls, and modern apartments/villas.",
        "strengths": [
            "strong family lifestyle",
            "modern buildings and community planning",
            "good option if parks and calm surroundings matter",
        ],
        "downside": "It can be expensive and usually works better with a car.",
        "first_steps": [
            "Check school, nursery, and commute distance if moving with family.",
            "Compare service charges and building facilities.",
            "Plan transport because metro access is limited.",
        ],
    },
]


def budget_level_from_monthly(monthly_budget_aed: int) -> str:
    """Convert a monthly AED rent budget into a simple budget category."""
    if monthly_budget_aed <= 4500:
        return "budget"
    if monthly_budget_aed <= 8000:
        return "mid"
    if monthly_budget_aed <= 14000:
        return "premium"
    return "luxury"


def _score_budget(user_budget_level: str, area_budget_level: str) -> tuple[int, str]:
    user_rank = BUDGET_LEVELS[user_budget_level]
    area_rank = BUDGET_LEVELS[area_budget_level]
    diff = area_rank - user_rank

    if diff == 0:
        return 30, "matches your rent budget"
    if diff < 0:
        return 24, "is likely comfortably within your budget"
    if diff == 1:
        return 10, "may be slightly above your target budget"
    return 0, "may be too expensive for your current budget"


def _score_commute(commute_target: str, area: Dict[str, Any]) -> tuple[int, str]:
    if commute_target == "Not sure yet":
        return 10, "keeps your commute flexible while you decide your work/study location"
    if commute_target in area["commute_tags"]:
        return 25, f"fits your commute target: {commute_target}"
    return 4, "does not strongly match your selected commute area"


def _score_lifestyle(lifestyle: str, area: Dict[str, Any]) -> tuple[int, str]:
    choice = lifestyle.strip().lower()
    tags = area["lifestyle_tags"]

    if choice in tags:
        return 20, f"matches your preferred {choice} lifestyle"
    if choice == "balanced":
        return 12, "still gives a reasonable balance of convenience and comfort"
    return 5, "has a different lifestyle feel than your preference"


def _score_household(household_type: str, area: Dict[str, Any]) -> tuple[int, str]:
    choice = household_type.strip().lower()
    if choice in area["household_tags"]:
        return 15, f"works well for a {choice} move"
    return 3, f"is not the strongest match for a {choice} move"


def _score_metro(needs_metro: str, area: Dict[str, Any]) -> tuple[int, str]:
    needs = needs_metro.strip().lower()
    has_metro = bool(area["has_metro"])

    if needs == "yes" and has_metro:
        return 10, "has metro access"
    if needs == "yes" and not has_metro:
        return 0, "does not have strong metro access"
    if needs == "flexible" and has_metro:
        return 7, "gives you metro access even though you are flexible"
    if needs == "flexible" and not has_metro:
        return 5, "can still work if you are flexible on transport"
    return 5, "metro access is not a priority for you"


def _score_priority(priority: str, profile: Dict[str, Any], area: Dict[str, Any]) -> tuple[int, str]:
    priority = priority.strip().lower()
    user_budget_level = budget_level_from_monthly(int(profile["monthly_budget_aed"]))
    area_budget_level = area["budget_level"]

    if priority == "affordability":
        if BUDGET_LEVELS[area_budget_level] <= BUDGET_LEVELS[user_budget_level]:
            return 15, "supports your affordability priority"
        return 0, "does not strongly support your affordability priority"

    if priority == "commute":
        if profile["commute_target"] in area["commute_tags"]:
            return 15, "supports your commute priority"
        return 0, "does not strongly support your commute priority"

    if priority == "lifestyle":
        if profile["lifestyle"].lower() in area["lifestyle_tags"]:
            return 15, "supports your lifestyle priority"
        return 0, "does not strongly support your lifestyle priority"

    if priority == "family convenience":
        if "family" in area["household_tags"]:
            return 15, "supports family convenience"
        return 0, "is not mainly family-oriented"

    return 0, "priority not recognised"


def score_neighbourhoods(profile: Dict[str, Any], limit: int = 3) -> List[Dict[str, Any]]:
    """Return the top matching neighbourhoods for a user profile.

    Expected profile keys:
    - monthly_budget_aed: int
    - commute_target: str
    - lifestyle: str
    - household_type: str
    - needs_metro: str
    - priority: str
    """
    max_score = 115
    user_budget_level = budget_level_from_monthly(int(profile["monthly_budget_aed"]))
    scored: List[Dict[str, Any]] = []

    for area in NEIGHBOURHOODS:
        reasons: List[str] = []
        cautions: List[str] = []
        total = 0

        budget_points, budget_reason = _score_budget(user_budget_level, area["budget_level"])
        commute_points, commute_reason = _score_commute(profile["commute_target"], area)
        lifestyle_points, lifestyle_reason = _score_lifestyle(profile["lifestyle"], area)
        household_points, household_reason = _score_household(profile["household_type"], area)
        metro_points, metro_reason = _score_metro(profile["needs_metro"], area)
        priority_points, priority_reason = _score_priority(profile["priority"], profile, area)

        factor_results = [
            (budget_points, budget_reason),
            (commute_points, commute_reason),
            (lifestyle_points, lifestyle_reason),
            (household_points, household_reason),
            (metro_points, metro_reason),
            (priority_points, priority_reason),
        ]

        for points, reason in factor_results:
            total += points
            if points >= 10:
                reasons.append(reason)
            elif "too expensive" in reason or "does not have strong metro" in reason:
                cautions.append(reason)

        match_percent = round((total / max_score) * 100)

        scored.append(
            {
                "name": area["name"],
                "score": total,
                "match_percent": match_percent,
                "summary": area["summary"],
                "reasons": reasons[:5],
                "cautions": cautions,
                "strengths": area["strengths"],
                "downside": area["downside"],
                "first_steps": area["first_steps"],
                "has_metro": area["has_metro"],
                "budget_level": area["budget_level"],
            }
        )

    scored.sort(key=lambda item: item["score"], reverse=True)
    return scored[:limit]


def build_llm_context(profile: Dict[str, Any], recommendations: List[Dict[str, Any]]) -> str:
    """Create a clean text block that can be passed to Groq later."""
    lines = [
        "User profile:",
        f"- Monthly rent budget: AED {profile['monthly_budget_aed']}",
        f"- Commute target: {profile['commute_target']}",
        f"- Lifestyle preference: {profile['lifestyle']}",
        f"- Household type: {profile['household_type']}",
        f"- Needs metro: {profile['needs_metro']}",
        f"- Main priority: {profile['priority']}",
        "",
        "Top neighbourhood matches:",
    ]

    for index, rec in enumerate(recommendations, start=1):
        lines.extend(
            [
                f"{index}. {rec['name']} ({rec['match_percent']}% match)",
                f"   Summary: {rec['summary']}",
                f"   Reasons: {', '.join(rec['reasons']) if rec['reasons'] else 'No strong reasons captured.'}",
                f"   Downside: {rec['downside']}",
            ]
        )

    return "\n".join(lines)


if __name__ == "__main__":
    demo_profile = {
        "monthly_budget_aed": 7000,
        "commute_target": "Dubai Internet City / Media City",
        "lifestyle": "Balanced",
        "household_type": "Solo professional",
        "needs_metro": "Flexible",
        "priority": "Commute",
    }
    for result in score_neighbourhoods(demo_profile):
        print(result["name"], result["match_percent"])
