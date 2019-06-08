# Data Science Summary

## Summaries
- https://segmentfault.com/a/1190000004411616
- https://www.zhihu.com/question/23149768

## Sampling
- Histogram
- Box plot
	- Quantile: x1 < ... < xn
		- x[ceil(np)] if np is not an integer
		- 0.5 (x[np]+x[np+1]) if np is an integer
	- Min, Q1, Median, Q3, Max
<img src="/Basic-ML/images/box-plot.png" alt="drawing" width="300"/>

- Descriptive Statistics, Predicative Statistics
	- Mean
	- Median
	- K-th order moments
	- Standard Deviation
	- Variance
- Empirical distribution
- Chi-square:
	- X^2 - Gamma(1/2, 2)
	- X1, X2, ... independent, according to additivity of Gamma distribution, we have sum(X^2) - Gamma(n/2, 2)
	- X - Gamma(a, theta), Y - Gamma(b, theta), then X+Y - Gamma(a+b, theta)
	- E(chi(n)) = n
	- V(chi(n)) = 2n
<img src="/Basic-ML/images/chi-square.png" alt="drawing" width="600"/>

- T-distribution
	- X - N(0, 1), Y - chi(n)
	- t = X / sqrt(Y/N), t - t(n)
	- n large, closed to normal
<img src="/Basic-ML/images/t-distribution.png" alt="drawing" width="600"/>

- F-distribution
	- U - chi(n1), V - chi(n2)
	- F = U/n1 / V/n2
<img src="/Basic-ML/images/f-distribution.png" alt="drawing" width="600"/>

## More Gaussian
- Distribution of mean
	- Suppose variance known, average of samples as an estimate of mean: Gaussian
<img src="/Basic-ML/images/gaussian-mean.png" alt="drawing" width="600"/>

- Distribution of Variance
	- Suppose X-bar and S^2 are sample mean and variance
	- (n-1)S^2 / std^2 observes chi(n-1)
	- X-bar and S^2 are independent
<img src="/Basic-ML/images/gaussian-var.png" alt="drawing" width="600"/>

- Empirical of (x-mean)/std: t-distribution
<img src="/Basic-ML/images/gaussian-meanvar.png" alt="drawing" width="600"/>

## Estimation
- Confidence interval:
	- p(theta1 < theta < theta2) = 1-alpha, out of interval: alpha
	- alpha = 0.05, Gaussian: +/-1.96sigma
- Estimate the interval of mean and variance of Gaussian
	- Sigma known: Gaussian
<img src="/Basic-ML/images/gaussian-mean-est1.png" alt="drawing" width="200"/>

	- Sigma unknown: t-distribution
<img src="/Basic-ML/images/gaussian-mean-est2.png" alt="drawing" width="200"/>
<img src="/Basic-ML/images/gaussian-mean-est3.png" alt="drawing" width="450"/>

	- Variance estimation: chi
<img src="/Basic-ML/images/gaussian-var-est.png" alt="drawing" width="500"/>
- Moment
- MLE
- Criteria
	- Unbiased
	- Smaller vaiance
	- Convergence
- Confidence Interval
	- Gaussian
		- std known, estimate mean: Gaussian
<img src="/Basic-ML/images/gaussian-mean-ci1.png" alt="drawing" width="200"/>

		- std unknown, estimate mean: student-t
<img src="/Basic-ML/images/gaussian-mean-ci2.png" alt="drawing" width="600"/>

		- estimate var: chi
<img src="/Basic-ML/images/gaussian-var-ci.png" alt="drawing" width="400"/>

		- Difference of two Gaussian
	- Bernoulli 0-1, n samples approximates as Gaussian
<img src="/Basic-ML/images/bernoulli-ci1.png" alt="drawing" width="500"/>
<img src="/Basic-ML/images/bernoulli-ci2.png" alt="drawing" width="600"/>

- Single-side CI

## Hypothesis Testing
- Type I, II error
- Testing of Normal distribution summary:
<img src="/Basic-ML/images/gaussian-test1.png" alt="drawing" width="600"/>
<img src="/Basic-ML/images/gaussian-test2.png" alt="drawing" width="600"/>

	- **Z-test**: known sigma, test mu
		- (mean-mu0)/(sigma/sqrt(n))
	- **t-test**: known sigma, test mu
<img src="/Basic-ML/images/t-test.png" alt="drawing" width="500"/>

	- t-test: difference of two normal with same unknown variance but different mean.
<img src="/Basic-ML/images/t-test2.png" alt="drawing" width="500"/>

	- Testing of Variance
		- Chi-square test: variance of some samples
		- F-test: Given two set of samples from (mean1, var1), (mean2, var2), test if var1 >=< var2?
- Distribution fitting test
	- **Chi-square-test** of k discrete non-overlapping events of
		- H0: x observes F(x)
		- H1: x does not observe F(x)
		- x observes chi-square(k-1) distribution
<img src="/Basic-ML/images/chi-square-test.png" alt="drawing" width="500"/>

	- Chi-square test of dividing continuous events into k bins for a distribution with r parameters;
<img src="/Basic-ML/images/chi-square-test2.png" alt="drawing" width="500"/>

- Skewness, Kurtosis
	- 3rd and 4th moments
<img src="/Basic-ML/images/Skewness.png" alt="drawing" width="450"/>

	- For normal distribution we have:
<img src="/Basic-ML/images/gaussian-skew.png" alt="drawing" width="450"/>

- Rank sum test:
	- f1(x) = f2(x+a) test a >=< 0?
	- rank x(1) < x(2) < ... < x(n)

- P-Value test:
	- e.g., 100 coins, 90H/10T, fair?
	- All more extreme cases
	- p-value=2(p(90H)+p(91H)+...)
	- Consider: p(10H)+p(9H)
	- p < alpha, reject

## Outlier, Anomaly

## ANOVA (Analysis of Variance)

## Causality, Relevance