import matplotlib.pyplot as plt
import math

# DFS function (same as yours)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Graph definition
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# -------- Plotting the Graph -------- #

# Arrange nodes in a circular layout
nodes = list(graph.keys())
n = len(nodes)
angle_step = 2 * math.pi / n

positions = {}
for i, node in enumerate(nodes):
    angle = i * angle_step
    x = math.cos(angle)
    y = math.sin(angle)
    positions[node] = (x, y)

plt.figure()

# Draw edges (avoid duplicates)
drawn_edges = set()
for node in graph:
    for neighbor in graph[node]:
        edge = tuple(sorted([node, neighbor]))
        if edge not in drawn_edges:
            x_values = [positions[node][0], positions[neighbor][0]]
            y_values = [positions[node][1], positions[neighbor][1]]
            plt.plot(x_values, y_values)
            drawn_edges.add(edge)

# Draw nodes
for node, (x, y) in positions.items():
    plt.scatter(x, y)
    plt.text(x, y, node)

plt.gca().set_aspect('equal', adjustable='box')
plt.xticks([])
plt.yticks([])
plt.title("Graph Visualization")
plt.show()

# -------- Run DFS -------- #
print("DFS Traversal starting from node A:")
dfs(graph, 'A')
