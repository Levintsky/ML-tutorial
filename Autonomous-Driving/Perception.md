# Perception

## Detection From 2D
- **BEV** (Bird-Eye View):
	- **AVOD**: J Ku, M Mozifian, J Lee, A Harakeh, and S L Waslander. Joint 3d proposal generation and object detection from view aggregation. CoRR'17
		- BEV: [-40, 40] x [0, 70]
		- VGG feature extractor: for both BEV and frontal images + FPN to map back;
		- Multimodal Fusion RPN: 80K - 100K 3D anchors;
		- Two stages like RCNN;
		- Detector;
		- https://github.com/kujason/avod
		<img src="/Autonomous-Driving/images/avod.png" alt="drawing" width="600"/>

	- M Liang, B Yang, S Wang, and R Urtasun. Deep continuous fusion for multi-sensor 3d object detection. ECCV'18
	- B Yang, W Luo, and R Urtasun. Pixor: Real-time 3d object detection from point clouds. CVPR'18

- Frontal View:
	- **PointRCNN**: S Shi, X Wang, H Li. PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud. CVPR'19
		- 1 Bottom-up 3D proposal;
		- 1.1 Point representation: PointNet++ with multi-scale grouping;
		- 1.2 Foreground point segmentation: focal loss; (generally, foreground is much smaller)
		- 1.3 Bin-based 3D bounding box generation: (x, y, z, h, w, l, theta) from BEV; Loss: bin-based coarse + regression-based residual;
		- 1.4 NMS, 300 top proposals;
		- 1.5 Point cloud region pooling;
		- 2 Canonical 3D bounding box refinement
		- 2.1 Canonical transformation;
		- 2.2 Feature learning for box proposal refinement.
		- 2.3 Losses for box proposal refinement
		<img src="/Autonomous-Driving/images/point-rcnn1.png" alt="drawing" width="500"/>
		<img src="/Autonomous-Driving/images/point-rcnn2.png" alt="drawing" width="600"/>
	- **MultiBin**: A Mousavian, D Anguelov, J Flynn, and J Kosecka. 3d bounding box estimation using deep learning and geometry. CVPR'17
		- **Geometry constraint**: Perspective projection of a 3D bounding box should fit tightly within its 2D detection window
		- Detect 2D bounding box first;
		- Estimate: center T = (tx,ty,tz), dimension D = (dx,dy,dz), rotation R, (R, T) in SE(3), Regress the box dimensions D rather than translation T
		- Point-to-point correspondence constraint:
		- Network structure: backbone CNN outputs feature 512 x 7 x 7, then three heads:
			- orientation: MLP -> bins x 2 for sin, cos
			- confidence: MLP -> bins, loss: cross-entropy
			- dimension: MLP -> 3, loss: MSE
		- Experiments: Kitti, PASCAL-3D;
		<img src="/Autonomous-Driving/images/waymo-multibin1.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/waymo-multibin2.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/waymo-multibin3.png" alt="drawing" width="400"/>

	- X Chen, H Ma, J Wan, B Li, and T Xia. Multi-view 3d object detection network for autonomous driving. CVPR'17
	- B Xu and Z Chen. Multi-level fusion based 3d object detection from monocular images. CVPR'18
- Geometry constraint:
	- **MultiBin**: A Mousavian, D Anguelov, J Flynn, and J Kosecka. 3d bounding box estimation using deep learning and geometry. CVPR'17
	- B Li, W Ouyang, L Sheng, X Zeng, and X Wang. Gs3d: An efficient 3d object detection frame- work for autonomous driving. 2019.

## Semantic Segmentation
- S Wang, S Suo, W Ma, A Pokrovsky, R Urtasun. Deep Parametric Continuous Convolutional Neural Networks. CVPR'18
<img src="/Autonomous-Driving/images/continuous1.png" alt="drawing" width="500"/>
<img src="/Autonomous-Driving/images/continuous2.png" alt="drawing" width="600"/>

## Detection from 3D
- 2D as a referral:
	- C Qi, W Liu, C Wu, H Su, and L Guibas. Frustum pointnets for 3d object detection from RGB-D data. CoRR'17
	- D Xu, D Anguelov, and A Jain. Pointfusion: Deep sensor fusion for 3d bounding box estimation. CoRR'17
- Voxelize:
	- S Song and J Xiao. Deep sliding shapes for amodal 3d object detection in rgb-d images. CVPR'16
	- Y Zhou and O Tuzel. Voxelnet: End-to-end learning for point cloud based 3d object detection. CoRR'17

## Detection from Graph
- Graph NN:
	- **GNN**: F. Scarselli, M. Gori, A. C. Tsoi, M. Hagenbuchner, and G. Monfardini. The graph neural network model. TNN'09
	- **GGNN**: Y. Li, D. Tarlow, M. Brockschmidt, and R. Zemel. Gated graph sequence neural networks. 2015
	- X. Qi, R. Liao, J. Jia, S. Fidler, and R. Urtasun. 3d graph neural networks for rgbd semantic segmentation. CVPR'17
- Graph Convolution Networks:
	- Graph Laplacian
	- J. Bruna, W. Zaremba, A. Szlam, and Y. LeCun. Spectral networks and locally connected networks on graphs. ICLR'14 
	- D. Boscaini, J. Masci, E. Rodola, and M. Bronstein. Learning shape correspondence with anisotropic convolutional neural networks. NIPS'16
	- M. Defferrard, X. Bresson, and P. Vandergheynst. Convolutional neural networks on graphs with fast localized spectral filtering. NIPS'16.
	- F. Monti, D. Boscaini, J. Masci, E. Rodola, J. Svoboda, and M. M. Bronstein. Geometric deep learning on graphs and manifolds using mixture model cnns. CVPR'17.