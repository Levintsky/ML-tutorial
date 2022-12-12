# Optimization Theory

## 0-th Order GD
- Chi Jin, Lydia T. Liu, Rong Ge, Michael I. Jordan. On the Local Minima of the Empirical Risk. NIPS'18
	- Insight: propose an optimization algorithm (ZPSGD), Gaussian smoothing 0-order grad;
	- Zero-th order Perturbed Stochastic Gradient Descent;
		- Sample m i.i.d. Gaussian (zt1, zt2, ..., ztm) ~ N(0, σ^2I)
		- Estimate gradient: g(xt) = ∑ zti[f(xt+zti)-f(xt)]/(mσ^2)
		- Update: xt+1 = xt - η(gt(xt) + ξt), ξt uniformly ∼ B0(r)
	- Main result:
		- Assump: F: B-bounded, l-gradient Lipschitz, ρ-Hessian Lipschitz;
		- find an ε-second-order stationary point of F with only access to values of f.

## Misc
- Brian Axelrod, Ilias Diakonikolas, Alistair Stewart, Anastasios Sidiropoulos, Gregory Valiant. A Polynomial Time Algorithm for Log-Concave Maximum Likelihood via Locally Exponential Families. NIPS'18
- Chizat, Lenaic, and Francis Bach. On the global convergence of gradient descent for over-parameterized models using optimal transport. NIPS'18
