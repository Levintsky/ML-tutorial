# Dual Algorithms

## Good Resources
- Summaries:
	- https://blog.csdn.net/asd136912/article/details/79149881
	- https://www.cnblogs.com/90zeng/p/Lagrange_duality.html
	- https://www.zhihu.com/question/58584814
	- https://zhuanlan.zhihu.com/p/26514613
- Tutorials:
	- https://people.eecs.berkeley.edu/~elghaoui/Teaching/EE227A/lecture7.pdf
- Courses:
	- Cornell: https://people.orie.cornell.edu/dpw/orie6300/
	- Berkeley: https://people.eecs.berkeley.edu/~elghaoui/Teaching/EE227A/
	- Washington: https://courses.cs.washington.edu/courses/cse521/16sp/

## Conjugate Function
- Fenchel-Legendre Duality: https://tintin.space/2019/04/20/Primal/
- https://www.ise.ncsu.edu/fuzzy-neural/wp-content/uploads/sites/9/2019/03/Lecturenote5.pdf

## Lagrange Dual
- Bishop, PRML, Appendix E;
	- Maximize f(x1, x2) s.t. g(x1, x2) = 0;
	- Equality constraint: g(x)=0, partial derivative of f and g must be parallel (λ);
		- L(x,λ) = f(x) + λg(x)
		- ∇f + λ∇g = 0; parallel;
	- Inequality constraint: g(x) >= 0; g(x) > 0 inactive constraint, g(x) = 0, active; introduce λg(x):
		- g(x) >= 0;
		- λ >= 0 
		- λg(x) = 0;
- Lagrange dual (https://people.eecs.berkeley.edu/~elghaoui/Teaching/EE227A/lecture7.pdf)
	- Primal problem: minimization with Lagrange multiplier:
		- minf0(x), s.t. fi(x) <= 0;
		- L(x, λ) = f0(x) + Σλifi(x)
	- Then, primal problem: p = min_x max_λ L(x, λ)
	- Dual problem: d = max_λg(λ) = max_λ min_x L(x, λ)
	- Weak duality theorem: p >= d;
	- Strong duality for convex problem (such as SVM), gap is 0;
	- KKT condition: if satisfying, then gap is 0:
		- fi(x) <= 0; primal feasible;
		- λi >= 0; dual feasible;
		- λifi(x) = 0; complementary slackness;
		- ∇L = 0
- Conic dual (https://inst.eecs.berkeley.edu/~ee227a/fa10/login/l_dual_conic.html):
	- SP duality
	- SOCP duality; (Examples: largest eigenvalue, non-convex quadratic problem, minimum distance to an affine subspace; robust least-square; relaxed SVM);
- Applications:
	- SVM;

## Strong Duality
- Linear programming:
	- Wasserstein metric (Wasserstein or Kantorovich–Rubinstein metric or distance):
		- Formulation (optimal transport);\
			<img src = '/Optimization/images/dual/wgan-dual.png' width='400'>
		- Weak duality: (z >= z-dual), z = (c, x) >= (Ay, x) = (y, b) = z-dual
		- Strong duality: z = z-dual;
			- 1. Farkas Theorem:
			- 2. Contruct a problem related to oringal LP;
		- Cost function:\
			<img src = '/Optimization/images/dual/wgan-dual-2.png' width='400'>
		- Constraints: f(xi) + g(xj) <= Dij (Dii = 0 gives f(xi) + g(xi) <= 0)
		- Since we optimize [p-r, p-fake] x [f, g], both f(xi), g(xi) should be large, we have g+f=0, or g=-f;
		- Final cost: E(x-Pr)f(x) - E(x-P-fake)f(x);
		- Constraint f(xi) + g(xj) <= Dij become f(xi) - f(xj) <= Dij. f(xi) + f(xj) >= -Dij, which becomes Lipschitz L <= 1.
- Nash Equilibrium of Mixed Strategy:

## Convex Dual

## Primal-Dual also Proximal Methods
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
		- x(t+1) = Πg(x - τdf/dx)
	- **ISTA** (iterative soft-thresholding algorithm);
- A. Chambolle and T. Pock. A first-order primal-dual algorithm for convex problems with applications to imaging. JMIV'11
- N. Parikh and S. Boyd. Proximal algorithms. Foundations and Trends in optimization, 2014.
- Problem: H(x) = F(Kx)+G(x), K is kernel;
- Fenchel duality with auxiliary y: L(x,y)= y'Kx-F∗(y) + G(x), where F∗(y)=sup_z {z'y-F(z)}
- Algorithm:\
	<img src="/Optimization/images/dual/primal-dual.png" alt="drawing" width="400"/>
- ADMM
	- Intuition:
	- Problem: minimize f(x)+g(z) s.t. Ax+Bz=c;
	- Introduce another multiplier y, L(x,z,y) is unconstrained;
	- Algorithm:\
		<img src="/Optimization/images/dual/admm.png" alt="drawing" width="400"/>
	- Generally slower than gradient descent, Newton's method;
	- D. Gabay and B. Mercier. A dual algorithm for the solution of nonlinear variational problems via finite element approximation. Computers & Mathematics with Applications, 1976
	- S Boyd. Alternating Direction Method of Multipliers. 2011
	- Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers. 
- Proximal Methods:
	- Bregman Divergence:
		- Resouces:
			- https://www.zhihu.com/question/22426561/answer/209945856
		- Intuition:
			- Given a random variable X={x1, x2, ...}, the minimizer of f(y)=d(x,y) is y=E[x], satisfies iff f(.) is convex;
			- d(x, y) = f(x) - (f(y)+ < grad(f(y)), x-y>)
			- d(x, y) >= 0 implies f(x) convex;
			- **Assymetry**: in general D(x,y) != D(y,x);
		- Common Bregman divergence:\
			<img src="/Optimization/images/distance/bregman.jpg" alt="drawing" width="400"/>
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
