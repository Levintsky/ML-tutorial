# Dynamic System View

## Basics
- Diffential equation:
	- Adjoint sensitivity analysis for differential-algebraic equations: algorithms and software. JIAM J. Sci. Comput 2003
- Fixed point:
	- https://zhuanlan.zhihu.com/p/58507915
	- http://wwwf.imperial.ac.uk/metric/metric_public/numerical_methods/iteration/fixed_point_iteration.html

## Dynamic Sequence, RNN
- Patrice Y Simard, Mary B Ottaway, and Dana H Ballard. Fixed point analysis for recurrent networks. NIPS'89
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

## Dynamic Sequence

## Deep Learning as Discretized Differential Equations
- Forward Euler (ResNet, RevNet, ResNeXt):
	- **LM-ResNet**: Yiping Lu, Aoxiao Zhong, Quanzheng Li, and Bin Dong. Beyond finite layer neural networks: Bridging deep architectures and numerical differential equations. ICML'18
	- **PDE-Net**: Zichao Long, Yiping Lu, Xianzhong Ma, Bin Dong. PDE-Net: Learning PDEs from Data. ICML'18
		- Two objectives at the same time:
			- To accurately predict dynamics of complex systems
			- To uncover the underlying hidden PDE models (previous PDEs are human designed)
		- The model\
			<img src = '/DL/images/dynamic-system/pde-net.png' width = '350'>
- Backward Euler Approx (PolyNet):
	- Xingcheng Zhang, Zhizhong Li, Chen Change Loy, Dahua Lin. PolyNet: A Pursuit of Structural Diversity in Very Deep Networks. 2017
- Runge-Kutta:
	- FractalNet: Gustav Larsson, Michael Maire, Gregory Shakhnarovich. FractalNet: Ultra-Deep Neural Networks without Residuals. 2014
	- DenseNet:

## Neural ODE
- Good summaries:
	- About adjoint method: https://blog.csdn.net/liangdaojun/article/details/100633277
	- About trace for flow generative: https://blog.csdn.net/hanss2/article/details/85331863
	- https://zhuanlan.zhihu.com/p/51514687
- Michael Schober, David Duvenaud, Philipp Hennig. Probabilistic ODE solvers with Runge-Kutta means. NIPS 2014
	- Gaussian Process to solve ODE
- **LGQ**: Laurent Lessard, Benjamin Recht, Andrew Packard. Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints. 2015
- **MSA**: Qianxiao Li, Long Chen, Cheng Tai, Weinan E. Maximum Principle Based Algorithms for Deep Learning. JMLR'18
	- Same thing as Neural ODE; Neural ODE is strong in flow-based generative modeling;
	- Formulation: f() could be a NN\
		<img src = '/DL/images/dynamic-system/msa.png' width = '400'>
	-  Pontryagin's Maximum Principle: existence of co-state process P\
		<img src = '/DL/images/dynamic-system/msa-pmp.png' width = '400'>
	- Algorithms:\
		<img src = '/DL/images/dynamic-system/msa-1.png' width = '400'>\
		<img src = '/DL/images/dynamic-system/msa-2.png' width = '400'>\
		<img src = '/DL/images/dynamic-system/msa-3.png' width = '400'>
- Aditya Grover, Christopher Chute, Rui Shu, Zhangjie Cao, Stefano Ermon. AlignFlow: Cycle Consistent Learning from Multiple Domains via Normalizing Flows. 2019
- Reversible:
	- Eldad Haber and Lars Ruthotto. Stable architectures for deep neural networks. Inverse Problems 2017
	- Chang B, Meng L, Haber E, et al. Reversible architectures for arbitrarily deep residual neura networks. AAAI'18
	- Chang Bo. Multi-level residual networks from dynamical systems view. ICLR 2018
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
