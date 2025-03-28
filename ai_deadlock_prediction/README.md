# AI-Based Deadlock Prediction

## 📌 Overview
This module uses **Machine Learning** (Decision Trees) to predict the probability of deadlock based on process-resource allocation patterns.  
It analyzes system states and classifies them as:
- **Safe State (No Deadlock)**
- **Unsafe State (Possible Deadlock)**

Using a **trained ML model**, the system predicts if the given process allocation leads to deadlock.

---

## 🚀 Installation
Ensure Python **3.7+** is installed.  
Then, install the required dependencies using:

```bash
pip install numpy pandas scikit-learn
