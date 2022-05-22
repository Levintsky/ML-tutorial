# Dynamic System View

## Unclassified
- Sonoda, Sho and Murata, Noboru. Double continuum limit of deep neural networks. ICML Workshop'17

## NN Inspired by ODE/PDE
- ODE:
	- Bao Wang, Binjie Yuan, Zuoqiang Shi, Stanley J. Osher. ResNets Ensemble via the Feynman-Kac Formalism to Improve Natural and Robust Accuracies. 2018
	- **Forward Euler**, or 1st-order Runge-Kutta (ResNet, RevNet, ResNeXt):
		- Bo Chang, Lili Meng, Eldad Haber, Frederick Tung, David Begert Multi-level residual networks from dynamical systems view. ICLR'18
			- Insight: multi-grid ODE; allow adding new layers if current time resolution not sufficient for modeling;
				<img src = '/DL/images/dynamic-system/multi-level-resnet.png' width = '400'>
		- **i-ResNet**: Jens Behrmann, Will Grathwohl, Ricky T. Q. Chen, David Duvenaud, Jörn-Henrik Jacobsen. Invertible Residual Networks. ICML'19
			- Main insight: same as RevNet and flow-based methods. but **free-form**; A comparison:\
				<img src = '/DL/images/dynamic-system/i-resnet-4.png' width = '400'>
			- https://github.com/jhjacobsen/invertible-resnet
			- With contractive g(), i.e., Lip(g(theta)) < 1, so **Spectral-Norm** layer added to make constraint always satisfied. Then backward Euler to compute x(t+1) from x(t) as fixed point:\
				<img src = '/DL/images/dynamic-system/i-resnet-1.png' width = '400'>
			- For generative model, ln(px(x)) = ln(pz(z))+ln|det(JF(x))|, with JF as the Jacobian of F(), since F=I+g() as the residual block, we could have a Taylor expansion.\
				<img src = '/DL/images/dynamic-system/i-resnet-2.png' width = '400'>
			- Three computation drawbacks: (1) evaluate tr(J); (2) power of J; (3) Taylor has infinite terms;
			- For (1), (2), the approximate trick;
			- For (3), truncated at n steps;
			- The algorithm:\
				<img src = '/DL/images/dynamic-system/i-resnet-3.png' width = '400'>
- PDE:
	- Haber, E.; Ruthotto, L.; and Holtham, E. Learning across scales- multiscale methods for convolution neural networks. AAAI'17
		- Supervised learning from optimal control formulation;\
			<img src = '/DL/images/dynamic-system/multi-scale-1.png' width = '400'>
		- The algorithm:\
			<img src = '/DL/images/dynamic-system/multi-scale-2.png' width = '400'>
	- Lars Ruthotto and Eldad Haber. Deep neural networks motivated by partial differential equations. 2018
		- https://www.youtube.com/watch?v=G2n2nJnh5kc&t=1391s
		- https://www.youtube.com/watch?v=1mVycBKb1TE
	- **PDE-Net**: Zichao Long, Yiping Lu, Xianzhong Ma, Bin Dong. PDE-Net: Learning PDEs from Data. ICML'18
		- https://github.com/ZichaoLong/PDE-Net
		- Insight: two objectives at the same time:
			- To accurately predict **dynamics** of complex systems
			- To uncover the underlying hidden PDE models (previous PDEs are human designed)
		- PDE function: du/dt=F(x,y,du/dx,du/dy,d2u/dx2,d2u/dxdy,d2u/dy2,...)
		- The 1st+2nd order solver: **learned** convolutional kernel\
			<img src = '/DL/images/dynamic-system/pde-net-1.png' width = '400'>\
			<img src = '/DL/images/dynamic-system/pde-net-2.png' width = '400'>
		- Multi-step: iterative weight shared as the first step;
		- Another view:\
			<img src = '/DL/images/dynamic-system/pde-net.png' width = '350'>
		- Application: dicovering hidden PDE;
	- Parabolic/hyperbolic CNNs, IMEX-Net; Lean ResNet;

## Numerical Time Integrator
- About the fast trace estimation trick:
	- About trace for flow generative: https://blog.csdn.net/hanss2/article/details/85331863
	- M.F. Hutchinson. A stochastic estimator of the trace of the influence matrix for laplacian smoothing splines. 1989.
		- First paper on the trace estimation trick;
	- https://zhuanlan.zhihu.com/p/51514687
- **FFJORD**: Will Grathwohl, Ricky T. Q. Chen, Jesse Bettencourt, Ilya Sutskever, David Duvenaud. FFJORD: Free-form Continuous Dynamics for Scalable Reversible Generative Models. ICLR'19
	- https://github.com/rtqichen/ffjord/
	- Insight: normalizing flow + trace estimation trick;
	- Formulation:\
		<img src = '/DL/images/dynamic-system/ffjord-1.png' width = '400'>
	- The algorithm:\
		<img src = '/DL/images/dynamic-system/ffjord-2.png' width = '400'>
	- A comparison:\
		<img src = '/DL/images/dynamic-system/ffjord-3.png' width = '400'>
- **HollowNet**: Ricky T. Q. Chen, David Duvenaud. Neural Networks with Cheap Differential Operators. NIPS'19
	<img src = '/DL/images/dynamic-system/hollow-net.png' width = '400'>
- **ODE-RNN**: Yulia Rubanova, Ricky T. Q. Chen, David Duvenaud. Latent ODEs for Irregularly-Sampled Time Series. NIPS'19
	- Insight: ODE-RNN hybrid; ODE during time steps; RNN update with new observation;
	- https://github.com/YuliaRubanova/latent_ode
	- Exponential decay as RNN; could also be modeled as ODE as dh/dt = -τt
		<img src = '/DL/images/dynamic-system/ode-rnn-1.png' width = '400'>
	- Algorithm:\
		<img src = '/DL/images/dynamic-system/ode-rnn-2.png' width = '400'>
- Eldad Haber, Keegan Lensink, Eran Treister, Lars Ruthotto. IMEXnet - A Forward Stable Deep Neural Network. ICML'19


## NN as ODE/PDE/Dynamic System, Equilibrium
- Legacy:
	- **Almeida-Pineda** algorithm;
	- Almeida, L. B. A learning rule for asynchronous perceptrons with feedback in a combinatorial environment. ICNN'87
	- Pineda, F. J. Generalization of back-propagation to recurrent neural networks. Physical review letters'87
	- Cessac, B. A view of neural networks as dynamical systems. International Journal of Bifurcation and Chaos. 2010
- **RBP**: Renjie Liao, Yuwen Xiong, Ethan Fetaya, Lisa Zhang, KiJung Yoon, Xaq Pitkow, Raquel Urtasun, Richard Zemel. Reviving and Improving Recurrent Back-Propagation. ICML'18
	- https://github.com/lrjconan/RBP
	- Insight: consider a class of RNNs whose **hidden state** converges to a steady state, with **Implicit Function Theorem**;
	- Fix point of phi w.r.t. h;\
		<img src = '/DL/images/dynamic-system/rbp-1.png' width = '400'>
	- Derivative of output, y=G(x,wG,h) and loss L(y,yGT);\
		<img src = '/DL/images/dynamic-system/rbp-2.png' width = '400'>
	- RBP algorithm:\
		<img src = '/DL/images/dynamic-system/rbp-3.png' width = '400'>
	- **CG-RBP**: conjugate gradient on normal equations:\
		<img src = '/DL/images/dynamic-system/rbp-4.png' width = '300'>
	- Neumann series (Neumann-RBP): sum(I+A+A^2+...) Neumann series, truncated at K:\
		<img src = '/DL/images/dynamic-system/rbp-5.png' width = '400'>
- Equilibrium Propagation
	- B. Scellier and Y. Bengio. Towards a biologically plausible backprop. arXiv'16
	- B. Scellier and Y. Bengio. Equilibrium propagation: Bridging the gap between energy-based models
	and backpropagation. 2017
		- A biologically inspired equilibrium propagation framework for an energy-based model whose prediction is the fixed-point of the energy dynamics at its local minimum;
	- B. Scellier and Y. Bengio. Equivalence of equilibrium propagation and recurrent backpropagation. NC'19
	- Maxence Ernoult, Julie Grollier, Damien Querlioz, Yoshua Bengio, Benjamin Scellier. Updates of Equilibrium Prop Match Gradients of Backprop Through Time in an RNN with Static Input. NIPS'19
		- https://github.com/ernoult/updatesEPgradientsBPTT
- **LMU**: Aaron Voelker, Ivana Kajić, Chris Eliasmith. Legendre Memory Units: Continuous-Time Representation in Recurrent Neural Networks. NIPS'19
	- https://github.com/abr/neurips2019

## Invert NN
- Reconstruct p(x\|z) with prior on x
	- Mahendran, A., and Vedaldi, A. Understanding deep image representations by inverting them. CVPR'15
		- Insight: find x s.t. representation phi(x) match with prior regularization plus a regularization:
			<img src = '/DL/images/dynamic-system/invert-cnn.png' width = '400'>
	- Dosovitskiy, A., and Brox, T. Inverting visual representations with convolutional networks. CVPR'16
		- Insight: find weight w s.t. reconstruction error is minimized; also tried on shallow features such as SIFT, HOG, LBP;\
			<img src = '/DL/images/dynamic-system/invert-cnn.png' width = '400'>
		- Operator: conv + upsample, padding with 0 and keep the value of top-left in a 2 x 2;	
- Theory:
	- Arora, S.; Liang, Y.; and Ma, T. Why are deep nets reversible: A simple theory, with implications for training. ICLR-Workshop'16
	- Gilbert, A. C.; Zhang, Y.; Lee, K.; Zhang, Y.; and Lee, H. Towards understanding the invertibility of convolutional neural networks. IJCAI'17
		- Theoretical connection between compressive sensing and neural network;
		- Model-based CS, MB-RIP; assume higher dimension observation and Gaussian kernel;
			<img src = '/DL/images/dynamic-system/mb-iht.png' width = '400'>
