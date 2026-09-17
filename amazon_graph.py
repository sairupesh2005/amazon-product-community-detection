import networkx as nx

# Load Amazon graph
G = nx.read_edgelist(
    "com-amazon.ungraph.txt\\com-amazon.ungraph.txt"
)

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Degree statistics
degrees = [degree for node, degree in G.degree()]

print("Average degree:", sum(degrees) / len(degrees))
print("Maximum degree:", max(degrees))

# Connected components
print("Number of connected components:", nx.number_connected_components(G))

# Top 10 most connected products
top_nodes = sorted(G.degree(), key=lambda x: x[1], reverse=True)[:10]

print("\nTop 10 most connected products:")
for node, degree in top_nodes:
    print("Product:", node, "Connections:", degree)