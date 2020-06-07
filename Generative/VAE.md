# Variational Auto Encoder

## Unclassified
- Constrained Generation of Semantically Valid Graphs via Regularizing Variational Autoencoders. NIPS'18
- Emile Mathieu, Charline Le Lan, Chris J. Maddison, Ryota Tomioka, Yee Whye Teh. Continuous Hierarchical Representations with Poincaré Variational Auto-Encoders. NIPS'19
- Muhan Zhang, Shali Jiang, Zhicheng Cui, Roman Garnett, Yixin Chen. D-VAE: A Variational Autoencoder for Directed Acyclic Graphs. NIPS'19

## Summaires
- https://www.jianshu.com/p/bfa6b5947cd9
- http://www.sohu.com/a/210551059_473283
- https://zhuanlan.zhihu.com/p/34342392
- https://blog.csdn.net/a7910932/article/details/46593691
- https://www.zhihu.com/question/41765860
- https://zhuanlan.zhihu.com/p/27239155
- https://lilianweng.github.io/lil-log/2018/08/12/from-autoencoder-to-beta-vae.html#loss-function-elbo

## VAE-Basics
- A great codebase:
	- https://github.com/wohlert/semi-supervised-pytorch/tree/master/examples/notebooks
- **VAE**: Diederik P Kingma and Max Welling. Auto-encoding variational bayes. ICLR'14
	- **ELBO**: L = -KL(q(z|x), p(z)) + E_q(p(x|z))
	- **BCE** (Binary Cross Entropy) for reconstruction (mnist)\
		<img src="/Generative/images/vae/vae-elbo.png" alt="drawing" width="500"/>
		<img src="/Generative/images/vae/vae-elbo2.png" alt="drawing" width="500"/>
- **DLGM**: Rezende, Danilo J, Mohamed, Shakir, and Wierstra, Daan. Stochastic backpropagation and approximate inference in deep generative models. ICML'14
	- Graphical model:\
		<img src="/Generative/images/vae/vae-dlgm-1.png" alt="drawing" width="350"/>
	- Top-down generative process:\
		<img src="/Generative/images/vae/vae-dlgm-2.png" alt="drawing" width="350"/>
	- Reparametrization trick:\
		<img src="/Generative/images/vae/vae-dlgm-3.png" alt="drawing" width="350"/>
	- Algorithm:\
		<img src="/Generative/images/vae/vae-dlgm-4.png" alt="drawing" width="350"/>
- Semi-VAE: Kingma, D.P., Jimenez Rezende, D., Mohamed, S., Welling, M.: Semi-supervised learning with deep generative models. NIPS'14
	- Problem setup: some (x, y) pairs, some x only;\
		<img src="/Generative/images/vae/vae-semi1.png" alt="drawing" width="300"/>
	- Formulation:\
		<img src="/Generative/images/vae/vae-semi2.png" alt="drawing" width="500"/>
- **cVAE**: Sohn, K., Lee, H., Yan, X.: Learning structured output representation using deep conditional generative models. NIPS 2015\
	<img src="/Generative/images/vae/cVAE.png" alt="drawing" width="450"/>
- **DVIB**: A Alemi, I. Fischer, J V. Dillon, K Murphy. Deep Variational Information Bottleneck. ICLR'17
	- The negative loss for connection with VAE; (Check Basic-ML/Info-Theory)

## Disentangle
- G. Desjardins, A. Courville, and Y. Bengio. Disentangling factors of variation via generative entangling. arxiv'12
	- First paper on deep disentangled representation learning;
- S. Reed, K. Sohn, Y. Zhang, and H. Lee. Learning to disentangle factors of variation with manifold interaction. ICML'14
- Z. Zhu, P. Luo, X. Wang, and X. Tang. Multi-view perceptron: a deep model for learning face identity and view representations. NIPS'14
- J. Yang, S. Reed, M.-H. Yang, and H.Lee. Weakly-supervised disentangling with recurrent transformations for 3d view synthesis. NIPS'15
- R. Goroshin, M. Mathieu, and Y. LeCun. Learning to linearize under uncertainty. NIPS'15
- **Beta-VAE**: Irina Higgins, Loic Matthey, Arka Pal, Christopher Burgess, Xavier Glorot, Matthew Botvinick, Shakir Mohamed, Alexander Lerchner. beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework. ICLR'17
	- Better disentangle
	- Measures disentanglement as the accuracy of a linear classifier that predicts the index of a fixed factor of variation
	<img src="/Generative/images/vae/beta-vae.png" alt="drawing" width="450"/>
- DIP-VAE: Kumar, A., Sattigeri, P., and Balakrishnan, A. Variational inference of disentangled latent concepts from unlabeled observations. ICLR'17
	- Extent beta-VAE by decomposing the KL-divergences into multiple terms, and only increase the weight on terms that analytically disentangles the models;
- AnnealedVAE: C P. Burgess, I Higgins, A Pal, L Matthey, N Watters, G Desjardins, A Lerchner. Understanding disentangling in β-VAE. ICLR'18\
	<img src="/Generative/images/vae/beta-vae-understand.png" alt="drawing" width="450"/>
- **β-TCVAE**: Tian Qi Chen, Xuechen Li, Roger B Grosse, and David K Duvenaud. Isolating sources of disentanglement in variational autoencoders. NIPS'18
	- https://github.com/rtqichen/beta-tcvae
	- Mutual Information Gap (MIG)
- F Locatello, S Bauer, M Lucic, G Rätsch, S Gelly, B Schölkopf, O Bachem. Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations. ICML'19 best paper
	- Fundamentally impossible without inductive biases: for any disentangled z, we can construct z2 fully entangled s.t. p(z2)=p(z), i.e., z and z2 are indistinguishable
	- Inductive biases:
		- Gaussian encoder: mean, log-variance
		- Bernoulli decoder: 10 latent dimension\
		<img src="/Generative/images/vae/vae-impossible.png" alt="drawing" width="500"/>
- **VITAE**: Nicki Skafte, Søren Hauberg. Explicit Disentanglement of Appearance and Perspective in Generative Models. NIPS'19
	- Insight: two latent codes zA, zP; then zP transform conanical view zA with a STN;
		<img src="/Generative/images/vae/vitae.png" alt="drawing" width="400"/>
	- Formulation:\
		<img src="/Generative/images/vae/vitae-2.png" alt="drawing" width="400"/>

## Discrete
- **VQ-VAE**: Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu. Neural Discrete Representation Learning. NIPS'17
	- VAE with discrete latent variables, K-means style codebook;\
		<img src="/Generative/images/vae/vq-vae1-1.png" alt="drawing" width="450"/>
	- Formulation:\
		<img src="/Generative/images/vae/vq-vae1-2.png" alt="drawing" width="450"/>
- **VQ-VAE-2**: Ali Razavi, Aäron van den Oord, Oriol Vinyals. Generating Diverse High-Fidelity Images with VQ-VAE-2. 2019
	- a two-level hierarchical VQ-VAE combined with self-attention autoregressive model.
	- Stage 1 is to train a hierarchical VQ-VAE: The design of hierarchical latent variables intends to separate local patterns (i.e., texture) from global information (i.e., object shapes). The training of the larger bottom level codebook is conditioned on the smaller top level code too, so that it does not have to learn everything from scratch.
	- Stage 2 is to learn a prior over the latent discrete codebook so that we sample from it and generate images. In this way, the decoder can receive input vectors sampled from a similar distribution as the one in training. A powerful autoregressive model enhanced with multi-headed self-attention layers is used to capture the prior distribution (like PixelSNAIL; Chen et al 2017).
	- Framework:\
		<img src="/Generative/images/vae/VQ-VAE-2.png" alt="drawing" width="450"/>
	- Algorithm:\
		<img src="/Generative/images/vae/VQ-VAE-2-algo.png" alt="drawing" width="450"/>

## Unclassified
- **DeepMind**:
	- Rezende, D., Danihelka, I., Gregor, K., Wierstra, D., et al. One-shot generalization in deep generative models. ICML'16.
	- **DRAW**: A Recurrent Neural Network For Image Generation. ICML 2015
		- https://github.com/ericjang/draw
		- https://github.com/chenzhaomin123/draw_pytorch
	- Eslami, S. A., Heess, N., Weber, T., Tassa, Y., Szepesvari, D., Kavukcuoglu, K., and Hinton, G. E. Attend, infer, repeat: Fast scene understanding with generative models. ICML'16.
	- **ACN**: Graves et. al., Associative Compression Networks for Representation Learning (2018)
	- FactorVAE: H Kim, A Mnih. Disentangling by Factorising. ICML'18
		- Better disentanglement: majority vote classifier on a different feature vector which accounts for a corner case in the BetaVAE metric 
- **OpenAI**:
	- Xi Chen, Diederik P Kingma, Tim Salimans, Yan Duan, Prafulla Dhariwal, John Schulman, Ilya Sutskever, and Pieter Abbeel. Variational lossy autoencoder. ICLR'16.
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
	- Gaussian Process Prior Variational Autoencoders
- Cian Eastwood, Christopher K. I. Williams. A framework for the quantitative evaluation of disentangled representations. ICLR'18
- Text:
	- Semeniuta, S., Severyn, A., and Barth, E. A hybrid convolutional variational autoencoder for text generation. 2017
		- 1D-Conv
	- Yang, Z., Hu, Z., Salakhutdinov, R., and Berg-Kirkpatrick, T. Improved variational autoencoders for text modeling using dilated convolutions. ICML'17
- Hierarchical VAE:
	- Harrison A Edwards and Amos J. Storkey. Towards a neural statistician. In ICLR, 2017

## Applications
- **MT-VAE**: Xinchen Yan, Akash Rastogi, Ruben Villegas, Kalyan Sunkavalli, Eli Shechtman, Sunil Hadap, Ersin Yumer, Honglak Lee. MT-VAE: Learning Motion Transformations to Generate Multimodal Human Dynamics. 2018

## Autoregressive
- **PixelVAE**: I Gulrajani, K Kumar, F Ahmed, A Ali Taiga, F Visin, D Vazquez, and A Courville. PixelVAE: A latent variable model for natural images. ICLR, 2017.
<img src="/Generative/images/autor/pixel-vae1.png" alt="drawing" width="450"/>
<img src="/Generative/images/autor/pixel-vae2.png" alt="drawing" width="250"/>

## Recurrent
- Good summaries:
	- https://chuansongme.com/n/1628774042621
- Fabius, O. and van Amersfoort, J. R. Variational recurrent auto-encoders. ICLR'15
- **VRNN**: J Chung, K Kastner, L Dinh, K Goel, A Courville, and Y Bengio. A recurrent latent variable model for sequential data. NIPS'15
- Samuel R. Bowman, Luke Vilnis, Oriol Vinyals, Andrew M. Dai, Rafal Jozefowicz, Samy Bengio. Generating Sentences From a Continuous Spaces, ICLR'16
- Neural Variational Inference for Text Processing, ICML'16
- Language as a Latent Variable: Discrete Generative Models for Sentence Compression, EMNLP'16
- A Hierarchical Latent Variable Encoder-Decoder Model for Generating Dialogues, AAAI'17
- **TD-VAE**: Karol Gregor, George Papamakarios, Frederic Besse, Lars Buesing, Theophane Weber. Temporal Difference Variational Auto-Encoder. 2019\
	<img src="/Generative/images/vae/td-vae.png" alt="drawing" width="500"/>

## Analysis of VAE
- Carter, S. and Nielsen, M. Using Artificial Intelligence to Augment Human Intelligence. 2017

## VAE on 3D
- Matheus Gadelha, Rui Wang, and Subhransu Maji. Multiresolution tree networks for 3d point cloud processing. ECCV'18
- **AAE**: Maciej Zamorski, Maciej Zieba, Rafał Nowak, Wojciech Stokowiec, and Tomasz Trzciński. Adversarial autoen-coders for generating 3d point clouds.
	- Alireza Makhzani, Jonathon Shlens, Navdeep Jaitly, Ian Goodfellow, and Brendan Frey. Adversarial autoencoders. 2015
