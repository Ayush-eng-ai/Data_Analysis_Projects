import json
from pathlib import Path
from collections import Counter

DATA_PATH = Path("data/candidates.jsonl")

title_counter = Counter()
company_counter = Counter()

total_candidates = 0
open_to_work_count = 0
github_50_plus = 0

TOP_TITLES = [
    "AI Engineer",
    "ML Engineer",
    "Data Scientist",
    "Data Engineer",
    "Backend Engineer",
    "Software Engineer",
    "Business Analyst"
]

SERVICE_COMPANIES = [
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Cognizant",
    "Capgemini"
]

with open(DATA_PATH, "r", encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            continue

        candidate = json.loads(line)

        total_candidates += 1

        profile = candidate.get("profile", {})
        signals = candidate.get("redrob_signals", {})

        title = profile.get("current_title", "Unknown")
        company = profile.get("current_company", "Unknown")

        title_counter[title] += 1
        company_counter[company] += 1

        if signals.get("open_to_work_flag"):
            open_to_work_count += 1

        if signals.get("github_activity_score", -1) > 50:
            github_50_plus += 1


print("=" * 60)
print("DATASET PROFILE")
print("=" * 60)

print(f"\nTotal Candidates: {total_candidates}")

print(f"\nOpen To Work: {open_to_work_count}")
print(f"GitHub Score > 50: {github_50_plus}")

print("\nTop 15 Titles")
for title, count in title_counter.most_common(15):
    print(f"{title}: {count}")

print("\nTop 15 Companies")
for company, count in company_counter.most_common(15):
    print(f"{company}: {count}")

print("\nTarget Titles")
for title in TOP_TITLES:
    print(f"{title}: {title_counter[title]}")

print("\nService Companies")
for company in SERVICE_COMPANIES:
    print(f"{company}: {company_counter[company]}")