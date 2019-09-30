# 3D Generative, Reconstruction and Synthesis

## 2D with 3D Input
- Alexey Dosovitskiy, Jost Tobias Springenberg, Maxim Tatarchenko, Thomas Brox. Learning to Generate Chairs, Tables and Cars with Convolutional Networks. PAMI 2017
- Multi-view 3D Models from Single Images with
a Convolutional Network. ECCV 2016
	- Encoder/Decoder
	- Input RGB, output RGB/D conditioned on any shape input (angle, ...)
	- https://github.com/lmb-freiburg/mv3d

## Recurrent
- J Yang. Weakly-supervised Disentangling with Recurrent Transformations for 3D View Synthesis. NIPS 2015
	- Input/output: images
	- https://github.com/jimeiyang/deepRotator
- Christopher B. Choy Danfei Xu? JunYoung Gwak?
Kevin Chen Silvio Savarese. 3D-R2N2: A Unified Approach for Single and Multi-view 3D Object Reconstruction. ECCV 2016
	- Update model with RNN each time with a new image;
	- https://github.com/chrischoy/3D-R2N2

## Template-Based
- Legacy:
	- A.-L. Chauve, P. Labatut, and J.-P. Pons. Robust piecewiseplanar 3d reconstruction and completion from large-scale unstructured point data. CVPR 2010
	- F. Lafarge and P. Alliez. Surface reconstruction through point set structuring. Computer Graphics Forum 2013
	- S. N. Sinha, D. Steedly, R. Szeliski, M. Agrawala, and M. Pollefeys. Interactive 3d architectural modeling from unordered photo collections. TOG 2008
	- A. Bodis-Szomoru, H. Riemenschneider, and L. Van Gool. Fast, approximate piecewise-planar modeling based on sparse structure-from-motion and superpixels. CVPR 2014
- Haibin Huang, Evangelos Kalogerakis, Benjamin Marlin. Analysis and synthesis of 3D shape families via deep-learned generative models of surfaces. Eurographics 2015
- **Voxlet**: Michael Firman, Oisin Mac Aodha, Simon Julier, Gabriel J. Brostow. Structured Prediction of Unobserved Voxels From a Single Depth Image. CVPR 2016
	- Shape prior
	- https://github.com/mdfirman/voxlets
- Jiajun Wu. 3D-INN. ECCV 2016
- - **Hao Su Summary**: http://cseweb.ucsd.edu/~haosu/slides/PartInduction.pdf
- S. Tulsiani, H. Su, L. J. Guibas, A. A. Efros, and J. Malik. Learning shape abstractions by assembling volumetric primitives. CVPR 2017
	- Input: voxel; output: mesh parts (triangles);
	- Unsupervised?
	- Each part (z, q, t): z, shape; q rotation; t translation;
	- Loss design:
		- Coverage loss: distance of primitives; penalize to confirm O in Pm
		- Consistency loss:
	- Variable number of primitives: (z, q, t, p), p binary for existence
	- REINFORCE; parsimony reward for fewer parts
	- Experiment: ShapeNet, 32x32x32, ADAM;
- M. Sung, H. Su, R. Yu, and L. Guibas. Deep functional dictionaries: Learning consistent semantic structures on 3D models from functions. NIPS 2018
	- Input n points; output:  n x k dictionary;
	- Structured sparsity;
	- https://github.com/mhsung/deep-functional-dictionaries
	- Different deep dictionaries;
	- Applications with adaptation in co-segmentation, keypoint correspondence, smooth functional approximation (modeled as constraint);
	- Given an input X, At = A(X; theta) to get basis
	- Solve x = argmin||At x - f||^2 s.t. C(x)
	- Update theta = theta - eta * d L(A(X, theta); f, x) / dx
- **GRASS**. Jun Li, Kai Xu, Siddhartha Chaudhuri, Ersin Yumer, Hao Zhang, Leonidas Guibas. GRASS: Generative Recursive Autoencoders for Shape Structures. SIGGRAPH 2017
	- Recursive
- Im2Struct: Recovering 3D Shape Structure from a Single RGB Image (2018 CVPR)
- Li Yi, Haibin Huang, Difan Liu, Evangelos Kalogerakis, Hao Su, Leonidas Guibas. Deep Part Induction from Articulated Object Pairs. SIGGRAPH Asia 2018
	- Deep Matching (Point Net)
	- Motion Discovery, Part Co-segmentation

## Reconstruction
- Warping, Flow:
	- Tinghui Zhou, Shubham Tulsiani, Weilun Sun, Jitendra Malik, Alexei A. Efros. View Synthesis by Appearance Flow. ECCV 2016
		- https://github.com/tinghuiz/appearance-flow
- Rohit Girdhar, David F. Fouhey, Mikel Rodriguez, Abhinav Gupta. Learning a Predictable and Generative Vector Representation for Objects. ECCV 2016

## GAN
- Jimei:
	- Perspective Transformer Nets: Learning Single-View 3D Object Reconstruction without 3D Supervision. NIPS 2016
		- https://github.com/xcyan/ptnbhwd
- MIT Series:
	- **3D-GAN**: Jiajun Wu, Learning a probabilistic latent space of object shapes via 3d generative-adversarial modeling, NIPS 2016
		- GAN / GAN-VAE;
		- Noisy / Blurry;
- **PrGAN**: Matheus Gadelha, Subhransu Maji and Rui Wang. 3D Shape Induction from 2D Views of Multiple Objects. 3DV 2017
	- https://github.com/matheusgadelha/PrGAN

## Generation
- Haibin Huang, Evangelos Kalogerakis, and Benjamin Marlin. Analysis and synthesis of 3d shape families via
deep-learned generative models of surfaces. CGF, 34(5):25–38, 2015.
- Interactive 3D modeling with a generative adversarial network, 3D Vision 2017
- Amir Arsalan Soltani, Haibin Huang, Jiajun Wu, Tejas D. Kulkarni, Joshua B. Tenenbaum. Synthesizing 3D Shapes via Modeling Multi-View Depth Maps and Silhouettes with Deep Generative Networks. CVPR 2017
	- https://github.com/Amir-Arsalan/Synthesize3DviaDepthOrSil

## 2.5-D, Intrinsic Images
- H. G. Barrow and J. M. Tenenbaum, Recovering intrinsic scene characteristics from images, Computer Vision Systems, 1978

## 3D-Reconstruction, Render
- W. Jakob, “Mitsuba renderer,” 2010, http://www.mitsuba-renderer.org.
- Hao Su, Charles R Qi, Yangyan Li, and Leonidas Guibas. Render for cnn: Viewpoint estimation in images using cnns trained with rendered 3d model views. ICCV'15

## Shape Editing
- A. Jain, T. Thormahlen, T. Ritschel, and H.-P. Seidel. Exploring shape variations by 3d-model decomposition and partbased recombination. CGF 2012