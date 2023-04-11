import networkx as nx
import matplotlib.pyplot as plt

def drawGraph(graph, path, adj):
    # Inisialisasi graf
    G = nx.Graph()

    # Tambahkan simpul
    G.add_nodes_from(range(len(graph)))

    # Tambahkan edge
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if adj[i][j] != 0:
                G.add_edge(i, j)

    # Gambar graf dengan jalur terpendek
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    plt.show()
