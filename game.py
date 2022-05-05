import networkx as nx
import matplotlib.pyplot as plt
import functions

G = nx.Graph()
G.add_node(0)

end_game = False
player = 1
num_of_edges = int(input("How many edges should there be? "))
edges = []
point1 = 0
point2 = 0

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
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    
    edge = [int(input("What should the first point of the edge be? ")), int(input("What should the second point of the edge be? "))]
    try:
        new_edges = functions.turn(G.edges(), edge)
        G.clear()
        G.add_node(0)
        G.add_edges_from(new_edges)
        player += 1
    except:
        end_game = True

print("")

if player % 2 == 0:
    print("Player 1 won!")
else:
    print("Player 2 won!")
