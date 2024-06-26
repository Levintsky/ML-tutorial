# General Adversarial Net

## GAN Inversion
- W Xia, Y Zhang, Y Yang, J Xue, B Zhou, and M Yang. GAN Inversion: A Survey. 2021

## Unclassified
- NIPS'19 oral:
	- Multi-marginal Wasserstein GAN. NIPS'19
- D W Shu, S W Park, and J Kwon. 3D Point Cloud Generative Adversarial Network Based on Tree Structured Graph Convolutions. ICCV'19
	- https://github.com/seowok/TreeGAN
- Specifying Object Attributes and Relations in Interactive Scene Generation. ICCV'19
- Counterfactual Critic Multi-Agent Training for Scene Graph Generation. ICCV'19
- Neural 3D Morphable Models: Spiral Convolutional Networks for 3D Shape Representation Learning and Generation. ICCV'19
- CompoNet: Learning to Generate the Unseen by Part Synthesis and Composition. ICCV'19
- Boundless: Generative Adversarial Networks for Image Extension. ICCV'19
- Others:
	- M. Liu and O. Tuzel. Coupled generative adversarial networks. NeurIPS'16
- PixelGAN: A Makhzani, B Frey. PixelGAN Autoencoders. 2017
	- q(z|x) and p(z) adversarial loss (encoded latent)
	- Loss = L-VAE - I(z;x)
- Graphical Generative Adversarial Networks. NIPS'18
- Yair Weiss. On GANs and GMMs. NIPS'18

## Loss Function
- **WGAN**: M Arjovsky, S Chintala and L Bottou. Wasserstein GAN. 2017
	- Very good explanation: https://vincentherrmann.github.io/blog/wasserstein/
	- Alex Irpan's blog: https://www.alexirpan.com/2017/02/22/wasserstein-gan.html
	- W-GAN is Earth-Mover-Distance, Kantorovich-Rubinstein duality
		- To calculate primal EMD(p1, p2) = minπ ∫c(x,y) dπ(x,y)
			- s.t. ∫π(x,y)dy=p1(x), ∫π(x,y)dx=p2(y)
		- With Lagrange dual, we have L=EMD + ∫λ(x)(∫π(x,y)dy-p1(x))dx + ∫λ(y)(∫π(x,y)dx-p2(y))dy
		- Dual loss: L=∫λ(x)p1(x)dx - ∫λ(x)p2(x)dx = E.p1[λ(x)] - E.p2[λ(x)], s.t. Lip(λ(x))≤1
		- Intuitively, Lagrange λ(x) is the cost at each position x, λ(x1)-λ(x2)≤|x1-x2|, cost diff ≤ moving cost;
	- LD = E[D(x)] - E[D(G(z)]
	- LG = E[D(G(z))]
	- WD = clip_value(-0.01, 0.01)
- WGAN-GP: I Gulrajani, F Ahmed, M Arjovsky, V Dumoulin, and A Courville. Improved training of Wasserstein gans. NeurIPS'17
	- Insight: force penalty w.r.t. input is 1 almost everywhere;
	- Code: https://github.com/igul222/improved_wgan_training
	- LD = LD-WGAN + λE[(∥∇.x D(αx-(1-α)G(z))∥-1)^2]
	- LG = LG-WGAN
- J Adler, S Lunz. Banach Wasserstein GAN. NIPS'18
- DRAGAN: LD = LD-GAN + λE(|∇D(αx-(1-α)xp)|-1)^2
	- LG = LG-GAN
- CGAN: LD = E(log(D(x, c))) + E(log(1-D(G(z), c)))
	- LG = E(log(D(G(z), c)))
- ACGAN: LD = LD-GAN + E(P(class=c|x)) + E(P(class=c|G(z)))
	- LG = LG-GAN + E(P(class=c|G(z)))
- BEGAN: D Berthelot, T Schumm, L Metz. BEGAN: Boundary Equilibrium Generative Adversarial Networks. 2017
	- LD = DAE(x) - kt DAE(G(z))
	- LG = DAE(G(z))
	- kt+1 = kt + λ(γDae(x)-Dae(G(z))
- S Nowozin, B Cseke, and R Tomioka. f-GAN: Training generative neural samplers using variational divergence minimization. NeurIPS'16
	- Build on generalized f-divergence: ∫q(x) f(p(x)/q(x))dx
- DeepMind. The Cramer distance as a solution to biased Wasserstein gradients. arxiv'17
- OpenAI. Improving GANs using optimal transport. ICLR'18.
- The relativistic discriminator: a key element missing
from standard GAN. ICLR'19
	- When training Generator, the discriminator should also decrease prob of real image;

## Feature Learning
- J Donahue, P Krähenbühl, T Darrell. Adversarial Feature Learning. ICLR'17
	- Learn to discriminate:
		- Real: x, Enc(x)
		- Fake: G(z), z
- ALI: Adversarially Learned Inference.
	- Similar idea;
- Jianlin Su. O-GAN: Extremely Concise Approach for Auto-Encoding Generative Adversarial Networks. 2019
	- https://github.com/bojone/o-gan

## Single shot
- A Shocher, N Cohen, and M Irani. Zero-Shot Super-Resolution using Deep Internal Learning. CVPR'18
- A Shocher, S Bagon, P Isola, and M Irani. InGAN: Capturing and Remapping the "DNA" of a Natural Image. ICCV'19
- T Shaham, T Dekel, T Michaeli. SinGAN: Learning a Generative Model From a Single Natural Image. ICCV'19 Marr Prize
	- Multi-scale GAN: patch-based GAN;
	- A single scale: conditionaed on lower scale;

## Techniques
- OpenAI. Improved techniques for training gans. NeurIPS'16
	- https://github.com/openai/improved_gan
	- Feature matching: immediate layer of discriminator
	- Minibatch discrimination
	- History averaging
	- One-sided label smoothing: replace 0, 1 with .1, .9; smooth only on positive examples in discriminator;
	- Virtual batch normalization: each example x is normalized based on the statistics collected on a reference batch
- BigGAN: DeepMind. Large Scale GAN Training for High Fidelity Natural Image Synthesis, ICLR 2019
	- https://github.com/ajbrock/BigGAN-PyTorch.git
	- SA-GAN network structure (Zhang 2018)
	- G: class-conditional BatchNorm (Dumoulin 2017, de Vries 2017)
	- D: projection (Miyato 2018)
	- 2D + 1G: per iteration
	- Moving average (Karras 2018)
	- Orthogonal Initialization (Saxe 2014)
	- **Truncated Norm** to sample z from: big trick
- X Wei, Z Liu, L Wang, and B Gong. Improving the improved training of Wasserstein GANs. ICLR'18
	- Another regularization term;

## Analaysis
- Regard GAN training as ODE and apply ODE analysis;
- Stability:
	- K Roth, A Lucchi, S Nowozin, T Hofmann. Stabilizing Training of Generative Adversarial Networks through Regularization.
	- Nagarajan, V. and Z Kolter. Gradient descent GAN optimization is locally stable. 2017
	- L Mescheder, S Nowozin, A Geiger. The Numerics of GANs. NeurIPS'17
		- https://github.com/LMescheder/TheNumericsOfGANs
		- Insight: a game theory perspective, Simultaneous Gradient Ascent;
		- Consensus Optimization;
	- L Mescheder, A Geiger, and S Nowozin. Which training methods for GANs do actually converge? ICML'18
		- https://github.com/LMescheder/GAN_stability
		- Simplified gradient penalty;
- Metz, L., Poole, B., Pfau, D., and Sohl-Dickstein, J. Unrolled generative adversarial networks. 2016
- S Arora and Y Zhang. Do gans actually learn the distribution? an empirical study. 2017
- Arora, S., Ge, R., Liang, Y., Ma, T., and Zhang, Y. Generalization and equilibrium in generative adversarial nets (gans). 2017
- TTUR. GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium. 2017
	- Borrows idea from stochastic approximation with two time scales.
- M Arjovsky and L Bottou. Towards Principled Methods for Training Generative Adversarial Networks. 2017
- W Fedus, M Rosca, B Lakshminarayanan, A Dai, S Mohamed, and I Goodfellow. Many paths to equilibrium: GANs do not need to decrease a divergence at every step. ICLR'18
	- View: a divergence between the training distribution and the model distribution obtains its minimum value at equilibrium
	- This paper: too restrictive
	- Conclusion 1: Both gradient penalties (GAN-GP and DRAGAN-NS) help when training non-saturating GANs, by making the models more robust to hyperparameters.
	- The non-saturating GAN trained with gradient penalties produces better sample (IS)
	- WGAN-GP models perform best on Color MNIST and CIFAR-10.
- A Odena, J Buckman, C Olsson, T Brown, C Olah, C Raffel, and I Goodfellow. Is generator conditioning causally related to GAN performance? ICML'18.
	- Follow Pennington et al., 2017 to analyze Jacobian;
	- Jacobian generally becomes ill-conditioned at the beginning of training: a good cluster in which the condition number stays the same or even gradually decreases, and a "bad cluster", in which the condition number continues to grow
	- that the average (with z ∼ p(z)) conditioning of the generator is highly predictive of IS and FID;
	- Propose to use Jacobian loss:
- A Convex Duality Framework for GANs. NIPS'18
- Are GANs Created Equal? A Large-Scale Study. NIPS'18
- D Bau, J Zhu, J Wulff, W Peebles, H Strobelt, B Zhou, A Torralba. Seeing What a GAN Cannot Generate. ICCV'19
	- http://ganseeing.csail.mit.edu/
	- https://github.com/davidbau/ganseeing

## Applications with Adversarial Loss
- Photo editting;
	- A Brock, T Lim, J Ritchie, and N Weston. Neural photo editing with introspective adversarial networks. ICLR 2017.
- Super-resolution:
	- C. Ledig, L. Theis, F. Huszar, J. Caballero, A. Aitken, A. Tejani, J. Totz, Z. Wang, and W. Shi. Photo-realistic single image super-resolution using a generative adversarial network. CVPR'17.
	- C Sønderby, J Caballero, L Theis, W Shi, and F Huszár. Amortised map inference for image super-resolution. ICLR'17

## Misc
- Louppe, G. and Cranmer, K. Adversarial variational optimization of non-differentiable simulators. arXiv preprint arXiv:1707.07113, 2017.
