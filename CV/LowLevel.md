# Low-Level Vision

## SLAM (Simultaneous Localization And Mapping)
- LiDAR SLAM
	- Step 1. Map initialization
	- Step 2. Pose Tracking: ICP (Iterative closest point), optimize for camera pose;
	- Step 3. Map optimization: occupancy grid map;
	- Iterate 2 and 3.
	<img src="/CV/images/low-level/icp.png" alt="drawing" width="450"/>

- Visual SLAM
	- Step 1. Initialization; (essential matrix, triangulation)
	- Step 2. Pose estimation: (feature tracking, pose-only BA)
	- Visual SLAM by SfM
	- PTAM (Parallel Tracking and Mapping)
		- Real time camera pose tracking
		- An offline thread for map maintenance: when key frame comes, do a BA
- Relocalization
	- Tracking can lose due to various reasons
- Robustness Techniques
	- Drifting

## Depth, Stereo
- Stereo:
	- J. Flynn, I. Neulander, J. Philbin, and N. Snavely. Deep-Stereo: Learning to predict new views from the world’s imagery. CVPR'16
	- A. Kendall, H. Martirosyan, S. Dasgupta, P. Henry, R. Kennedy, A. Bachrach, and A. Bry. End-to-end learning of geometry and context for deep stereo regression. 2017
	- J. Zbontar and Y. LeCun. Stereo matching by training a convolutional neural network to compare image patches. JMLR'16
	- X Cheng, P Wang and R Yang. Learning Depth with Convolutional Spatial Propagation Network. PAMI'18
	<img src="/CV/images/low-level/cspn.png" alt="drawing" width="600"/>

	- F Zhang, V Prisacariu, R Yang, Philip H.S. Torr. GA-Net: Guided Aggregation Net for End-to-end Stereo Matching. CVPR'19
		- https://github.com/feihuzhang/GANet
	- X Du, M El-Khamy, J Lee. AMNet: Deep Atrous Multiscale Stereo Disparity Estimation Networks. 2019
- T Zhou, M Brown, N Snavely, D Lowe. Unsupervised Learning of Depth and Ego-Motion from Video. CVPR'17
	- https://github.com/tinghuiz/SfMLearner
	- Input: ego video;
	- Output: monocular depth, camera motion;
	- View synthesis as supervision, all source frames s to predict target frame t
	- Differentiable depth image-based rendering: similar to SPN (Spatial Transformer Network)
	- Modeling the model limitation: weighted correspondence, regularization on weight to avoid trivial all-zero weight
	<img src="/CV/images/low-level/ssl-depth1.png" alt="drawing" width="600"/>
	<img src="/CV/images/low-level/ssl-depth2.png" alt="drawing" width="600"/>
	<img src="/CV/images/low-level/ssl-depth3.png" alt="drawing" width="400"/>

## Optical Flow
- **FlowNet**: A Dosovitskiy, P Fischer, E Ilg, P Hausser, C Hazırbas, V Golkov. FlowNet: Learning Optical Flow with Convolutional Networks. ICCV'15
	- FlowNetS: stacks two images as input
	- FlowNetC: convolute separately, combine with correlation layer

- **FlowNet 2.0**: E Ilg, N Mayer, T Saikia, M Keuper, A Dosovitskiy, T Brox. FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks. CVPR'17
	- FlowNetC: explicit correlation
	- FlowNetS: a straightforward encoder-decoder architecture
	- FlowNetSD: small displacement
	- FlowNetFusion: fusion of different flows
	- Improvement over 1.0: smooth flow fields; preserve fine-motion detail; fast;
	<img src="/CV/images/low-level/flownet2.png" alt="drawing" width="600"/>

- **MFF**: Z Ren, O Gallo, D Sun, M Yang, E Sudderth and J Kautz. A Fusion Approach for Multi-Frame Optical Flow Estimation. 2019
- **SelFlow**: P Liu, M R. Lyu, I 
King, J Xu. Self-Supervised Learning of Optical Flow. CVPR'19
<img src="/CV/images/low-level/selflow1.png" alt="drawing" width="600"/>
<img src="/CV/images/low-level/selflow2.png" alt="drawing" width="500"/>

## Scene Flow
- W Ma, S Wang, R Hu, Y Xiong, R Urtasun. Deep Rigid Instance Scene Flow. 2019
<img src="/CV/images/low-level/deep-rigid-scene-flow.png" alt="drawing" width="500"/>

- **HD^3-Flow**: Z Yin, T Darrell, F Yu. Hierarchical Discrete Distribution Decomposition for Match Density Estimation. CVPR'19
	- https://github.com/ucbdrive/hd3
	<img src="/CV/images/low-level/hier-matching.png" alt="drawing" width="600"/>

## Camera Pose
- A. Kendall, M. Grimes, and R. Cipolla. PoseNet: A convolutional network for real-time 6-DOF camera relocalization. ICCV'15

## View Synthesis
- T.Zhou,S.Tulsiani,W.Sun,J.Malik,andA.A.Efros.View synthesis by appearance flow. ECCV'16
- Legacy:
	- S. E. Chen and L. Williams. View interpolation for image synthesis. 1993
	- C. L. Zitnick, S. B. Kang, M. Uyttendaele, S. Winder, and R. Szeliski. High-quality video view interpolation using a layered representation. TOG'04
	- S. M. Seitz and C. R. Dyer. View morphing. 1996
	- P. E. Debevec, C. J. Taylor, and J. Malik. Modeling and rendering architecture from photographs: A hybrid geometry- and image-based approach. 1996
	- A. Fitzgibbon, Y. Wexler, and A. Zisserman. Image-based rendering using image-based priors. IJCV'05

## Keypoints, Feature Matching
- X. Han, T. Leung, Y. Jia, R. Sukthankar, and A. C. Berg. MatchNet: Unifying feature and metric learning for patch-based matching. CVPR'15

## Legacy
- Structure from motion: simultaneous estimate structure and motion
	- Y. Furukawa, B. Curless, S. M. Seitz, and R. Szeliski. Towards internet-scale multi-view stereo. CVPR'10
	- R. A. Newcombe, S. J. Lovegrove, and A. J. Davison. DTAM: Dense tracking and mapping in real-time. ICCV'11
	- C. Wu. VisualSFM: A visual structure from motion system. http://ccwu.me/vsfm, 2011
	- Failure: low-texture, occlusion, thin structure