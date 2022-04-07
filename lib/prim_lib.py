
##### imports #####
import networkx as nx

# pip3 install --user pqdict
from pqdict import PQDict

def prim(G,start,weight='weight'):
    """Function recives a graph and a starting node, and returns a MST"""
    stopN = G.number_of_nodes() - 1
    current = start
    closedSet = set()
    pq = PQDict()
    mst = []

    while len(mst) < stopN:
        for node in G.neighbors(current):
            if node not in closedSet and current not in closedSet:
                if (current,node) not in pq and (node,current) not in pq:
                    w = G.edges[current,node][weight]
                    pq.additem((current,node), w)

        closedSet.add(current)

        tup, wght = pq.popitem()
        while(tup[1] in closedSet):
            tup, wght = pq.popitem()
        mst.append(tup)
        current = tup[1]

    mst_graph = nx.Graph()
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
