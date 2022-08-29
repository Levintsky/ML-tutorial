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
	- Batch GD: batch-sze = whole training set;
	- SGD: θ = θ - η∇θ J(θ;xi, yi)
	- SGD with mini-batch: θ = θ - η∇θ J(θ;xi..i+n, yi..i+n)
- Gradient descent optimization algorithms:
	- Momentum: Qian, N. On the momentum term in gradient descent learning algorithms. 1999
		- vt = γ vt-1 + η∇θ J(θ), average of historical gradient
		- θ = θ - vt
	- **NAG (Nestorov)**: Y Nesterov. A method for unconstrained convex minimization problem with the rate of convergence o(1/k2). 1983
		- vt = γ vt-1 + η∇θ J(θ-γvt-1), average of historical gradient
		- θ = θ - vt
	- **AdaGrad**: J Duchi, E Hazan, and Y Singer. Adaptive subgradient methods for online learning and stochastic optimization. JMLR'11
		- Insight: It adapts the learning rate to the parameters, performing smaller updates (i.e. low learning rates) for parameters associated with frequently occurring features, and larger updates (i.e. high learning rates) for parameters associated with infrequent features
		- Adagrad's main weakness is its accumulation of the squared gradients in the denominator: gradient diminish;
		- Let s ∈ Rd, H ∈ Rdxd,
		- Get subgradient: gt = ∇f(xt);
		- Ht = δI + diag(st), Ψt(x)=1/2(x, Htx)
		- Primal-dual subgradient: xt+1 = argmin_x[η(1/tΣgt,x)+ηφ(x)+1/t Ψt]
		- Compositve Mirror decent: xt+1 = argmin_x[η(gt,x)+ηφ(x)+BΨt(x,xt)]
	- **AdaDelta**: M Zeiler. ADADELTA: An Adaptive Learning Rate Method. 2012
		- Improves over adagrad
		<img src="/Optimization/images/sgd/adadelta.png" alt="drawing" width="500"/>
	- **Rmsprop**:
		- E[g^2]t = 0.9E[g^2]t-1 + 0.1 gt^2; average 2nd-order momentum
		- θt+1 = θt - η/sqrt(E[g^2]t+ε)gt; normalize gradient by 2nd-order momentum
	- **ADAM**: D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. ICLR'15
		- Whereas momentum can be seen as a ball running down a slope, Adam behaves like a heavy ball with friction, which thus prefers flat minima in the error surface;
		- Let β1, β2 be exponentil decay rates of momentum; m0=0, v0=0;
		- gt = ∇θft(θt-1), gradient at timestep t;
		- mt = β1 mt-1 + (1-β1) gt; 1st-order moment;
		- vt = β2 vt-1 + (1-β2) gt^2; 2st-order moment;
		- mt' = mt/(1-β1^t); correct bias;
		- vt' = mt/(1-β2^t); correct bias;
		- θt+1 = θt - ηmt/sqrt(E[g^2]t+ε);
	- AdaMax
	- Nadam
	- AMSGrad
	- Other recent optimizers
	- Visualization of algorithms
	- Which optimizer to use?
- Legacy: Robbins, H. and Monro, S. A stochastic approximation method. Annals of Mathematical Statistics, 1951.
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

## Basics
- Struggle to improve over first-order baselines for non-convex loss surfaces;
- Intuition for natural gradient:
	- 2nd order: Left multiplying inverse of Fisher Information matrix
	- Fisher Information Matrix:
		- PSD (positive semi-definite);
	- Differential manifold on probability measure;

## SVGD
- Qiang Liu, Dilin Wang. Stein variational gradient descent: A general purpose bayesian inference algorithm, NIPS'16
	- https://github.com/DartML/Stein-Variational-Gradient-Descent
