# Dual Algorithms

## Lagrange Dual
- A good summary:
	- https://blog.csdn.net/asd136912/article/details/79149881
	- https://www.cnblogs.com/90zeng/p/Lagrange_duality.html
	- https://www.zhihu.com/question/58584814
	- https://zhuanlan.zhihu.com/p/26514613
- Application:
	- SVM;

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