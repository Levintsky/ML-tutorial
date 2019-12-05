# Flow based Approaches

## Good Summaries
- https://lilianweng.github.io/lil-log/2018/10/13/flow-based-deep-generative-models.html
	- p(x) = p(z)|det(dz/dx)|
- https://blog.evjang.com/2018/01/nf1.html
- https://blog.evjang.com/2018/01/nf2.html
- http://akosiorek.github.io/ml/2018/04/03/norm_flows.html

## Problem Definition
- GAN and VAE can't model p(x), because sum p(x|z)p(z) is hard!
- Important! change of variable theorem: 

## Normalizing Flows
- **Normalizing flows**: D. J. Rezende and S. Mohamed. Variational inference with normalizing flows. ICML'15
	- Transforms a simple distribution into a complex one by applying a sequence of invertible transformation functions.\
		<img src = '/Generative/images/flow/nf.png' width = '600'>
	- Maximize likelihood directly:\
		<img src = '/Generative/images/flow/nf2.png' width = '400'>
	- Transformation fi should satisfy:
		- It is easily invertible.
		- Its Jacobian determinant is easy to compute.
- NF Models:
	- **NICE**: L Dinh, D Krueger, and Y Bengio. Non-linear Independent Component Estimation. ICLRW'15
		- Predecessor of RealNVP; Additive layer only without scale;
			<img src = '/Generative/images/flow/nice.png' width = '500'>
	- **MADE**: M Germain, K Gregor, I Murray, and H Larochelle. Made: Masked autoencoder for distribution estimation. ICML'15
		- A specially designed architecture to enforce the autoregressive property in the autoencoder efficiently
			<img src = '/Generative/images/flow/made.png' width = '500'>
	- **RealNVP**: L Dinh, J Sohl-Dickstein, S Bengio. Density estimation using Real NVP. ICLR'17
		- Model design:\
			<img src = '/Generative/images/flow/realnvp1.png' width = '500'>
			<img src = '/Generative/images/flow/realnvp2.png' width = '500'>
	- **Glow**: D Kingma, P Dhariwal. Glow: Generative Flow with Invertible 1x1 Convolutions. NIPS'18
		- https://github.com/openai/glow
		- Building modules:\
			<img src = '/Generative/images/flow/glow1.png' width = '300'>
			<img src = '/Generative/images/flow/glow2.png' width = '500'>
- VAE + Flow:
	- **f-VAEs**: J Su, G Wu. f-VAEs: Improve VAEs with Conditional Flows. 2018
- Autoregressive Flow:
	- **IAF**: Kingma, D. P., Salimans, T., Jozefowicz, R., Chen, X., Sutskever, I., and Welling, M. Improved variational inference with inverse autoregressive flow. NIPS'16\
		<img src = '/Generative/images/flow/iaf.png' width = '400'>
	- **MAF**: G Papamakarios, T Pavlakou, I Murray. Masked Autoregressive Flow for Density Estimation. NIPS'17
		- A type of NF, where the transformation layer is built as an autoregressive neural network
		- https://github.com/gpapamak/maf
			<img src = '/Generative/images/flow/maf.png' width = '400'>
- W Grathwohl, R Chen, J Bettencourt, I Sutskever, and D Duvenaud. Ffjord: Free-form continuous dynamics for scalable reversible generative models. ICLR'19
- **PointFlow**: G Yang, X Huang, Z Hao, M Liu, S Belongie, B Hariharan. PointFlow: 3D Point Cloud Generation with Continuous Normalizing Flows. ICCV'19
	- https://www.guandaoyang.com/PointFlow/

## Neural ODE
- Yiping Lu, Aoxiao Zhong, Quanzheng Li, and Bin Dong. Beyond finite layer neural networks:
Bridging deep architectures and numerical differential equations. 2017
- Eldad Haber and Lars Ruthotto. Stable architectures for deep neural networks. Inverse Problems 2017
- Lars Ruthotto and Eldad Haber. Deep neural networks motivated by partial differential equations. 2018
- Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud. Neural ordinary differential equations. NIPS'18
	- Another ODE-Solver for back-prop
	- dh/dt = f(h, t, theta)
	- https://github.com/rtqichen/torchdiffeq
	- Gradient w.r.t. parameter
		<img src = '/Generative/images/flow/neural-ode.png' width = '400'>
	- Residual net with ODE: 6 x residual blocks
	- Continuous Normalizing Flows
	- Generative latent function time-series
- **FFJORD**: Will Grathwohl, Ricky T. Q. Chen, Jesse Bettencourt, Ilya Sutskever, David Duvenaud. FFJORD: Free-form Continuous Dynamics for Scalable Reversible Generative Models. ICLR'19
	- https://github.com/rtqichen/ffjord/
- Jens Behrmann, Will Grathwohl, Ricky T. Q. Chen, David Duvenaud, Jörn-Henrik Jacobsen.
Invertible Residual Networks. ICML'19
- Yulia Rubanova, Ricky T. Q. Chen, David Duvenaud. Latent ODEs for Irregularly-Sampled Time Series. NIPS'19
- Ricky T. Q. Chen, Jens Behrmann, David Duvenaud, Jörn-Henrik Jacobsen. Residual Flows for Invertible Generative Modeling. NIPS'19
- Ricky T. Q. Chen, David Duvenaud. Neural Networks with Cheap Differential Operators. NIPS'19