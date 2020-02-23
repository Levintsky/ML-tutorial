# Continuous NN, Neural-ODE/PDE

## Basics
- Adjoint sensitivity analysis for di$erential-algebraic equations: algorithms and software. JIAM J. Sci. Comput 2003

## Deep Learning as Discretized Differential Equations
- Forward Euler (ResNet, RevNet, ResNeXt):
	- **LM-ResNet**: Yiping Lu, Aoxiao Zhong, Quanzheng Li, and Bin Dong. Beyond finite layer neural networks: Bridging deep architectures and numerical differential equations. ICML'18
	- **PDE-Net**: Zichao Long, Yiping Lu, Xianzhong Ma, Bin Dong. PDE-Net: Learning PDEs from Data. ICML'18
		- Two objectives at the same time:
			- To accurately predict dynamics of complex systems
			- To uncover the underlying hidden PDE models (previous PDEs are human designed)
		- The model\
			<img src = '/Generative/images/ode-pde/pde-net.png' width = '350'>
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
		<img src = '/Generative/images/ode-pde/msa.png' width = '400'>
	-  Pontryagin's Maximum Principle: existence of co-state process P\
		<img src = '/Generative/images/ode-pde/msa-pmp.png' width = '400'>
	- Algorithms:\
		<img src = '/Generative/images/ode-pde/msa-1.png' width = '400'>\
		<img src = '/Generative/images/ode-pde/msa-2.png' width = '400'>\
		<img src = '/Generative/images/ode-pde/msa-3.png' width = '400'>
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
		<img src = '/Generative/images/ode-pde/node.png' width = '400'>
	- Gradient w.r.t. parameter\
		<img src = '/Generative/images/ode-pde/neural-ode.png' width = '400'>
	- Residual net with ODE: 6 x residual blocks
	- Continuous Normalizing Flows
	- Generative latent function time-series
- **FFJORD**: Will Grathwohl, Ricky T. Q. Chen, Jesse Bettencourt, Ilya Sutskever, David Duvenaud. FFJORD: Free-form Continuous Dynamics for Scalable Reversible Generative Models. ICLR'19
	- https://github.com/rtqichen/ffjord/
- Yulia Rubanova, Ricky T. Q. Chen, David Duvenaud. Latent ODEs for Irregularly-Sampled Time Series. NIPS'19
- Ricky T. Q. Chen, Jens Behrmann, David Duvenaud, Jörn-Henrik Jacobsen. Residual Flows for Invertible Generative Modeling. NIPS'19
- Ricky T. Q. Chen, David Duvenaud. Neural Networks with Cheap Differential Operators. NIPS'19
- Emilien Dupont, Arnaud Doucet, Yee Whye Teh. Augmented Neural ODEs. NIPS'19
