# Optimization for Deep Learning

## Unclassified
- Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. 2018
- Provably Correct Automatic Sub-Differentiation for Qualified Programs. NIPS'18
- L4: Practical loss-based stepsize adaptation for deep learning
- Natasha 2: Faster Non-Convex Optimization Than SGD. NIPS'18
- Learning with SGD and Random Features. NIPS'18

## Loss Surface
- A. Choromanska, M. Henaff, M. Mathieu, G. B. Arous, and Y. LeCun. The Loss Surfaces of Multilayer Networks. JMLR'15
- J. Pennington and Y. Bahri. Geometry of neural network loss surfaces via random matrix theory. ICML'16
- S. Mei, A. Montanari, and P.-M. Nguyen. A mean field view of the landscape of two-layer neural networks. PNAS'18
- L. Sagun, U. Evci, V. U. Guney, Y. Dauphin, and L. Bottou. Empirical analysis of the hessian of over-parametrized neural networks. CoRR'17

## Saddle Point
- Y. N. Dauphin, R. Pascanu, C. Gulcehre, K. Cho, S. Ganguli, and Y. Bengio. Identifying and attacking the saddle point problem in high-dimensional non-convex optimization. NIPS'14
- R. Pascanu, Y. N. Dauphin, S. Ganguli, and Y. Bengio. On the saddle point problem for non-convex optimization. arxiv'14

## SGD Dynamics
- SGD prefers flat minima, flatter minima seem to generalize  better:
	- S. Hochreiter and J. Schmidhuber. Flat minima. NC'97
	- N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, and P. T. P. Tang. On large-batch training for deep learning: Generalization gap and sharp minima. ICLR'17
	- L Wu, Z Zhu, and W E. Towards understanding generalization of deep learning: Perspective of loss landscapes. arxiv'17
- Learning rate and batch size:
	- P Goyal, et. al. Accurate, large minibatch sgd: training imagenet in 1 hour. arxiv'17
	- E Hoffer, I Hubara, and D Soudry. Train longer, generalize better: closing the generalization gap in large batch training of neural networks. NIPS'17
	- S Jastrzebski, Z Kenton, D Arpit, N Ballas, A Fischer, Y Bengio, and A Storkey. Three factors influencing minima in sgd. arxiv'17
		- the ratio between the learning rate and the batch size η/B is a key factor for flatness;
	- Z Zhu, J Wu, B Yu, L Wu, and J Ma. The anisotropic noise in stochastic gradient descent: Its behavior of escaping from minima and regularization effects. arxiv'18
		- the specific non-isotropic structure of the noise is important for SGD to find flat minima;
		- minima found by GD (gradient decent) can be unstable for SGD;
- Convergence:
	- L Wu, C Ma, W E. How SGD Selects the Global Minima in Over-parameterized Learning: A Dynamical Stability Perspective. NIPS'18
		- GD to SGD: escape from minimum and converge to another;
		- Def3. Sharpness, non-uniformity. Let H = 1/nΣHi, Σ=1/nΣi=1..n Hi^2-H^2, We define a = max(H) to be the sharpness, and s = max(Σ^1/2) to be the non-uniformity, respectively.

## Beyond SGD
- S. Günther, L. Ruthotto, J.B. Schroder, E.C. Cyr, N.R. Gauger. Layer-Parallel Training of Deep Residual Neural Networks. 2019
	- Training layer-parallel rather than sequential, with inexact gradient info;
- Capsule:
	- Resources
		- https://www.jiqizhixin.com/articles/2017-11-05
		- https://www.cnblogs.com/wangxiaocvpr/p/7884454.html
		- https://zhuanlan.zhihu.com/p/34336279
	- S Sabour, N Frosst. Dynamic Routing Between Capsules. NIPS'17
	- G Hinton, S Sabour, N Frosst. Matrix Capsules with EM routing. ICLR'18
	- Y Zhao, T Birdal, H Deng, F Tombari. 3D Point Capsule Networks. CVPR'19
		- Claims: works on both classification and AE, better than AE [ICML'18];
		- https://github.com/yongheng1991/3D-point-capsule-networks
	- Z Xinyi, L Chen. Capsule Graph Neural Network. ICLR'19
		- https://docs.google.com/presentation/d/1g48ETPJGzi8xDAWEB53KiYxUCWVHwOBQCePvK5c10Ow/edit#slide=id.g2645f83e45_0_0
	- Codes
		- https://github.com/shzygmyx/Matrix-Capsules-pytorch
		- https://github.com/naturomics/CapsNet-Tensorflow
		- https://github.com/gyang274/capsulesEM