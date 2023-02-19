# 3D Reconstruction

## Basics
- Problem definition:
	- Shape from X:
		- Shape from shading: Photometric stereo: control light sources;
		- Shape from texture: Assume: regular textures;
		- Shape from focus: from blur;
	- SLAM:
		- Input: real-time ordered images;
		- Output: 6-DOF camera (localization); 3D-reconstruction (mapping);
	- SfM:
		- Input: unordered images; no time constraint;
		- Output: camera pose; sparse 3D points;
	- Visual Odometry:
		- Input: images from single/multiple cameras;
		- Output: camera path only (x, y, z, θ1, θ2, θ3) Euler Angles
		- Local consistency, can be a building block of a V-SLAM;
	- MVS:
		- Input: images, known camera poses;
		- Output: dense 3D reconstruction;
- Resources
	- https://github.com/openMVG/awesome_3DReconstruction_list
	- **COLMAP** (SOA): Structure-from-Motion Revisited. CVPR'16
	- **COLMAP** (SOA): Pixelwise View Selection for Unstructured Multi-View Stereo. ECCV'16
		- https://colmap.github.io/

## Realtime Dense Geometry
- Stühmer, Gumhold, Cremers, DAGM 2010

## SFM
- Basics:
	- 1. Feature extraction;
	- 2. Feature matching;
	- 3. Graph construction (one node for each image/camera?)
	- 4. Loop consistency, bundle adjustment;
	- Generally **sparse** reconstruction;
	- Offline;
- Build Rome in a Day (UW)
	- Feature matching, epipolar geometry: {f, h, R, t}
		- Matching efficiency (pairwise costly!): scalable recognition with a vocabulary tree (CVPR’06, David Nister);
		- Erroneous matches: Loop consistency: Christopher Zach CVPR’10: R12 * R23* R31 = I
- Software case study: OpenSfM (in Python)
	- Input: images; output: camera pose (para, position), sparse 3D points;
	- HA-HOG; (rgb2gray, cv2 -> features.extract_features, save at ./features);
	- Mask features? (a few hundreds out of 4000+)
	- Matching image pairs; Pair matching (8 processes)
	- Merge features onto tracks; (create_tracks.py, take matches, create ./tracks.csv)
	- Incremental reconstruction;
	- Triangulation;
	- Ceres solver;
	- Undistort the image;
	- Compute neighbors;
	- Clean/Prune/Merge depthmap;
	- Start a server to visualize;

## MVS
- Basics:
	- Input: calibrated images;
	- Output: **dense** 3D reconstruction;
- Y Furukawa, C Hernández. Multi-View Stereo: A Tutorial. 2015
	- Collect images;
	- Camera parameter for each image;
	- Reconstruct 3D geometry;
	- Bundle adjustment: fuse more info (GPS, IMU, ...) in your cost function;
	- Camera parameter known?
		- Known: 1D search, with epipolar constraint;
		- Unknown: 2D search, optical flow first?
	- Photo consistency: SSD, SAD, NCC, Census, Rank, MI;
	- Space Carving: remove all voxels not photo-consistent;
	- Visual hull?
	- Region growing MVS;
	- Depth-map fusion for MVS;
	- Fast multi-frame stereo scene flow with motion segmentation;
- Google Street View: Capturing the World at Street Level
	- Chevy van: side- and front facing laser scanner; 2 x high-speed video cameras; 8 x camera (Rosette configuration);
- Pose optimization: http://code.google.com/p/gpo/wiki/GPO
- Align the pose to the road network;

## Depth Fusion
- Basics:
	- Input: a bunch of depth images (noisy with holes)
	- Output: nice depth;
	- Real-time (with GPU);
	- Support object moving (scene change);
	- RGB not used in KinectFusion;
- Legacy:
	- Brian Curless and Marc Levoy. A Volumetric Method for Building Complex Models from Range Images. '96
- Pose alignment + 3D:
	- J. Chen, D. Bautembach, and S. Izadi. Scalable real-time volumetric surface reconstruction.
- **KinectFusion**: R Newcombe, S Izadi, O Hilliges, D Molyneaux, D Kim, A Davison, P Kohli, J Shotton, S Hodges, A Fitzgibbon. KinectFusion: Real-Time Dense Surface Mapping and Tracking, ISMAR 2011;
	- Key novelty: 30Hz tracking;
	- https://blog.csdn.net/tanmengwen/article/details/9231297
	- https://docs.opencv.org/master/d8/d1f/classcv_1_1kinfu_1_1KinFu.html (opencv)
	- Real-time volumetric reconstruction; 6DOF pose;
	- Input: 640 x 480 depth maps; output voxels;
	- Steps:
		- 1. Surface measurement (pre-processing): depth map to dense vertex map, normal map;
		- 2. Sensor pose estimation: live sensor tracking with multi-scale ICP; energy minization with good init and try to match surface and normal;
		- 3. Surface reconstruction update: global scene fusion, produce TSDF on voxel space;
		- 4. Surface prediction: ray-casting on new TSDF; close the loop between mapping and localisation;
	<img src="/CV-3D/images/reconstruction/kinect-fusion.png" alt="drawing" width="500"/>
- J. Chen, D. Bautembach, and S. Izadi. Scalable real-time volumetric surface reconstruction. TOG'12
	- Improve on KinectFusion by octree, to make voxel sdf more efficient;
- **Voxel-Block-Hashing**: M Nießner, M Zollhofer, S Izadi, M Stamminger. Real-time 3D Reconstruction at Scale using Voxel Hashing. SIGGRAPH'13
	<img src="/CV-3D/images/reconstruction/voxel-hashing1.png" alt="drawing" width="500"/>
	<img src="/CV-3D/images/reconstruction/voxel-hashing2.png" alt="drawing" width="500"/>
- **ElasticFusion**:
	- T. Whelan, S. Leutenegger, R. F. Salas-Moreno, B. Glocker and A. J. Davison. ElasticFusion: Dense SLAM Without A Pose Graph. RSS '15
	- T. Whelan, R. F. Salas-Moreno, B. Glocker, A. J. Davison and S. Leutenegger. ElasticFusion: Real-Time Dense SLAM and Light Source Estimation. IJRR '16
	- https://github.com/mp3guy/ElasticFusion
- O. Kahler, V. A. Prisacariu, C. Y. Ren, X. Sun, P. Torr, and D. Murray. Very high frame rate volumetric integration of depth images on mobile devices. TVCG'15
- **SemanticFusion**: SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks. 2016
	- Combine ElasticFusion and CNN;
	- https://github.com/seaun163/semanticfusion
	<img src="/CV-3D/images/reconstruction/semanticfusion.png" alt="drawing" width="500"/>

## Depth Estimation
- Single view:
	- D. Eigen, C. Puhrsch, and R. Fergus. Depth map prediction from a single image using a multi-scale deep network. NIPS'14
		- Estimate depth up to an unknown scale factor;
	- D. Eigen and R. Fergus. Predicting depth, surface normals and semantic labels with a common multi-scale convolutional architecture. ICCV'15
	- R. Garg, V. Kumar BG, and I. Reid. Unsupervised CNN for single view depth estimation: Geometry to the rescue. ECCV'16
	- **MonoDepth**: C. Godard, O. Mac Aodha, and G. J. Brostow. Unsupervised monocular depth estimation with left-right consistency. CVPR'17
		- Insight: **Self-Supervision**; no gt required in training; disp estimated can directly applied;
		- https://github.com/mrharicot/monodepth (TF); https://github.com/OniroAI/MonoDepth-PyTorch (pytorch);
		- Supervision:
			- Appearance matching loss (ap): SSIM
			- Disparity Smoothness loss (ds): l1;
			- L-R Disparity Consistency Loss; (warping)
	- **DORN**: H. Fu, M. Gong, C. Wang, K. Batmanghelich, and D. Tao. Deep ordinal regression network for monocular depth estimation. CVPR'18
		- Key insight: ordinal prediction; ASPP; dilated conv;
		- https://github.com/hufu6371/DORN
		<img src="/CV-3D/images/reconstruction/dorn.png" alt="drawing" width="600"/>
	- **MonoDepth-v2**: C Godard, O Aodha, M Firman and G Brostow. Digging Into Self-Supervised Monocular Depth Estimation. ICCV'19
		- https://github.com/nianticlabs/monodepth2
- **Multi-view/video supervised**:
	- **DeMoN**: B Ummenhofer, H Zhou, J Uhrig, N Mayer, E Ilg, A Dosovitskiy, T Brox. DeMoN: Depth and Motion Network for Learning Monocular Stereo. CVPR'17
		- Insight: depth est from two images; progressive refine; mixing synthetic and real-world is important;
		- https://github.com/lmb-freiburg/demon (TF); https://github.com/cvfish/pytorch_demon.git (Pytorch)
		- Input: two images; Output: depth, camera motion;
		- Bootstrap net:
			- Flow from flow-block(image-pair), image only init;
			- Initial depth, normal and camera pose (R, t) from image pairs;
		- Iterative net x 3:
			- Flow refine: flow-block(image-pair, im2, intrinsics, prev-prediction)
			- Depth, normal, camera pose iteration;
		- Refinement net;
		- Loss design:
			- Pointwise inverse depth;
			- Motion loss: (r, t)
		- **DeMon dataset**: real-world datasets (SUN3D [40], RGB-D SLAM [36], CITYWALL and ACHTECK-TURM [6]) of outdoor and indoor scenes and a synthesized dataset (SCENES 11 [37, 2]) with random objects flying in the air.
		<img src="/CV-3D/images/reconstruction/demon1.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/reconstruction/demon2.png" alt="drawing" width="600"/>
	- **RayNet**: Potentials, D. Paschalidou and A. O. Ulusoy and C. Schmitt and L. Gool and A. Geiger. Learning Volumetric 3D Reconstruction with Ray. CVPR'18
		- Insight: combine the power of CNN and unrolled MRF message passing;
		- https://avg.is.tue.mpg.de/research_projects/raynet
		- Input: images with camera poses; output: voxels?
		- 1. Multi-View CNN for stereo;
		- 2. Unrolled MRF message passing;
		<img src="/CV-3D/images/reconstruction/raynet.png" alt="drawing" width="600"/>
	- **Factor-3d**: S Tulsiani, S Gupta, D Fouhey, A Efros, J Malik. Factoring Shape, Pose, and Layout from the 2D Image of a 3D Scene. CVPR'18
		- Key insight: 3D-scene + 3D-object;
		- https://github.com/shubhtuls/factored3d
		- Input: single image; bounding boxes (objects); shape, pose, scene-3d;
		- Output: layout, objects with 3D shape (voxel) and pose (location, rotation);
		<img src="/CV-3D/images/reconstruction/factor3d.png" alt="drawing" width="600"/>
	- **DeepTAM**: H Zhou, B Ummenhofer,T Brox. DeepTAM: Deep Tracking and Mapping. ECCV'18
		- keyframe-based dense camera tracking and depth map estimation
		- https://github.com/lmb-freiburg/deeptam
		<img src="/CV-3D/images/reconstruction/deeptam1.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/reconstruction/deeptam2.png" alt="drawing" width="600"/>
	- **Neural-RGBD**: C Liu, J Gu, K Kim, S Narasimhan, J Kautz. Neural RGB-D Sensing: Depth and Uncertainty from a Video Camera. CVPR'19
		- Insight: depth as a probability with confidence, single frame depth, then Bayesian filtering to refine;
		- https://github.com/NVlabs/neuralrgbd
		- Input: videos; Output: depth-map;
		- Assumption: camera poses known (from GPS, odometer or IMU, or SOA Visual SLAM DSO[12])
		- D-Net: estimate DPV (depth probability volume) and confidence;
			- PSM-Net [6] to extract features and compute warping loss;
		- K-Net: Integrating DPV over time; (Kalman Gain)
			- Adaptive damping to combine warped depth and new estimation;
		- R-Net: upsample and refine DPV
		- Experiments:
			- Indoor scene: trained on ScanNet [10], tested on 7Scenes [43]; (pose provided by IMU); good meshes can be obtained by post-processing [33];
			- Outdoor: trained on Kitti, tested on virtual Kitti; better than Eigen [11], Mono [17], DORN [13];\
		<img src="/CV-3D/images/reconstruction/neural-rgbd.png" alt="drawing" width="600"/>
- **Multi-view/video self-Supervised**:
	- **SfM-Net**: S Vijayanarasimhan, S Ricco, C Schmid, R Sukthankar, K Fragkiadaki. SfM-Net: Learning of Structure and Motion from Video. 2017
		- https://github.com/waxz/sfm_net (TF)
		- Input: two frames; Output: depth, segmentation, camera and rigid object motions; optical flow;
		- Assumption: use camera intrinsics when available, otherwise: default;
		- Supervision: ssl reprojection photometric error; ego-motion; depth;
		- Architecture:
			- Single-image stream: depth (U-Net)
			- Two-frame stream: camera motion, (object motion, object masks) x K;
			- Dense Optical Flow from two streams;
		- Supervision: different motion could generate same frame;
			- Self supervision; (color)
			- Spatial smoothness; L1
			- Forward-backward consistency check: depth consistency
			- Depth supervision (if GT available)
			- Camera motion (if GT available)
			- Optical flow (if GT available) \
		<img src="/CV-3D/images/reconstruction/sfm-net1.png" alt="drawing" width="500"/>
		<img src="/CV-3D/images/reconstruction/sfm-net2.png" alt="drawing" width="500"/>
	- **SFM-Learner**: T Zhou, M Brown, N Snavely, D Lowe. Unsupervised Learning of Depth and Ego-Motion from Video. CVPR'17
		- https://github.com/tinghuiz/SfMLearner (TF); https://github.com/ClementPinard/SfmLearner-Pytorch (pytorch)
		- Input 2+ frames; output: depth; camera pose;
		- Assumption: intrinsic K known;
		- Single stream: depth estimation;
		- Two stream: camera pose, explanability mask;
		- Supervision:
			- Photometric by view synthesis: inverse warp back to target frame; (L1)
			- Explanability mask \* photometric loss
			- Regularization: multi-scale smoothness loss; \
		<img src="/CV-3D/images/reconstruction/ssl-depth1.png" alt="drawing" width="500"/>
		<img src="/CV-3D/images/reconstruction/ssl-depth2.png" alt="drawing" width="500"/>
		<img src="/CV-3D/images/reconstruction/ssl-depth3.png" alt="drawing" width="400"/>
	- C Pinard, L Chevalley, A Manzanera and D Filliat. Learning structure-from-motion from motion. ECCV'18
		- Insight: depth-net has two inputs, STAB as preprocessing;
		- Input: pair of frames (Ir, It); Output: depth map;
		- 1. Estimate camera pose (R, t), compensate rotation for Ir (stablization)
		- 2. DepthNet(Ir-stab, It): Normalize traslation tr;
		- Supervision: SSIM on warped images
		<img src="/CV-3D/images/reconstruction/sfmfm.png" alt="drawing" width="600"/>
	- Mahjourian, R., Wicke, M., Angelova, A.: Unsupervised learning of depth and ego-motion from monocular video using 3d geometric constraints. CoRR'18
	- A Gordon, H Li, R Jonschkowski, A Angelova. Depth from Videos in the Wild: Unsupervised Monocular Depth Learning from Unknown Cameras. ICCV'19
		- Insight: Improve on T. Zhou on semantic detection; layer-normalization;
		- https://github.com/google-research/google-research/tree/master/depth_from_video_in_the_wild
		- Input: two images; Output: depth, egomtion, object motion, **camera intrinsic**;
		- Network structure:
			- Bottleneck: intrinsics, extrinsics;
			- Occlusion-aware: from depth-ordering?
		- Regularization:
			- 0/1 semantic detection (union of bounding boxes of pedestrians, cyclist, ...) of mobile objects mask;
			- Randomized layer-normalization (running inference as training mode);
		- Supervision:
			- Consistency 
		- Experiments:
			- Kitti; Cityscapes; YouTube videos
		<img src="/CV-3D/images/reconstruction/depth-from-video.png" alt="drawing" width="600"/>
	- **Geonet**: Yin, Z., Shi, J.: Geonet: Unsupervised learning of dense depth, optical flow and camera pose. CVPR'18
		- https://github.com/yzcjtr/GeoNet
		- Input: images; output: depth, camera motion, flow;
		<img src="/CV-3D/images/reconstruction/geonet.png" alt="drawing" width="600"/>
	- **BA-Net**: C Tang, P Tan. BA-Net: Dense Bundle Adjustment Networks. ICLR'19
		- https://github.com/frobelbest/BANet
		- Input: images; Output: camera poses T and dense depth map;
		- 1. DRN [dilated-residual-net CVPR'17] for depth est backbone;
		- 2. FPN: Feature Pyramid Constructor for multi-scale; concat upscaled est and merge from last conv;
		- 3. BA-Layer: differentiable LM (Levenberg-Marquadt)
		- Supervision: camera pose; depth map;
		<img src="/CV-3D/images/reconstruction/ba-net.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/reconstruction/ba-net2.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/reconstruction/ba-net3.png" alt="drawing" width="600"/>
- J Ruben A Moniz, C Beckham, S Rajotte, S Honari, C Pal. Unsupervised Depth Estimation, 3D Face Rotation and Replacement. NIPS'18

## Stereo
- Unclassified:
	- C Lin, O Wang, B Russell, E Shechtman, V Kim, M Fisher, and S Lucey. Photometric mesh optimization for video-aligned 3d object reconstruction. CVPR'19
- Legacy:
	- Descriptors:
		- CENSUS, BRIEF
	- SGM;
	- MVS:
		- Voxel-based: (space-carving)
			- K. N. Kutulakos and S. M. Seitz. A theory of shape by space carving. ICCV'99
			- S. M. Seitz and C. R. Dyer. Photorealistic scene reconstruction by voxel coloring. IJCV'99
		- Fusion-based:
			- N. D. Campbell, G. Vogiatzis, C. Hernández, and R. Cipolla. Using multiple hypotheses to improve depth-maps for multiview stereo. ECCV'08
			- E. Tola, C. Strecha, and P. Fua. Efficient large-scale multi-view stereo for ultra high-resolution image sets. MVA'12
			- S. Galliani, K. Lasinger, and K. Schindler. Massively parallel multiview stereopsis by surface normal diffusion. ICCV'15
- DL: patch-similarity:
	- S. Zagoruyko and N. Komodakis. Learning to compare image patches via convolutional neural networks. CVPR'15
	- J. Zbontar and Y. LeCun. Stereo matching by training a convolutional neural network to compare image patches. JMLR'16
	- W. Luo, A. G. Schwing, and R. Urtasun. Efficient deep learning for stereo matching. CVPR'16
	- P Knobelreiter, C Reinbacher, A Shekhovtsov, and T Pock. End-to-end training of hybrid cnn-crf models for stereo. CVPR'17
	- W. Hartmann, S. Galliani, M. Havlena, L. V. Gool, K. Schindler. Learned multi-patch similarity. ICCV'17.
		- Input: **> 2** image patches (32 x 32);
		- Output: potential depth (discretized);
		<img src="/CV-3D/images/stereo/multi-patch-sim.png" alt="drawing" width="600"/>
		- Application in MVS (plane-sweep): discretize depth and iterate over all;
	- **GC-Net**: A. Kendall, H. Martirosyan, S. Dasgupta, P. Henry, R. Kennedy, A. Bachrach, and A. Bry. End-to-end learning of geometry and context for deep stereo regression. ICCV'17
		- Input: rectified stereo pair;
		- Output: stereo;
		- Cost volume;
		- Conv-Deconv on cost volume;
		- Differentiable arg-max;
		<img src="/CV-3D/images/stereo/gc-net.png" alt="drawing" width="500"/>
	- S Duggal, S Wang, W Ma, Rui Hu, and R Urtasun. Deeppruner: Learning efficient stereo matching via differentiable patchmatch. 2019
- DL: affinity:
	- **Sgm-net**: A Seki and M Pollefeys. Sgm-nets: Semi-global matching with neural networks. CVPR'17
	- **SPN**: S. Liu, S. De Mello, J. Gu, G. Zhong, M.-H. Yang, and J. Kautz, Learning affinity via spatial propagation networks. NIPS'17
		- https://github.com/danieltan07/spatialaffinitynetwork
		- https://github.com/Liusifei/caffe-spn
	- **CSPN (SOA)**: X Cheng, P Wang and R Yang. Learning Depth with Convolutional Spatial Propagation Network. PAMI'18
		- https://github.com/XinJCheng/CSPN
		<img src="/CV-3D/images/stereo/cspn.png" alt="drawing" width="600"/>
	- **GA-Net (SOA)**: F Zhang, V Prisacariu, R Yang, Philip H.S. Torr. GA-Net: Guided Aggregation Net for End-to-end Stereo Matching. CVPR'19
		- https://github.com/feihuzhang/GANet
	- X Du, M El-Khamy, J Lee. AMNet: Deep Atrous Multiscale Stereo Disparity Estimation Networks. 2019
	- **HD3**: Z. Yin, T. Darrell and F. Yu: Hierarchical Discrete Distribution Decomposition for Match Density Estimation. CVPR 2019.
		- https://github.com/ucbdrive/hd3
	- **PSM-Net**: J Chang and Y Chen. Pyramid stereo matching network. CVPR'18
	- T. Khot, S. Agrawal, S. Tulsiani, C. Mertz, S. Lucey, M. Hebert. Learning Unsupervised Multi-View Stereopsis via Robust Photometric Consistency. 2019.
	- C Tang and P Tan. BA-Net: Dense Bundle Adjustment Network. 2018
	- **Unsupervised-Deep-VO**: Ruihao Li, Sen Wang, Zhiqiang Long, and Dongbing Gu. Undeepvo: Monocular visual odometry through unsupervised deep learning. In ICRA, 2018.
- DL: PSV (plane-sweep algorithm):
	- J. Flynn, I. Neulander, J. Philbin, and N. Snavely. Deep-Stereo: Learning to predict new views from the world's imagery. CVPR'16
		- Problem: new view synthesis
		- Input images with camera poses;
		- Output: new 2d synthesized view;
		- Preprocess: PSV (Plane-Sweep Volume)
		<img src="/CV-3D/images/stereo/deep-stereo.png" alt="drawing" width="500"/>
	- **DeepMVS**: P Huang, K Matzen, J Kopf, N Ahuja, and J Huang. DeepMVS: Learning Multi-view Stereopsis. CVPR'18
		- https://github.com/phuang17/DeepMVS
		- Input: an **arbitrary number** of images with known camera poses and calibration;
		- Steps:
			- 0. Images, camera pose and calibration (**COLMAP** to estimate);
			- 1. Produce plane-sweep volumes;
			- 2.1 Patch Matching
			- 2.2 Encoder-decoder intra-volume feature aggregation;
			- 2.3 Max-pooling to aggregate inter-volume and produce disparity map;
			- 3. Refinement: dense-crf
		- Dataset:
			- DeMoN dataset: 640 x 480 resolution;
			- **MVS-SYNTH**: 120 sequences synthetic (greatly helpful), each seq contains 100 images of 1920 x 1080 resolution, ground truth disparity map, extrinsic and intrinsic camera;
			- ETH3D
	- **DPSNet**: S Im, H Jeon, S Lin, I S Kweon. DPSNet: End-to-end Deep Plane Sweep Stereo, ICLR'19.
		- Assume: intrinsic K; extrinsic (R, t) known
		<img src="/CV-3D/images/stereo/dpsnet.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/stereo/dpsnet2.png" alt="drawing" width="500"/>
- DL: MVS:
	- **MVSNet**: Y. Yao, Z. Luo, S. Li, T. Fang, L. Quan. MVSNet: Depth Inference for Unstructured Multi-view Stereo. ECCV'18.
	- **Point-MVSNet**: R Chen, S Han, J Xu, H Su. Point-based Multi-view Stereo Network. ICCV'19.
		- https://github.com/callmeray/PointMVSNet
		- MVSNet for a low-resolution depth; 1/4 resolution, 48 or 96 depth plane;
		- Cost metric based on variance;
		- Dynamic feature fetching (extracted at different location after iterative refine);
		- PointFlow for iterative refine;
			- Edge conv: with kNN
		- Supervision: L1-loss with ground truth for regression;
		- Experiments: DTU; 
		<img src="/CV-3D/images/stereo/point-mvs-net.png" alt="drawing" width="600"/>

## Scene/Shape Completion
- Shape Completion:
	- A. Dai, C. R. Qi, and M. Nießner. Shape completion using 3d-encoder-predictor cnns and shape synthesis
- Scene (Depth) Inpainting/Completion
	- S. Song, F. Yu, A. Zeng, A. X. Chang, M. Savva, and T. Funkhouser. Semantic scene completion from a single depth image.
	- **DeepLiDAR**: J. Qiu, Z. Cui, Y. Zhang, X. Zhang, S. Liu, B. Zeng and M. Pollefeys. DeepLiDAR: Deep Surface Normal Guided Depth Prediction for Outdoor Scene from Sparse LiDAR Data and Single Color Image.
		- https://github.com/JiaxiongQ/DeepLiDAR
	- W. Van Gansbeke, D. Neven, B. De Brabandere and L. Van Gool: Sparse and noisy LiDAR completion with RGB guidance and uncertainty. International Conference on Machine Vision Applications (MVA) 2019.
		- https://github.com/wvangansbeke/Sparse-Depth-Completion
	- **GuideNet**: Tang, F. Tian, W. Feng, J. Li and P. Tan: Learning Guided Convolutional Network for Depth Completion. TIP'19
		- https://github.com/kakaxi314/GuideNet
		- Inspired by guided-image filter, learnable filter;\
		<img src="/CV-3D/images/depth-est/guide-net1.png" alt="drawing" width="500"/>
		<img src="/CV-3D/images/depth-est/guide-net2.png" alt="drawing" width="500"/>
	- **FuseNet**: Y. Chen, B. Yang, M. Liang and R. Urtasun: Learning Joint 2D-3D Representations for Depth Completion. ICCV'19.
		- 2D-3D Fuse-block:
			- Multi-scale 2D convolution net: with skip
			- 3D continuous convolution [Shenlong, CVPR'18]: K-nn
			- Fusion: element-wise summation;\
		<img src="/CV-3D/images/depth-est/fusenet1.png" alt="drawing" width="500"/>
		<img src="/CV-3D/images/depth-est/fusenet2.png" alt="drawing" width="500"/>
	- D Frossard, R Urtasun. Probabilistic Depth Completion. Mini-29
		- Input: image + Lidar;
		- Output: depth, semantic class, instance id;
		- Semantic by [Deep Watershed, Min Bai];
		- Assume a probabilistic model
		- Model to optimize MLE;
	- S Duggal, S Wang, W Ma, R Urtasun. Learning Spatially Consistent Depth using Graph Neural Network based Poisson Solver. Mini-17
	- A Dai, D Ritchie, M Bokeloh, S Reed, J Sturm, M Nießner. ScanComplete: Large-Scale Scene Completion and Semantic Segmentation for 3D Scans. 2018
	- A Dai, C Diller, M Nießner. SG-NN: Sparse Generative Neural Networks for Self-Supervised Scene Completion of RGB-D Scans. CVPR'20 submission

## Misc
- X. Wang, D. Fouhey, and A. Gupta. Designing deep networks for surface normal estimation. CVPR'15
- SurfNet: Generating 3D shape surfaces using deep residual networks, CVPR 2017
- Deep Marching Cubes: Learning Explicit Surface Representations. CVPR'18
- Learning Category-Specific Mesh Reconstruction from Image Collections. 2018
- Pixels, voxels, and views: A study of shape representations for single view 3D object shape prediction. CVPR'18
- Learning View Priors for Single-view 3D Reconstruction. CVPR'19
- CompoNet: Learning to Generate the Unseen by Part Synthesis and Composition. ICCV'19
