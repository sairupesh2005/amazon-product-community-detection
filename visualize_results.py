from collections import Counter
import csv
import matplotlib.pyplot as plt


# ---------------------------------------
# 1. Load Louvain community sizes
# ---------------------------------------

louvain_sizes = Counter()

with open("louvain_communities.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        community_id = row["Community_ID"]
        louvain_sizes[community_id] += 1

louvain_sizes = list(louvain_sizes.values())


# ---------------------------------------
# 2. Load ground-truth community sizes
# ---------------------------------------

ground_truth_sizes = []

file_path = (
    "com-amazon.all.dedup.cmty.txt\\"
    "com-amazon.all.dedup.cmty.txt"
)

with open(file_path, "r") as file:

    for line in file:

        nodes = line.strip().split()

        if nodes:
            ground_truth_sizes.append(len(nodes))


# ---------------------------------------
# 3. Categorize
# ---------------------------------------

def categorize(sizes):

    small = sum(
        1 for size in sizes
        if size < 1000
    )

    medium = sum(
        1 for size in sizes
        if 1000 <= size < 5000
    )

    large = sum(
        1 for size in sizes
        if size >= 5000
    )

    return [small, medium, large]


louvain = categorize(louvain_sizes)
ground_truth = categorize(ground_truth_sizes)


# ---------------------------------------
# 4. Convert to percentages
# ---------------------------------------

louvain_total = sum(louvain)
ground_truth_total = sum(ground_truth)

louvain_percent = [
    x / louvain_total * 100
    for x in louvain
]

ground_truth_percent = [
    x / ground_truth_total * 100
    for x in ground_truth
]


# ---------------------------------------
# 5. Print results
# ---------------------------------------

print("Louvain community percentages:")

for name, value in zip(
    ["Small", "Medium", "Large"],
    louvain_percent
):
    print(name, ":", round(value, 2), "%")


print("\nGround-truth community percentages:")

for name, value in zip(
    ["Small", "Medium", "Large"],
    ground_truth_percent
):
    print(name, ":", round(value, 2), "%")


# ---------------------------------------
# 6. Plot
# ---------------------------------------

categories = [
    "Small\n(<1000)",
    "Medium\n(1000-4999)",
    "Large\n(>=5000)"
]

x = range(len(categories))

width = 0.35

plt.figure(figsize=(10, 6))

plt.bar(
    [i - width / 2 for i in x],
    louvain_percent,
    width=width,
    label="Louvain"
)

plt.bar(
    [i + width / 2 for i in x],
    ground_truth_percent,
    width=width,
    label="Ground Truth"
)

plt.xlabel("Community Size Category")
plt.ylabel("Percentage of Communities (%)")

plt.title(
    "Louvain vs Ground-Truth Community Size Distribution"
)

plt.xticks(
    list(x),
    categories
)

plt.legend()

plt.tight_layout()

plt.savefig(
    "community_size_percentage_comparison.png",
    dpi=300
)

plt.show()