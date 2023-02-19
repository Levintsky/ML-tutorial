# Black-Box Optimization (Gradient-Free)

## Basics
- Build a model f() explicitly
	- Quadratic: NO-9.2
- Estimate gradient

## Derivative-Free Optimization
- NO-Chap-9
	- 9.1 Finite Difference and Noise
		- f(x) = h(x) + φ(x), φ(x): noise
		- η(x; ε) = sup|φ(z)|
		- Lemma-9.1. ∇^h(x) L-Lipschitz, central derivative:
			- |∇εf(x)-∇h(x)| ≤ Lε^2 + η(x; ε)/ε
	- 9.2 Model-Based Methods
		- Algorithm:
			- Form a quadratic model by interpolation:
				- mk(xk + p) = c + gT p + 1/2 p'Gp
			- Solve trust region minimization:
				- minp mk(xk+p) s.t. |p|≤Δ
			- Ratio: actual/predicted reduction
				- ρ = (f(xk)−f(xk+))/(m(xk)−m(xk+))
			- If sufficient ρ ≥ η:
				- Add in xk+, enlarge trust-region Δ;
			- If not:
				- Reason 1: interpolation set inaccurate, monitor condition number;
				- Reason 2: trust-region Δ too large;
		- Interpolation and Polynomial Bases
		- Updating the interpolation set
	- 9.3 Coodinate and Pattern Search Methods
		- Coordinate search: Cycle through coordinates with other fixed;
	- 9.4 A Conjugate-Direction Method
		- Insight: two parallel lines l1(α)=x1+αp and l2(α)= x2+αp with optimal step size for x1∗, x2∗, then x1∗ − x2∗ is conjugate to p.
		- DFO CG (1-step from xk to xk+1): search in each direction, then get CG direction;
			- pi = ei; (standard coord direction)
			- zi = xk;
			- Calculate αj s.t. f(zj+αj pj) is minimized
			- zj+1 ← zj + αjpj;
			- Last step pn ← zn+1 − z1; (conjugate direction)
			- Calculate αn so that f(zn+1+αn pn) is minimized;
			- xk+1 ←zn+1 + αnpn;
	- 9.5 Nelder-Mead Method
		- Keep track of current n-best solutions to form a simplex;
		- Replace worst a better;
	- 9.6 Implicit filtering
		- Variant of steepest descent + line search;

## Estimate Gradient
- C Jin, L Liu, R Ge, M Jordan. On the Local Minima of the Empirical Risk. NIPS'18
	- Insight: propose an optimization algorithm (ZPSGD), Gaussian smoothing 0-order grad;
	- Zero-th order Perturbed Stochastic Gradient Descent;
		- Sample m i.i.d. Gaussian (zt1, zt2, ..., ztm) ~ N(0, σ^2I)
		- Estimate gradient: g(xt) = ∑ zti[f(xt+zti)-f(xt)]/(mσ^2)
		- Update: xt+1 = xt - η(gt(xt) + ξt), ξt uniformly ∼ B0(r)
	- Main result:
		- Assump: F: B-bounded, l-gradient Lipschitz, ρ-Hessian Lipschitz;
		- find an ε-second-order stationary point of F with only access to values of f.

## Evoluation Strategy
- https://lilianweng.github.io/lil-log/2019/09/05/evolution-strategies.html
- Basics:
	- Black-box optimization, gradient free;
	- Simple Gaussian-ES:
		- θ = (μ, σ) ~ μ + σ N(0, I)
		- Sample population, select a top subset of λ samples, elite set;
		- Estimate new mean and std;
	- **CMA-ES** (Covariance Matrix Adaptation-ES): 
		- Insight: θ = (μ, σ^2C) ~ μ + σ N(0, C), Stochastic version of BFGS (quasi-Newton);
			- Small number of samples to estimate covariance, so complicated rules to adapt;
		- Sample xt = mt + σt Ct^(1/2) zt, zt ~ N(0,I)
		- Rank the solutions, select the best λ performers to get new mean;
			- μt+1 = μt + α_μ 1/λ Σ_i=1..λ (xi.t+1-μt)
		- Update path with Polyak averaging of update compensated with C^(-1/2):
			- p_σ,t+1 = (1-α_σ)p_σ,t + √(α_σ(2-α_σ)λ) Ct^(-1/2) (μt+1-μt)/σt
		- Cumulative step-size adaptation to update σt;
			- σt+1 = σt exp(α_σ/d_σ(pσ-1))
		- Update rank-1 and rank-μ to update covariance matrix;
	- A population of parameter vectors ("genotypes") is perturbed "mutated", and their objective function value ("fitness") is evaluated.
	- The highest scoring parameter vectors are then recombined to form the population for the next generation, and this procedure is iterated until the objective is fully optimized;
	- Successful in optimization in low-medium dimension;
- Legacy:
	- I. Rechenberg and M. Eigen. Evolutionsstrategie: Optimierung Technischer Systeme nach Prinzipien der Biologischen Evolution. 1973
	- H Schwefel. Numerische optimierung von computer-modellen mittels der evolutionsstrategie. 1977
	- J Schmidhuber and J Zhao. Direct policy search and uncertain policy evaluation. 1998
	- S Risi and J Togelius. Neuroevolution in games: State of the art and open challenges. 2015
- N Hansen and A Ostermeier. Completely derandomized self-adaptation in evolution strategies. 2001
- N Hansen. The CMA Evolution Strategy: A Tutorial. 2016
- **NES**: natural ES;
	- Similar to REINFORCE, use func-eval f(x) as reward;
		- E_x ~ p(θ)[f(x)∇logp(x;θ)]; enhance the probability of sampling good x;
	- θ = θ + α F^(-1)∇J
	- D Wierstra, T Schaul, J Peters, and J Schmidhuber. Natural evolution strategies. 2008
	- D Wierstra, T Schaul, T Glasmachers, Y Sun, J Peters, and J Schmidhuber. Natural evolution strategies. JMLR'14
- D Ha. A Visual Guide to Evolution Strategies. blog.otoro.net. Oct 2017.
	- http://blog.otoro.net/2017/10/29/visual-evolution-strategies/
- PBT:
	- M Jaderberg, et. al. Population Based Training of Neural Networks, NeurIPS'17
	- M Jaderberg, et. al. Human-level performance in 3D multiplayer games with population-based reinforcement learning. Science'19

## Random Search, Grid Search
- J. Bergstra and Y. Bengio. Random search for hyperparameter optimization. JMLR'12
- L Li, K Jamieson, G DeSalvo, A Rostamizadeh, A Talwalkar. Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimization, ICLR'17, JMLR'18
	- https://www.argmin.net/2016/06/23/hyperband/
