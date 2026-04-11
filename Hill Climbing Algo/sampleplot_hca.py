import random
import numpy as np
import matplotlib.pyplot as plt

# Objective function
def objective_function(x, y):
    return -(x**2 + 3*y**2 ) 

# Neighbor function
def get_neighbors(x, y, step=0.1):
    return [
        (x+step, y), (x-step, y),
        (x, y+step), (x, y-step)
    ]

# Hill Climbing
def hill_climbing():
    x = random.uniform(-3,3)
    y = random.uniform(-3,3)

    current_value = objective_function(x,y)

    while True:
        neighbors = get_neighbors(x,y)
        next_x, next_y = x, y
        next_value = current_value

        for nx, ny in neighbors:
            value = objective_function(nx,ny)

            if value > next_value:
                next_x, next_y = nx, ny
                next_value = value

        if next_value <= current_value:
            break

        x, y = next_x, next_y
        current_value = next_value

    return x, y, current_value


# Run algorithm
best_x, best_y, best_value = hill_climbing()

print("Best solution:", best_x, best_y)
print("Best value:", best_value)


# Create surface grid
x = np.linspace(-3,3,100)
y = np.linspace(-3,3,100)
X, Y = np.meshgrid(x,y)
Z = objective_function(X,Y)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X,Y,Z,alpha=0.7)

# Plot solution point
ax.scatter(best_x, best_y, best_value,
           color='red', s=100, label="Best Solution")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("f(x,y)")
ax.legend()

plt.show()
