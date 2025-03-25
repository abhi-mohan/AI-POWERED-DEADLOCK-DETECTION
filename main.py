import numpy as np

def is_deadlock(allocation, max_demand, available):
    """
    Detects deadlocks using the Banker's Algorithm.
    
    :param allocation: Resources allocated to each process.
    :param max_demand: Maximum resources each process may need.
    :param available: Available resources.
    :return: True if deadlock detected, False otherwise.
    """
    num_processes, num_resources = allocation.shape
    need = max_demand - allocation  # Remaining resources needed
    work = available.copy()
    finish = np.zeros(num_processes, dtype=bool)

    while True:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(need[i] <= work):
                work += allocation[i]
                finish[i] = True
                found = True
        
        if not found:
            break
    
    return not all(finish)

# Sample input
allocation = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])
max_demand = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]])
available = np.array([3, 3, 2])

if is_deadlock(allocation, max_demand, available):
    print("⚠️ Deadlock detected!")
else:
    print("✅ No deadlock detected.")
