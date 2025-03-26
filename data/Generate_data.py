import os
import numpy as np
import pandas as pd

# Ensure the 'data/' directory exists
os.makedirs("data", exist_ok=True)

# Generate random process allocation data
def generate_data(num_samples=1000, num_resources=3):
    np.random.seed(42)  # For reproducibility

    data = []
    for _ in range(num_samples):
        allocation = np.random.randint(0, 5, num_resources)  # Random allocated resources
        max_demand = allocation + np.random.randint(1, 5, num_resources)  # Ensure max > allocated
        available = np.random.randint(1, 5, num_resources)  # Random available resources
        
        # Simulate deadlock (1 if resources are insufficient, else 0)
        deadlock = int(np.sum(allocation) > np.sum(available))

        data.append(list(allocation) + list(max_demand) + list(available) + [deadlock])

    columns = [f"alloc_R{i+1}" for i in range(num_resources)] + \
              [f"max_R{i+1}" for i in range(num_resources)] + \
              [f"avail_R{i+1}" for i in range(num_resources)] + ["deadlock"]

    return pd.DataFrame(data, columns=columns)

# Save dataset
df = generate_data()
df.to_csv("data/deadlock_dataset.csv", index=False)
print("✅ Deadlock dataset generated & saved in 'data/' folder.")
