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

## Misc
- Kelvin Wong, Shenlong Wang, Mengye Ren, and Raquel Urtasun. Identifying Unknown Instances for Autonomous Driving. CoRL'19
	- Unseen: deer, ... detect and group the point-clouds

## Detection From 2D
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