print("Alpha Decoder - Redrob Hackathon")
print("Ranking Engine Started")


import json
from pathlib import Path

DATA_PATH = Path("data/candidates.jsonl")

def count_candidates():
    count = 0
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                count += 1
    return count

def main():
    total = count_candidates()
    print("Alpha Decoder - Redrob Ranking Engine")
    print("-" * 40)
    print(f"Total candidates found: {total}")

if __name__ == "__main__":
    main()