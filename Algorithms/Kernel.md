# Kernel, Embedding, Metric Learning

## Basics
- Kernel functions:
	- RBF, Mercer, linear, ...
	- Kernel Trick: NN, ridge regression, PCA, SVM;

## Tutorials, Books
- Ralf Herbrich. Learning Kernel Classifiers. 2001
- Bernhard Scholkopf, Alexander J. Smola. Learning with kernels. 2002
- John Shawe-Taylor and Nello Cristianini. Kernel Methods for Pattern Analysis. 2004

## Kernel Methods (PRML, Chap 6, Kevin Murphy Chap 14)
- 14.1 Introduction
- 14.2 Kernel functions;
	- κ(x,x') ∈ R
	- 14.2.1 RBF: κ(x, x^) = exp(−1/2(x−x^)'Σ^(−1)(x−x^)
	- 14.2.2 Kernels for comparing documents
		- Cosine similarity
		- tf-idf
	- 14.2.3 Mercer kernels
		- Gram matrix positive definite kernel;
		- Mercer theo: kij = φ(xi)'φ(xj)
	- 14.2.4 Linear kernels
	- 14.2.5 Matern kernels (commonly used in GP)
		- k(r) = 2^(1−ν)/Γ(ν) (√2νr/l)^ν Kν(√2νr/l)
		- κ(r) = exp(−r/l) if ν=1/2
	- 14.2.6 String;
	- 14.2.7 Pyramid match kernels;
	- 14.2.8 Kernels derived from probabilistic generative models
		- κ(xi,xj) = ∫p(x|xi)^ρ p(x|xj)^ρdx
	- Fisher kernel;
		- κ(x, x^) = g(x)'F^(−1)g(x^)
		- F = ∇∇logp(x|θ)|θˆ
- 14.3 Using kernels inside GLMs
	- 14.3.1 Kernel machines
	- 14.3.2 L1VMs, RVMs, and other sparse vector machines
- 14.4 Kernel trick;
	- 14.4.1 Kernel NN;
	- 14.4.2 Kernel K-medoids; (kernelized K-means)
	- 14.4.3 Kernel ridge regression;
		- Primal: J(w) = (y−Xw)'(y−Xw) + λ|w|^2
		- Optimal: w = (X'X+λI)^(−1)X'y=(Σxixi'+λI)^(−1)X'y
		- Dual:
			- Dual variable: α := (K + λI)^(−1)y
			- f(x) = w(x) = Σαiκ(x,xi)
	- 14.4 Kernel PCA;
		- PCA: S=(1/N)X'X (dxd)
		- XX' (NxN): let U, Λ be eigen of XX': (XX')U = UΛ
			- (X'X)(X'U) = (X'U)Λ
			- eigenvector of X'X is V=X'U and Λ
			- Normalized V=X'UΛ^(-1/2)
		- KPCA: S=(1/N)Σ_i φiφi', let Φ=[φ1,φ2,...,φN]
			- eigenvector: V=(Φ'U)Λ^(-1/2)
			- a new test vector x∗ with φ∗:
				- φ∗'Vkpca = φ∗'ΦUΛ^(−1/2) = k∗'UΛ^(−1/2)
				- k∗ = [κ(x∗,x1),...,κ(x∗,xN)]
			- Make the data φ zero-mean;
		- In practice alg:
			- Centerize K as K^;
			- [U, Λ]=eig(K^);
			- Normalize vi=ui/λi
			- Centerize K∗ as K∗^;
			- Z∗ = K∗^V[:,:L]
	- 14.5 SVM
		- J(w, λ) = ΣL(yi, yˆi) + λ|w|2
		- 14.5.1 SVMs for regression
			- Huber like regression loss: E(y(x)-t) = (|y(x)-t|-ε)+
			- J(w, λ) = Σ(ξi+, ξi-) + λ|w|2
			- Optimal solution has form: wˆ = Σ αi xi (Schoelkopf and Smola 2002)
			- yˆ(x) = wˆ0 + Σαi κ(xi, x)
		- 14.5.2 SVMs for classification
			- Hinge loss: Lnll(y, η) = −logp(y|x, w) = log(1+e−yη) (logistic)
			- L(y, η) = max(0, 1−yη) = (1−yη)+
			- J(w, λ) = 1/2|w|2 + CΣ(1−yη)+ equivalent to Σξ
			- yˆ(x) = sgn(wˆ0 + Σαi κ(xi, x))
			- Large margin learning: x=x⊥+rw/|w|, then f(x)=rw'w/|w|
			- ν-SVM classifier: CΣξ (C=1/(νN))
			- Probabilistic output
			- SVMs for multi-class classification
		- 14.5.3 Choosing C
		- 14.5.4 Summary of key points
		- 14.5.5 A probabilistic interpretation of SVMs
- 14.6 Comparison of discriminative kernel methods
- 14.7 Kernels for building generative models
	- 14.7.1 Smoothing kernels
		- ∫κ(x)dx = 1, ∫xκ(x)dx = 0, ∫x^2κ(x)dx > 0
	- 14.7.2 Kernel density estimation (KDE)
		- p(x) = 1/N Σκ(x-xi)
	- 14.7.3 From KDE to KNN
	- 14.7.4 Kernel regression
		- f(x) = Σwi(x)yi (kernel regression, kernel smoothing, or the Nadaraya-Watson mode)
		- wi(x) = κ(x-xi)/Σκ(x-xi)
	- 14.7.5 Locally weighted regression
		- f(x) = Σyiκ(x,xi)
		- min_β(x^) Σ_i κ(x^,xi)[yi-β(x^)φ(xi)]
		- β(x∗) = (Φ'D(x∗)Φ)^(−1) Φ'D(x∗)y

## Sparse Kernel Machines (PRML, Chap 7)
- Computational learning theory:
	- The goal of the PAC framework is to understand how large a data set needs to be in order to give good generalization;
- Relevance Vector Machines:
	- Bayesian version of SVM; SVM only gives decision boundary, no posterior;
	- Problem formulation:\
		<img src="/Basic-ML/images/svm/rvm-1.png" alt="drawing" width="300"/>\
		<img src="/Basic-ML/images/svm/rvm-2.png" alt="drawing" width="400"/>
		<img src="/Basic-ML/images/svm/rvm-3.png" alt="drawing" width="400"/>
	- Hyper-parameter optimization:\
		<img src="/Basic-ML/images/svm/rvm-4.png" alt="drawing" width="400"/>
		<img src="/Basic-ML/images/svm/rvm-5.png" alt="drawing" width="400"/>
		<img src="/Basic-ML/images/svm/rvm-6.png" alt="drawing" width="400"/>
	- Approach 1: (direct-iterative): 1. alpha and beta; 2. mean and variance in (7.82), (7.83);
	- Approach 2: EM;
	- RVM for classification:
		- For fixed alpha, Laplacian approximation:\
			<img src="/Basic-ML/images/svm/rvm-7.png" alt="drawing" width="400"/>
			<img src="/Basic-ML/images/svm/rvm-8.png" alt="drawing" width="400"/>
		- Alpha:\
			<img src="/Basic-ML/images/svm/rvm-9.png" alt="drawing" width="400"/>

## Structured-SVM
- http://www.csc.kth.se/cvap/cvg/rg/materials/magnus_004_slides.pdf
- Generalize classical SVM to structured output;
- Learn linear weight w for the loss/utility < w, phi(x, y) >
	- with desired loss delta(y, y')
	- argmin w, s.t. ||w||^2 + C max(y) (delta(y, ygt) + w (phi(x,y)-phi(x,ygt)))
- Special case: ranking-SVM;
- Kevin Murphy, Chap 19.7
	- Training/testing time, minimize expected loss:\
		<img src="/Basic-ML/images/svm/ssvm-1.png" alt="drawing" width="400"/>
	- Lower/upper bound:\
		<img src="/Basic-ML/images/svm/ssvm-2.png" alt="drawing" width="400"/>\
		<img src="/Basic-ML/images/svm/ssvm-3.png" alt="drawing" width="400"/>
	- Gaussian prior:\
		<img src="/Basic-ML/images/svm/ssvm-4.png" alt="drawing" width="400"/>
	- Non-probabilistic view:\
		<img src="/Basic-ML/images/svm/ssvm-5.png" alt="drawing" width="400"/>\
		<img src="/Basic-ML/images/svm/ssvm-6.png" alt="drawing" width="400"/>
	- Cutting plane methods (http://svmlight.joachims.org/svm_struct.html)
		- We start with an initial guess w and no constraints. At each iteration, we then do the following: for each example i, we find the "most violated" constraint involving x and yˆ . If the loss-augmented margin violation exceeds the current value of ξ by more than ε, we add yˆ to the working set of constraints for this training case, W , and then  solve the resulting new QP to find the new w, ξ.
		- Loss-augmented decoding: the other key to efficiency is the ability to find the most violated constraint in line 5 of the algorithm
		<img src="/Basic-ML/images/svm/ssvm-7.png" alt="drawing" width="400"/>
	- The structured perceptron algorithm;
	- Stochastic subgradient descent;
	- **Latent structural SVMs**: hidden h; e.g. in machine translation, we may know the source text x (say English) and the target text y (say French), but we typically do not know the alignment;
		- Formulation:\
			<img src="/Basic-ML/images/svm/latent-svm-1.png" alt="drawing" width="400"/>
		- Bound:\
			<img src="/Basic-ML/images/svm/latent-svm-2.png" alt="drawing" width="400"/>
		- CCCP (concave-convex procedure): this objective is no longer convex; minimizing functions of the form f(w) − g(w), where f and g are convex. The method alternates between finding a linear upper bound u on −g, and then minimizing the convex function f(w) + u(w);\
			<img src="/Basic-ML/images/svm/latent-svm-3.png" alt="drawing" width="400"/>
		- A hard EM alg:\
			<img src="/Basic-ML/images/svm/latent-svm-4.png" alt="drawing" width="400"/>

## Classical
- A. Rahimi and B. Recht. Random features for large-scale kernel machines. NIPS'08

## Deep Learning
- Y. Cho and L. K. Saul. Kernel methods for deep learning. NIPS'09
- **NTK**: Arthur Jacot, Franck Gabriel, and Clément Hongler. Neural tangent kernel: Convergence and generalization in neural networks. NIPS'18
- Jaehoon Lee, Yasaman Bahri, Roman Novak, Sam Schoenholz, Jeffrey Pennington, and Jascha Sohl-dickstein. Deep neural networks as gaussian processes. ICLR'18
- Neal Jean, Sang Michael Xie, Stefano Ermon. Semi-supervised Deep Kernel Learning: Regression with Unlabeled Data by Minimizing Predictive Variance. NIPS'18
- Lenaic Chizat, Edouard Oyallon, and Francis Bach. On lazy training in differentiable programming. arXiv preprint arXiv:1812.07956, 2019
- **GNN**: Simon S Du, Kangcheng Hou, Russ R Salakhutdinov, Barnabas Poczos, Ruosong Wang, and Keyulu Xu. Graph neural tangent kernel: Fusing graph neural networks with graph kernels. NeurIPS'19
- Greg Yang. Scaling limits of wide neural networks with weight sharing: Gaussian process behavior, gradient independence, and neural tangent kernel derivation. arxiv'19
- Jiri Hron, Yasaman Bahri, Jascha Sohl-Dickstein, Roman Novak. Infinite attention: NNGP and NTK for deep attention networks. ICML'20
- Soufiane Hayou, Arnaud Doucet, and Judith Rousseau. Mean-field behaviour of neural tangent kernel for deep neural networks, 2019

## NIPS'18
- Motonobu Kanagawa, Philipp Hennig. Convergence Guarantees for Adaptive Bayesian Quadrature Methods
- Ulysse Marteau-Ferey, Francis Bach, Alessandro Rudi. Globally Convergent Newton Methods for Ill-conditioned Generalized Self-concordant Losses
- Rahul Singh, Maneesh Sahani, Arthur Gretton. Kernel Instrumental Variable Regression
- Jen Ning Lim, Makoto Yamada, Bernhard Schölkopf, Wittawat Jitkrittum. Kernel Stein Tests for Multiple Model Comparison
- Sanjeev Arora, Simon Du, Wei Hu, Zhiyuan Li, Russ Salakhutdinov, Ruosong Wang. On Exact Computation with an Infinitely Wide Neural Net
- Chieh Wu, Jared Miller, Yale Chang, Mario Sznaier, Jennifer Dy. Solving Interpretable Kernel Dimensionality Reduction
