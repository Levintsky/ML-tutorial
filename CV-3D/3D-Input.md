# 3D Data as Input

## Basics
- Point clouds;
- Voxel;
- Mesh;
- Multi-view images;

## Unclassified
- L. Yi, H. Su, X. Guo, and L. J. Guibas. SyncSpecCNN: Synchronized spectral CNN for 3D shape segmentation. CVPR'17
- S. Savarese and L. Fei-Fei. 3d generic object categorization, localization and pose estimation, ICCV'17
- Rosanne Liu, Joel Lehman, Piero Molino, Felipe Petroski Such, Eric Frank, Alex Sergeev, Jason Yosinski. An intriguing failing of convolutional neural networks and the CoordConv solution. NIPS'18
	- 2D as 3D;
- **PVCNN**: Zhijian Liu, Haotian Tang, Yujun Lin, Song Han. Point-Voxel CNN for Efficient 3D Deep Learning. NIPS'19

## Point Clouds
- Unclassified:
	- Matheus Gadelha, Rui Wang, and Subhransu Maji. Multiresolution tree networks for 3d point cloud processing. ECCV'18
		- VAE
	- Y. Xu, T. Fan, M. Xu, L. Zeng, and Y. Qiao. SpiderCNN: Deep learning on point sets with parameterized convolutional filters. ECCV'18
		- **SOA**
	- P. Hermosilla, T. Ritschel, P.-P. Vazquez, A. Vinacua, and T. Ropinski. Monte carlo convolution for learning on non-uniformly sampled point clouds. TOG'18
		- Point Clouds (generally non-uniform);
		- Estimate sample density distribution;
		- https://github.com/viscom-ulm/MCCNN
	- J. Li, B. M. Chen, and G. H. Lee. SO-Net: Self-organizing network for point cloud analysis. CVPR'18
- **Grid-Cell**: still within regular grid;
	- **PointGrid**: T. Le and Y. Duan. PointGrid: A deep network for 3D shape understanding. CVPR 2018
		- Preprocessing: normalize to [-1, 1]
		- Each grid cell: **exactly K=4 points** in 16 x 16 x 16, each cell 3K-dim feature; if originally >= K points, sample; < K, sample with replacement
		<img src="/CV-3D/images/3d_input/pointgrid.png" alt="drawing" width="500"/>
	- **SplatNet**: H. Su, V. Jampani, D. Sun, S. Maji, E. Kalogerakis, M.-H. Yang, and J. Kautz. SplatNet: Sparse lattice networks for point cloud processing. CVPR'18
		- Input: point clouds and images; output semantic for each point;
		- BCL (Bilateral Convolution Layer): 1. Splat: project onto lattice; 2. Convolve; 3. Slice. Can have different scale size;
		- 2D-3D: DeepLab segmentation for 2D images/rendered from mesh; project pixels to 3D, BCL;
		<img src="/CV-3D/images/3d_input/splatnet1.png" alt="drawing" width="450"/>
		<img src="/CV-3D/images/3d_input/splatnet2.png" alt="drawing" width="500"/>
		<img src="/CV-3D/images/3d_input/splatnet3.png" alt="drawing" width="600"/>
	- **Kd-network**: R. Klokov and V. Lempitsky. Escape from cells: Deep Kd-networks for the recognition of 3D point cloud models. ICCV'17
		- Irregular grid;
		- http://sites.skoltech.ru/compvision/kdnets/
		- Construction: Work with Kd-tree; (top-down, every node split the axis with largest span);
		- Non-leaf nodes: Recursive bottom-up, Recursive-NN;
		- Properties: Layerwise parameter sharing; Hierarchical representation; Partial invariance to jitter; Non-invariance to rotations; Role of kd-tree structure;
		- Experiments: MNIST 2D points; ModelNet;
		<img src="/CV-3D/images/3d_input/kd-network1.png" alt="drawing" width="500"/>
		<img src="/CV-3D/images/3d_input/kd-network2.png" alt="drawing" width="400"/>
		<img src="/CV-3D/images/3d_input/kd-network3.png" alt="drawing" width="500"/>
- **Unordered**:
	- **PointNet**: H Su, C Qi, K Mo, L Guibas. PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation, CVPR'17\
		<img src="/CV-3D/images/3d_input/pointnet.png" alt="drawing" width="600"/>
	- **PointNet++**:  Charles R. Qi, Li Yi, Hao Su, Leonidas J. Guibas. Deep Hierarchical Feature Learning on Point Sets in a Metric Space, NIPS'17
		- **Classification mode**: [SA module x 3] + FC_layers;
		- **Semantic Segmentation mode**: [SA-module x3] + [FP-modules x4] + [Conv1d x2]
		- SA module #1, #2: xyz, features = model(xyz, features=None), xyz: (B, 2048, 3)
			- Gather operation: **FPS** (furtherest point sampling), from N points, select N' < N centers as new_xyz (B, N', 3)
			- Group-Query-MLP x 3 (with different radius)
				- Group and Query: to (B, d, N', nS), dim: feature dim; each N' centers will be assigned nS=16 members
				- Shared MLPs: with dim like [d, 32, 32, 64], output (B, 64, N', nS), implement FC with 2D-Conv with kernel-size (1, 64)
				- Max-pooling along last dimension (B, 64, 512)
			- After SA-1: xyz=(B, 512, 3), feat=(B, 320, 512)
			- After SA-2: xyz=(B, 128, 3), feat=(B, 640, 128)
		- SA module #3:
			- No gather operation: new_xyz=None
			- GroupAll: (B, 643, 1, nS), 643=640+3, nS=128
			- Shared MLPs: (B, 1024, 1)
		- FC_layers: [1024, 512, 256, nClass]
		- Finally a 256-dim feature
		- FPN-modules are used to **interpolate features back**;
		```python
		feat[i-1] = self.FP_modules[i](xyz[i-1], xyz[i], feat[i-1], feat[i])
		```	
		- With shape: (B, n, 3), (B, m, 3), (B, C1, n), (B, C2, m), returns (B, mlp[-1], n)
		<img src="/CV-3D/images/3d_input/pointnet++.png" alt="drawing" width="600"/>
- **Attention**:
	- **3D-Transformer**: S Xie, S Liu, Z Chen, Z Tu. Attentional ShapeContextNet for Point Cloud Recognition. CVPR'18
		- Feature of point pi: Histogram of pj-pi (24 bins = 3 radius x 8 angle)
		<img src="/CV-3D/images/3d_input/3d-transformer.png" alt="drawing" width="600"/>
	- S Wang, S Suo, W Ma, A Pokrovsky, R Urtasun. Deep Parametric Continuous Convolutional Neural Networks. CVPR'18
		- key idea: exploit **parameterized kernel** functions that span the full continuous vector space
		- Gaussian kernel: K. T. Schutt, P. Kindermans, H. Sauceda, S. Chmiela, A. Tkatchenko, and K. Muller. Schnet: A continuous-filter convolutional neural network for modeling quantum interactions. 2017\
			<img src="/Autonomous-Driving/images/detection/continuous1.png" alt="drawing" width="500"/>
			<img src="/Autonomous-Driving/images/detection/continuous2.png" alt="drawing" width="600"/>
	- Y. Li, R. Bu, M. Sun, and B. Chen. PointCNN: Convolution on X-transformed points. NIPS'18
		- 1 weighting: of the input features associated with the points, 
		- 2.permutation: into a latent and potentially canonical order
		- https://github.com/yangyanli/PointCNN
		<img src="/CV-3D/images/3d_input/pointcnn1.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/3d_input/pointcnn2.png" alt="drawing" width="600"/>
- **Graph**:
	- **FoldingNet**: Y. Yang, C. Feng, Y. Shen, and D. Tian. Foldingnet: Interpretable unsupervised learning on 3d point clouds. CVPR'18 \
		<img src="/CV-3D/images/3d_input/foldingnet.png" alt="drawing" width="600"/>
	- **DGCNN**: Y Wang, Y Sun, Z Liu, S Sarma, M Bronstein, and J Solomon. Dynamic Graph CNN for Learning on Point Clouds. TOG'19
		- Graph **changes by layer**: compute nn on the fly;
		- EdgeConv-layer:
			- Dynamic Graph construction: Each node has k nearest neighbors in feature space, form k-edges; 
			- Node interaction by edge: Collect features from neighboring nodes, do f-f'; (?, d, 1024, k)
			- Channel-wise Conv - BN - LReLU (implemented by Conv2d);
			- Aggregation: maxpool edges with the same node, maps the feature back;
	- X. Wang, B. Zhou, H. Fang, X. Chen, Q. Zhao, and K. Xu. Learning to group and label fine-grained shape components. SIGGRAPH Asia'18	

## Voxel
- **ModelNet**: Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang and J. Xiao. 3D ShapeNets: A Deep Representation for Volumetric Shapes. CVPR'15
	- Predict next best angle (most uncertain by max entropy diff)
- D Maturana and S Scherer. VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition. IROS 2015
	- https://github.com/dimatura/voxnet
- C R Qi, H Su, M Niessner, A Dai, M Yan, and L J Guibas. Volumetric and multi-view cnns for object classification on 3d data. CVPR'16
- N Sedaghat, M Zolfaghari, E Amiri, T Brox. Orientation-boosted voxel nets for 3D object recognition. BMVC'17
- B. Graham, M. Engelcke, and L. van der Maaten. 3D semantic segmentation with submanifold sparse convolutional networks. CVPR'18
	- SSCN (submanifold sparse Conv Net)
	- https://github.com/facebookresearch/SparseConvNet
	- SSCN(m, n, f, s): m input, n output, f filter-size, s stride;
	- Implementation: a hash table (https://github.com/sparsehash/sparsehash) and a matrix;
	- **Sparse Voxelized**: applied on Submanifold FCN and U-Nets;
	- CPU-only;
	- Experiments: ShapeNet; NYU depth;
- Oct-tree:
	- **OGN**: M. Tatarchenko, A. Dosovitskiy, and T. Brox. Octree generating networks: Efficient convolutional architectures for high-resolution 3d outputs. ICCV'17
	- P.-S. Wang, Y. Liu, Y.-X. Guo, C.-Y. Sun, and X. Tong. OCNN: Octree-based convolutional neural networks for 3D shape analysis. TOG 2017
		- SOA classification;
- Z. Wang and F. Lu. VoxSegNet: Volumetric CNNs for semantic part segmentation of 3D shapes. TVCG'19
- Z. Wu, X. Wang, D. Lin, D. Lischinski, D. Cohen-Or, and H. Huang. Structure-aware generative network for 3d-shape modeling. TOG'19

## Mesh
- Legacy:
	- M. Tarini, K. Hormann, P. Cignoni, and C. Montani. Polycube-maps. TOG'04
- Graph-NN:
	- J. Bruna, W. Zaremba, A. Szlam, and Y. LeCun. Spectral networks and locally connected networks on graphs. 2013
	- K. Guo, D. Zou, and X. Chen. 3D mesh labeling via deep convolutional neural networks. SIGGRAPH'15
	- M. Defferrard, X. Bresson, and P. Vandergheynst. Convolutional neural networks on graphs with fast localized spectral filtering. NIPS'16 
	- M. M. Bronstein, J. Bruna, Y. LeCun, A. Szlam, and P. Vandergheynst. Geometric deep learning: Going beyond euclidean data. SPM'17
	- N. Verma, E. Boyer, and J. Verbeek. Feastnet: Feature- steered graph convolutions for 3d shape analysis. CVPR'18
		- https://github.com/nitika-verma/FeaStNet
		- https://pdfs.semanticscholar.org/2b19/17cda67f8a741680300a45123eeecae10ce2.pdf
- K. Guo, D. Zou, and X. Chen. 3D mesh labeling via deep convolutional neural networks. SIGGRAPH'15
- A. Sinha, J. Bai, and K. Ramani. Deep learning 3d shape surfaces using geometry images. ECCV'16
- T. Bagautdinov, C. Wu, J. Saragih, P. Fua, and Y. Sheikh. Modeling facial geometry using compositional vaes.
- O. Litany, A. Bronstein, M. Bronstein, and A. Makadia. Deformable shape completion with graph convolutional autoencoders. CVPR'17.
- H. Maron, M. Galun, N. Aigerman, M. Trope, N. Dym, E. Yumer, V. G. Kim, and Y. Lipman. Convolutional neural networks on surfaces via seamless toric covers. 2017.
- P. Wang, Y. Gan, Y. Zhang, and P. Shui. 3D shape segmentation via shape fully convolutional networks. 2017
- Q Tan, L Gao, Y Lai, J Yang and S Xia. Mesh-based Autoencoders for Localized Deformation Component Analysis. 2017
- P. Baque, E. Remelli, F. Fleuret, and P. Fua. Geodesic convolutional shape optimization. 2018
- H. B. Hamu, H. Maron, I. Kezurer, G. Avineri, and Y. Lipman. Multi-chart generative surface modeling. 2018
- **MeshNet**: Y Feng, Y Feng, H You, X Zhao, Y Gao. MeshNet: Mesh Neural Network for 3D Shape Representation. AAAI'19 \
	<img src="/CV-3D/images/3d_input/meshnet.png" alt="drawing" width="600"/>
- **MeshCNN**: Rana Hanocka, Amir Hertz, Noa Fish, Raja Giryes, Shachar Fleishman, Daniel Cohen-Or. MeshCNN: A Network with an Edge. SIGGRAPH'19
	- https://ranahanocka.github.io/MeshCNN/
	- https://github.com/ranahanocka/MeshCNN/

## Multiple 2D Images
- Hang Su, Subhransu Maji, Evangelos Kalogerakis, Erik Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. ICCV'15
	- https://github.com/jongchyisu/mvcnn_pytorch
	- Multi-view pooling
- S. Galliani and K. Schindler. Just look at the image: Viewpoint-specific surface normal prediction for improved multi-view reconstruction. CVPR'16
- B Shi, S Bai, X Bai. DeepPano: Deep Panoramic Representation for 3-D Shape Recognition. SPL'15
- **3D-R2N2**: Christopher B. Choy, Danfei Xu, JunYoung Gwak, Kevin Chen, Silvio Savarese. 3D-R2N2: A Unified Approach for Single and Multi-view 3D Object Reconstruction. ECCV'16
- **Surfacenet**: Ji, M., Gall, J., Zheng, H., Liu, Y., Fang, L. Surfacenet: An end-to-end 3d neural network for multiview stereopsis. ICCV'17
- **LSM**: A. Kar, C. Häne, J. Malik. Learning a multi-view stereo machine. NIPS'17

## Temporal or Multi-3D
- Fast-and-Furious;
- **MinkowskiNet**: Christopher Choy, JunYoung Gwak, and Silvio Savarese. 4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks. CVPR'19
	- 4D-occupancy grid;
	- https://github.com/StanfordVL/MinkowskiEngine
- Xingyu Liu, Mengyuan Yan, Jeannette Bohg. MeteorNet: Deep Learning on Dynamic 3D Point Cloud Sequences. ICCV'19
	- https://sites.google.com/view/meteornet
	- https://github.com/xingyul/meteornet
	- Two grouping: direct v.s. chain-flow-based;
	- Problem setup: classification; semantic segmentation; scene-flow;\
		<img src="/CV-3D/images/3d_input/meteor-net-1.png" alt="drawing" width="400"/>
	- Algorithm:\
		<img src="/CV-3D/images/3d_input/meteor-net-2.png" alt="drawing" width="500"/>
	- Experiments: SOA on Synthia dataset semantic segmentation;

## RGBD
- Saurabh Gupta, Ross Girshick, Pablo Arbelaez, and Jitendra Malik. Learning rich features from rgb-d images for object detection and segmentatio. ECCV'14
- Shuran Song and Jianxiong Xiao. Deep Sliding Shapes for amodal 3D object detection in RGB-D images. CVPR'16

## Implicit Functions
- Legacy:
	- B. Curless and M. Levoy. A volumetric method for building complex models from range images. SIGGRAPH'96
	- **Kinectfusion**: R. A. Newcombe, S. Izadi, O. Hilliges, D. Molyneaux, D. Kim, A. J. Davison, P. Kohi, J. Shotton, S. Hodges, and A. Fitzgibbon. Kinectfusion: Real-time dense surface mapping and tracking. ISMAR'11
- Voxel-based SDF:
	- A. Zeng, S. Song, M. Nießner, M. Fisher, J. Xiao, and T. Funkhouser. 3dmatch: Learning local geometric descriptors from rgb-d reconstructions. CVPR'17
	- **3D-EPN**: A. Dai, C. R. Qi, and M. Nießner,  Shape completion using 3d-encoder-predictor cnns and shape synthesis, CVPR'17
		- https://github.com/angeladai/cnncomplete
	- D. Stutz and A. Geiger. Learning 3d shape completion from laser scan data with weak supervision. CVPR'18
- Point-based SDF:
	- **DeepSDF**: J Park, P Florence, J Straub, R Newcombe, S Lovegrove. DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation. 2019
		- https://github.com/facebookresearch/DeepSDF
- I Cherabier, J Schonberger, M Oswald, M Pollefeys, A Geiger. Learning Priors for Semantic 3D Reconstruction. ECCV'18

## 2D-3D Fusion
- Charles R. Qi, Hao Su, Matthias Nießner, Angela Dai, Mengyuan Yan, Leonidas J. Guibas. Volumetric and Multi-View CNNs for Object Classification on 3D Data. CVPR'16
	- https://github.com/charlesq34/
- Vishakh Hegde, Reza Zadeh. FusionNet: 3D Object Classification Using Multiple Data Representations. NIPS'16

## Touch (Robotics, with grasping, touch)
- M. Bjorkman, Y. Bekiroglu, V. Hogman, and D. Kragic, Enhancing visual perception of shape through tactile glances, IROS 2013.
- 3D Shape Perception from Monocular Vision, Touch, and Shape Priors, Shaoxiong Wang, Jiajun Wu, Xingyuan Sun, Wenzhen Yuan, William T. Freeman, Joshua B. Tenenbaum, and Edward H. Adelson
- W. Yuan, S. Dong, and E. H. Adelson, Gelsight: High-resolution robot tactile sensors for estimating geometry and force, Sensors 2017.