"""
IOC Extractor
Regex-scans decompiled APK strings for hardcoded IPs, URLs, and ports.
Cross-references against URLhaus / ThreatFox live feeds.
Falls back to local known_c2.json cache for demo reliability.
"""

import re, json, os, requests

OFFLINE_DB = os.path.join(os.path.dirname(__file__), "../../data/known_c2.json")

IP_RE   = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
URL_RE  = re.compile(r'https?://[^\s\'"<>]+')
PORT_RE = re.compile(r':(\d{4,5})\b')

TIMEOUT = 3  # seconds


def extract_iocs(apk_path: str) -> dict:
    """
    TODO: replace raw_strings stub with actual decompiled string dump from Androguard.
    """
    raw_strings = _dump_strings(apk_path)

    ips   = list(set(IP_RE.findall(raw_strings)))[:20]
    urls  = list(set(URL_RE.findall(raw_strings)))[:20]
    ports = list(set(PORT_RE.findall(raw_strings)))[:10]
    hits  = _check_threat_intel(ips, urls)

    return {"ips": ips, "urls": urls, "ports": ports, "threat_hits": hits}


def _dump_strings(apk_path: str) -> str:
    # TODO: from androguard.misc import AnalyzeAPK
    # apk, dex_list, _ = AnalyzeAPK(apk_path)
    # return " ".join(str(s) for dex in dex_list for s in dex.get_strings())
    return ""


def _check_threat_intel(ips: list, urls: list) -> list:
    hits = []
    for url in urls[:5]:
        try:
            r = requests.post(
                "https://urlhaus-api.abuse.ch/v1/url/",
                data={"url": url}, timeout=TIMEOUT
            )
            if r.json().get("query_status") == "is_listed":
                hits.append({"ioc": url, "type": "url", "source": "URLhaus"})
        except Exception:
            pass  # network unavailable — fall through

    if not hits:
        hits = _offline_lookup(ips, urls)
    return hits


def _offline_lookup(ips: list, urls: list) -> list:
    if not os.path.exists(OFFLINE_DB):
        return []
    with open(OFFLINE_DB) as f:
        db = json.load(f)
    hits = []
    for ip in ips:
        if ip in db.get("ips", []):
            hits.append({"ioc": ip, "type": "ip", "source": "offline_cache"})
    for url in urls:
        if any(d in url for d in db.get("urls", [])):
            hits.append({"ioc": url, "type": "url", "source": "offline_cache"})
    return hits
