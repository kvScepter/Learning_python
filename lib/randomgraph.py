import networkx as nx
from numpy.random import default_rng

'''
returns a random graph

required parameters:
    - number of nodes (int)
    - probability of link (float between 0 and 1)
    - directed graph or not (boolean)

optional parameters:
    - seed for random generator (int)
    - edgerange: tuple (A,B) of integers, A < B
        + the weights of the edges are chosen from the range
        + the right endpoint B is excluded
    - the name for the edge weight attribute (default: 'weight')
'''
def randomgraph(nodes, link_probability, directed, seed=None, edgerange=None, weight='weight'):
    while True:
        G = nx.erdos_renyi_graph(nodes, link_probability, directed=directed, seed=seed)
        connected = nx.is_strongly_connected if directed else nx.is_connected
        if connected(G):
            break
    if edgerange is not None:
        rng = default_rng(seed) if seed is not None else default_rng()
        for (u, v) in G.edges():
            G.edges[u,v][weight] = int(rng.integers(*edgerange))
    return G
