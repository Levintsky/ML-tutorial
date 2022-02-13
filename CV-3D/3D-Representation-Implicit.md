# Implicit Functions (N-SDF)

## Legacy:
	- B. Curless and M. Levoy. A volumetric method for building complex models from range images. SIGGRAPH'96
	- **RBF**: Jonathan C. Carr, Richard K. Beatson, Jon B. Cherrie, Tim J. Mitchell, W. Richard Fright, Bruce C. McCallum, and Tim R. Evans. Reconstruction and representation of 3d objects with radial basis functions. SIGGRAPH'01
	- Greg Turk and James F. O'Brien. Modelling with implicit surfaces that interpolate. TOG'02
	- **Unity implicits**: Yutaka Ohtake, Alexander Belyaev, Marc Alexa, Greg Turk, and Hans-Peter Seidel. Multi-level partition of unity implicits, volume 22. ACM, 2003
	- Chen Shen, James F. O'Brien, and Jonathan Richard Shewchuk. Interpolating and approximating implicit surfaces from polygon soup. TOG'04

## Render for implicit models:
	- Marching Cube;
	- John C. Hart. Sphere tracing: A geometric method for the antialiased ray tracing of implicit surfaces. 1996
	- **Surface-Finding**: Sarah F. Frisken, Ronald N. Perry, Alyn P. Rockwood, and Thouis R. Jones. Adaptively sampled distance fields: A general representation of shape for computer graphics. 2000

## Generalized Neural-SDF or indicator function:
- Songyou Peng, Michael Niemeyer, Lars Mescheder, Marc Pollefeys, and Andreas Geiger. Convolutional occupancy networks. ECCV, 2020.
- Matan Atzmon, Niv Haim, Lior Yariv, Ofer Israelov, Haggai Maron, and Yaron Lipman. Controlling neural level sets. NeurIPS'19
- Union of piecewise SDF/indicator (parts?):
	- Boyang Deng, Kyle Genova, Soroosh Yazdani, Sofien Bouaziz, Geoffrey Hinton, Andrea Tagliasacchi. CvxNet: Learnable Convex Decomposition. CVPR'20
		- https://cvxnet.github.io/
		- https://github.com/tensorflow/graphics/tree/master/tensorflow_graphics/projects/cvxnet
- Local/global:
	- **DISN**: Qiangeng Xu, Weiyue Wang, Duygu Ceylan, Radomir Mech, and Ulrich Neumann. Disn: Deep implicit surface network for high-quality single-view 3d reconstruction. NeurIPS'19
		- https://github.com/laughtervv/DISN
	- Chiyu Max Jiang, Avneesh Sud, Ameesh Makadia, Jingwei Huang, Matthias Nießner, and Thomas A. Funkhouser. Local implicit grid representations for 3d scenes. 2020
	- Rohan Chabra, Jan Eric Lenssen, Eddy Ilg, Tanner Schmidt, Julian Straub, Steven Lovegrove, and Richard Newcombe. Deep local shapes: Learning local SDF priors for detailed 3d reconstruction. CoRR'20
	- PatchNets: Edgar Tretschk, Ayush Tewari, Vladislav Golyanik, Michael Zollhöfer, Carsten Stoll, and Christian Theobalt. PatchNets: Patch-Based Generalizable Deep Implicit 3D Shape Representations. ECCV'20
		- https://github.com/edgar-tr/patchnets
	- Moritz Ibing, Isaak Lim, Leif Kobbelt. 3D Shape Generation With Grid-Based Implicit Functions. CVPR'21
- **OccNet**: Lars Mescheder, Michael Oechsle, Michael Niemeyer, Sebastian Nowozin, and Andreas Geiger. Occupancy networks: Learning 3d reconstruction in function space. CVPR'19
	- Insight: new 3D representation, could generate mesh at any resolution;
	- https://github.com/autonomousvision/occupancy_networks
	- Input image; output: **continuous decision boundary of a deep-NN**;
	- Learn an occupancy function: R3 to [0,1];
	- Surface at inference time: Multiresolution IsoSurface Extraction (MISE) or Marching Cube;
- **IM-Net**: Zhiqin Chen and Hao Zhang. Learning implicit fields for generative shape modeling. CVPR'19
	- https://github.com/czq142857/implicit-decoder
- **DeepSDF**: Jeong Joon Park, Peter Florence, Julian Straub, Richard Newcombe, and Steven Lovegrove. DeepSDF: Learning continuous signed distance functions for shape representation. CVPR'19
	- Insight: point-based SDF;
	- https://github.com/facebookresearch/DeepSDF
	- Formulation: given a point x, a NN with latent code z as a classifier \
		<img src="/CV-3D/images/3d_output/deepsdf-1.png" alt="drawing" width="350"/>
	- Autoencoder: \
		<img src="/CV-3D/images/3d_output/deepsdf-2.png" alt="drawing" width="400"/>
	- Auto-decoder (encoder-less) training and inference: \
		<img src="/CV-3D/images/3d_output/deepsdf-3.png" alt="drawing" width="400"/>
		<img src="/CV-3D/images/3d_output/deepsdf-4.png" alt="drawing" width="400"/>
- **SIF**: Kyle Genova, Forrester Cole, Daniel Vlasic, Aaron Sarna, William T Freeman, and Thomas Funkhouser. Learning shape templates with structured implicit functions. ICCV'19
	- https://github.com/google/ldif
	- Union of scaled axis-aligned anisotropic 3D Gaussians;
- **DSIF**: Kyle Genova, Forrester Cole, Avneesh Sud, Aaron Sarna, and Thomas A. Funkhouser. Deep structured implicit functions. CoRR, abs/1912.06126, 2019
- **Pifu**: Shunsuke Saito, Zeng Huang, Ryota Natsume, Shigeo Morishima, Angjoo Kanazawa, and Hao Li. Pifu: Pixel-aligned implicit function for high-resolution clothed human digitization. ICCV'19
	- https://shunsukesaito.github.io/PIFu/
	- Learn inside/outside, then marching cube;
- Amos Gropp, Lior Yariv, Niv Haim, Matan Atzmon, and Yaron Lipman. Implicit geometric regularization for learning shapes. ICML'20
	- Add a regularization:
		- encourages f() to vanish on X and
		- if normal data exists (i.e., τ = 1), that df/dx is close to the supplied normals N
- **PIFuHD**: Shunsuke Saito, Tomas Simon, Jason Saragih, and Hanbyul Joo. PIFuHD: Multi-level pixel-aligned implicit function for high-resolution 3D human digitization. CVPR'20
- **SAL**: Matan Atzmon and Yaron Lipman. SAL: Sign agnostic learning of shapes from raw data. CVPR'20
- Saurabh Singh, Danhang Danny Tang, Phil Chou, Christian Haene, Mingsong Dou, Sean Fanello, Jonathan Taylor, Onur Gonen Guleryuz, Yinda Zhang, Shahram Izadi, Andrea Tagliasacchi, Sofien Bouaziz, and Cem Keskin. Deep implicit volume compression. CVPR'20
- SAL++: Matan Atzmon and Yaron Lipman. SAL++: Sign agnostic learning with derivatives. arxiv'20
- **BSPNet**: Zhiqin Chen, Andrea Tagliasacchi, and Hao Zhang. BSPNet: Generating compact meshes via binary space partitioning. CVPR'20
- **Dualsdf**: Zekun Hao, Hadar Averbuch-Elor, Noah Snavely, and Serge Belongie. Dualsdf: Semantic shape manipulation using a two-level representation. arXiv, 2020.
- Michael Niemeyer, Lars Mescheder, Michael Oechsle, and Andreas Geiger. Differentiable volumetric rendering: Learning implicit 3D representations without 3D supervision. CVPR'20
	- https://github.com/autonomousvision/differentiable_volumetric_rendering
	- Learn implicit function from 2D supervision;
- Yueqi Duan, Haidong Zhu, He Wang, Li Yi, Ram Nevatia, and Leonidas J. Guibas. Curriculum deepsdf, 2020
	- https://github.com/haidongz-usc/Curriculum-DeepSDF
	- Built on DeepSDF, train with progressive difficulty (error tolenrance)
- Vincent Sitzmann, Julien NP Martel, Alexander W Bergman, David B Lindell, and Gordon Wetzstein. Implicit neural representations with periodic activation functions. NeurIPS'20
	- https://vsitzmann.github.io/siren/
- Lior Yariv, Yoni Kasten, Dror Moran, Meirav Galun, Matan
Atzmon, Basri Ronen, and Yaron Lipman. Multiview neural surface reconstruction by disentangling geometry and appearance. NeurIPS'20
- Thomas Davies, Derek Nowrouzezahrai, and Alec Jacobson. On the effectiveness of weight-encoded neural implicit 3D shapes. ICML'21
	- https://github.com/u2ni/ICML2021
	- Neural SDF fitting;

## Matching, N-SDF across frames/shapes;
- Michael Niemeyer, Lars M. Mescheder, Michael Oechsle, and Andreas Geiger. Occupancy flow: 4d reconstruction by learning particle dynamics. ICCV'19
	- CNF;
- Feng Liu and Xiaoming Liu. Learning implicit functions for topology-varying dense 3d shape correspondence. NeurIPS'20	

## Sampling technique:
- Wang Yifan, Shihao Wu, Cengiz Öztireli, Olga Sorkine-Hornung. Iso-Points: Optimizing Neural Implicit Surfaces With Hybrid Representations. CVPR'21

## Misc
- Matthew Tancik, Pratul P. Srinivasan, Ben Mildenhall, Sara Fridovich-Keil, Nithin Raghavan, Utkarsh Singhal, Ravi Ramamoorthi, Jonathan T. Barron, and Ren Ng. Fourier features let networks learn high frequency functions in low dimensional domains. NeurIPS'20
