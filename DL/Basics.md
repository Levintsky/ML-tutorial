# Deep Learning Models

## Tutorials
- Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. nature, 521(7553):436, 2015.

## Books
- **Deep learning**: Ian Goodfellow, Yoshua Bengio, Aaron Courville, and Yoshua Bengio. volume 1. MIT press Cambridge, 2016.

## PRML (Chapter 5)
- Feed-forward:
	- Notation: aj = sum_i w_ji xi + wj0;
	- Weight space symmetry: tanh(-a) = -tanh(a);
	- Target regression: p(t|w, x) = N(y(x, w), beta^(-1)), with beta as the precision;
	- Cross entropy loss: -sum t_k ln y_k(x, w), with softmax;
- Training:
	- SGD, Hessian;
- Error backprop: Jacobian matrix;
- Hessian matrix:
	- Diagonal approximation:\
		<img src="/DL/images/hessian-approx.png" alt="drawing" width="500"/>
	- Outer product approx, ignore the 2nd term in (5.83);\
		<img src="/DL/images/hessian-1.png" alt="drawing" width="300"/>\
		<img src="/DL/images/hessian-2.png" alt="drawing" width="200"/>\
		<img src="/DL/images/hessian-3.png" alt="drawing" width="200"/>
	- Fast approximation by Hessian;
- Regularization:
	- Regularization;
	- Early stopping;
	- Invariance;
	- Tangent propagation [Simard'92];
	- Training with transformed data;
	- CNN;
	- Soft weight sharing;
		- L2-regularization: Gaussian prior;
		- Mixture of Gaussian;
- Mixture density networks:
	- Mixture Gaussian for multi-modal;\
		<img src="/DL/images/mdn-1.png" alt="drawing" width="450"/>
		<img src="/DL/images/mdn-2.png" alt="drawing" width="450"/>

## Dropout
- Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: A simple way to prevent neural networks from overfitting. JMLR, 15:1929–1958, 2014
- Y Gal, J Hron, A Kendall. Concrete Dropout. NIPS'17
- Aidan N. Gomez, Ivan Zhang, Kevin Swersky, Yarin Gal, Geoffrey E. Hinton. Targeted Dropout. ICLR 2019
	- https://github.com/for-ai/TD

## Regularization
- Xavier Gastaldi. Shake-Shake regularization. 2017

## Gumbel-Softmax
- E Jang, S Gu, B Poole. Categorical Reparameterization with Gumbel-Softmax. ICLR'17
<img src="/DL/images/gumbel-softmax.png" alt="drawing" width="500"/>
<img src="/DL/images/gumbel-softmax2.png" alt="drawing" width="500"/>

- Good summaries:
	- https://casmls.github.io/general/2017/02/01/GumbelSoftmax.html
	- https://www.zhihu.com/question/62631725
	- https://blog.csdn.net/a358463121/article/details/80820878
- Make sampling process differentiable;
- Wouter Kool, Herke van Hoof, Max Welling. Stochastic Beams and Where to Find Them: The Gumbel-Top-k Trick for Sampling Sequences Without Replacement. ICML'19 best paper honorable mention
