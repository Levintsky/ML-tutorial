# Kernel, Embedding, Metric Learning

## Tutorials, Books
- Ralf Herbrich. Learning Kernel Classifiers. 2001
- Bernhard Scholkopf, Alexander J. Smola. Learning with kernels. 2002
- John Shawe-Taylor and Nello Cristianini. Kernel Methods for Pattern Analysis. 2004

## Kernel Methods (PRML, Chap 6)
- Formulation with the dual a:\
	<img src="/Basic-ML/images/kernel/kernel-1.1.png" alt="drawing" width="400"/>
- Then, for a we have:\
	<img src="/Basic-ML/images/kernel/kernel-1.2.png" alt="drawing" width="400"/>
- For prediction:\
	<img src="/Basic-ML/images/kernel/kernel-1.3.png" alt="drawing" width="400"/>
- Constructing Kernels:\
	<img src="/Basic-ML/images/kernel/kernel-2.1.png" alt="drawing" width="400"/>\
	<img src="/Basic-ML/images/kernel/kernel-2.2.png" alt="drawing" width="400"/>\
- Kernel between sets:\
	<img src="/Basic-ML/images/kernel/kernel-2.3.png" alt="drawing" width="200"/>
- Kernels of generative models:\
	<img src="/Basic-ML/images/kernel/kernel-2.4.png" alt="drawing" width="250"/>\
	<img src="/Basic-ML/images/kernel/kernel-2.5.png" alt="drawing" width="300"/>\
	<img src="/Basic-ML/images/kernel/kernel-2.6.png" alt="drawing" width="400"/>
- Radial Basis Function:\
	<img src="/Basic-ML/images/kernel/nadaraya-watson.png" alt="drawing" width="400"/>

## Sparse Kernel Machines (PRML, Chap 7)
- SVM: for Lagrange Dual, check opt.pdf
- Large margin classifier:\
	<img src="/Basic-ML/images/svm/svm-1.png" alt="drawing" width="400"/>
- Lagrange dual, notice we have negative a since we maximize w.r.t. a:
	<img src="/Basic-ML/images/svm/svm-2.png" alt="drawing" width="400"/>
- Optimize the dual problem:\
	<img src="/Basic-ML/images/svm/svm-3.png" alt="drawing" width="400"/>
- Tradeoff: For a fixed set of basis functions whose number M is smaller than the number N of data points, the move to the dual problem appears disadvantageous. However, it allows the model to be reformulated using kernels, and so the maximum margin classifier can be applied efficiently to feature spaces whose dimensionality exceeds the number of data points, including infinite feature spaces.
- Prediction:\
	<img src="/Basic-ML/images/svm/svm-4.png" alt="drawing" width="400"/>
- Relaxed version, with KKT condition:\
	<img src="/Basic-ML/images/svm/svm-5.png" alt="drawing" width="400"/>\
	<img src="/Basic-ML/images/svm/svm-6.png" alt="drawing" width="400"/>\
	<img src="/Basic-ML/images/svm/svm-7.png" alt="drawing" width="400"/>\
	<img src="/Basic-ML/images/svm/svm-8.png" alt="drawing" width="400"/>\
	<img src="/Basic-ML/images/svm/svm-9.png" alt="drawing" width="400"/>
- Relation with logistic regression: hinge-loss;\
	<img src="/Basic-ML/images/svm/svm-10.png" alt="drawing" width="400"/>
- Multiclass SVM;
	- Train K separate; Vapnik 1998
- SVM for regression:\
	<img src="/Basic-ML/images/svm/svm-11.png" alt="drawing" width="400"/>
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

## NN
- Tobias Plötz, Stefan Roth. Neural Nearest Neighbors Networks. NIPS'18
- Ignacio Rocco, Mircea Cimpoi, Relja Arandjelovic, Akihiko Torii, Tomas Pajdla, Josef Sivi. Neighbourhood Consensus Networks. NIPS'18
- Ari Morcos, Maithra Raghu, Samy Bengio. Insights on representational similarity in neural networks with canonical correlation. NIPS'18

## Kernel
- Neal Jean, Sang Michael Xie, Stefano Ermon. Semi-supervised Deep Kernel Learning: Regression with Unlabeled Data by Minimizing Predictive Variance. NIPS'18
