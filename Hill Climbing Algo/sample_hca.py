import random
# Objective function
def objective_function(x):
    return -x**2 + 4*x
# Neighbor function: this will generate a neighboring solution by moving a small step.
def get_neighbors(x, step_size=0.1):
    return [x - step_size, x + step_size]
# Hill Climbing Algorithm
def hill_climbing():
    # Start with a random initial solution
    current_solution = random.uniform(-10, 10)  # Random start point between -10 and 10
    current_value = objective_function(current_solution)
    
    # Iteratively improve the solution
    while True:
        neighbors = get_neighbors(current_solution)
        # Evaluate the neighbors
        next_solution = None
        next_value = current_value
        
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            if neighbor_value > next_value:  # Select the neighbor with the higher value
                next_solution = neighbor
                next_value = neighbor_value
        
        # If no better neighbor is found, exit
        if next_value <= current_value:
            break
        
        # Move to the better neighbor
        current_solution = next_solution
        current_value = next_value
    
    return current_solution, current_value

# Run Hill Climbing algorithm
best_solution, best_value = hill_climbing()
print(f"Best solution: {best_solution}, with value: {best_value}")
