# Data Science Summary

## Basics
- Summaries
	- https://segmentfault.com/a/1190000004411616
	- https://www.zhihu.com/question/23149768
- Books
	- Statistics. Freedman, Pisani & Purves.
- Classes
	- Stanford STATS 60: https://web.stanford.edu/class/stats60/

## Graphical Summaries
- Histogram
- Box plot
	- Quantile: x1 < ... < xn
		- x[ceil(np)] if np is not an integer
		- 0.5 (x[np]+x[np+1]) if np is an integer
	- Min, Q1, Median, Q3, Max

## Numeric Summaries
- Descriptive Statistics, Predicative Statistics
	- Mean
	- Median
	- Correlation
	- K-th order moments
	- Standard Deviation
	- Variance

## Parameter Estimation
- Parameter distribution summary:
	<img src="/Basic-ML/images/stat/gaussian-sum.png" alt="drawing" width="600"/>
- Bernoulli 0-1, n samples approximates as Gaussian:\
	<img src="/Basic-ML/images/stat/bernoulli-ci1.png" alt="drawing" width="400"/>\
	<img src="/Basic-ML/images/stat/bernoulli-ci2.png" alt="drawing" width="400"/>

## Hypothesis Testing
- Z-scores:
	- z = (obs-expected)/SE(observed)
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
		- X follows a **normal** distribution with mean mu and variance σ^2/n;
		- s^2 follows a χ-square with n−1 dof;
		- Z and s are independent.
		- t = Z/s = (E[X]-μ) / (σ/√n)
- Pearson's χ-squared test:
	- Assumption: valid to perform when the test statistic is χ-squared distributed under the null hypothesis;

## Hypothesis Testing
- Type I error: false positive
- Type II error: false negative
- Testing of Normal distribution summary:
<img src="/Basic-ML/images/stat/gaussian-test1.png" alt="drawing" width="600"/>
<img src="/Basic-ML/images/stat/gaussian-test2.png" alt="drawing" width="600"/>

	- Testing of Variance
		- χ-square test: variance of some samples
		- F-test: Given two set of samples from (μ1, σ1), (μ2, σ2), test if var1 ? var2
- Distribution fitting test
- Skewness, Kurtosis
	- 3rd and 4th moments
	- For normal distribution we have:
		- G1 ~ N(0, 6(n-2)/(n+1)(n+3))
		- G2 ~ N(3-6/n+1, 24(n-2)(n-3)/(n+1)^2(n+3)(n+5))
- Rank sum test:
	- f1(x) = f2(x+a) test a ? 0
	- rank x(1) < x(2) < ... < x(n)
- P-Value test:
	- e.g., 100 coins, 90H/10T, fair?
	- All more extreme cases
	- p-value=2(p(90H)+p(91H)+...)
	- Consider: p(10H)+p(9H)
	- p < α, reject

## Outlier, Anomaly

## ANOVA (Analysis of Variance)

## Causality, Relevance