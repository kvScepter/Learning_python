import networkx as nx 
import numpy as np
from pathlib import Path
import sys
sys.path.append("./Lib")
from randomgraph import randomgraph
from cytoscape1_js import create_html

output_filepath = Path('./testi.html')
-------
#8 noodin verkko, linkin todennäköisyys 0.4
#Suunnattu True
#edgerange miltä väliltä luvut arvotaan linkkeihin
#G = randomgraph(8, 0.4, True, edgerange=(7,24))
-------
G = nx.read_graphml("peruspiirto.graphml", node_type=int, edge_key_type=int)
create_html(G, output_filepath)
print(f"wrote {output_filepath.absolute()}")
