"""
FCG Extractor
Builds a Function Call Graph from decompiled .dex bytecode via Androguard.
Converts the graph topology into a numerical fingerprint vector
(degree sequence hash) that is obfuscation-resistant.
"""

# from androguard.misc import AnalyzeAPK
# import networkx as nx
import hashlib


def extract_fcg(apk_path: str) -> dict:
    """
    Returns FCG hash, node/edge counts, and degree sequence for DNA matching.
    TODO: replace stub with live Androguard + NetworkX FCG build below.
    """
    # apk, _, analysis = AnalyzeAPK(apk_path)
    # G = nx.DiGraph()
    # for method in analysis.get_methods():
    #     caller = str(method.get_method())
    #     for _, call, _ in method.get_xref_to():
    #         G.add_edge(caller, str(call))
    # return _vectorize(G)

    return {
        "fcg_hash":   "stub_hash",
        "nodes":      0,
        "edges":      0,
        "degree_seq": [],
    }


def _vectorize(G) -> dict:
    nodes      = G.number_of_nodes()
    edges      = G.number_of_edges()
    deg_seq    = sorted([d for _, d in G.degree()], reverse=True)
    raw        = f"{nodes}:{edges}:{deg_seq[:50]}"
    fcg_hash   = hashlib.sha256(raw.encode()).hexdigest()
    return {"fcg_hash": fcg_hash, "nodes": nodes, "edges": edges, "degree_seq": deg_seq[:20]}
