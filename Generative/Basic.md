# Generative Modeling

## Basics
- Goal:
	- Authentic, high-quality;
	- Steerable;
	- Disentangled;
	- Conditional
- Evaluation
	- Image:
		- IS (Inception Score);
		- FID score;
	- Probability model:
		- To model p(x)
		- NLL/perplexity (VAE, flow);
- Applications
	- Music (1D);
		- CocoNet (Google Magenta), MuseNet, JukeBox (OpenAI);
	- TTS;
		- WaveNet, Baidu-Series, Heiga Zen (Google);
	- Inpainting;
	- Image super-resolution;
	- Style-Transfer:
		- pix2pix, CRN, Cycle-GAN;
	- Conditional: class/text/... guided;
		- CLIP;
	- Video:
		- VPN (autoregressive);
		- VGAN, MoCoGAN, pix2pixHD, vid2vid;
		- Everybody dance now;

## Approaches
- Legacy
	- Copy and Paste/Flow/Warp
	- Basics: image-based rendering;
- Framework/Loss design:
	- GAN/adversarial;
	- VAE/DLGM;
	- Energy/score-based;
	- Autoregressive;
		- PixelCNN, PixelRNN, PixcelCNN++, Pixel-SNAIL, VPN, PixelVAE;
	- Flow-based/NODE/CNF;
		- CNF: NICE, MADE, RealNVP, Glow;
		- Continuous: NODE, PointFlow, ...
	- Diffusion: DDPM;
	- Implicit;
- Backbone design:
	- Attention: A-GAN;
- Operator design:
	- Spectral-norm: SN-GAN;
- Progressive:
	- Progressive GAN;
- Two-stage/Latent-space;
	- Discrete: VQ-VAE, VQ-VAE2 (VQ+AR);
- Conditional:
	- semi-VAE, c-VAE, c-GAN;
- Disentangled:
	- beta-VAE;
	- ICML'19 best paper: not possbile for disentabled representation;

## Backbone/Op
- RBM/MLP:
	- AR: NADE;
- RNN/LSTM:
	- AR: PixelCNN, PixelRNN;
	- Flow: recurrent-flow;
	- VAE: DRAW, VRNN, TD-VAE;
- Conv/Deconv:
	- DCGAN;
	- AR: WaveNet, Audio-DeepDream;
	- VAE: PixelVAE;
- **Invertible** Op (required by Flow):
	- Affine/location-scale: NICE, RealNVP, IAF, MAF, Glow;
	- Non-affine: conic (NAF, block NAF, B-NAF, Flow++);
		- drawback: not inverted analytically, only iteratively via bp;
	- Residual flow (with Lip < 1)
	- CNF: PointFlow ICCV'19;
	- 1D: WaveGlow;
	- Graph: GNF'19, 
- Transformer:
	- AR:
		- Image transformer. ICML'18
		- OpenAI. Generating Long Sequences with Sparse Transformers. 2019
	- GAN: SA-GAN, BigGAN;
- UNet:
	- Standard: UNet MICCAI'15,
	- AR: PixelCNN++;
	- DM:
		- Prafulla Dhariwal and Alex Nichol. Diffusion Models Beat GANs on Image Synthesis. 2021
		- DDPM '19;
		- Score-Based Generative Modeling through Stochastic Differential Equations. ICLR'21
- Multiscale:
	- AR:
		- OpenAI. Parallel multiscale autoregressive density estimation. ICML'17.
		- Generating high fidelity images with subscale pixel networks and multidimensional upscaling. 2018
	- Style-transfer: SPADE;
- Progressive/Refine:
	- Naturally all AR, Flow, DM;
	- Progressive-GAN: NVIDIA ICLR'18
	- CRN. Q Chen, Koltun. ICCV'17
	- Stroke/sketch-based:
		- Neural Program. NIPS'18; NPI (ICLR'16);
		- D. Ha Chinese-char 15; sketch-RNN;
		- GAN+RL: SPIRAL (ICML'18);
		- VAE: Draw ICML'15; Conceptual-compression NIPS'16;
- Conditional/Multimodal
	- cGAN, cVAE;
	- DM:
		- Classifier: target class y predictable by a classifer;
			- ADMNet, 
		- Classifier-free (implicit): p(x|y) and p(x|∅)
		- CLIP-based:
			- GLIDE: CLIP + classifier-free guidance;
			- DALLE-2;
- Operators:
	- Dilated-Conv: PixelSNAIL (AR);
	- Spectral-Norm; (to guarantee Lip/op-norm <= 1)

## Latent/Hierarchical (Always Two-Stage)
- VAE:
	- VQ-VAE, VQ-VAE-2, DVAE;
- AR:
	- VQ-VAE-2;
- GAN:
	- VQ-GAN;
- DM:
	- LDM: Stable-Diffusion CVPR'22
	- Hierarchical: Cascaded Diffusion. '21

## Loss Design
- Standard: (L1/L2/...)
	- AE;
	- By byte:
		- AR: DeepMind. ByteNet.'16
- Latent space distance:
	- CRN: L1-norm on intermediate;
- Diversity loss;
- Adversarial:
	- GAN, WGAN, pix2pix;
	- Flow: Flow-GAN, ...
	- AE: AAE (Adv-loss for decoding quality);
- Likelihood:
	- AR: PixelCNN++;
	- Flow: 
- Reweighted objective:
	- Common and critical in DM;
- AE/DAE;
	- DM, score-matching;
- Information:
	- InfoGAN;
	- Beta-VAE;
- Consistency (a lot in style-transfer)
	- Cycle-GAN: |F(G(x))-x| + |G(F(y))-y|

## Combination
- VAE + AR:
	- IAF: D Kingma and T Salimans. Improving variational inference with inverse autoregressive flow. NIPS'16
	- PixelVAE;
- VAE + Flow:
	- Variational lossy autoencoder. ICLR'16
	- f-VAE, 
- Adversarial:
	- AR: PixelGAN;

## Special
- VAE
	- DVIB;
- GAN:
	- WGAN, WGAN-GP;
	- Training tricks;
- DM:
	- Advanced sampling: DDIM, ...
	- Theory: SMLD ~ DDPM; (an SDE look)

## Energy/Optimization-Based
- Energy-based:
	- J Zhao, M Mathieu, Y LeCun. Energy-based Generative Adversarial Network. 2016
	- Yilun Du and Igor Mordatch. Implicit generation and modeling with energy based models. NeurIPS'19
- Erik Nijkamp, Mitch Hill, Song-Chun Zhu, Ying Nian Wu. Learning Non-Convergent Non-Persistent Short-Run MCMC Toward Energy-Based Model. NIPS'19

## Autoregressive/Progressive
- NADE, RNADE, ...
- IAF;
- Transformer:
	- Parmar, N., Vaswani, A., Uszkoreit, J., Kaiser, Ł., Shazeer, N., and Ku, A. Image transformer. ICML'18
	- R. Child, S. Gray, A. Radford, I. Sutskever. Generating Long Sequences with Sparse Transformers. 2019
- Audio: WaveNet;
- More high-level action: one-stroke at a time;
	- DRAW, sketch-RNN, Spiral;

## Flow-based
- VAE+Flow:
	- f-VAE, sylvester-nf;
- IAF, NAF, Flow++;
- Continuous flow:
	- Neural ODE, PointFlow, occflow;

## Implicit
- Only defines generating process, likelihood-free;
- Shakir Mohamed, Balaji Lakshminarayanan. Learning in Implicit Generative Models. axriv'16

## Diffusion/Score-based
- DDPM:
- Score-based:
	- Yang Song and Stefano Ermon. Generative modeling by estimating gradients of the data distribution. NeurIPS'19

## Theory and Analysis
- Shengjia Zhao, Hongyu Ren, Arianna Yuan, Jiaming Song, Noah Goodman, Stefano Ermon. Bias and Generalization in Deep Generative Models: An Empirical Study. NIPS'18
- Hisham Husain, Richard Nock, Robert Williamson. A Primal-Dual link between GANs and Autoencoders. NIPS'19
- Zhiting Hu, Zichao Yang, Ruslan Salakhutdinov, Xiaodan Liang, Lianhui Qin, Haoye Dong, Eric Xing. Deep Generative Models with Learnable Knowledge Constraints. NIPS'18
