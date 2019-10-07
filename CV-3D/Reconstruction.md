# 3D Reconstruction

## Problem Setup
- Direct 3D reconstruction;
- Infer cues:
	- 2.5-D: - H. G. Barrow and J. M. Tenenbaum, Recovering intrinsic scene characteristics from images, Computer Vision Systems, 1978

## Benchmarks
- Kitti;
- Cityscape;
- DeMon dataset: combination of SUN3D, ...
- **DTU**: H Aanæs, R Jensen, G Vogiatzis, E Tola, and A Dahl. Large-Scale Data for Multiple-View Stereopsis. IJCV'16
	- MVS benchmark;
- **ETH-3D**: T. Schöps, J. L. Schönberger, S. Galliani, T. Sattler, K. Schindler, M. Pollefeys, and A. Geiger. A multi-view stereo benchmark with high-resolution images and multi-camera videos. CVPR'17
- **Tanks and Temples**: A Knapitsch, J Park, Q Zhou, and V Koltun. Tanks and Temples: Benchmarking Large-scale Scene Reconstruction. TOG'17
	- MVS benchmark;

## Evaluation
- Geometric: depth/disparity with GT;
- Photometric;

## Latest
- Tom, Shenlong, Raquel:
	- https://docs.google.com/presentation/d/1Mxpq_EQvlHXAsF_fz18-VN2UN6WPaACKIQvRFj7o7YM/edit#slide=id.g5058d9e3b1_0_0
- Deep Structured 3D Estimation. Mini-12
	- Input: stereo image, LiDAR;
	- Output: pose, shape;
	- Supervision:
		- Multi-view geometry;
		- Intuitive physics;
		- Photo consistency;
		- Silhouette;
		- Consistency;
		- Intuitive physics;
		- Symmetry;
	- Metrics: shape; (Chamfer distance) pose;
	- Exp: ShapeNet, Tor4D, Kitti;

## Depth Estimation
- Single view:
	- **MonoDepth**: C. Godard, O. Mac Aodha, and G. J. Brostow. Unsupervised monocular depth estimation with left-right consistency. CVPR'17
	- **DORN**: H. Fu, M. Gong, C. Wang, K. Batmanghelich, and D. Tao. Deep ordinal regression network for monocular depth estimation. CVPR'18
- Multi-view/video supervised:
	- **DeMoN**: B Ummenhofer, H Zhou, J Uhrig, N Mayer, E Ilg, A Dosovitskiy, T Brox. DeMoN: Depth and Motion Network for Learning Monocular Stereo. CVPR'17
		- https://github.com/lmb-freiburg/demon (TF)
		- https://github.com/cvfish/pytorch_demon.git (Pytorch)
		- Input: two images;
		- Output: depth, camera motion
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
		- Insight: mixing synthetic and real-world is important;
		<img src="/CV-3D/images/reconstruction/demon1.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/reconstruction/demon2.png" alt="drawing" width="600"/>
	- **Neural-RGBD**: C Liu, J Gu, K Kim, S Narasimhan, J Kautz. Neural RGB-D Sensing: Depth and Uncertainty from a Video Camera. CVPR'19
		- https://github.com/NVlabs/neuralrgbd
		- Insight: single frame depth, then Bayesian filtering
		- Input: videos
		- Output: depth-map
		- Assumption: camera poses known (from GPS, odometer or IMU, or SOA Visual SLAM DSO[12])
		- D-Net: estimate DPV (depth probability volume) and confidence;
			- PSM-Net [6] to extract features and compute warping loss;
		- K-Net: Integrating DPV over time; (Kalman Gain)
			- Adaptive damping to combine warped depth and new estimation;
		- R-Net: upsample and refine DPV
		- Experiments:
			- Indoor scene: trained on ScanNet [10], tested on 7Scenes [43]; (pose provided by IMU); good meshes can be obtained by post-processing [33];
			- Outdoor: trained on Kitti, tested on virtual Kitti; better than Eigen [11], Mono [17], DORN [13];
		<img src="/CV-3D/images/reconstruction/neural-rgbd.png" alt="drawing" width="600"/>
- Multi-view/video self-Supervised:
	- Google: SfM-Net: Learning of Structure and Motion from Video. 2017
		- Input: two frames; (use camera intrinsics when available, otherwise: default;)
		- Output: depth, segmentation, camera and rigid object motions; optical flow;
		- Supervision: ssl reprojection photometric error; ego-motion; depth;
		- https://github.com/waxz/sfm_net (TF)
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
			- Optical flow (if GT available)
		<img src="/CV-3D/images/reconstruction/sfm-net1.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/reconstruction/sfm-net2.png" alt="drawing" width="600"/>
	- Google (T. Zhou): Unsupervised Learning of Depth and Ego-Motion from Video. CVPR'17
		- Input 2+ frames, **intrinsic known**
		- Single stream: depth
		- Two stream: camera pose, explanability mask
		- Supervision:
			- View synthesis: inverse warp back to target frame; (L1)
			- Explanability mask \* photometric loss
			- Regularization: multi-scale smoothness loss;
		<img src="/CV-3D/images/reconstruction/ssl-depth1.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/reconstruction/ssl-depth2.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/reconstruction/ssl-depth3.png" alt="drawing" width="400"/>
	- Google: A Gordon, H Li, R Jonschkowski, A Angelova. Depth from Videos in the Wild: Unsupervised Monocular Depth Learning from Unknown Cameras. ICCV'19
		- https://github.com/google-research/google-research/tree/master/depth_from_video_in_the_wild
		- Improve on T. Zhou
		- Output: depth, egomtion, object motion, **camera intrinsic**;
		- Network structure:
			- Bottleneck: intrinsics, extrinsics;
			- Occlusion-aware: from depth-ordering?
		- Regularization:
			- 0/1 semantic detection (union of bounding boxes of pedestrians, cyclist, ...) of mobile objects mask;
			- Randomized layer-normalization (running inference as training mode);
		- Supervision:
			- Consistency 
		- Experiments:
			- Kitti
			- Cityscapes
			- YouTube videos
		<img src="/CV-3D/images/reconstruction/depth-from-video.png" alt="drawing" width="600"/>
	- Learning structure-from-motion from motion. ECCV'18
		- Input: pair of frames (Ir, It)
		- Estimate camera pose (R, t), compensate rotation for Ir (stablization)
		- DepthNet(Ir-stab, It): **key difference: depth-net has two inputs**
		- Normalize traslation tr;
	- **DeepMind**:
		- Unsupervised Learning of 3D Structure from Images
		- Andrew Brock, Theodore Lim, J.M. Ritchie, Nick Weston. Generative and Discriminative Voxel Modeling with Convolutional Neural Networks
			- https://github.com/ajbrock/Generative-and-Discriminative-Voxel-Modeling
			- VAE, GAN

## Depth Inpainting/Completion
- **DeepLiDAR**: J. Qiu, Z. Cui, Y. Zhang, X. Zhang, S. Liu, B. Zeng and M. Pollefeys. DeepLiDAR: Deep Surface Normal Guided Depth Prediction for Outdoor Scene from Sparse LiDAR Data and Single Color Image.
	- https://github.com/JiaxiongQ/DeepLiDAR
- W. Van Gansbeke, D. Neven, B. De Brabandere and L. Van Gool: Sparse and noisy LiDAR completion with RGB guidance and uncertainty. International Conference on Machine Vision Applications (MVA) 2019.
	- https://github.com/wvangansbeke/Sparse-Depth-Completion
- **GuideNet**: Tang, F. Tian, W. Feng, J. Li and P. Tan: Learning Guided Convolutional Network for Depth Completion. TIP'19
	- https://github.com/kakaxi314/GuideNet
	- Inspired by guided-image filter, learnable filter;
	<img src="/CV-3D/images/depth-est/guide-net1.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/depth-est/guide-net2.png" alt="drawing" width="600"/>
- **FuseNet**: Y. Chen, B. Yang, M. Liang and R. Urtasun: Learning Joint 2D-3D Representations for Depth Completion. ICCV'19.
	- 2D-3D Fuse-block:
		- Multi-scale 2D convolution net: with skip
		- 3D continuous convolution [Shenlong, CVPR'18]: K-nn
		- Fusion: element-wise summation
	<img src="/CV-3D/images/depth-est/fusenet1.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/depth-est/fusenet2.png" alt="drawing" width="600"/>
- D Frossard, R Urtasun. Probabilistic Depth Completion. Mini-29
	- Input: image + Lidar;
	- Output: depth, semantic class, instance id;
	- Semantic by [Deep Watershed, Min Bai];
	- Assume a probabilistic model
	- Model to optimize MLE;
- S Duggal, S Wang, W Ma, R Urtasun. Learning Spatially Consistent Depth using Graph Neural Network based Poisson Solver. Mini-17

## View Synthesis
- Image Simulation by Geometry-Aware Composition. Mini-conference.
	- Separate static and dynamic modeling;
	- Input: a tuple of RGB image, BEV layout, semantic and instance segmentation masks, LiDAR sweep data, and ground height data (in BEV space);
		- BEV layout: lane info, bounding boxes of dynamic objects;
	- Object bank: precise geometry; from RGB images with semantic and instance segmentation;
	- 1. Placement Sampling;
	- 2. Segment Retrieval;
	- 3. Novel View Warping;
	- 4. Final image synthesis;
	- Geometry refinement: optimize Nx3 mesh with energy with silhoutte, lidar and symmetry;
- J. Xie, R. B. Girshick, and A. Farhadi. Deep3D: Fully automatic 2D-to-3D video conversion with deep convolutional neural networks. ECCV'16
	- Input: left view;
	- Output: right view?
	- Evaluation: Kitti, NYU
	<img src="/CV-3D/images/depth-est/deep3d.png" alt="drawing" width="600"/>
- E Park, J Yang, E Yumer, D Ceylan, and A Berg. Transformation-Grounded Image Genera- 510 tion Network for Novel 3d View Synthesis. 2017
- T. Zhou, S. Tulsiani, W. Sun, J. Malik and A. Efros. View synthesis by appearance flow. ECCV'16
	- https://github.com/tinghuiz/appearance-flow
- J Yang. Weakly-supervised Disentangling with Recurrent Transformations for 3D View Synthesis. NIPS 2015
	- Input/output: images
	- https://github.com/jimeiyang/deepRotator
- Legacy:
	- S. E. Chen and L. Williams. View interpolation for image synthesis. 1993
	- C. L. Zitnick, S. B. Kang, M. Uyttendaele, S. Winder, and R. Szeliski. High-quality video view interpolation using a layered representation. TOG'04
	- S. M. Seitz and C. R. Dyer. View morphing. 1996

## Single/Multi-Image, Object Reconstruction
- Single-image:
	- C B Choy, D Xu, J Gwak, K Chen, and S Savarese. 3d-r2n2: A unified approach for single and multiview 3d object reconstruction. ECCV'16
		- Update model with RNN each time with a new image;
		- https://github.com/chrischoy/3D-R2N2
	- X Yan, J Yang, E Yumer, Y Guo, and H Lee. Perspective transformer nets: Learning single-view 3d object reconstruction without 3d supervision. NIPS'16
		- https://github.com/xcyan/ptnbhwd
	- H Fan, H Su, and L Guibas. A point set generation network for 3d object reconstruction from a single image. CVPR'17
	- L Mescheder, M Oechsle, M Niemeyer, S Nowozin, and A Geiger. Occupancy networks: Learning 3d reconstruction in function space. CVPR'19
	- **DeepSDF**: J Park, P Florence, J Straub, R Newcombe, S Lovegrove. DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation. 2019
- **DRC**: S Tulsiani, T Zhou, A Efros, J Malik. Multi-view Supervision for Single-view Reconstruction via Differentiable Ray Consistency.  PAMI'19
	- https://github.com/shubhtuls/drc
	- Input: image (model) + multiple images (refine?);
	- Output: voxel for 3d;
	- Assume: camera poses known?
	- Model: ray termination event;	Event: a ray intersect a voxel, previous voxels are all unoccupied
	- Cost:
		- Depth, Foreground mask
		- Per-ray consistency loss
	- Experiment:
		- ShapeNet
		- PASCAL 3D
	<img src="/CV-3D/images/reconstruction/drc.png" alt="drawing" width="600"/>

- **MVC**: S Tulsiani, A Efros, J Malik. Multi-view Consistency as Supervisory Signal for Learning Shape and Pose Prediction. CVPR'18
	- https://github.com/shubhtuls/mvcSnP
- S Tulsiani, S Gupta, D Fouhey, A Efros, J Malik. Factoring Shape, Pose, and Layout from the 2D Image of a 3D Scene. CVPR'18
	- https://github.com/shubhtuls/factored3d
	- Input: single image; bounding boxes (objects);
	- Output: layout, objects with 3D shape (voxel) and pose (location, rotation);
	<img src="/CV-3D/images/reconstruction/factor3d.png" alt="drawing" width="600"/>

	- A Kar, S Tulsiani, J Carreira, J Malik. Category-Specific Object Reconstruction from a Single Image. CVPR'15
		- https://github.com/akar43/CategoryShapes

- C Hane, S Tulsiani, J Malik. Hierarchical Surface Prediction for 3D Object Reconstruction. 2017
	- Input: color, depth, partial volume
	- Ouptut: voxel
	- CNN with deep-supervision on different resolution
	- Most important part: predict layer l+1 based on layer l
		- Feature Cropping
		- Upsampling
		- Output generation
- **AtlasNet**. T. Groueix, M. Fisher, V. G. Kim, B. C. Russell, and M. Aubry. Atlasnet: A papier-mache approach to learning 3d surface generation. CVPR'18
- **GenRe**: X Zhang, Z Zhang, C Zhang, J Tenenbaum, W Freeman and J Wu. Learning to Reconstruct Shapes from Unseen Classes. NIPS'18
	- https://github.com/xiumingzhang/GenRe-ShapeHD
	<img src="/CV-3D/images/reconstruction/genre.png" alt="drawing" width="600"/>

- **MarrNet**: J Wu, Y Wang, T Xue, X Sun, W Freeman, and J Tenenbaum. MarrNet: 3D Shape Reconstruction via 2.5D Sketches. NIPS'17
	- First predict a 2.5-D (normal, depth, silhouette)
	- Reprojection consistency;
- **3D-INN**:
	- J Wu, T Xue, J Lim, Y Tian, J Tenenbaum, A Torralba, and W Freeman. Single Image 3D Interpreter Network, ECCV'16, IJCV'18
		- Detect 2d keypoints as well as 3d structure;
		- Keypoint detection (CNN) -> keypoint refinement (mini-network like auto-encoder) -> 3D interpreter -> Projection Layer;
	- **ShapeHD**: J Wu, C Zhang, X Zhang, Z Zhang, W Freeman, and J Tenenbaum. Learning Shape Priors for Single-View 3D Completion and Reconstruction. ECCV'18
		- Extension of **3D-INN**
		- An "adversarial" Naturalness Network to determine quality, with Wasserstein-GAN loss;

## Misc
- SurfNet: Generating 3D shape surfaces using deep residual networks, CVPR 2017
- M Tatarchenko, A Dosovitskiy, T Brox. Octree Generating Networks: Efficient Convolutional Architectures for High-resolution 3D Outputs.