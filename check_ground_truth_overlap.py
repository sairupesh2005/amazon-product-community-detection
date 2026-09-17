from collections import Counter

file_path = "com-amazon.all.dedup.cmty.txt\\com-amazon.all.dedup.cmty.txt"

node_membership = Counter()
community_count = 0

with open(file_path, "r") as file:
    for line in file:
        nodes = line.strip().split()

        if nodes:
            community_count += 1

            for node in nodes:
                node_membership[node] += 1

print("Ground-truth communities:", community_count)

print("Unique products:", len(node_membership))

overlapping_nodes = sum(
    1 for count in node_membership.values()
    if count > 1
)

print("Products in multiple communities:", overlapping_nodes)

print(
    "Maximum communities for one product:",
    max(node_membership.values())
)

print("\nMembership distribution:")

for k in sorted(set(node_membership.values())):
    count = sum(
        1 for v in node_membership.values()
        if v == k
    )
    print(
        "Products in", k,
        "community/communities:", count
    )