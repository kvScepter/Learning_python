
##### imports #####

import networkx as nx
import numpy as np

import sys
sys.path.append('../lib')

# omat kirjastot
# itse kruskal-algoritmi (oma)
# löytyy kruskal_lib.py -kirjastosta
from kruskal_lib import kruskal
from randomgraph import randomgraph
from cytoscape1_js import create_html


##### config #####

# muuta tämä
output_file = './kruskal.html'

# huom. kruskal vaatii aina suuntaamattoman ja painotetun verkon
#G = randomgraph(8, 0.4, directed=False, edgerange=(2,42))

G = nx.read_graphml('AA5360_verkko.graphml', node_type=int, edge_key_type=int)



# kruskal-funktiomme palauttaa minimaalisen virittäjäpuun
# (Graph) mutta sitä ei käytetä tässä ...
# käytetään ainoastaan kruskal-algoritmin läpikäymien linkkien järjestystä
# joka löytyy algoritmin palauttaman verkon highlight-attribuutista
G.graph['highlight'] = kruskal(G).graph['highlight']
print(G.graph['highlight'])

# luodaan html-tiedosto
# (animointi default-nopeuksilla, ks. bfs ja dfs)
create_html(G, f'{output_file}', animate=True)

# kerrotaan siitä
print(f'wrote {output_file}')

print("kruskal output:!", list(kruskal(G)))
