# 3D Detection and Segmentation

## Benchmarks
- **SUN RGB-D**: Shuran Song, Samuel P Lichtenberg, and Jianxiong Xiao. Sun rgb-d: A rgb-d scene understanding benchmark suite. CVPR'15
	- 10,355 training, 2,860 testing;
- **ScanNet**: Angela Dai, Angel X. Chang, Manolis Savva, Maciej Halber, Thomas Funkhouser and Matthias Nießner. 2017. ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes. CVPR'17

## Misc
- Sliding Shapes:
	- Shuran Song and Jianxiong Xiao. Sliding shapes for 3d ob- ject detection in depth images. ECCV'14
	- Shuran Song and Jianxiong Xiao. Deep sliding shapes for amodal 3d object detection in rgb-d images. CVPR'16
- Template-based:
	- Liangliang Nan, Ke Xie, and Andrei Sharf. A search-classify approach for cluttered indoor scene understanding. TOG'12
	- Yangyan Li, Angela Dai, Leonidas Guibas, and Matthias Nießner. Database-assisted object retrieval for real-time 3d reconstruction. CSG'15
	- Or Litany, Tal Remez, Daniel Freedman, Lior Shapira, Alex Bronstein, and Ran Gal. CVIU'17
- Zhile Ren and Erik B Sudderth. Three-dimensional object detection and layout prediction using clouds of oriented gradients. CVPR'16
- Ji Hou, Angela Dai, and Matthias Nießner. 3D-SIS: 3d semantic instance segmentation of rgb-d scans. arxiv'18
- Li Yi, Wang Zhao, He Wang, Minhyuk Sung, and Leonidas Guibas. Gspn: Generative shape proposal network for 3d instance segmentation in point cloud. arxiv'18
- **Pointrcnn**: Shaoshuai Shi, Xiaogang Wang, and Hongsheng Li. Pointrcnn: 3d object proposal generation and detection from point cloud. arxiv'18

## BEV
- Check AV;

## RGB-D 3D Bounding Box from Images
- Dahua Lin, Sanja Fidler, and Raquel Urtasun. Holistic scene understanding for 3d object detection with rgbd cameras. ICCV'13
- Reduce search space by 2D:
	- Byung-soo Kim, Shili Xu, and Silvio Savarese. Accurate localization of 3d objects from rgb-d data using segmenta- tion hypotheses. CVPR'13
	- Jean Lahoud and Bernard Ghanem. 2d-driven 3d object detection in rgb-d images. CVPR'17
	- Charles R Qi, Wei Liu, Chenxia Wu, Hao Su, and Leonidas J Guibas. Frustum pointnets for 3d object detection from rgb-d data. CVPR'18
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

## 2D-3D Fusion
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
