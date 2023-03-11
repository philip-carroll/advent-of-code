import networkx as nx

if __name__ == '__main__':
    G = nx.Graph([(0, 1), (0, 2), (1, 2)])
    # nx.find_cycle(G, orientation="original")

    print(nx.find_cycle(G, orientation="ignore"))
