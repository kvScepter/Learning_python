import numpy as np
import networkx as nx
import sys
sys.path.append("./lib")

#csv tiedostossa oleva matriisi käyttöön
numpy_matriisi = np.genfromtxt('distance.csv', delimiter=',')
G = nx.from_numpy_array(numpy_matriisi)

#Lyhin reitti ja etäisyys
#ajettava algorytmi (mikä, mistä, mihin tässä 6 --> 4 noodiin) 
reitti = nx.dijkstra_path(G, 6, 4)
reitti_pituus = nx.dijkstra_path_length(G, 6, 4)


#tulostaa tuloksen, reitin pituun kun matriisissa painoarvot
# ja reitin mikä on lyhin reitti
print(reitti_pituus)
print(reitti)
