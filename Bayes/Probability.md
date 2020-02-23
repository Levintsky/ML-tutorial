# Probability

## Discrete (Kevin Murphy 2.3)
- Binary:
	- Bernoulli
		- E(x) = p
		- V(x) = p(1-p)
	- Binomial: conjugacy prior is Beta \
		- E(x) = np
		- V(x) = np(1-p) \
			<img src="/Bayes/images/prob/binomial.png" alt="drawing" width="300"/>
		- Beta: **conjugacy prior** of binomial \
			<img src="/Bayes/images/prob/beta1.png" alt="drawing" width="350"/>\
			<img src="/Bayes/images/prob/beta2.png" alt="drawing" width="350"/>
	- Conjugacy: posterior of the same functional form with prior
		<img src="/Bayes/images/prob/binomial-post.png" alt="drawing" width="400"/>
- Multinomial:
	- Multinomial: \
		<img src="/Bayes/images/prob/multinomial.png" alt="drawing" width="400"/>
	- Dirichlet: **conjugacy** of multinomial \
		<img src="/Bayes/images/prob/dirichlet.png" alt="drawing" width="350"/>	
- Poisson:
	- Physical meaning: x ~ Binomial(n, p), n very large, n x p = labmda, then k appearancd observes Poisson
	- p(k) = lambda^k exp(-lambda)/k!
	- E(x) = lambda
	- V(x) = lambda \
	<img src="/Bayes/images/prob/poisson.png" alt="drawing" width="400"/>

## Continuous (Kevin Murphy 2.4)
- Uniform U(a, b)
	- E(x) = (a+b)/2
	- V(x) = (b-a)^2/12
- Exponential: p(x) = exp(-x/theta) / theta
	- E(x) = theta
	- V(x) = theta^2
- Laplace:\
	<img src="/Bayes/images/prob/laplace.png" alt="drawing" width="400"/>
- Gamma:\
	<img src="/Bayes/images/prob/gamma-1.png" alt="drawing" width="300"/>\
	<img src="/Bayes/images/prob/gamma-2.png" alt="drawing" width="300"/>
	- Exponential, Erlang and Chi-square are special case of Gamma:
		<img src="/Bayes/images/prob/gamma-3.png" alt="drawing" width="450"/>
	- Inverse Gamma:\
		<img src="/Bayes/images/prob/igamma.png" alt="drawing" width="450"/>
- Beta: **conjugacy prior** of binomial \
	<img src="/Bayes/images/prob/beta1.png" alt="drawing" width="300"/>\
	<img src="/Bayes/images/prob/beta2.png" alt="drawing" width="300"/>

## Gaussian (PRML, Chap 2; Kevin Murphy, Chap 4)
- Definition: \
	<img src="/Bayes/images/prob/gaussian.png" alt="drawing" width="400"/>
- Eigen value and vector of covariance matrix; with y=U(x-mu) \
	<img src="/Bayes/images/prob/gaussian-eigen0.png" alt="drawing" width="200"/>\
	<img src="/Bayes/images/prob/gaussian-eigen1.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/prob/gaussian-eigen2.png" alt="drawing" width="400"/>
- Conditional, precision matrix;
	- Lambda = inv(Cov);\
	<img src="/Bayes/images/prob/gaussian-joint1.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/prob/gaussian-joint2.png" alt="drawing" width="400"/>
- Special case: joint 2-dim Gaussian distribution: \
	<img src="/Bayes/images/prob/gaussian-2d.png" alt="drawing" width="400"/>
- **Gaussian Bayes Theorem**: x, y=Ax+b, x ~ N(mu, Simga) with precision matrix Lambda, y ~ N(Ax+b, L^-1), with L as the precision matrix; then analyzing variable z = [x;y], we could have:
	<img src="/Bayes/images/prob/gaussian-bayes-the.png" alt="drawing" width="400"/>
- MLE for Gaussian: \
	<img src="/Bayes/images/prob/gaussian-mle.png" alt="drawing" width="200"/>
- Posterior inference (PRML, Chap 2; focus on **Precision**):
	- Single var, variance known, for mean mu as **Gaussian**(mu0, sigma0): \
		<img src="/Bayes/images/prob/gaussian-inf-1.png" alt="drawing" width="400"/>
	- Single var, mean known, infer **precision** lambda=1/sigma^2 as **Gamma**(a, b): \
		<img src="/Bayes/images/prob/gaussian-inf-2.png" alt="drawing" width="400"/>
		- Gamma distribution:
			- E(x) = a / b
			- Var(x) = a / b^2 \
			<img src="/Bayes/images/prob/gamma.png" alt="drawing" width="300"/>
		<img src="/Bayes/images/prob/gaussian-inf-3.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/prob/gaussian-inf-4.png" alt="drawing" width="400"/>
	- Single var, both mean and precision unknown: **Gaussian-Gamma**;
		- Likelihood: \
			<img src="/Bayes/images/prob/gaussian-inf-5.png" alt="drawing" width="400"/>
		- Prior take the same form with (c, d, beta); \
			<img src="/Bayes/images/prob/gaussian-inf-6.png" alt="drawing" width="400"/>
		- With mu0 = c/beta, a = 1 + beta/2, b = d - c^2/2beta; \
			<img src="/Bayes/images/prob/gaussian-inf-7.png" alt="drawing" width="400"/>
	- Multi var, both mean and precision unknown; **Gaussian-Wishart**\
		<img src="/Bayes/images/prob/wishart.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/prob/gaussian-inf-8.png" alt="drawing" width="400"/>
	- We know x ~ N(mu, tau^-1) has conjagate Gamma prior Gam(tau|a, b). We integrate out precision tau, marginal distribution of p(x\|mu, a, b) is a **student-t** distribution: \
		<img src="/Bayes/images/prob/gaussian-inf-9.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/prob/gaussian-inf-10.png" alt="drawing" width="400"/>
- Posterior inference (Kevin Murphy, Chap 4.6; focus on **Covariance**):
	- x ~ Gamma; 1/x ~ Inverse-Gamma; single var case:\
		<img src="/Bayes/images/prob/gaussian-inf-11.png" alt="drawing" width="400"/>
	- Inverse of Wishart: I-Wishart;
		<img src="/Bayes/images/prob/gaussian-inf-12.png" alt="drawing" width="400"/>
	- Posterior of Covariance: Inverse-Wishart;
	- Multi var, both mean and variance unknown: **NIW** (Normal-inverse-wishart);
		- Likelihood:\
			<img src="/Bayes/images/prob/gaussian-inf-13.png" alt="drawing" width="400"/>
		- Prior:\
			<img src="/Bayes/images/prob/gaussian-inf-14.png" alt="drawing" width="400"/>
		- Posterior:\
			<img src="/Bayes/images/prob/gaussian-inf-15.png" alt="drawing" width="400"/>
	- Posterior predictive:
		- Definition:\
			<img src="/Bayes/images/prob/gaussian-inf-16.png" alt="drawing" width="400"/>
		- NIX (normal inverse chi-squared):\
			<img src="/Bayes/images/prob/gaussian-inf-17.png" alt="drawing" width="400"/>\
			<img src="/Bayes/images/prob/gaussian-inf-18.png" alt="drawing" width="400"/>
	- Bayesian t-test:\
		<img src="/Bayes/images/prob/t-test.png" alt="drawing" width="400"/>

## Periodic
- On a circle: average angle \
	<img src="/Bayes/images/prob/periodic-1.png" alt="drawing" width="200"/>
- Definition: distribution with period 2pi \
	<img src="/Bayes/images/prob/periodic-2.png" alt="drawing" width="200"/>
- With (x1, x2) and (mu1, mu2) as prior, we have: \
	<img src="/Bayes/images/prob/periodic-3.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/prob/periodic-4.png" alt="drawing" width="400"/>
- Mises distribution:\
	<img src="/Bayes/images/prob/periodic-5.png" alt="drawing" width="400"/>

## Exponential Family
- Definition: h(x)g(eta)exp{eta \* u(x)}; \
	<img src="/Bayes/images/prob/exp-family-1.png" alt="drawing" width="300"/>
- General form for a lot of distributions: Bernoulli, Gaussian;
- Sufficient statistics: u(x); \
	<img src="/Bayes/images/prob/exp-family-2.png" alt="drawing" width="400"/>
- Congugate prior and posterior: \
	<img src="/Bayes/images/prob/exp-family-3.png" alt="drawing" width="350"/>\
	<img src="/Bayes/images/prob/exp-family-4.png" alt="drawing" width="400"/>

## Multidimensional
- Joint distribution
- Covariance Matrix
	- Cov(X, Y) = E[(X-EX)(Y-EY)]
- Pearson correlation coefficient
	- rho(X, Y) = cov(X, Y) / std(X)std(Y)
- Marginal distribution
- Conditional distribution
- Distribution
	- Z=X+Y (Convolution): fx * fy
	- Y/X: int |x|fx(x)fy(xz) dx
	- XY: int 1/|x| fx(x)fy(z/x) dx
	- max(X,Y): Fz(z)=Fx(z)Fy(z)

## Measure Distance between Distributions
- KL
- f-duvergence
- IPM

## Bounds, Theory
- Weak law of large numbers (Khinchin's law)
	- the sample average converges in probability towards the expected value\
		<img src="/Basic-ML/images/law-weak.png" alt="drawing" width="400"/>
- Chebyshev\
	<img src="/Basic-ML/images/chebyshev.png" alt="drawing" width="600"/>
- Central Limit:
	- X i.i.d., with mean, std
	- (sum(x) - n mu) / sqrt(n)std close to N(0, 1)\
		<img src="/Basic-ML/images/law-central-limit.png" alt="drawing" width="600"/>