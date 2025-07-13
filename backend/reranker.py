# reranker.py

# Keyword rules
keyword_rules = {
    "urgent": 15,
    "call me": 10,
    "interested": 10,
    "ready to close": 20,
    "not interested": -15,
    "just exploring": -10,
    "price too high": -10,
    "price high": -10,
    "no time": -10
}

def rerank_score(initial_score: float, comment: str) -> float:
    comment_lower = comment.lower()
    adjustment = 0
    matched = False

    for keyword, score in keyword_rules.items():
        if keyword in comment_lower:
            adjustment += score
            matched = True

    # If no keyword matched, fallback adjustment is zero (no change)
    if not matched:
        adjustment = 0

    final_score = max(0, min(100, initial_score + adjustment))
    return final_score
