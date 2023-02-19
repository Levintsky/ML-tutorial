# 3D Detection and Segmentation

## Benchmarks
- SUN RGB-D: CVPR'15
	- 10,355 training, 2,860 testing;
- ScanNet: CVPR'17
- Matterport3D: 3DV'17
	- RGB-D indoor Environment;

## Codebase
- Libraries:
	- OpenPCDet: https://github.com/open-mmlab/OpenPCDet
		- Support: PointRCNN, second, pointpillar, Part-A2, PV-RCNN;
		- spconv
	- Minkowski Engine:
- 3D-SIS: https://github.com/Sekunde/3D-SIS
- SECOND: https://github.com/traveller59/second.pytorch
- Tensorflow:
	- GSPN: https://github.com/ericyi/GSPN

## Misc
- Template-based:
	- Liangliang Nan, Ke Xie, and Andrei Sharf. A search-classify approach for cluttered indoor scene understanding. TOG'12
	- Yangyan Li, Angela Dai, Leonidas Guibas, and Matthias Nießner. Database-assisted object retrieval for real-time 3d reconstruction. CSG'15
	- **ASIST**: Or Litany, Tal Remez, Daniel Freedman, Lior Shapira, Alex Bronstein, and Ran Gal. ASIST: Automatic Semantically Invariant Scene Transformation. CVIU'17
- B. Li. 3d fully convolutional network for vehicle detection in point cloud. IROS'16
	- 3D Box from Depth

## Input
- Point-cloud only;
- RGBD:
	- D Lin, S Fidler, and R Urtasun. Holistic scene understanding for 3d object detection with rgbd cameras. ICCV'13
	- 3D-SIS: CVPR'19

## Input and Backbones
- Summary:
	- PointNet, 3D-Conv, GNN, BEV-2D-Conv
	- 2D: Camera intrinsic and extrinsic info;
	- Hybrid: voxelnet (pointnet + conv3d)
- General idea:
	- Downsample/UNet + FPN;
	- 2d/3d Fusion: project/unproject;
- Input:
	- Frontal-View:
	- BEV:
	- Range-View: VeloFCN, Baidu [RSS'16]; LaserNet CVPR'19;
	- 2D + 3D fusion:
		- Uber: Multi-Senor [CVPR'18]; MTMF [CVPR'19]
		- MV3D: Baidu. CVPR'17
- Preprocessing:
	- Pointpillars: CVPR'19
- Legacy (human-designed):
	- COG: Cloud of Orientated Gradient feature
		- Z Ren and E Sudderth. Three-dimensional object detection and layout prediction using clouds of oriented gradients. CVPR'16
		- Z Ren and E Sudderth. 3D Object Detection with Latent Support Surfaces. CVPR'18
- 3D/Sparse-Conv:
	- Sliding Shapes:
		- S Song and J Xiao. Sliding shapes for 3d object detection in depth images. ECCV'14
		- S Song and J Xiao. Deep sliding shapes for amodal 3d object detection in rgb-d images. CVPR'16
	- M Engelcke, D Rao, D Wang, C H Tong, and I Posner. Vote3Deep: Fast Object Detection in 3D Point Clouds Using Efficient Convolutional Neural Networks. ICRA'17
	- B Li. 3D Fully Convolutional Network for Vehicle Detection in Point Cloud. IROS'17
	- SECOND: Bo Li. [Sensors'18]
	- C. Zhang, W. Luo, and R. Urtasun. Efficient convolutions for real-time semantic segmentation of 3d point clouds. 3DV'18
		- Model: voxelize + ResNet;
	- 3D-SIS CVPR'19
	- PartA2-Net: CUHK [PAMI'20]
		- 3D-conv + compress height + 2d-conv;
	- **3D-MPA**: F Engelmann, M Bokeloh, A Fathi, B Leibe, M Nießner. Multi Proposal Aggregation for 3D Semantic Instance Segmentation. CVPR'20
	- DOPS: Learning to Detect 3D Objects and Predict their 3D Shapes. CVPR'20
		- 3D-sparse-U-Net + GNN;
	- GSDN [ECCV'20]: https://github.com/jgwak/GSDN
- PointNet:
	- Q Huang, W Wang, and U Neumann. Recurrent Slice Networks for 3D Segmentation of Point Clouds. CVPR'18
	- Pointrcnn [CVPR'19]
	- **Gspn**: L Guibas. Gspn: Generative shape proposal network for 3d instance segmentation in point cloud. CVPR'19
		- https://github.com/ericyi/GSPN
	- STD: Jiaya Jia.  ICCV'19
	- 3DSSD: Jiaya Jia. CVPR'20
	- 3Detr: ICCV'21
		- https://github.com/facebookresearch/3detr
		- Encoder:
			- Atomic layer: linear embed src to k, q, v, where k, q has pos-enc; then residual layer src+attn(); (optional: followed by linear, dropout, norm);
			- Encoder: clones of atomic, support mask (by fps);
		- Decoder:
			- Atomic layer: linear embed src to k, q, v, where k, q has pos-enc; then residual layer src+attn(); (optional: followed by linear, dropout, norm);
			- Decoder: N point feat, B query, predict B features then 3D bounding boxes;
		- Pipeline:
			- Run Encoder to get enc_xyz, enc_feat;
			- Get query embeddings by fps to get query_xyz, query_embed;
			- Position embedding: enc_pos with sine, cos to get enc_pos;
- GNN/Attention:
	- MLCVNet: CVPR'20; Point-GNN: CVPR'20
- Frontal/BEV 2D backbone:
	- AVOD: CoRR'17
	- Uber: Pixor [CVPR'18], FaF [CVPR'18], HDNET [CoRL'18] Add map;
	- **Complex-YOLO**: M Simon, S Milz, K Amende, H Gross. Complex-YOLO: An Euler-Region-Proposal for Real-time 3D Object Detection on Point Clouds. 2018
	- **CenterPoint**: T Yin, X Zhou, P Krähenbühl. Center-based 3D Object Detection and Tracking. NIPS'20
		- https://github.com/tianweiy/CenterPoint
- Hybrid:
	- VoxelNet [CVPR'18]: PointNet in voxel + 3D-Conv on voxels;

## Proposal/Superivion
- Basics:
	- 3D axis-aligned boxes + angle θ;
	- Focal loss, NMS, ...
	- Box proposals interaction: GNN/tranasformer
- 2-stage (RPN), 1-stage;
- 1-stage, vote for center, then center for box;
	- SECOND: [Sensors'18], SESS [CVPR'20], H3DNet [ECCV'20]
	- Pixor [CVPR'18]
	- **Complex-YOLO**: Martin Simon, Stefan Milz, Karl Amende, Horst-Michael Gross. Complex-YOLO: An Euler-Region-Proposal for Real-time 3D Object Detection on Point Clouds. 2018
		- E-RPN (Euler): complex number for angle;
	- **HGNet**: J Chen, B Lei, Q Song, H Ying, D Chen, J Wu. A Hierarchical Graph Network for 3D Object Detection on Point Clouds. CVPR'20
		- GNN backbone, GNN module relation, 1-stage output;
- 2-Stage, RPN:
	- MV3D: X Chen, H Ma, J Wan, B Li, T Xia. Multi-View 3D Object Detection Network for Autonomous Driving. CVPR'17
		- Generates 3D object proposals from BEV map and project them to three views;
		- Deep fusion network is used to combine region-wise features obtained via ROI pooling for each view;
	- **AVOD**: J Ku, M Mozifian, J Lee, A Harakeh, and S L Waslander. Joint 3d proposal generation and object detection from view aggregation. CoRR'17
	- VoxelNet: Apple [CVPR'18]
	- Pointrcnn: CUHK [CVPR'19]
		- 10k point, each predict a box;
		- RPN-based refinement;
	- STD: Jiaya Jia. STD: Sparse-to-Dense 3D Object Detector for Point Cloud. ICCV'19
- 2D detection superivision:
	- B Kim, S Xu, and Silvio Savarese. Accurate localization of 3d objects from rgb-d data using segmentation hypotheses. CVPR'13
	- J Lahoud and B Ghanem. 2d-driven 3d object detection in rgb-d images. CVPR'17
	- Frustum-Net: CVPR'18
- Segmentation:
	- C. Zhang, W Luo, and R. Urtasun. Efficient convolutions for real-time semantic segmentation of 3d point clouds. 3DV'18
	- E Kalogerakis, et.al. 3d shape segmentation with projective convolutional networks. CVPR'17
	- 3DMV: 2018
	- 3D-SIS [CVPR'19]
	- Pham, Q.H., Nguyen, T., Hua, B.S., Roig, G., Yeung, S.K.: Jsis3d: Joint semantic instance segmentation of 3d point clouds with multi-task pointwise networks and multi-value conditional random fields. CVPR'19
	- Wang, X., Liu, S., Shen, X., Shen, C., Jia, J.: Associatively segmenting instances and semantics in point clouds.
- Box proposals interaction:
	- 3D-MPA: M Nießner. Multi Proposal Aggregation for 3D Semantic Instance Segmentation. CVPR'20
- Extra superivison:
	- Box primitives: H3DNet [ECCV'20]
		- https://github.com/zaiweizhang/H3DNet
		- Extend from VoteNet, predict corner and edge;
		- Proposals from SDF;
- Analysis-by-Synthesis:
	- **Gspn**: L Guibas. Gspn: Generative shape proposal network for 3d instance segmentation in point cloud. CVPR'19
		- c-VAE to generate the object;
- Consistency after transformation:
	- SESS [CVPR'20]

## RGB-D Detection
- Viewpoint-dependent detector, pose estimation by clustering 3D:
	- Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Data-driven 3d voxel patterns for object category recognition. CVPR'15
		- Input: 2D images
		- Output: 3DVP, occlusion\
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
- P Marion, P Florence, L Manuelli, and R Tedrake. Labelfusion: A pipeline for generating ground truth labels for real rgbd data of cluttered scenes. ICRA'18
- S Suwajanakorn, N Snavely, J Tompson, and M Norouzi. Discovery of latent 3d keypoints via end-to-end geometric reasoning. NIPS'18
- 6D pose of known rigid objects:
	- Y Xiang, T Schmidt, V Narayanan, and D Fox. Posecnn: A convolutional neural network for 6d object pose estimation in cluttered scenes. RSS'18
	- X Deng, A Mousavian, Y Xiang, F Xia, Timothy Bretl, and Dieter Fox. Poserbpf: A rao-blackwellized particle filter for 6d object pose tracking. RSS'19
- 9D of unknown objects:
	- L Guibas. Normalized object coordinate space for category-level 6d object pose and size estimation. CVPR'19
- X Liu, R Jonschkowski, A Angelova, K Konolige. KeyPose: Multi-view 3D Labeling and Keypoint Estimation for Transparent Objects. CVPR'20
	- TOD dataset;
	- Problem setup: input: stereo camera with known parameters; output 3D keypoints;
	- Algorithm:\
		<img src="/CV-3D/images/detection/tod-1.png" alt="drawing" width="400"/>

## Active Learning
- L Yi, L Guibas. A Scalable Active Framework for Region Annotation in 3D Shape Collections. SIGGRAPH Asia'18