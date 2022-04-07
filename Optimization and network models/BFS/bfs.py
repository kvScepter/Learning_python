
#### HUOM! ###

# älkää suotta ihmetelkö paikoin puuttuvaa dokumentaatiota
# se on ihan samaa kuin peruspiirto-koodissa
# siksi puuttuu
# terveisin harri


##### imports #####

import networkx as nx
import numpy as np

import sys
sys.path.append('/home/varpha/ovm/public/vko2/lib')

from randomgraph import randomgraph
from cytoscape_js import create_html


##### config #####

# muuta tämä
output_file = './bfs.html'


##### main #####

# yhtenäinen satunnaisverkko
#G = randomgraph(nodes=8, link_probability=0.4, directed=False)
G = nx.read_graphml('AA5360_verkko.graphml', node_type=int, edge_key_type=int)
#G = nx.Graph()
#G.add_edges_from([(0, 1), (0, 3), (0, 4), (0, 11), (0, 15), (0, 18), (1, 5), (1, 7), (1, 8), (1, 12), 
#(1, 19), (3, 2), (3, 6), (3, 13), (3, 16), (4, 10), (4, 14), (11, 9), (5, 17)])

# mistä noodista aloitetaan bfs
bfs_start_node = 0
print(list(nx.bfs_edges(G, bfs_start_node)))


# käytetään networkx:n bfs-funktiota
# bfs_edges palauttaa edget läpikäyntijärjestyksessä
G.graph['highlight'] = list(nx.bfs_edges(G, bfs_start_node))

# ulostetaan html
# offset = kauanko odotetaan (ms) ennen animointia
# frequency = animaatioaskeleiden välinen aika (ms)
create_html(G, output_file, animate=True, offset=10000, frequency=5000)

# kerrotaan siitä
print(f'wrote {output_file}')
