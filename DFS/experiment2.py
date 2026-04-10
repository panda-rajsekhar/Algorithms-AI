from collections import defaultdict
import matplotlib.pyplot as plt

# ------------------ DFS FUNCTION ------------------
def dfs_tree(graph, start, visited=None, tree_edges=None, levels=None, level=0):
    if visited is None:
        visited = set()
        tree_edges = []
        levels = {}

    visited.add(start)
    levels[start] = level

    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            tree_edges.append((start, neighbor))
            dfs_tree(graph, neighbor, visited, tree_edges, levels, level + 1)

    return tree_edges, levels


# ------------------ GRAPH (Library Maze) ------------------
graph = {
    'Entrance': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['F'],
    'E': [],
    'F': ['RareBook'],
    'RareBook': []
}

start_node = 'Entrance'

# ------------------ RUN DFS ------------------
print("DFS Traversal starting from node", start_node, ":")
edges, levels = dfs_tree(graph, start_node)
print()


# ------------------ DRAW DFS TREE ------------------

positions = {}
level_nodes = {}

# Group nodes by level
for node, level in levels.items():
    level_nodes.setdefault(level, []).append(node)

# Assign positions
for level, nodes in level_nodes.items():
    for i, node in enumerate(nodes):
        positions[node] = (i * 2, -level * 2)

plt.figure(figsize=(10, 6))

# Draw edges
for parent, child in edges:
    x1, y1 = positions[parent]
    x2, y2 = positions[child]
    plt.arrow(x1, y1, x2 - x1, y2 - y1,
              length_includes_head=True,
              head_width=0.1)

# Draw nodes
for node, (x, y) in positions.items():
    plt.scatter(x, y, s=500)
    plt.text(x, y + 0.2, node, ha='center', fontsize=9)

plt.title("DFS Tree Representation (Library Search)")
plt.axis("off")

# ------------------ SAVE IMAGE ------------------
plt.savefig("dfs_output.png")
plt.show()
