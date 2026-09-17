import csv
from collections import defaultdict

# ---------------------------------------
# 1. Load Louvain communities
# ---------------------------------------

louvain = defaultdict(set)

with open("louvain_communities.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        node = row["Product_ID"]
        community_id = int(row["Community_ID"])

        louvain[community_id].add(node)

print("Louvain communities:", len(louvain))


# ---------------------------------------
# 2. Load ground-truth communities
# ---------------------------------------

file_path = (
    "com-amazon.all.dedup.cmty.txt\\"
    "com-amazon.all.dedup.cmty.txt"
)

ground_truth = []

with open(file_path, "r") as file:

    for line in file:
        nodes = set(line.strip().split())

        if nodes:
            ground_truth.append(nodes)

print("Ground-truth communities:", len(ground_truth))


# ---------------------------------------
# 3. Create node -> GT communities map
# ---------------------------------------

node_to_gt = defaultdict(list)

for gt_id, community in enumerate(ground_truth):

    for node in community:
        node_to_gt[node].append(gt_id)


# ---------------------------------------
# 4. Evaluate each Louvain community
# ---------------------------------------

results = []

for louvain_id, community in louvain.items():

    # Count how many nodes from this
    # Louvain community occur in each GT community

    gt_overlap = defaultdict(int)

    for node in community:

        for gt_id in node_to_gt.get(node, []):
            gt_overlap[gt_id] += 1

    if not gt_overlap:
        continue

    # Find GT community with largest intersection

    best_gt, intersection = max(
        gt_overlap.items(),
        key=lambda x: x[1]
    )

    gt_size = len(ground_truth[best_gt])
    louvain_size = len(community)

    # Precision:
    # How much of the Louvain community
    # belongs to the best GT community?

    precision = intersection / louvain_size

    # Recall:
    # How much of the GT community
    # was captured by the Louvain community?

    recall = intersection / gt_size

    # F1 score

    if precision + recall > 0:
        f1 = (
            2 * precision * recall
            / (precision + recall)
        )
    else:
        f1 = 0

    results.append(
        (
            louvain_id,
            louvain_size,
            best_gt,
            gt_size,
            intersection,
            precision,
            recall,
            f1
        )
    )


# ---------------------------------------
# 5. Display results
# ---------------------------------------

results.sort(
    key=lambda x: x[7],
    reverse=True
)

print("\nTop 10 Louvain communities by F1:")
print("-----------------------------------------------")

for result in results[:10]:

    (
        louvain_id,
        louvain_size,
        gt_id,
        gt_size,
        intersection,
        precision,
        recall,
        f1
    ) = result

    print(
        "Louvain:", louvain_id,
        "| Size:", louvain_size,
        "| GT:", gt_id,
        "| GT Size:", gt_size,
        "| Intersection:", intersection,
        "| Precision:", round(precision, 4),
        "| Recall:", round(recall, 4),
        "| F1:", round(f1, 4)
    )


# ---------------------------------------
# 6. Average scores
# ---------------------------------------

average_precision = sum(
    r[5] for r in results
) / len(results)

average_recall = sum(
    r[6] for r in results
) / len(results)

average_f1 = sum(
    r[7] for r in results
) / len(results)


print("\nAverage Precision:", round(average_precision, 4))
print("Average Recall:", round(average_recall, 4))
print("Average F1:", round(average_f1, 4))