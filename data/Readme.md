# Deadlock Detection Dataset

## 📌 Overview
This dataset is used for training and testing an AI model to detect deadlock in a system. It includes resource allocation details for multiple processes.

## 📂 Files
- **`deadlock_dataset.csv`** → Main dataset containing process allocations and available resources.
- **`generate_data.py`** → Script to generate synthetic datasets for testing.

## 📊 Dataset Columns
- `alloc_R1`, `alloc_R2`, `alloc_R3` → Allocated resources for each process.
- `max_R1`, `max_R2`, `max_R3` → Maximum resources required.
- `avail_R1`, `avail_R2`, `avail_R3` → Available resources in the system.

## 🛠 Usage
- If you need more training data, run `generate_data.py` to create a new dataset.

---
