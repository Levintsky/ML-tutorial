# Generative Modeling

## Basics
- Goal:
	- Authentic, high-quality;
	- Steerable;
	- Disentangled;
- Evaluation
	- Image:
		- IS (Inception Score);
		- FID score;
	- Probability model:
		- To model p(x)
		- NLL/perplexity (VAE, flow);
- Applications
	- Inpainting;
	- Image super-resolution;
	- Style-Transfer:
		- pix2pix, CRN, Cycle-GAN;
	- Music;
		- CocoNet (Google Magenta), MuseNet, JukeBox (OpenAI);
	- TTS;
		- WaveNet, Baidu-Series, Heiga Zen (Google);
	- Video:
		- VPN (autoregressive);
		- VGAN, MoCoGAN, pix2pixHD, vid2vid;
		- Everybody dance now;

## Legacy (Copy and Paste/Flow/Warp)
- Basics: image-based rendering;

## GAN
- Basics:
	- Another Neural Net to discriminate (adversarial);
- WGAN, WGAN-GP, InfoGAN;
- SN-GAN;
- Attention/Transformer:
	- SA-GAN;
- Progressive GAN;
- Steerability;

## VAE
- Basics: ELBO, variational;
- Legacy: VAE, DLGM, semi-VAE, c-VAE, DVIB, beta-VAE;
- ICML'19 best paper: not possbile for disentabled representation;
- Discrete: VQ-VAE, VQ-VAE2;

## Energy/Optimization-Based
- Basics: generate signals with lower energy;
- Energy-based:
	- J Zhao, M Mathieu, Y LeCun. Energy-based Generative Adversarial Network. 2016
	- Yilun Du and Igor Mordatch. Implicit generation and modeling with energy based models. NeurIPS'19
- Score-based:
	- Yang Song and Stefano Ermon. Generative modeling by estimating gradients of the data distribution. NeurIPS'19

## Autoregressive/Progressive
- Basics: Generate result piece by piece;
- NADE, RNADE, ...
- PixelCNN, PixelRNN, PixcelCNN++, Pixel-SNAIL, VPN, PixelVAE;
- IAF;
- Transformer:
	- Parmar, N., Vaswani, A., Uszkoreit, J., Kaiser, Ł., Shazeer, N., and Ku, A. Image transformer. ICML'18
	- R. Child, S. Gray, A. Radford, I. Sutskever. Generating Long Sequences with Sparse Transformers. 2019
- Audio: WaveNet;
- More high-level action: one-stroke at a time;
	- DRAW, sketch-RNN, Spiral;

## Flow-based
- Normalsing flow: NICE, MADE, RealNVP, Glow;
- VAE+Flow:
	- f-VAE, sylvester-nf;
- IAF, NAF, Flow++;
- Continuous flow:
	- Neural ODE, PointFlow, occflow;

## Implicit
- Only defines generating process, likelihood-free;
- Shakir Mohamed, Balaji Lakshminarayanan. Learning in Implicit Generative Models. axriv'16

## Theory and Analysis
- Shengjia Zhao, Hongyu Ren, Arianna Yuan, Jiaming Song, Noah Goodman, Stefano Ermon. Bias and Generalization in Deep Generative Models: An Empirical Study. NIPS'18
- Hisham Husain, Richard Nock, Robert Williamson. A Primal-Dual link between GANs and Autoencoders. NIPS'19
- Zhiting Hu, Zichao Yang, Ruslan Salakhutdinov, Xiaodan Liang, Lianhui Qin, Haoye Dong, Eric Xing. Deep Generative Models with Learnable Knowledge Constraints. NIPS'18
