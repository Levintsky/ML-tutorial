# Flow based Approaches

## Good Summaries
- https://lilianweng.github.io/lil-log/2018/10/13/flow-based-deep-generative-models.html
	- p(x) = p(z)|det(dz/dx)|
- https://blog.evjang.com/2018/01/nf1.html
- https://blog.evjang.com/2018/01/nf2.html
- http://akosiorek.github.io/ml/2018/04/03/norm_flows.html
- **Survey**: George Papamakarios, Eric Nalisnick, Danilo Jimenez Rezende, Shakir Mohamed
Balaji Lakshminarayanan. Normalizing Flows for Probabilistic Modeling and Inference. 2019
	- Expressive power: universal representation is possible under reasonable conditions (proved with Autogressive flows);
	- Optimize theta = (phi, psi), for Transform phi and prior psi:\
		<img src = '/Generative/images/flow/survey1.png' width = '400'>
	- Constructing Flows (finite compositions):
		- Autoregressive flows (Jacobian determinant is triangular and tractable), zi only based on inputs z(j<=i);
			- Affine/location-scale: NICE, RealNVP, IAF, MAF, Glow;
			- Non-affine: conic (NAF, block NAF, B-NAF, Flow++); drawback: not inverted analytically, only iteratively via bp;
			- Recurrent autoregressive flows [Olivia 18, IAF 16]: share parameters across conditioners with RNN;
			- MAF: masking out connections with (1/0 matrix); or soft-attention (transformer)
		- Linear flow: z'=Wz, W: DxD invertible; shortcoming:
		- Residual flow: guaranteed to be invertible if contractive; shortcoming: no known general efficient procedure for computing Jacobian determinant;
			- Planar flow;
			- Sylvester flow;
			- Radial flow;
		- Practical consideration:
			- Normalization;
	- Constructing Flows: continuous-time transformation;
		- Neural ODE; trace for flow; Hutchinson’s trace estimator [1990] to make trace estimation fast;
		- Solving forward: Runge-Kutta family;
		- Solving backward: adjoint [adjoint sensitivity method, Pontryagin 1962];
	- Generalization: generate probability;
		- RAD;
		- Discrete distribution;
		- Riemannian manifold;
	- Applications:
		- Probabilistic modeling: MLE: KL(px(x), px(x, theta)), density estimation;
		- Generation;
		- Inference: modeling parameters to infer unkonwn quantities within a model;
		- Representation learning;
		- RL: imitation learning; Yannick Schroecker, Mel Vecerik, and Jon Scholz. Generative predecessor models for sample-efficient imitation learning. ICLR'19

## Problem Definition
- GAN and VAE can't model p(x), because sum p(x|z)p(z) is hard!
- Important! change of variable theorem: 

## Normalizing Flows
- **Normalizing flows** or **Planar Flows**: D. J. Rezende and S. Mohamed. Variational inference with normalizing flows. ICML'15
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
			<img src = '/Generative/images/flow/glow1.png' width = '200'>\
			<img src = '/Generative/images/flow/glow2.png' width = '500'>
- VAE + Flow:
	- Xi Chen, Diederik P Kingma, Tim Salimans, Yan Duan, Prafulla Dhariwal, John Schulman, Ilya Sutskever, and Pieter Abbeel. Variational lossy autoencoder. ICLR'16
	- **f-VAEs**: J Su, G Wu. f-VAEs: Improve VAEs with Conditional Flows. 2018
	- **Sylvester-nf**: Rianne van den Berg, Leonard Hasenclever, Jakub M. Tomczak, Max Welling. Sylvester Normalizing Flows for Variational Inference. UAI'18
		- Motivation:\
			<img src = '/Generative/images/flow/sylvester-nf1.png' width = '300'>
		- VAE-flow:\
			<img src = '/Generative/images/flow/sylvester-nf2.png' width = '350'>
- Autoregressive Flow:
	- **IAF**: Kingma, D. P., Salimans, T., Jozefowicz, R., Chen, X., Sutskever, I., and Welling, M. Improved variational inference with inverse autoregressive flow. NIPS'16\
		<img src = '/Generative/images/flow/iaf.png' width = '400'>
	- **MAF**: G Papamakarios, T Pavlakou, I Murray. Masked Autoregressive Flow for Density Estimation. NIPS'17
		- A type of NF, where the transformation layer is built as an autoregressive neural network
		- https://github.com/gpapamak/maf \
			<img src = '/Generative/images/flow/maf.png' width = '400'>
	- Yang Song, Chenlin Meng, and Stefano Ermon. MintNet: Building invertible neural networks with masked convolutions. NIPS'19
	- **NAF**: Chin-Wei Huang, David Krueger, Alexandre Lacoste, and Aaron C. Courville. Neural autoregressive flows. ICML'18
	- Priyank Jaini, Kira A. Selby, and Yaoliang Yu. Sum-of-squares polynomial flow. ICML'19
	- **B-NAF** Nicola De Cao, Ivan Titov, and Wilker Aziz. Block neural autoregressive flow. UAI'19
	- **Flow++**: Jonathan Ho, Xi Chen, Aravind Srinivas, Yan Duan, and Pieter Abbeel. Flow++: Improving flow-based generative models with variational dequantization and architecture. ICML'19
design.
- Flow + GAN:
	- Ivo Danihelka, Balaji Lakshminarayanan, Benigno Uria, Daan Wierstra, and Peter Dayan. Comparison of maximum likelihood and gan-based training of real nvps. 2017
	- Aditya Grover, Manik Dhar, and Stefano Ermon. Flow-gan: Combining maximum likelihood and adversarial learning in generative models. AAAI'18
- Recurrent:
	- Junier Oliva, Avinava Dubey, Manzil Zaheer, Barnabas Poczos, Ruslan Salakhutdinov, Eric Xing, and Jeff Schneider. Transformation autoregressive networks. ICML'18
- W Grathwohl, R Chen, J Bettencourt, I Sutskever, and D Duvenaud. Ffjord: Free-form continuous dynamics for scalable reversible generative models. ICLR'19
- **PointFlow**: G Yang, X Huang, Z Hao, M Liu, S Belongie, B Hariharan. PointFlow: 3D Point Cloud Generation with Continuous Normalizing Flows. ICCV'19
	- https://www.guandaoyang.com/PointFlow/
	- https://github.com/stevenygd/PointFlow
	- Based on CNF (FFJORD)\
		<img src = '/Generative/images/flow/pointflow.png' width = '600'>
- Manoj Kumar, Mohammad Babaeizadeh, Dumitru Erhan, Chelsea Finn, Sergey Levine, Laurent Dinh, and Durk Kingma. Videoflow: A flow-based generative model for video. 2019
- Ryan Prenger, Rafael Valle, and Bryan Catanzaro. Waveglow: A flow-based generative network for speech synthesis. 2019

## Flow-based Graph Generation
- Jenny Liu, Aviral Kumar, Jimmy Ba, Jamie Kiros, Kevin Swersky. Graph Normalizing Flows. 2019
	- Invertible message passing process:\
		<img src = '/Generative/images/flow/gnf1.png' width = '450'>
	- Sample prior for generation:\
		<img src = '/Generative/images/flow/gnf2.png' width = '350'>
- Chence Shi, Minkai Xu, Zhaocheng Zhu, Weinan Zhang, Ming Zhang, Jian Tang. GraphAF: a Flow-based Autoregressive Model for Molecular Graph Generation. ICLR'20
	- https://drive.google.com/drive/folders/1LFfB5l0B6Zb-8WtV0EhmgolpHc9h-rcI

## Generalization
- **RAD**: Laurent Dinh, Jascha Sohl-Dickstein, Razvan Pascanu, and Hugo Larochelle. A RAD approach to deep mixture models. ICLR'19

## Invertible
- **Revnet**: Aidan N. Gomez, Mengye Ren, Raquel Urtasun, Roger B. Grosse. The reversible residual network: Backpropagation without storing activations. NIPS 2017
	- Insight: resnet expensive to store activation in memory, revnet could calculate activation from next layer;
	- Modularized: an auxiliary z = x1 + F(x2), the rev-block could only use stride=1 unlike resnet:\
		<img src = '/Generative/images/flow/Revnet1.png' width = '450'>
	- Forward and reverse:\
		<img src = '/Generative/images/flow/Revnet2.png' width = '450'>
	- Backward:\
		<img src = '/Generative/images/flow/Revnet3.png' width = '450'>
- Yunfei Teng, Anna Choromanska, and Mariusz Bojarski. Invertible autoencoder for domain adaptation. 2018
- R.T. Schirrmeister, P. Chraba ̧szcz, F. Hutter, and T. Ball. Training generative reversible networks. 2018
- Fangchang Ma, Ulas Ayaz, Sertac Karaman. Invertibility of Convolutional Generative Networks from Partial Measurements. NIPS'18
- Lynton Ardizzone, Jakob Kruse, Sebastian Wirkert, Daniel Rahner, Eric W. Pellegrini, Ralf S. Klessen, Lena Maier-Hein, Carsten Rother, Ullrich Köthe. Analyzing Inverse Problems with Invertible Neural Networks. ICLR'19
- Jens Behrmann, Will Grathwohl, Ricky T. Q. Chen, David Duvenaud, Jörn-Henrik Jacobsen. Invertible Residual Networks. ICML'19
	- A density model, main insight: free-form! A comparison:\
		<img src = '/Generative/images/flow/i-resnet4.png' width = '400'>
	- https://github.com/jhjacobsen/invertible-resnet
	- With contractive g(), i.e., Lip(g(theta)) < 1:\
		<img src = '/Generative/images/flow/i-resnet.png' width = '400'>
	- For generative model, ln(px(x)) = ln(pz(z))+ln|det(JF(x))|, with JF as the Jacobian of F(), since F=I+g() as the residual block, we could have a Taylor expansion.
	- Three computation drawbacks: (1) evaluate tr(J); (2) power of J; (3) Taylor has infinite terms;
	- For (1), (2), the approximate trick;
	- For (3), truncated at n steps;
	- The algorithm:\
		<img src = '/Generative/images/flow/i-resnet3.png' width = '400'>
- Conor Durkan, Artur Bekasov, Iain Murray, and George Papamakarios. Neural spline flows. NIPS'19
- Aditya Grover, Christopher Chute, Rui Shu, Zhangjie Cao, Stefano Ermon. AlignFlow: Cycle Consistent Learning from Multiple Domains via Normalizing Flows. 2019
