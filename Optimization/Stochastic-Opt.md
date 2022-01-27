# SGD

## Summaries
- http://ruder.io/optimizing-gradient-descent/
- Heavily used in neural networks;
- A summary:
	- GD: batch/mini-batch sgd;
	- SGD: Momentum, Nesterov accelerated gradient, Adagrad, Adadelta, RMSprop, Adam, AdaMax, Nadam, AMSGrad
	- Parallel/distributed: Hogwild!, Downpour SGD, Delay-tolerant Algorithms for SGD, TensorFlow, Elastic Averaging SGD
	- Additional strategies: Shuffling and Curriculum Learning, Batch normalization, Early Stopping, Gradient noise

## 1st-Order
- GD:
	- Batch GD: batch-sze = whole traning set;
	- SGD:\
		<img src="/Optimization/images/sgd/sgd.png" alt="drawing" width="200"/>
	- SGD with mini-batch:\
		<img src="/Optimization/images/sgd/sgd-batch.png" alt="drawing" width="200"/>
- Gradient descent optimization algorithms:
	- Momentum: Qian, N. On the momentum term in gradient descent learning algorithms. 1999\
		<img src="/Optimization/images/sgd/momentum.png" alt="drawing" width="200"/>
	- **NAG (Nestorov)**: Y Nesterov. A method for unconstrained convex minimization problem with the rate of convergence o(1/k2). 1983\
		<img src="/Optimization/images/sgd/nag.png" alt="drawing" width="200"/>
	- **AdaGrad**: J Duchi, E Hazan, and Y Singer. Adaptive subgradient methods for online learning and stochastic optimization. JMLR'11
		- Insight: It adapts the learning rate to the parameters, performing smaller updates (i.e. low learning rates) for parameters associated with frequently occurring features, and larger updates (i.e. high learning rates) for parameters associated with infrequent features
		- Adagrad's main weakness is its accumulation of the squared gradients in the denominator: gradient diminish;
		<img src="/Optimization/images/sgd/adagrad.png" alt="drawing" width="450"/>
	- **AdaDelta**: M Zeiler. ADADELTA: An Adaptive Learning Rate Method. 2012
		- Improves over adagrad
		<img src="/Optimization/images/sgd/adadelta.png" alt="drawing" width="500"/>
	- **Rmsprop**:\
		<img src="/Optimization/images/sgd/rmsprop.png" alt="drawing" width="300"/>
	- **ADAM**: D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. ICLR'15
		- Whereas momentum can be seen as a ball running down a slope, Adam behaves like a heavy ball with friction, which thus prefers flat minima in the error surface
		<img src="/Optimization/images/sgd/adam.png" alt="drawing" width="500"/>
	- AdaMax
	- Nadam
	- AMSGrad
	- Other recent optimizers
	- Visualization of algorithms
	- Which optimizer to use?
- U Şimşekli，L Sagun, M Gürbüzbalaban. A Tail-Index Analysis of Stochastic Gradient Noise in Deep Neural Networks. ICML'19 best paper honorable mention

## Parallel/Distributed
- **Hogwild!**: Niu, F., Recht, B., Christopher, R., & Wright, S. J. . Hogwild!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent. 2011
- **Downpour SGD**: used in DistBelief, at risk of Diverging;
- Tensorflow;
- **EASGD** Elastic Averaging SGD: Zhang, S., Choromanska, A., & LeCun, Y. Deep learning with Elastic Averaging SGD. NIPS'15
- R Anil, V Gupta, T Koren, and Y Singer. Memory-efficient adaptive optimization for large-scale learning. 2019
- Frank Wood. Bayesian Distributed Stochastic Gradient Descent. NIPS'18

## Additional strategies for optimizing SGD
- Shuffling and Curriculum Learning
- Batch normalization
- Early stopping
- Gradient noise: Neelakantan, A., Vilnis, L., Le, Q. V., Sutskever, I., Kaiser, L., Kurach, K., & Martens, J. Adding Gradient Noise Improves Learning for Very Deep Networks. 2015

## Unclassified
- Zeyuan Zhu. The Lingering of Gradients: How to Reuse Gradients Over Time. NIPS'18
- Wotao Yin. On Markov Chain Gradient Descent. NIPS'18

## 2nd-Order Optimizer

## Basics
- Struggle to improve over first-order baselines for non-convex loss surfaces;
- Intuition for natural gradient:
	- 2nd order: Left multiplying inverse of Fisher Information matrix
	- Fisher Information Matrix:
		- PSD (positive semi-definite);
	- Differential manifold on probability measure;

## Natural Gradient
- Resources and Tutorials:
	- Relation with Gauss-Newton
	- https://www.zhihu.com/question/266846405
	- https://zhuanlan.zhihu.com/p/82934100
	- James Martens. New insights and perspectives on the natural gradient method. 2017
		- Geometric interpretation: the steepest change of KL(P(theta+d)||P(theta)), locally symmetric;
- Legacy:
	- S.-I. Amari. Natural gradient works efficiently in learning. Neural Computation, 10(2): 251–276, 1998.
	- S.-i. Amari and A. Cichocki. Adaptive blind signal processing-neural network approaches. Proceedings of the IEEE, 86(10):2026–2048, 1998.
	- S.-i. Amari and H. Nagaoka. Methods of information geometry, volume 191. American Mathematical Soc., 2007.
- Alberto Bernacchia, Mate Lengyel, Guillaume Hennequin. Exact natural gradient in deep linear networks and application to the nonlinear case. NIPS'18
- Thomas George, César Laurent, Xavier Bouthillier, Nicolas Ballas, Pascal Vincent. Fast Approximate Natural Gradient Descent in a Kronecker Factored Eigenbasis. NIPS'18
- **FANG**: R. Grosse and R. Salakhudinov. Scaling up natural gradient by sparsely factorizing the inverse fisher matrix.
	- Cholesky decomposition.
- Octavian-Eugen Ganea, Gary Bécigneul, Thomas Hofmann. Hyperbolic Neural Networks. NIPS'18
- Higher-order:
	- Yang Song, Jiaming Song, Stefano Ermon. Accelerating Natural Gradient with Higher-Order Invariance. ICML'18
		- https://ermongroup.github.io/blog/geo/

## Low-Rank Approximation
- Martens, James. Deep learning via hessian-free optimization. ICML'10
- **KFAC**: J. Martens and R. Grosse. Optimizing neural networks with kronecker-factored approximate curvature. ICML'15
	- Kronecker approximation to Fisher
	- Assumption: FC (si = Wi\* ai) + non-linear (ai = phi(si)), then DWi=gi x ai-1, Fisher:\
		<img src="/Optimization/images/2nd/k-fac1.png" alt="drawing" width="400"/>
	- Approx:\
		<img src="/Optimization/images/2nd/k-fac2.png" alt="drawing" width="400"/>
- R. Grosse and J. Martens. A Kronecker-factored approximate Fisher matrix for convolutional layers. ICML'16
	- Follow-up on KFAC for convolutions
- Instability:
	- Byrd, R., Hansen, S., Nocedal, J., and Singer, Y. A stochastic quasi-newton method for large-scale optimization. SIAM Journal on Optimization'16
- Estimate the metric:
	- Pascanu, Razvan and Bengio, Yoshua. Revisiting natural gradient for deep networks. ICLR'14
	- KFAC. ICML'15
	- **PRONG**: G. Desjardins, K. Simonyan, R. Pascanu, et.al. Natural neural networks. NIPS'15
		- Whitening each layer.

## SVGD
- Qiang Liu, Dilin Wang. Stein variational gradient descent: A general purpose bayesian inference algorithm, NIPS'16
	- https://github.com/DartML/Stein-Variational-Gradient-Descent
