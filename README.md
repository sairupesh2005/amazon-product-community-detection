# Community Detection in Amazon Product Co-Purchasing Network Using Louvain Algorithm

## Project Overview

This project applies Graph Mining techniques to the Amazon Product Co-Purchasing Network from the Stanford Network Analysis Project (SNAP).

The main objective is to identify communities of products that are strongly connected through customer co-purchasing relationships using the Louvain Community Detection Algorithm.

In this network:

- Each node represents an Amazon product.
- Each edge represents a co-purchasing relationship between two products.
- Communities represent groups of products that are more densely connected with each other.

The project also compares the detected Louvain communities with the available Amazon ground-truth communities.

## Dataset

Dataset: Stanford SNAP Amazon Product Co-Purchasing Network

The network represents the "Customers Who Bought This Item Also Bought" relationship.

### Dataset Statistics

| Property | Value |
|---|---:|
| Nodes | 334,863 |
| Edges | 925,872 |
| Average Degree | 5.53 |
| Maximum Degree | 549 |
| Connected Components | 1 |
| Graph Type | Undirected |
| Edge Weight | Unweighted |

The original dataset is not included in this repository because of its large size.

## Objectives

1. Construct the Amazon product co-purchasing graph.
2. Analyze basic graph properties.
3. Analyze the degree distribution of products.
4. Detect communities using the Louvain algorithm.
5. Measure community structure using modularity.
6. Analyze community size distribution.
7. Compare detected communities with Amazon ground-truth communities.
8. Evaluate community similarity using Jaccard similarity, Precision, Recall and F1-score.
9. Visualize important graph and community properties.

## Graph Model

The Amazon network is modeled as an undirected graph:

```text
G = (V, E)
````

where:

* V = set of Amazon products
* E = co-purchasing relationships

An edge between two products indicates that they occur together in the co-purchasing network.

## Graph Analysis

The project performs the following graph analyses:

* Number of nodes and edges
* Average degree
* Maximum degree
* Connected components
* Degree distribution
* Log-log degree distribution
* Network visualization

### Highest-Degree Products

| Product ID | Degree |
| ---------- | -----: |
| 548091     |    549 |
| 458358     |    324 |
| 222074     |    257 |
| 199628     |    230 |
| 515301     |    228 |
| 291117     |    219 |
| 502784     |    217 |
| 296016     |    212 |
| 239107     |    205 |
| 436020     |    197 |

## Community Detection

### Louvain Algorithm

The main community detection algorithm used in this project is the Louvain algorithm.

Louvain is a modularity-based community detection algorithm that identifies groups of densely connected nodes.

The implementation uses NetworkX:

```python
communities = nx.community.louvain_communities(G, seed=42)
```

A fixed seed is used for reproducibility.

### Louvain Results

The Louvain algorithm detected:

* Number of communities: **229**
* Modularity: **0.9258**
* Largest community: **12,666 nodes**
* Smallest community: **10 nodes**
* Average community size: **1,462.28 nodes**

### Top 10 Largest Communities

| Rank | Community Size |
| ---: | -------------: |
|    1 |         12,666 |
|    2 |         12,446 |
|    3 |         11,458 |
|    4 |         10,990 |
|    5 |          8,839 |
|    6 |          8,566 |
|    7 |          6,949 |
|    8 |          6,767 |
|    9 |          6,297 |
|   10 |          5,969 |

## Ground-Truth Communities

The Amazon dataset also provides ground-truth communities based on Amazon product categories.

The ground-truth communities are highly overlapping, meaning that a product can belong to multiple ground-truth communities.

### Ground-Truth Statistics

| Property                            |   Value |
| ----------------------------------- | ------: |
| Ground-truth communities            |  75,149 |
| Unique products in ground truth     | 317,194 |
| Products in multiple communities    | 301,594 |
| Maximum communities for one product |     116 |
| Ground-truth coverage               |  94.72% |

Because the ground truth is overlapping while Louvain produces a non-overlapping partition, direct one-to-one comparison is not appropriate.

## Community Evaluation

The detected communities are compared with the ground-truth communities using set-based evaluation metrics.

### Jaccard Similarity

```text
J(A,B) = |A ∩ B| / |A ∪ B|
```

### Precision

```text
Precision = |A ∩ B| / |A|
```

### Recall

```text
Recall = |A ∩ B| / |B|
```

### F1-Score

```text
F1 = 2 × Precision × Recall / (Precision + Recall)
```

### Best-Match Evaluation

For each Louvain community, the best matching ground-truth community is identified.

Average best-match Jaccard similarity:

**0.4029**

The results show that some Louvain communities have strong overlap with particular ground-truth communities, while others have weaker overlap.

## Directional Ground-Truth Evaluation

The comparison was also performed from the ground-truth perspective.

For each ground-truth community, the best matching Louvain community was identified.

Results:

| Metric    | Average |
| --------- | ------: |
| Precision |  0.0107 |
| Recall    |  0.9494 |
| F1-score  |  0.0172 |
| Jaccard   |  0.0102 |

The difference between the evaluation directions is mainly due to the difference in granularity and overlap between the ground-truth communities and the non-overlapping Louvain partition.

## Visualizations

The project generates the following visualizations:

1. Degree distribution
2. Log-log degree distribution
3. Louvain community size distribution
4. Ground-truth community size distribution
5. Louvain vs ground-truth community size comparison
6. Community size percentage comparison
7. Louvain community network visualization
8. Connected Louvain community visualization

## Project Structure

```text
graph_mining/
│
├── amazon_graph.py
├── community_detection.py
├── analyze_communities.py
├── analyze_ground_truth.py
├── check_coverage.py
├── check_ground_truth_overlap.py
├── compare_communities.py
├── overlap_evaluation.py
├── ground_truth_to_louvain.py
├── save_evaluation.py
├── visualize_results.py
├── community_visualization.py
├── degree_distribution.py
├── degree_loglog.py
│
├── louvain_communities.csv
├── community_evaluation_results.csv
├── ground_truth_to_louvain_results.csv
│
├── degree_distribution.png
├── degree_distribution_loglog.png
├── louvain_community_size_distribution.png
├── ground_truth_community_size_distribution.png
├── community_size_comparison.png
├── community_size_percentage_comparison.png
├── louvain_community_visualization.png
├── connected_louvain_community.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

* Python
* NetworkX
* NumPy
* Pandas
* Matplotlib
* VS Code
* Git
* GitHub

## Installation

Clone the repository:

```bash
git clone https://github.com/sairupesh2005/amazon-product-community-detection.git
cd amazon-product-community-detection
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Dataset Setup

Download the Amazon network dataset from Stanford SNAP.

Place the dataset folders inside the project directory:

```text
graph_mining/
│
├── com-amazon.ungraph.txt/
│   └── com-amazon.ungraph.txt
│
└── com-amazon.all.dedup.cmty.txt/
    └── com-amazon.all.dedup.cmty.txt
```

The dataset folders are excluded from Git using `.gitignore`.

## Running the Project

Run the graph analysis:

```bash
python amazon_graph.py
```

Run Louvain community detection:

```bash
python community_detection.py
```

Analyze communities:

```bash
python analyze_communities.py
```

Analyze ground-truth communities:

```bash
python analyze_ground_truth.py
```

Check ground-truth overlap:

```bash
python check_ground_truth_overlap.py
```

Compare Louvain communities with ground truth:

```bash
python compare_communities.py
```

Run overlap evaluation:

```bash
python overlap_evaluation.py
```

Run ground-truth-to-Louvain evaluation:

```bash
python ground_truth_to_louvain.py
```

Generate visualizations:

```bash
python visualize_results.py
```

## Reproducibility

The Louvain algorithm uses:

```python
seed=42
```

This allows the community detection experiment to be reproduced consistently.

## Important Evaluation Note

The Amazon ground-truth communities are highly overlapping, while Louvain produces a non-overlapping partition.

Therefore, the evaluation metrics should be interpreted as **community overlap measurements**, not classification accuracy.

The different Precision, Recall, F1-score and Jaccard values from the two evaluation directions reflect the granularity mismatch between the ground-truth communities and Louvain communities.

## References

### Dataset

Stanford Network Analysis Project (SNAP)

Amazon Product Co-Purchasing Network:

[https://snap.stanford.edu/data/com-Amazon.html](https://snap.stanford.edu/data/com-Amazon.html)

### Algorithm

Blondel, V. D., Guillaume, J.-L., Lambiotte, R., & Lefebvre, E. (2008).

Fast unfolding of communities in large networks.

Journal of Statistical Mechanics: Theory and Experiment.

## Project Title

**Community Detection in Amazon Product Co-Purchasing Networks Using Louvain Algorithm**
