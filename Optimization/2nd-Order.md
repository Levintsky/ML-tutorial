# 2nd-Order Optimizer

## Basics
- Struggle to improve over first-order baselines for non-convex loss surfaces;
- Intuition for natural gradient:
	- 2nd order: Left multiplying inverse of Fisher Information matrix
	- Fisher Information Matrix:
		- PSD (positive semi-definite);
	- Differential manifold on probability measure;

## Natural Gradient
- Resources and Tutorials:
	- Relation with Gauss-Newton
	- https://www.zhihu.com/question/266846405
	- https://zhuanlan.zhihu.com/p/82934100
	- James Martens. New insights and perspectives on the natural gradient method. 2017
		- Geometric interpretation: the steepest change of KL(P(theta+d)||P(theta)), locally symmetric;
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

## Low-Rank Approximation
- Martens, James. Deep learning via hessian-free optimization. ICML'10
- **KFAC**: J. Martens and R. Grosse. Optimizing neural networks with kronecker-factored approximate curvature. ICML'15
	- Kronecker approximation to Fisher
	- Assumption: FC (si = Wi\* ai) + non-linear (ai = phi(si)), then DWi=gi x ai-1, Fisher:\
		<img src="/Optimization/images/2nd/k-fac1.png" alt="drawing" width="400"/>
	- Approx:\
		<img src="/Optimization/images/2nd/k-fac2.png" alt="drawing" width="400"/>
- R. Grosse and J. Martens. A Kronecker-factored approximate Fisher matrix for convolutional layers. ICML'16
	- Follow-up on KFAC for convolutions
- Instability:
	- Byrd, R., Hansen, S., Nocedal, J., and Singer, Y. A stochastic quasi-newton method for large-scale optimization. SIAM Journal on Optimization'16
- Estimate the metric:
	- Pascanu, Razvan and Bengio, Yoshua. Revisiting natural gradient for deep networks. ICLR'14
	- KFAC. ICML'15
	- **PRONG**: G. Desjardins, K. Simonyan, R. Pascanu, et.al. Natural neural networks. NIPS'15
		- Whitening each layer.
