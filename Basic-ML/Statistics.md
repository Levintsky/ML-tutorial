# Data Science Summary

## Summaries
- https://segmentfault.com/a/1190000004411616
- https://www.zhihu.com/question/23149768

## Books
- Statistics. Freedman, Pisani & Purves.

## Classes
- Stanford STATS 60: https://web.stanford.edu/class/stats60/

## Graphical Summaries
- Histogram
- Box plot
	- Quantile: x1 < ... < xn
		- x[ceil(np)] if np is not an integer
		- 0.5 (x[np]+x[np+1]) if np is an integer
	- Min, Q1, Median, Q3, Max
	<img src="/Basic-ML/images/stat/box-plot.png" alt="drawing" width="300"/>

## Numeric Summaries
- Descriptive Statistics, Predicative Statistics
	- Mean
	- Median
	- Correlation
	- K-th order moments
	- Standard Deviation
	- Variance

## Hypothesis Testing
- Z-scores:\
	<img src="/Basic-ML/images/stat/z-score.png" alt="drawing" width="400"/>
- P-Value:
	- In general, if we test a null hypothesis with some observed data or observed test statistic, the P-value is the chance that we would observe such an extreme Z-score, assuming the null hypothesis is true. 
	- When computing chances using a z score, the test is called a z-test.
	- Note: P−value is random!
- Threshold for significance:
	- Often, a P-value is used to assess significance of a hypothesis test.
		- If the P-value is less than 5%, the result is statistically significant.
		- If the P-value is less than 1%, the result is called highly significant.
- T-test: SD+ instead of SD compared to Z-test;
	- Most test statistics have the form t=Z/s, where Z and s are functions of the data.
	- The **assumptions** underlying a t-test in its simplest form are that:
		- X follows a **normal** distribution with mean mu and variance sig^2/n;
		- s^2 follows a **chi-square** distribution with n−1 degrees of freedom. This assumption is met when the observations used for estimating s2 come from a normal distribution (and i.i.d for each group).
		- Z and s are **independent**.
		<img src="/Basic-ML/images/stat/t-test.png" alt="drawing" width="400"/>
- Pearson's **chi-squared** test:
	- Assumption: valid to perform when the test statistic is **chi-squared** distributed under the null hypothesis;
		<img src="/Basic-ML/images/stat/chi-squared-test.png" alt="drawing" width="400"/>

## More Gaussian
- Distribution of mean
	- Suppose variance known, average of samples as an estimate of mean: Gaussian
<img src="/Basic-ML/images/stat/gaussian-mean.png" alt="drawing" width="600"/>

- Distribution of Variance
	- Suppose X-bar and S^2 are sample mean and variance
	- (n-1)S^2 / std^2 observes chi(n-1)
	- X-bar and S^2 are independent
<img src="/Basic-ML/images/stat/gaussian-var.png" alt="drawing" width="600"/>

- Empirical of (x-mean)/std: t-distribution
<img src="/Basic-ML/images/stat/gaussian-meanvar.png" alt="drawing" width="600"/>

## Estimation
- Confidence interval:
	- p(theta1 < theta < theta2) = 1-alpha, out of interval: alpha
	- alpha = 0.05, Gaussian: +/-1.96sigma
- Estimate the interval of mean and variance of Gaussian
	- Sigma known: Gaussian
<img src="/Basic-ML/images/stat/gaussian-mean-est1.png" alt="drawing" width="200"/>

	- Sigma unknown: t-distribution
<img src="/Basic-ML/images/stat/gaussian-mean-est2.png" alt="drawing" width="200"/>
<img src="/Basic-ML/images/stat/gaussian-mean-est3.png" alt="drawing" width="450"/>

	- Variance estimation: chi
<img src="/Basic-ML/images/stat/gaussian-var-est.png" alt="drawing" width="500"/>
- Moment
- MLE
- Criteria
	- Unbiased
	- Smaller vaiance
	- Convergence
- Confidence Interval
	- Gaussian
		- std known, estimate mean: Gaussian
<img src="/Basic-ML/images/stat/gaussian-mean-ci1.png" alt="drawing" width="200"/>

		- std unknown, estimate mean: student-t
<img src="/Basic-ML/images/stat/gaussian-mean-ci2.png" alt="drawing" width="600"/>

		- estimate var: chi
<img src="/Basic-ML/images/stat/gaussian-var-ci.png" alt="drawing" width="400"/>

		- Difference of two Gaussian
	- Bernoulli 0-1, n samples approximates as Gaussian
<img src="/Basic-ML/images/stat/bernoulli-ci1.png" alt="drawing" width="500"/>
<img src="/Basic-ML/images/stat/bernoulli-ci2.png" alt="drawing" width="600"/>

- Single-side CI

## Hypothesis Testing
- Type I, II error
- Testing of Normal distribution summary:
<img src="/Basic-ML/images/stat/gaussian-test1.png" alt="drawing" width="600"/>
<img src="/Basic-ML/images/stat/gaussian-test2.png" alt="drawing" width="600"/>

	- Testing of Variance
		- Chi-square test: variance of some samples
		- F-test: Given two set of samples from (mean1, var1), (mean2, var2), test if var1 >=< var2?
- Distribution fitting test
- Skewness, Kurtosis
	- 3rd and 4th moments
<img src="/Basic-ML/images/stat/Skewness.png" alt="drawing" width="450"/>

	- For normal distribution we have:
<img src="/Basic-ML/images/stat/gaussian-skew.png" alt="drawing" width="450"/>

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