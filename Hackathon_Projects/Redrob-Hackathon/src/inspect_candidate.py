import json
from pathlib import Path

DATA_PATH = Path("data/candidates.jsonl")

TARGET_ID = "CAND_0000031"  # Replace with the actual candidate ID you want to inspect

with open(DATA_PATH, "r", encoding="utf-8") as file:
    for line in file:
        candidate = json.loads(line)

        if candidate["candidate_id"] == TARGET_ID:

            print("=" * 80)
            print("CANDIDATE FOUND")
            print("=" * 80)

            print("\nPROFILE")
            print(candidate["profile"])

            print("\nCAREER HISTORY")
            for job in candidate["career_history"]:
                print("\n---")
                print(job)

            print("\nSKILLS")
            for skill in candidate["skills"]:
                print(skill)

            print("\nSIGNALS")
            print(candidate["redrob_signals"])

            break