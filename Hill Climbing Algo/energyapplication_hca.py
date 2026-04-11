import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# =============================================================================
# ENERGY APPLICATION: Minimum Energy Configuration in 2D Potential Field
# Using Steepest-Ascent Hill Climbing (adapted for minimization)
#
# Real-world analogy:
#   - Finding the lowest energy state of a particle/molecule in a rough energy landscape
#   - Common in physics, chemistry, and materials science (e.g., molecular conformation,
#     protein folding approximation, crystal structure optimization)
# =============================================================================

def energy(X, Y):
    """Ackley function - classic multimodal energy landscape (to be MINIMIZED)"""
    a = 20
    b = 0.2
    c = 2 * np.pi
    term1 = -a * np.exp(-b * np.sqrt(0.5 * (X**2 + Y**2)))
    term2 = -np.exp(0.5 * (np.cos(c * X) + np.cos(c * Y)))
    return term1 + term2 + a + np.e


# ─── Hill Climbing for MINIMIZATION ────────────────────────────────────────
def hill_climb_energy(start, step_size=0.18, max_iter=200, tol=1e-6):
    current = np.array(start, dtype=float)
    path = [current.copy()]
    energies = [energy(*current)]

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

        neighbor_energies = [energy(*n) for n in neighbors]
        best_idx = np.argmin(neighbor_energies)          # ← MIN instead of MAX
        best_energy = neighbor_energies[best_idx]

        # No improvement? Stop (local minimum reached)
        if best_energy >= energies[-1] - tol:
            break

        current = neighbors[best_idx]
        path.append(current.copy())
        energies.append(best_energy)

    return np.array(path), np.array(energies)


# ─── Visualization ────────────────────────────────────────────────────────
def visualize_energy_optimization():
    # Grid for energy surface
    x = np.linspace(-5, 5, 140)
    y = np.linspace(-5, 5, 140)
    X, Y = np.meshgrid(x, y)
    Z = energy(X, Y)

    # Fixed starting point (same as previous examples)
    np.random.seed(42)
    start = np.random.uniform(-4, 4, 2)

    print("=== ENERGY OPTIMIZATION RESULTS ===")
    print(f"Start position      : {start}")
    print(f"Initial energy      : {energy(*start):.6f}")
    
    path, energies = hill_climb_energy(start)

    print(f"Final position      : {path[-1]}")
    print(f"Minimum energy found: {energies[-1]:.6f}  (steps: {len(path)-1})")
    print(f"Global optimum is 0 at (0,0) → Hill climbing often gets stuck in local minima!")

    # ── Plotting ─────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(12, 5))

    # 3D Energy Surface + path
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.plot_surface(X, Y, Z, cmap='plasma', alpha=0.75, rcount=80, ccount=80, linewidth=0)

    # Path (red line going downhill)
    ax1.plot(path[:,0], path[:,1], energies, 'r.-', lw=1.8, ms=4, zorder=10)

    # Start & End markers
    ax1.scatter(start[0], start[1], energy(*start),
                color='lime', s=100, edgecolor='black', linewidth=1.5, label='Start')
    ax1.scatter(path[-1,0], path[-1,1], energies[-1],
                color='red', marker='*', s=180, edgecolor='black', linewidth=1.5, label='Minimum')

    ax1.set_title("3D Energy Landscape – Hill Climbing Path\n(Lower = Better)")
    ax1.set_xlabel('x'); ax1.set_ylabel('y'); ax1.set_zlabel('Energy E(x,y)')
    ax1.legend()

    # Contour plot
    ax2 = fig.add_subplot(122)
    cont = ax2.contourf(X, Y, Z, levels=60, cmap='plasma')
    ax2.plot(path[:,0], path[:,1], 'r.-', lw=1.6, ms=5)
    ax2.scatter(start[0], start[1], color='lime', s=120, edgecolor='k', label='Start')
    ax2.scatter(path[-1,0], path[-1,1], color='red', marker='*', s=200, edgecolor='k', label='Minimum')

    ax2.set_title("Contour View – Path to Local Minimum")
    ax2.set_xlabel('x'); ax2.set_ylabel('y')
    ax2.legend()
    plt.colorbar(cont, ax=ax2, fraction=0.046, pad=0.04)

    plt.suptitle("Energy Application: Minimum Energy Configuration using Hill Climbing\n"
                 "(Ackley Energy Landscape – Classic multimodal test)", fontsize=14, y=0.98)
    plt.tight_layout()
    plt.show()


# =============================================================================
if __name__ == "__main__":
    visualize_energy_optimization()
