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

## VI Basics:
- MCMC:
	- Hard to do m-step, sample some z and average
- VI, ELBO:
	- KL(q(z) | p(z|x)) = E(log q(z)) - E(log p(z,x)) + log p(x)
	- ELBO(q) = E(log p(z, x)) - E(log q(z))

## Mean Field
- Mean field
	<img src="/Basic-ML/images/VI/mean-field1.png" alt="drawing" width="200"/>
- LDA:

## MCMC with Mini-Batch
- **SGLD**: Max Welling, Yee Whye Teh. Bayesian Learning via Stochastic Gradient Langevin Dynamics. ICML'11
	- Insight: a new framework for learning from large scale datasets based on iterative learning from small mini-batches.
	- https://github.com/henripal/sgld
	- A very good resource: https://docs.google.com/presentation/d/1jDXcH7jcnr1SoWMaH6qZqgZJxvvoqvifs6xk65KEzN0/edit#slide=id.p
	- By adding the right amount of noise to a standard stochastic gradient optimization algorithm we show that the iterates will converge to samples from the true posterior distribution as we anneal the stepsize;
	- Problem setup: estimate posterior p(W|D)
	- Background:
		- Lagrange Mechanics: q as coordinates, v=dq/dt as velocity, then we have Euler-Lagrange equation: dL/dq - d(dL/dv)/dt=0, Lagrangian L satisifying this equation could be L=mv^2/2-V(q), with V as the potential energy;
		- Legendre Transform: K=mv^2/2, then the slope p; applying duality to Lagrange and maximum, T(v) = mv^2/2
		- Hamilton: H=pq-L (Legendre), H(q,p)=T(p)+V(q); energy conservation: dH/dt=0 
	- Application: a mixture of Gaussians, logistic regression and ICA with natural gradients\
		<img src="/Basic-ML/images/VI/sgld.png" alt="drawing" width="400"/>
- **SGHMC**: Tianqi Chen, Emily Fox, Carlos Guestrin. Stochastic Gradient Hamiltonian Monte Carlo. ICML'14
- Henri Palacci, Henry Hess. Scalable Natural Gradient Langevin Dynamics in Practice. ICML Workshop 2018