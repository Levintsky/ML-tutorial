# Optimization Methods

## Lagrange Dual
- A good summary:
	- https://blog.csdn.net/asd136912/article/details/79149881
	- https://www.cnblogs.com/90zeng/p/Lagrange_duality.html
	- https://www.zhihu.com/question/58584814
	- https://zhuanlan.zhihu.com/p/26514613
- Application:
	- SVM;

## Deep-Learning optimizers
- Summaries:
	- http://ruder.io/optimizing-gradient-descent/

## 1st-Order
- SGD:
	<img src="/Basic-ML/images/optimization/sgd.png" alt="drawing" width="200"/>
- SGD with batch:
	<img src="/Basic-ML/images/optimization/sgd-batch.png" alt="drawing" width="200"/>
- Momentum:
	<img src="/Basic-ML/images/optimization/momentum.png" alt="drawing" width="200"/>
- Nestorov:
	<img src="/Basic-ML/images/optimization/nag.png" alt="drawing" width="200"/>
- **AdaGrad**: J Duchi, E Hazan, and Y Singer. Adaptive subgradient methods for online learning and stochastic optimization. JMLR'11
	<img src="/Basic-ML/images/optimization/adagrad.png" alt="drawing" width="500"/>
- Rmsprop:
	<img src="/Basic-ML/images/optimization/rmsprop.png" alt="drawing" width="400"/>
- **ADAM**: D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. 2014
	<img src="/Basic-ML/images/optimization/adam.png" alt="drawing" width="600"/>
- Adadelta: M Zeiler. ADADELTA: An Adaptive Learning Rate Method. 2012
	<img src="/Basic-ML/images/optimization/adadelta.png" alt="drawing" width="600"/>
- U Şimşekli，L Sagun, M Gürbüzbalaban. A Tail-Index Analysis of Stochastic Gradient Noise in Deep Neural Networks. ICML'19 best paper honorable mention

## 2nd-Order
- Natural Gradient:
	- Left multiplying inverse of Fisher Information Matrix
- **KFAC**: J. Martens and R. Grosse. Optimizing neural networks with kronecker-factored approximate curvature. 2015
	- Kronecker approximation to Fisher
- **FANG**: R. Grosse and R. Salakhudinov. Scaling up natural gradient by sparsely factorizing the inverse fisher
matrix.
	- Cholesky decomposition.
- **PRONG**: G. Desjardins, K. Simonyan, R. Pascanu, et.al. Natural neural networks. NIPS 2015
	- Whitening each layer.

## SVGD
- Stein variational gradient descent: A general purpose bayesian inference algorithm, NIPS'16
	- https://github.com/DartML/Stein-Variational-Gradient-Descent

## Large-Scale
- Rohan Anil, Vineet Gupta, Tomer Koren, and Yoram Singer. Memory-efficient adaptive optimiza- tion for large-scale learning. 2019

## Misc
- Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. 2018