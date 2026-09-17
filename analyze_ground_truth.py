from collections import Counter

file_path = "com-amazon.all.dedup.cmty.txt\\com-amazon.all.dedup.cmty.txt"

community_sizes = []

with open(file_path, "r") as file:
    for line in file:
        nodes = line.strip().split()

        if nodes:
            community_sizes.append(len(nodes))

print("Number of ground-truth communities:", len(community_sizes))
print("Largest community:", max(community_sizes))
print("Smallest community:", min(community_sizes))
print("Average community size:", sum(community_sizes) / len(community_sizes))

print("\nCommunity size distribution:")

small = sum(1 for x in community_sizes if 3 <= x < 10)
medium = sum(1 for x in community_sizes if 10 <= x < 100)
large = sum(1 for x in community_sizes if x >= 100)

print("Small (3-9):", small)
print("Medium (10-99):", medium)
print("Large (100+):", large)