import matplotlib.pyplot as plt
import networkx as nx 

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(2,3),(4,1),(5,2),(3,4)])
G.edges[2,3]["linkki"] = "löytyy"
G.nodes[1]["noodi"] = "on tässä"
G.graph["tämä on"] = "testi kaavio"
print('nodes', G.nodes(data=True))
print('Edges', G.edges(data=True))
print("kaavion tarkoitus", G.graph)

mylayout = nx.circular_layout(G)
nx.draw(G, mylayout, with_labels=True)
mylabels = {
    (2,3): "linkki 2 - 3",
    (3,4): "linkki 3 - 4",
    (1,4): "linkki 1 - 4",
    (5,2): "linkki 5 - 2"
}

nx.draw_networkx_edge_labels(G, pos=mylayout, edge_labels=mylabels)

plt.savefig("peruspiirto.png")
nx.write_graphml(G, "peruspiirto.graphml")
plt.show()
