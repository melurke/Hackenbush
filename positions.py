import networkx as nx
import functions as f

G = nx.Graph()
edges = []
G.add_edges_from(edges)
G.remove_edges_from(f.fall(G.edges(), G))

position_value = f.value(list(G.edges()))
print(position_value)
