# View Synthesis

## Basics
- Task definition:
	- Synthesize a novel view from a different view point;
	- More general: 3D-aware 2D generation;
- Approaches:
	- Direct output or from optical flow;
	- 3D voxel or mesh first;
	- Single depth;
	- Layered depth (LDI);

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
- Tinghui Zhou, Richard Tucker, John Flynn, Graham Fyffe, Noah Snavely. Stereo Magnification: Learning View Synthesis using Multiplane Images. SIGGRAPH'18
	- https://people.eecs.berkeley.edu/~tinghuiz/projects/mpi/
- S Sun, M Huh, Y Liao, N Zhang, and J Lim. Multi-view to Novel view: Synthesizing Novel Views with Self-Learned Confidence. ECCV'18
	- Problem: novel view synthesis
	- Input: many images;
	- https://github.com/shaohua0116/Multiview2Novelview
- **LDI**: Shubham Tulsiani, Richard Tucker, Noah Snavely. Layer-structured 3D Scene Inference via View Synthesis. ECCV'18
	- https://shubhtuls.github.io/lsi/
	- https://github.com/google/layered-scene-inference
- John Flynn, Michael Broxton, Paul Debevec, Matthew DuVall, Graham Fyffe, Ryan Overbeck, Noah Snavely, Richard Tucker. DeepView: View synthesis with learned gradient descent. CVPR'19
	- https://augmentedperception.github.io/deepview/
- **MPI**: Pratul P. Srinivasan, Richard Tucker, Jonathan T. Barron, Ravi Ramamoorthi, Ren Ng, Noah Snavely. Pushing the Boundaries of View Extrapolation with Multiplane Images. CVPR'19
	- https://github.com/google-research/google-research/tree/master/mpi_extrapolation
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
