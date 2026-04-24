# 🧩 Maze Solver Visualization (DFS / BFS / A*)

## 📌 Overview

This project is a **visual simulation of classical AI search algorithms** applied to a maze-solving problem. It demonstrates how different algorithms explore a maze and find a path from a **start point** to a **goal** while avoiding obstacles.

The visualization helps you clearly understand:

* How each algorithm explores nodes
* Differences in efficiency and behavior
* Pathfinding strategies in action (step-by-step animation)

---

## 🚀 Features

* Interactive visualization using **Pygame**
* Supports three algorithms:

  * **Depth-First Search (DFS)**
  * **Breadth-First Search (BFS)**
  * **A* Search (with Manhattan Distance heuristic)**
* Real-time animation of:

  * Visited nodes
  * Final path
* Simple keyboard controls to switch algorithms

---

## 🧠 AI Concepts Used

* **Goal-Based Agent**
* **Classical Search Algorithms**
* **Heuristic Function (Manhattan Distance for A*)**

---

## 🧩 Problem Description

The maze is represented as a **2D grid** where:

* `0` → Free cell
* `1` → Wall

The agent:

* Starts at a predefined position
* Moves in four directions (up, down, left, right)
* Attempts to reach the goal efficiently

---

## ⚙️ Algorithms Explained

### 🔹 DFS (Depth-First Search)

* Explores as deep as possible before backtracking
* Not guaranteed to find the shortest path

### 🔹 BFS (Breadth-First Search)

* Explores level by level
* **Guarantees the shortest path**

### 🔹 A* Search

* Uses a heuristic (Manhattan Distance)
* Balances exploration and optimality
* Efficient and finds the shortest path

---

## 🎮 Controls

| Key            | Action                        |
| -------------- | ----------------------------- |
| `D`            | Run DFS                       |
| `B`            | Run BFS                       |
| `A`            | Run A*                        |
| `R`            | Reset (currently placeholder) |
| `Close Window` | Exit program                  |

---

## 🖥️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/maze-solver.git
cd maze-solver
```

### 2. Install dependencies

```bash
pip install pygame
```

### 3. Run the project

```bash
python maze_solver.py
```

---

## 📊 Visualization Details

* **Blue** → Start
* **Red** → Goal
* **Light Blue** → Visited nodes
* **Green** → Final path
* **Black** → Walls
* **White** → Free space

---

## 🧪 Performance Goals (PEAS)

* Reach the goal successfully
* Find shortest path (BFS & A*)
* Minimize explored nodes
* Improve time efficiency

---

## 🌍 Environment Properties

* Fully Observable
* Deterministic
* Discrete
* Single-Agent
* Sequential
* Static

---

## 👥 Team Members

* Baher rabea rizq mostafa
* Hazem abdelrahman abdelrahman rizq
* Eyad hany mohamed mosa

---

## 📌 Future Improvements

* Add maze generation feature
* Implement weighted graphs
* Compare execution time and node count
* Add GUI controls instead of keyboard
* Improve reset functionality

---

## 📄 License

This project is for educational purposes.

---

## 💡 Notes

This project is ideal for students learning:

* Artificial Intelligence basics
* Search algorithms
* Pathfinding techniques
* Visualization with Pygame

