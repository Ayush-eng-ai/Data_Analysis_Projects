import json
from pathlib import Path

from extract_features import extract_candidate_text
from scoring import score_candidate

DATA_PATH = Path("data/candidates.jsonl")


def load_candidates(limit=10):
    candidates = []

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        for i, line in enumerate(file):
            if i >= limit:
                break

            if line.strip():
                candidates.append(json.loads(line))

    return candidates


def main():
    candidates = load_candidates(10)
    results = []

    for candidate in candidates:
        text = extract_candidate_text(candidate)
        score_data = score_candidate(candidate, text)

        profile = candidate.get("profile", {})

        results.append({
            "candidate_id": candidate.get("candidate_id"),
            "title": profile.get("current_title"),
            "experience": profile.get("years_of_experience"),
            "score": score_data["score"],
            "positives": score_data["positive_matches"],
            "negatives": score_data["negative_matches"]
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    print("=" * 70)
    print("FIRST 10 CANDIDATE SCORING TEST")
    print("=" * 70)

    for rank, item in enumerate(results, start=1):
        print(f"\nRank {rank}")
        print(f"ID: {item['candidate_id']}")
        print(f"Title: {item['title']}")
        print(f"Experience: {item['experience']}")
        print(f"Score: {item['score']}")
        print(f"Positive: {item['positives']}")
        print(f"Negative: {item['negatives']}")


if __name__ == "__main__":
    main()