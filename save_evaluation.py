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


# ---------------------------------------
# 2. Load ground truth
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


# ---------------------------------------
# 3. Node -> GT communities
# ---------------------------------------

node_to_gt = defaultdict(list)

for gt_id, community in enumerate(ground_truth):

    for node in community:
        node_to_gt[node].append(gt_id)


# ---------------------------------------
# 4. Calculate best matches
# ---------------------------------------

results = []

for louvain_id, community in louvain.items():

    overlap_counts = defaultdict(int)

    for node in community:

        for gt_id in node_to_gt.get(node, []):

            overlap_counts[gt_id] += 1


    if not overlap_counts:
        continue


    best_gt, intersection = max(
        overlap_counts.items(),
        key=lambda x: x[1]
    )

    louvain_size = len(community)
    gt_size = len(ground_truth[best_gt])

    precision = intersection / louvain_size
    recall = intersection / gt_size

    if precision + recall > 0:

        f1 = (
            2 * precision * recall
            / (precision + recall)
        )

    else:

        f1 = 0


    union = (
        louvain_size
        + gt_size
        - intersection
    )

    jaccard = intersection / union


    results.append([
        louvain_id,
        louvain_size,
        best_gt,
        gt_size,
        intersection,
        precision,
        recall,
        f1,
        jaccard
    ])


# ---------------------------------------
# 5. Sort by F1
# ---------------------------------------

results.sort(
    key=lambda x: x[7],
    reverse=True
)


# ---------------------------------------
# 6. Save CSV
# ---------------------------------------

with open(
    "community_evaluation_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Louvain_Community",
        "Louvain_Size",
        "Best_GT_Community",
        "GT_Size",
        "Intersection",
        "Precision",
        "Recall",
        "F1",
        "Jaccard"
    ])

    writer.writerows(results)


# ---------------------------------------
# 7. Print confirmation
# ---------------------------------------

print(
    "Evaluation results saved to:"
)

print(
    "community_evaluation_results.csv"
)

print(
    "Number of evaluated communities:",
    len(results)
)

print("\nTop 10:")
print("------------------------------")

for row in results[:10]:

    print(
        "Louvain:", row[0],
        "| F1:", round(row[7], 4),
        "| Jaccard:", round(row[8], 4)
    )