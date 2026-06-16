import json
from pathlib import Path

DATA_PATH = Path("data/candidates.jsonl")

TARGET_TITLES = [
    "Recommendation Systems Engineer",
    "Search Engineer",
    "AI Engineer",
    "AI Research Engineer",
    "ML Engineer",
    "Data Scientist",
    "Backend Engineer",
    "Senior Software Engineer"
]

matches = []

with open(DATA_PATH, "r", encoding="utf-8") as file:
    for line in file:
        candidate = json.loads(line)

        profile = candidate["profile"]

        title = profile.get("current_title", "")
        exp = profile.get("years_of_experience", 0)

        if title in TARGET_TITLES and exp >= 5:
            matches.append({
                "id": candidate["candidate_id"],
                "title": title,
                "exp": exp,
                "company": profile.get("current_company")
            })

print(f"Matches Found: {len(matches)}")

for row in matches[:100]:
    print(row)