
##### imports #####

import networkx as nx
import numpy as np

import sys
sys.path.append('./lib')

from randomgraph import randomgraph
from cytoscape1_js import create_html


##### config #####

# muuta tämä
output_file = './dfs.html'


##### main #####

# yhtenäinen satunnaisverkko
#G = randomgraph(nodes=8, link_probability=0.4, directed=False)
G = nx.read_graphml('AA5360_verkko.graphml', node_type=int, edge_key_type=int)

# mistä noodista aloitetaan dfs
dfs_start_node = 0
print(list(nx.dfs_edges(G, dfs_start_node)))


# käytetään networkx:n dfs-funktiota
# dfs_edges palauttaa edget läpikäyntijärjestyksessä
G.graph['highlight'] = list(nx.dfs_edges(G, dfs_start_node))

# ulostetaan html
# offset = kauanko odotetaan (ms) ennen animointia
# frequency = animaatioaskeleiden välinen aika (ms)
create_html(G, output_file, animate=True, offset=10000, frequency=5000)

# kerrotaan siitä
print(f'wrote {output_file}')
