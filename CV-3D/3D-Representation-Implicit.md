# Implicit Functions (N-SDF)

## Legacy
- B. Curless and M. Levoy. A volumetric method for building complex models from range images. SIGGRAPH'96
- **RBF**: J Carr, R Beatson, J Cherrie, T Mitchell, W Fright, B McCallum, and T Evans. Reconstruction and representation of 3d objects with radial basis functions. SIGGRAPH'01
- G Turk and J O'Brien. Modelling with implicit surfaces that interpolate. TOG'02
- **Unity implicits**: Y Ohtake, A Belyaev, M Alexa, G Turk, and H Seidel. Multi-level partition of unity implicits, volume 22. ACM, 2003
- C Shen, J O'Brien, and J Shewchuk. Interpolating and approximating implicit surfaces from polygon soup. TOG'04

## Render for implicit models:
- Marching Cube;
- J Hart. Sphere tracing: A geometric method for the antialiased ray tracing of implicit surfaces. 1996
- **Surface-Finding**: S Frisken, R Perry, A Rockwood, and T Jones. Adaptively sampled distance fields: A general representation of shape for computer graphics. 2000

## Generalized Neural-SDF or indicator Function:
- Matan Atzmon, Niv Haim, Lior Yariv, Ofer Israelov, Haggai Maron, and Yaron Lipman. Controlling neural level sets. NeurIPS'19
- Songyou Peng, Michael Niemeyer, Lars Mescheder, Marc Pollefeys, and Andreas Geiger. Convolutional occupancy networks. ECCV'20.
- Backbone:
	- 3D-Conv: OCCNet;
	- Point-Cloud: DeepSdf [Facebook, CVPR'19]
	- MLP: Nerf, GRAF, GIRRAFE,
	- SIREN: Siren [G Wetzstein NeurIPS'20] Pi-GAN [CVPR'21];
		- Periodic activation function (e.g. sin, cos)
- Supervision:
	- Point in/out: OCCNet [L Mescheder, A Geiger, CVPR'19]; DeepSDF [CVPR'19]; IM-Net [Z.Chen, H. Zhang CVPR'19];
	- GAN
	- GAN on rendered image: GIRAFFE, Pi-GAN;
- Post-processing to get mesh:
	- Marching Cube;
	- MISE -> Marching cube (OCCNet)
- Union/Composition of piecewise/lobal SDF/indicator:
	- **SIF**: Union of Gaussian Ball [Kyle Genova. ICCV'19]
		- https://github.com/google/ldif
	- **DSIF**: Relaxed Gaussian assumption [Kyle Genova'19]
	- Union of scaled axis-aligned anisotropic 3D Gaussians;	- **CvxNet**: Boyang Deng. CVPR'20
		- https://cvxnet.github.io/
		- https://github.com/tensorflow/graphics/tree/master/tensorflow_graphics/projects/cvxnet
	- **GIRAFFE**: M Niemeyer, A Geiger. CVPR'21
		- Composing GRAF [NeurIPS'20] together
- Local/global:
	- **DISN**: Q Xu, W Wang, D Ceylan, R Mech, and U Neumann. Disn: Deep implicit surface network for high-quality single-view 3d reconstruction. NeurIPS'19
		- https://github.com/laughtervv/DISN
	- Chiyu Max Jiang, Avneesh Sud, Ameesh Makadia, Jingwei Huang, Matthias Nießner, and Thomas A. Funkhouser. Local implicit grid representations for 3d scenes. 2020
	- Rohan Chabra, Jan Eric Lenssen, Eddy Ilg, Tanner Schmidt, Julian Straub, Steven Lovegrove, and Richard Newcombe. Deep local shapes: Learning local SDF priors for detailed 3d reconstruction. CoRR'20
	- PatchNets: Edgar Tretschk, Ayush Tewari, Vladislav Golyanik, Michael Zollhöfer, Carsten Stoll, and Christian Theobalt. PatchNets: Patch-Based Generalizable Deep Implicit 3D Shape Representations. ECCV'20
		- https://github.com/edgar-tr/patchnets
	- Moritz Ibing, Isaak Lim, Leif Kobbelt. 3D Shape Generation With Grid-Based Implicit Functions. CVPR'21
- **Pifu**: Shunsuke Saito, Zeng Huang, Ryota Natsume, Shigeo Morishima, Angjoo Kanazawa, and Hao Li. Pifu: Pixel-aligned implicit function for high-resolution clothed human digitization. ICCV'19
	- https://shunsukesaito.github.io/PIFu/
	- Learn inside/outside, then marching cube;
- Amos Gropp, Lior Yariv, Niv Haim, Matan Atzmon, and Yaron Lipman. Implicit geometric regularization for learning shapes. ICML'20
	- Add a regularization:
		- encourages f() to vanish on X and
		- if normal data exists (i.e., τ = 1), that df/dx is close to the supplied normals N
- **PIFuHD**: Shunsuke Saito, Tomas Simon, Jason Saragih, and Hanbyul Joo. PIFuHD: Multi-level pixel-aligned implicit function for high-resolution 3D human digitization. CVPR'20
- **SAL**: Matan Atzmon and Yaron Lipman. SAL: Sign agnostic learning of shapes from raw data. CVPR'20
- S Singh, D Tang, P Chou, C Haene, M Dou, S Fanello, J Taylor, O Gonen Guleryuz, Y Zhang, S Izadi, A Tagliasacchi, S Bouaziz, and C Keskin. Deep implicit volume compression. CVPR'20
- SAL++: M Atzmon and Y Lipman. SAL++: Sign agnostic learning with derivatives. arxiv'20
- **BSPNet**: Z Chen, A Tagliasacchi, and H Zhang. BSPNet: Generating compact meshes via binary space partitioning. CVPR'20
- **Dualsdf**: Zekun Hao, Hadar Averbuch-Elor, Noah Snavely, and Serge Belongie. Dualsdf: Semantic shape manipulation using a two-level representation. arXiv, 2020.
- M Niemeyer, L Mescheder, M Oechsle, and A Geiger. Differentiable volumetric rendering: Learning implicit 3D representations without 3D supervision. CVPR'20
	- https://github.com/autonomousvision/differentiable_volumetric_rendering
	- Learn implicit function from 2D supervision;
- Yueqi Duan, Haidong Zhu, He Wang, Li Yi, Ram Nevatia, and Leonidas J. Guibas. Curriculum deepsdf, 2020
	- https://github.com/haidongz-usc/Curriculum-DeepSDF
	- Built on DeepSDF, train with progressive difficulty (error tolenrance)
- L Yariv, Y Kasten, D Moran, M Galun, M Atzmon, B Ronen, and Y Lipman. Multiview neural surface reconstruction by disentangling geometry and appearance. NeurIPS'20
- Thomas Davies, Derek Nowrouzezahrai, and Alec Jacobson. On the effectiveness of weight-encoded neural implicit 3D shapes. ICML'21
	- https://github.com/u2ni/ICML2021
	- Neural SDF fitting;

## Matching, N-SDF across frames/shapes;
- Michael Niemeyer, Lars M. Mescheder, Michael Oechsle, and Andreas Geiger. Occupancy flow: 4d reconstruction by learning particle dynamics. ICCV'19
	- CNF;
- Feng Liu and Xiaoming Liu. Learning implicit functions for topology-varying dense 3d shape correspondence. NeurIPS'20	

## Sampling Technique
- Wang Yifan, Shihao Wu, Cengiz Öztireli, Olga Sorkine-Hornung. Iso-Points: Optimizing Neural Implicit Surfaces With Hybrid Representations. CVPR'21

## Misc
- M Tancik, P Srinivasan, B Mildenhall, S Fridovich-Keil, N Raghavan, U Singhal, R Ramamoorthi, J Barron, and R Ng. Fourier features let networks learn high frequency functions in low dimensional domains. NeurIPS'20
