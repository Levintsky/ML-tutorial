# Linear Regression

## MLE
- OLS (ordinary least squares) \
	<img src="/Bayes/images/lr/linear-regression1.png" alt="drawing" width="300"/>\
	<img src="/Bayes/images/lr/linear-regression2.png" alt="drawing" width="200"/>
- Geometric interpretation:\
	<img src="/Bayes/images/lr/linear-regression3.png" alt="drawing" width="150"/>
- Robust linear regression:
	- L1-norm
	- Huber-loss
- Ridge-regression:\
	<img src="/Bayes/images/lr/ridge-regression1.png" alt="drawing" width="200"/>\
	<img src="/Bayes/images/lr/ridge-regression2.png" alt="drawing" width="200"/>
- Numerical stability:
	- Avoid inverting matrix
	- Cholesky decomposition
	- QR decomposition
- Bayesian linear regression
- Conjugate prior

## Linear Regression (Bishop, Chap 3)
- Linear model: basics with basis function \
	<img src="/Bayes/images/lr/lr-1.png" alt="drawing" width="200"/>
- Multiple output target t, with Moore-Penrose pseudo-inverse: \
	<img src="/Bayes/images/lr/lr-2.png" alt="drawing" width="200"/>\
	<img src="/Bayes/images/lr/lr-3.png" alt="drawing" width="200"/>\
	<img src="/Bayes/images/lr/lr-4.png" alt="drawing" width="350"/>
- Regularized:
	- L2: ridge regression;
	- L1: Lasso;
- Bias and Variance trade-off, let h(x)=E(t|x), the true mean of t(x); bias measures diff y(x;D) from h; variance of a solution measures its vary around its own average; \
	<img src="/Bayes/images/lr/lr-5.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/lr/lr-6.png" alt="drawing" width="400"/>
	- An example: given L=100 datasets, each dataset contains N=25 point. We use a linear combination of Gaussian to fit h(x)=sin(x); bias models deviation of average of different fit mean(y(x)) from h(x); variance measures each yi(x) from mean(y(x)); \
		<img src="/Bayes/images/lr/lr-7.png" alt="drawing" width="400"/>
- Bayesian LR: conjugate **prior** Gaussian w ~ N(m0, S0), then **posterior** is\
	<img src="/Bayes/images/lr/lr-8.png" alt="drawing" width="300"/>\
	<img src="/Bayes/images/lr/lr-9.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/lr/lr-10.png" alt="drawing" width="400"/>
- Beyesian LR prediction. Problem definition:
	<img src="/Bayes/images/lr/lr-11.0.png" alt="drawing" width="400"/>\
	- With Gaussian Bayes theorem of convolving two Gaussian, we have:
		<img src="/Bayes/images/lr/lr-11.png" alt="drawing" width="400"/>\
	- With smoother matrix, or the equivalent kernel, satisfying sum_n k(x,x_n)=1, we have \
	<img src="/Bayes/images/lr/lr-12.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/lr/lr-13.png" alt="drawing" width="200"/>
- Bayesian Model comparison:
	- L models {Mi}, i = 1, ..., L. **Bayes factor**: p(D|Mi)/p(D|Mj)
- Evidence approximation:
	- **Empirical Bayes**: set the hyperparameters alpha, beta (w ~ N(0, alpha^-1), y ~ N(xw, beta^-1)) to specific values determined by maximizing the marginal likelihood function obtained by first integrating over the parameters w; \
		<img src="/Bayes/images/lr/lr-14.png" alt="drawing" width="400"/>
	- Marginalize over w, then do implicit optimization for alpha, beta respetively;

## Latent Linear Models (Kevin Murphy, Chap 12)
- Factor Analysis (FA)
- PCA
- ICA (Independent Component Analysis)

## Sparse Linear Models (Kevin Murphy, Chap 13)
- Spike and Slab model
- Bayesian Variable Selection:
	- OMP (Orthogonal Matching Pursuit) 
	- MP (Matching Pursuit)
	- LASSO
	- LARS