# EM, Variational Inference

## Summaries and Tutorials
- David Blei. Variational Inference: A Review for Statisticians, 2018
	- ELBO (Evidence Lower-Bound)

## Mixture of Experts
- Important property:
	- **log-sum-exp is Convex**, so Z(w) is always convex for mixture models
- p(x) = sum_z p(x,z)
- EM:
	- E-step: p(z), (In VBEM, will be q(z))
	- M-step: argmax_theta Q(theta, theta_old)
- EM Theory:
	<img src="/Basic-ML/images/VI/em1.png" alt="drawing" width="600"/>
- Modern:
	- Benefits of over-parameterization with EM. NIPS'18

## VI Basics:
- MCMC:
	- Hard to do m-step, sample some z and average
- VI, ELBO:
	- KL(q(z) | p(z|x)) = E(log q(z)) - E(log p(z,x)) + log p(x)
	- ELBO(q) = E(log p(z, x)) - E(log q(z))

## Mean Field
- Mean field\
	<img src="/Basic-ML/images/VI/mean-field1.png" alt="drawing" width="200"/>
- LDA:

## MCMC with Mini-Batch
- Physics Background:
	- Lagrange Mechanics: q as coordinates, v=dq/dt as velocity, then we have Euler-Lagrange equation: dL/dq - d(dL/dv)/dt=0, Lagrangian L satisifying this equation could be L=mv^2/2-V(q), with V as the potential energy;
	- Legendre Transform: K=mv^2/2, then the slope p; applying duality to Lagrange and maximum, T(v) = mv^2/2
	- Hamilton: H=pq-L (Legendre), H(q,p)=T(p)+V(q); energy conservation: dH/dt=0 
	- T(p) or K(p): kinetic energy; p^TM^(-1)p, where M is mass matrix;
	- U(q) or V(q): potential energy;
	- Equation of motion: dqi/dt=dH/dpi, dpi/dt=-dH/dqi;
- **HMC**: MCMC using Hamiltonian dynamics. Radford M. Neal 2012
	- https://blog.csdn.net/qy20115549/article/details/54561643
- **SGLD**: Max Welling, Yee Whye Teh. Bayesian Learning via Stochastic Gradient Langevin Dynamics. ICML'11
	- Insight: a new framework for learning from large scale datasets based on iterative learning from small mini-batches.
	- https://github.com/henripal/sgld
	- A very good resource: https://docs.google.com/presentation/d/1jDXcH7jcnr1SoWMaH6qZqgZJxvvoqvifs6xk65KEzN0/edit#slide=id.p
	- By adding the right amount of noise to a standard stochastic gradient optimization algorithm we show that the iterates will converge to samples from the true posterior distribution as we anneal the stepsize;
	- Problem setup: estimate posterior p(W|D)
	- Application: a mixture of Gaussians, logistic regression and ICA with natural gradients\
		<img src="/Basic-ML/images/VI/sgld.png" alt="drawing" width="400"/>
- **SGHMC**: Tianqi Chen, Emily Fox, Carlos Guestrin. Stochastic Gradient Hamiltonian Monte Carlo. ICML'14
- Henri Palacci, Henry Hess. Scalable Natural Gradient Langevin Dynamics in Practice. ICML Workshop 2018

## Theory
- Theoretical guarantees for EM under misspecified Gaussian mixture models. NIPS'18

## Unclassified
- DropMax: Adaptive Variational Softmax. NIPS'18
- Latent Alignment and Variational Attention. NIPS'18
- Topic Modeling
	- Distilled Wasserstein Learning for Word Embedding and Topic Modeling (Lawrence Carin) NIPS'18
	- Dirichlet belief networks for topic structure learning NIPS'18
- Stein Variational Gradient Descent as Moment Matching NIPS'18
- Improving Explorability in Variational Inference with Annealed Variational Objectives (MILA) NIPS'18
- Mean-field theory of graph neural networks in graph partitioning NIPS'18
- Regret bounds for meta Bayesian optimization with an unknown Gaussian process prior (MIT) NIPS'18
- Eric Xing. DAGs with NO TEARS: Continuous Optimization for Structure Learning, NIPS'18
- GPyTorch: Blackbox Matrix-Matrix Gaussian Process Inference with GPU Acceleration, NIPS'18
- Coupled Variational Bayes via Optimization Embedding (Le Song) NIPS'18
- Discretely Relaxing Continuous Variables for tractable Variational Inference NIPS'18
- Cluster Variational Approximations for Structure Learning of Continuous-Time Bayesian Networks from Incomplete Data NIPS'18
- A Stein variational Newton method NIPS'18
- Wasserstein Variational Inference NIPS'18
- Variational Inference with Tail-adaptive f-Divergence NIPS'18
- Boosting Black Box Variational Inference NIPS'18
- Using Large Ensembles of Control Variates for Variational Inference NIPS'18
- Streamlining Variational Inference for Constraint Satisfaction Problems NIPS'18
- Importance Weighting and Variational Inference NIPS'18
- Orthogonally Decoupled Variational Gaussian Processes NIPS'18
- Improving Explorability in Variational Inference with Annealed Variational Objectives NIPS'18
- Amortized Inference
	- Amortized Inference Regularization. NIPS'18
	- A General Method for Amortizing Variational Filtering. NIPS'18
	- **Faithful Inversion of Generative Models for Effective Amortized Inference**. NIPS'18