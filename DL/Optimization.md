# Optimization Methods

## Loss Design
- Visualizing the Loss Landscape of Neural Nets. NIPS'18

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
- Natural Gradient (check RL section):
	- Left multiplying inverse of Fisher Information Matrix
	- Exact natural gradient in deep linear networks and application to the nonlinear case. NIPS'18
	- Fast Approximate Natural Gradient Descent in a Kronecker Factored Eigenbasis. NIPS'18
- **KFAC**: J. Martens and R. Grosse. Optimizing neural networks with kronecker-factored approximate curvature. 2015
	- Kronecker approximation to Fisher
- **FANG**: R. Grosse and R. Salakhudinov. Scaling up natural gradient by sparsely factorizing the inverse fisher matrix.
	- Cholesky decomposition.
- **PRONG**: G. Desjardins, K. Simonyan, R. Pascanu, et.al. Natural neural networks. NIPS 2015
	- Whitening each layer.

## Noise
- Mirrored Langevin Dynamics. NIPS'18
- The promises and pitfalls of Stochastic Gradient Langevin Dynamics. NIPS'18

## SVGD
- Stein variational gradient descent: A general purpose bayesian inference algorithm, NIPS'16
	- https://github.com/DartML/Stein-Variational-Gradient-Descent

## Variance Reduction:
- UCLA. Stochastic Nested Variance Reduced Gradient Descent for Nonconvex Optimization. NIPS'18
- SEGA: Variance Reduction via Gradient Sketching. NIPS'18
- Stochastic Expectation Maximization with Variance Reduction. NIPS'18

## Large-Scale
- R Anil, V Gupta, T Koren, and Y Singer. Memory-efficient adaptive optimization for large-scale learning. 2019
- Frank Wood. Bayesian Distributed Stochastic Gradient Descent. NIPS'18

## Mix-Integer Programming (MIP)
- Take-aways:
	- These types of trained networks can be modeled as a MIP and embedded into another optimization problem.
	- there are ways to accelerate the solution process of these MIPs by understanding the polyhedral geometry
- MIP commercial solver: gurobi
- M Fischetti and J Jo. Deep Neural Networks as 0-1 Mixed Integer Linear Programs: A Feasibility Study. 2017
	- x = RELU(wy+b)
	- option 1: wy+b=x-s, s.t., x >= 0, s >= 0;
	- option 2: z = 0,1 for +/-, 
- R Anderson, J Huchette, W Ma, C Tjandraatmadja, J Vielma. Strong mixed-integer programming formulations for trained neural networks. 2019
	- Contained in tf.opt, will be open source;
	- Experiments: Faster MNIST;
- M Ryu, Y Chow, R Anderson, C Tjandraatmadja, C Boutilier. CAQL: Continuous Action Q-Learning. ICLR'20

## Optimization as a layer
- A Ferber, B Wilder, B Dilkina, M Tambe. MIPaaL: Mixed Integer Program as a Layer. 2019
	- Take-away: We can handle "hard convex problems" using cutting planes
	- Forward Pass: solve MIP
	- Backward Pass: construct an LP to approximate the MIP exactly at the solution using cutting planes;
- **cvxlayers**: A Agrawal, B Amos, S Barratt, S Boyd, S Diamond, and Z Kolter. Differentiable Convex Optimization Layers. NIPS'19
	- https://github.com/cvxgrp/cvxpylayers (support both pytorch and tf)

## Unclassified
- Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. 2018
- Provably Correct Automatic Sub-Differentiation for Qualified Programs. NIPS'18
- L4: Practical loss-based stepsize adaptation for deep learning
