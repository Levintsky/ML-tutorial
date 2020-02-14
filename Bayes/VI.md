# EM, Variational Inference

## Summaries and Tutorials
- David Blei. Variational Inference: A Review for Statisticians, 2018
	- ELBO (Evidence Lower-Bound)

## Mixture Models, EM (PRML, Chap 9)
- K-means;
- Mixture of Gaussian;\
	<img src="/Bayes/images/VI/gmm.png" alt="drawing" width="300"/>
- {X, Z}, Because we cannot use the complete-data log likelihood, we consider instead its **expected value** under the posterior distribution of the latent variable, which corresponds (as we shall see) to the E step of the EM algorithm;\
	<img src="/Bayes/images/VI/mixture-em.png" alt="drawing" width="400"/>
- EM for Bayesian linear regression: converge to the same result with direct method:
	<img src="/Bayes/images/VI/em-bayes-lr-1.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/VI/em-bayes-lr-2.png" alt="drawing" width="400"/>
- General EM:\
	<img src="/Bayes/images/VI/em-elbo1.png" alt="drawing" width="250"/>\
	<img src="/Bayes/images/VI/em-elbo2.png" alt="drawing" width="400"/>
-  The generalized EM, or GEM, algorithm addresses the problem of an intractable M step. Instead of aiming to maximize L(q, θ) with respect to θ, it seeks instead to change the parameters in such a way as to increase its value;

## Approximate Inference (PRML, Chap 10)
- Basics: Many problems can be expressed in terms of an optimization problem in which the quantity being optimized is a functional. This is done by restricting the range of functions over which the optimization is performed. Our goal is to find an approximation for the posterior distribution p(Z\|X) as well as for the model evidence p(X).
- Factorized model: mean field;\
	<img src="/Bayes/images/VI/mean-field-1.png" alt="drawing" width="300"/>\
	<img src="/Bayes/images/VI/mean-field-2.png" alt="drawing" width="450"/>\
	<img src="/Bayes/images/VI/mean-field-3.png" alt="drawing" width="350"/>
- E.g.1: factorized Gaussian to approximate 2-dimension Gaussian:\
	<img src="/Bayes/images/VI/em-gauss-1.png" alt="drawing" width="400"/>\
	- Iteratively optimize:\
		<img src="/Bayes/images/VI/em-gauss-2.png" alt="drawing" width="400"/>
- E.g.2: Gaussian, factorized prior (mean, precision) for conjugate prior:\
	<img src="/Bayes/images/VI/em-gauss-prior-1.png" alt="drawing" width="400"/>\
	- Assume q(mu, tau) = q(mu) q(tau), we have\
		<img src="/Bayes/images/VI/em-gauss-prior-2.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/VI/em-gauss-prior-3.png" alt="drawing" width="400"/>
- E.g.3: EM of GMM with Dirichlet prior on pi (PRML 10.2), Gaussian-Wishart prior on mean, precision;\
	<img src="/Bayes/images/VI/em-gmm-1.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/VI/em-gmm-2.png" alt="drawing" width="300"/>
- E.g.4: EM of linear regression: a gamma prior alpha ~ gamma(a0, b0) for weight precision; assume q(w, alpha) ~ q(w) q(alpha)
	<img src="/Bayes/images/VI/em-lr-1.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/VI/em-lr-2.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/VI/em-lr-3.png" alt="drawing" width="300"/>
	- Assume variational factorized posterior: q(w, alpha) = q(w) q(alpha)
	- Prior alpha:\
		<img src="/Bayes/images/VI/em-lr-4.png" alt="drawing" width="400"/>
	- Weight w:\
		<img src="/Bayes/images/VI/em-lr-5.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/VI/em-lr-6.png" alt="drawing" width="400"/>
	- Predict:\
		<img src="/Bayes/images/VI/em-lr-7.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/VI/em-lr-8.png" alt="drawing" width="400"/>
- E.g.5: exponential family;
	- Model: (x, z) with latent z, conjagate prior on nita;\
		<img src="/Bayes/images/VI/em-exp-family-1.png" alt="drawing" width="400"/>
	- Variational factorized posterior: q(z, nita) = q(z) q(nita)
	- q(z)\
		<img src="/Bayes/images/VI/em-exp-family-2.png" alt="drawing" width="400"/>
	- q(nita)\
		<img src="/Bayes/images/VI/em-exp-family-3.png" alt="drawing" width="400"/>
- Local variational method, **conjugate function**:\
	<img src="/Bayes/images/VI/local-vi-1.png" alt="drawing" width="400"/>
	- For convex function f(x) and g(lambda), we define its **lower bound**:\
		<img src="/Bayes/images/VI/local-vi-2.png" alt="drawing" width="400"/>
	- For concave funtions, we could get **upper bound**:\
		<img src="/Bayes/images/VI/local-vi-3.png" alt="drawing" width="400"/>
	- Log(logistic) is concave, with upper bound:\
		<img src="/Bayes/images/VI/local-vi-4.png" alt="drawing" width="400"/>
	- Log(logistic) lower bound:\
		<img src="/Bayes/images/VI/local-vi-5.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/VI/local-vi-6.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/VI/local-vi-7.png" alt="drawing" width="400"/>
- E.g.6: variational logistic regression:
- Expectation propagation: the **reverse form KL(p, q)**:
	- We use an exponential family q(z) to approx p(z):\
		<img src="/Bayes/images/VI/ep-1.png" alt="drawing" width="400"/>
	- E.g. Moment matching; the cost:\
		<img src="/Bayes/images/VI/ep-2.png" alt="drawing" width="400"/>

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

## Legacy
- M. J. Wainwright and M. I. Jordan, Graphical models, exponential families, and variational inference, Foundations and Trends in Machine Learning. 2008

## Black-box VI
- John Paisley, David M. Blei, Michael I. Jordan. Variational Bayesian Inference with Stochastic Search. ICML'12
- Rajesh Ranganath Sean Gerrish David M. Blei. Black Box Variational Inference. AISTATS'14
	- Basics behind VAE;
	- ELBO:\
		<img src="/Bayes/images/VI/bb-vi-1.png" alt="drawing" width="600"/>
	- Algorithm:\
		<img src="/Bayes/images/VI/bb-vi-2.png" alt="drawing" width="600"/>

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