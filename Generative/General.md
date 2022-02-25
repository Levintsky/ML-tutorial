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

## Diffusion Process
- Basics:
	- x0 (original signal)
	- Denoising: p() xT - ... - xt - xt-1 - x0
		- Prob model: p(x0:T)=p(xT) prod p(xt-1|xt); i.e., denoising process;
		- p(xt-1|x) = N(xt-1; mu(xt, t), Sigma(xt, t))
	- Adding noise: q() x0 - x1 - x2 - ... - xT as the approximate posterior q()
		- Forward pass (diffusion process), q(x1:T|x0)=prod q(xt|xt-1);
		- Model: q(xt|xt-1)=N(xt; sqrt(1-beta_t)xt-1, beta_t)
		- beta can be constant or learned by reparametrization trick;
	- Goal: maximise p(x0;theta) = int p(x0:T) dx1:T
		- ELBO: E(-log p(x0)) = Eq(-log p(x0:T)/q(x1:T|x0))
		- q(xt|x0) ~ N(xt; sqrt(alpha't)x0, (1-alpha't)I), because of Gaussian additive!
	- Training:
		- Optimize any term of Lt-1=KL(q(xt-1|x0, xt) || p(xt-1|xt))
		- Fit p(xt-1|xt,x0) with mean given x0, xt
	- Inference:
		- Start from XT, xt-1=xt+sigmat z, z ~ N(0, 1) Langevin dynamics;
- Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. Deep unsupervised learning using nonequilibrium thermodynamics. ICML'15
- Jonathan Ho, Ajay Jain, Pieter Abbeel. Denoising Diffusion Probabilistic Models. NeurIPS'20
	- https://github.com/hojonathanho/diffusion
	- High-quality result with Langevin dynamics;

## Energy/Optimization-Based
- Basics: generate signals with lower energy;
- J Zhao, M Mathieu, Y LeCun. Energy-based Generative Adversarial Network. 2016
- Yilun Du and Igor Mordatch. Implicit generation and modeling with energy based models. NeurIPS'19
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

## Theory and Analysis
- Shengjia Zhao, Hongyu Ren, Arianna Yuan, Jiaming Song, Noah Goodman, Stefano Ermon. Bias and Generalization in Deep Generative Models: An Empirical Study. NIPS'18
- Hisham Husain, Richard Nock, Robert Williamson. A Primal-Dual link between GANs and Autoencoders. NIPS'19
- Zhiting Hu, Zichao Yang, Ruslan Salakhutdinov, Xiaodan Liang, Lianhui Qin, Haoye Dong, Eric Xing. Deep Generative Models with Learnable Knowledge Constraints. NIPS'18
