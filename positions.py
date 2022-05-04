import networkx as nx
import functions

G = nx.Graph()
G.add_nodes_from([0, 1, 2])
G.add_edges_from([(0, 1), (0, 2)])

print(functions.g(G))
