"""
Graph Cluster Engine
Uses NetworkX to build a cross-case infrastructure graph.
IPs and URLs sharing subnet ranges or registrars are connected —
visually mapping independent cases to a single threat actor group.
"""

# import networkx as nx


def build_cluster(iocs: dict) -> dict:
    """
    Returns nodes and edges for the frontend Network Flow Visualization.
    TODO: replace stub with live NetworkX graph build below.
    """
    ips  = iocs.get("ips", [])
    urls = iocs.get("urls", [])
    hits = {h["ioc"] for h in iocs.get("threat_hits", [])}

    # G = nx.Graph()
    # for ip in ips:
    #     G.add_node(ip, node_type="ip", malicious=(ip in hits))
    # for url in urls:
    #     G.add_node(url, node_type="url", malicious=(url in hits))
    # for url in urls:
    #     for ip in ips:
    #         if ip[:6] in url:
    #             G.add_edge(ip, url, relation="serves")
    # nodes = [{"id": n, **G.nodes[n]} for n in G.nodes]
    # edges = [{"source": u, "target": v} for u, v in G.edges]

    nodes = [{"id": ip,  "node_type": "ip",  "malicious": ip  in hits} for ip  in ips]
    nodes += [{"id": url, "node_type": "url", "malicious": url in hits} for url in urls]
    edges = []  # TODO: populate from NetworkX

    return {"nodes": nodes, "edges": edges}
