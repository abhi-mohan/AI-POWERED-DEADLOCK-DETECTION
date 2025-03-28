# Visual Deadlock Analyzer (Graph-Based Representation)

## 📌 Overview
This module provides a **graphical representation of process-resource allocation** to visualize potential deadlocks.  
Using **NetworkX** and **Matplotlib**, we generate a directed graph where:
- **Processes** are represented as circles (nodes).
- **Resources** are represented as squares (nodes).
- **Edges** indicate process-resource allocation and request.

If a cycle is detected in the graph, it indicates a **deadlock**.

---

## 🚀 Installation
Ensure Python **3.7+** is installed.  
Then, install the required dependencies using:

```bash
pip install networkx matplotlib
