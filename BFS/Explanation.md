# Breadth-First Search (BFS) Algorithm

## 1. Introduction

**Breadth-First Search (BFS)** is a fundamental graph traversal algorithm that explores all vertices at the present depth level before moving on to vertices at the next depth level.

- It uses a **Queue** (FIFO - First In First Out) data structure.
- It is the best algorithm for finding the **shortest path** in an unweighted graph.
- It explores the graph "breadth-wise" (level by level).

### Key Characteristics:
- **Time Complexity**: O(V + E) where V = number of vertices, E = number of edges
- **Space Complexity**: O(V)
- Optimal for **shortest path** in unweighted graphs
- Guarantees the shortest path in terms of number of edges

## 2. How BFS Works

BFS starts at a source vertex and explores all its neighboring vertices first, then moves to the neighbors of those neighbors, and so on.

### Step-by-Step Process:
1. Start at the source vertex
2. Mark it as visited and enqueue it
3. While the queue is not empty:
   a. Dequeue a vertex from the front of the queue
   b. Process the vertex (print it, store distance, etc.)
   c. Enqueue all its unvisited adjacent vertices
   d. Mark them as visited
