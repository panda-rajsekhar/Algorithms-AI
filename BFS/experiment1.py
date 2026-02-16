from collections import deque
import matplotlib.pyplot as plt

# ------------------ BFS FUNCTION ------------------
def bfs_tree(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    tree_edges = []          # BFS tree edges (parent -> child)
    levels = {start: 0}      # Level (depth) of each node

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


# ------------------ GRAPH DEFINITION ------------------
graph = {
    'Dashratha': ['Kaushalya', 'Kaikai', 'Sumitra'],
    'Kaushalya': ['Dashratha', 'Rama'],
    'Kaikai': ['Dashratha', 'Lakshmana', 'Shatrughana'],
    'Sumitra': ['Dashratha', 'Bharat'],

    # Leaf nodes (must be present to avoid KeyError)
    'Rama': [],
    'Lakshmana': [],
    'Shatrughana': [],
    'Bharat': []
}

start_node = 'Dashratha'

# ------------------ RUN BFS ------------------
edges, levels = bfs_tree(graph, start_node)

# ------------------ DRAW BFS TREE ------------------

# Assign positions based on level
positions = {}
level_nodes = {}

for node, level in levels.items():
    level_nodes.setdefault(level, []).append(node)

for level, nodes in level_nodes.items():
    for i, node in enumerate(nodes):
        positions[node] = (i, -level)

# Plot setup
plt.figure(figsize=(10, 6))

# Draw edges
for parent, child in edges:
    x1, y1 = positions[parent]
    x2, y2 = positions[child]
    plt.plot([x1, x2], [y1, y2], linewidth=1)

# Draw nodes
for node, (x, y) in positions.items():
    plt.scatter(x, y, s=500)
    plt.text(x, y + 0.08, node, ha='center', fontsize=9)

plt.title("BFS Tree Representation")
plt.axis("off")
plt.show()
