# Deep Learning Models

## Unclassified
- Gamaleldin F. Elsayed, Dilip Krishnan, Hossein Mobahi, Kevin Regan, Samy Bengio. Large Margin Deep Networks for Classification. NIPS'18

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

## Differentiable Sampling (Reparametrization Trick)
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
- Gumbel-Softmax:
	- Basics: differentiable sample y s.t. y={v1, v2, ...} with prob {alpha1, alpha2, ...}
	- Gumble distribution:
		- pdf: f(x) = exp(-(x+exp(-x)))
		- cdf: F(x) = exp(-exp(-x))
		- To sample from gumble, **G=-log(-log(U))**, with U ~ Uniform(0, 1)
		- **Key insight**: With prob {alpha1, alpha2, ...}, Gumble var {g1, g2, ...}, then if we let ind=argmax(log alpha_k + gk), then p(ind=k)=alpha_k;
		- Proof: with uk=log a_k+gk, p(ind=k)=int prod p(uj < uk) f(uk) duk, where p(uj < uk) can be obtained from Gumbel cdf F(x)
			<img src="/DL/images/basics/gumbel-proof.png" alt="drawing" width="400"/>
	- Differentiable sampling:
		- argmax is not differentiable;
		- we can use f(x, tau) = softmax(x/tau), for vector x=(x1, x2, ...)
		- then y as a weighted sum of {v1, v2} with prob f(x, tau)
		- y is both differentiable w.r.t. {v1, v2, ...} and {alpha1, alpha2, ...}
		- when tau approaches 0, sampling behavior is exact;
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

## Capsule
- Resources
	- https://www.jiqizhixin.com/articles/2017-11-05
	- https://www.cnblogs.com/wangxiaocvpr/p/7884454.html
	- https://zhuanlan.zhihu.com/p/34336279
- Sara Sabour, Nicholas Frosst. Dynamic Routing Between Capsules. NIPS'17
- Geoffrey Hinton, Sara Sabour, Nicholas Frosst. Matrix Capsules with EM routing. ICLR'18
- Yongheng Zhao, Tolga Birdal, Haowen Deng, Federico Tombari. 3D Point Capsule Networks. CVPR'19
	- Claims: works on both classification and AE, better than AE [ICML'18];
	- https://github.com/yongheng1991/3D-point-capsule-networks
- Z Xinyi, L Chen. Capsule Graph Neural Network. ICLR'19
	- https://docs.google.com/presentation/d/1g48ETPJGzi8xDAWEB53KiYxUCWVHwOBQCePvK5c10Ow/edit#slide=id.g2645f83e45_0_0
- Codes
	- https://github.com/shzygmyx/Matrix-Capsules-pytorch
	- https://github.com/naturomics/CapsNet-Tensorflow
	- https://github.com/gyang274/capsulesEM

## Data Augmentation
- Unclassified
	- **mixup**: Zhang, H., Cisse, M., Dauphin, Y. N., and Lopez-Paz, D. mixup: Beyond empirical risk minimization. arXiv'17
- Legacy
	- Bellegarda, J. R., de Souza, P. V., Nadas, A. J., Nahamoo, D., Picheny, M. A., and Bahl, L. R. Robust speaker adaptation using a piecewise linear acoustic mapping. In ICASSP-92
- Vision
	- AlexNet;
	- **cutout**: DeVries, T. and Taylor, G. W. Improved regularization of convolutional neural networks with cutout. arxiv'17
		- useful on CIFAR-10 and not on ImageNet
	- Lopes, R. G., Yin, D., Poole, B., Gilmer, J., and Cubuk, E. D. Improving robustness without sacrificing accu- racy with patch gaussian augmentation. arXiv'19
	- **RandAugment**: Ekin D. Cubuk, Barret Zoph, Jonathon Shlens, and Quoc V. Le. Randaugment: Practical automated data augmentation with a reduced search space. 2019
		- https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet
		- Transformation: identity, autoContrast, equalize, rotate, solarize, color, posterize, contrast, brightness, sharpness, shear-x, shear-y, translate-x, translate-y;
		- Scale 0 - 10 augmentation magnitude;\
			<img src = '/DL/images/augment/randaugment.png' width = '400'>
	- Raphael Gontijo-Lopes, Sylvia J. Smullin, Ekin D. Cubuk, Ethan Dyer. Affinity and Diversity: Quantifying Mechanisms of Data Augmentation. 2020
		- Define Affinity and Diversity: affinity = accuracy gap on validation; diversity = training loss gap;\
			<img src = '/DL/images/augment/affinity.png' width = '400'>
			<img src = '/DL/images/augment/diversity.png' width = '400'>
		- Empiricaly study: the larger the affinity/diversity, the better\
			<img src = '/DL/images/augment/aff-div.png' width = '400'>
- NLP
	- Adams Wei Yu, David Dohan, Minh-Thang Luong, Rui Zhao, Kai Chen, Mohammad Norouzi, and Quoc V Le. Qanet: Combining local convolution with global self-attention for reading comprehension. 2018
- Speech
	- Awni Hannun, Carl Case, Jared Casper, Bryan Catanzaro, Greg Diamos, Erich Elsen, Ryan Prenger, Sanjeev Satheesh, Shubho Sengupta, Adam Coates, et al. Deep speech: Scaling up end-to-end speech recognition. 2014
	- **Specaugment**: Daniel S Park, William Chan, Yu Zhang, Chung-Cheng Chiu, Barret Zoph, Ekin D Cubuk, and
	Quoc V Le. Specaugment: A simple data augmentation method for automatic speech recognition. 2019
- Dataset Reduction
	- Tongzhou Wang, Jun-Yan Zhu, Antonio Torralba, Alexei A. Efros. Dataset Distillation. ICLR'19 reject

# Normalization Operators
- Batch-Norm
	- **Batch Norm**: Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In ICML, 2015.
	<img src="/DL/images/batch-norm.png" alt="drawing" width="500"/>
- Class Conditioned BN:
	- Harm de Vries, Florian Strub, Jeremie Mary, Hugo Larochelle, Olivier Pietquin, and Aaron Courville. Modulating early visual processing by language. NIPS 2017.
- Takeru Miyato, Toshiki Kataoka, Masanori Koyama, and Yuichi Yoshida. **Spectral normalization** for generative adversarial networks. ICLR'18
- **Group Norm**: Y Wu, K He. Group Normalization. ECCV'18
	<img src="/DL/images/group-norm1.png" alt="drawing" width="500"/>
	<img src="/DL/images/group-norm2.png" alt="drawing" width="500"/>
- Layer-Norm: J L Ba, J R Kiros, G E. Hinton. Layer Normalization. 2016
	<img src="/DL/images/layer-norm1.png" alt="drawing" width="500"/>
	<img src="/DL/images/layer-norm2.png" alt="drawing" width="600"/>
- Weight-Norm: Tim Salimans and Diederik Kingma. Weight normalization: A simple reparameterization to accelerate training of deep neural networks. In NIPS, 2016.
	- w = g * (v / ||v||)
	- w is scale invariant to v, and the norm is always g
	- Data-dependent initialization (to make output with invariant scales)
	<img src="/DL/images/weight-norm.png" alt="drawing" width="500"/>
- Instance Norm: Dmitry Ulyanov, Andrea Vedaldi, Victor Lempitsky. Instance Normalization: The Missing Ingredient for Fast Stylization. 2017

## Equivarance
- Maurice Weiler, Mario Geiger, Max Welling, Wouter Boomsma, Taco Cohen. 3D Steerable CNNs: Learning Rotationally Equivariant Features in Volumetric Data. NIPS'18

## Invert NN
- Reconstruct p(x\|z) with prior on x
	- Mahendran, A., and Vedaldi, A. Understanding deep image representations by inverting them. CVPR'15
		- Insight: find x s.t. representation phi(x) match with prior regularization plus a regularization:
			<img src = '/DL/images/dynamic-system/invert-cnn.png' width = '400'>
	- Dosovitskiy, A., and Brox, T. Inverting visual representations with convolutional networks. CVPR'16
		- Insight: find weight w s.t. reconstruction error is minimized; also tried on shallow features such as SIFT, HOG, LBP;\
			<img src = '/DL/images/dynamic-system/invert-cnn.png' width = '400'>
		- Operator: conv + upsample, padding with 0 and keep the value of top-left in a 2 x 2;	