# - Depth-First Search (DFS)**: Explores as deep as possible into the search space before backtracking.

def dfs(graph, start, goal):
    visited = set()
    stack = [start]
    
    path = {start: []}
    while stack:
        node = stack.pop()
        if node == goal:
            return path[node]  # Return the path taken
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    path[neighbor] = path[node] + [neighbor]  # Update the path for the neighbor
    return False

def main():
    # Example usage:
    graph = {'A': {'B', 'C'}, 'B': {'A', 'D', 'E'}, 'C': {'A', 'F'}, 'D': {'B'}, 'E': {'B', 'F'}, 'F': {'C', 'E'}}
    start_node = 'A'
    goal_node = 'F'
    print(dfs(graph, start_node, goal_node))

if __name__ == '__main__':
    main()
