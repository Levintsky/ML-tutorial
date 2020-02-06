# Continuous Latent Variables

## PCA, ICA (PRML, Chap 12)
- PCA:
	- Maximum variation;
	- Minimum error;
	- Whitening;\
		<img src="/Bayes/images/pca/whiten.png" alt="drawing" width="400"/>
- Probabilistic PCA:
	- expressed as the maximum likelihood solution of a probabilistic latent variable model;
		<img src="/Bayes/images/pca/pca-1.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/pca-2.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/pca-3.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/pca-4.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/pca-5.png" alt="drawing" width="250"/>
	- MLE-PCA:\
		<img src="/Bayes/images/pca/pca-6.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/pca-7.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/pca-8.png" alt="drawing" width="400"/>
	- EM-PCA:\
		<img src="/Bayes/images/pca/em-pca1.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/em-pca2.png" alt="drawing" width="400"/>
		- E-step:\
			<img src="/Bayes/images/pca/em-pca3.png" alt="drawing" width="400"/>
		- M-step:\
			<img src="/Bayes/images/pca/em-pca4.png" alt="drawing" width="400"/>
	- Bayesian PCA:\
		<img src="/Bayes/images/pca/bayes-pca.png" alt="drawing" width="400"/>
	- Factor analysis: different in that the variance of x is diagonal rather than isotropic:
		<img src="/Bayes/images/pca/factor-analysis-1.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/factor-analysis-2.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/factor-analysis-3.png" alt="drawing" width="400"/>
- Kernel PCA: N samples, M-dim features;
	- Feature space (M x M):\
		<img src="/Bayes/images/pca/k-pca-1.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/k-pca-2.png" alt="drawing" width="400"/>
	- Sample space (N x N):\
		<img src="/Bayes/images/pca/k-pca-3.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/k-pca-4.png" alt="drawing" width="400"/>
	- Prediction:\
		<img src="/Bayes/images/pca/k-pca-5.png" alt="drawing" width="400"/>
	- Normalization (feature 0 mean):\
		<img src="/Bayes/images/pca/k-pca-6.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/pca/k-pca-7.png" alt="drawing" width="400"/>
- Non-linear latent
	- ICA: blind source separation;
	- Autoassociative neural network;
	- Modeling nonlinear manifold;

## PCA
- Quan Wang. Kernel Principal Component Analysis and its Applications in Face Recognition and Active Shape Models. 2014
	- Key insight: preimage, iteratively optimize z, such that the projection with on true feature-space eigen-vector v1, v2, ... is the same as the kernelized result;
		<img src="/Bayes/images/pca/pre-image-1.png" alt="drawing" width="400"/>
	- Gaussian kernels:\
		<img src="/Bayes/images/pca/pre-image-2.png" alt="drawing" width="400"/>

## ICA
- Example:
```python
# mix s1 and s2, and get 
s1, s2 = imread(im1), imread(im2)
A = [[0.8, 0.2], [.5, .5]]
x1 = A[0, 0] * s1 + A[0, 1] * s2
x2 = A[1, 0] * s1 + A[1, 1] * s2
m, n = X1.shape
x1, x2 = x1.reshape(m*n, 1), x2.reshape(m*n, 1)
# step 1: normalize, whiten, toremove >= 2nd order correlation
x1 = x1 - mean(x1)
x2 = x2 - mean(x2)
theta0 = 0.5 * atan(-2. * sum(x1 * x2) / sum(x1 ** 2 + x2 ** 2))
Us = [[cos(theta0), sin(theta0)], [-sin(theta0), cos(theta0)]]
sig1, sig2 = sum((Us * [[x1], [x2]]) ** 2)
Sigma = [[1/sqrt(sig1), 0], [0, 1/sqrt(sig2)]]
# prob density
x1bar, x2bar = Sigma * Us  * [[x1], [x2]]
phi0 = .25 * atan(-sum(2 * x1bar ** 3 .* x2bar - 2 * x2bar ** 3 .* x1bar) / 
    sum(3 * x1bar ** 2 .* x2bar ** 2 - 0.5 * x1bar ** 4 - 0.5 * x2bar ** 4))
V = [[cos(phi0), sin(phi0)], [-sin(phi0), cos(phi0)]]
s1bar, s2bar = V * [x1bar; x2bar]
```
- Mutual information (MI) estimation:
	- **Kernel-ICA**: Francis R. Bach, Michael I. Jordan. Kernel Independent Component Analysis. JMLR'02
- Entropy, negentropy estimation
	- **Infomax-ICA**: AJ Bell, TJ Sejnowski. An information-maximization approach to blind separation and blind deconvolution. Neural computation'95
	- **RADICAL**: Erik. G. Learned-Miller, John W. Fisher III, ICA Using Spacings Estimates of Entropy. JMLR'03
	- **FastICA**: A. Hyvärinen. Fast and Robust Fixed-Point Algorithms for Independent Component Analysis. TNN'99
	- M Girolami, C Fyfe. Stochastic ICA contrast maximisation using OJA's nonlinear PCA algorithm. 1997
- ML estimation
	- **KDICA**: Aiyou Chen, Peter Bickel. Fast Kernel Density Independent Component Analysis. 2006
	- **EM-ICA**: Max Welling and Markus Weber. A Constrained EM Algorithm for Independent Component Analysis. Neural Computation'01
	- [MacKay 1996; Pearlmutter & Parra 1996; Cardoso 1997]
- Higher order moments, cumulants based methods
	- JADE[Cardoso,1993]
- Nonlinear correlation based methods
	- [Jutten and Herault, 1991]