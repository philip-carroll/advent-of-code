from queue import Queue, PriorityQueue

opposite = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L',
}


def dijkstra_pure(graph, start):
    visited = []
    D = {v: float('inf') for v in graph.keys()}
    D[start] = 0

    pq = Queue()
    pq.put(start)

    while not pq.empty():
        current = pq.get()
        visited.append(current)

        for neighbor in graph[current]:
            distance = graph[current][neighbor]
            if neighbor not in visited:
                old_cost = D[neighbor]
                new_cost = D[current] + distance

                # looking for shortest path
                if new_cost < old_cost:
                    pq.put(neighbor)
                    D[neighbor] = new_cost

    return D


def dijkstra(graph, start, max_steps, min_steps=None):
    visited = []

    D = {(start, '', 0): 0}

    pq = Queue()
    pq.put((start, '', 0))

    while not pq.empty():
        current = pq.get()
        visited.append(current)
        # print(current)

        curr_node = current[0]
        curr_dir = current[1]
        curr_steps = current[2]

        for neighbor in graph[curr_node]:
            steps = curr_steps
            direction, distance = graph[curr_node][neighbor]
            if direction == curr_dir:
                steps += 1
            else:  # direction change
                if curr_dir == '' or steps >= min_steps:
                    steps = 1
                else:
                    continue
            neighbor = (neighbor, direction, steps)
            # if neighbor not in visited:
            if steps <= max_steps and curr_dir != opposite[direction]:
                # if curr_dir == '' or curr_dir == direction or (curr_dir != direction and steps > min_steps):
                if neighbor in D:
                    old_cost = D[neighbor]
                else:
                    old_cost = float('inf')

                if current in D:
                    new_cost = D[current] + distance
                else:
                    new_cost = distance

                # looking for shortest path
                if new_cost < old_cost:
                    pq.put(neighbor)
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
