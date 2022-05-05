import ast
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
        if not nx.has_path(G, 0, edge[0]):
            falling.append(edge)
    return falling

def fall_nodes(nodes, G):
    falling = []
    for node in nodes:
        if not nx.has_path(G, node, 0):
            falling.append(node)
    return falling

def turn(edges, edge):
    G = nx.Graph()
    G.add_edges_from(edges)
    G.remove_edge(edge[0], edge[1])
    G.remove_edges_from(fall(G.edges(), G))
    G.remove_nodes_from(fall_nodes(G.nodes(), G))
    return list(G.edges())

def followers(G):
    next = []
    test = list(G.edges())
    for edge in G.edges():
        edges = test.copy()
        next.append(turn(edges, edge))

G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 2)])
print(followers(G))
