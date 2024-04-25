# - Uniform-Cost Search**: Expands the least cost node and is used when action costs vary.

from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    
    path = {start: []}
    while queue:
        cost, node = queue.get()
        if node == goal:
            return path[node]  # Return the path taken
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_cost = cost + graph[node][neighbor]
                    queue.put((new_cost, neighbor))
                    path[neighbor] = path[node] + [neighbor]  # Update the path for the neighbor
    return False

def main():
    # Example usage:
    graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 2, 'E': 5}, 'C': {'A': 4, 'F': 3}, 'D': {'B': 2}, 'E': {'B': 5, 'F': 1}, 'F': {'C': 3, 'E': 1}}
    start_node = 'A'
    goal_node = ''
    print(uniform_cost_search(graph, start_node, goal_node))

if __name__ == '__main__':
    main()