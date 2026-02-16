import matplotlib.pyplot as plt
from collections import deque

# Genealogy Tree (Parent -> Children)
family_tree = {
    "Rickard Stark": ["Eddard Stark"],
    "Eddard Stark": ["Robb Stark", "Sansa Stark", "Arya Stark", "Bran Stark", "Jon Snow"],
    "Rhaegar Targaryen": ["Jon Snow", "Daenerys Targaryen"],
    "Robb Stark": [],
    "Sansa Stark": [],
    "Arya Stark": [],
    "Bran Stark": [],
    "Jon Snow": [],
    "Daenerys Targaryen": []
}

# -------- BFS Algorithm -------- #
def bfs(tree, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()
        print(node)

        for child in tree[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)


# Run BFS from Rickard Stark
bfs(family_tree, "Rickard Stark")


# -------- Plotting the Tree -------- #

# Manually assigning positions for genealogy layout
positions = {
    "Rickard Stark": (0, 4),
    "Eddard Stark": (0, 3),
    "Robb Stark": (-3, 2),
    "Sansa Stark": (-1.5, 2),
    "Arya Stark": (0, 2),
    "Bran Stark": (1.5, 2),
    "Jon Snow": (3, 2),
    "Rhaegar Targaryen": (4, 4),
    "Daenerys Targaryen": (5, 3)
}

plt.figure()

# Draw edges
for parent in family_tree:
    for child in family_tree[parent]:
        if parent in positions and child in positions:
            x_values = [positions[parent][0], positions[child][0]]
            y_values = [positions[parent][1], positions[child][1]]
            plt.plot(x_values, y_values)

# Draw nodes
for node, (x, y) in positions.items():
    plt.scatter(x, y)
    plt.text(x, y, node, fontsize=8)

plt.gca().set_aspect('equal', adjustable='box')
plt.xticks([])
plt.yticks([])
plt.title("Game of Thrones Genealogy (BFS Tree)")
plt.show()
