"""
Manifest Parser
Extracts declared permissions from AndroidManifest.xml and flags
dangerous combinations commonly used in financial fraud APKs.
"""

# from androguard.misc import AnalyzeAPK

DANGEROUS_COMBOS = [
    {"RECEIVE_SMS", "INTERNET"},
    {"READ_SMS", "INTERNET"},
    {"BIND_ACCESSIBILITY_SERVICE", "INTERNET"},
    {"READ_CONTACTS", "RECEIVE_SMS", "INTERNET"},
]


def parse_manifest(apk_path: str) -> dict:
    """
    Returns declared permissions and flagged dangerous combos.
    TODO: replace stub return with live Androguard parse below.
    """
    # apk, _, _ = AnalyzeAPK(apk_path)
    # permissions = [p.replace("android.permission.", "") for p in apk.get_permissions()]
    # combos = _flag_combos(permissions)
    # return {"package": apk.get_package(), "permissions": permissions, "dangerous_combos": combos}

    return {
        "package":          "com.example.stub",
        "permissions":      [],
        "dangerous_combos": [],
    }


def _flag_combos(permissions: list) -> list:
    perm_set = set(permissions)
    return [sorted(c) for c in DANGEROUS_COMBOS if c.issubset(perm_set)]
