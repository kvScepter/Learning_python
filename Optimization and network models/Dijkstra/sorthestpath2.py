import numpy as np
import networkx as nx


numpy_matriisi = np.genfromtxt('AA5360_kaupungit.csv', delimiter=',')
G = nx.from_numpy_array(numpy_matriisi)
#valitaan mistä noodista mihin noodiin reitti ja etäisyys
reitti = nx.dijkstra_path(G, 6, 4)
reitti_pituus = nx.dijkstra_path_length(G, 6, 4)


print(reitti_pituus)
print(reitti)
