import json
from pathlib import Path
from collections import Counter

DATA_PATH = Path("data/candidates.jsonl")

counter = Counter()

with open(DATA_PATH, "r", encoding="utf-8") as file:
    for line in file:
        candidate = json.loads(line)

        title = candidate["profile"].get(
            "current_title",
            "Unknown"
        )

        counter[title] += 1

print("\nTOP AI TITLES\n")

for title, count in counter.most_common(30):
    if any(word in title.lower() for word in [
        "engineer",
        "scientist",
        "ai",
        "ml",
        "search",
        "backend"
    ]):
        print(title, count)