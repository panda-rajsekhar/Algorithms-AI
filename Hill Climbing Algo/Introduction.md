# Introduction to Hill Climbing Algorithm

🧗‍♂️ **Hill Climbing Algorithm**

### 📌 Overview
The Hill Climbing Algorithm is a heuristic search algorithm used in Artificial Intelligence for solving optimization problems. It works by iteratively improving a solution until no better neighboring solution is found.

> 👉 **Think of it like climbing a hill:**

> You start at a random point  
> Move in the direction of increasing height (better solution)  
> Stop when you reach the top (optimum)

---

## ⚙️ Key Idea

At each step:
1. Evaluate neighboring states
2. Move to the neighbor with the best value
3. Repeat until no improvement is possible

## 🧠 Algorithm Steps

1. Initialize the current state
2. **Loop:**
   - a. Generate neighbors of current state
   - b. Evaluate each neighbor
   - c. Select the best neighbor
   - d. If best neighbor is better than current:
     - Move to best neighbor
   - Else:
     - Stop (local optimum reached)
3. Return current state as solution

---

### 📊 Types of Hill Climbing

1. **Simple Hill Climbing**  
   - Picks the first better neighbor  
   - Fast but may miss better solutions

2. **Steepest Ascent Hill Climbing**  
   - Evaluates all neighbors  
   - Chooses the best among them  
   - More accurate but slower

3. **Stochastic Hill Climbing**  
   - Chooses a random better neighbor  
   - Adds randomness → helps avoid some traps

---

### 🔍 Example

Suppose we want to maximize the function:

$$ f(x) = -x^2 + 4x $$

- Start at \( x = 0 \)
- Move toward increasing values of \( f(x) \)
- Eventually reach the maximum at \( x = 2 \)

---

## ⚠️ Problems with Hill Climbing

1. **Local Maximum**  
   Algorithm may stop at a peak that is **not** the global maximum.

2. **Plateau**  
   Flat region where no improvement is detected.

3. **Ridge Problem**  
   Narrow ridge where it's hard to find the correct direction.

---

## 🛠️ Solutions to Limitations

- **Random Restart**  
  Run the algorithm multiple times from different starting points.

- **Simulated Annealing**  
  Allows occasional downhill moves to escape local maxima.

- **Beam Search**  
  Keeps multiple states instead of just one.

---

## 📈 Advantages

- ✅ Simple to implement
- ✅ Low memory usage
- ✅ Works well for many optimization problems

## ❌ Disadvantages

- ❌ Can get stuck in local maxima
- ❌ Not guaranteed to find the global optimum
- ❌ Sensitive to the initial state
