# 3D Detection and Segmentation

## Benchmarks
- **SUN RGB-D**: Shuran Song, Samuel P Lichtenberg, and Jianxiong Xiao. Sun rgb-d: A rgb-d scene understanding benchmark suite. CVPR'15
	- 10,355 training, 2,860 testing;
- **ScanNet**: Angela Dai, Angel X. Chang, Manolis Savva, Maciej Halber, Thomas Funkhouser and Matthias Nießner. ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes. CVPR'17
- **Matterport3D**: Chang, Angel and Dai, Angela and Funkhouser, Thomas and Halber, Maciej and Niessner, Matthias and Savva, Manolis and Song, Shuran and Zeng, Andy and Zhang, Yinda. Matterport3D: Learning from RGB-D Data in Indoor Environments. 3DV'17
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
	- Dahua Lin, Sanja Fidler, and Raquel Urtasun. Holistic scene understanding for 3d object detection with rgbd cameras. ICCV'13
	- **3D-SIS**: Ji Hou, Angela Dai, and Matthias Nießner. 3D-SIS: 3d semantic instance segmentation of rgb-d scans. CVPR'19

## Input and Backbones
- Summary:
	- PointNet, 3D-Conv, GNN, BEV-2D-Conv
	- 2D: Camera intrinsic and extrinsic info;
	- Hybrid: voxelnet (pointnet + conv3d)
- Legacy (human-designed):
	- **COG**: Cloud of Orientated Gradient feature
		- Zhile Ren and Erik B Sudderth. Three-dimensional object detection and layout prediction using clouds of oriented gradients. CVPR'16
		- Zhile Ren and Erik B Sudderth. 3D Object Detection with Latent Support Surfaces. CVPR'18
- 3D/Sparse-Conv:
	- Sliding Shapes:
		- Shuran Song and Jianxiong Xiao. Sliding shapes for 3d object detection in depth images. ECCV'14
		- Shuran Song and Jianxiong Xiao. Deep sliding shapes for amodal 3d object detection in rgb-d images. CVPR'16
	- Martin Engelcke, Dushyant Rao, Dominic Zeng Wang, Chi Hay Tong, and Ingmar Posner. Vote3Deep: Fast Object Detection in 3D Point Clouds Using Efficient Convolutional Neural Networks. ICRA'17
	- Bo Li. 3D Fully Convolutional Network for Vehicle Detection in Point Cloud. IROS'17
	- **SECOND**: Yan Yan, Yuxing Mao and Bo Li. SECOND: Sparsely Embedded Convolutional Detection. Sensors'18
	- C. Zhang,W. Luo, and R. Urtasun. Efficient convolutions for real-time semantic segmentation of 3d point clouds. 3DV'18
		- Model: voxelize + ResNet;
	- **3D-SIS**: Ji Hou, Angela Dai, and Matthias Nießner. 3D-SIS: 3d semantic instance segmentation of rgb-d scans. CVPR'19
	- **PartA2-Net**: Shi, Shaoshuai and Wang, Zhe and Shi, Jianping and Wang, Xiaogang and Li, Hongsheng. From Points to Parts: 3D Object Detection from Point Cloud with Part-aware and Part-aggregation Network. PAMI'20
		- 3D-conv, compress height, 2d-conv;
	- **3D-MPA**: Francis Engelmann, Martin Bokeloh, Alireza Fathi, Bastian Leibe, Matthias Nießner. Multi Proposal Aggregation for 3D Semantic Instance Segmentation. CVPR'20
	- Mahyar Najibi, Guangda Lai, Abhijit Kundu, Zhichao Lu, Vivek Rathod, Thomas Funkhouser, Caroline Pantofaru, David Ross, Larry S. Davis, Alireza Fathi. DOPS: Learning to Detect 3D Objects and Predict their 3D Shapes. CVPR'20
		- 3D-sparse U-Net;
		- GNN;
	- **GSDN**: JunYoung Gwak, Christopher Choy, Silvio Savarese. Generative Sparse Detection Networks for 3D Single-shot Object Detection. ECCV'20
		- https://github.com/jgwak/GSDN
- PointNet:
	- Qiangui Huang, Weiyue Wang, and Ulrich Neumann. Recurrent Slice Networks for 3D Segmentation of Point Clouds. CVPR'18
	- **Pointrcnn**: Shaoshuai Shi, Xiaogang Wang, and Hongsheng Li. Pointrcnn: 3d object proposal generation and detection from point cloud. CVPR'19
	- **Gspn**: Li Yi, Wang Zhao, He Wang, Minhyuk Sung, and Leonidas Guibas. Gspn: Generative shape proposal network for 3d instance segmentation in point cloud. CVPR'19
		- https://github.com/ericyi/GSPN
	- **STD**: Zetong Yang, Yanan Sun, Shu Liu, Xiaoyong Shen, Jiaya Jia. STD: Sparse-to-Dense 3D Object Detector for Point Cloud. ICCV'19
	- **3DSSD**: Zetong Yang, Yanan Sun, Shu Liu, Jiaya Jia. 3DSSD: Point-based 3D Single Stage Object Detector. CVPR'20
		- https://github.com/Jia-Research-Lab/3DSSD
- GNN/Attention:
	- **MLCVNet**: Qian Xie, Yu-Kun Lai, Jing Wu, Zhoutao Wang, Yiming Zhang, Kai Xu, and Jun Wang. MLCVNet: Multi-Level Context VoteNet for 3D Object Detection. CVPR'20
		- https://github.com/NUAAXQ/MLCVNet
		- Indoor
	- **Point-GNN**: Weijing Shi and Ragunathan (Raj) Rajkumar. Graph Neural Network for 3D Object Detection in a Point Cloud. CVPR'20
- Frontal/BEV 2D backbone:
	- **AVOD**: J Ku, M Mozifian, J Lee, A Harakeh, and S L Waslander. Joint 3d proposal generation and object detection from view aggregation. CoRR'17
		- Input: image + BEV; output: bounding boxes;
		- BEV: [-40, 40] x [0, 70]
		- VGG feature extractor: for both BEV and frontal images + FPN to map back;
	- **MV3D**: X Chen, H Ma, J Wan, B Li, T Xia. Multi-View 3D Object Detection Network for Autonomous Driving. CVPR'17
		- Input: BEV Lidar + Front-view Lidar + 2D image;
		- Output: object class, 3D bounding boxes;
	- **Pixor**: B Yang, W Luo, and R Urtasun. Pixor: Real-time 3d object detection from point clouds. CVPR'18
		- Input: BEV; 800 x 700 x 36 (70m x 80m, rasterized by 0.1m bin)
		- Backbone:
			- 16x downsample, add more layers for details;
			- Similar to FPN, combine feature of different resolution with skip;
	- **FaF**: W. Luo, B. Yang, and R. Urtasun. Fast and furious: Real time end-to-end 3d detection, tracking and motion forecasting with a single convolutional net. CVPR'18
	- **HDNET**: B. Yang, M. Liang, R. Urtasun. HDNET: Exploiting HD Maps for 3D Object Detection. CoRL'18
		- Extend Pixor with HD-Map, which has z0 (ground-level)
		- Then z-z0 as input feature;
	- **Complex-YOLO**: Martin Simon, Stefan Milz, Karl Amende, Horst-Michael Gross. Complex-YOLO: An Euler-Region-Proposal for Real-time 3D Object Detection on Point Clouds. 2018
	- **Pointpillars**: Alex H Lang, Sourabh Vora, Holger Caesar, Lubing Zhou, Jiong Yang, and Oscar Beijbom. Pointpillars: Fast encoders for object detection from point clouds. CVPR'19
	- **CenterPoint**: Tianwei Yin, Xingyi Zhou, Philipp Krähenbühl. Center-based 3D Object Detection and Tracking. NIPS'20
		- https://github.com/tianweiy/CenterPoint
- Range view (cylindrical range images? also 2D?):
	- **VeloFCN**: B Li, T Zhang, and T Xia. Vehicle detection from 3D lidar using fully convolutional network. RSS'16
	- **LaserNet**: G Meyer, A Laddha, E Kee, C Vallespi-Gonzalez, Carl K. Wellington. LaserNet: An Efficient Probabilistic 3D Object Detector for Autonomous Driving. CVPR'19
- **Fusion** 2D/3D:
	- M Liang, B Yang, S Wang, and R Urtasun. Deep continuous fusion for multi-sensor 3d object detection. ECCV'18
		- Unproject 2d image feature to 3d lidar point;
	- **MTMF**: M Liang, B Yang, Y Chen, R Hu, R Urtasun. Multi-Task Multi-Sensor Fusion for 3D Object Detection. CVPR'19
- Hybrid:
	- **VoxelNet**: Y Zhou, O Tuzel. VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection. CVPR'18
		- PointNet for each voxel, encode each voxel with VFE-layer;
		- 3D-Conv on voxels;

## Proposal
- 2-stage (RPN), 1-stage;
- 1-stage, vote for center, then center for box;
	- **SECOND**: Yan Yan, Yuxing Mao and Bo Li. SECOND: Sparsely Embedded Convolutional Detection. Sensors'18
	- **Pixor**: B Yang, W Luo, and R Urtasun. Pixor: Real-time 3d object detection from point clouds. CVPR'18
		- 2D-oriented bounding box {θ, xc, yc, w, l}, per-pixel prediction;
		- Head: upsample x2 twice,
			- 200 x 175 x 1: cross entropy + 200 x 175 x6 {cosθ, sinθ, dx, dy, w, l}
		- Learning: Focal loss on classification for class imbalance;
		- Inference: NMS;
	- **Complex-YOLO**: Martin Simon, Stefan Milz†, Karl Amende, Horst-Michael Gross. Complex-YOLO: An Euler-Region-Proposal for Real-time 3D Object Detection on Point Clouds. 2018
		- E-RPN (Euler): complex number for angle;
	- **HGNet**: Jintai Chen, Biwen Lei, Qingyu Song, Haochao Ying, Danny Z. Chen, Jian Wu. A Hierarchical Graph Network for 3D Object Detection on Point Clouds. CVPR'20
		- GNN backbone, GNN module relation, 1-stage output;
	- **SESS**: Na Zhao, Tat-Seng Chua, Gim Hee Lee. SESS: Self-Ensembling Semi-Supervised 3D Object Detection. CVPR'20
	- **H3DNet**: Zaiwei Zhang, Bo Sun, Haitao Yang, and Qixing Huang. H3DNet: 3D Object Detection Using Hybrid Geometric Primitives. ECCV'20
		- https://github.com/zaiweizhang/H3DNet
		- Extend from VoteNet, predict corner and edge;
		- Proposals from SDF;
- Fancier: interaction between proposals by PointNet/GNN;
	- **3D-MPA**: Francis Engelmann, Martin Bokeloh, Alireza Fathi, Bastian Leibe, Matthias Nießner. Multi Proposal Aggregation for 3D Semantic Instance Segmentation. CVPR'20
- 2-Stage, RPN:
	- **MV3D**: X Chen, H Ma, J Wan, B Li, T Xia. Multi-View 3D Object Detection Network for Autonomous Driving. CVPR'17
		- Generates 3D object proposals from BEV map and project them to three views;
		- Deep fusion network is used to combine region-wise features obtained via ROI pooling for each view;
	- **AVOD**: J Ku, M Mozifian, J Lee, A Harakeh, and S L Waslander. Joint 3d proposal generation and object detection from view aggregation. CoRR'17
	- **VoxelNet**: Y Zhou, O Tuzel. VoxelNet: End-to-End Learning for Point Cloud Based 3D Object Detection. CVPR'18
	- **Pointrcnn**: Shaoshuai Shi, Xiaogang Wang, and Hongsheng Li. Pointrcnn: 3d object proposal generation and detection from point cloud. CVPR'19
		- 10k point, each predict a box;
		- RPN-based refinement;
	- **STD**: Zetong Yang, Yanan Sun, Shu Liu, Xiaoyong Shen, Jiaya Jia. STD: Sparse-to-Dense 3D Object Detector for Point Cloud. ICCV'19
- **RGBD-only** (based on 2D detection):
	- Byung-soo Kim, Shili Xu, and Silvio Savarese. Accurate localization of 3d objects from rgb-d data using segmentation hypotheses. CVPR'13
	- Jean Lahoud and Bernard Ghanem. 2d-driven 3d object detection in rgb-d images. CVPR'17
	- Charles R Qi, Wei Liu, Chenxia Wu, Hao Su, and Leonidas J Guibas. Frustum pointnets for 3d object detection from rgb-d data. CVPR'18
- Segmentation output:
	- C. Zhang,W. Luo, and R. Urtasun. Efficient convolutions for real-time semantic segmentation of 3d point clouds. 3DV'18

## RGB-D Detection
- Viewpoint-dependent detector, pose estimation by clustering 3D:
	- Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Data-driven 3d voxel patterns for object category recognition. CVPR'15
		- Input: 2D images
		- Output: 3DVP, occlusion\
			<img src="/CV-3D/images/detection/3dvp1.png" alt="drawing" width="400"/>
			<img src="/CV-3D/images/detection/3dvp2.png" alt="drawing" width="600"/>
	- Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Subcategory-aware convolutional neural networks for object proposals and detection. WACV'17

## Output/Supervision
- Consistency after transformation:
	- **SESS**: Na Zhao Tat-Seng Chua Gim Hee Lee. SESS: Self-Ensembling Semi-Supervised 3D Object Detection. CVPR'20
- Segmentation
	- Evangelos Kalogerakis, Melinos Averkiou, Subhransu Maji, and Siddhartha Chaudhuri. 3d shape segmentation with projective convolutional networks. CVPR'17
	- **3DMV**: Angela Dai and Matthias Nießner. 3dmv: Joint 3d-multiview prediction for 3d semantic scene segmentation. 2018
	- **3D-SIS**: Ji Hou, Angela Dai, and Matthias Nießner. 3D-SIS: 3d semantic instance segmentation of rgb-d scans. CVPR'19
	- Pham, Q.H., Nguyen, T., Hua, B.S., Roig, G., Yeung, S.K.: Jsis3d: Joint semantic instance segmentation of 3d point clouds with multi-task pointwise networks and multi-value conditional random fields. CVPR'19
	- Wang, X., Liu, S., Shen, X., Shen, C., Jia, J.: Associatively segmenting instances and semantics in point clouds.
- Analysis-by-Synthesis:
	- **Gspn**: Li Yi, Wang Zhao, He Wang, Minhyuk Sung, and Leonidas Guibas. Gspn: Generative shape proposal network for 3d instance segmentation in point cloud. CVPR'19
		- c-VAE to generate the object;

## 3D Object Pose, Keypoints
- R-CNN (ROI, then pose regression):
	- S. Tulsiani and J. Malik. Viewpoints and keypoints. CVPR'15
		- CNN for view points: Nc class x Na angle/instance x Ntheta
		- Multiscale Convolutional Response Maps
		- Viewpoint Conditioned Keypoint Likelihood
		<img src="/CV-3D/images/detection/viewpts_keypts.png" alt="drawing" width="500"/>
- Pat Marion, Peter R. Florence, Lucas Manuelli, and Russ Tedrake. Labelfusion: A pipeline for generating ground truth labels for real rgbd data of cluttered scenes. ICRA'18
- Supasorn Suwajanakorn, Noah Snavely, Jonathan Tompson, and Mohammad Norouzi. Discovery of latent 3d keypoints via end-to-end geometric reasoning. NIPS'18
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
