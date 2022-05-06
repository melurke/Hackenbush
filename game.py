import networkx as nx
import matplotlib.pyplot as plt
import functions

G = nx.MultiGraph()
H = nx.MultiDiGraph()
G.add_node(0)

end_game = False
player = 1
num_of_edges = int(input("How many edges should there be? "))
edges = []
point1 = 0
point2 = 0
options = {
    'edge_color': 'green'
}

for i in range(0, num_of_edges):
    point1 = int(input(f"What should the first point of the {i+1}. edge be? "))
    point2 = int(input(f"What should the second point of the {i+1}. edge be? "))
    if not point1 in G.nodes():
        G.add_node(point1)
    if not point2 in G.nodes():
        G.add_node(point2)

    edges.append((point1, point2))

G.add_edges_from(edges)

G.remove_edges_from(functions.fall(G.edges(), G))
G.remove_nodes_from(functions.fall_nodes(G.nodes(), G))

while not end_game:
    H = G.copy()
    test = list(G.edges()).copy()
    H.remove_edges_from(G.edges())
    for edge in functions.double_edges(test):
        print(edge)
        H.add_edge(edge[0], edge[1])
        print(H.edges())
    pos = nx.spring_layout(H)
    nx.draw_networkx_nodes(H, pos, node_size = 500)
    nx.draw_networkx_labels(H, pos)
    nx.draw_networkx_edges(H, pos, connectionstyle='arc3, rad = 0.1', width = 2, arrows=True)
    plt.show()
    
    edge = (int(input("What should the first point of the edge be? ")), int(input("What should the second point of the edge be? ")))
    
    try:
        new_edges = functions.turn(G.edges(), edge)
        G.clear()
        G.add_node(0)
        G.add_edges_from(new_edges)
        player += 1
        edges = new_edges.copy()
    except:
        end_game = True

print("")

if player % 2 == 0:
    print("Player 1 won!")
else:
    print("Player 2 won!")
