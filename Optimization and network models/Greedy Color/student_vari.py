import networkx as nx
import sys
sys.path.append('./lib')
from cytoscape_js import create_html
from bruteforce_color import bruteforce_color

G = nx.read_graphml("AA5360.graphml", node_type=int, edge_key_type=int)

colors = nx.greedy_color(G, strategy='saturation_largest_first')
#colors = bruteforce_color(G)

print('algoritmin antama väritys:', colors)
print('värien lukumäärä:', len(set(colors.values())))

G.graph['colors'] = colors

polku = './suurin_kylläisyys_ensin.html'
create_html(G, polku)
print('wrote', polku)
