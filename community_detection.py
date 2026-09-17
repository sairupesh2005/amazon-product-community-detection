import networkx as nx
import csv

# Load the Amazon graph
G = nx.read_edgelist(
    "com-amazon.ungraph.txt\\com-amazon.ungraph.txt"
)

print("Graph loaded")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# Louvain community detection
print("\nRunning Louvain community detection...")

communities = nx.community.louvain_communities(
    G,
    seed=42
)

print("Number of communities:", len(communities))

# Modularity
modularity = nx.community.modularity(G, communities)

print("Modularity:", modularity)

# Sort communities by size
communities = sorted(
    communities,
    key=len,
    reverse=True
)

print("\nTop 10 largest communities:")

for i, community in enumerate(communities[:10], start=1):
    print(
        "Community", i,
        "| Size:", len(community)
    )

# Save community assignments
with open("louvain_communities.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Product_ID", "Community_ID"])

    for community_id, community in enumerate(communities):
        for node in community:
            writer.writerow([node, community_id])

print("\nCommunity assignments saved to louvain_communities.csv")

# Community size statistics
sizes = [len(c) for c in communities]

print("\nCommunity size statistics:")
print("Largest community:", max(sizes))
print("Smallest community:", min(sizes))
print("Average community size:", sum(sizes) / len(sizes))

# Count communities by size
small = sum(1 for s in sizes if s < 1000)
medium = sum(1 for s in sizes if 1000 <= s < 5000)
large = sum(1 for s in sizes if s >= 5000)

print("\nCommunity size groups:")
print("Small (<1000):", small)
print("Medium (1000-4999):", medium)
print("Large (>=5000):", large)
