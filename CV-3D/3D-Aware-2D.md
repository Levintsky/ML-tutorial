# 3D-Aware Image Generation

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

## Disentangled
- **3D-SDN**: Shunyu Yao, Tzu Ming Harry Hsu, Jun-Yan Zhu, Jiajun Wu, Antonio Torralba, William T. Freeman, Joshua B. Tenenbaum. 3D-Aware Scene Manipulation via Inverse Graphics. NIPS'18
	- http://3dsdn.csail.mit.edu/
	- https://github.com/ysymyth/3D-SDN
	- Algorithm:\
		<img src = '/Composition/images/2d/3d-sdn.png' width = '400'>