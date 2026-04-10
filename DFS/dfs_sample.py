def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set
    
    # Mark the current node as visited and print it
    visited.add(start)
    print(start, end=" ")


    # Recur for all the vertices adjacent to this node
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


start_node = 'A'
print("DFS Traversal starting from node", start_node, ":")
dfs(graph, start_node)
