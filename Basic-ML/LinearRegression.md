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