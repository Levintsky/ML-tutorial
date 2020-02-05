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

## Papers
- Quan Wang. Kernel Principal Component Analysis and its Applications in Face Recognition and Active Shape Models. 2014
	- Key insight: preimage, iteratively optimize z, such that the projection with on true feature-space eigen-vector v1, v2, ... is the same as the kernelized result;
		<img src="/Bayes/images/pca/pre-image-1.png" alt="drawing" width="400"/>
	- Gaussian kernels:\
		<img src="/Bayes/images/pca/pre-image-2.png" alt="drawing" width="400"/>
