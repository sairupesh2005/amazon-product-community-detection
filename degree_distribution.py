import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

# ---------------------------------------
# 1. Load Amazon graph
# ---------------------------------------

G = nx.read_edgelist(
    "com-amazon.ungraph.txt\\com-amazon.ungraph.txt"
)

print("Graph loaded")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())


# ---------------------------------------
# 2. Calculate degrees
# ---------------------------------------

degrees = [
    degree
    for node, degree in G.degree()
]

print("Average degree:", sum(degrees) / len(degrees))
print("Maximum degree:", max(degrees))
print("Minimum degree:", min(degrees))


# ---------------------------------------
# 3. Count degree frequencies
# ---------------------------------------

degree_counts = Counter(degrees)


# ---------------------------------------
# 4. Plot degree distribution
# ---------------------------------------

x = sorted(degree_counts.keys())

y = [
    degree_counts[d]
    for d in x
]

plt.figure(figsize=(10, 6))

plt.bar(
    x,
    y,
    width=1
)

plt.xlabel("Node Degree")
plt.ylabel("Number of Products")

plt.title(
    "Degree Distribution of Amazon Co-Purchasing Network"
)

plt.tight_layout()

plt.savefig(
    "degree_distribution.png",
    dpi=300
)

plt.show()