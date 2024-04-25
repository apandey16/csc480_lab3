# Breadth-First Search (BFS)**: Explores the search space level by level, expanding all children of a node before moving to the next level.

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    
    path = {start: []}
    while queue:
        node = queue.popleft()
        if node == goal:
            return path[node]  # Return the path taken
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    path[neighbor] = path[node] + [neighbor]  # Update the path for the neighbor
    return False

# Example usage:
graph = {'A': {'B', 'C'}, 'B': {'A', 'D', 'E'}, 'C': {'A', 'F'}, 'D': {'B'}, 'E': {'B', 'F'}, 'F': {'C', 'E'}}
start_node = 'A'
goal_node = 'F'
print(bfs(graph, start_node, goal_node))