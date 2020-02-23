# 3D-Aware Image Generation

## Basics
- Synthesize a novel view from a different view point;
- Approaches:
	- Direct output or from optical flow;
	- 3D voxel or mesh first;
	- Single depth;
	- Layered depth (LDI);

## Unclassified
- M Tatarchenko, A Dosovitskiy, T Brox. Multi-view 3D Models from Single Images with a Convolutional Network. ECCV'16
	- Encoder/Decoder
	- Problem setup: Input RGB, output RGB/D conditioned on any shape input (angle, ...)
	- Separate model for 3D reconstruction (Point-cloud) from multiple RGBD, then mesh;
	- https://github.com/lmb-freiburg/mv3d
- A Dosovitskiy, J Springenberg, M Tatarchenko, T Brox. Learning to Generate Chairs, Tables and Cars with Convolutional Networks. PAMI'17
	- Input: class c, view v, transfrom param theta;
	- Output: image;
	- Conv, deconv, upsampling;
- Johanna Delanoy, Mathieu Aubry, Phillip Isola, Alexei A. Efros, Adrien Bousseau. 3D Sketching using Multi-View Deep Volumetric Prediction. CGIT'18
- Tinghui Zhou, Richard Tucker, John Flynn, Graham Fyffe, Noah Snavely. Stereo Magnification: Learning View Synthesis using Multiplane Images. SIGGRAPH'18
	- https://people.eecs.berkeley.edu/~tinghuiz/projects/mpi/
- **LDI**: Shubham Tulsiani, Richard Tucker, Noah Snavely. Layer-structured 3D Scene Inference via View Synthesis. ECCV'18
	- https://shubhtuls.github.io/lsi/
	- https://github.com/google/layered-scene-inference
- John Flynn, Michael Broxton, Paul Debevec, Matthew DuVall, Graham Fyffe,
Ryan Overbeck, Noah Snavely, Richard Tucker. DeepView: View synthesis with learned gradient descent. CVPR'19
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