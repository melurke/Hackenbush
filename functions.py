import networkx as nx

pos = {
    "[]": 0,
}

def mex(K):
    for i in range(0, max(K)+2):
        if not i in K:
            return i

def fall(edges, G):
    falling = []

    for edge in edges:
        if not nx.has_path(G, 0, edge[0]) and not nx.has_path(G, edge[0], 0) and not nx.has_path(G, 0, edge[1]) and not nx.has_path(G, edge[1], 0):
            falling.append(edge)
    return falling

def fall_nodes(nodes, G):
    falling = []
    for node in nodes:
        if not nx.has_path(G, 0, node) and not nx.has_path(G, node, 0):
            falling.append(node)
    return falling

def turn(edges, edge):
    G = nx.MultiDiGraph()
    edges = list(edges)
    edges.remove(edge)
    G.add_edges_from(edges)
    G.remove_edges_from(fall(G.edges(), G))
    G.remove_nodes_from(fall_nodes(G.nodes(), G))
    return list(G.edges())

def followers(G):
    next = []
    test = list(G.edges())
    for edge in G.edges():
        edges = test.copy()
        next.append(turn(edges, edge))

def double_edges(edges):
    for edge in edges:
        e = edges.copy()
        e.remove(edge)
        if edge in e:
            edges[edges.index(edge)] = (edge[1], edge[0])
    return edges
