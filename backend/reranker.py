# reranker.py

# Keyword rules
keyword_rules = {
    # Strong Positive Intents
    "urgent": 15,
    "very urgent": 18,
    "call me": 10,
    "please call": 10,
    "interested": 10,
    "very interested": 12,
    "ready to close": 20,
    "ready to proceed": 18,
    "looking to buy": 15,
    "buying now": 18,
    "need this": 12,
    "want to purchase": 15,
    "confirm asap": 10,
    "ready to pay": 20,
    "finalizing soon": 18,
    "decision made": 15,
    "serious buyer": 15,
    "hot lead": 18,
    "send quotation": 10,
    "send proposal": 10,
    "budget approved": 15,
    "next step": 10,
    "moving ahead": 12,
    "let's do this": 10,
    "willing to close": 18,
    "need call back": 10,
    "schedule call": 10,
    "discuss deal": 12,
    "confirm deal": 15,
    "make it quick": 10,
    "closing this week": 20,
    "today": 8,
    "priority": 8,
    "genuine inquiry": 8,
    "get in touch": 10,
    "asap": 10,
    "talk now": 10,
    "in a hurry": 12,
    "proceeding": 12,
    "deal ready": 15,
    
    # Strong Negative Intents
    "not interested": -15,
    "no interest": -15,
    "not now": -12,
    "maybe later": -10,
    "just exploring": -10,
    "just looking": -10,
    "just enquiring": -8,
    "only browsing": -8,
    "price too high": -10,
    "too expensive": -12,
    "no budget": -15,
    "budget not approved": -12,
    "no time": -10,
    "not a priority": -10,
    "low priority": -10,
    "thinking": -6,
    "not urgent": -8,
    "no decision yet": -10,
    "not sure": -8,
    "undecided": -10,
    "window shopping": -12,
    "browsing only": -10,
    "doubtful": -10,
    "just checking": -8,
    "comparing options": -8,
    "need time": -8,
    "not planning": -12,
    "don’t call": -15,
    "stop calling": -15,
    "already bought": -12,
    "deal closed": -10,
    "talked to someone else": -10,
    "not convinced": -10,
    "not ready": -10,
    "not looking": -12,
    "already decided": -8,
    "reached out by mistake": -15,
    "spam": -20,
    "wrong number": -15,
    "remove me": -20,
    "unsubscribe": -20
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
