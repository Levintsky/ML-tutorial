# Data Science Summary

## Summaries
- https://segmentfault.com/a/1190000004411616
- https://www.zhihu.com/question/23149768

## Sampling
- Histogram
- Quantile
- Empirical distribution
- Chi-square:
	- E(chi(n)) = n
	- V(chi(n)) = 2n
<img src="/Basic-ML/images/chi-square.png" alt="drawing" width="600"/>

- T-distribution
	- X - N(0, 1), Y - chi(n)
	- t = X / sqrt(Y/N)
<img src="/Basic-ML/images/t-distribution.png" alt="drawing" width="600"/>

- F-distribution
	- U - chi(n1), V - chi(n2)
	- F = U/n1 / V/n2
<img src="/Basic-ML/images/f-distribution.png" alt="drawing" width="600"/>

## More Gaussian
- Distribution of mean
<img src="/Basic-ML/images/gaussian-mean.png" alt="drawing" width="600"/>

- Distribution of Var
<img src="/Basic-ML/images/gaussian-var.png" alt="drawing" width="600"/>

- Empirical of (x-mean)/var
<img src="/Basic-ML/images/gaussian-meanvar.png" alt="drawing" width="600"/>

## Estimation
- Confidence range:
	- p(theta1 < theta < theta2) = 1-alpha, out of range: alpha
	- alpha = 0.05, Gaussian: +/-1.96sigma
- Estimate the range of mean and variance of Gaussian
	- Sigma known: Gaussian
<img src="/Basic-ML/images/gaussian-mean-est1.png" alt="drawing" width="300"/>

	- Sigma unknown: t-distribution
<img src="/Basic-ML/images/gaussian-mean-est2.png" alt="drawing" width="300"/>
<img src="/Basic-ML/images/gaussian-mean-est3.png" alt="drawing" width="450"/>

	- Variance estimation: chi
<img src="/Basic-ML/images/gaussian-var-est.png" alt="drawing" width="300"/>

## P-Value
- e.g., 100 coins, 90H/10T, fair?
	- All more extreme cases
	- p-value=2(p(90H)+p(91H)+...)
	- Consider: p(10H)+p(9H)
	- p < alpha, reject

## Descriptive Statistics, Predicative Statistics
- Mean
- Median
- Range
- Standard Deviation
- Variance

## Outlier, Anomaly

## Probability Theory

## Bayes Theory

## Stochastic Variable

## Some Common Distributions
- Normal (Gaussian) Distribution
- Poisson distribution

## Skewness

## ANOVA (Analysis of Variance)

## Central Limit Theorem

## Monte Carlo Methods

## Hypothesis Testing
- p-value

## Estimation
- Moment
- MLE

## Covriance, Correlation Coefficient, Pearson Correlation Coefficient

## Causality, Relevance