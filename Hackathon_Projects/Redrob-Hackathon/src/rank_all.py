import csv
import json
from pathlib import Path

from extract_features import extract_candidate_text
from scoring import score_candidate

DATA_PATH = Path("data/candidates.jsonl")
OUTPUT_PATH = Path("output/submission_v1.csv")


def load_and_score_candidates():
    results = []

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            candidate = json.loads(line)
            text = extract_candidate_text(candidate)
            score_data = score_candidate(candidate, text)

            results.append({
                "candidate_id": candidate["candidate_id"],
                "score": score_data["score"],
                "reasoning": build_reasoning(candidate, score_data)
            })

    return results


def build_reasoning(candidate, score_data):
    profile = candidate.get("profile", {})
    title = profile.get("current_title", "candidate")
    years = profile.get("years_of_experience", 0)

    positives = score_data.get("career_matches", []) + score_data.get("positive_matches", [])
    positives_text = ", ".join(positives[:3]) if positives else "limited direct AI/ranking evidence"

    return (
        f"{title} with {years} years of experience; matched signals include {positives_text}. "
        f"Score reflects experience, technical fit, behavioral signals, and profile-risk penalties."
    )


def write_submission(results):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    top_100 = sorted(
        results,
        key=lambda x: (-x["score"], x["candidate_id"])
    )[:100]

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])

        for rank, item in enumerate(top_100, start=1):
            writer.writerow([
                item["candidate_id"],
                rank,
                item["score"],
                item["reasoning"]
            ])


def main():
    print("Loading and scoring candidates...")
    results = load_and_score_candidates()

    print(f"Scored candidates: {len(results)}")

    write_submission(results)

    print(f"Submission file created: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()