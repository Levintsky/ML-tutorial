# Perception in 3D

## Detection
- BEV + Frontal (Fusion)
	- **MV3D**: X Chen, H Ma, J Wan, B Li, T Xia. Multi-View 3D Object Detection Network for Autonomous Driving. CVPR'17
		- Input: BEV point-clouds, Front-view pc, 2D image;
		- Output: object class, 3D bounding boxes;
		- Generates 3D object proposals from BEV map and project them to three views;
		- Deep fusion network is used to combine region-wise features obtained via ROI pooling for each view;\
			<img src="/Autonomous-Driving/images/detection/mv3d.png" alt="drawing" width="600"/>
- BEV + image:
	- **AVOD**: J Ku, M Mozifian, J Lee, A Harakeh, and S L Waslander. Joint 3d proposal generation and object detection from view aggregation. CoRR'17
		- Input: image + BEV; output: bounding boxes;
		- BEV: [-40, 40] x [0, 70]
		- VGG feature extractor: for both BEV and frontal images + FPN to map back;
		- Multimodal Fusion RPN: 80K - 100K 3D anchors;
		- Two stages like RCNN;
		- Detector;
		- https://github.com/kujason/avod \
			<img src="/Autonomous-Driving/images/detection/avod.png" alt="drawing" width="600"/>
	- M Liang, B Yang, S Wang, and R Urtasun. Deep continuous fusion for multi-sensor 3d object detection. ECCV'18
		- Input: image + BEV; output: 3D bounding box;
		- Lidar: VeloFCN, 3DFCN, DPT;
		- Image + LiDAR: F-Pointnet; (generally project lidar onto image);
		- Key idea: project image onto Lidar;\
			<img src="/Autonomous-Driving/images/detection/cont-fusion.png" alt="drawing" width="450"/>
		- Continuous fusion layer:\
			<img src="/Autonomous-Driving/images/detection/cont-fusion2.png" alt="drawing" width="450"/>
	- **MTMF**: M Liang, B Yang, Y Chen, R Hu, R Urtasun. Multi-Task Multi-Sensor Fusion for 3D Object Detection. CVPR'19
		- Key idea: by solving **multiple perception tasks** jointly, we can learn better feature representations which result in better detection performanc;
		- Input: RGB, LiDAR-BEV; Output: 2D, 3D detection; ground estimation; depth completion;
		- Knowledge about the location of the **ground** can provide useful cues for 3D object detection in the context of self-driving vehicles, as the traffic participants of interest are restrained to this plane;\
		<img src="/Autonomous-Driving/images/detection/mtms-fusion.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/detection/mtms-fusion2.png" alt="drawing" width="600"/>
- BEV:
	- **Pixor**: B Yang, W Luo, and R Urtasun. Pixor: Real-time 3d object detection from point clouds. CVPR'18
		- Key: real-time, proposal free, single-stage Detector (YOLO, SSD);
		- Input: BEV; Output: 2D-oriented bounding box {θ, xc, yc, w, l}, per-pixel prediction;
		- Overall:\
			<img src="/Autonomous-Driving/images/detection/pixor.png" alt="drawing" width="450"/>
		- FCN:\
			<img src="/Autonomous-Driving/images/detection/pixor2.png" alt="drawing" width="450"/>
		- Supervision: angle, box, focal loss;\
			<img src="/Autonomous-Driving/images/detection/pixor3.png" alt="drawing" width="450"/>
		- Experiment: Kitti, TOR4D;
- Frontal view:
	- **VoxelNet**: Y Zhou, O Tuzel. VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection. CVPR'18
		- Input: H x D x W pc;
		- Key idea: voxel; within each voxel: VFE; RPN-based detection;
		- Backbone: feature-learning + Conv-middle layer + RPN;
			- Divides the point cloud into equally spaced 3D voxels;
			- encodes each voxel via stacked VFE layers;
			- then 3D convolution further aggregates local voxel features, transforming the point cloud into a high-dimensional volumetric representation;\
			<img src="/Autonomous-Driving/images/detection/voxel-net.png" alt="drawing" width="600"/>
		- 1. PointNet for each voxel;
		- 2. 3D-Conv on voxels;
		- VFE-layer:\
			<img src="/Autonomous-Driving/images/detection/voxel-net.png" alt="drawing" width="450"/>
		- 3. RPN consumes the volumetric representation and yields the detection result;
		- Experiments: 3D detection from Lidar on KITTI;
- Canonical view:
	- **PointRCNN**: S Shi, X Wang, H Li. PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud. CVPR'19
		- Two stages: RCNN detection for 3D point clouds;
		- https://github.com/sshaoshuai/PointRCNN
		- Comparison with AVOD and f-PointNet;\
			<img src="/Autonomous-Driving/images/detection/point-rcnn1.png" alt="drawing" width="500"/>
		- Stage-1: Bottom-up 3D proposal;
			- 1.1 Point representation: PointNet++ with multi-scale grouping;
			- 1.2 Foreground point segmentation: focal loss; (generally, foreground is much smaller)
			- 1.3 Bin-based 3D bounding box generation: (x, y, z, h, w, l, theta) from BEV; Loss: bin-based coarse + regression-based residual;
			- 1.4 NMS, 300 top proposals;
			- 1.5 Point cloud region pooling;\
			<img src="/Autonomous-Driving/images/detection/point-rcnn2.png" alt="drawing" width="600"/>
		- Stage-2: Canonical 3D bounding box refinement;
			- 2.1 Canonical transformation;
			- 2.2 Feature learning for box proposal refinement;
			- 2.3 Losses for box proposal refinement\
			<img src="/Autonomous-Driving/images/detection/point-rcnn3.png" alt="drawing" width="400"/>
- Range view (cylindrical range images?):
	- **VeloFCN**: B Li, T Zhang, and T Xia. Vehicle detection from 3D lidar using fully convolutional network. RSS'16
	- G Meyer, A Laddha, E Kee, C Vallespi-Gonzalez, Carl K. Wellington. LaserNet: An Efficient Probabilistic 3D Object Detector for Autonomous Driving. CVPR'19
		- 0. Range view;
		- 1. FCN (class probability for each LIDAR point)
		- 2. Mean-shift clustering for points; adaptive-NMS;
	<img src="/Autonomous-Driving/images/detection/laser-net.png" alt="drawing" width="600"/>

## Methodology
- Kernel:
	- S Wang, S Suo, W Ma, A Pokrovsky, R Urtasun. Deep Parametric Continuous Convolutional Neural Networks. CVPR'18
		- key idea: exploit **parameterized kernel** functions that span the full continuous vector space
		- Gaussian kernel: K. T. Schutt, P. Kindermans, H. Sauceda, S. Chmiela, A. Tkatchenko, and K. Muller. Schnet: A continuous-filter convolutional neural network for modeling quantum interactions. 2017\
			<img src="/Autonomous-Driving/images/detection/continuous1.png" alt="drawing" width="500"/>
			<img src="/Autonomous-Driving/images/detection/continuous2.png" alt="drawing" width="600"/>
- Graph NN:
	- D. Boscaini, J. Masci, E. Rodola, and M. Bronstein. Learning shape correspondence with anisotropic convolutional neural networks. NIPS'16
	- X. Qi, R. Liao, J. Jia, S. Fidler, and R. Urtasun. 3d graph neural networks for rgbd semantic segmentation. CVPR'17
	- M. Defferrard, X. Bresson, and P. Vandergheynst. Convolutional neural networks on graphs with fast localized spectral filtering. NIPS'16.
	- F. Monti, D. Boscaini, J. Masci, E. Rodola, J. Svoboda, and M. M. Bronstein. Geometric deep learning on graphs and manifolds using mixture model cnns. CVPR'17.

## Misc
- FaF: Detection, Tracking and Motion Forecasting [CVPR'18, Wenjie];
- OSIS: Identifying Unknown Instances [Kelvin Wong, Shenlong]
	- Unseen: deer, … detect and group the point-clouds
- Exemplar memory module for rare-seen object recognition [Mengfei Liu];
- MultiNet: Real-time Joint Semantic Reasoning for Autonomous Driving [IV’18]

## Detection From 2D
- B Xu and Z Chen. Multi-level fusion based 3d object detection from monocular images. CVPR'18
- Geometry constraint:
	- **MultiBin**: A Mousavian, D Anguelov, J Flynn, and J Kosecka. 3d bounding box estimation using deep learning and geometry. CVPR'17
	- B Li, W Ouyang, L Sheng, X Zeng, and X Wang. Gs3d: An efficient 3d object detection framework for autonomous driving. 2019.

## Fusion (LiDAR + Image)
- Multi-Level Radar Fusion for Perception and Prediction.
	- Insight: Radar has better long-range and speed;
	- Input: radar, lidar
	- Lidar: 
	- Radar: 2D-Conv on raterized image;
	- 1. Point-level fusion: better long-range detection;
	- 2. Detection-level fusion: (Association; Aggregation; Refinement;) better state estimation for tracking and prediction;
	- 3. Track-level fusion: track before detect;
- Y Chen, M Liang, B Yang, R Urtasun. Bi-directional Multi-Sensor Fusion for 3D Perception. Mini-26
	- Input: RGB, LiDAR;
	- MMF: 3D-BEV + 2D;
	- FuseNet: 3D + 2D for depth completion (Uber);
	- Ours: Voxel + 2D;
	- Tasks:

## Detection from 3D Point-Clouds
- 2D as a referral:
	- D Xu, D Anguelov, and A Jain. Pointfusion: Deep sensor fusion for 3d bounding box estimation. CoRR'17
- Voxelize:
	- S Song and J Xiao. Deep sliding shapes for amodal 3d object detection in rgb-d images. CVPR'16
- HDNET: Exploiting HD Maps for 3D Object Detection. B. Yang, M. Liang, R. Urtasun. CoRL'18

## 3D Tracking
- D. Frossard, R. Urtasun. End-to-end Learning of Multi-sensor 3D Tracking by Detection. ICRA'18