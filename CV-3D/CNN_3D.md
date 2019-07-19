# CNN for 3D Data

## Point Clouds
- R. Klokov and V. Lempitsky. Escape from cells: Deep Kd-networks for the recognition of 3D point cloud models. ICCV 2017
	- Point clouds
	- http://sites.skoltech.ru/compvision/kdnets/
	- Work with Kd-tree; (top-down, every node split the axis with largest span);
	- Recursive bottom-up;
	- Properties:
		- Layerwise parameter sharing;
		- Hierarchical representation;
		- Partial invariance to jitter;
		- Non-invariance to rotations;
		- Role of kd-tree structure;
	- Experiments: MNIST 2D points; ModelNet;
- **3D-Transformer**: S Xie, S Liu, Z Chen, Z Tu. Attentional ShapeContextNet for Point Cloud Recognition. CVPR'18
- P. Hermosilla, T. Ritschel, P.-P. Vazquez, A. Vinacua,  and T. Ropinski. Monte carlo convolution for learning on non-uniformly sampled point clouds. 2018
	- Point Clouds (generally non-uniform);
	- Estimate sample density distribution;
	- https://github.com/viscom-ulm/MCCNN
- J. Li, B. M. Chen, and G. H. Lee. SO-Net: Self-organizing network for point cloud analysis. CVPR 2018
- Y. Li, R. Bu, M. Sun, and B. Chen. PointCNN: Convolution on X -transformed points. NIPS 2018

## Voxel
- B. Graham, M. Engelcke, and L. van der Maaten. 3D semantic segmentation with submanifold sparse convolutional networks. CVPR 2018
	- SSCN (submanifold sparse Conv Net)
	- https://github.com/facebookresearch/SparseConvNet
	- SSCN(m, n, f, s): m input, n output, f filter-size, s stride;
	- Implementation: a hash table (https://github.com/sparsehash/sparsehash) and a matrix;
	- **Sparse Voxelized**: applied on Submanifold FCN and U-Nets;
	- CPU-only;
	- Experiments: ShapeNet; NYU depth;