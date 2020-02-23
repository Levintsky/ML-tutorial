# 2nd-Order Optimizer

## Natural Gradient
- Resources and Tutorials:
	- Relation with Gauss-Newton
	- https://www.zhihu.com/question/266846405
	- https://zhuanlan.zhihu.com/p/82934100
	- James Martens. New insights and perspectives on the natural gradient method. 2017
		- Geometric interpretation: the steepest change of KL(P(theta+d)||P(theta)), locally symmetric;
- Key idea:
	- Left multiplying inverse of Fisher Information matrix
- Fisher Information Matrix:
	- PSD (positive semi-definite);
- Legacy:
	- S.-I. Amari. Natural gradient works efficiently in learning. Neural Computation, 10(2): 251–276, 1998.
	- S.-i. Amari and A. Cichocki. Adaptive blind signal processing-neural network approaches. Proceedings of the IEEE, 86(10):2026–2048, 1998.
	- S.-i. Amari and H. Nagaoka. Methods of information geometry, volume 191. American Mathematical Soc., 2007.
- **PRONG**: G. Desjardins, K. Simonyan, R. Pascanu, et.al. Natural neural networks. NIPS'15
	- Whitening each layer.
- **KFAC**: J. Martens and R. Grosse. Optimizing neural networks with kronecker-factored approximate curvature. 2016
	- Kronecker approximation to Fisher
	- Assumption: FC (si = Wi\* ai) + non-linear (ai = phi(si)), then DWi=gi x ai-1, Fisher:\
		<img src="/Optimization/images/2nd/k-fac1.png" alt="drawing" width="400"/>
	- Approx:\
		<img src="/Optimization/images/2nd/k-fac2.png" alt="drawing" width="400"/>
- R. Grosse and J. Martens. A Kronecker-factored approximate Fisher matrix for convolutional layers. ICML'16
- Alberto Bernacchia, Mate Lengyel, Guillaume Hennequin. Exact natural gradient in deep linear networks and application to the nonlinear case. NIPS'18
- Thomas George, César Laurent, Xavier Bouthillier, Nicolas Ballas, Pascal Vincent. Fast Approximate Natural Gradient Descent in a Kronecker Factored Eigenbasis. NIPS'18
- **FANG**: R. Grosse and R. Salakhudinov. Scaling up natural gradient by sparsely factorizing the inverse fisher matrix.
	- Cholesky decomposition.
- Octavian-Eugen Ganea, Gary Bécigneul, Thomas Hofmann. Hyperbolic Neural Networks. NIPS'18
