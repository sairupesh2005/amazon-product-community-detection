import csv
from collections import defaultdict


# ---------------------------------------
# 1. Load Louvain assignments
# ---------------------------------------

node_to_louvain = {}

with open("louvain_communities.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        node = row["Product_ID"]
        community = int(row["Community_ID"])

        node_to_louvain[node] = community


print(
    "Louvain nodes:",
    len(node_to_louvain)
)


# ---------------------------------------
# 2. Load ground-truth communities
# ---------------------------------------

ground_truth = []

file_path = (
    "com-amazon.all.dedup.cmty.txt\\"
    "com-amazon.all.dedup.cmty.txt"
)

with open(file_path, "r") as file:

    for line in file:

        nodes = set(line.strip().split())

        if nodes:
            ground_truth.append(nodes)


print(
    "Ground-truth communities:",
    len(ground_truth)
)


# ---------------------------------------
# 3. Compare GT -> Louvain
# ---------------------------------------

results = []

for gt_id, gt_community in enumerate(ground_truth):

    overlap_counts = defaultdict(int)

    for node in gt_community:

        if node in node_to_louvain:

            louvain_id = node_to_louvain[node]

            overlap_counts[louvain_id] += 1


    if not overlap_counts:
        continue


    # Best Louvain match
    best_louvain, intersection = max(
        overlap_counts.items(),
        key=lambda x: x[1]
    )


    gt_size = len(gt_community)

    louvain_size = sum(
        1
        for node, community in node_to_louvain.items()
        if community == best_louvain
    )


    # Precision
    precision = intersection / louvain_size


    # Recall
    recall = intersection / gt_size


    # F1
    if precision + recall > 0:

        f1 = (
            2 * precision * recall
            / (precision + recall)
        )

    else:

        f1 = 0


    # Jaccard
    union = (
        gt_size
        + louvain_size
        - intersection
    )

    jaccard = intersection / union


    results.append([
        gt_id,
        gt_size,
        best_louvain,
        louvain_size,
        intersection,
        precision,
        recall,
        f1,
        jaccard
    ])


# ---------------------------------------
# 4. Calculate averages
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

average_jaccard = sum(
    r[8] for r in results
) / len(results)


# ---------------------------------------
# 5. Print final results
# ---------------------------------------

print("\nGround Truth -> Louvain")
print("--------------------------------")

print(
    "Evaluated GT communities:",
    len(results)
)

print(
    "Average Precision:",
    round(average_precision, 4)
)

print(
    "Average Recall:",
    round(average_recall, 4)
)

print(
    "Average F1:",
    round(average_f1, 4)
)

print(
    "Average Jaccard:",
    round(average_jaccard, 4)
)


# ---------------------------------------
# 6. Save results
# ---------------------------------------

with open(
    "ground_truth_to_louvain_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "GT_Community",
        "GT_Size",
        "Best_Louvain",
        "Louvain_Size",
        "Intersection",
        "Precision",
        "Recall",
        "F1",
        "Jaccard"
    ])

    writer.writerows(results)


print(
    "\nResults saved to:"
)

print(
    "ground_truth_to_louvain_results.csv"
)