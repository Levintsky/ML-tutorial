# Perception in 3D

## Basics
- Input (mainly Lidar)
- Mainly 3 types of models:
	- BEV: fast, make use of z (height) at most 2 meters; most popular in company;
	- GNN/Attention: e.g., DGCNN, Transformer...; no perfect support on Cuda, so slower;
	- Sparse-Conv: strong at public benchmarks;
- (HD)-Map:
	- Ground height information: as offset for z;
	- Semantic meaning (different lanes): e.g., cars in different directions will not interact;
	- Generally we need larger receptive field;
- Fusion (Lidar, image, radar):
	- Image feature to point cloud: "paste" the feature by unprojection;
	- Image feature to BEV/Voxel: GNN/bilinear interpolation;
	- Radar is more noisy and sparse, but larger range with speed, great for prediction;
- Taste:
	- Different from 2D, BEV/3D signal does not have large scale variation;
	- Multi-scale is very important in 2D detection;

## Survey
- Eduardo Arnold, Omar YAl-Jarrah, Mehrdad Dianati, Saber Fallah, David Oxtoby, and Alex Mouzakitis. A Survey on 3D Object Detection Methods for Autonomous Driving Applications. T-ITS'19

## Detection
- BEV + Frontal (Fusion)
	- **MV3D**: X Chen, H Ma, J Wan, B Li, T Xia. Multi-View 3D Object Detection Network for Autonomous Driving. CVPR'17
		- Input: BEV Lidar, Front-view Lidar, 2D image;
		- Output: object class, 3D bounding boxes;
		- Generates 3D object proposals from BEV map and project them to three views;
		- Deep fusion network is used to combine region-wise features obtained via ROI pooling for each view;\
			<img src="/Autonomous-Driving/images/detection/mv3d.png" alt="drawing" width="600"/>
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
		- Insight: unproject image onto Lidar to improve performance;
		- Input: image + BEV; output: 3D bounding box;
		- Lidar: VeloFCN, 3DFCN, DPT;
		- Image + LiDAR: F-Pointnet; (generally project lidar onto image);\
			<img src="/Autonomous-Driving/images/detection/cont-fusion.png" alt="drawing" width="450"/>
		- Continuous fusion layer:\
			<img src="/Autonomous-Driving/images/detection/cont-fusion2.png" alt="drawing" width="450"/>
	- **MTMF**: M Liang, B Yang, Y Chen, R Hu, R Urtasun. Multi-Task Multi-Sensor Fusion for 3D Object Detection. CVPR'19
		- Key idea: by solving **multiple perception tasks** jointly, we can learn better feature representations which result in better detection performance;
		- Input: RGB, LiDAR-BEV; Output: 2D, 3D detection; ground estimation; depth completion;
		- Knowledge about the location of the **ground** can provide useful cues for 3D object detection in the context of self-driving vehicles, as the traffic participants of interest are restrained to this plane;\
		<img src="/Autonomous-Driving/images/detection/mtms-fusion.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/detection/mtms-fusion2.png" alt="drawing" width="600"/>
	- Y Chen, M Liang, B Yang, R Urtasun. Bi-directional Multi-Sensor Fusion for 3D Perception.
		- Input: RGB, LiDAR;
		- MMF: 3D-BEV + 2D;
		- FuseNet: 3D + 2D for depth completion (Uber);
		- Ours: Voxel + 2D;
		- Tasks:
- BEV:
	- **Pixor**: B Yang, W Luo, and R Urtasun. Pixor: Real-time 3d object detection from point clouds. CVPR'18
		- Key: real-time, proposal free, single-stage Detector (YOLO, SSD);
		- Input: BEV; 800 x 700 x 36 (70m x 80m, rasterized by 0.1m bin)
		- Output: 2D-oriented bounding box {θ, xc, yc, w, l}, per-pixel prediction;
		- Backbone:
			- 16x downsample, add more layers for details;
			- Similar to FPN, combine feature of different resolution with skip;
		- Head: upsample x2 twice,
			- 200 x 175 x 1: cross entropy + 200 x 175 x6 {cosθ, sinθ, dx, dy, w, l}
		- Training:
			- Learning: Focal loss on classification for class imbalance;
			- Inference: NMS;
		- Overall:\
			<img src="/Autonomous-Driving/images/detection/pixor.png" alt="drawing" width="450"/>
		- FCN:\
			<img src="/Autonomous-Driving/images/detection/pixor2.png" alt="drawing" width="450"/>
		- Supervision: angle, box, focal loss;\
			<img src="/Autonomous-Driving/images/detection/pixor3.png" alt="drawing" width="450"/>
		- Experiment: Kitti, TOR4D; **28 fps**;
		- AP: area under precision recall;
	- **FaF**: W. Luo, B. Yang, and R. Urtasun. Fast and furious: Real time end-to-end 3d detection, tracking and motion forecasting with a single convolutional net. CVPR'18
		- Insight: **PIXOR** + tracking + prediction;
		- Input: 4D tensor from BEV 3D LiDAR (144 × 80m / 0.2m/bin), previous 5 timesteps;
		- Output: 1. 3D detection; 2. tracking; 3. motion forecasting; (predict next 1 sec; no intent;)
		- Model:
			- Early/late fusion on 5 frames: tradeoff between speed (early is fast) and accuracy;
			- SSD-like one-stage detection: multi-boxes each location; different aspect ratio;
			- Tracking by detection: decoding tracklets;
		- Supervision:
			- Binary cross-entropy classification loss;
			- Regression-loss: find correspondence first (IoU > 0.4 with ground truth), 
		<img src="/Autonomous-Driving/images/prediction/faf.png" alt="drawing" width="500"/>
	- B. Yang, M. Liang, R. Urtasun. HDNET: Exploiting HD Maps for 3D Object Detection. CoRL'18
		- HD-Map: has z0 (ground-level)
		- Then z-z0 as input feature;
	- **IntentNet**: S Casas, W Luo, R Urtasun. IntentNet: Learning to Predict Intention from Raw Sensor Data. CoRL'18
		- Insight: **Improve on FaF with HDMap**;
		- Input: 1. 3D point cloud; (BEV) stack time on height; 2. dynamic maps;
		- Output: 1. trajectory regression; (a sequence of bounding boxes); 2. high level actions (keep lane, turn left/right, left/right lane change, stopping, stopped, parked)
		- Output head: 1. detection branch; (anchors) 2. intention branch; 3. intention as an embedding for motion estimation/regression;
		- **Two-stream + Late fusion**: predict probability of being a vehicle; predict bounding box into the future;
		- Predicts: detection scores for vehicle and background classes, high level action probabilities corresponding to discrete intention, and bounding box regressions in the current and future time steps to represent the intended trajectory;\
			<img src="/Autonomous-Driving/images/prediction/intentnet.png" alt="drawing" width="600"/>
	- **SPAGNN**: Sergio Casas, Cole Gulino, Renjie Liao, Raquel Urtasun. SPAGNN: Spatially-Aware Graph Neural Networks for Relational Behavior Forecasting from Sensor Data. ICRA'20
		- Insight: Improve on FaF and IntentNet with GraphNN + GaBP to handle interaction.\
			<img src="/Autonomous-Driving/images/prediction/spagnn.png" alt="drawing" width="600"/>
	- **STINet**: Zhishuai Zhang, Jiyang Gao, Junhua Mao, Yukai Liu, Dragomir Anguelov, Congcong Li. STINet: Spatio-Temporal-Interactive Network for Pedestrian Detection and Trajectory Prediction. CVPR'20
		- Problem: preception + tracking (previous frames) + prediction from BEV for pedestrian;
		- Model: T-RPN\
			<img src="/Autonomous-Driving/images/detection/stinet-1.png" alt="drawing" width="500"/>
		- Backbone: ResUNet\
			<img src="/Autonomous-Driving/images/detection/stinet-2.png" alt="drawing" width="400"/>
		- Past + trajejory as feature, GNN for interaction:\
			<img src="/Autonomous-Driving/images/detection/stinet-3.png" alt="drawing" width="400"/>
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
	- **LaserNet**: G Meyer, A Laddha, E Kee, C Vallespi-Gonzalez, Carl K. Wellington. LaserNet: An Efficient Probabilistic 3D Object Detector for Autonomous Driving. CVPR'19
		- 0. Range view;
		- 1. FCN (class probability for each LIDAR point)
		- 2. Mean-shift clustering for points; adaptive-NMS;
		<img src="/Autonomous-Driving/images/detection/laser-net.png" alt="drawing" width="600"/>

## Lidar Segmentation
- C. Zhang,W. Luo, and R. Urtasun. Efficient convolutions for real-time semantic segmentation of 3d point clouds. 3DV'18
	- Model: voxelize + ResNet;

## Misc
- OSIS: Identifying Unknown Instances [Kelvin Wong, Shenlong]
	- Unseen: deer, ... detect and group the point-clouds
- Exemplar memory module for rare-seen object recognition [Mengfei Liu];

## Detection From 2D
- May need (estimate)
	- Camera intrinsic and extrinsic info;
- B Xu and Z Chen. Multi-level fusion based 3d object detection from monocular images. CVPR'18
	- Insight: estimate depth first, then 3D detection;
- Geometry constraint:
	- **MultiBin**: A Mousavian, D Anguelov, J Flynn, and J Kosecka. 3d bounding box estimation using deep learning and geometry. CVPR'17
		- 2D bounding box first, then 3D;
	- B Li, W Ouyang, L Sheng, X Zeng, and X Wang. Gs3d: An efficient 3d object detection framework for autonomous driving. 2019.

## Radar
- Multi-Level Radar Fusion for Perception and Prediction.
	- Insight: Radar has better long-range and speed;
	- Input: radar, lidar
	- Lidar: 
	- Radar: 2D-Conv on raterized image;
	- 1. Point-level fusion: better long-range detection;
	- 2. Detection-level fusion: (Association; Aggregation; Refinement;) better state estimation for tracking and prediction;
	- 3. Track-level fusion: track before detect;

## Detection from 3D Point-Clouds
- **PointFusion**: D Xu, D Anguelov, A Jain. PointFusion: Deep Sensor Fusion for 3D Bounding Box Estimation. CVPR'18\
	<img src="/CV-3D/images/detection/pointfusion.png" alt="drawing" width="600"/>
	- Input: RGB + 3D point cloud
	- Output: 3 x 8 corner points
	- Global fusion (baseline): (1 x 3072) -> MLP (512, 128, 128) -> 1x8x3 (L1-loss)
	- Dense fusion:
	- STN
	- Experiments: KITTI, AP-3D
- Voxelize:
	- S Song and J Xiao. Deep sliding shapes for amodal 3d object detection in rgb-d images. CVPR'16

## 3D Tracking
- D. Frossard, R. Urtasun. End-to-end Learning of Multi-sensor 3D Tracking by Detection. ICRA'18