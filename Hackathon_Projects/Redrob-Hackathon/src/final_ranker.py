import csv
import json
from pathlib import Path

from extract_features import extract_candidate_text
from scoring import score_candidate

DATA_PATH = Path("data/candidates.jsonl")
OUTPUT_PATH = Path("output/submission_final_v1.csv")


def build_reasoning(candidate, result):
    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    title = profile.get("current_title", "Candidate")
    years = profile.get("years_of_experience", 0)
    company = profile.get("current_company", "current company")

    career_matches = result.get("career_matches", [])
    ai_matches = result.get("positive_matches", [])

    evidence = career_matches[:3] + ai_matches[:2]
    evidence_text = ", ".join(evidence) if evidence else "limited direct evidence"

    behavior_parts = []

    if signals.get("open_to_work_flag"):
        behavior_parts.append("open to work")

    if signals.get("recruiter_response_rate", 0) >= 0.7:
        behavior_parts.append("strong recruiter response rate")
    elif signals.get("recruiter_response_rate", 0) < 0.35:
        behavior_parts.append("lower recruiter response rate")

    if signals.get("notice_period_days", 180) <= 30:
        behavior_parts.append("short notice period")
    elif signals.get("notice_period_days", 180) >= 90:
        behavior_parts.append("longer notice period")

    behavior_text = ", ".join(behavior_parts) if behavior_parts else "moderate engagement signals"

    reason = (
    f"{title} with {years} years at {company}, showing JD-relevant evidence such as {evidence_text}. "
    f"Behavioral fit includes {behavior_text}, so the rank balances technical match with hiring availability."
)

    return " ".join(reason.split())

    return (
        f"{title} with {years} years at {company}, showing JD-relevant evidence such as {evidence_text}. "
        f"Behavioral fit includes {behavior_text}, so the rank balances technical match with hiring availability."
    )


def main():
    results = []

    print("Scoring all candidates...")

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        for line in file:
            if not line.strip():
                continue

            candidate = json.loads(line)
            text = extract_candidate_text(candidate)
            result = score_candidate(candidate, text)

            results.append({
                "candidate_id": candidate["candidate_id"],
                "score": result["score"],
                "reasoning": build_reasoning(candidate, result)
            })

    results.sort(key=lambda x: (-x["score"], x["candidate_id"]))
    top_100 = results[:100]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

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

    print("Done.")
    print(f"Total scored: {len(results)}")
    print(f"Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()