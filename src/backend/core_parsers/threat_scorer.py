"""
Threat Confidence Scorer
Combines manifest analysis and spoof detection into a weighted
0–100 threat score. Returns bilingual risk classification.
"""

WEIGHTS = {
    "dangerous_combo":       40,
    "brand_spoof":           35,
    "excessive_permissions": 15,
}


def compute_threat_score(manifest: dict, spoof: dict) -> dict:
    score = 0

    combos = manifest.get("dangerous_combos", [])
    if combos:
        score += WEIGHTS["dangerous_combo"] * min(len(combos), 2)

    if spoof.get("spoof_detected"):
        score += WEIGHTS["brand_spoof"]

    if len(manifest.get("permissions", [])) > 15:
        score += WEIGHTS["excessive_permissions"]

    score = min(score, 100)
    return {"score": score, **_classify(score)}


def _classify(score: int) -> dict:
    if score >= 75:
        return {"label": "HIGH RISK",   "label_kn": "ಅತ್ಯಧಿಕ ಅಪಾಯ", "color": "#FF3B30"}
    elif score >= 40:
        return {"label": "MEDIUM RISK", "label_kn": "ಮಧ್ಯಮ ಅಪಾಯ",   "color": "#FF9500"}
    else:
        return {"label": "LOW RISK",    "label_kn": "ಕಡಿಮೆ ಅಪಾಯ",   "color": "#34C759"}
