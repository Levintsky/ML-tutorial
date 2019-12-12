# Probability

## Discrete
- Bernoulli
	- E(x) = p
	- V(x) = p(1-p)
- Poisson:
	- Physical meaning: x ~ Binomial(n, p), n very large, n x p = labmda, then k appearancd observes Poisson
	- p(k) = lambda^k exp(-lambda)/k!
	- E(x) = lambda
	- V(x) = lambda
<img src="/Basic-ML/images/poisson.png" alt="drawing" width="600"/>

## Continuous
- Uniform U(a, b)
	- E(x) = (a+b)/2
	- V(x) = (b-a)^2/12
- Exponential: p(x) = exp(-x/theta) / theta
	- E(x) = theta
	- V(x) = theta^2
- Gaussian Distribution

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
- Joint Gaussian distribution
<img src="/Basic-ML/images/gaussian-2d.png" alt="drawing" width="500"/>
<img src="/Basic-ML/images/Gaussian.png" alt="drawing" width="600"/>

## Bounds, Theory
- Weak law of large numbers (Khinchin's law)
	- the sample average converges in probability towards the expected value
<img src="/Basic-ML/images/law-weak.png" alt="drawing" width="600"/>

- Chebyshev
<img src="/Basic-ML/images/chebyshev.png" alt="drawing" width="600"/>

- Central Limit:
	- X i.i.d., with mean, std
	- (sum(x) - n mu) / sqrt(n)std close to N(0, 1)
<img src="/Basic-ML/images/law-central-limit.png" alt="drawing" width="600"/>