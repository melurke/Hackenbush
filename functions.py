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
        if not nx.has_path(G, 0, node):
            falling.append(node)
    return falling

def turn(G, edge):
    G.remove_edge(edge[0], edge[1])
    G.remove_edges_from(fall(G.edges(), G))
    G.remove_nodes_from(fall_nodes(G.nodes(), G))
    return G

def test_turn(G):
    next = []
    F = G.edges()
    for edge in F:
        G.remove_edge(edge[0], edge[1])
        G.remove_edges_from(fall(G.edges(), G))
        G.remove_nodes_from(fall_nodes(G.nodes(), G))
        next.append(G)
    return next

def g(G):
    next = test_turn(G)
    for follower in next:
        if not str(follower.edges) in pos:
            pos[follower.edges] = g(follower)

    for i in range(0, len(next)):
        next[i] = [next[i], g(next[i])]
    
    return mex(next[:][1])