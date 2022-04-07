import numpy as np
import networkx as nx
from pathlib import Path
import sys
sys.path.append("./Lib")
from cytoscape1_js import create_html

#millä nimellä tekee luettavan html tiedoston
html_ulostus = Path('./spanning_tree.html')

#csv tiedostossa oleva matriisi ulos, sisältää kaupunkien etäisyydet.
numpy_matriisi = np.genfromtxt('city.csv', delimiter=',')
G = nx.from_numpy_array(numpy_matriisi)

#itse algoritmi mikä ajetaan matriisille. Oletus Kruskal.. muuta lisäämällä esim: , algorithm='prim'
#mikä on lyhin reitti kaupunkien välillä kaapelille
min = nx.minimum_spanning_tree(G, weight="weight")

#print(min)
#print(min.edges(data=True))

#ajetaan for looppi jotta saadaan kaaapelin pituus
pituus = 0
for edge in min.edges(data=True):
    pituus += edge[2]["weight"]

# alla verkko ennen miminum spannig tree algoa
#create_html(G, html_ulostus)

#piirtää miminum spanning tree algoritmin.
create_html(min, html_ulostus)
print("tehty html tiedosto")
print("Kaupunkien välille tarvittava kaapeli määrä on:", pituus, " Km")
