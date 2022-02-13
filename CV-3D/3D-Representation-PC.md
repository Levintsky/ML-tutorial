# Point Cloud

## Basics:
- Directly map from latent space z to nx3 dim as n points; (most AE)
- Fold a 2D surface/rectangle (folding net)
- Deform a Gaussian ball (CNF, pointflow)

## Misc
- **PSGN**: H Fan, H Su, and L Guibas. A point set generation network for 3d object reconstruction from a single image. CVPR'17
	- Key insight: hourglass better; random variable;
	- https://github.com/fanhqme/PointSetGeneration
	- Input: image, random variable r; output: point cloud;
	- Net-structure: encoder, predictor;
	- Supervision: 1. Chamfer distance; 2. EMD with approximation;
	<img src="/CV-3D/images/3d_output/point-set-gen.png" alt="drawing" width="600"/>
- Nobuyuki Umetani. Exploring Generative 3D Shapes Using Autoencoder Networks. SIGGRAPH Asia'17
	- AutoEncoder on 3D points and hand-coded features;
- **AAE**: Maciej Zamorski, Maciej Zieba, Rafał Nowak, Wojciech Stokowiec, and Tomasz Trzciński. Adversarial autoencoders for generating 3d point clouds. 2018
	- Build on Alireza Makhzani, Jonathon Shlens, Navdeep Jaitly, Ian Goodfellow, and Brendan Frey. Adversarial autoencoders. 2015
- Chen-Hsuan Lin, Chen Kong, and Simon Lucey. Learning efficient point cloud generation for dense 3d object reconstruction. AAAI'18
- Panos Achlioptas, Olga Diamanti, Ioannis Mitliagkas, and Leonidas Guibas. Learning representations and generative models for 3d point clouds. ICML'18
	- Input/output: point cloud;
	- AE, x -> z=f(x) -> x'
	- Supervision: Chamfer(x, x')
- **FoldingNet**: Y. Yang, C. Feng, Y. Shen, and D. Tian. Foldingnet: Interpretable unsupervised learning on 3d point clouds. CVPR'18
	- https://www.merl.com/research/license#FoldingNet
	- AE
	- Encoder: MLP + graph-based matrix pooling; output a 512 x 1 dim feature;
		- Graph: K-NN graph, 3 (xyz) + 9 (covariance) = 12-dimension; (local pooling like PointNet++)
	- Decoder: takes 512-dim feature and fixed 2D grid, fold; m x 514-dim input; 512d + xy;
		- MLP;
- Matheus Gadelha, Rui Wang, and Subhransu Maji. Multiresolution tree networks for 3d point cloud processing. ECCV'18
	- VAE
- Chun-Liang Li, Manzil Zaheer, Yang Zhang, Barnabas Poczos, and Ruslan Salakhutdinov. Point cloud gan. ICLR'19
	- Theoretical paper: derive WGAN-style divergence for point set;
	- Experiment: built on AE
- Diego Valsesia, Giulia Fracastoro, and Enrico Magli. Learning localized generative models for 3d point clouds via graph convolution. ICLR'19
- Ruihui Li, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. PU-GAN: A point cloud upsampling adversarial network. ICCV'19
- **CNF**:
	- **Pointflow**: Guandao Yang, Xun Huang, Zekun Hao, Ming-Yu Liu, Serge Belongie, and Bharath Hariharan. Pointflow: 3d point cloud generation with continuous normalizing flows. ICCV'19
		- CNF based model;
	- Shitong Luo, Wei Hu. Diffusion Probabilistic Models for 3D Point Cloud Generation. CVPR'21
		- https://github.com/luost26/diffusion-point-cloud
		- MCMC
- Dong Wook Shu, Sung Woo Park, and Junseok Kwon. 3d point cloud generative adversarial network based on tree structured graph convolutions. ICCV'19
