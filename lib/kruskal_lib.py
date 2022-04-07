# muokattu reposta
# https://github.com/MUSoC/Visualization-of-popular-algorithms-in-Python

# aika rumaa koodia, vain välttämättömät korjaukset tehty

import networkx as nx
import numpy as np

# A utility function that returns the smallest unprocessed edge
def getMin(G, mstFlag, weight):
    min_edge = (0,0)
    min = float('inf')  # start with min = infinite
    for i in [(u, v, d[weight]) for u, v, d in G.edges(data=True) if weight in d]:
        if mstFlag[i] == False and i[2] < min:
            min = i[2]
            min_edge = i
    return min_edge


# A utility function to find root or origin of the node i in MST
def findRoot(parent, i):
    if parent[i] == i:
        return i
    return findRoot(parent, parent[i])


# A function that does union of set x and y based on the order
def union(parent, order, x, y):
    xRoot = findRoot(parent, x)
    yRoot = findRoot(parent, y)
    # Attach smaller order tree under root of high order tree
    if order[xRoot] < order[yRoot]:
        parent[xRoot] = yRoot
    elif order[xRoot] > order[yRoot]:
        parent[yRoot] = xRoot
    # If orders are same, then make any one as root and increment its order by one
    else:
        parent[yRoot] = xRoot
        order[xRoot] += 1


# function that performs Kruskals algorithm on the graph G
def kruskal(G, weight='weight'):

    if not isinstance(G, nx.Graph):
        print('Kruskal needs an undirected graph')
        print(f'Your graph is of type {type(G)}')
        print('Exiting.')
        sys.exit()

    eLen = len(G.edges())  # eLen denotes the number of edges in G
    vLen = len(G.nodes())  # vLen denotes the number of vertices in G
    mst = []  # mst contains the MST edges
    # mstFlag[i] will hold true if the edge i has been processed for MST
    mstFlag = {}
    for i in [(u, v, d[weight]) for u, v, d in G.edges(data=True) if weight in d]:
        mstFlag[i] = False

    # parent[i] will hold the vertex connected to i, in the MST
    parent = {}
    # order[i] will hold the order of appearance of the node in the MST
    order = {}
    for v in G.nodes():
        parent[v] = v
        order[v] = 0
    while len(mst) < vLen - 1:
        # pick the smallest egde from the set of edges
        curr_edge = getMin(G, mstFlag, weight)
        mstFlag[curr_edge] = True  # update the flag for the current edge
        y = findRoot(parent, curr_edge[1])
        x = findRoot(parent, curr_edge[0])
        if x != y:
            mst.append(curr_edge)
            union(parent, order, x, y)

    mst_graph = nx.Graph()
    # mst_graph.add_nodes_from(list(G.nodes()))
    # mst_graph.add_edges_from([(u,v,{'weight':d}) for (u,v,d) in mst])

    for X in mst:
        if (X[0], X[1]) in G.edges():
            mst_graph.add_node(X[0])
            mst_graph.add_node(X[1])
            mst_graph.add_edges_from([(X[0],X[1],{weight:G[X[0]][X[1]]['weight']})])
        elif (X[1], X[0]) in G.edges():
            mst_graph.add_node(X[1])
            mst_graph.add_node(X[0])
            mst_graph.add_edges_from([(X[1],X[0],{weight:G[X[1]][X[0]]['weight']})])

    # oikean puolen mst on lista, joka sisältää edget järjestyksessä
    # laitetaan se verkkoattribuutiksi visualisointia varten
    mst_graph.graph['highlight'] = mst

    # palautetaan verkko
    return mst_graph
