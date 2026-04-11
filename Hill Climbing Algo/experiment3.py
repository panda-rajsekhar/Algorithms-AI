import random
import matplotlib.pyplot as plt
import numpy as np

# Objective function (height of hill)
def hill_function(x):
    return -x**2 + 5*x + 10

# Hill Climbing Algorithm (store path)
def hill_climb(start, step_size=0.5, max_iterations=100):
    current = start
    path = [current]

    print(f"Start at x = {current:.2f}, height = {hill_function(current):.2f}")

    for i in range(max_iterations):
        neighbors = [current - step_size, current + step_size]

        next_point = current
        for n in neighbors:
            if hill_function(n) > hill_function(next_point):
                next_point = n

        if next_point == current:
            print("\nReached peak!")
            break

        current = next_point
        path.append(current)

        print(f"Step {i+1}: x = {current:.2f}, height = {hill_function(current):.2f}")

    return path

# Run algorithm
start_position = random.uniform(-10, 10)
path = hill_climb(start_position)

# Plotting
x_vals = np.linspace(-10, 10, 400)
y_vals = hill_function(x_vals)

plt.figure()
plt.plot(x_vals, y_vals, label="Hill Function")

# Plot path taken
path_y = [hill_function(x) for x in path]
plt.scatter(path, path_y)
plt.plot(path, path_y, linestyle='--', label="Path Taken")

plt.title("Hill Climbing Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

plt.show()
