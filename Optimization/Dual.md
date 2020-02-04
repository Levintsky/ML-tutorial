# Dual Algorithms

## Lagrange Dual
- A good summary:
	- https://blog.csdn.net/asd136912/article/details/79149881
	- https://www.cnblogs.com/90zeng/p/Lagrange_duality.html
	- https://www.zhihu.com/question/58584814
	- https://zhuanlan.zhihu.com/p/26514613
- Good tutorials:
	- https://people.eecs.berkeley.edu/~elghaoui/Teaching/EE227A/lecture7.pdf
- Application:
	- SVM;
- Bishop, PRML, Appendix E;
	- Maximize f(x1, x2) s.t. g(x1, x2) = 0;
	- Equality constraint: partial derivative of f and g must be parallel (lambda);
		<img src="/Optimization/images/dual/lagrange-dual-1.png" alt="drawing" width="400"/>
	- Inequality constraint: g(x) >= 0; g(x) > 0 inactive constraint, g(x) = 0, active; introduce lambda \* g(x):
		<img src="/Optimization/images/dual/lagrange-dual-2.png" alt="drawing" width="400"/>
- Lagrange dual (https://people.eecs.berkeley.edu/~elghaoui/Teaching/EE227A/lecture7.pdf)
	- Primal problem: minimization with Lagrange multiplier\
		<img src="/Optimization/images/dual/l-dual-1.png" alt="drawing" width="400"/>
		<img src="/Optimization/images/dual/l-dual-2.png" alt="drawing" width="400"/>\
	- Then, primal problem:\
		<img src="/Optimization/images/dual/l-dual-3.png" alt="drawing" width="400"/>
	- Dual problem:\
		<img src="/Optimization/images/dual/l-dual-4.png" alt="drawing" width="400"/>\
		<img src="/Optimization/images/dual/l-dual-5.png" alt="drawing" width="400"/>
	- Weak duality theorem:\
		<img src="/Optimization/images/dual/l-dual-6.png" alt="drawing" width="400"/>
	- Strong duality for convex problem (such as SVM), gap is 0;
	- KKT condition: if satisfying, then gap is 0:\
		<img src="/Optimization/images/dual/l-dual-7.png" alt="drawing" width="400"/>
- Conic dual (https://inst.eecs.berkeley.edu/~ee227a/fa10/login/l_dual_conic.html):
	- SP duality
	- SOCP duality; (Examples: largest eigenvalue, non-convex quadratic problem, minimum distance to an affine subspace; robust least-square; relaxed SVM);

## Primal Dual
- Fenchel-Legendre Duality
- https://tintin.space/2019/04/20/Primal/
- **ADMM**: D. Gabay and B. Mercier. A dual algorithm for the solution of nonlinear variational problems via finite element approximation. Computers & Mathematics with Applications, 1976
- S Boyd. Alternating Direction Method of Multipliers. 2011
- A. Chambolle and T. Pock. A first-order primal-dual algorithm for convex problems with applications to imaging. JMIV'11
- N. Parikh and S. Boyd. Proximal algorithms. Foundations and Trends in optimization, 2014.
- https://huixuan.wordpress.com/2015/01/02/primal-dual-algorithm%E7%9A%84%E7%B2%97%E6%B5%85%E8%A7%A3%E9%87%8A/
- Problem: H(x) = F(Kx)+G(x), K is kernel;
- Fenchel duality with auxiliary y: L(x,y)= < y, Kx > - F\*(y) + G(x), where F\*(y)=sup_z {< z, y> - F(z)}
- Algorithm:\
	<img src="/Optimization/images/dual/primal-dual.png" alt="drawing" width="400"/>

## Conjugate Dual

## Convex Dual