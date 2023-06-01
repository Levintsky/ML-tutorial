# Continuous Latent Variables

## Basics
- PCA: check Probability/Linear-Model
	- PCA: obs x=Wz, z Gaussian, minimize reconstruction error;
- ICA: check Probability/Linear-Model
	- ICA: obs x=Wz, z-Non-Gaussian;
	- fast-ICA;
- CCA: X=(x1,...,xn), Y=(y1,...,ym), maximize their correlation;
	- (a', b') = argmax_a,b corr(a'X, b'Y)

## PCA
- Applications:
	- Q Wang. Kernel Principal Component Analysis and its Applications in Face Recognition and Active Shape Models. 2014
		- Key insight: preimage, iteratively optimize z, such that the projection with on true feature-space eigen-vector v1, v2, ... is the same as the kernelized result;
			<img src="/Bayes/images/pca/pre-image-1.png" alt="drawing" width="400"/>
		- Gaussian kernels:\
			<img src="/Bayes/images/pca/pre-image-2.png" alt="drawing" width="400"/>

## ICA
- Legacy
	- Mutual information (MI) estimation:
		- **Kernel-ICA**: F Bach, M Jordan. Kernel Independent Component Analysis. JMLR'02
	- Entropy, negentropy estimation
		- **Infomax-ICA**: A Bell, T Sejnowski. An information-maximization approach to blind separation and blind deconvolution. Neural computation'95
		- **RADICAL**: Erik. G. Learned-Miller, John W. Fisher III, ICA Using Spacings Estimates of Entropy. JMLR'03
		- **FastICA**: A. Hyvärinen. Fast and Robust Fixed-Point Algorithms for Independent Component Analysis. TNN'99
		- M Girolami, C Fyfe. Stochastic ICA contrast maximisation using OJA's nonlinear PCA algorithm. 1997
	- ML estimation
		- **KDICA**: A Chen, P Bickel. Fast Kernel Density Independent Component Analysis. 2006
		- **EM-ICA**: M Welling and M Weber. A Constrained EM Algorithm for Independent Component Analysis. NC'01
		- [MacKay 1996; Pearlmutter & Parra 1996; Cardoso 1997]
	- Higher order moments, cumulants based methods
		- JADE[Cardoso,1993]
	- Nonlinear correlation based methods
		- [Jutten and Herault, 1991]
- Identifiability in Time Series:
	- **TCL**: A Hyvärinen and H Morioka. Unsupervised feature extraction by time-contrastive learning and nonlinear ICA. NIPS'16
	- A Hyvarinen and H Morioka. Nonlinear ICA of temporally dependent stationary sources. PMLR'17
- A Hyvärinen, H Sasaki, and R Turner. Nonlinear ICA Using Auxiliary Variables and Generalized Contrastive Learning. AISTATS'19
- W Wang, Z Dang, Y Hu, P Fua, Mathieu Salzmann. Backpropagation-Friendly Eigendecomposition. NIPS'19
- P Indyk, A Vakilian, Y Yuan. Learning-Based Low-Rank Approximations. NIPS'19
- Applications
	- ICA: blind source separation;
	- Autoassociative neural network;
	- Modeling nonlinear manifold;
- **Deep Latent Model (ICA)**
	- A Shocher, Ml Irani. Blind Super-Resolution Kernel Estimation using an Internal-GAN Sefi Bell-Kligler. NIPS'19
	- I Khemakhem, D Kingma, R Monti, A Hyvärinen. Variational Autoencoders and Nonlinear ICA: A Unifying Framework. AISTATS'20 submission.
		- x d-dim, u m-dim both observed; z n-dim, n <= d latent;
		- Parameters: θ = (f, T, λ); f: mixing? T sufficient statistics;
		- Model assumption:
			- p(x,z|u; θ) = p(x|z;f)p(z|u; T, λ)
			- p(x|z; f) = p(x-f(z); ε)
			- p(z|u; T, λ) = Π_i pi(zi|u) = Π_i Qi(zi)/Zi(ui) exp[Σj=1..k Tij(zi)λi,j(u)]
		- Main result: (theorem) θ = (f, T, λ) are identifiable
	- P Sorrenson, C Rother, U Köthe. Disentanglement by Nonlinear ICA with General Incompressible-flow Networks (GIN). ICLR'20
		- Architecture:\
			<img src="/Bayes/images/pca/ica-flow-1.png" alt="drawing" width="400"/>
		- Model:\
			<img src="/Bayes/images/pca/ica-flow-2.png" alt="drawing" width="400"/>
		- Given {(x1, u1), (x2, u2), ...}, x: data, u: class label, our cost function:\
			<img src="/Bayes/images/pca/ica-flow-3.png" alt="drawing" width="400"/>
