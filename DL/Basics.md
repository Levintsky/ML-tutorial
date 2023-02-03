# Deep Learning Basics

## Resources
- Tutorials
	- Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. nature, 521(7553):436, 2015.
- Books
	- **Deep learning**: I Goodfellow, Y Bengio, Aaron Courville, and Yoshua Bengio. volume 1. MIT press Cambridge, 2016.

## Unclassified
- Gamaleldin F. Elsayed, D Krishnan, H Mobahi, K Regan, Samy Bengio. Large Margin Deep Networks for Classification. NIPS'18

## PRML (Chapter 5)
- Feed-forward:
	- Notation: aj = Σi w_ji xi + wj0;
	- Weight space symmetry: tanh(-a) = -tanh(a);
	- Target regression: p(t|w, x) = N(y(x, w), β^(-1)), with β as the precision;
	- Cross entropy loss: -Σ t_k ln y_k(x, w), with softmax;
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

## Operator Design
- Invariance:
	- Conv, pooling;
- Equivarance:
	- Maurice Weiler, Mario Geiger, Max Welling, Wouter Boomsma, Taco Cohen. 3D Steerable CNNs: Learning Rotationally Equivariant Features in Volumetric Data. NIPS'18
	- Esteves, C., Allen-Blanchette, C., Makadia, A., and Daniilidis, K. Learning SO(3) equivariant representations with spherical CNNs. ECCV'18

## Activation
- **ReLU**: Nair, V. and Hinton, G. E. Rectified linear units improve restricted boltzmann machines. ICML'10
	- xI(x>0)
- **Leaky-ReLU**;
- **GeLU**: Dan Hendrycks, Kevin Gimpel. Gaussian Error Linear Units (GELUs). '16
	- Smoother than ReLU;
	- Used in BERT and GPT-3;
- **SENet**: J Hu, L Shen, G Sun. Squeeze-and-Excitation Networks. CVPR'18
	- https://github.com/hujie-frank/SENet
	- Insight: channel-wise scaling (learn by MLP);
	- Model: channel-wise selection/attention;
		- For a HxWxC feature x, calculate channel-wise W 1x1xC;
		- Then apply the weight channel-wise: W x

## Normalization Operators
- **Batch Norm**: S Ioffe and C Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. ICML'15
	- Insight: normalize NxHxW pixels with same channel-idx;
	- μ, σ^2: batch mean, variance;
	- x = (x-μ) / √(σ^2+ε)
	- y = γx + β
	- Moving mean and variance for inference time;
- **Layer-Norm**: J L Ba, J R Kiros, G E. Hinton. Layer Normalization. 2016
	- Insight: normalize dxHxW pixels within the same instance, no batch required;
	- Same eqn as BN: x = (x-μ) / √(σ^2+ε)
- **Weight-Norm**: Tim Salimans and Diederik Kingma. Weight normalization: A simple reparameterization to accelerate training of deep neural networks. NIPS'16
	- Insight: weight w is scale invariant to v, and the norm is always g;
	- y = φ(wx+b)
	- w = gv / |v|
	- Data-dependent initialization (to make output with invariant scales)
	- ∇g L, ∇v L, ∇w L: check paper derivation;
- **Instance Norm**: D Ulyanov, A Vedaldi, V Lempitsky. Instance Normalization: The Missing Ingredient for Fast Stylization. 2017
	- Same as BN and Layer-Norm, normalize within HxW for each channel, no batch required;
- **Class-BN**: H Vries, F Strub, J Mary, H Larochelle, O Pietquin, and A Courville. Modulating early visual processing by language. NIPS'17.
	- Class Conditioned BN;
- **Spectral normalization**: T Miyato, T Kataoka, M Koyama, and Y Yoshida. Spectral normalization for generative adversarial networks. ICLR'18
	- Insight: W-GAN need D() to be K-Lipschitz;
		- |Ax| <= K|x|
		- (Ax, Ax) <= K^2 (x, x)
		- ((A'A-K^2)x, x) <= 0
		- ∑(K^2-λi)xi^2 >= 0, or K^2 >= λi always holds;
		- **spectral norm** of a matrix: largest singular value;
	- Composition: upper bound of function composition;
		- |g f|Lip <= |g|Lip |f|Lip
	- v = W'Wv / |W'Wv|
		- Scale each principal vec by λi/λ1;
		- Do infinite times: v = e1 (principal of λ1)
	- In practice, finite times:
		- Forward of a normal layer (e.g. conv, fc), update weight first:
			- u(t+1) = L2-norm[W v(t)]
			- v(t+1) = L2-norm[W' u(t+1)]
			- Spectral-norm of W: σ(W) = |Wv| = uWv;
			- W = W/σ(W) guarantee Lipschitz always holds;
		- Normal forward: y = Wx...
- **Group Norm**: Y Wu, K He. Group Normalization. ECCV'18
	- Similar to BN, layer-N, IN;
	- Divide channel into groups Dim = d g;
	- Average over HWd, each group has same μ and σ;
		- Between Layer-norm and IN;

## Dropout
- N Srivastava, G Hinton, A Krizhevsky, I Sutskever, and R Salakhutdinov. Dropout: A simple way to prevent neural networks from overfitting. JMLR, 15:1929–1958, 2014
- Y Gal, J Hron, A Kendall. Concrete Dropout. NIPS'17
- A Gomez, I Zhang, K Swersky, Y Gal, G Hinton. Targeted Dropout. ICLR 2019
	- https://github.com/for-ai/TD

## Regularization
- Behnam Neyshabur, Ryota Tomioka, Nathan Srebro. In Search of the Real Inductive Bias: On the Role of Implicit Regularization in Deep Learning. ICLR'15
- Xavier Gastaldi. Shake-Shake regularization. 2017

## Differentiable Sampling (Reparametrization Trick)
- Make sampling process differentiable;
- **Score-function**: the gradient of the log-likelihood function with respect to the parameter vector;
	- s(θ) = ∂logL(θ)/∂θ; L: likelihood;
- Reinforce: unbiased but high variance:
	- ∇θ Ez[f(z)] = Ez[f(z) ∇θlogp(z;θ)]
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
	- Basics: differentiable sample y s.t. y={v1, v2, ...} with prob {α1, α2, ...}
	- Gumbel distribution:
		- pdf: f(x) = exp(-(x+exp(-x)))
		- cdf: F(x) = exp(-exp(-x))
		- To sample from gumbel, **G=-log(-log(U))**, with U ~ Uniform(0, 1)
	- **Key insight**: sample {z1, z2, ...} with prob {α1, α2, ...}:
		- Sample Gumbel var {g1, g2, ...} ~ -log(-log(u));
		- Let ind = argmax(log α_k + gk)
		- Then p(ind=k) = α_k;
	- Proof: with uk=log α_k+gk,
		- p(ind=k) = ∫ Πp(uj < uk) f(uk) duk
		- p(uj < uk) ~ Gumbel cdf F(x);
		- f(uk) ~ Gumbel pdf;
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
- M Figurnov, S Mohamed, A Mnih. Implicit Reparameterization Gradients. NIPS'18
- Wonyeol Lee, Hangyeol Yu, Hongseok Yang. Reparameterization Gradient for Non-differentiable Models. NIPS'18

## Memory-Augmented NN
- C. G. Atkeson and S. Schaal. Memory-based neural networks for robot learning. Neurocomputing, 9:243–269, 1995.
- End-To-End Memory Networks

## Invert NN
- Invertible/reversible:
	- D. Maclaurin, D. K. Duvenaud, and R. P. Adams. Gradient-based hyperparameter optimization through reversible learning. ICML'15
		- made use of the reversible nature of SGD to tune hyperparameters via GD;
	- NICE: unit determinant Jacobian;
		- y1 = x1;
		- y2 = x2 + F(x1);
	- Real NVP:
		- y1 = x1;
		- y2 = x2 exp(F(x1)) + G(x1)
	- **RevNet**: A Gomez, M Ren, R Urtasun, R Grosse. The Reversible Residual Network: Backpropagation Without Storing Activations. NIPS'17
- Reconstruct p(x|z) with prior on x
	- Mahendran, A., and Vedaldi, A. Understanding deep image representations by inverting them. CVPR'15
		- Insight: find x s.t. representation φ(x) match with prior regularization plus a regularization:
			<img src = '/DL/images/dynamic-system/invert-cnn.png' width = '400'>
	- Dosovitskiy, A., and Brox, T. Inverting visual representations with convolutional networks. CVPR'16
		- Insight: find weight w s.t. reconstruction error is minimized; also tried on shallow features such as SIFT, HOG, LBP;\
			<img src = '/DL/images/dynamic-system/invert-cnn.png' width = '400'>
		- Operator: conv + upsample, padding with 0 and keep the value of top-left in a 2 x 2;	