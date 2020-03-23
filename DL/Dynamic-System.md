# Dynamic System View

## Unclassified
- **LGQ**: Laurent Lessard, Benjamin Recht, Andrew Packard. Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints. 2015
- Bo Chang, Lili Meng, Eldad Haber, Frederick Tung, David Begert Multi-level residual networks from dynamical systems view. ICLR'18
- Lars Ruthotto and Eldad Haber. Deep neural networks motivated by partial differential equations. 2018
- **DURR**: Xiaoshuai Zhang, Yiping Lu, Jiaying Liu, Bin Dong. Dynamically Unfolding Recurrent Restorer: A Moving Endpoint Control Method for Image Restoration. ICLR'19
- Tao Y, Sun Q, Du Q, et al. Nonlocal Neural Networks, Nonlocal Diffusion and Nonlocal
Modeling. NIPS'18
- Rassi. Multistep neural networks for data-driven discovery of nonlinear dynamical systems. 2018
- Rassi. Numerical Gaussian processes for time-dependent and nonlinear partial differential equations. 2018
- Lei Wu, Chao Ma, Weinan E. How SGD Selects the Global Minima in Over-parameterized Learning: A Dynamical Stability Perspective. NIPS'18
- **L-PDE**: Fang, Cong, Zhao, Zhenyu, Zhou, Pan, and Lin, Zhouchen. Feature learning via partial differential equation with applications to face recognition. Pattern Recognition, 69 (C):14–25, 2017.
	- Learned-PDE;
- Sonoda, Sho and Murata, Noboru. Double continuum limit of deep neural networks. ICML Workshop'17

## Basics on Dynamic System
- Classical solvers:
	- Forward Euler (simplest RK);
	- Midpoint, leapfrog;
	- Backward Euler;
	- Runge-Kutta method;
		- Most classical RK4;\
			<img src = '/DL/images/dynamic-system/rk4.png' width = '400'>
- Diffential equation, adjoint method:
	- Pontryagin's maximum principle (Boltyanskii et al., 1960; Pontryagin, 1987)
	- About adjoint method: https://blog.csdn.net/liangdaojun/article/details/100633277
	- Adjoint sensitivity analysis for differential-algebraic equations: algorithms and software. JIAM J. Sci. Comput 2003
- Fixed point:
	- https://zhuanlan.zhihu.com/p/58507915
	- http://wwwf.imperial.ac.uk/metric/metric_public/numerical_methods/iteration/fixed_point_iteration.html
- Dong, Bin, Jiang, Qingtang, and Shen, Zuowei. Image restoration: wavelet frame shrinkage, nonlinear evolution pdes, and beyond. Multiscale Modeling & Simulation'17
	- Insight: Conv operator as differentiation;
- Reversible ODE:
	- Nguyen, B. D., and McMechan, G. A. Five ways to avoid storing source wavefield snapshots in 2d elastic prestack reverse time migration. Geophysics'14
		- Reversible numerical methods for ODEs have been studied in the context of hyperbolic differential equations;

## Resources
- Books:
	- Hairer and Peters. Solving ordinary differential equations I. Springer Berlin Heidelberg, 1987.
	- Dimitri P Bertsekas. Dynamic programming and optimal control, volume 1. Athena scientific Belmont, MA, 1995.

## Neural ODE Series
- Good summaries:
	- About trace for flow generative: https://blog.csdn.net/hanss2/article/details/85331863
	- M.F. Hutchinson. A stochastic estimator of the trace of the influence matrix for laplacian smoothing splines. 1989.
		- First paper on the trace estimation trick;
	- https://zhuanlan.zhihu.com/p/51514687
- Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud. Neural ordinary differential equations. NIPS'18
	- Another ODE-Solver for back-prop
	- dh/dt = f(h, t, theta)
	- https://github.com/rtqichen/torchdiffeq
	- Analogy:\
		<img src = '/DL/images/dynamic-system/node.png' width = '400'>
	- Gradient w.r.t. parameter\
		<img src = '/DL/images/dynamic-system/neural-ode.png' width = '400'>
	- Residual net with ODE: 6 x residual blocks
	- Continuous Normalizing Flows
	- Generative latent function time-series
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
- **ANODE**: Emilien Dupont, Arnaud Doucet, Yee Whye Teh. Augmented Neural ODEs. NIPS'19
	- https://github.com/EmilienDupont/augmented-neural-odes
	- Insight: ODE preserves topology and is not able to present some functions; augment to higher-dimension to make it possible;
	- E.g.1: f(1) = -1, f(-1) = 1; (cross each other)
	- E.g.2: two circles; (not linear separable)
	- Proposed method: augment with vector a;\
		<img src = '/DL/images/dynamic-system/anode.png' width = '400'>
- **ODE-RNN**: Yulia Rubanova, Ricky T. Q. Chen, David Duvenaud. Latent ODEs for Irregularly-Sampled Time Series. NIPS'19
	- Insight: ODE-RNN hybrid; ODE during time steps; RNN update with new observation;
	- https://github.com/YuliaRubanova/latent_ode
	- Exponential decay as RNN; could also be modeled as ODE as dh/dt = -tau t
		<img src = '/DL/images/dynamic-system/ode-rnn-1.png' width = '400'>
	- Algorithm:\
		<img src = '/DL/images/dynamic-system/ode-rnn-2.png' width = '400'>
- Xuechen Li, Ting-Kam Leonard Wong, Ricky T. Q. Chen, David Duvenaud. Scalable Gradients for Stochastic Differential Equations. AISTATS'20
	- Insight: extend adjoint to **SDE**;\
		<img src = '/DL/images/dynamic-system/sde-adjoint.png' width = '400'>

## ML ODE/PDE/SDE Solver:
- GP solver:
	- Michael Schober, David Duvenaud, Philipp Hennig. Probabilistic ODE solvers with Runge-Kutta means. NIPS 2014
		- Gaussian Process to solve ODE;
	- Weinan E. A proposal on machine learning via dynamical systems. Communications in Mathematics and Statistics. 2017
		- First proposed connection between ResNet and ODE; ResNet = Forward Euler;
- Deep Learning as Discretized Differential Equations
	- Legacy:
		- Isaac E Lagaris, Aristidis Likas, and Dimitrios I Fotiadis. Artificial neural networks for solving ordinary and partial differential equations. IEEE transactions on neural networks, 9(5):987–1000, 1998.
	- Forward Euler, or 1st-order Runge-Kutta (ResNet, RevNet, ResNeXt):
		- Eldad Haber and Lars Ruthotto. Stable architectures for deep neural networks. Inverse Problems 2017
			- Insight: view ResNet as ODE to address exploding/vanishing gradients; Condition of stable: real part of Jacobian's Eigenvalue <= 0;\
				<img src = '/DL/images/dynamic-system/stable-nn-1.png' width = '400'>
			- Which requires constraint. The paper proposes an intrinsically stable method;
			- Model: 1 Layer ResNet, inspired by Hamiltonian system;\
				<img src = '/DL/images/dynamic-system/stable-nn-2.png' width = '400'>
		- Haber, E.; Ruthotto, L.; and Holtham, E. Learning across scales- multiscale methods for convolution neural networks. arxiv'17
			- Supervised learning from optimal control formulation;\
				<img src = '/DL/images/dynamic-system/multi-scale-1.png' width = '400'>
			- The algorithm:\
				<img src = '/DL/images/dynamic-system/multi-scale-2.png' width = '400'>
		- **RevNet**: Gomez, A. N.; Ren, M.; Urtasun, R.; and Grosse, R. B. The reversible residual network: Backpropagation without storing activations. NIPS'17
			- https://github.com/renmengye/revnet-public
			- Insight: modularized to make computation reversible: activation saving not required for bp;
				<img src = '/DL/images/dynamic-system/rev-net-1.png' width = '400'>\
				<img src = '/DL/images/dynamic-system/rev-net-2.png' width = '400'>
			- The backprop: reversibleconstruct the value first;\
				<img src = '/DL/images/dynamic-system/rev-net-3.png' width = '400'>
			- Chang Bo's insight from ODE:\
				<img src = '/DL/images/dynamic-system/rev-net.png' width = '400'>
		- Chang B, Meng L, Haber E, et al. Reversible architectures for arbitrarily deep residual neural networks. AAAI'18
			- Insigh: ODE version of RevNet;
			- Module: 2 Layer NN;\
				<img src = '/DL/images/dynamic-system/rev-ode-1.png' width = '350'>\
				<img src = '/DL/images/dynamic-system/rev-ode-2.png' width = '350'>
			- Middle-point; Leapfrog Network; make use of the trick Y(j+1)-Y(j-1)/2h=F(Yj)
				<img src = '/DL/images/dynamic-system/rev-ode-3.png' width = '350'>
			- Whole model:\
				<img src = '/DL/images/dynamic-system/rev-ode-4.png' width = '500'>
		- **MSA**: Qianxiao Li, Long Chen, Cheng Tai, Weinan E. Maximum Principle Based Algorithms for Deep Learning. JMLR'18
			- Same thing as Neural ODE; Neural ODE is strong in flow-based generative modeling;
			- Formulation: dX/dt=f(t,X,theta) could be a NN; first term: fitting; second term: regularization\
				<img src = '/DL/images/dynamic-system/msa.png' width = '400'>
			-  **PMP** (Pontryagin's Maximum Principle): for optimally controlled status, existence of co-state process P, s.t. the Hamiltonian equations satisfy, and optimal than other states\
				<img src = '/DL/images/dynamic-system/msa-pmp.png' width = '400'>
			- Algorithms:\
				<img src = '/DL/images/dynamic-system/msa-1.png' width = '400'>
				<img src = '/DL/images/dynamic-system/msa-2.png' width = '400'>
				<img src = '/DL/images/dynamic-system/msa-3.png' width = '400'>
		- **LM-ResNet**: Yiping Lu, Aoxiao Zhong, Quanzheng Li, and Bin Dong. Beyond finite layer neural networks: Bridging deep architectures and numerical differential equations. ICML'18
			- https://web.stanford.edu/~yplu/proj/lm/
			- Linear multi-step;
			- Previous model comparison:\
				<img src = '/DL/images/dynamic-system/lm-net-1.png' width = '400'>
			- LM-ResNet:\
				<img src = '/DL/images/dynamic-system/lm-net-2.png' width = '400'>\
				<img src = '/DL/images/dynamic-system/lm-net-3.png' width = '400'>
		- **PDE-Net**: Zichao Long, Yiping Lu, Xianzhong Ma, Bin Dong. PDE-Net: Learning PDEs from Data. ICML'18
			- https://github.com/ZichaoLong/PDE-Net
			- Two objectives at the same time:
				- To accurately predict dynamics of complex systems
				- To uncover the underlying hidden PDE models (previous PDEs are human designed)
			- The 1st+2nd order solver:\
				<img src = '/DL/images/dynamic-system/pde-net-1.png' width = '400'>\
				<img src = '/DL/images/dynamic-system/pde-net-2.png' width = '400'>
			- Multi-step:\
				<img src = '/DL/images/dynamic-system/pde-net-3.png' width = '400'>
			- Another view:\
				<img src = '/DL/images/dynamic-system/pde-net.png' width = '350'>
		- **i-ResNet**: Jens Behrmann, Will Grathwohl, Ricky T. Q. Chen, David Duvenaud, Jörn-Henrik Jacobsen. Invertible Residual Networks. ICML'19
			- Main insight: same as RevNet and flow-based methods. but **free-form**; A comparison:\
				<img src = '/DL/images/dynamic-system/i-resnet-4.png' width = '400'>
			- https://github.com/jhjacobsen/invertible-resnet
			- With contractive g(), i.e., Lip(g(theta)) < 1, so **Spectral-Norm** layer added to make constraint always satisfied. Then backward Euler to compute x(t+1) from x(t) as fixed point:\
				<img src = '/DL/images/dynamic-system/i-resnet-1.png' width = '400'>
			- For generative model, ln(px(x)) = ln(pz(z))+ln|det(JF(x))|, with JF as the Jacobian of F(), since F=I+g() as the residual block, we could have a Taylor expansion.
				<img src = '/DL/images/dynamic-system/i-resnet-2.png' width = '400'>
			- Three computation drawbacks: (1) evaluate tr(J); (2) power of J; (3) Taylor has infinite terms;
			- For (1), (2), the approximate trick;
			- For (3), truncated at n steps;
			- The algorithm:\
				<img src = '/DL/images/dynamic-system/i-resnet-3.png' width = '400'>
		- **Residual-Flow**: Ricky T. Q. Chen, Jens Behrmann, David Duvenaud, Jörn-Henrik Jacobsen. Residual Flows for Invertible Generative Modeling. NIPS'19
			- Main insight: Unbiased Log Density Estimation for Maximum Likelihood Estimation with **Russian roulette**; flip a coin (Bernoulli) to decide when to stop; Improve on **i-ResNet**;
			- https://github.com/rtqichen/residual-flows
			- Forward: notice the importance sampling;\
				<img src = '/DL/images/dynamic-system/res-flow-1.png' width = '400'>
			- Backward:\
				<img src = '/DL/images/dynamic-system/res-flow-2.png' width = '400'>
	- Backward Euler Approx:
		- **PolyNet**: Xingcheng Zhang, Zhizhong Li, Chen Change Loy, Dahua Lin. PolyNet: A Pursuit of Structural Diversity in Very Deep Networks. CVPR'17
			- Insight: structural diversity; "polynomial" combination of Inception units;
			- https://github.com/CUHK-MMLAB/polynet
			- An ODE view:\
				<img src = '/DL/images/dynamic-system/poly-net.png' width = '400'>
			- Composition:\
				<img src = '/DL/images/dynamic-system/poly-net-2.png' width = '400'>
	- Runge-Kutta:
		- **FractalNet**: Gustav Larsson, Michael Maire, Gregory Shakhnarovich. FractalNet: Ultra-Deep Neural Networks without Residuals. ICLR'17
			- Model:\
				<img src = '/DL/images/dynamic-system/fractal-net-2.png' width = '400'>
			- An ODE view:\
				<img src = '/DL/images/dynamic-system/fractal-net.png' width = '400'>
		- DenseNet:
- Neural SDE:
	- Junteng Jia and Austin R. Benson. Neural Jump Stochastic Differential Equations. arxiv'19
	- Xuanqing Liu, Si Si, Qin Cao, Sanjiv Kumar, and Cho-Jui Hsieh. Neural sde: Stabilizing neural ode networks with stochastic noise. arxiv'19
	- Belinda Tzen and Maxim Raginsky. Neural stochastic differential equations: Deep latent gaus- sian models in the diffusion limit. arxiv'19
	- Belinda Tzen and Maxim Raginsky. Theoretical guarantees for sampling and inference in generative models with latent diffusions. COLT'19

## NN as ODE/PDE/Dynamic System, Equilibrium
- Legacy:
	- **Almeida-Pineda** algorithm;
	- Almeida, L. B. A learning rule for asynchronous perceptrons with feedback in a combinatorial environment. ICNN'87
	- Pineda, F. J. Generalization of back-propagation to recurrent neural networks. Physical review letters'87
	- Patrice Y Simard, Mary B Ottaway, and Dana H Ballard. Fixed point analysis for recurrent networks. NIPS'89
	- Cessac, B. A view of neural networks as dynamical systems. International Journal of Bifurcation and Chaos. 2010
- John Miller and Moritz Hardt. When recurrent models don't need to be recurrent. arXiv'18
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
- Shaojie Bai, J. Zico Kolter, Vladlen Koltun. Deep Equilibrium Models. NIPS'19
	- https://github.com/locuslab/deq
	- Model:\
		<img src = '/DL/images/dynamic-system/deq-1.png' width = '350'>
	- Back prop through fixed point;\
		<img src = '/DL/images/dynamic-system/deq-2.png' width = '400'>
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
