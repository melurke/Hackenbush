import networkx as nx
import functions as f
import ast

G = nx.Graph()

while True:
    edges = ast.literal_eval(input("What are the edges in the graph?\n"))
    if edges == []:
        break
    G.clear()
    G.add_edges_from(edges)
    G.remove_edges_from(f.fall(G.edges(), G))

    followers = f.followers(G)
    follower_values = []
    edge_to_remove = ()

    for follower in followers:
        follower_values.append(f.value(follower))

    if 0 in follower_values:
        edge_to_remove = list(G.edges())[follower_values.index(0)]
    else:
        edge_to_remove = list(G.edges())[follower_values.index(max(follower_values))]

    print(edge_to_remove, 0 in follower_values)
