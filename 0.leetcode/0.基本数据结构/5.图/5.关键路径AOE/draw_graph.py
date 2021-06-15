import networkx as nx
import matplotlib.pyplot as plt
point=[1,2,3,4,5,6,7,8,9]
edges = [(1, 2, 3), (1, 3, 2), (1, 4, 4), (2, 5, 4), (2, 3, 0), (3, 5, 4), (3, 6, 4), (3, 4, 2), (4, 7, 5),
         (5, 9, 6), (5, 7, 3), (5, 6, 0), (6, 8, 3), (8, 9, 1), (7, 8, 1)]
G=nx.DiGraph()

G.add_nodes_from(point)
edgelist=[edgei[:2] for edgei in edges]
print(edgelist)
G.add_edges_from(edgelist)
position = nx.circular_layout(G)
nx.draw_networkx_nodes(G,position, nodelist=point, node_color="r")
nx.draw_networkx_edges(G,position)
nx.draw_networkx_labels(G,position)
plt.show()