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

## Survey
- https://github.com/zhoushengisnoob/DeepClustering
- A Survey of Clustering With Deep Learning: From the Perspective of Network Architecture.
- Clustering with Deep Learning: Taxonomy and New Methods. 2018

## Deep Learning-based
- **DCN**: Deep Clustering Network. 2016
- **DBC**: Discriminatively Boosted Image Clustering with Fully Convolutional Auto-Encoders. 2017
- **MIXAE**: Deep Unsupervised Clustering Using Mixture of Autoencoders. 2017
- R LaLonde, D Zhang, M Shah. ClusterNet: Detecting Small Objects in Large Scenes by Exploiting Spatio-Temporal Information. 2017
- **GRACE**: Graph Clustering with Dynamic Embedding. 2017
- **DCC**: Deep Continuous Clustering. 2018
- **CPAC**: Clustering-driven Deep Embedding with Pairwise Constraints. 2018
- **ClusterNet**: B Wilder, E Ewing, B Dilkina, M Tambe. End-to-end learning and optimization on graphs. ICMLW'19
	- Insight: Instead of performing inference and optimization in two separate stages, do both simultaneously
	- Graph Embedding Layer
	- Differentiable K-means layer
- Attributed Graph Clustering: A Deep Attentional Embedding Approach. 2019
- **N2D**: N2D: (Not Too) Deep Clustering via Clustering the Local Manifold of an Autoencoded Embedding.
- **BCL**: Video Face Clustering with Unknown Number of Clusters. ICCV'19
	- https://github.com/makarandtapaswi/BallClustering_ICCV2019
- **ClusterSLAM**: ClusterSLAM: A SLAM Backend for Simultaneous Rigid Body. ICCV'19
- **DGG**: Deep Clustering by Gaussian Mixture Variational Autoencoders with Graph Embedding. ICCV'19
- **DCCM**: Deep Comprehensive Correlation Mining for Image Clustering. ICCV'19
	- https://github.com/Cory-M/DCCM
- **IIC**: Invariant Information Clustering for Unsupervised Image Classification and Segmentation. ICCV'19

## DBSCAN
- Ester, M., H. P. Kriegel, J. Sander, and X. Xu. A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise. In: Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining, Portland, OR, AAAI'96
- Schubert, E., Sander, J., Ester, M., Kriegel, H. P., & Xu, X. DBSCAN revisited, revisited: why and how you should (still) use DBSCAN. TODS'17

## Information Theory
- J. S. Bridle, A. J. Heading, and D. J. MacKay. Unsupervised classifiers, mutual information and 'phantom targets'. NIPS'92
- D. Barber and F. V. Agakov. Kernelized infomax clustering. NIPS'05
- A. Krause, P. Perona, and R. G. Gomes. Discriminative clustering by regularized information maximization. NIPS'10

## Dirichlet process mixture models
- Inifinite mixture models, non-parametric prior\
	<img src="/Basic-ML/images/dirichlet-process.png" alt="drawing" width="600"/>
- Statistical and Computational Trade-Offs in Kernel K-Means. NIPS'18
- Overlapping Clustering Models, and One (class) SVM to Bind Them All. NIPS'18
