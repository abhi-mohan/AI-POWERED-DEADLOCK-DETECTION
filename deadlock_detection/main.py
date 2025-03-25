import networkx as nx
import pandas as pd
import time
import random
import os

# Ensure data/logs directory exists
os.makedirs("logs", exist_ok=True)

class DeadlockDetectionSystem:
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed Graph for Wait-for Graph

    def add_process(self, process_id):
        """ Adds a process to the wait-for graph """
        self.graph.add_node(process_id)
    
    def add_dependency(self, from_process, to_process):
        """ Adds an edge to represent a dependency between two processes """
        self.graph.add_edge(from_process, to_process)

    def detect_deadlock(self):
        """ Uses cycle detection in a directed graph to check for deadlocks """
        try:
            cycle = nx.find_cycle(self.graph, orientation="original")
            return True, cycle
        except nx.NetworkXNoCycle:
            return False, None

    def log_status(self, iteration):
        """ Logs the current graph and detection status """
        is_deadlocked, cycle = self.detect_deadlock()
        log_entry = f"Iteration {iteration}: Deadlock Detected - {is_deadlocked} | Cycle: {cycle if cycle else 'None'}\n"
        
        # Write to log file
        with open("logs/deadlock_log.txt", "a") as log_file:
            log_file.write(log_entry)

        return log_entry


# Simulated Deadlock Detection Execution
if __name__ == "__main__":
    system = DeadlockDetectionSystem()
    processes = ["P1", "P2", "P3", "P4"]

    # Add processes
    for p in processes:
        system.add_process(p)

    # Simulate dependencies (randomized for dynamic behavior)
    dependencies = [
        ("P1", "P2"),
        ("P2", "P3"),
        ("P3", "P4"),
        ("P4", "P1")  # This creates a cycle (deadlock)
    ]
    
    for dep in dependencies:
        system.add_dependency(*dep)

    print("🔍 Running Deadlock Detection...")

    for i in range(5):  # Simulate multiple checks
        time.sleep(1)  # Simulate processing delay
        log_entry = system.log_status(i+1)
        print(log_entry.strip())

    print("✅ Deadlock Detection Completed. Check logs/deadlock_log.txt for details.")
