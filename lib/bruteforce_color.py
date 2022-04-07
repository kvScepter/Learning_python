# brute force -värityskoodi by harri

# ladataan koodikirjastoja
import networkx as nx
from itertools import permutations
import math

# apufunktio, jossa noodien järjestys fiksattu
def color_ordered(G, node_list):

    # väreille dict-rakenne joka lopuksi ulostetaan 
    # (kuten nx.greedy_color-algoritmissa)
    colors = {}

    # käydään noodit läpi annetussa järjestyksessä
    for i, node in enumerate(node_list):

        # väritetään ensimmäinen noodi ensimmäisellä värillä
        # (värit numeroita alkaen nollasta)
        # ja hypätään seuraavaan iteraatioon
        if i == 0:
          colors[node] = 0
          continue

        # nyt node ei voi enää olla ensimmäinen
        # nodea aiemmilla noodeilla on jo väri

        # otetaan talteen tähän asti väritetyt noodit
        previous_nodes = set(node_list[:i])

        # otetaan talteen myös noden naapurit
        current_neighbors = set(G.neighbors(node))

        # ja niihin käytetyt värit
        neighbors_colors = set()
        for neighbor in iter(current_neighbors):
            if neighbor in colors:
                neighbors_colors.add(colors[neighbor])

        # tsekataan löytyykö aiemmista väreistä sellaisia,
        # joilla yksikään noden naapuri ei ole väritetty
        available_colors = set()
        available_nodes = previous_nodes - current_neighbors
        for available_node in iter(available_nodes):
            if available_node in colors and colors[available_node] not in neighbors_colors:
                available_colors.add(colors[available_node])

        # jos löytyy
        if len(available_colors) > 0:

            # niin mikä vaan väri, joka ei ole jonkun naapurin väri, kelpaa
            available_color = next(iter(available_colors))
            colors[node] = available_color
   
        # muutoin
        else:
            # valitaan uusi väri
            colors[node] = len(set(colors.values()))

    # palautetaan värit
    return colors


# itse funktio
def bruteforce_color(G):

    # kaikki järjestykset talteen
    node_orders = permutations(G.nodes())

    jarjestysten_lkm = math.factorial(len(G.nodes()))

    # väritys-dict kuten apufunktiossa
    current_colors = {}

    # alustetaan väritys siten, että kukin noodi on
    # väritetty omalla värillään
    for i, node in enumerate(G.nodes()):
        current_colors[node] = i

    # ajetaan apufunktio kullekin järjestykselle
    # ja päivitetään dict-rakennetta sitä mukaa kun
    # löytyy tähänastista pienempi värien määrä
    for i, node_order in enumerate(node_orders):
        print(f'bruteforce: järjestys {i+1}/{jarjestysten_lkm}')
        colors = color_ordered(G, node_order)
        if len(set(colors.values())) < len(set(current_colors.values())):
            current_colors = colors

    # lopuksi dict-rakenteessa on pienin mahdollinen määrä värejä
    return current_colors

