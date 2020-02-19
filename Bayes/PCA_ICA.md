# Continuous Latent Variables

## PCA, ICA
- PRML, Chap 12
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
- Latent Linear Model (Kevin Murphy, Chap 12);
	- Factor Analysis: problem definition: infer latent z; learn W\
		<img src="/Bayes/images/pca/fa-def.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/fa-def2.png" alt="drawing" width="400"/>
	- Mixture of FA: a latent discrete indicator q\
		<img src="/Bayes/images/pca/mixture-fa.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/mixture-fa2.png" alt="drawing" width="400"/>
	- EM for mixuter FA:
		- E-step: infer q and z;\
			<img src="/Bayes/images/pca/mixture-fa-em1.png" alt="drawing" width="400"/>
		- M-step: learning;\
			<img src="/Bayes/images/pca/mixture-fa-em2.png" alt="drawing" width="400"/>
	- PCA (check PCA.md)
	- PPCA: factor analysis;
	- Categorical PCA: logistic normal;\
		<img src="/Bayes/images/pca/cat-pca.png" alt="drawing" width="400"/>
	- Supervised PCA:\
		<img src="/Bayes/images/pca/sup-pca.png" alt="drawing" width="400"/>
	- Discriminative PCA: solve the problem in supervised PCA, x and y has same weight;
	- Discriminative supervised PCA: partial least square;\
		<img src="/Bayes/images/pca/pls.png" alt="drawing" width="400"/>
	- CCA (Canonical correlation analysis);\
		<img src="/Bayes/images/pca/cca.png" alt="drawing" width="400"/>
- Applications:
	- Quan Wang. Kernel Principal Component Analysis and its Applications in Face Recognition and Active Shape Models. 2014
		- Key insight: preimage, iteratively optimize z, such that the projection with on true feature-space eigen-vector v1, v2, ... is the same as the kernelized result;
			<img src="/Bayes/images/pca/pre-image-1.png" alt="drawing" width="400"/>
		- Gaussian kernels:\
			<img src="/Bayes/images/pca/pre-image-2.png" alt="drawing" width="400"/>

## ICA
- Non-linear latent (PRML, Chap 12)
	- ICA: blind source separation;
	- Autoassociative neural network;
	- Modeling nonlinear manifold;
- Kevin Murphy, 12.6
	- Problem definition: z, independent non-Gaussian variance=1;
		<img src="/Bayes/images/pca/ica-def.png" alt="drawing" width="400"/>
	- MLE: problem definition:\
		<img src="/Bayes/images/pca/ica-mle.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/ica-mle-2.png" alt="drawing" width="400"/>
	- FastICA (Hyvarinen and Oja 2000): assume all source distributions are **known** and are the **same**;
		<img src="/Bayes/images/pca/fast-ica-1.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/pca/fast-ica-2.png" alt="drawing" width="400"/>
	- Modeling source distribution:
		- Super-Gaussian distributions: kurt(z) > 0; natural signals (images) with filtering;
			<img src="/Bayes/images/pca/kurt.png" alt="drawing" width="200"/>
		- Skewed distribution:\
			<img src="/Bayes/images/pca/skew.png" alt="drawing" width="200"/>
- Example:
```python
# mix s1 and s2, and get 
s1, s2 = imread(im1), imread(im2)
A = [[0.8, 0.2], [.5, .5]]
x1 = A[0, 0] * s1 + A[0, 1] * s2
x2 = A[1, 0] * s1 + A[1, 1] * s2
m, n = X1.shape
x1, x2 = x1.reshape(m*n, 1), x2.reshape(m*n, 1)
# step 1: normalize, whiten, to remove >= 2nd order correlation
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

## Legacy
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

## Deep Latent Model (ICA)
- Assaf Shocher, Michal Irani. Blind Super-Resolution Kernel Estimation using an Internal-GAN Sefi Bell-Kligler. NIPS'19
- Ilyes Khemakhem, Diederik P. Kingma, Ricardo Pio Monti, Aapo Hyvärinen. Variational Autoencoders and Nonlinear ICA: A Unifying Framework. AISTATS'20 submission.
	- x d-dim, u m-dim both observed; z n-dim, n <= d latent;
	- Parameters: theta = (f, T, lambda); f: mixing? T sufficient statistics;
	- Model assumption:\
		<img src="/Bayes/images/pca/ica-vae-1.png" alt="drawing" width="250"/>\
		<img src="/Bayes/images/pca/ica-vae-2.png" alt="drawing" width="250"/>\
		<img src="/Bayes/images/pca/ica-vae-3.png" alt="drawing" width="250"/>
	- Main result:\
		<img src="/Bayes/images/pca/ica-vae-4.png" alt="drawing" width="400"/>
- Peter Sorrenson, Carsten Rother, Ullrich Köthe. Disentanglement by Nonlinear ICA with General Incompressible-flow Networks (GIN). ICLR'20
	- Architecture:\
		<img src="/Bayes/images/pca/ica-flow-1.png" alt="drawing" width="400"/>
	- Model:\
		<img src="/Bayes/images/pca/ica-flow-2.png" alt="drawing" width="400"/>
	- Given {(x1, u1), (x2, u2), ...}, x: data, u: class label, our cost function:\
		<img src="/Bayes/images/pca/ica-flow-3.png" alt="drawing" width="400"/>

## Unclassified
- Identifiability in Time Series:
	- **TCL**: Hyvärinen, A. and Morioka, H. Unsupervised feature extraction by time-contrastive learning and nonlinear ICA. NIPS'16
	- Aapo Hyvarinen and Hiroshi Morioka. Nonlinear ICA of temporally dependent stationary sources. PMLR'17
- Aapo Hyvarinen, Hiroaki Sasaki, and Richard E Turner. Nonlinear ICA using auxiliary variables and generalized contrastive learning. 2018
- Hyvärinen, A., Sasaki, H., and Turner, R. Nonlinear ICA Using Auxiliary Variables and Generalized Contrastive Learning. AISTATS'19
- Wei Wang, Zheng Dang, Yinlin Hu, Pascal Fua, Mathieu Salzmann. Backpropagation-Friendly Eigendecomposition. NIPS'19
- Piotr Indyk, Ali Vakilian, Yang Yuan. Learning-Based Low-Rank Approximations. NIPS'19
