import networkx as nx


def get_data(sample=False):
    file = __file__
    if sample:
        file = file.replace('.py', '.sample')
    else:
        file = file.replace('.py', '.txt')

    data = []

    with open(file) as f:
        for line in f.readlines():
            data.append(line.rstrip())

    return data


def one(data, steps, mod, invert=False):
    G = nx.Graph()
    start = None
    plots = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '#':
                if not start and data[i][j] == 'S':
                    start = (i, j)
                # up
                if i > 0 and data[i - 1][j] != '#':
                    G.add_edge((i, j), (i - 1, j))
                # down
                if i < len(data) - 1 and data[i + 1][j] != '#':
                    G.add_edge((i, j), (i + 1, j))
                # left
                if j > 0 and data[i][j - 1] != '#':
                    G.add_edge((i, j), (i, j - 1))
                # right
                if j < len(data[0]) - 1 and data[i][j + 1] != '#':
                    G.add_edge((i, j), (i, j + 1))

    for i in range(len(data)):
        line = ''
        for j in range(len(data[0])):
            if data[i][j] != '#':
                if (i, j) in G:
                    distance = len(nx.shortest_path(G, start, (i, j))) - 1
                    if ((not invert and distance <= steps) or (invert and distance > steps)) and distance % 2 == mod:
                        plots.add((i, j))
                        line += '1'
                    else:
                        line += ' '
                else:
                    line += ' '
            else:
                line += '0'
        print(line)

    return len(plots)


def two(data, steps):
    odd_full = 7574
    even_full = 7612
    odd_edge = 3726  # one(data, steps, 1)
    even_edge = 3854  # one(data, steps, 0)

    tiles = (steps - 65) // 131
    odd_full_tiles = (tiles + 1) ** 2
    even_full_tiles = tiles ** 2
    odd_edge_tiles = tiles + 1
    even_edge_tiles = tiles

    return ((odd_full_tiles * odd_full) +
            (even_full_tiles * even_full) -
            (odd_edge_tiles * odd_edge) +
            (even_edge_tiles * even_edge))


if __name__ == '__main__':
    data = get_data(False)

    # print(one(data, 65, 0, True))
    # print(one(data, 65, 1, True))
    # print(one(data, 200, 0))
    # print(one(data, 200, 1))

    print(two(data, 26501365))
