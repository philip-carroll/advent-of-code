import ast
from collections import defaultdict
from aoc2022.utils.search_utils import bfs_shortest_path


def prepare(p=True, t=True):
    graph = defaultdict(dict)

    with open('valves.txt') as f:
        for line in f.readlines():
            line = line.rstrip()

            valve, tunnels = line.split(';')
            node, pressure = valve.replace('Valve ', '').split(' has flow rate=')
            tunnels = [t.strip() for t in
                       tunnels.replace(' tunnels lead to valves ', '').
                       replace(' tunnel leads to valve ', '').
                       split(',')]
            if p and not t:
                graph[node] = ast.literal_eval(pressure)
            elif not p and t:
                graph[node] = tunnels
            else:
                graph[node]['p'] = ast.literal_eval(pressure)
                graph[node]['t'] = tunnels

    return graph


# https://www.geeksforgeeks.org/maximum-sum-of-values-of-nodes-among-all-connected-components-of-an-undirected-graph/
# Function to implement DFS
def dfs(graph, visited, node):
    global sum
    global minute

    minute += 1

    if minute < 30:
        # Marking the visited vertex as true
        visited.add(node)

        # Updating the value of connection
        sum += graph[node]['p'] * minute
        print('%s Open valve %s, releasing %s pressure' % (minute, node, graph[node]['p']))

        # Traverse for all adjacent nodes
        for neighbour in graph[node]['t']:
            if neighbour not in visited:
                # Recursive call to the DFS algorithm
                dfs(graph, visited, neighbour)
            else:
                print('Back')


def dfs_max_sum(graph):
    global sum
    global minute

    minute = 0
    # to mark visited vertices
    visited = set()

    # stores maximum node sum
    max_sum = float('-inf')

    # loop invokes DFS algorithm
    for node in graph.keys():
        if node not in visited:

            # hold temporary values
            sum = 0

            # DFS algorithm
            dfs(graph, visited, node)

            # Conditional to update max value
            if sum > max_sum:
                max_sum = sum

            sum = 0

    return max_sum


if __name__ == '__main__':
    # print(dfs_max_sum(g))

    g = prepare(p=False)
    d = defaultdict(dict)
    p = prepare(t=False)

    for i in g.keys():
        for j in g.keys():
            if i != j:
                d[i][j] = len(bfs_shortest_path(g, i, j)) - 1

    print(g)
    print(d)
    print(p)

    minute = 0
    pressure = 0
    visited = ['AA']
    n = 'AA'
    duration = 30

    while minute < duration:
        maxval = 0
        move = None
        for node in d[n]:
            if node not in visited:
                val = (duration - minute - (d[n][node] + 1)) * p[node]
                if val > maxval:
                    maxval = val
                    move = node
        if move:
            visited.append(move)
            pressure += p[move]
            minute += d[n][move] + 1
            n = move
        else:
            minute += 1

        print('%s: %s %s' % (minute, move, pressure))
