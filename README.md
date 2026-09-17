\# Community Detection in Amazon Product Co-Purchasing Networks Using Louvain Algorithm



\## Project Overview



This project analyzes the Amazon product co-purchasing network using graph mining techniques and detects communities using the Louvain algorithm.



The network represents relationships between Amazon products based on co-purchasing behavior.



\- Vertex (Node): Amazon product

\- Edge: Co-purchasing relationship between two products

\- Graph Type: Undirected graph

\- Community Detection Algorithm: Louvain



\## Dataset



The dataset is obtained from the Stanford Network Analysis Project (SNAP).



Dataset:

Amazon Product Co-Purchasing Network



The original dataset is not included in this repository. It can be downloaded from the official SNAP website:



https://snap.stanford.edu/data/com-Amazon.html



\## Dataset Statistics



\- Nodes: 334,863

\- Edges: 925,872

\- Average Degree: 5.53

\- Maximum Degree: 549

\- Connected Components: 1



\## Method



The Louvain community detection algorithm is used to identify groups of densely connected products.



The algorithm attempts to maximize modularity by moving nodes between communities and finding a partition with strong internal connectivity.



\## Results



\- Louvain Communities: 229

\- Modularity: 0.9258

\- Largest Louvain Community: 12,666 nodes

\- Average Best-Match Jaccard: 0.4029



\## Ground Truth Comparison



The Amazon dataset also contains ground-truth communities based on Amazon product categories.



The ground truth contains overlapping communities, while Louvain produces a non-overlapping partition.



Therefore, community evaluation was performed using set-based metrics such as:



\- Jaccard similarity

\- Precision

\- Recall

\- F1-score



\### Directional Evaluation



For Louvain communities compared against ground truth:



\- Average Precision: 0.6888

\- Average Recall: 0.2003

\- Average F1-score: 0.2131



For ground-truth communities compared against Louvain communities:



\- Average Precision: 0.0107

\- Average Recall: 0.9494

\- Average F1-score: 0.0172

\- Average Jaccard: 0.0102



These differences occur because the ground-truth communities are highly overlapping and much more fine-grained, whereas Louvain produces a non-overlapping partition.



\## Project Structure



```text

Amazon-Graph-Mining/

│

├── README.md

├── requirements.txt

├── .gitignore

│

├── amazon\_graph.py

├── community\_detection.py

├── analyze\_communities.py

├── analyze\_ground\_truth.py

├── check\_coverage.py

├── check\_ground\_truth\_overlap.py

├── community\_visualization.py

├── compare\_communities.py

├── degree\_distribution.py

├── degree\_loglog.py

├── ground\_truth\_to\_louvain.py

├── overlap\_evaluation.py

├── save\_evaluation.py

├── visualize\_results.py

│

├── community\_evaluation\_results.csv

├── ground\_truth\_to\_louvain\_results.csv

├── louvain\_communities.csv

│

└── figures/

&#x20;   ├── community\_size\_comparison.png

&#x20;   ├── community\_size\_percentage\_comparison.png

&#x20;   ├── connected\_louvain\_community.png

&#x20;   ├── degree\_distribution.png

&#x20;   ├── degree\_distribution\_loglog.png

&#x20;   ├── ground\_truth\_community\_size\_distribution.png

&#x20;   ├── louvain\_community\_size\_distribution.png

&#x20;   └── louvain\_community\_visualization.png

