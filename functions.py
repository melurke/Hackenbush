import ast
import networkx as nx

pos = {
    "[]": 0,
}

def mex(K):
    for i in range(0, max(K)+2):
        if not i in K:
            return i

def remove_letters(word):
    result = []
    for letter in word:
        try:
            result.append(int(letter))
        except:
            pass
    return result

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

def test_turn(F):
    next = []
    edges = ""
    nodes = ""
    G = F.copy()
    for edge in G.edges():
        G = F.copy()
        G.remove_edge(edge[0], edge[1])
        G.remove_edges_from(fall(G.edges(), G))
        G.remove_nodes_from(fall_nodes(G.nodes(), G))
        edges = remove_letters(str(G.edges()))
        nodes = remove_letters(str(G.nodes()))
        next.append([nodes, edges])
    return next

def g(G):
    next = test_turn(G)

    for follower in next:
        G = nx.Graph()
        G.add_nodes_from(follower[0])
        G.add_edges_from(follower[1])
        if not str(G.edges()) in pos:
            pos[G.edges()] = g(G)
        print(G.edges())

    for i in range(0, len(next)):
        next[i] = [next[i], g(next[i])]
    
    return mex(next[:][1])
