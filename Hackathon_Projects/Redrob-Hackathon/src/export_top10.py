import csv

with open("output/submission_final_v1.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("=" * 80)
    print("TOP 10 FINAL CANDIDATES")
    print("=" * 80)

    for i, row in enumerate(reader, start=1):
        print(
            f"{i}. {row['candidate_id']} | Score={row['score']}"
        )

        if i == 10:
            break