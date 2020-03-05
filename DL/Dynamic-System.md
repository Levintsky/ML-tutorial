# Dynamic System View

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
- Reversible:
	- Nguyen, B. D., and McMechan, G. A. Five ways to avoid storing source wavefield snapshots in 2d elastic prestack reverse time migration. Geophysics'14
		- Reversible numerical methods for ODEs have been studied in the context of hyperbolic differential equations;

## Resources
- Books:
	- Dimitri P Bertsekas. Dynamic programming and optimal control, volume 1. Athena scientific Belmont, MA, 1995.

## Unclassified
- **L-PDE**: Fang, Cong, Zhao, Zhenyu, Zhou, Pan, and Lin, Zhouchen. Feature learning via partial differential equation with applications to face recognition. Pattern Recognition, 69 (C):14–25, 2017.
	- Learned-PDE;
- Sonoda, Sho and Murata, Noboru. Double continuum limit of deep neural networks. ICML Workshop'17

## ML ODE Solver:
- GP solver:
	- Michael Schober, David Duvenaud, Philipp Hennig. Probabilistic ODE solvers with Runge-Kutta means. NIPS 2014
		- Gaussian Process to solve ODE;
	- Weinan E. A proposal on machine learning via dynamical systems. Communications in Mathematics and Statistics. 2017
		- First proposed connection between ResNet and ODE; ResNet = Forward Euler;
- Deep Learning as Discretized Differential Equations
	- Forward Euler, or 1st-order Runge-Kutta (ResNet, RevNet, ResNeXt):
		- **RevNet**: Gomez, A. N.; Ren, M.; Urtasun, R.; and Grosse, R. B. The reversible residual network: Backpropagation without storing activations. NIPS'17
			<img src = '/DL/images/dynamic-system/rev-net.png' width = '400'>
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
			- An ODE view:
				<img src = '/DL/images/dynamic-system/fractal-net.png' width = '400'>
		- DenseNet:

## Legacy NN as ODE/PDE
- Patrice Y Simard, Mary B Ottaway, and Dana H Ballard. Fixed point analysis for recurrent networks. NIPS'89
- Cessac, B. A view of neural networks as dynamical systems. International Journal of Bifurcation and Chaos. 2010

## Dynamic Sequence, RNN
- John Miller and Moritz Hardt. When recurrent models don't need to be recurrent. arXiv'18
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

## Dynamic Transformer
- Shaojie Bai, J. Zico Kolter, Vladlen Koltun. Deep Equilibrium Models. NIPS'19
	- https://github.com/locuslab/deq
	- Model:\
		<img src = '/DL/images/dynamic-system/deq-1.png' width = '350'>
	- Back prop through fixed point;\
		<img src = '/DL/images/dynamic-system/deq-2.png' width = '400'>

## Neural ODE
- Good summaries:
	- About trace for flow generative: https://blog.csdn.net/hanss2/article/details/85331863
	- https://zhuanlan.zhihu.com/p/51514687
- **LGQ**: Laurent Lessard, Benjamin Recht, Andrew Packard. Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints. 2015
- **MSA**: Qianxiao Li, Long Chen, Cheng Tai, Weinan E. Maximum Principle Based Algorithms for Deep Learning. JMLR'18
	- Same thing as Neural ODE; Neural ODE is strong in flow-based generative modeling;
	- Formulation: dX/dt=f(t,X,theta) could be a NN; first term: fitting; second term: regularization\
		<img src = '/DL/images/dynamic-system/msa.png' width = '400'>
	-  **PMP** (Pontryagin's Maximum Principle): for optimally controlled status, existence of co-state process P\
		<img src = '/DL/images/dynamic-system/msa-pmp.png' width = '400'>
	- Algorithms:\
		<img src = '/DL/images/dynamic-system/msa-1.png' width = '400'>\
		<img src = '/DL/images/dynamic-system/msa-2.png' width = '400'>\
		<img src = '/DL/images/dynamic-system/msa-3.png' width = '400'>
- Reversible:
	- Mahendran, A., and Vedaldi, A. Understanding deep image representations by inverting them. CVPR'15
		- Insight: find x s.t. representation phi(x) match with prior regularization:
			<img src = '/DL/images/dynamic-system/invert-cnn.png' width = '400'>
	- Arora, S.; Liang, Y.; and Ma, T. Why are deep nets reversible: A simple theory, with implications for training. ICLR-Workshop'16
	- Dosovitskiy, A., and Brox, T. Inverting visual representations with convolutional networks. CVPR'16
	- Gilbert, A. C.; Zhang, Y.; Lee, K.; Zhang, Y.; and Lee, H. Towards understanding the invertibility of convolutional neural networks. arxiv'17
		- Theoretical connection between compressive sensing and neural network;
	- Eldad Haber and Lars Ruthotto. Stable architectures for deep neural networks. Inverse Problems 2017
		- 1 Layer NN, inspired by Hamiltonian system;
			<img src = '/DL/images/dynamic-system/stable-nn.png' width = '400'>
	- Haber, E.; Ruthotto, L.; and Holtham, E. Learning across scales-a multiscale method for convolution neural networks. arxiv'17
	- Chang B, Meng L, Haber E, et al. Reversible architectures for arbitrarily deep residual neura networks. AAAI'18
		- Module: 2 Layer NN;\
			<img src = '/DL/images/dynamic-system/rev-ode-1.png' width = '350'>\
			<img src = '/DL/images/dynamic-system/rev-ode-2.png' width = '350'>
		- Middle-point; Leapfrog Network; make use of the trick Y(j+1)-Y(j-1)/2h=F(Yj)
			<img src = '/DL/images/dynamic-system/rev-ode-3.png' width = '350'>
		- Whole model:\
			<img src = '/DL/images/dynamic-system/rev-ode-4.png' width = '500'>
	- Bo Chang, Lili Meng, Eldad Haber, Frederick Tung, David Begert Multi-level residual networks from dynamical systems view. ICLR'18
	- Lars Ruthotto and Eldad Haber. Deep neural networks motivated by partial differential equations. 2018
- **DURR**: Xiaoshuai Zhang, Yiping Lu, Jiaying Liu, Bin Dong. Dynamically Unfolding Recurrent Restorer: A Moving Endpoint Control Method for Image Restoration. ICLR'19
- Tao Y, Sun Q, Du Q, et al. Nonlocal Neural Networks, Nonlocal Diffusion and Nonlocal
Modeling. NIPS'18
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
- Yulia Rubanova, Ricky T. Q. Chen, David Duvenaud. Latent ODEs for Irregularly-Sampled Time Series. NIPS'19
- Ricky T. Q. Chen, Jens Behrmann, David Duvenaud, Jörn-Henrik Jacobsen. Residual Flows for Invertible Generative Modeling. NIPS'19
- Ricky T. Q. Chen, David Duvenaud. Neural Networks with Cheap Differential Operators. NIPS'19
- Emilien Dupont, Arnaud Doucet, Yee Whye Teh. Augmented Neural ODEs. NIPS'19
