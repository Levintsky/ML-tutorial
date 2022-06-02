# 2nd-Order Optimizer

## Natural Gradient
- Resources and Tutorials:
	- Relation with Gauss-Newton
	- https://www.zhihu.com/question/266846405
	- https://zhuanlan.zhihu.com/p/82934100
	- James Martens. New insights and perspectives on the natural gradient method. 2017
		- Geometric interpretation: the steepest change of KL(P(θ+d)||P(θ)), locally symmetric;
- Legacy:
	- S.-I. Amari. Natural gradient works efficiently in learning. Neural Computation, 10(2): 251–276, 1998.
	- S.-i. Amari and A. Cichocki. Adaptive blind signal processing-neural network approaches. Proceedings of the IEEE, 86(10):2026–2048, 1998.
	- S.-i. Amari and H. Nagaoka. Methods of information geometry, volume 191. American Mathematical Soc., 2007.
- Alberto Bernacchia, Mate Lengyel, Guillaume Hennequin. Exact natural gradient in deep linear networks and application to the nonlinear case. NIPS'18
- Thomas George, César Laurent, Xavier Bouthillier, Nicolas Ballas, Pascal Vincent. Fast Approximate Natural Gradient Descent in a Kronecker Factored Eigenbasis. NIPS'18
- **FANG**: R. Grosse and R. Salakhudinov. Scaling up natural gradient by sparsely factorizing the inverse fisher matrix.
	- Cholesky decomposition.
- Octavian-Eugen Ganea, Gary Bécigneul, Thomas Hofmann. Hyperbolic Neural Networks. NIPS'18
- Higher-order:
	- Yang Song, Jiaming Song, Stefano Ermon. Accelerating Natural Gradient with Higher-Order Invariance. ICML'18
		- https://ermongroup.github.io/blog/geo/
