# AE/Variational Auto Encoder

## Basics
- ELBO: logp(x) ≥ E_q(z)[logp(x,z)-logq(z)] (check VI)
	- LatentGMM/...: p(x,z) = p(x)p(z|x)
	- = E_q(z)[logp(x,z)] + H(q(z))
- VAE: q(z) as q(z|x), p(x,z) as p(z)p(x|z) in ELBO
	- logp(x) ≥ L = E_q(z|x)[logp(x|z)] - KL(q(z|x)||p(z))
	- Main diff: p(x,z) = p(x|z)p(z), b/c p(z|x) intractable;
	- Gap: KL(q(z|x)||p(z|x))
- Learn q(z|x), s.t. Eq[logp(x|z)+logp(z)] + H(q(z|x))
	- Let r=logp(x|z)+logp(z), reward;
	- Can learn with REINFORCE; (wake-sleep)
		- J(φ) = Eq(z|x;φ)[r(xi,z)]
		- ∇J(φ) = Eq[∇logq(z|x;φ)r(x,z)]
	- Sampling + Reparametrization is much better;
		- ∇J(φ) = 1/M Σ ∇φ r(xi, μ(xi;φ)+σ(xi;φ)ε)
		- ∇r is more informational;
- Summaires
	- https://www.jianshu.com/p/bfa6b5947cd9
	- http://www.sohu.com/a/210551059_473283
	- https://zhuanlan.zhihu.com/p/34342392
	- https://blog.csdn.net/a7910932/article/details/46593691
	- https://www.zhihu.com/question/41765860
	- https://zhuanlan.zhihu.com/p/27239155
	- https://lilianweng.github.io/lil-log/2018/08/12/from-autoencoder-to-beta-vae.html#loss-function-elbo
- Common techniques:
	- Reparametrization trick;
	- Conditional: cVAE, semi-VAE;
	- Discrete (VQ-VAE, DVAE);
	- Backbone:
		- Recurrent encoder/decoder;
		- Hierarchical VAE;
	- Regularization on Latent code;
		- KL(q(z|x), p(z));
		- AAE: D(z-real, z-fake)
	- Latent-space disentangle;
		- β-VAE;
		- Impossible: ICML'19 best-paper;
	- Analysis:
		- with GAN;

## VAE-Basics
- A great codebase:
	- https://github.com/wohlert/semi-supervised-pytorch/tree/master/examples/notebooks
- **DLGM**: Rezende, Danilo J, Mohamed, Shakir, and Wierstra, Daan. Stochastic backpropagation and approximate inference in deep generative models. ICML'14
	- Graphical model:\
		<img src="/Generative/images/vae/vae-dlgm-1.png" alt="drawing" width="350"/>
	- Top-down generative process: from hL -> h1 -> v;
		- ξl ~ N(ξl|0, I), l=1, ..., L
		- hL = GL ξL
		- hl = Tl(hl+1) + Gl ξl, l=1, ..., L-1
		- v ~ π(v|T0(h1))
	- Reparametrization trick: p(v, h) = p(v, ξ)
	- Algorithm: data V NxD;
		- Sample mini-batch v;
		- Bottom up: ξn ~ q(ξn|vn)
			- q(ξ|V, θ) = Πn Πl N(ξn,l|μl(vn), Cl(vn))
		- Top down: h ~ h(ξ)
			- hl = Tl(hl+1) + Gl ξl
		- Upgrade gradient, SGD:
			- ∇θg F(v) = -Eq[∇θg logp(V|h)] + 1/κ θg
			- ∇μl F(v) = -Eq[∇ξl logp(v|h(ξ))] + μl
			- Let C = RR'
			- ∇Rl F(v) = -1/2 Eq[εl,j ∇ξl logp(v|h(ξ))] + 1/2 ∇Rl[TrCn,l - log|Cn,l|]
			- ∇θr F(v) = ∇μF(v) ∂μ/∂θr + Tr(∇RF(v) ∂R/∂θr)
- Semi-VAE: Kingma, D.P., Jimenez Rezende, D., Mohamed, S., Welling, M.: Semi-supervised learning with deep generative models. NIPS'14
	- Problem setup: some (x, y) pairs, some x only;
	- Formulation:
		- Generative: p(x|y, z)
		- Recognition: q(z,y|x) = q(y|x)q(z|x,y)
	- Formulation:
		- Known y: logp(x,y) >= Eq(z|x,y)[logpθ(x|y, z) + logpθ(y) + logp(z) − logqφ(z|x, y)] = −L(x, y);
		- Unknown y: logp(x) >= Eq(y,z|x)[log pθ(x|y, z) + log pθ(y) + log p(z) − log qφ(y, z|x)]
			- = Σy q(y|x)(-L(x,y)) + H(q(y|x))
- **cVAE**: Sohn, K., Lee, H., Yan, X.: Learning structured output representation using deep conditional generative models. NIPS'15
	- Insight: condition everything on class c;
	- ELBO := E_q(z|x,c)[logp(x|z, c)] - KL(q(z|x,c)|p(z|c))
- **VIMCO**: A Mnih and D Rezende. Variational inference for monte carlo objectives. ICML'16

## Backbone
- Recurrent encoder/decoder:
	- Good summaries: https://chuansongme.com/n/1628774042621
	- **DRAW**: A Recurrent Neural Network For Image Generation. ICML'15
		- https://github.com/ericjang/draw
		- https://github.com/chenzhaomin123/draw_pytorch
		- Recurrent encoder: q(zt|x, z1:t-1)
		- Recurrent decoder: recurrent h, ct = ct-1 + write(ht), one stroke at a time;
		- Loss: p(x|z1:T) reconstruction loss;
	- Rezende, D., Danihelka, I., Gregor, K., Wierstra, D., et al. One-shot generalization in deep generative models. ICML'16
	- Fabius, O. and van Amersfoort, J. R. Variational recurrent auto-encoders. ICLR'15
	- **VRNN**: J Chung, K Kastner, L Dinh, K Goel, A Courville, and Y Bengio. A recurrent latent variable model for sequential data. NIPS'15
	- Samuel R. Bowman, Luke Vilnis, Oriol Vinyals, Andrew M. Dai, Rafal Jozefowicz, Samy Bengio. Generating Sentences From a Continuous Spaces, ICLR'16
	- Neural Variational Inference for Text Processing, ICML'16
	- Language as a Latent Variable: Discrete Generative Models for Sentence Compression, EMNLP'16
	- A Hierarchical Latent Variable Encoder-Decoder Model for Generating Dialogues, AAAI'17
	- **TD-VAE**: K Gregor, G Papamakarios, F Besse, L Buesing, T Weber. Temporal Difference Variational Auto-Encoder. 2019
- Hierarchical:
	- R Ranganath, D Tran, and D Blei. Hierarchical variational models. ICML'16
	- Harrison A Edwards and Amos J. Storkey. Towards a neural statistician. ICLR'17
	- A Klushyn, N Chen, R Kurle, B Cseke, and P Smagt. Learning hierarchical priors in vaes. NIPS'19
		- Prior: p(z) = Πp(zl|z..l-1)
		- Approx posterior: q(z|x)=Πq(zl|z..l-1, x)
		- LVAE(x) := Eq(z|x)[logp(x|z)] − KL(q(z1|x)||p(z1)) − ΣEq(z..l-1|x)[KL(q(zl|x,z..l-1), p(zl|z..l-1))]

## Latent code
- Discrete
	- **DVAE**: Discrete Variational Autoencoders with Relaxed Boltzmann Priors. NIPS'18
		- https://github.com/QuadrantAI/dvae
- Disentanglement:
	- G. Desjardins, A. Courville, and Y. Bengio. Disentangling factors of variation via generative entangling. arxiv'12
		- First paper on deep disentangled representation learning;
	- S. Reed, K. Sohn, Y. Zhang, and H. Lee. Learning to disentangle factors of variation with manifold interaction. ICML'14
	- Z. Zhu, P. Luo, X. Wang, and X. Tang. Multi-view perceptron: a deep model for learning face identity and view representations. NIPS'14
	- J. Yang, S. Reed, M.-H. Yang, and H.Lee. Weakly-supervised disentangling with recurrent transformations for 3d view synthesis. NIPS'15
	- R. Goroshin, M. Mathieu, and Y. LeCun. Learning to linearize under uncertainty. NIPS'15
	- **β-VAE**: I Higgins, L Matthey, A Pal, C Burgess, X Glorot, M Botvinick, S Mohamed, A Lerchner. β-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework. ICLR'17
		- Better disentangle
		- Measures disentanglement as the accuracy of a linear classifier that predicts the index of a fixed factor of variation
		- max Ex[Eq(z|x)[logp(x|z)]], s.t. KL(q(z|x), p(z)) < ε
		- F = Eq(z|x)[logp(x|z)] - β(KL(q(z|x), p(z)) - ε)
	- DIP-VAE: Kumar, A., Sattigeri, P., and Balakrishnan, A. Variational inference of disentangled latent concepts from unlabeled observations. ICLR'17
		- Extend β-VAE by decomposing the KL-divergences into multiple terms, and only increase the weight on terms that analytically disentangles the models;
	- FactorVAE: H Kim, A Mnih. Disentangling by Factorising. ICML'18
		- Better disentanglement: majority vote classifier on a different feature vector which accounts for a corner case in the BetaVAE metric;
	- AnnealedVAE: C P. Burgess, I Higgins, A Pal, L Matthey, N Watters, G Desjardins, A Lerchner. Understanding disentangling in β-VAE. ICLR'18\
		<img src="/Generative/images/vae/beta-vae-understand.png" alt="drawing" width="450"/>
	- **β-TCVAE**: T Chen, X Li, R Grosse, and D Duvenaud. Isolating sources of disentanglement in variational autoencoders. NIPS'18
		- https://github.com/rtqichen/beta-tcvae
		- Mutual Information Gap (MIG)
	- F Locatello, S Bauer, M Lucic, G Rätsch, S Gelly, B Schölkopf, O Bachem. Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations. ICML'19 best paper
		- Fundamentally impossible without inductive biases: for any disentangled z, we can construct z2 fully entangled s.t. p(z2)=p(z), i.e., z and z2 are indistinguishable
		- Inductive biases:
			- Gaussian encoder: mean, log-variance
			- Bernoulli decoder: 10 latent dimension\
			<img src="/Generative/images/vae/vae-impossible.png" alt="drawing" width="500"/>
	- **VITAE**: N Skafte, S Hauberg. Explicit Disentanglement of Appearance and Perspective in Generative Models. NIPS'19
		- Insight: two latent codes zA, zP; then zP transform conanical view zA with a STN;

## Unclassified
- **DeepMind**:
	- Attend, infer, repeat: Fast scene understanding with generative models. ICML'16.
	- **ACN**: Graves et. al., Associative Compression Networks for Representation Learning (2018)
- **FAIR**:
	- Bouchacourt, D., Tomioka, R., and Nowozin, S. Multi-level variational autoencoder: Learning disentangled representations from grouped observations. AAAI'18.
	- **Non-Adversarial Mapping with VAEs**, NIPS'18
- **SOA**: L Maaløe, C Sønderby, S Sønderby, O Winther. Auxiliary Deep Generative Models. 2016
- **FVAE**: Z. Deng, R. Navarathna, P. Carr, S. Mandt, Y. Yue, I. Matthews, and G. Mori. Factorized variational autoencoders for modeling audience reactions to movies. CVPR'17.
- C Eastwood, C Williams. A framework for the quantitative evaluation of disentangled representations. ICLR'18

## Applications
- Temporal sequence:
	- Semeniuta, S., Severyn, A., and Barth, E. A hybrid convolutional variational autoencoder for text generation. ACL'17
		- 1D-Conv
	- Yang, Z., Hu, Z., Salakhutdinov, R., and Berg-Kirkpatrick, T. Improved variational autoencoders for text modeling using dilated convolutions. ICML'17
		- Dilated Conv;
	- **MT-VAE**: X Yan. MT-VAE: Learning Motion Transformations to Generate Multimodal Human Dynamics. ECCV'18
		- Encoder and decode motion sequence with LSTM;
- 3D:
	- M Gadelha, R Wang, and S Maji. Multiresolution tree networks for 3d point cloud processing. ECCV'18
		- z=Enc(.): image 2d encoder + MRT-pc-encoder (multiresolution-tree)
	- **PC-AAE**: M Zamorski, M Zieba, R Nowak, W Stokowiec, and T Trzciński. Adversarial autoencoders for generating 3d point clouds.
		- Encoder: pointnet;
		- Decoder: MLP + ReLU;

## Analysis of VAE
- Carter, S. and Nielsen, M. Using Artificial Intelligence to Augment Human Intelligence. 2017
- **GAN-VAE**: Z Hu, Z Yang, R Salakhutdinov, E Xing. On Unifying Deep Generative Models. ICLR'18
	- Understanding VAE and GAN with Wake-Sleep