import csv
from collections import defaultdict

# -----------------------------
# 1. Load Louvain communities
# -----------------------------

louvain = defaultdict(set)

with open("louvain_communities.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        node = row["Product_ID"]
        community = int(row["Community_ID"])

        louvain[community].add(node)

print("Louvain communities:", len(louvain))


# -----------------------------
# 2. Load ground-truth
# -----------------------------

ground_truth = []

file_path = "com-amazon.all.dedup.cmty.txt\\com-amazon.all.dedup.cmty.txt"

with open(file_path, "r") as file:
    for line in file:
        nodes = set(line.strip().split())

        if nodes:
            ground_truth.append(nodes)

print("Ground-truth communities:", len(ground_truth))


# -----------------------------
# 3. Find best Jaccard match
# -----------------------------

results = []

for community_id, community in louvain.items():

    best_jaccard = 0
    best_gt = -1

    for gt_id, gt_community in enumerate(ground_truth):

        intersection = len(community & gt_community)
        union = len(community | gt_community)

        if union > 0:
            jaccard = intersection / union

            if jaccard > best_jaccard:
                best_jaccard = jaccard
                best_gt = gt_id

    results.append(
        (community_id, len(community), best_gt, best_jaccard)
    )


# -----------------------------
# 4. Sort by Louvain size
# -----------------------------

results.sort(
    key=lambda x: x[1],
    reverse=True
)


# -----------------------------
# 5. Display top 10
# -----------------------------

print("\nTop 10 Louvain communities:")
print("-----------------------------------------------")

for community_id, size, gt_id, score in results[:10]:

    print(
        "Louvain Community:",
        community_id,
        "| Size:",
        size,
        "| Best GT:",
        gt_id,
        "| Jaccard:",
        round(score, 4)
    )


# -----------------------------
# 6. Average best-match score
# -----------------------------

average_jaccard = sum(
    x[3] for x in results
) / len(results)

print("\nAverage best-match Jaccard:", average_jaccard)