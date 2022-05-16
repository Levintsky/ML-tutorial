# Distance, Divergence

## Distance
- Bregman Divergence: a class for convex functions;
- Squared Mahalanobis distance
- Probability:
	- KL Divergence;
- Matrix:
	- von Neumann divergence
- Empirical distribution:
	- **MMD** (Maximum Mean Discrepancy): A. Gretton, K. M. Borgwardt, M. J. Rasch, B. Scholkopf, and A. Smola. A kernel two-sample test. JMLR'02
		- https://www.zhihu.com/question/288185961/answer/459888198

## Distribution Distance
- Fisher Divergence: Johnson, O. Information theory and the central limit theorem, 2004.
	- F(p,q)=Ex||∇logp(x)−∇logq(x)||^2,
- KSD: Q. Liu, J. Lee, and M. Jordan. A kernelized stein discrepancy for goodness-of-fit tests. ICML'16
	- S(p, q) = Ex,x'∼p\[δq,p(x)k(x, x')δq,p(x')\]
	- where δq,p(x) = sq(x) − sp(x) is the score difference;
	- Su(p,q) = 1/n(n-1) Σij uq(xi,xj)