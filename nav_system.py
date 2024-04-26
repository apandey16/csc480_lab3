from dfs import dfs
from bfs import bfs
from uniform import uniform_cost_search
from random import randint, random

def generate_nodes(nodes):
    nodes_list =[]
    for node in range(nodes):
        nodes_list.append(str(node))
    return nodes_list

# Constants for graph generation
NODES = generate_nodes(15)
MAX_COST = 10
START = NODES[randint(0, len(NODES)-1)]
END = START
while END == START:
    END = NODES[randint(0, len(NODES)-1)]

def generate_graph(nodes, max_cost):
    graph = {}
    for node in nodes:
        graph[node] = {}
        neighbor = nodes[randint(0, len(nodes)-1)]
        while neighbor == node:
            neighbor = nodes[randint(0, len(nodes)-1)]
        cost = randint(1, max_cost)
        graph[node][neighbor] = cost
        for neighbor in nodes:
            if neighbor != node and neighbor not in graph[node]:
                if random() < 0.5:
                    cost = randint(1, max_cost)
                    graph[node][neighbor] = cost
    return graph
def main():
    graph = generate_graph(NODES, MAX_COST)
    print("Graph: " + str(graph))
    print("Start: " + str(START))
    print("End: " + str(END))

    dfs_path = dfs(graph, START, END)
    if dfs_path:
        dfs_path = [START] + dfs_path
    else:
        dfs_path = "No path found"
    print("DFS Path: " + str(dfs_path))

    bfs_path = bfs(graph, START, END)
    if bfs_path:
        bfs_path = [START] + bfs_path
    else:
        bfs_path = "No path found"
    print("BFS Path: " + str(bfs_path))

    uniform_cost_search_path = uniform_cost_search(graph, START, END)
    if uniform_cost_search_path:
        uniform_cost_search_path = [START] + uniform_cost_search_path
    else:
        uniform_cost_search_path = "No path found"

    print("Uniform Search Path: " + str(uniform_cost_search_path))

if __name__ == '__main__':
    main()