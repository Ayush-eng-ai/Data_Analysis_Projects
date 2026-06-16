import csv

with open("output/submission_final_v1.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("=" * 80)
    print("TOP 20 CANDIDATES")
    print("=" * 80)

    count = 0

    for row in reader:
        print()
        print("Rank:", row["rank"])
        print("Candidate:", row["candidate_id"])
        print("Score:", row["score"])
        print("Reason:", row["reasoning"])

        count += 1

        if count == 20:
            break