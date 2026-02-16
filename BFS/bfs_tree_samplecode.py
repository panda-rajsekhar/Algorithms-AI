from collections import deque
import matplotlib.pyplot as plt

# BFS function that also builds a BFS tree
def bfs_tree(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    tree_edges = []   # store BFS tree edges (parent -> child)
    levels = {start: 0}  # level of each node

    print("BFS Traversal starting from node", start, ":")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

                tree_edges.append((node, neighbor))
                levels[neighbor] = levels[node] + 1

    print()
    return tree_edges, levels


# Graph definition
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'

# Run BFS
edges, levels = bfs_tree(graph, start_node)

# ------------------ DRAW BFS TREE ------------------

# Assign x positions for nodes in each level
positions = {}
level_nodes = {}

for node, level in levels.items():
    level_nodes.setdefault(level, []).append(node)

for level, nodes in level_nodes.items():
    for i, node in enumerate(nodes):
        positions[node] = (i, -level)

# Plot
plt.figure()

# Draw edges
for parent, child in edges:
    x1, y1 = positions[parent]
    x2, y2 = positions[child]
    plt.plot([x1, x2], [y1, y2])

# Draw nodes
for node, (x, y) in positions.items():
    plt.scatter(x, y)
    plt.text(x, y + 0.05, node, ha='center')

plt.title("BFS Tree using Matplotlib")
plt.axis("off")
plt.show()

