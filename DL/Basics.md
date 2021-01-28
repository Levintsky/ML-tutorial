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

## Reparametrization Trick
- Make sampling process differentiable;
- **Score-function**: the gradient of the log-likelihood function with respect to the parameter vector;
- Reinforce: unbiased but high variance\
	<img src="/DL/images/basics/reinforce.png" alt="drawing" width="400"/>
- Variance reduction: control-variate baseline\
	<img src="/DL/images/basics/var-reduce.png" alt="drawing" width="400"/>
- **DARN**: K. Gregor, I. Danihelka, A. Mnih, C. Blundell, and D. Wierstra. Deep autoregressive networks. arxiv'13
	- First-order Taylor, estimator biased for non-quadratic f:
		<img src="/DL/images/basics/darn.png" alt="drawing" width="400"/>
- **NVIL**: A. Mnih and K. Gregor. Neural variational inference and learning in belief networks. ICML'14
	- Baseline 1: moving average f-bar;
	- Baseline 2: input dependent f(x);
	- Variance normalization /Var(f);
- Straight-Through (ST) estimator:
	- **ST**: Y. Bengio, N. Leonard, and A. Courville. Estimating or propagating gradients through stochastic neurons for conditional computation. arxiv'13
	- J. Chung, S. Ahn, and Y. Bengio. Hierarchical multiscale recurrent neural networks. arXiv'16
	- J. T. Rolfe. Discrete Variational Autoencoders. ArXiv'16
- **MuProp**: S. Gu, S. Levine, I. Sutskever, and A Mnih. MuProp: Unbiased Backpropagation for Stochastic Neural Networks. ICLR'16\
	<img src="/DL/images/basics/muprop.png" alt="drawing" width="400"/>
- **VIMCO**: A. Mnih and D. J. Rezende. Variational inference for monte carlo objectives. arXiv'16
	<img src="/DL/images/basics/vimco.png" alt="drawing" width="400"/>
- Gumbel-Softmax
	- About Gumbel distribution: pdf f(.) and cdf F(.)\
		<img src="/DL/images/basics/gumbel-1.png" alt="drawing" width="400"/>\
		<img src="/DL/images/basics/gumbel-2.png" alt="drawing" width="300"/>\
		<img src="/DL/images/basics/gumbel-3.png" alt="drawing" width="300"/>
	- Gumbel-Max trick:\
		<img src="/DL/images/basics/gumbel-softmax.png" alt="drawing" width="450"/>
	- Proof:\
		<img src="/DL/images/basics/gumbel-proof.png" alt="drawing" width="400"/>
	- C. J. Maddison, A. Mnih, and Y. Whye Teh. The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables. 2016
		- Independently discover the same trick;
	- E Jang, S Gu, B Poole. Categorical Reparameterization with Gumbel-Softmax. ICLR'17
		- Main insight: Gumbel-max trick to make sampling differentiable; the argmax operation is still non-differentiable. When tau approaches 0, equivalent to Gumbel:\
			<img src="/DL/images/basics/gumbel-softmax2.png" alt="drawing" width="500"/>
		- True Gumbel-softmax distribution:\
			<img src="/DL/images/basics/gumbel-softmax-true.png" alt="drawing" width="500"/>
	- Good summaries:
		- https://casmls.github.io/general/2017/02/01/GumbelSoftmax.html
		- https://www.zhihu.com/question/62631725
		- https://blog.csdn.net/a358463121/article/details/80820878
		- https://laurent-dinh.github.io/2016/11/22/gumbel-max.html