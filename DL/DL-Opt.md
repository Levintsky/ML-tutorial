# Optimization for Deep Learning

## Unclassified
- Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. 2018
- Provably Correct Automatic Sub-Differentiation for Qualified Programs. NIPS'18
- L4: Practical loss-based stepsize adaptation for deep learning
- Natasha 2: Faster Non-Convex Optimization Than SGD. NIPS'18
- Learning with SGD and Random Features. NIPS'18

## NIPS'19
- Difan Zou, Quanquan Gu. An Improved Analysis of Training Over-parameterized Deep Neural Networks
- Matan Atzmon, Niv Haim, Lior Yariv, Ofer Israelov, Haggai Maron, Yaron Lipman. Controlling Neural Level Sets
- Shaojie Bai, J. Zico Kolter, Vladlen Koltun. Deep Equilibrium Models
- Junbang Liang, Ming Lin, Vladlen Koltun. Differentiable Cloth Simulation for Inverse Problems
- Mahyar Fazlyab, Alexander Robey, Hamed Hassani, Manfred Morari, George Pappas. Efficient and Accurate Estimation of Lipschitz Constants for Deep Neural Networks
- Yuan Cao, Quanquan Gu. Generalization Bounds of Stochastic Gradient Descent for Wide and Deep Neural Networks
- Lili Su, Pengkun Yang. On Learning Over-parameterized Neural Networks: A Functional Approximation Perspective
- Zhuoning Yuan, Yan Yan, Rong Jin, Tianbao Yang. Stagewise Training Accelerates Convergence of Testing Error Over SGD
- Yuanzhi Li, Colin Wei, Tengyu Ma. Towards Explaining the Regularization Effect of Initial Large Learning Rate in Training Neural Networks
- Dinghuai Zhang, Tianyuan Zhang, Yiping Lu, Zhanxing Zhu, Bin Dong. You Only Propagate Once: Accelerating Adversarial Training via Maximal Principle
- Florian Scheidegger, Luca Benini, Costas Bekas, A. Cristiano I. Malossi. Constrained deep neural network architecture search for IoT devices accounting for hardware calibration
- Gauthier Gidel, Francis Bach, Simon Lacoste-Julien. Implicit Regularization of Discrete Gradient Dynamics in Linear Neural Networks
- Hui Guan, Lin Ning, Zhen Lin, Xipeng Shen, Huiyang Zhou, Seung-Hwan Lim. In-Place Zero-Space Memory Protection for CNN
- Stanislav Fort, Stanislaw Jastrzebski. Large Scale Structure of Neural Network Loss Landscapes
- Zeyuan Allen-Zhu, Yuanzhi Li, Yingyu Liang. Learning and Generalization in Overparameterized Neural Networks, Going Beyond Two Layers
- Frederik Kunstner, Philipp Hennig, Lukas Balles. Limitations of the empirical Fisher approximation for natural gradient descent
- Michael Arbel, Anna Korba, Adil SALIM, Arthur Gretton. Maximum Mean Discrepancy Gradient Flow
- Lénaïc Chizat, Edouard Oyallon, Francis Bach. On Lazy Training in Differentiable Programming
- Sébastien Arnold, Pierre-Antoine Manzagol, Reza Babanezhad Harikandeh, Ioannis Mitliagkas, Nicolas Le Roux. Reducing the variance in online optimization by transporting past gradients
- Yuan Cao, Quanquan Gu. Tight Sample Complexity of Learning One-hidden-layer Convolutional Neural Networks
- Jingjing Xu, Xu Sun, Zhiyuan Zhang, Guangxiang Zhao, Junyang Lin. Understanding and Improving Layer Normalization
- Janice Lan, Rosanne Liu, Hattie Zhou, Jason Yosinski. LCA: Loss Change Allocation for Neural Network Training

## Loss Surface
- A. Choromanska, M. Henaff, M. Mathieu, G. B. Arous, and Y. LeCun. The Loss Surfaces of Multilayer Networks. JMLR'15
- J. Pennington and Y. Bahri. Geometry of neural network loss surfaces via random matrix theory. ICML'16
- S. Mei, A. Montanari, and P.-M. Nguyen. A mean field view of the landscape of two-layer neural networks. PNAS'18
- L. Sagun, U. Evci, V. U. Gu ̈ney, Y. Dauphin, and L. Bottou. Empirical analysis of the hessian of over-parametrized neural networks. CoRR'17

## Saddle Point
- Y. N. Dauphin, R. Pascanu, C. Gulcehre, K. Cho, S. Ganguli, and Y. Bengio. Identifying and attacking the saddle point problem in high-dimensional non-convex optimization. NIPS'14
- R. Pascanu, Y. N. Dauphin, S. Ganguli, and Y. Bengio. On the saddle point problem for non-convex optimization. arxiv'14

## SGD Dynamics
- SGD prefers flat minima, flatter minima seem to generalize  better:
	- S. Hochreiter and J. Schmidhuber. Flat minima. NC'97
	- N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, and P. T. P. Tang. On large-batch training for deep learning: Generalization gap and sharp minima. ICLR'17
	- Lei Wu, Zhanxing Zhu, and Weinan E. Towards understanding generalization of deep learning: Perspective of loss landscapes. arxiv'17
- Learning rate and batch size:
	- Priya Goyal, Piotr Dollár, Ross Girshick, Pieter Noordhuis, Lukasz Wesolowski, Aapo Kyrola, Andrew Tulloch, Yangqing Jia, and Kaiming He. Accurate, large minibatch sgd: training imagenet in 1 hour. arxiv'17
	- Elad Hoffer, Itay Hubara, and Daniel Soudry. Train longer, generalize better: closing the generalization gap in large batch training of neural networks. NIPS'17
	- Stanisław Jastrz˛ebski, Zachary Kenton, Devansh Arpit, Nicolas Ballas, Asja Fischer, Yoshua Bengio, and Amos Storkey. Three factors influencing minima in sgd. arxiv'17
		- the ratio between the learning rate and the batch size η/B is a key factor for flatness;
	- Zhanxing Zhu, Jingfeng Wu, Bing Yu, Lei Wu, and Jinwen Ma. The anisotropic noise in stochastic gradient descent: Its behavior of escaping from minima and regularization effects. arxiv'18
		- the specific non-isotropic structure of the noise is important for SGD to find flat minima;
		- minima found by GD (gradient decent) can be unstable for SGD;
- Convergence:
	- Lei Wu, Chao Ma, Weinan E. How SGD Selects the Global Minima in Over-parameterized Learning: A Dynamical Stability Perspective. NIPS'18
		- GD to SGD: escape from minimum and converge to another;
		- Def3. Sharpness, non-uniformity. Let H = 1/nΣHi, Σ=1/nΣi=1..n Hi^2-H^2, We define a = max(H) to be the sharpness, and s = max(Σ^1/2) to be the non-uniformity, respectively.

## Beyond SGD
- S. Günther, L. Ruthotto, J.B. Schroder, E.C. Cyr, N.R. Gauger. Layer-Parallel Training of Deep Residual Neural Networks. 2019
	- Training layer-parallel rather than sequential, with inexact gradient info;