import json
from pathlib import Path

from extract_features import extract_candidate_text
from scoring import score_candidate

DATA_PATH = Path("data/candidates.jsonl")

TARGET_IDS = {
    "CAND_0000031",
    "CAND_0009024",
    "CAND_0000666",
    "CAND_0000001",
}


def main():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        for line in file:
            candidate = json.loads(line)

            if candidate["candidate_id"] in TARGET_IDS:
                text = extract_candidate_text(candidate)
                result = score_candidate(candidate, text)
                profile = candidate["profile"]

                print("=" * 70)
                print("ID:", candidate["candidate_id"])
                print("Title:", profile["current_title"])
                print("Company:", profile["current_company"])
                print("Experience:", profile["years_of_experience"])
                print("Final Score:", result["score"])
                print("Title Score:", result["title_score"])
                print("Experience Score:", result["experience_score"])
                print("Career Score:", result["career_score"])
                print("AI Score:", result["ai_score"])
                print("Behavior Score:", result["behavior_score"])
                print("Penalty:", result["penalty_score"])
                print("Career Matches:", result["career_matches"])
                print("AI Matches:", result["positive_matches"])


if __name__ == "__main__":
    main()