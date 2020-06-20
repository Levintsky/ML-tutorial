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