import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.animation as animation   # ← not used yet → can be commented out

# Objective (maximization)
def objective(X, Y):
    return (X**2 + Y**2)/20 + 8*np.sin(X) + 6*np.sin(1.4*Y + 0.8) - 12

# Hill climbing (steepest ascent in 8 directions)
def hill_climb(start, step_size=0.15, max_iter=120, tol=1e-5):
    current = np.array(start, dtype=float)
    path = [current.copy()]
    scores = [objective(*current)]

    for _ in range(max_iter):
        neighbors = []
        for dx in [-step_size, 0, step_size]:
            for dy in [-step_size, 0, step_size]:
                if dx == 0 and dy == 0:
                    continue
                candidate = current + np.array([dx, dy])
                neighbors.append(candidate)

        if not neighbors:
            break

        neighbor_scores = [objective(*n) for n in neighbors]
        best_idx = np.argmax(neighbor_scores)
        best_score = neighbor_scores[best_idx]

        if best_score <= scores[-1] + tol:
            break

        current = neighbors[best_idx]
        path.append(current.copy())
        scores.append(best_score)

    return np.array(path), np.array(scores)


def visualize_hill_climbing():
    x = np.linspace(-5, 5, 130)
    y = np.linspace(-5, 5, 130)
    X, Y = np.meshgrid(x, y)
    Z = objective(X, Y)

    # Fixed seed → same start point every time (good for debugging)
    np.random.seed(42)
    start = np.random.uniform(-4, 4, 2)
    print(f"Start position: {start}")
    print(f"Initial value:  {objective(*start):.4f}")

    path, scores = hill_climb(start, step_size=0.18)   # slightly larger step often looks nicer

    print(f"Final position: {path[-1]}")
    print(f"Final value:     {scores[-1]:.4f}  (steps: {len(path)-1})")

    # ─────────────── Plotting ────────────────────────────────
    fig = plt.figure(figsize=(12, 5))

    # 3D surface + path
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, rcount=80, ccount=80)
    
    # The two lines you asked about – now explicit & safe
    z_start = objective(*start)
    ax1.scatter(start[0], start[1], z_start,   color='lime', s=100, edgecolor='black', linewidth=1.5, label='start')
    ax1.scatter(path[-1, 0], path[-1, 1], scores[-1], color='red', marker='*', s=180, edgecolor='black', linewidth=1.5, label='end')

    ax1.plot(path[:,0], path[:,1], scores, 'r.-', linewidth=1.6, markersize=4, zorder=10)

    ax1.set_title("3D view – Hill Climbing path")
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('f(x,y)')
    ax1.legend()

    # Contour
    ax2 = fig.add_subplot(122)
    cont = ax2.contourf(X, Y, Z, levels=50, cmap='viridis')
    ax2.plot(path[:,0], path[:,1], 'r.-', lw=1.5, ms=5)
    ax2.scatter(start[0], start[1], color='lime', s=120, edgecolor='k', label='start')
    ax2.scatter(path[-1,0], path[-1,1], color='red', marker='*', s=200, edgecolor='k', label='end')

    ax2.set_title("Contour view + path")
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.legend()
    plt.colorbar(cont, ax=ax2, fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.show()           # This MUST be called to display the figure


if __name__ == "__main__":
    visualize_hill_climbing()
