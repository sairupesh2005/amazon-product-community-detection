# Load graph nodes
graph_nodes = set()

graph_file = "com-amazon.ungraph.txt\\com-amazon.ungraph.txt"

with open(graph_file, "r") as file:

    for line in file:

        line = line.strip()

        # Ignore comments/empty lines
        if not line or line.startswith("#"):
            continue

        parts = line.split()

        if len(parts) >= 2:
            graph_nodes.add(parts[0])
            graph_nodes.add(parts[1])


# Load ground-truth nodes
ground_truth_nodes = set()

gt_file = (
    "com-amazon.all.dedup.cmty.txt\\"
    "com-amazon.all.dedup.cmty.txt"
)

with open(gt_file, "r") as file:

    for line in file:

        line = line.strip()

        if not line or line.startswith("#"):
            continue

        nodes = line.split()

        for node in nodes:
            ground_truth_nodes.add(node)


# Compare
covered = graph_nodes & ground_truth_nodes
missing = graph_nodes - ground_truth_nodes

print("Graph nodes:", len(graph_nodes))
print("Ground-truth nodes:", len(ground_truth_nodes))
print("Nodes covered by ground truth:", len(covered))
print("Graph nodes missing from ground truth:", len(missing))

coverage = len(covered) / len(graph_nodes) * 100

print(
    "Ground-truth coverage:",
    round(coverage, 2),
    "%"
)