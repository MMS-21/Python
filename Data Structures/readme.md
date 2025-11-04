# 🧱 Data Structures in Python

A collection of fundamental **data structures** implemented from scratch in Python, designed to demonstrate their internal logic, behavior, and performance characteristics.

Each data structure includes:
- Clean, well-documented Python implementation
- Comprehensive `README.md` with explanations and examples
- Time/space complexity analysis
- Practical use cases

---

## 📂 Directory Structure
```
data_structures/
├── linked_list/
│   ├── linked_list.py
│   └── README.md
├── stack/
│   ├── stack.py
│   └── README.md
├── queue/
│   ├── queue.py
│   └── README.md
├── binary_tree/
│   ├── binary_tree.py
│   └── README.md
└── graph/
    ├── graph.py
    └── README.md
```

---

## 🧩 Implemented Data Structures

| Data Structure  | Description | Key Operations |
|-----------------|-------------|----------------|
| **Linked List** | Sequential nodes connected via pointers for dynamic memory allocation | Insert: O(1), Access: O(n), Delete: O(1)* |
| **Stack** | LIFO structure for function calls, undo/redo, and expression parsing | Push: O(1), Pop: O(1), Peek: O(1) |
| **Queue** | FIFO structure for task scheduling, buffering, and BFS | Enqueue: O(1), Dequeue: O(1) |
| **Binary Tree** | Hierarchical structure for efficient searching and sorting | Insert/Search: O(log n)**, Delete: O(log n)** |
| **Graph** | Nodes and edges representing networks, maps, and relationships | Varies by implementation (adjacency list/matrix) |

*\*With reference to node*  
*\*\*Average case for balanced trees*

---

## 🚀 Quick Start

Run any implementation directly:
```bash
python data_structures/stack/stack.py
```

Each file includes example usage and test cases to demonstrate functionality.

---

## 🎯 Learning Goals

- **Understand** the internal mechanics of core data structures
- **Analyze** time and space complexity trade-offs
- **Build** a foundation for algorithmic problem-solving
- **Prepare** for technical interviews and competitive programming

---

## 📚 Resources

- [GeeksforGeeks - Data Structures](https://www.geeksforgeeks.org/data-structures/)
- [VisuAlgo](https://visualgo.net/) - Interactive algorithm visualizations
- *Introduction to Algorithms* (CLRS) - Cormen, Leiserson, Rivest & Stein

---

## 🤝 Contributing

Contributions are welcome! Whether it's:
- Bug fixes or optimizations
- Additional data structures
- Improved documentation
- Test coverage

Feel free to open an issue or submit a pull request.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with 🐍 Python for learning and teaching data structures**
