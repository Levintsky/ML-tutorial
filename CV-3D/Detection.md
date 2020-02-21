# 3D Detection and Segmentation

## 3D Bounding Box from Images
- Viewpoint-dependent detector, pose estimation by clustering 3D:
	- Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Data-driven 3d voxel patterns for object category recognition. CVPR'15
		- Input: 2D images
		- Output: 3DVP, occlusion
		<img src="/CV-3D/images/detection/3dvp1.png" alt="drawing" width="400"/>
		<img src="/CV-3D/images/detection/3dvp2.png" alt="drawing" width="600"/>
	- Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Subcategory-aware convolutional neural networks for object proposals and detection. WACV'17

## 3D Object Pose, Keypoints
- R-CNN (ROI, then pose regression):
	- S. Tulsiani and J. Malik. Viewpoints and keypoints. CVPR'15
		- CNN for view points: Nc class x Na angle/instance x Ntheta
		- Multiscale Convolutional Response Maps
		- Viewpoint Conditioned Keypoint Likelihood
		<img src="/CV-3D/images/detection/viewpts_keypts.png" alt="drawing" width="500"/>
- Pat Marion, Peter R. Florence, Lucas Manuelli, and Russ Tedrake. Labelfusion: A pipeline for generating ground truth labels for real rgbd data of cluttered scenes. ICRA'18
- Wenjie Luo, Bin Yang, and Raquel Urtasun. Fast and furious: Real time end-to-end 3d detection, tracking and motion forecasting with a single convolutional net. CVPR'18
- Supasorn Suwajanakorn, Noah Snavely, Jonathan Tompson, and Mohammad Norouzi. Discovery of latent 3d keypoints via end-to-end geometric reasoning. NIPS'18
- Alex H Lang, Sourabh Vora, Holger Caesar, Lubing Zhou, Jiong Yang, and Oscar Beijbom. Pointpillars: Fast encoders for object detection from point clouds. CVPR'19
- 6D pose of known rigid objects:
	- Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and Dieter Fox. Posecnn: A convolutional neural network for 6d object pose estimation in cluttered scenes. RSS'18
	- Xinke Deng, Arsalan Mousavian, Yu Xiang, Fei Xia, Timothy Bretl, and Dieter Fox. Poserbpf: A rao-blackwellized particle filter for 6d object pose tracking. RSS'19
- 9D of unknown objects:
	- He Wang, Srinath Sridhar, Jingwei Huang, Julien Valentin, Shuran Song, and Leonidas J. Guibas. Normalized object coordinate space for category-level 6d object pose and size estimation. CVPR'19
- Xingyu Liu, Rico Jonschkowski, Anelia Angelova, Kurt Konolige. KeyPose: Multi-view 3D Labeling and Keypoint Estimation for Transparent Objects. CVPR'20
	- TOD dataset;
	- Problem setup: input: stereo camera with known parameters; output 3D keypoints;
	- Algorithm:\
		<img src="/CV-3D/images/detection/tod-1.png" alt="drawing" width="400"/>

## 3D Box from Depth
- S. Song and J. Xiao. Sliding shapes for 3d object detection in depth images. ECCV'14
- S. Song and J. Xiao. Deep sliding shapes for amodal 3d object detection in rgb-d images. ECCV'16
- B. Li. 3d fully convolutional network for vehicle detection in point cloud. IROS'16
- **VeloFCN**: B. Li, T. Zhang, and T. Xia. Vehicle detection from 3d lidar using fully convolutional network. arxiv'16

## 2D-3D Fusion
- A Mousavian, D Anguelov, J Flynn, J Kosecka. 3d bounding box estimation using deep learning and geometry. CVPR'17
- **PointFusion**: D Xu, D Anguelov, A Jain. PointFusion: Deep Sensor Fusion for 3D Bounding Box Estimation. CVPR'18\
	<img src="/CV-3D/images/detection/pointfusion.png" alt="drawing" width="600"/>
	- Input: RGB + 3D point cloud
	- Output: 3 x 8 corner points
	- Global fusion (baseline): (1 x 3072) -> MLP (512, 128, 128) -> 1x8x3 (L1-loss)
	- Dense fusion:
	- STN
	- Experiments: KITTI, AP-3D
- **Frustum PointNet**: C Qi, W Liu, C Wu, H Su, L Guibas. Frustum PointNets for 3D Object Detection from RGB-D Data, CVPR'18
	- RGB-D
	- 2D-detection: 2D bounding boxes;
	- 3D-frustum: FPN; pointnet classification for each point; T-net (STN)
	<img src="/CV-3D/images/3d_input/frustum-pointnet.png" alt="drawing" width="600"/>

## Active Learning
- Li Yi, Vladimir G. Kim, Duygu Ceylan, I-Chao Shen, Mengyan Yan, Hao Su, Cewu Lu, Qixing Huang, Alla Sheffer, Leonidas Guibas. A Scalable Active Framework for Region Annotation in 3D Shape Collections. SIGGRAPH Asia'18
	- Problem setup: per-point human-verified annotations of 3D shapes; reduce human effort;
	- Human task set: Annotation Am, verification Vm;
	- Propagates labels from the annotated shapes to unlabeled ones by exploiting both local geometric features and global shape structure;\
		<img src="/CV-3D/images/detection/active-anno.png" alt="drawing" width="500"/>
	- Goal: optimize utility function N-good / Time;
	- 1.1 Selecting Annotation set: Prediction confidence: similarity between shape sk to its most similar sx + global;
	- 1.2 Selecting Verification set:
	- 2. Human labels: obtaining input;
	- 3. Propagate labels:
