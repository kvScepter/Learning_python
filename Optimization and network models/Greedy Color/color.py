
# color.py:
# - luodaan verkko
# - väritetään verkko
# - piirretään lopputulos html-tiedostoon

##### imports #####

import sys
sys.path.append('./lib')

# perus-import
import networkx as nx

# omat importit
from bruteforce_color import bruteforce_color
from randomgraph import randomgraph
from cytoscape_js import create_html


##### main #####

# luodaan satunnaisverkko
# suuntaamaton ja painottamaton oltava värityshommissa
G = randomgraph(8, 0.4, False)

# väritetään verkko
# ks. nx-dokumentaatio
# voi kokeilla muitakin strategioita kuin largest_first
colors = nx.greedy_color(G, strategy='largest_first')

# mutta optimaalisen värityksen saa varmasti vain bruteforcella
# (kestää helposti eliniän ja yli)
# colors = bruteforce_color(G)

# ulostetaan värit tekstimuodossa
print('algoritmin antama väritys:', colors)
print('värien lukumäärä:', len(set(colors.values())))

# asetetaan väritys verkon attribuutiksi
G.graph['colors'] = colors

# luodaan html-tiedosto ja kerrotaan siitä
html_path = './tmp.html'
create_html(G, html_path)
print('wrote', html_path)
