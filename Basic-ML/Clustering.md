# Clustering

## Basics
- Hierarchical: find successive clusters;
	- Agglomerative (bottom-up);
	- Divisive (top-down);
	- Competitive learning: K-SOM;
- Partitional: determine all clusters at once;
	- K-means; [MacQueen, 1967]
		- Weakness: outliers, initial seed;
	- Model-based;
	- Graph Theoretic;
	- Spectral;
- Bayesian (Posterior over collection of data):
	- Decision based;
	- Nonparametric;

## DBSCAN
- Ester, M., H. P. Kriegel, J. Sander, and X. Xu. A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise. In: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI Press, pp. 226-231. 1996
- Schubert, E., Sander, J., Ester, M., Kriegel, H. P., & Xu, X. (2017). DBSCAN revisited, revisited: why and how you should (still) use DBSCAN. ACM Transactions on Database Systems (TODS), 42(3), 19.

## Information Theory
- J. S. Bridle, A. J. Heading, and D. J. MacKay. Unsupervised classifiers, mutual information and
'phantom targets'. NIPS'92
- D. Barber and F. V. Agakov. Kernelized infomax clustering. NIPS'05
- A. Krause, P. Perona, and R. G. Gomes. Discriminative clustering by regularized information maximization. NIPS'10

## Dirichlet process mixture models
- Inifinite mixture models, non-parametric prior\
	<img src="/Basic-ML/images/dirichlet-process.png" alt="drawing" width="600"/>
- Statistical and Computational Trade-Offs in Kernel K-Means. NIPS'18
- Overlapping Clustering Models, and One (class) SVM to Bind Them All. NIPS'18

## NIPS'19
- Lingxiao Huang, Shaofeng Jiang, Nisheeth Vishnoi. Coresets for Clustering with Fairness Constraints
- Marco Bressan, Nicolò Cesa-Bianchi, Andrea Paudice, Fabio Vitale. Correlation Clustering with Adaptive Similarity Queries
- Sanchit Kalhan, Konstantin Makarychev, Timothy Zhou. Correlation clustering with local objectives
- Debarghya Ghoshdastidar, Michaël Perrot, Ulrike von Luxburg. Foundations of Comparison-Based Hierarchical Clustering
- Vincent Cohen-Addad, Niklas Oskar D Hjuler, Nikos Parotsidis, David Saulpic, Chris Schwiegelshohn. Fully Dynamic Consistent Facility Location
- Aditya Bhaskara, Sharvaree Vadgama, Hong Xu. Greedy Sampling for Approximate Clustering in the Presence of Outliers
- Yair Marom, Dan Feldman. k-Means Clustering of Lines for Big Data
- Sariel Har-Peled, Sepideh Mahabadi. Near Neighbor: Who is the Fairest of Them All?
- Stefan Meintrup, Alexander Munteanu, Dennis Rohde. Random Projections and Sampling Algorithms for Clustering of High-Dimensional Polygonal Curves
- Wasim Huleihel, Arya Mazumdar, Muriel Medard, Soumyabrata Pal. Same-Cluster Querying for Overlapping Clusters
- Shin Matsushima, Maria Brbic. Selective Sampling-based Scalable Sparse Subspace Clustering
- Ioannis Koutis, Huong Le. Spectral Modification of Graphs for Improved Spectral Clustering
- Amir Abboud, Vincent Cohen-Addad, Hussein Houdrouge. Subquadratic High-Dimensional Hierarchical Clustering
- Tavor Baharav, David Tse. Ultra Fast Medoid Identification via Correlated Sequential Halving
- Giovanni Chierchia, Benjamin Perret. Ultrametric Fitting by Gradient Descent
