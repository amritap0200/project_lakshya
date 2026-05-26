"""
DNA Matcher
Compares an APK's FCG fingerprint against the local case database
using cosine similarity on degree sequences.
Matches >= 80% similarity flag a genealogy hit — even if the hacker
renamed functions or obfuscated variable names.
"""

import json, os, uuid

DB_PATH = os.path.join(os.path.dirname(__file__), "../../data/dna_db.json")


def match_dna(fcg: dict) -> dict:
    """
    Returns list of prior cases with >= 80% structural similarity.
    Also persists the new fingerprint to the case database.
    """
    matches = _compare_against_db(fcg)
    _store(fcg)
    return {"matches": matches, "total_cases_checked": _db_size()}


def _compare_against_db(fcg: dict) -> list:
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH) as f:
        db = json.load(f)
    results = []
    for case in db.get("cases", []):
        sim = _cosine(fcg.get("degree_seq", []), case.get("degree_seq", []))
        if sim >= 0.80:
            results.append({"case_id": case["case_id"], "similarity": round(sim * 100, 1)})
    return sorted(results, key=lambda x: -x["similarity"])


def _cosine(a: list, b: list) -> float:
    n     = max(len(a), len(b))
    a_pad = a + [0] * (n - len(a))
    b_pad = b + [0] * (n - len(b))
    dot   = sum(x * y for x, y in zip(a_pad, b_pad))
    ma    = sum(x ** 2 for x in a_pad) ** 0.5
    mb    = sum(x ** 2 for x in b_pad) ** 0.5
    return dot / (ma * mb) if ma and mb else 0.0


def _store(fcg: dict):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    db = {"cases": []}
    if os.path.exists(DB_PATH):
        with open(DB_PATH) as f:
            db = json.load(f)
    db["cases"].append({"case_id": str(uuid.uuid4())[:8], **fcg})
    with open(DB_PATH, "w") as f:
        json.dump(db, f, indent=2)


def _db_size() -> int:
    if not os.path.exists(DB_PATH):
        return 0
    with open(DB_PATH) as f:
        return len(json.load(f).get("cases", []))
