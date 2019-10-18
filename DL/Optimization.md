# Optimization Methods

## 1st-Order
- **AdaGrad**: J Duchi, E Hazan, and Y Singer. Adaptive subgradient methods for online learning and stochastic optimization. JMLR'11
- **ADAM**: D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. 2014
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

## Large-Scale
- Rohan Anil, Vineet Gupta, Tomer Koren, and Yoram Singer. Memory-efficient adaptive optimiza- tion for large-scale learning. 2019

## Misc
- Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. 2018