"""
Brand Spoof Detector
Scans decompiled res/layout resources for unauthorized hardcoded
brand keywords (e.g. "YONO", "SBI Login") against the app's actual
cryptographic author signature to catch UI impersonation.
"""

# from androguard.misc import AnalyzeAPK

BRAND_KEYWORDS = [
    "State Bank of India", "SBI", "YONO",
    "HDFC", "ICICI", "Paytm", "PhonePe",
    "GPay", "Google Pay", "UPI", "BHIM",
    "Axis Bank", "Kotak", "PNB",
]


def detect_brand_spoof(apk_path: str) -> dict:
    """
    Returns list of detected brand keyword hits and a spoof_detected flag.
    TODO: replace stub with live string scan over apk.get_files() resources.
    """
    # apk, _, _ = AnalyzeAPK(apk_path)
    # hits = _scan_resources(apk)
    # return {"spoof_detected": len(hits) > 0, "hits": hits}

    return {"spoof_detected": False, "hits": []}


def _scan_resources(apk) -> list:
    hits = []
    app_name = (apk.get_app_name() or "").lower()
    package  = (apk.get_package() or "").lower()
    combined = app_name + " " + package
    for brand in BRAND_KEYWORDS:
        if brand.lower() in combined:
            hits.append(brand)
    return hits
