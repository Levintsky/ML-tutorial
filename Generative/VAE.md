# Variational Auto Encoder

## VAE-Basics
- A Very good tutorial:
	- https://www.jianshu.com/p/bfa6b5947cd9
	- http://www.sohu.com/a/210551059_473283
	- https://zhuanlan.zhihu.com/p/34342392
	- https://blog.csdn.net/a7910932/article/details/46593691
	- https://www.zhihu.com/question/41765860
	- https://zhuanlan.zhihu.com/p/27239155
- A great codebase:
	- https://github.com/wohlert/semi-supervised-pytorch/tree/master/examples/notebooks
- **VAE**:
	- Diederik P Kingma and Max Welling. Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114, 2013.
		- **ELBO**: L = -KL(q(z|x), p(z)) + E_q(p(x|z))
		- **BCE** (Binary Cross Entropy) for reconstruction (mnist)
		<img src="/Generative/images/vae-elbo.png" alt="drawing" width="500"/>
		<img src="/Generative/images/vae-elbo2.png" alt="drawing" width="500"/>

	- Conditional VAE: Kingma, D.P., Jimenez Rezende, D., Mohamed, S., Welling, M.: Semi-supervised learning with deep generative models. NIPS 2014
	<img src="/Generative/images/vae-semi1.png" alt="drawing" width="350"/>
	<img src="/Generative/images/vae-semi2.png" alt="drawing" width="500"/>

	- Sohn, K., Lee, H., Yan, X.: Learning structured output representation using deep conditional generative models. NIPS 2015
- **DeepMind**:
	- Rezende, Danilo J, Mohamed, Shakir, and Wierstra, Daan. Stochastic backpropagation and approximate inference in deep generative models. ICML 2014
	- D. J. Rezende and S. Mohamed. Variational inference with normalizing flows. ICML'15
	- Rezende, D., Danihelka, I., Gregor, K., Wierstra, D., et al. One-shot generalization in deep generative models. In ICML, 2016.
	- **DRAW**: A Recurrent Neural Network For Image Generation. ICML 2015
		- https://github.com/ericjang/draw
		- https://github.com/chenzhaomin123/draw_pytorch
	- Eslami, S. A., Heess, N., Weber, T., Tassa, Y., Szepesvari, D., Kavukcuoglu, K., and Hinton, G. E. Attend, infer, repeat: Fast scene understanding with generative models. ICML'16.
	- **Beta-VAE**: Irina Higgins, Loic Matthey, Arka Pal, Christopher Burgess, Xavier Glorot, Matthew Botvinick, Shakir Mohamed, Alexander Lerchner. beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework. ICLR 2017
		- Better disentangle
		- Measures disentanglement as the accuracy of a linear classifier that predicts the index of a fixed factor of variation
	- **VQ-VAE**: Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu. Neural Discrete Representation Learning. NIPS'17
		- VAE with discrete latent variables
	- AnnealedVAE: C P. Burgess, I Higgins, A Pal, L Matthey, N Watters, G Desjardins, A Lerchner. Understanding disentangling in β-VAE. ICLR'18
	- **ACN**: Graves et. al., Associative Compression Networks for Representation Learning (2018)
	- FactorVAE: H Kim, A Mnih. Disentangling by Factorising. ICML'18
		- Better disentanglement: majority vote classifier on a different feature vector which accounts for a corner case in the BetaVAE metric
	- **VQ-VAE-2**: Ali Razavi, Aäron van den Oord, Oriol Vinyals. Generating Diverse High-Fidelity Images with VQ-VAE-2. 2019
- **Google-Brain**:
	- **DVIB**: A Alemi, I. Fischer, J V. Dillon, K Murphy. Deep Variational Information Bottleneck. ICLR'16
	- F Locatello, S Bauer, M Lucic, G Rätsch, S Gelly, B Schölkopf, O Bachem. Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations. ICML'19 best paper
		<img src="/Generative/images/vae-impossible.png" alt="drawing" width="500"/>

		- Fundamentally impossible without inductive biases: for any disentangled z, we can construct z2 fully entangled s.t. p(z2)=p(z), i.e., z and z2 are indistinguishable
		- Inductive biases:
			- Gaussian encoder: mean, log-variance
			- Bernoulli decoder: 10 latent dimension 

- **OpenAI**:
	- Xi Chen, Diederik P Kingma, Tim Salimans, Yan Duan, Prafulla Dhariwal, John Schulman, Ilya Sutskever, and Pieter Abbeel. Variational lossy autoencoder. arXiv preprint arXiv:1611.02731, 2016.
	- **IAF**: Kingma, D. P., Salimans, T., Jozefowicz, R., Chen, X., Sutskever, I., and Welling, M. Improved variational inference with inverse autoregressive flow. NIPS'16
- **FAIR**:
	- Bouchacourt, D., Tomioka, R., and Nowozin, S. Multi-level variational autoencoder: Learning disentangled representations from grouped observations. AAAI'18.
	- **Non-Adversarial Mapping with VAEs**, NIPS'18
- **GAN-VAE**: Z Hu, Z Yang, R Salakhutdinov, E Xing. On Unifying Deep Generative Models. ICLR'18
	- Understanding VAE and GAN with Wake-Sleep
- **LVAE**: Casper Kaae Sønderby, Tapani Raiko, Lars Maaløe, Søren Kaae Sønderby, Ole Winther. Ladder Variational Autoencoders. 2016
- **SOA**: Lars Maaløe, Casper Kaae Sønderby, Søren Kaae Sønderby, Ole Winther. Auxiliary Deep Generative Models. 2016
- Chen at. al., **Variational Lossy Autoencoder** (2017)
	- Minimum Description Length for VAE
- **FVAE**: Z. Deng, R. Navarathna, P. Carr, S. Mandt, Y. Yue, I. Matthews, and G. Mori. Factorized variational autoencoders for modeling audience reactions to movies. CVPR 2017.
- NIPS 2018:
	- **DVAE**: Discrete Variational Autoencoders with Relaxed Boltzmann Priors
		- https://github.com/QuadrantAI/dvae
	- Information Constraints on Auto-Encoding Variational Bayes
	- IntroVAE: Introspective Variational Autoencoders for Photographic Image Synthesis
	- Hamiltonian Variational Auto-Encoder
	- Importance Weighting and Variational Inference
	- beta-TCVAE: Chen, T. Q., Li, X., Grosse, R. B., and Duvenaud, D. K. **Isolating Sources of Disentanglement in Variational Autoencoders**
		- Mutual Information Gap (MIG)
	- Gaussian Process Prior Variational Autoencoders
- Cian Eastwood, Christopher K. I. Williams. A framework for the quantitative evaluation of disentangled representations. ICLR'18
- DIP-VAE: Kumar, A., Sattigeri, P., and Balakrishnan, A. Variational inference of disentangled latent concepts from unlabeled observations. ICLR'17
- Text:
	- Semeniuta, S., Severyn, A., and Barth, E. A hybrid convolutional variational autoencoder for text generation. 2017
		- 1D-Conv
	- Yang, Z., Hu, Z., Salakhutdinov, R., and Berg-Kirkpatrick, T. Improved variational autoencoders for text modeling using dilated convolutions. ICML'17

## Autoregressive
- **PixelVAE**: I Gulrajani, K Kumar, F Ahmed, A Ali Taiga, F Visin, D Vazquez, and A Courville. PixelVAE: A latent variable model for natural images. ICLR, 2017.
<img src="/Generative/images/pixel-vae1.png" alt="drawing" width="500"/>
<img src="/Generative/images/pixel-vae2.png" alt="drawing" width="300"/>

## Recurrent
- Good summaries:
	- https://chuansongme.com/n/1628774042621
- Fabius, O. and van Amersfoort, J. R. Variational recurrent auto-encoders. ICLR'15
- Samuel R. Bowman, Luke Vilnis, Oriol Vinyals, Andrew M. Dai, Rafal Jozefowicz, Samy Bengio. Generating Sentences From a Continuous Spaces, ICLR'16
- Neural Variational Inference for Text Processing, ICML'16
- Language as a Latent Variable: Discrete Generative Models for Sentence Compression, EMNLP'16
- A Hierarchical Latent Variable Encoder-Decoder Model for Generating Dialogues, AAAI'17

## Analysis of VAE
- Alemi, A. A., Poole, B., Fischer, I., Dillon, J. V., Saurous, R. A., and Murphy, K. An information-theoretic analysis of deep latent-variable models. 2017
- Carter, S. and Nielsen, M. Using Artificial Intelligence to Augment Human Intelligence. 2017