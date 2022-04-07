from matplotlib.font_manager import _Weight
import networkx as nx
import sys

G = nx.DiGraph()

G.add_node("A", demand=-5)
G.add_node("D", demand=5)
G.add_edge("A", "B", weight=3, capasity=4)
G.add_edge("A", "C", weight=6, capasity=10)
G.add_edge("B", "D", weight=1, capasity=9)
G.add_edge("C", "D", weight=2, capasity=5)

flowcost, flowdict = nx.network_simplex(G)

print(flowcost, flowdict)
