# Flow based Approaches

## Good Summaries
- https://blog.evjang.com/2018/01/nf1.html
- https://blog.evjang.com/2018/01/nf2.html
- http://akosiorek.github.io/ml/2018/04/03/norm_flows.html
- **Survey**: George Papamakarios, Eric Nalisnick, Danilo Jimenez Rezende, Shakir Mohamed Balaji Lakshminarayanan. Normalizing Flows for Probabilistic Modeling and Inference. 2019
	- Expressive power: universal representation is possible under reasonable conditions (proved with Autogressive flows);
	- Optimize θ = (φ, ψ), for Transform φ and prior ψ:\
		<img src = '/Generative/images/flow/survey1.png' width = '400'>
	- Constructing Flows (finite compositions):
		- Practical consideration:
			- Normalization;
	- Generalization: generate probability;
		- RAD;
		- Discrete distribution;
		- Riemannian manifold;
	- Applications:
		- Probabilistic modeling: MLE: KL(px(x), px(x, θ)), density estimation;
		- Generation;
		- Inference: modeling parameters to infer unkonwn quantities within a model;
		- Representation learning;
		- RL: imitation learning; Yannick Schroecker, Mel Vecerik, and Jon Scholz. Generative predecessor models for sample-efficient imitation learning. ICLR'19

## Misc
- Jonathan Ho, Evan Lohn, Pieter Abbeel. Compression with Flows via Local Bits-Back Coding. NIPS'19
- ClothFlow: A Flow-Based Model for Clothed Person Generation. ICCV'19
- DUAL-GLOW: Conditional Flow-Based Generative Model for Modality Transfer. ICCV'19

## Normalizing Flows
- NF Models:
	- **MADE**: M Germain, K Gregor, I Murray, and H Larochelle. Made: Masked autoencoder for distribution estimation. ICML'15
		- A specially designed architecture to enforce the autoregressive property in the autoencoder efficiently
			<img src = '/Generative/images/flow/made.png' width = '500'>
- VAE + Flow:
	- Xi Chen, Diederik P Kingma, Tim Salimans, Yan Duan, Prafulla Dhariwal, John Schulman, Ilya Sutskever, and Pieter Abbeel. Variational lossy autoencoder. ICLR'16
	- **f-VAEs**: J Su, G Wu. f-VAEs: Improve VAEs with Conditional Flows. 2018
- Autoregressive Flow:
	- Yang Song, Chenlin Meng, and Stefano Ermon. MintNet: Building invertible neural networks with masked convolutions. NIPS'19
	- Priyank Jaini, Kira A. Selby, and Yaoliang Yu. Sum-of-squares polynomial flow. ICML'19
	- **B-NAF** Nicola De Cao, Ivan Titov, and Wilker Aziz. Block neural autoregressive flow. UAI'19
- Flow + GAN:
	- Ivo Danihelka, Balaji Lakshminarayanan, Benigno Uria, Daan Wierstra, and Peter Dayan. Comparison of maximum likelihood and gan-based training of real nvps. 2017
	- Aditya Grover, Manik Dhar, and Stefano Ermon. Flow-gan: Combining maximum likelihood and adversarial learning in generative models. AAAI'18
- **PointFlow**: G Yang, X Huang, Z Hao, M Liu, S Belongie, B Hariharan. PointFlow: 3D Point Cloud Generation with Continuous Normalizing Flows. ICCV'19
	- https://www.guandaoyang.com/PointFlow/
	- https://github.com/stevenygd/PointFlow
	- Based on CNF (FFJORD)\
		<img src = '/Generative/images/flow/pointflow.png' width = '600'>
- Manoj Kumar, Mohammad Babaeizadeh, Dumitru Erhan, Chelsea Finn, Sergey Levine, Laurent Dinh, and Durk Kingma. Videoflow: A flow-based generative model for video. 2019

## Flow-based Graph Generation
- Chence Shi, Minkai Xu, Zhaocheng Zhu, Weinan Zhang, Ming Zhang, Jian Tang. GraphAF: a Flow-based Autoregressive Model for Molecular Graph Generation. ICLR'20
	- https://drive.google.com/drive/folders/1LFfB5l0B6Zb-8WtV0EhmgolpHc9h-rcI

## Generalization
- **RAD**: Laurent Dinh, Jascha Sohl-Dickstein, Razvan Pascanu, and Hugo Larochelle. A RAD approach to deep mixture models. ICLR'19

## Invertible
- Yunfei Teng, Anna Choromanska, and Mariusz Bojarski. Invertible autoencoder for domain adaptation. 2018
- R.T. Schirrmeister, P. Chraba ̧szcz, F. Hutter, and T. Ball. Training generative reversible networks. 2018
- Fangchang Ma, Ulas Ayaz, Sertac Karaman. Invertibility of Convolutional Generative Networks from Partial Measurements. NIPS'18
- Lynton Ardizzone, Jakob Kruse, Sebastian Wirkert, Daniel Rahner, Eric W. Pellegrini, Ralf S. Klessen, Lena Maier-Hein, Carsten Rother, Ullrich Köthe. Analyzing Inverse Problems with Invertible Neural Networks. ICLR'19
- Aditya Grover, Christopher Chute, Rui Shu, Zhangjie Cao, Stefano Ermon. AlignFlow: Cycle Consistent Learning from Multiple Domains via Normalizing Flows. 2019
