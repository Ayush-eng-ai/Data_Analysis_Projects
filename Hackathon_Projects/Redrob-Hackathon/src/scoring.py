# def keyword_score(text, keywords, points_per_match=5, max_score=40):
#     score = 0
#     matched = []

#     for keyword in keywords:
#         if keyword.lower() in text:
#             score += points_per_match
#             matched.append(keyword)

#     return min(score, max_score), matched


# AI_KEYWORDS = [
#     "retrieval", "ranking", "recommendation", "search",
#     "embeddings", "vector", "faiss", "milvus", "qdrant",
#     "pinecone", "elasticsearch", "opensearch", "nlp", "llm",
#     "python", "machine learning", "evaluation", "ndcg", "mrr", "map"
# ]

# NEGATIVE_KEYWORDS = [
#     "marketing manager", "accountant", "hr manager", "customer support",
#     "content writing", "seo", "brand design", "mechanical engineer",
#     "civil engineer"
# ]


# def experience_score(years):
#     if 6 <= years <= 8:
#         return 20
#     if 5 <= years < 6 or 8 < years <= 9:
#         return 16
#     if 4 <= years < 5 or 9 < years <= 11:
#         return 8
#     return 0


# def behavior_score(signals):
#     score = 0

#     if signals.get("open_to_work_flag"):
#         score += 5

#     score += min(signals.get("recruiter_response_rate", 0) * 5, 5)
#     score += min(signals.get("interview_completion_rate", 0) * 5, 5)

#     github = signals.get("github_activity_score", -1)
#     if github > 0:
#         score += min(github / 20, 5)

#     notice = signals.get("notice_period_days", 180)
#     if notice <= 30:
#         score += 5
#     elif notice <= 60:
#         score += 3
#     elif notice <= 90:
#         score += 1

#     return score


# def score_candidate(candidate, text):
#     profile = candidate.get("profile", {})
#     signals = candidate.get("redrob_signals", {})

#     years = profile.get("years_of_experience", 0)
#     exp_score = experience_score(years)

#     text_score, positives = keyword_score(
#         text, AI_KEYWORDS, points_per_match=4, max_score=40
#     )

#     penalty_score, negative_matches = keyword_score(
#         text, NEGATIVE_KEYWORDS, points_per_match=6, max_score=30
#     )

#     beh_score = behavior_score(signals)

#     final_score = exp_score + text_score + beh_score - penalty_score
#     final_score = max(0, round(final_score, 2))

#     return {
#         "score": final_score,
#         "experience_score": exp_score,
#         "text_score": text_score,
#         "behavior_score": round(beh_score, 2),
#         "penalty_score": penalty_score,
#         "positive_matches": positives,
#         "negative_matches": negative_matches
#     }

TITLE_BOOST = {
    "search engineer": 25,
    "recommendation systems engineer": 25,
    "ml engineer": 20,
    "ai research engineer": 20,
    "data scientist": 16,
    "backend engineer": 12,
    "data engineer": 12,
    "senior software engineer": 10,
    "software engineer": 8,
}

CAREER_EVIDENCE_KEYWORDS = [
    "learning-to-rank",
    "ranking model",
    "ranking models",
    "ranking layer",
    "re-ranking",
    "recommendation system",
    "recommendation systems",
    "search system",
    "embedding-based retrieval",
    "information retrieval",
    "offline-online",
    "a/b testing",
    "relevance labeling",
    "feature pipeline",
    "production",
]

AI_KEYWORDS = [
    "python", "embeddings", "sentence transformers", "faiss", "milvus",
    "qdrant", "pinecone", "elasticsearch", "opensearch", "vector",
    "nlp", "llm", "machine learning", "retrieval", "ranking",
    "recommendation", "mlflow", "xgboost", "lightgbm"
]

NEGATIVE_KEYWORDS = [
    "marketing manager", "accountant", "hr manager", "customer support",
    "content writing", "seo", "brand design", "mechanical engineer",
    "civil engineer", "operations manager", "sales executive",
    "graphic designer"
]


def keyword_score(text, keywords, points_per_match=5, max_score=40):
    score = 0
    matched = []

    for keyword in keywords:
        if keyword.lower() in text:
            score += points_per_match
            matched.append(keyword)

    return min(score, max_score), matched


def experience_score(years):
    if 6 <= years <= 8:
        return 20
    if 5 <= years < 6 or 8 < years <= 9:
        return 16
    if 4 <= years < 5 or 9 < years <= 11:
        return 8
    return 0


def title_score(title):
    title = title.lower()

    for key, value in TITLE_BOOST.items():
        if key in title:
            return value

    return 0


def behavior_score(signals):
    score = 0

    if signals.get("open_to_work_flag"):
        score += 5

    score += min(signals.get("recruiter_response_rate", 0) * 5, 5)
    score += min(signals.get("interview_completion_rate", 0) * 5, 5)

    github = signals.get("github_activity_score", -1)
    if github > 0:
        score += min(github / 20, 5)

    notice = signals.get("notice_period_days", 180)
    if notice <= 30:
        score += 5
    elif notice <= 60:
        score += 3
    elif notice <= 90:
        score += 1

    if signals.get("willing_to_relocate"):
        score += 3

    return score


def score_candidate(candidate, text):
    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    years = profile.get("years_of_experience", 0)
    current_title = profile.get("current_title", "")

    exp_score = experience_score(years)
    t_score = title_score(current_title)

    career_score, career_matches = keyword_score(
        text,
        CAREER_EVIDENCE_KEYWORDS,
        points_per_match=8,
        max_score=45
    )

    ai_score, ai_matches = keyword_score(
        text,
        AI_KEYWORDS,
        points_per_match=3,
        max_score=30
    )

    penalty_score, negative_matches = keyword_score(
        text,
        NEGATIVE_KEYWORDS,
        points_per_match=10,
        max_score=50
    )

    beh_score = behavior_score(signals)

    final_score = (
        exp_score
        + t_score
        + career_score
        + ai_score
        + beh_score
        - penalty_score
    )

    final_score = max(0, round(final_score, 2))

    return {
        "score": final_score,
        "experience_score": exp_score,
        "title_score": t_score,
        "career_score": career_score,
        "ai_score": ai_score,
        "behavior_score": round(beh_score, 2),
        "penalty_score": penalty_score,
        "career_matches": career_matches,
        "positive_matches": ai_matches,
        "negative_matches": negative_matches
    }