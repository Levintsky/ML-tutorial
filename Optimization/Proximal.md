# Proximal Gradient Descent

## Proximal Methods (Also Primal Dual)
- Resources:
	- Shenlong's slides;
	- https://zhuanlan.zhihu.com/p/82622940
	- https://zhuanlan.zhihu.com/p/103161094
	- https://huixuan.wordpress.com/2015/01/02/primal-dual-algorithm%E7%9A%84%E7%B2%97%E6%B5%85%E8%A7%A3%E9%87%8A/
- Intuition:
	- Mainly used for non-differentiable problem (l1);
		- f(x)+g(x)
		- f() convex differntiable;
		- g() convex non-differntiable, **cheap proximal operator**;
		- x(t+1) = prox_g(x - tau df/dx)
	- **ISTA** (iterative soft-thresholding algorithm);
- A. Chambolle and T. Pock. A first-order primal-dual algorithm for convex problems with applications to imaging. JMIV'11
- N. Parikh and S. Boyd. Proximal algorithms. Foundations and Trends in optimization, 2014.
- Problem: H(x) = F(Kx)+G(x), K is kernel;
- Fenchel duality with auxiliary y: L(x,y)= < y, Kx > - F\*(y) + G(x), where F\*(y)=sup_z {< z, y> - F(z)}
- Algorithm:\
	<img src="/Optimization/images/dual/primal-dual.png" alt="drawing" width="400"/>

## ADMM
- Intuition:
	- Problem: minimize f(x)+g(z) s.t. Ax+Bz=c;
	- Introduce another multiplier y, L(x,z,y) is unconstrained;
	- Algorithm:\
		<img src="/Optimization/images/dual/admm.png" alt="drawing" width="400"/>
	- Generally slower than gradient descent, Newton's method;
- D. Gabay and B. Mercier. A dual algorithm for the solution of nonlinear variational problems via finite element approximation. Computers & Mathematics with Applications, 1976
- S Boyd. Alternating Direction Method of Multipliers. 2011
- Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers. 

## Proximal Methods
- Bregman Divergence:
	- Resouces:
		- https://www.zhihu.com/question/22426561/answer/209945856
	- Intuition:
		- Given a random variable X={x1, x2, ...}, the minimizer of f(y)=d(x,y) is y=E[x], satisfies iff f(.) is convex;
		- d(x, y) = f(x) - (f(y)+ < grad(f(y)), x-y>)
		- d(x, y) >= 0 implies f(x) convex;
		- **Assymetry**: in general D(x,y) != D(y,x);
	- Common Bregman divergence:\
		<img src="/Optimization/images/distance/bregman.png" alt="drawing" width="400"/>
	- Legacy:
		- Banerjee, Arindam, Xin Guo, and Hui Wang. On the optimality of conditional expectation as a Bregman predictor. IEEE Transactions on Information Theory'05
		- Banerjee, Arindam, et al. Clustering with Bregman divergences. JMLR'05
- Mirror descent:
	- Resources:
		- https://zhuanlan.zhihu.com/p/34299990
		- E. Candes. Mathematical optimization, MATH301 lecture notes, Stanford.
		- S. Boyd. Convex optimization, EE364B lecture notes. Stanford.
		- D. Bertsekas. Nonlinear Programming (2nd Edition). Athena Scientific, 2016.
	- Intuition: replace the L2 regularization of ||xt-xt+1||^2 with Bregman Divergence;
	- Legacy:
		- A. Nemirovski, D. Yudin, Wiley. Problem complexity and method efficiency in optimization.  1983.
		- Ben-Tal, Aharon, Tamar Margalit, and Arkadi Nemirovski. The ordered subsets mirror descent optimization method with applications to tomography. SIAM Journal on Optimization'01
		- A. Beck, M. Teboulle. Mirror descent and nonlinear projected subgradient methods for convex optimization. Operations Research Letters, 31(3), 2003.
		- I. Dhillon, J. Tropp. Matrix nearness problems with Bregman divergences. , SIAM Journal on Matrix Analysis and Applications, 29(4), 2007.
		- S. Bubeck. Convex optimization: algorithms and complexity. Foundations and trends in machine learning, 2015.
		- A. Beck. First-order methods in optimization. Vol. 25, SIAM, 2017.
	- Mirror descent:
		- Naive, 1/t convergence:\
			<img src="/Optimization/images/distance/mirror-1.png" alt="drawing" width="400"/>
		- Nestorov: 1/t^2 convergence:\
			<img src="/Optimization/images/distance/mirror-2.png" alt="drawing" width="400"/>
	- A good summary by Yuxin Chen: http://www.princeton.edu/~yc5/ele522_optimization/lectures/mirror_descent.pdf