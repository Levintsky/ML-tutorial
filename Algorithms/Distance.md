# Distance, Divergence

## Distance
- Bregman Divergence: a class for convex functions;
	- Resouces:
		- https://www.zhihu.com/question/22426561/answer/209945856
	- Intuition:
		- Given a random variable X={x1, x2, ...}, the minimizer of f(y)=d(x,y) is y=E[x], satisfies iff f(.) is convex;
		- d(x, y) >= 0 implies f(x) convex;
		- **Assymetry**: in general D(x,y) != D(y,x);
	- Legacy:
		- A Banerjee, X Guo, and H Wang. On the optimality of conditional expectation as a Bregman predictor. TIT'05
		- A Banerjee, et al. Clustering with Bregman divergences. JMLR'05
- Hausdorff distance: Let K, L ⊆ Rd be two sets.
	- dH(K, L) := inf {λ ≥ 0 | K ⊆ L + λB(0, 1), L ⊆ K + λB(0, 1)}
- Squared Mahalanobis distance
- Matrix:
	- von Neumann divergence
- Empirical distribution:
	- **MMD** (Maximum Mean Discrepancy): A. Gretton, K. M. Borgwardt, M. J. Rasch, B. Scholkopf, and A. Smola. A kernel two-sample test. JMLR'02
		- https://www.zhihu.com/question/288185961/answer/459888198

## Distribution Distance
- Fisher Divergence: Johnson, O. Information theory and the central limit theorem, 2004.
	- F(p,q)=Ex||∇logp(x)−∇logq(x)||^2,
- Alpha divergence:
	- Dα(p||q) = 4/(1-α^2)[1-∫p(x)^(1+α)/2 q(x)^(1-α)/2 dx]
	- General, α -> 1, KL(p|q); α -> -1, KL(q|p); α=-, Hellinger;
- Hellinger distance:
	- D(p||q) = ∫(p(x)^.5 - q(x)^.5)^2 dx
- KSD: Q. Liu, J. Lee, and M. Jordan. A kernelized stein discrepancy for goodness-of-fit tests. ICML'16
	- S(p, q) = Ex,x'∼p[δq,p(x)k(x, x')δq,p(x')]
	- where δq,p(x) = sq(x) − sp(x) is the score difference;
	- Su(p,q) = 1/n(n-1) Σij uq(xi,xj)
