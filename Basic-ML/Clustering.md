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