from collections import deque
import matplotlib.pyplot as plt

# Graph definition
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    traversal_order = []   # to store BFS order

    print("BFS Traversal starting from node", start, ":")

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        traversal_order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print()  # new line
    return traversal_order

# Start node
start_node = 0

# Run BFS
order = bfs(graph, start_node)

# ------------------ Matplotlib Plot ------------------
plt.plot(range(len(order)), order, marker='o')
plt.xlabel("Step Number")
plt.ylabel("Node Visited")
plt.title("BFS Traversal Order")
plt.grid(True)
plt.show()
