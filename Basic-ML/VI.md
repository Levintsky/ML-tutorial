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
<img src="/Basic-ML/images/em1.png" alt="drawing" width="600"/>

## VI Basics:
- MCMC:
	- Hard to do m-step, sample some z and average
- VI, ELBO:
	- KL(q(z) | p(z|x)) = E(log q(z)) - E(log p(z,x)) + log p(x)
	- ELBO(q) = E(log p(z, x)) - E(log q(z))

## Mean Field
<img src="/Basic-ML/images/mean-field1.png" alt="drawing" width="200"/>

- LDA:

## MCMC with Mini-Batch
- **SGLD**: Max Welling, Yee Whye Teh. Bayesian Learning via Stochastic Gradient Langevin Dynamics. ICML'11
	- Insight: a new framework for learning from large scale datasets based on iterative learning from small mini-batches.
	- By adding the right amount of noise to a standard stochastic gradient optimization algorithm we show that the iterates will converge to samples from the true posterior distribution as we anneal the stepsize;
	- Problem setup: estimate posterior p(W|D)
	- Application: a mixture of Gaussians, logistic regression and ICA with natural gradients
- **SGHMC**: Tianqi Chen, Emily Fox, Carlos Guestrin. Stochastic Gradient Hamiltonian Monte Carlo. ICML'14