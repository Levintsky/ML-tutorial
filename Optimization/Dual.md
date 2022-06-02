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
