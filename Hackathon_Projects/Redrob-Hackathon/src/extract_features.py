import json
from pathlib import Path
from scoring import score_candidate

DATA_PATH = Path("data/candidates.jsonl")


def load_first_candidate():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        first_line = file.readline()
        return json.loads(first_line)


def extract_candidate_text(candidate):
    profile = candidate.get("profile", {})
    career_history = candidate.get("career_history", [])
    skills = candidate.get("skills", [])

    profile_text = " ".join([
        profile.get("headline", ""),
        profile.get("summary", ""),
        profile.get("current_title", ""),
        profile.get("current_industry", "")
    ])

    career_text = " ".join([
        f"{job.get('title', '')} {job.get('industry', '')} {job.get('description', '')}"
        for job in career_history
    ])

    skills_text = " ".join([
        skill.get("name", "")
        for skill in skills
    ])

    return f"{profile_text} {career_text} {skills_text}".lower()


def main():
    candidate = load_first_candidate()
    text = extract_candidate_text(candidate)

    result = score_candidate(candidate, text)

    print("=" * 50)
    print("SCORING TEST")
    print("=" * 50)
    print("Candidate ID:", candidate["candidate_id"])
    print("Text Length:", len(text))

    print("\nFinal Score:", result["score"])
    print("Experience Score:", result["experience_score"])
    print("Text Score:", result["text_score"])
    print("Behavior Score:", result["behavior_score"])
    print("Penalty Score:", result["penalty_score"])
    print("Positive Matches:", result["positive_matches"])
    print("Negative Matches:", result["negative_matches"])


if __name__ == "__main__":
    main()