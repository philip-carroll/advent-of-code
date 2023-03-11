from collections import defaultdict
from aoc2022.utils.search_utils import bfs_shortest_path

elevation = {
    'S': 1,
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'E': 26
}

starts = []


def prepare_grid():
    grid = None

    with open('hill.txt') as f:
        for line in f.readlines():
            line = line.rstrip()

            # should only run once
            if not grid:
                grid = [[] for _ in range(len(line))]

            for col in range(len(line)):
                grid[col].append(line[col])

    return grid


def prepare_tree(grid):
    tree = defaultdict(list)
    x, y = len(grid), len(grid[0])

    for i in range(x):
        for j in range(y):
            # if grid[i][j] == 'S':
            #     start = (i, j)
            if grid[i][j] in ('S', 'a'):
                starts.append((i, j))
            if grid[i][j] == 'E':
                end = (i, j)

            node = elevation[grid[i][j]]
            if i > 0:
                left = elevation[grid[i - 1][j]]
                if left - node < 2:
                    tree[(i, j)].append((i - 1, j))  # left
            if i < x - 1:
                right = elevation[grid[i + 1][j]]
                if right - node < 2:
                    tree[(i, j)].append((i + 1, j))  # right
            if j > 0:
                up = elevation[grid[i][j - 1]]
                if up - node < 2:
                    tree[(i, j)].append((i, j - 1))  # up
            if j < y - 1:
                down = elevation[grid[i][j + 1]]
                if down - node < 2:
                    tree[(i, j)].append((i, j + 1))  # down

    # return tree, start, end
    return tree, end


if __name__ == '__main__':
    graph, end = prepare_tree(prepare_grid())
    for start in starts:
        route = bfs_shortest_path(graph, start, end)
        print(len(route) - 1)
    # xs = [x[0] for x in route]
    # ys = [x[1] for x in route]
    # plt.plot(xs, ys)
    # plt.grid()
    # plt.show()
