from queue import PriorityQueue


def dijkstra(graph, start):
    visited = []

    D = {v: float('-inf') for v in graph.keys()}
    D[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in graph[current_vertex]:
            if graph[current_vertex][neighbor] != -1:
                distance = graph[current_vertex][neighbor]
                if neighbor not in visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost > old_cost:  # looking for max
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost

    return D


def dfs(graph, visited, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, visited, neighbor)


def bfs(graph, node):
    visited = [node]
    queue = [node]

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


def bfs_shortest_path(graph, start, end):
    path_list = [[start]]
    path_index = 0  # path that we’re currently following
    visited = {start}  # to keep track of previously visited nodes

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if end in next_nodes:
            current_path.append(end)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if next_node not in visited:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                visited.add(next_node)
        # Continue to next path in list
        path_index += 1

    # No path is found
    return []
