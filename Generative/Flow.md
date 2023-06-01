# Flow based Approaches

## Good Summaries
- https://blog.evjang.com/2018/01/nf1.html
- https://blog.evjang.com/2018/01/nf2.html
- http://akosiorek.github.io/ml/2018/04/03/norm_flows.html
- **Survey**: G Papamakarios, E Nalisnick, D J Rezende, S M B Lakshminarayanan. Normalizing Flows for Probabilistic Modeling and Inference. 2019
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
- J Ho, E Lohn, P Abbeel. Compression with Flows via Local Bits-Back Coding. NIPS'19
- ClothFlow: A Flow-Based Model for Clothed Person Generation. ICCV'19
- DUAL-GLOW: Conditional Flow-Based Generative Model for Modality Transfer. ICCV'19

## Normalizing Flows
- NF Models:
	- **MADE**: M Germain, K Gregor, I Murray, and H Larochelle. Made: Masked autoencoder for distribution estimation. ICML'15
		- A specially designed architecture to enforce the autoregressive property in the autoencoder efficiently
			<img src = '/Generative/images/flow/made.png' width = '500'>
- VAE + Flow:
	- OpenAI. Variational lossy autoencoder. ICLR'16
	- f-VAEs: J Su, G Wu. f-VAEs: Improve VAEs with Conditional Flows. 2018
		- Encoder as flow: q(z|x) invertible, can be conditioned on x;
- Autoregressive Flow:
	- Y Song, C Meng, and S Ermon. MintNet: Building invertible neural networks with masked convolutions. NIPS'19
	- P Jaini, K Selby, and Y Yu. Sum-of-squares polynomial flow. ICML'19
	- N D Cao, I Titov, and W Aziz. Block neural autoregressive flow. UAI'19
- Flow + GAN:
	- DeepMind. Comparison of maximum likelihood and gan-based training of real nvps. 2017
	- A Grover, M Dhar, and S Ermon. Flow-gan: Combining maximum likelihood and adversarial learning in generative models. AAAI'18
- PointFlow: G Yang, X Huang, Z Hao, M Liu, S Belongie, B Hariharan. PointFlow: 3D Point Cloud Generation with Continuous Normalizing Flows. ICCV'19
	<img src = '/Generative/images/flow/pointflow.png' width = '600'>
- Z Xiao, Q Yan, and Y Amit. Generative latent flow. arxiv'19
- M Kumar, M Babaeizadeh, D Erhan, C Finn, S Levine, L Dinh, and D Kingma. Videoflow: A flow-based generative model for video. 2019

## Flow-based Graph Generation
- C Shi, M Xu, Z Zhu, W Zhang, M Zhang, J Tang. GraphAF: a Flow-based Autoregressive Model for Molecular Graph Generation. ICLR'20
	- https://drive.google.com/drive/folders/1LFfB5l0B6Zb-8WtV0EhmgolpHc9h-rcI

## Generalization
- **RAD**: L Dinh, J Sohl-Dickstein, R Pascanu, and H Larochelle. A RAD approach to deep mixture models. ICLR'19

## Invertible
- Y Teng, A Choromanska, and M Bojarski. Invertible autoencoder for domain adaptation. 2018
- R Schirrmeister, P. Chraba ̧szcz, F. Hutter, and T. Ball. Training generative reversible networks. 2018
- F Ma, U Ayaz, S Karaman. Invertibility of Convolutional Generative Networks from Partial Measurements. NIPS'18
- L Ardizzone, J Kruse, S Wirkert, D Rahner, E Pellegrini, R Klessen, L Maier-Hein, C Rother, U Köthe. Analyzing Inverse Problems with Invertible Neural Networks. ICLR'19
- A Grover, C Chute, R Shu, Z Cao, S Ermon. AlignFlow: Cycle Consistent Learning from Multiple Domains via Normalizing Flows. 2019
