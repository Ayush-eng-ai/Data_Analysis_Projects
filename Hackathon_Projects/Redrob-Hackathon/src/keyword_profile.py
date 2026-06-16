import json
from pathlib import Path
from collections import Counter

DATA_PATH = Path("data/candidates.jsonl")

KEYWORDS = [
    "retrieval",
    "ranking",
    "recommendation",
    "embeddings",
    "vector",
    "pinecone",
    "milvus",
    "faiss",
    "qdrant",
    "elasticsearch",
    "opensearch",
    "llm",
    "machine learning",
    "ndcg",
    "mrr",
    "map",
    "a/b testing",
    "python"
]

keyword_counts = Counter()
total_candidates = 0

with open(DATA_PATH, "r", encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            continue

        candidate = json.loads(line)
        total_candidates += 1

        profile = candidate.get("profile", {})
        career_history = candidate.get("career_history", [])
        skills = candidate.get("skills", [])

        text = " ".join([
            profile.get("headline", ""),
            profile.get("summary", ""),
            " ".join(job.get("description", "") for job in career_history),
            " ".join(skill.get("name", "") for skill in skills)
        ]).lower()

        for keyword in KEYWORDS:
            if keyword.lower() in text:
                keyword_counts[keyword] += 1

print("=" * 60)
print("KEYWORD PROFILE")
print("=" * 60)

print(f"\nTotal Candidates: {total_candidates}")

print("\nKeyword Frequency:")
for keyword, count in keyword_counts.most_common():
    percentage = round((count / total_candidates) * 100, 2)
    print(f"{keyword:<20} {count:<8} ({percentage}%)")