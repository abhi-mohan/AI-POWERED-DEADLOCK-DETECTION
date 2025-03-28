
import networkx as nx
import matplotlib.pyplot as plt

# Sample process-resource allocation
allocation = {
  "P1": ["R1"],
  "P2": ["R2"],
  "P3": ["R3"],
  "P4": ["R1", "R4"],
}

request = {
  "P1": ["R2"],
  "P2": ["R3"],
  "P3": ["R1"],
  "P4": ["R3"]
}

def create_graph():
  G = nx.DiGraph()

  for process, resources in allocation.items():
      for resource in resources:
          G.add_edge(resource, process)  # Resource assigned to process

  for process, resources in request.items():
      for resource in resources:
          G.add_edge(process, resource)  # Process requesting resource

  return G

def detect_deadlock(G):
  try:
      cycle = nx.find_cycle(G, orientation='original')
      return cycle
  except nx.NetworkXNoCycle:
      return None

def draw_graph(G, deadlock_cycle=None):
  pos = nx.spring_layout(G)
  node_colors = []

  for node in G.nodes:
      if node.startswith("P"):
          node_colors.append("lightblue")  # Process nodes
      else:
          node_colors.append("lightcoral")  # Resource nodes

  plt.figure(figsize=(8, 6))
  nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color="black", arrows=True, node_size=2000)

  if deadlock_cycle:
      deadlock_edges = [(u, v) for u, v, _ in deadlock_cycle]
      nx.draw_networkx_edges(G, pos, edgelist=deadlock_edges, edge_color="red", width=2.5)

  plt.title("Process-Resource Graph (Deadlock Detection)")
  plt.show()

# Run the visualization
G = create_graph()
deadlock_cycle = detect_deadlock(G)
draw_graph(G, deadlock_cycle)

if deadlock_cycle:
  print("🔴 Deadlock Detected!")
else:
  print("🟢 No Deadlock Found.")
