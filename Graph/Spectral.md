# Spectral Clustering/Analysis

## Resources
- https://zhuanlan.zhihu.com/p/65539782
- https://zhuanlan.zhihu.com/p/120311352
- https://zhuanlan.zhihu.com/p/112277874

## Basics
- Find a **good** partition;
- Criteria:
	- Min edges: cut(A, B);
	- Normalized cut: cut(A, B)/ min(vol(A), vol(B));

## Adjacency, Laplacian
- Adjacency A:
	- Symmetric
	- Largest eigen-vector: (1, 1, 1, ...)
	- Not connected?
		- Each component: (1, 1, ...)
- Degree matrix: D
- Laplacian: L = D - A
	- All eigenvalue >= 0
	- Smallest: (1, 1, 1, ...)

## Classic Spectral Clustering
- A Ng, M Jordan, Y Weiss. On spectral clustering: Analysis and an algorithm. NIPS'02
- M Belkin, P Niyogi. Laplacian eigenmaps and spectral techniques for embedding and clustering. NIPS'02
- M Belkin, P Niyogi. Laplacian eigenmaps for dimensionality reduction and data representation. NC'03
- X Stella, J Shi. Multiclass spectral clustering. 2003
- F Bach, M Jordan. Learning spectral clustering. NIPS'04
- L Zelnik-Manor, P Perona. Self-tuning spectral clustering. NIPS'05
- U Von Luxburg. A tutorial on spectral clustering. 2007
- M Belkin, P Niyogi. Towards a theoretical foundation for Laplacian-based manifold methods. 2008
- U Von Luxburg, M Belkin, O Bousquet. Consistency of spectral clustering. Annual of Statistics'08

## NIPS'19
- Gecia Bravo Hermsdorff, Lee Gunderson. A Unifying Framework for Spectrum-Preserving Graph Sparsification and Coarsening
- Gail Weiss, Yoav Goldberg, Eran Yahav. Learning Deterministic Weighted Automata with Queries and Counterexamples
- Lorenzo Dall'Amico, Romain Couillet, Nicolas Tremblay. Revisiting the Bethe-Hessian: Improved Community Detection in Sparse Heterogeneous Graphs
