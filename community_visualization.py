import networkx as nx
import csv
import matplotlib.pyplot as plt

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
# 2. Load Louvain community assignments
# ---------------------------------------

community_map = {}

with open("louvain_communities.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        node = row["Product_ID"]
        community = int(row["Community_ID"])

        community_map[node] = community


# ---------------------------------------
# 3. Select Louvain Community 0
# ---------------------------------------

target_community = 0

community_nodes = [
    node for node in G.nodes()
    if community_map.get(node) == target_community
]

community_graph = G.subgraph(community_nodes).copy()

print("Community 0 size:", community_graph.number_of_nodes())


# ---------------------------------------
# 4. Find connected components
# ---------------------------------------

components = list(
    nx.connected_components(community_graph)
)

components.sort(
    key=len,
    reverse=True
)

print("Connected components:", len(components))

print(
    "Largest connected component:",
    len(components[0])
)


# ---------------------------------------
# 5. Select largest connected component
# ---------------------------------------

largest_component = components[0]

subgraph = community_graph.subgraph(
    largest_component
).copy()


# ---------------------------------------
# 6. Limit visualization to 100 nodes
# ---------------------------------------

if subgraph.number_of_nodes() > 100:

    # Start with the highest-degree node
    start_node = max(
        subgraph.nodes(),
        key=subgraph.degree
    )

    selected_nodes = {start_node}

    # Expand through neighbors
    frontier = [start_node]

    while frontier and len(selected_nodes) < 100:

        current = frontier.pop(0)

        neighbors = sorted(
            subgraph.neighbors(current),
            key=subgraph.degree,
            reverse=True
        )

        for neighbor in neighbors:

            if neighbor not in selected_nodes:

                selected_nodes.add(neighbor)
                frontier.append(neighbor)

                if len(selected_nodes) >= 100:
                    break

    subgraph = subgraph.subgraph(
        selected_nodes
    ).copy()


# ---------------------------------------
# 7. Calculate node sizes
# ---------------------------------------

node_sizes = []

for node in subgraph.nodes():

    degree = subgraph.degree(node)

    node_sizes.append(
        50 + degree * 30
    )


# ---------------------------------------
# 8. Layout
# ---------------------------------------

plt.figure(figsize=(12, 8))

pos = nx.spring_layout(
    subgraph,
    seed=42,
    k=0.5
)


# ---------------------------------------
# 9. Draw edges
# ---------------------------------------

nx.draw_networkx_edges(
    subgraph,
    pos,
    alpha=0.4
)


# ---------------------------------------
# 10. Draw nodes
# ---------------------------------------

nx.draw_networkx_nodes(
    subgraph,
    pos,
    node_size=node_sizes
)


# ---------------------------------------
# 11. Title
# ---------------------------------------

plt.title(
    "Connected Sample from Louvain Community 0"
)

plt.axis("off")

plt.tight_layout()


# ---------------------------------------
# 12. Save image
# ---------------------------------------

plt.savefig(
    "connected_louvain_community.png",
    dpi=300
)

plt.show()