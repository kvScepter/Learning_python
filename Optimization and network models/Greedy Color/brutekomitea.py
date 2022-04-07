import networkx as nx
import matplotlib.pyplot as plt
import sys
sys.path.append('./lib')
from cytoscape_js import create_html
from bruteforce_color import bruteforce_color

G = nx.Graph()

G.add_nodes_from([1,7])

G.add_edges_from([
    (1,3),
    (1,7),
    (2,7),
    (2,5),
    (2,6),
    (3,4),
    (3,5),
    (3,6),
    (4,5),
    (5,6),
    (5,7),
    (6,7)
])

#colors = nx.greedy_color(G, strategy='independent_set')
colors = bruteforce_color(G)
print('Algoritmin tekemä komitea jako:', colors)
print('Kokousten määrä:', len(set(colors.values())))
G.graph['colors'] = colors
polku = './komitea_kokous2.html'
create_html(G, polku)
print('Komitea in html', polku)
#nx.draw(G, with_labels=True)
#plt.show