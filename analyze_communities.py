import csv
from collections import Counter

community_sizes = Counter()

with open("louvain_communities.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        community_id = row["Community_ID"]
        community_sizes[community_id] += 1

sizes = list(community_sizes.values())

print("Number of communities:", len(sizes))
print("Largest community:", max(sizes))
print("Smallest community:", min(sizes))
print("Average community size:", sum(sizes) / len(sizes))

small = sum(1 for s in sizes if s < 1000)
medium = sum(1 for s in sizes if 1000 <= s < 5000)
large = sum(1 for s in sizes if s >= 5000)

print("\nCommunity size groups:")
print("Small (<1000):", small)
print("Medium (1000-4999):", medium)
print("Large (>=5000):", large)

print("\nTop 10 largest communities:")

for community, size in community_sizes.most_common(10):
    print("Community:", community, "| Size:", size)