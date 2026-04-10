import matplotlib.pyplot as plt

# Original Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS function that also builds DFS tree
def dfs_tree(graph, start, visited=None, tree_edges=None):
    if visited is None:
        visited = set()
    if tree_edges is None:
        tree_edges = []

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            tree_edges.append((start, neighbor))  # store DFS tree edge
            dfs_tree(graph, neighbor, visited, tree_edges)

    return tree_edges


# Get DFS Tree edges
dfs_edges = dfs_tree(graph, 'A')

# Create DFS tree structure
tree = {}
for parent, child in dfs_edges:
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

# Ensure all nodes exist in tree dictionary
for node in graph:
    if node not in tree:
        tree[node] = []


# -------- Plotting DFS Tree -------- #

# Manually position nodes in DFS order
positions = {
    'A': (0, 4),
    'B': (-2, 3),
    'D': (-3, 2),
    'E': (-1, 2),
    'F': (1, 1),
    'C': (2, 0)
}

plt.figure()

# Draw tree edges
for parent in tree:
    for child in tree[parent]:
        x_values = [positions[parent][0], positions[child][0]]
        y_values = [positions[parent][1], positions[child][1]]
        plt.plot(x_values, y_values)

# Draw nodes
for node, (x, y) in positions.items():
    plt.scatter(x, y)
    plt.text(x, y, node)

plt.gca().set_aspect('equal', adjustable='box')
plt.xticks([])
plt.yticks([])
plt.title("DFS Spanning Tree")
plt.show()
