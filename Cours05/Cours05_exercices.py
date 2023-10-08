from math import *

import networkx as nx
import matplotlib.pyplot as plt

def show_graph(dAdj, oriented=False, dispo='circ'):
    n = len(dAdj)
    positions = {i: (cos(pi/2 + 2*pi*i/n), sin(pi/2 + 2*pi*i/n))
                 for i in range(n)}
    G=nx.Graph(dAdj)
    # Tracé
    fig, ax = plt.subplots()
    plt.figure(figsize=(4, 3))
    nx.draw(G, pos=positions, with_labels=True)
    plt.axis('equal')
    plt.show()
