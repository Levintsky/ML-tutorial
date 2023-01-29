# Point Cloud

## Basics
- Directly map from latent space z to nx3 dim as n points; (most AE)
- Fold a 2D surface/rectangle (folding net)
- Deform a Gaussian ball (CNF, pointflow)

## Upsampling
- Wang Yifan, Shihao Wu, Hui Huang, Daniel Cohen-Or, and Olga Sorkine-Hornung. Patch-based progressive 3d point set upsampling. arXiv preprint arXiv:1811.11286, 2018
- Lequan Yu, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. Ec-net: an edge-aware point set consolidation network. ECCV'18
- Lequan Yu, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. Pu-net: Point cloud upsampling network. CVPR'18

## Backbones (Decoder)
Framework:
	- Flow/CNF: Pointflow, SoftFlow, DiscreteFlow,
	- AR: SoftFlow, PointGrow,
	- Diffusion: LION
- MLP:
	- **PSGN**: H Fan, H Su, and L Guibas. CVPR'17
	- AE: P Achlioptas, O Diamanti, I Mitliagkas, and L Guibas. Learning representations and generative models for 3d point clouds. ICML'18
	- **FoldingNet**: Y. Yang, C. Feng, Y. Shen, and D. Tian. CVPR'18
		- Encoder: GNN; Decoder: MLP;
	- **Pointflow**: Guandao Yang, et. al. ICCV'19
		- Reconstuction: P(x|z; θ), CNF;
		- Prior (flow-based): P(z; ψ)
		- Encoder: x -> Qφ -> μ, σ
	- R Klokov, E Boyer, J Verbeek. Discrete Point Flow Networks for Efficient Point Cloud Generation. ECCV'20
	- Y Sun, Y Wang, Z Liu, J Siegel, S E Sarma. PointGrow: Autoregressively Learned Point Cloud Generation with Self-Attention. WACV'20
- CNN:
	- H Kim, H Lee, W Kang, J Lee, N Kim. SoftFlow: Probabilistic Framework for Normalizing Flow on Manifolds. NeurIPS'20
		- Formulation similar as PointFlow;
		- Glow AR instead of continuous ODE;
- GNN:
	- Learning localized generative models for 3d point clouds via graph convolution [D Valsesia ICLR'19];
	- Or Litany, et. al. Deformable Shape Completion with Graph Convolutional Autoencoders. CVPR'18
	- Dong Wook Shu, et. al. 3d point cloud generative adversarial network based on tree structured graph convolutions. ICCV'19
- Hierarchical:
	- Matheus Gadelha, et. al. Multiresolution tree networks for 3d point cloud processing. ECCV'18
- Diffusion:
	- Shitong Luo, Wei Hu. Diffusion Probabilistic Models for 3D Point Cloud Generation. CVPR'21

## Supervision
- Pointwise:
	- Chamfer Distance or EMD/Wasserstein:
- Whole (GAN/Adversarial): [D Valsesia ICLR'19]; [Dong Wook Shu ICCV'19]
- VAE: [Or Litany; CVPR'18]
	- PointFlow [ICCV'19]
		- KL: KL(Qφ(z|x)||Pψ(z))
		- Reconstruction: log Pθ(x|z)
- Chun-Liang Li, Manzil Zaheer, Yang Zhang, Barnabas Poczos, and Ruslan Salakhutdinov. Point cloud gan. ICLR'19
	- Theoretical paper: derive WGAN-style divergence for point set;
	- Experiment: built on AE

## Misc
- Nobuyuki Umetani. Exploring Generative 3D Shapes Using Autoencoder Networks. SIGGRAPH Asia'17
	- AutoEncoder on 3D points and hand-coded features;
- **AAE**: Maciej Zamorski, Maciej Zieba, Rafał Nowak, Wojciech Stokowiec, and Tomasz Trzciński. Adversarial autoencoders for generating 3d point clouds. 2018
	- Build on Alireza Makhzani, Jonathon Shlens, Navdeep Jaitly, Ian Goodfellow, and Brendan Frey. Adversarial autoencoders. 2015
- Chen-Hsuan Lin, Chen Kong, and Simon Lucey. Learning efficient point cloud generation for dense 3d object reconstruction. AAAI'18
- Ruihui Li, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. PU-GAN: A point cloud upsampling adversarial network. ICCV'19
