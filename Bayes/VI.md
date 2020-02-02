# EM, Variational Inference

## Summaries and Tutorials
- David Blei. Variational Inference: A Review for Statisticians, 2018
	- ELBO (Evidence Lower-Bound)

## Mixture Models, EM (PRML, Chap 9)
- K-means;
- Mixture of Gaussian;
	<img src="/Bayes/images/VI/gmm.png" alt="drawing" width="400"/>
- {X, Z}, Because we cannot use the complete-data log likelihood, we consider instead its **expected value** under the posterior distribution of the latent variable, which corresponds (as we shall see) to the E step of the EM algorithm;
	<img src="/Bayes/images/VI/mixture-em.png" alt="drawing" width="400"/>
- EM for Bayesian linear regression: converge to the same result with direct method:
	<img src="/Bayes/images/VI/em-bayes-lr-1.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/VI/em-bayes-lr-2.png" alt="drawing" width="400"/>
- General EM:\
	<img src="/Bayes/images/VI/em-elbo-1.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/VI/em-elbo-2.png" alt="drawing" width="400"/>
-  The generalized EM, or GEM, algorithm addresses the problem of an intractable M step. Instead of aiming to maximize L(q, θ) with respect to θ, it seeks instead to change the parameters in such a way as to increase its value;

## Approximate Inference (PRML, Chap 10)
- Basics: Many problems can be expressed in terms of an optimization problem in which the quantity being optimized is a functional. This is done by restricting the range of functions over which the optimization is performed. Our goal is to find an approximation for the posterior distribution p(Z\|X) as well as for the model evidence p(X).
- Factorized model: mean field;\
	<img src="/Bayes/images/VI/mean-field-1.png" alt="drawing" width="300"/>
	<img src="/Bayes/images/VI/mean-field-2.png" alt="drawing" width="450"/>
	<img src="/Bayes/images/VI/mean-field-3.png" alt="drawing" width="350"/>
- E.g.1: EM of GMM with Dirichlet prior on pi (PRML 10.2);
	<img src="/Bayes/images/VI/em-gmm-1.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/VI/em-gmm-2.png" alt="drawing" width="400"/>
- E.g.2: EM of linear regression: a gamma prior alpha ~ gamma(a0, b0) for weight precision;
	<img src="/Bayes/images/VI/em-lr-1.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/VI/em-lr-2.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/VI/em-lr-3.png" alt="drawing" width="400"/>
	- Assume variational factorized posterior: q(w, alpha) = q(w) q(alpha)
	- Prior alpha:\
		<img src="/Bayes/images/VI/em-lr-4.png" alt="drawing" width="400"/>
	- Weight w:\
		<img src="/Bayes/images/VI/em-lr-5.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/VI/em-lr-6.png" alt="drawing" width="400"/>
	- Predict:
		<img src="/Bayes/images/VI/em-lr-7.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/VI/em-lr-8.png" alt="drawing" width="400"/>
- E.g.3: exponential family;
	- Model: (x, z) with latent z, conjagate prior on nita
		<img src="/Bayes/images/VI/em-exp-family-1.png" alt="drawing" width="400"/>
	- Variational factorized posterior: q(z, nita) = q(z) q(nita)
	- q(z)
		<img src="/Bayes/images/VI/em-exp-family-2.png" alt="drawing" width="400"/>
	- q(nita)
		<img src="/Bayes/images/VI/em-exp-family-3.png" alt="drawing" width="400"/>
- Local variational method:
	<img src="/Bayes/images/VI/local-vi.png" alt="drawing" width="400"/>

## Mixture of Experts
- Important property:
	- **log-sum-exp is Convex**, so Z(w) is always convex for mixture models
- p(x) = sum_z p(x,z)
- EM:
	- E-step: p(z), (In VBEM, will be q(z))
	- M-step: argmax_theta Q(theta, theta_old)
- EM Theory:
	<img src="/Bayes/images/VI/em1.png" alt="drawing" width="600"/>
- Modern:
	- Benefits of over-parameterization with EM. NIPS'18

## VI Basics:
- MCMC:
	- Hard to do m-step, sample some z and average
- VI, ELBO:
	- KL(q(z) | p(z|x)) = E(log q(z)) - E(log p(z,x)) + log p(x)
	- ELBO(q) = E(log p(z, x)) - E(log q(z))

## Mean Field
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
		<img src="/Bayes/images/VI/sgld.png" alt="drawing" width="400"/>
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