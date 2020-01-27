# Linear Regression

## MLE
- OLS (ordinary least squares)
	<img src="/Basic-ML/images/lr/linear-regression1.png" alt="drawing" width="150"/>
	<img src="/Basic-ML/images/lr/linear-regression2.png" alt="drawing" width="150"/>
- Geometric interpretation:\
	<img src="/Basic-ML/images/lr/linear-regression3.png" alt="drawing" width="150"/>
- Robust linear regression:
	- L1-norm
	- Huber-loss
- Ridge-regression:\
	<img src="/Basic-ML/images/lr/ridge-regression1.png" alt="drawing" width="150"/>
	<img src="/Basic-ML/images/lr/ridge-regression2.png" alt="drawing" width="150"/>
- Numerical stability:
	- Avoid inverting matrix
	- Cholesky decomposition
	- QR decomposition
- Bayesian linear regression
- Conjugate prior

## Linear Model (Bishop, Chap 3)
- Linear model: basics with Moore-Penrose pseudo-inverse: \
	<img src="/Basic-ML/images/lr/lr-1.png" alt="drawing" width="200"/>
	<img src="/Basic-ML/images/lr/lr-2.png" alt="drawing" width="200"/>
	<img src="/Basic-ML/images/lr/lr-3.png" alt="drawing" width="200"/>
	<img src="/Basic-ML/images/lr/lr-4.png" alt="drawing" width="350"/>
- Regularized:
	- L2: ridge regression;
	- L1: Lasso;
- Bias Variance; \
	<img src="/Basic-ML/images/lr/lr-5.png" alt="drawing" width="400"/>
	<img src="/Basic-ML/images/lr/lr-6.png" alt="drawing" width="400"/>
	- An example: we use a linear combination of Gaussian to fit h(x)=sin(x); bias models deviation of average of different fit mean(y(x)) from h(x); variance measures each yi(x) from mean(y(x)); \
		<img src="/Basic-ML/images/lr/lr-7.png" alt="drawing" width="400"/>

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