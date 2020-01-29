# Probability

## Discrete
- Binary:
	- Bernoulli
		- E(x) = p
		- V(x) = p(1-p)
	- Binomial: \
		- E(x) = np
		- V(x) = np(1-p) \
		<img src="/Bayes/images/prob/binomial.png" alt="drawing" width="400"/>
	- Beta: **conjugacy** of binomial \
		<img src="/Bayes/images/prob/beta1.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/prob/beta2.png" alt="drawing" width="400"/>
	- Conjugacy: posterior of the same functional form with prior
		<img src="/Bayes/images/prob/binomial-post.png" alt="drawing" width="400"/>
- Multinomial:
	- Multinomial: \
		<img src="/Bayes/images/prob/multinomial.png" alt="drawing" width="400"/>
	- Dirichlet: **conjugacy** of multinomial \
		<img src="/Bayes/images/prob/dirichlet.png" alt="drawing" width="400"/>	
- Poisson:
	- Physical meaning: x ~ Binomial(n, p), n very large, n x p = labmda, then k appearancd observes Poisson
	- p(k) = lambda^k exp(-lambda)/k!
	- E(x) = lambda
	- V(x) = lambda \
	<img src="/Bayes/images/prob/poisson.png" alt="drawing" width="400"/>

## Gaussian
- Definition: \
	<img src="/Bayes/images/prob/gaussian.png" alt="drawing" width="400"/>
- Eigen value and vector of covariance matrix; with y=U(x-mu) \
	<img src="/Bayes/images/prob/gaussian-eigen0.png" alt="drawing" width="250"/>\
	<img src="/Bayes/images/prob/gaussian-eigen1.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/prob/gaussian-eigen2.png" alt="drawing" width="400"/>
- Conditional, precision matrix;
	- Lambda = inv(Cov);
	<img src="/Bayes/images/prob/gaussian-joint1.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/prob/gaussian-joint2.png" alt="drawing" width="400"/>
- Joint 2-dim Gaussian distribution: \
	<img src="/Bayes/images/prob/gaussian-2d.png" alt="drawing" width="400"/>
- **Gaussian Bayes Theorem**: x, y=Ax+b, x ~ N(mu, Simga) with precision matrix Lambda, y ~ N(Ax+b, L^-1), with L as the precision matrix; then analyzing variable z = [x;y], we could have:
	<img src="/Bayes/images/prob/gaussian-bayes-the.png" alt="drawing" width="400"/>
- MLE for Gaussian: \
	<img src="/Bayes/images/prob/gaussian-mle.png" alt="drawing" width="250"/>
- Inference:
	- Single var, variance known, for mean mu as **Gaussian**(mu0, sigma0): \
		<img src="/Bayes/images/prob/gaussian-inf-1.png" alt="drawing" width="400"/>
	- Single var, mean known, infer precision lambda=1/sigma^2 as **Gamma**(a, b): \
		<img src="/Bayes/images/prob/gaussian-inf-2.png" alt="drawing" width="400"/>
		- Gamma distribution:
			- E(x) = a / b
			- Var(x) = a / b^2 \
			<img src="/Bayes/images/prob/gamma.png" alt="drawing" width="300"/>
		<img src="/Bayes/images/prob/gaussian-inf-3.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/prob/gaussian-inf-4.png" alt="drawing" width="400"/>
	- Singel var, both mean and precision unknown; \
		- Likelihood: \
			<img src="/Bayes/images/prob/gaussian-inf-5.png" alt="drawing" width="400"/>
		- Prior take the same form with (c, d, beta); \
			<img src="/Bayes/images/prob/gaussian-inf-6.png" alt="drawing" width="400"/>
		- With mu0 = c/beta, a = 1 + beta/2, b = d - c^2/2beta; \
			<img src="/Bayes/images/prob/gaussian-inf-7.png" alt="drawing" width="400"/>
	- Multi var, both mean and precision unknown; \
		<img src="/Bayes/images/prob/wishart.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/prob/gaussian-inf-8.png" alt="drawing" width="400"/>
	- Integrate out precision with Gamma prior Gam(tau|a, b), marginal distribution of x: \
		<img src="/Bayes/images/prob/gaussian-inf-9.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/prob/gaussian-inf-10.png" alt="drawing" width="400"/>

## Periodic
- On a circle: average angle \
	<img src="/Bayes/images/prob/periodic-1.png" alt="drawing" width="400"/>
- Definition: distribution with peorid 2pi \
	<img src="/Bayes/images/prob/periodic-2.png" alt="drawing" width="400"/>
- With (x1, x2) and (mu1, mu2) as prior, we have: \
	<img src="/Bayes/images/prob/periodic-3.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/prob/periodic-4.png" alt="drawing" width="400"/>
- Mises distribution:\
	<img src="/Bayes/images/prob/periodic-5.png" alt="drawing" width="400"/>

## Exponential Family
- Definition: h(x)g(eta)exp{eta \* u(x)}; \
	<img src="/Bayes/images/prob/exp-family-1.png" alt="drawing" width="300"/>
- General form for a lot of distributions: Bernoulli, Gaussian; \
- Sufficient statistics: u(x); \
	<img src="/Bayes/images/prob/exp-family-2.png" alt="drawing" width="400"/>
- Congugate prior and posterior: \
	<img src="/Bayes/images/prob/exp-family-3.png" alt="drawing" width="400"/>
	<img src="/Bayes/images/prob/exp-family-4.png" alt="drawing" width="400"/>

## Continuous
- Uniform U(a, b)
	- E(x) = (a+b)/2
	- V(x) = (b-a)^2/12
- Exponential: p(x) = exp(-x/theta) / theta
	- E(x) = theta
	- V(x) = theta^2

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
		<img src="/Basic-ML/images/law-weak.png" alt="drawing" width="600"/>
- Chebyshev\
	<img src="/Basic-ML/images/chebyshev.png" alt="drawing" width="600"/>
- Central Limit:
	- X i.i.d., with mean, std
	- (sum(x) - n mu) / sqrt(n)std close to N(0, 1)\
		<img src="/Basic-ML/images/law-central-limit.png" alt="drawing" width="600"/>