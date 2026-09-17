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
# 2. Calculate degree frequencies
# ---------------------------------------

degrees = [
    degree
    for node, degree in G.degree()
]

degree_counts = Counter(degrees)


# ---------------------------------------
# 3. Remove degree 0
# ---------------------------------------

x = []
y = []

for degree in sorted(degree_counts):

    if degree > 0:

        x.append(degree)
        y.append(degree_counts[degree])


# ---------------------------------------
# 4. Log-log plot
# ---------------------------------------

plt.figure(figsize=(10, 6))

plt.loglog(
    x,
    y,
    marker="o",
    markersize=3,
    linestyle="none"
)

plt.xlabel("Node Degree (log scale)")
plt.ylabel("Number of Products (log scale)")

plt.title(
    "Log-Log Degree Distribution of Amazon Network"
)

plt.grid(
    True,
    which="both",
    alpha=0.3
)

plt.tight_layout()


# ---------------------------------------
# 5. Save
# ---------------------------------------

plt.savefig(
    "degree_distribution_loglog.png",
    dpi=300
)

plt.show()