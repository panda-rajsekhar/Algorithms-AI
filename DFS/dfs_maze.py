import random
import time

# 0 = wall, 1 = path
def create_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]
    
    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and maze[y][x] == 0
    
    def get_neighbors(x, y):
        dirs = [(0, -2), (2, 0), (0, 2), (-2, 0)]  # up, right, down, left
        random.shuffle(dirs)
        neighbors = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                neighbors.append((nx, ny, dx//2, dy//2))  # also save wall position
        return neighbors
    
    def carve(x, y):
        maze[y][x] = 1  # mark as visited / path
        
        for nx, ny, wall_x, wall_y in get_neighbors(x, y):
            if maze[ny][nx] == 0:  # not visited
                # remove wall
                maze[y + wall_y][x + wall_x] = 1
                # recurse
                carve(nx, ny)
    
    # Start from top-left (can be random)
    start_x, start_y = 1, 1
    carve(start_x, start_y)
    
    # Make entrance and exit (optional)
    maze[0][1] = 1          # entrance
    maze[height-1][width-2] = 1  # exit
    
    return maze


def print_maze(maze):
    for row in maze:
        line = ""
        for cell in row:
            if cell == 1:
                line += "  "   # path
            else:
                line += "██"   # wall
        print(line)


# Example usage
if __name__ == "__main__":
    WIDTH =101   # must be odd number
    HEIGHT =101  # must be odd number
    
    maze = create_maze(WIDTH, HEIGHT)
    print_maze(maze)
