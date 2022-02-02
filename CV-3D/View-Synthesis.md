# View Synthesis

## Basics
- Task definition:
	- Synthesize a novel view from a different view point;
	- More general: 3D-aware 2D generation;
	- Roughly 3D Representation + Rendering;
- Approaches:
	- Direct output or from optical flow;
	- 3D voxel or mesh first;
	- Single depth;
	- Multiple plane (MPI)/Layered depth (LDI);
- Generally 2D rendered by volumetric rendering;
	- James T Kajiya and Brian P Von Herzen. Ray tracing volume densities. ACM SIGGRAPH'84

## Unclassified
- SM Ali Eslami, Danilo Jimenez Rezende, Frederic Besse, Fabio Viola, Ari S Morcos, Marta Garnelo, Avraham Ru- derman, Andrei A Rusu, Ivo Danihelka, Karol Gregor, et al. Neural scene representation and rendering. Science'18
- Shao-Hua Sun, Minyoung Huh, Yuan-Hong Liao, Ning Zhang, and Joseph J Lim. Multi-view to novel view: Synthesizing novel views with self-learned confidence. ECCV'18
- One object:
	- Kyle Olszewski, Sergey Tulyakov, Oliver Woodford, Hao Li, and Linjie Luo. Transformable bottleneck networks. ICCV'19
- Gernot Riegler and Vladlen Koltun. Stable view synthesis. arxiv'20

## Implicit Radience Field
- Basic idea:
	- Use a MLP to overfit color and occupancy of a scene, supervised by each image;
- Xu Chen, Jie Song, and Otmar Hilliges. Monocular neural image based rendering with continuous view control. ICCV'19
	- Analysis
- **SRN**: Vincent Sitzmann, Michael Zollhofer, and Gordon Wetzstein. Scene representation networks: Continuous 3d-structure-aware neural scene representations. NeurIPS'19
	- https://github.com/vsitzmann/scene-representation-networks
- **NERF**: Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik, Jonathan T. Barron, Ravi Ramamoorthi, and Ren Ng. NeRF: Representing scenes as neural radiance fields for view synthesis. ECCV'20
	- Insight: overfit a function mlp(x,y,z,theta,phi) to explain the scene;
	- Key techniques to improve novel view synthesis performance:
		- Positional encoding;
		- Multi-resolution;
- Zhengqi Li, Simon Niklaus, Noah Snavely,and Oliver Wang. Neural scene flow fields for space-time view synthesis of dynamic scenes. arxiv'20
- Alex Yu, Vickie Ye, Matthew Tancik, and Angjoo Kanazawa. pixelnerf: Neural radiance fields from one or few images. arxiv'20
	- Similar to IBRNet, with abs coord?
- Daniel Rebain, Wei Jiang, Soroosh Yazdani, Ke Li, Kwang Moo Yi, and Andrea Tagliasacchi. Derf: Decomposed radiance fields. arxiv'20
- Keunhong Park, Utkarsh Sinha, Jonathan T. Barron, Sofien Bouaziz, Dan B Goldman, Steven M. Seitz, and Ricardo Martin-Brualla. Deformable neural radiance fields. arxiv'20
- Konstantinos Rematas, Ricardo Martin-Brualla, and Vittorio Ferrari. Sharf: Shape-conditioned radiance fields from a single view. arxiv'21
- Ricardo Martin-Brualla, Noha Radwan, Mehdi S. M. Sajjadi, Jonathan T. Barron, Alexey Dosovitskiy, and Daniel Duckworth. NeRF in the Wild: Neural Radiance Fields for Unconstrained Photo Collections. CVPR'21
- Generative
	- Marco Fraccaro, Danilo Jimenez Rezende, Yori Zwols, Alexander Pritzel, SM Eslami, and Fabio Viola. Generative temporal models with spatial memory for partially observed environments. arxiv'18
	- Philipp Henzler, Niloy J Mitra, and Tobias Ritschel. Escaping plato's cave: 3d shape from adversarial rendering. ICCV'19
	- Thu Nguyen-Phuoc, Chuan Li, Lucas Theis, Christian Richardt, and Yong-Liang Yang. Hologan: Unsupervised learning of 3d representations from natural images. ICCV'19
	- Eric R Chan, Marco Monteiro, Petr Kellnhofer, Jiajun Wu, and Gordon Wetzstein. pi-GAN: Periodic implicit generative adversarial networks for 3d-aware image synthesis. arxiv'20
	- Michael Niemeyer and Andreas Geiger. Giraffe: Representing scenes as compositional generative neural feature fields. arxiv'20
	- Katja Schwarz, Yiyi Liao, Michael Niemeyer, and Andreas Geiger. GRAF: Generative radiance fields for 3d-aware image synthesis. arxiv'20
	- Alex Trevithick and Bo Yang. Grf: Learning a general radiance field for 3d scene representation and rendering. arxiv'20
		- Similar to IBRNet, but use absolute coord;
	- **SGN**: Terrance DeVries, Miguel Angel Bautista, Nitish Srivastava, Graham W. Taylor, Joshua M. Susskind. Unconstrained Scene Generation with Locally Conditioned Radiance Fields. ICCV'21
		- Global generator from a latent code z: W=g(z); with StyleGAN2;
		- Local radience field from an angle p: (sigma, color)=f(wij, p); modulated linear layers similar to CIPS;
- Pratul P. Srinivasan, Boyang Deng, Xiuming Zhang, Matthew Tancik, Ben Mildenhall, and Jonathan T. Barron. Nerv: Neural reflectance and visibility fields for relighting and view synthesis. arxiv'20

## Explicit
- For combination:
	- Alpha-Compositing: Thomas Porter and Tom Duff. Compositing digital images. Computer graphics and interactive techniques, 1984.
- Voxels:
	- **Refer to Voxels in 3D-represenation**;
	- Nima Khademi Kalantari, Ting-Chun Wang, and Ravi Ramamoorthi. Learning-based view synthesis for light field cameras. ACM TOG, 2016
	- Eric Penner and Li Zhang. Soft 3D reconstruction for view synthesis. SIGGRAPH Asia, 2017
	- Shubham Tulsiani, Tinghui Zhou, Alexei A. Efros,and Jitendra Malik. Multi-view supervision for single-view reconstruction via differentiable ray consistency. CVPR, 2017.
	- Abhishek Kar, Christian Hane, and Jitendra Malik. Learning a multi-view stereo machine. NeurIPS, 2017
	- Vincent Sitzmann, Justus Thies, Felix Heide, Matthias Nießner, Gordon Wetzstein, and Michael Zollhofer. Deepvoxels: Learning persistent 3d feature embeddings. CVPR'19
	- Lingjie Liu, Jiatao Gu, Kyaw Zaw Lin, Tat-Seng Chua, and Christian Theobalt. Neural sparse voxel fields. arxiv'20
	- Philipp Henzler, Niloy J. Mitra, and Tobias Ritschel. Learning a neural 3d texture space from 2d exemplars. CVPR'20
- Layered/Multiplane
	- John Flynn, Ivan Neulander, James Philbin, and Noah Snavely. Deepstereo: Learning to predict new views from the world's imagery. CVPR'16
	- **LDI**: Shubham Tulsiani, Richard Tucker, Noah Snavely. Layer-structured 3D Scene Inference via View Synthesis. ECCV'18
		- https://shubhtuls.github.io/lsi/
		- https://github.com/google/layered-scene-inference
	- Tinghui Zhou, Richard Tucker, John Flynn, Graham Fyffe, Noah Snavely. Stereo Magnification: Learning View Synthesis using Multiplane Images. SIGGRAPH'18
		- https://people.eecs.berkeley.edu/~tinghuiz/projects/mpi/
	- **MPI**: Pratul P. Srinivasan, Richard Tucker, Jonathan T. Barron, Ravi Ramamoorthi, Ren Ng, Noah Snavely. Pushing the Boundaries of View Extrapolation with Multiplane Images. CVPR'19
		- https://github.com/google-research/google-research/tree/master/mpi_extrapolation
	- John Flynn, Michael Broxton, Paul Debevec, Matthew DuVall, Graham Fyffe, Ryan Overbeck, Noah Snavely, Richard Tucker. DeepView: View synthesis with learned gradient descent. CVPR'19
		- https://augmentedperception.github.io/deepview/
	- Ben Mildenhall, Pratul P Srinivasan, Rodrigo Ortiz-Cayon, Nima Khademi Kalantari, Ravi Ramamoorthi, Ren Ng, and Abhishek Kar. Local light field fusion: Practical view synthesis with prescriptive sampling guidelines. TOG'19
	- Peng Dai, Yinda Zhang, Zhuwen Li, Shuaicheng Liu, and Bing Zeng. Neural point cloud rendering via multi-plane projection. CVPR'20
	- Zhengqi Li, Wenqi Xian, Abe Davis, and Noah Snavely. Crowdsampling the plenoptic function. ECCV'20

## Extroplate, Large Angle
- Inchang Choi, Orazio Gallo, Alejandro Troccoli, Min H Kim, and Jan Kautz. Extreme view synthesis. ICCV'19
- Andrew Liu, Richard Tucker, Varun Jampani, Ameesh Makadia, Noah Snavely, and Angjoo Kanazawa. Infinite nature: Perpetual view generation of natural scenes from a single image. arxiv'20

## Image Based Rendering: Multi Images/Warping/Alpha-Blending
- Legacy:
	- Shenchang Eric Chen and Lance Williams. View interpolation for image synthesis. SIGGRAPH'93.
	- Marc Levoy and Pat Hanrahan. Light field rendering. SIGGRAPH'96
		- Blending weight based on ray proximity;
- Proxy geometry:
	- Gaurav Chaurasia, Sylvain Duchene, Olga Sorkine-Hornung, and George Drettakis. Depth synthesis and local warps for plausible image-based navigation. ACM TOG, 2013.
	- Peter Hedman, Tobias Ritschel, George Drettakis, and Gabriel Brostow. Scalable inside-out image-based rendering. TOG'16
- Optical flow:
	- Martin Eisemann, Bert De Decker, Marcus Magnor, Philippe Bekaert, Edilson De Aguiar, Naveed Ahmed, Christian Theobalt, and Anita Sellent. Floating textures. Computer graphics forum, 2008
	- Dan Casas, Christian Richardt, John Collomosse, Christian Theobalt, and Adrian Hilton. 4d model flow: Precomputed appearance alignment for real-time 4d video interpolation. CGF'15
	- Ruofei Du, Ming Chuang, Wayne Chang, Hugues Hoppe,and Amitabh Varshney. Montage4d: Interactive seamless fusion of multiview video textures. ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games, 2018
- Soft blending:
	- Eric Penner and Li Zhang. Soft 3D reconstruction for view synthesis. SIGGRAPH Asia, 2017
	- Gernot Riegler and Vladlen Koltun. Free view synthesis. ECCV'20
- Mesh surface:
	- Paul Debevec, Yizhou Yu, and George Borshukov. Efficient view-dependent image-based rendering with projective texture-mapping. Eurographics W'98
	- Jingwei Huang, Justus Thies, Angela Dai, Abhijit Kundu, Chiyu Jiang, Leonidas J Guibas, Matthias Nießner, and Thomas Funkhouser. Adversarial texture optimization from rgb-d scans. CVPR, 2020.
	- Justus Thies, Michael Zollhofer, and Matthias Nießner. Deferred neural rendering: Image synthesis using neural textures. ACM TOG'19
- Point cloud:
	- Kara-Ali Aliev, Artem Sevastopolsky, Maria Kolos,Dmitry Ulyanov, and Victor Lempitsky. Neural point-based graphics. arxiv'19
	- Moustafa Mahmoud Meshry, Dan B Goldman, Sameh Khamis, Hugues Hoppe, Rohit Kumar Pandey, Noah Snavely, and Ricardo Martin Brualla. Neural rerendering in the wild. CVPR'19
	- Francesco Pittaluga, Sanjeev JKoppal, Sing Bing Kang, and Sudipta N Sinha. Revealing scenes by inverting structure from motion reconstructions. CVPR'19
- Peter Hedman, Julien Philip, True Price, Jan-Michael Frahm, George Drettakis, and Gabriel Brostow. Deep blending for free-viewpoint image-based rendering. SIGGRAPH Asia'18
	- Generate 2 MVS, then CNN to blend;
		- Michal Jancosek and Tomas Pajdla. Multi-view reconstruction preserving weakly-supported surfaces. CVPR, 2011
		- Johannes L Schonberger and Jan-Michael Frahm. Structure- from-motion revisited. CVPR, 2016
- **IBRNet**: Qianqian Wang, Zhicheng Wang, Kyle Genova, Pratul Srinivasan, Howard Zhou, Jonathan T Barron, Ricardo Martin-Brualla, Noah Snavely, and Thomas Funkhouser. Ibrnet: Learning multi-view image-based rendering. CVPR'21

## Unclassified
- Hao Su, Fan Wang, Eric Yi, Leonidas Guibas. 3D-Assisted Feature Synthesis for Novel Views of an Object. ICCV'15
- J Yang. Weakly-supervised Disentangling with Recurrent Transformations for 3D View Synthesis. NIPS 2015
	- Input/output: images
	- https://github.com/jimeiyang/deepRotator
- M Tatarchenko, A Dosovitskiy, T Brox. Multi-view 3D Models from Single Images with a Convolutional Network. ECCV'16
	- Encoder/Decoder
	- Problem setup: Input RGB, output RGB/D conditioned on any shape input (angle, ...)
	- Separate model for 3D reconstruction (Point-cloud) from multiple RGBD, then mesh;
	- https://github.com/lmb-freiburg/mv3d
- T. Zhou, S. Tulsiani, W. Sun, J. Malik and A. Efros. View synthesis by appearance flow. ECCV'16
	- https://github.com/tinghuiz/appearance-flow
- A Dosovitskiy, J Springenberg, M Tatarchenko, T Brox. Learning to Generate Chairs, Tables and Cars with Convolutional Networks. PAMI'17
	- Input: class c, view v, transfrom param theta;
	- Output: image;
	- Conv, deconv, upsampling;
- J. Xie, R. B. Girshick, and A. Farhadi. Deep3D: Fully automatic 2D-to-3D video conversion with deep convolutional neural networks. ECCV'16
	- Key insight: Unsupervised;
	- Input: left view; Output: right view
	- Evaluation: Kitti, NYU;\
		<img src="/CV-3D/images/depth-est/deep3d.png" alt="drawing" width="500"/>
- E Park, J Yang, E Yumer, D Ceylan, and A Berg. Transformation-Grounded Image Generation Network for Novel 3d View Synthesis. 2017
- Johanna Delanoy, Mathieu Aubry, Phillip Isola, Alexei A. Efros, Adrien Bousseau. 3D Sketching using Multi-View Deep Volumetric Prediction. CGIT'18
- S Sun, M Huh, Y Liao, N Zhang, and J Lim. Multi-view to Novel view: Synthesizing Novel Views with Self-Learned Confidence. ECCV'18
	- Problem: novel view synthesis
	- Input: many images;
	- https://github.com/shaohua0116/Multiview2Novelview
- Daeyun Shin, Zhile Ren, Erik B. Sudderth, Charless C. Fowlkes. 3D Scene Reconstruction with Multi-layer Depth and Epipolar Transformers. ICCV'19
	- https://research.dshin.org/iccv19/multi-layer-depth/
- **SynSin**: Olivia Wiles, Georgia Gkioxari, Richard Szeliski, Justin Johnson. SynSin: End-to-end View Synthesis from a Single Image. CVPR'20 submission
	- http://www.robots.ox.ac.uk/~ow/synsin.html

## Disentangled
- **3D-SDN**: Shunyu Yao, Tzu Ming Harry Hsu, Jun-Yan Zhu, Jiajun Wu, Antonio Torralba, William T. Freeman, Joshua B. Tenenbaum. 3D-Aware Scene Manipulation via Inverse Graphics. NIPS'18
	- http://3dsdn.csail.mit.edu/
	- https://github.com/ysymyth/3D-SDN
	- Algorithm:\
		<img src = '/Composition/images/2d/3d-sdn.png' width = '400'>

## Legacy:
- S. E. Chen and L. Williams. View interpolation for image synthesis. 1993
- C. L. Zitnick, S. B. Kang, M. Uyttendaele, S. Winder, and R. Szeliski. High-quality video view interpolation using a layered representation. TOG'04
- S. M. Seitz and C. R. Dyer. View morphing. 1996
