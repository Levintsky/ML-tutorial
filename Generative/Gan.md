# General Adversarial Net

## Evaluation
- Wu, Yuhuai, Burda, Yuri, Salakhutdinov, Ruslan, and Grosse, Roger. On the quantitative analysis of decoder- based generative models. 2017.
- Sanjeev Arora and Yi Zhang. Do gans actually learn the distribution? an empirical study. 2017
- Evaluation: GenEval: A benchmark suite for evaluating generative models, in submission to ICLR 2019

## GAN
*Name* | *Paper Link* | *Value Function*
:---: | :---: | :--- |
**GAN** | [Arxiv](https://arxiv.org/abs/1406.2661) | <img src = '/Generative/images/equations/GAN.png' height = '70px'>
**LSGAN**| [Arxiv](https://arxiv.org/abs/1611.04076) | <img src = '/Generative/images/equations/LSGAN.png' height = '70px'>
**WGAN**| [Arxiv](https://arxiv.org/abs/1701.07875) | <img src = '/Generative/images/equations/WGAN.png' height = '105px'>
**WGAN_GP**| [Arxiv](https://arxiv.org/abs/1704.00028) | <img src = '/Generative/images/equations/WGAN_GP.png' height = '70px'>
**DRAGAN**| [Arxiv](https://arxiv.org/abs/1705.07215) | <img src = '/Generative/images/equations/DRAGAN.png' height = '70px'>
**CGAN**| [Arxiv](https://arxiv.org/abs/1411.1784) | <img src = '/Generative/images/equations/CGAN.png' height = '70px'>
**infoGAN**| [Arxiv](https://arxiv.org/abs/1606.03657) | <img src = '/Generative/images/equations/infoGAN.png' height = '70px'>
**ACGAN**| [Arxiv](https://arxiv.org/abs/1610.09585) | <img src = '/Generative/images/equations/ACGAN.png' height = '70px'>
**EBGAN**| [Arxiv](https://arxiv.org/abs/1609.03126) | <img src = '/Generative/images/equations/EBGAN.png' height = '70px'>
**BEGAN**| [Arxiv](https://arxiv.org/abs/1703.10717) | <img src = '/Generative/images/equations/BEGAN.png' height = '105px'>

<img src = '/Generative/images/etc/GAN_structure.png' height = '600px'>

## GAN
- Google Brain, Magenta:
	- **GAN**: I Goodfellow, J Pouget-Abadie, M Mirza, B Xu, D Warde-Farley, S Ozair, A Courville, and Y Bengio. Generative adversarial nets. In NIPS, 2014.
	- W Fedus, M Rosca, B Lakshminarayanan, A Dai, S Mohamed, and I Goodfellow. Many paths to equilibrium: GANs do not need to decrease a divergence at every step. In ICLR, 2018.
	- A Odena, C Olah, and J Shlens. Conditional image synthesis with auxiliary classifier GANs. In ICML, 2017.
	- BEGAN: Boundary Equilibrium Generative Adversarial Networks
	- Augustus Odena, Jacob Buckman, Catherine Olsson, Tom B. Brown, Christopher Olah, Colin Raffel, and Ian Goodfellow. Is generator conditioning causally related to GAN performance? ICML 2018.
	- **WGAN-GP**: Gulrajani, I., Ahmed, F., Arjovsky, M., Dumoulin, V., and Courville, A. C. Improved training of Wasserstein gans. NIPS 2017.
		- Very good explanation: https://vincentherrmann.github.io/blog/wasserstein/
		- Alex Irpan's blog: https://www.alexirpan.com/2017/02/22/wasserstein-gan.html
		- W-GAN is Earth-Mover-Distance
		- Kantorovich-Rubinstein duality
		- sup[E_pr(f(x))-E_pg(f(x))]/K, where f() is K-Lipschitz (f's gradient < K)
		- D-step: loss(D)=D(fake, 1) - D(real,-1) + gradient-penalty
		- G-step: loss(G)=D(G(fake), -1)
	- **SA-GAN**: H Zhang, I Goodfellow, D Metaxas, and A Odena. Self-attention generative adversarial networks. ICML'19
		- https://github.com/heykeetae/Self-Attention-GAN
		- Generator
		- Inception score: 36.8 -> 52.52
		- Frechet Inception distance: 27.62 -> 18.65
```python
def forward(self, z):
    z = z.view(z.size(0), z.size(1), 1, 1) # (?, 100, 1, 1)
    # deconv + spectral-norm + ReLU
    out = self.l1(z) # (?, 512, 4, 4)
    out = self.l2(out) # (?, 256, 8, 8)
    out = self.l3(out) # (?, 128, 16, 16)
    out, p1 = self.attn1(out) # (?, 128, 16, 16)
    out = self.l4(out) # (?, 64, 32, 32)
    out, p2 = self.attn2(out) # (?, 64, 32, 32)
    out = self.last(out) # (?, 3, 64, 64)

    return out, p1, p2
```
		- Discriminator:
```python
def forward(self, x):
    out = self.l1(x)
    out = self.l2(out)
    out = self.l3(out)
    out,p1 = self.attn1(out)
    out=self.l4(out)
    out,p2 = self.attn2(out)
    out=self.last(out)

    return out.squeeze(), p1, p2
```
		- two-timescale update rule (TTUR)
- FAIR:
	- E Denton, S Chintala, A Szlam, and R Fergus. Deep generative image models using a laplacian pyramid of adversarial networks. NIPS 2015.
	- **DC-GAN**: A Radford, L Metz, and S Chintala. Unsupervised representation learning with deep convolutional generative adversarial networks. In ICLR, 2016.
	- J Zhao, M Mathieu, Y LeCun. Energy-based Generative Adversarial Network. 2016
	- Y. Taigman, A. Polyak, and L. Wolf. Unsupervised cross-domain image generation. In ICLR, 2017.
- OpenAI:
	- T Salimans, I Goodfellow, W Zaremba, V Cheung, A Radford, and X Chen. Improved techniques for training gans. NIPS 2016
		- **Perception Score** as evaluation
	- X Chen, Y Duan, R Houthooft, J Schulman, I Sutskever, and P Abbeel. **Infogan**: Interpretable representation learning by information maximizing generative adversarial nets. NIPS 2016
	<img src = '/Generative/images/info-gan1.png' height = '60px'>
	<img src = '/Generative/images/info-gan2.png' height = '200px'>

		- A Q(c|x) to encode x to attributes c, Q shared base-conv with D
		- System Design: 4 modules: G, Shared Bottom CNN, D, Q
		- Discriminator: log(D(x)) + log(1-D(G(z))), D-only
			- Real-x: CrossEntropy(D(FE(x)), 1)
			- Fake part:
				- Sample z, discrete-c, continuous-c
				- Generate images: fake-x = G(z,c), detach fake-x
				- CrossEntropy(D(FE(x)), 0)
		- Generator: log(D(G(z))) + I(c, Q(c|x)), G and Q
			- CrossEntropy(D(G(z)), 1) for G
			- CrossEntropy(FE(x), idx) or entropy?
	- Tim Salimans, Han Zhang, Alec Radford, and Dimitris Metaxas. Improving GANs using optimal transport. In ICLR, 2018.
- DeepMind:
	- **BigGAN**: Andrew Brock, Jeff Donahue, Karen Simonyan. **Large Scale GAN Training for High Fidelity Natural Image Synthesis**, ICLR 2019
		- https://github.com/ajbrock/BigGAN-PyTorch.git
		- SA-GAN network structure (Zhang 2018)
		- G: class-conditional BatchNorm (Dumoulin 2017, de Vries 2017)
		- D: projection (Miyato 2018)
		- 2D + 1G: per iteration
		- Moving average (Karras 2018)
		- Orthogonal Initialization (Saxe 2014)
		- **Truncated Norm** to sample z from: big trick
		- IS: precision; FID: recall
	- Andrew Brock, Theodore Lim, J.M. Ritchie, and Nick Weston. Neural photo editing with introspective adversarial networks. ICLR 2017.
	- Marc G. Bellemare, Ivo Danihelka, Will Dabney, Shakir Mohamed, Balaji Lakshminarayanan, Stephan Hoyer, and Remi Munos. The Cramer distance as a solution to biased Wasserstein gradients. In arXiv preprint arXiv:1705.10743, 2017.
- **NVIDIA**:
	- **Progressive**: Tero Karras, Timo Aila, Samuli Laine, and Jaakko Lehtinen. Progressive growing of GANs for improved quality, stability, and variation. ICLR 2018.
- Conditional-GAN:
	- **CGAN**: Mirza, M. and Osindero, S. Conditional generative adversarial nets. arXiv preprint arXiv:1411.1784, 2014.
	- Takeru Miyato and Masanori Koyama. cGANs with projection discriminator. In ICLR, 2018.
- **SeqGAN**: Yu, L., Zhang, W., Wang, J., and Yu, Y. SeqGAN: Sequence generative adversarial nets with policy gradient. In AAAI, 2017.
- **SN-GAN**: Spectral Normalization for Generative Adversarial Networks, ICLR 2018
- Wei, X., Liu, Z., Wang, L., and Gong, B. Improving the improved training of Wasserstein GANs. ICLR'18
- **BAIR**:
	- **Cycle-GAN**: Zhu, J.-Y., Park, T., Isola, P., and Efros, A. A. Unpaired image-to-image translation using cycle-consistent adversarial networks. CVPR 2017
		- https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
		- G: X -> Y; discriminator: D_Y;
		- F: Y -> X; discriminator: D_X;
		- Adversarial loss: E[logD_Y(y)] + E[log(1-D_Y(G(x)))]
		- Similar loss for D_X
		- Consistency loss: ||F(G(x))-x|| + ||G(F(y))-y|| with L1 norm
	- **pix2pix**: Isola, P., Zhu, J.-Y., Zhou, T., and Efros, A. A. Image-to-image translation with conditional adversarial networks. CVPR, 2017.
- Attention:
	- **Attngan**: T. Xu, P. Zhang, Q. Huang, H. Zhang, Z. Gan, X. Huang, and X. He. Attngan: Fine-grained text
to image generation with attentional generative adversarial networks. In CVPR, 2018.
- Feature Learning:
	- Donahue, J., Krahenbuhl, P., and Darrell, T. Adversarial feature learning.
- Inference:
	- Dumoulin, V., Belghazi, I., Poole, B., Lamb, A., Arjovsky, M., Mastropietro, O., and Courville, A. Adversarially learned inference.
- Domain adaptation:
	- Ganin, Y. and Lempitsky, V. Unsupervised domain adaptation by backpropagation. ICML 2015
- Others:
	- **LSGAN**: X Mao, Q Li, H Xie, R Y.K. Lau, Z Wang, and S. Paul Smolley. Least Squares Generative Adversarial Networks. 2017
	- **DRAGAN**: N Kodali, J Abernethy, J Hays, Z Kira. On Convergence and Stability of GANs
	- M. Liu and O. Tuzel. Coupled generative adversarial networks. In NIPS, 2016
- Super-resolution:
	- C. Ledig, L. Theis, F. Huszar, J. Caballero, A. Aitken, A. Tejani, J. Totz, Z. Wang, and W. Shi. Photo-realistic single image super-resolution using a generative adversarial network. In CVPR, 2017.
	- C. K. Sønderby, J. Caballero, L. Theis, W. Shi, and F. Huszár. Amortised map inference for image super-resolution. In ICLR, 2017.
- GAN + AE (Reconstruction ability):
	- **PixelGAN**: Alireza Makhzani, Brendan Frey. PixelGAN Autoencoders. 2017
		- q(z|x) and p(z) adversarial loss (encoded latent)
		- Reconstruction loss
<img src = '/Generative/images/pixel-gan.png' height = '100px'>

## Evaluation
- Lucas Theis, Aaron van den Oord, and Matthias Bethge. A note on the evaluation of generative models. In arXiv preprint arXiv:1511.01844, 2015.
- **Perception Score (IS)**: Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen. Improved
techniques for training gans. NIPS 2016
-  **Frechet Inception Distance (FID)**: Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Gunter Klambauer, and Sepp Hochreiter. GANs trained by a two time-scale update rule converge to a local nash equilibrium. NIPS 2017

## Variational
- Sebastian Nowozin, Botond Cseke, and Ryota Tomioka. **f-GAN**: Training generative neural samplers using variational divergence minimization. NIPS 2016

## Analysis
- Lars Mescheder, Andreas Geiger, and Sebastian Nowozin. Which training methods for GANs do actually converge? In ICML, 2018.

## RL, Imitation Learning
- Merel, J., Tassa, Y., Srinivasan, S., Lemmon, J., Wang, Z., Wayne, G., and Heess, N. Learning human behaviors from motion capture by adversarial imitation. arXiv preprint arXiv:1707.02201, 2017.

## Misc
- Eslami, S. A., Heess, N., Weber, T., Tassa, Y., Szepesvari, D., Kavukcuoglu, K., and Hinton, G. E. Attend, infer, repeat: Fast scene understanding with generative models. In NIPS, 2016.
- Loper, M. M. and Black, M. J. Opendr: An approximate differentiable renderer. In ECCV, 2014.
- Louppe, G. and Cranmer, K. Adversarial variational optimization
of non-differentiable simulators. arXiv preprint arXiv:1707.07113, 2017.

## Codes
- StarGAN: https://github.com/yunjey/StarGAN
- Deepak: Unsupervised Feature Learning by Image Inpainting using GANs, CVPR 2016, https://github.com/pathak22/context-encoder