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

for edge in edges:
    edge1 = edge[0]
    edge2 = edge[1]
    G.add_edge(edge1, edge2)

G.remove_edges_from(functions.fall(G.edges(), G))
G.remove_nodes_from(functions.fall_nodes(G.nodes(), G))

while not end_game:
    H = G.copy()
    H.remove_edges_from(G.edges())
    cool = functions.double_edges(list(G.edges()))
    for edge in cool:
        H.add_edge(edge[0], edge[1])
    print(cool)
    print(H.edges())

    pos = nx.random_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='b', node_size=100, alpha = 1)
    ax = plt.gca()
    for e in G.edges:
        ax.annotate("",
                    xy=pos[e[0]], xycoords='data',
                    xytext=pos[e[1]], textcoords='data',
                    arrowprops=dict(arrowstyle="-", color="0.5",
                                    shrinkA=5, shrinkB=5,
                                    patchA=None, patchB=None,
                                    connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                                    ),
                                    ),
                    )
    plt.axis('off')
    plt.show()
    
    edge = (int(input("What should the first point of the edge be? ")), int(input("What should the second point of the edge be? ")))
    
    try:
        new_edges = functions.turn(G.edges(), edge)
        G.clear()
        G.add_node(0)
        for edge in new_edges:
            edge1 = edge[0]
            edge2 = edge[1]
            G.add_edge(edge1, edge2)
        player += 1
        edges = new_edges.copy()
    except:
        end_game = True

print("")

if player % 2 == 0:
    print("Player 1 won!")
else:
    print("Player 2 won!")
