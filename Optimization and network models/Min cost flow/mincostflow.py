import networkx as nx

#cost. Row 1 = worker 1. Column 1 = task 1
kustannukset = [ 
        [186,152,51,184],
        [163,100,114,202],
        [60,150,160,71],
        [157,131,175,195]
]


duunarit = ['w0', 'w1', 'w2', 'w3']
duunit = ['t0', 't1', 't2', 't3']

#directed grapfh
G = nx.DiGraph()

#add nodes to task and workers
G.add_nodes_from(duunarit)
G.add_nodes_from(duunit)

for d in duunarit:
    for t in duunit:
        G.add_edge(d,t)

for d in duunarit:
    G.nodes[d]['demand'] = -1

for t in duunit:
    G.nodes[t]['demand'] = 1

for i in range(4):
    for j in range(4):
        G.edges[f'w{i}', f't{j}']['weight'] = kustannukset[i][j]

(cost, flow) = nx.network_simplex(G)
print(cost)
print(flow)
#print(G.nodes())
#print(G.edges())
