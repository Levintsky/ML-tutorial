# 3D Generative and Synthesis

## 3D-Aware 2D Generation
- M Tatarchenko, A Dosovitskiy, T Brox. Multi-view 3D Models from Single Images with a Convolutional Network. ECCV'16
	- Encoder/Decoder
	- Input RGB, output RGB/D conditioned on any shape input (angle, ...)
	- https://github.com/lmb-freiburg/mv3d
- A Dosovitskiy, J Springenberg, M Tatarchenko, T Brox. Learning to Generate Chairs, Tables and Cars with Convolutional Networks. PAMI'17
	- Input: class c, view v, transfrom param theta;
	- Output: image;
	- Conv, deconv, upsampling;

## Template-Based
- Legacy:
	- A.-L. Chauve, P. Labatut, and J.-P. Pons. Robust piecewise planar 3d reconstruction and completion from large-scale unstructured point data. CVPR 2010
	- F. Lafarge and P. Alliez. Surface reconstruction through point set structuring. Computer Graphics Forum 2013
	- S. N. Sinha, D. Steedly, R. Szeliski, M. Agrawala, and M. Pollefeys. Interactive 3d architectural modeling from unordered photo collections. TOG 2008
	- A. Bodis-Szomoru, H. Riemenschneider, and L. Van Gool. Fast, approximate piecewise-planar modeling based on sparse structure-from-motion and superpixels. CVPR 2014
- Haibin Huang, Evangelos Kalogerakis, Benjamin Marlin. Analysis and synthesis of 3D shape families via deep-learned generative models of surfaces. Eurographics 2015
- **Voxlet**: Michael Firman, Oisin Mac Aodha, Simon Julier, Gabriel J. Brostow. Structured Prediction of Unobserved Voxels From a Single Depth Image. CVPR 2016
	- Shape prior
	- https://github.com/mdfirman/voxlets
- Im2Struct: Recovering 3D Shape Structure from a Single RGB Image (2018 CVPR)
- Li Yi, Haibin Huang, Difan Liu, Evangelos Kalogerakis, Hao Su, Leonidas Guibas. Deep Part Induction from Articulated Object Pairs. SIGGRAPH Asia 2018
	- Deep Matching (Point Net)
	- Motion Discovery, Part Co-segmentation

## Reconstruction
- Rohit Girdhar, David F. Fouhey, Mikel Rodriguez, Abhinav Gupta. Learning a Predictable and Generative Vector Representation for Objects. ECCV 2016

## GAN		
- MIT Series:
	- **3D-GAN**: Jiajun Wu, Learning a probabilistic latent space of object shapes via 3d generative-adversarial modeling, NIPS 2016
		- GAN / GAN-VAE;
		- Noisy / Blurry;
- **PrGAN**: Matheus Gadelha, Subhransu Maji and Rui Wang. 3D Shape Induction from 2D Views of Multiple Objects. 3DV 2017
	- https://github.com/matheusgadelha/PrGAN
- Chun-Liang Li, Manzil Zaheer, Yang Zhang, Barnabas Poczos, and Ruslan Salakhutdinov. Point cloud gan. ICLR'19

## AE, VAE
- AE:
	- Q Tan, L Gao, Y Lai, J Yang and S Xia. Mesh-based Autoencoders for Localized Deformation Component Analysis. 2017
		- Input: multiple mesh; output: new mesh synthesis (deformation);
	- Panos Achlioptas, Olga Diamanti, Ioannis Mitliagkas, and Leonidas Guibas. Learning representations and generative models for 3d point clouds. ICML'18
	- Exploring Generative 3D Shapes Using Autoencoder Networks. SIGGRAPH Asia
- VAE
	- A Brock, T Lim, J Ritchie, N Weston. Generative and Discriminative Voxel Modeling with Convolutional Neural Networks. NIPSW'16
		- https://github.com/ajbrock/Generative-and-Discriminative-Voxel-Modeling
	- Matheus Gadelha, Rui Wang, and Subhransu Maji. Multiresolution tree networks for 3d point cloud processing. ECCV'18
	- **AAE**: Maciej Zamorski, Maciej Zieba, Rafał Nowak, Wojciech Stokowiec, and Tomasz Trzciński. Adversarial autoen-coders for generating 3d point clouds.
		- Build on Alireza Makhzani, Jonathon Shlens, Navdeep Jaitly, Ian Goodfellow, and Brendan Frey. Adversarial autoencoders. 2015

## Conditional
- Text to 3D:
	- A. X. Chang, M. Savva, and C. D. Manning. Learning spatial knowledge for text to 3d scene generation. EMNLP'14
	- A. Chang, W. Monroe, M. Savva, C. Potts, and C. D. Manning. Text to 3d scene generation with rich lexical grounding. ACL'15

## Generation
- Haibin Huang, Evangelos Kalogerakis, and Benjamin Marlin. Analysis and synthesis of 3d shape families via deep-learned generative models of surfaces. CGF, 34(5):25–38, 2015.
- Interactive 3D modeling with a generative adversarial network, 3D Vision 2017
- Amir Arsalan Soltani, Haibin Huang, Jiajun Wu, Tejas D. Kulkarni, Joshua B. Tenenbaum. Synthesizing 3D Shapes via Modeling Multi-View Depth Maps and Silhouettes with Deep Generative Networks. CVPR 2017
	- https://github.com/Amir-Arsalan/Synthesize3DviaDepthOrSil

## Completion
- A. Dai, C. R. Qi, and M. Nießner. Shape completion using 3D-encoder-predictor CNNs and shape synthesis. CVPR'17
- L. Ladicky, O. Saurer, S. Jeong, F. Maninchedda, and M. Pollefeys. From point clouds to mesh using regression. ICCV'17
- G. Riegler, A. O. Ulusoy, H. Bischof, and A. Geiger. OctNetFusion: Learning depth fusion from data. 3DV'17

## 3D-Reconstruction, Render
- W. Jakob, Mitsuba renderer, 2010, http://www.mitsuba-renderer.org.

## Shape Editing
- A. Jain, T. Thormahlen, T. Ritschel, and H.-P. Seidel. Exploring shape variations by 3d-model decomposition and partbased recombination. CGF 2012

## PC Upsampling
- Wang Yifan, Shihao Wu, Hui Huang, Daniel Cohen-Or, and Olga Sorkine-Hornung. Patch-based progressive 3d point set upsampling. arXiv preprint arXiv:1811.11286, 2018
- Lequan Yu, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. Ec-net: an edge-aware point set consolidation network. ECCV'18
- Lequan Yu, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. Pu-net: Point cloud upsampling network. CVPR'18