import json
from pathlib import Path

DATA_PATH = Path("data/candidates.jsonl")

ELITE_KEYWORDS = [
    "ndcg",
    "mrr",
    "map",
    "ranking",
    "a/b testing",
    "retrieval",
    "recommendation"
]

elite = []

with open(DATA_PATH, "r", encoding="utf-8") as file:
    for line in file:
        candidate = json.loads(line)

        profile = candidate.get("profile", {})
        career_history = candidate.get("career_history", [])
        skills = candidate.get("skills", [])

        text = " ".join([
            profile.get("headline", ""),
            profile.get("summary", ""),
            " ".join(job.get("description", "") for job in career_history),
            " ".join(skill.get("name", "") for skill in skills)
        ]).lower()

        matches = [kw for kw in ELITE_KEYWORDS if kw in text]

        if matches:
            elite.append({
                "id": candidate["candidate_id"],
                "title": profile.get("current_title"),
                "exp": profile.get("years_of_experience"),
                "matches": matches
            })

print(f"Elite candidates found: {len(elite)}")

for row in elite[:50]:
    print(row)
    