# 3D Reconstruction

## Benchmarks
- Kitti
- DeMon dataset
- **ETH-3D**: T. Schöps, J. L. Schönberger, S. Galliani, T. Sattler, K. Schindler, M. Pollefeys, and A. Geiger. A multi-view stereo benchmark with high-resolution images and multi-camera videos. CVPR'17

## Evaluation
- Geometric: depth/disparity with GT;
- Photometric;

## Deep SFM
- Google: SfM-Net: Learning of Structure and Motion from Video. 2017
	- Input: two frames;
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
- Google (T. Zhou): Unsupervised Learning of Depth and Ego-Motion from Video. CVPR'17
	- Input 2+ frames, **intrinsic known**
	- Single stream: depth
	- Two stream: camera pose, explanability mask
	- Supervision:
		- View synthesis: inverse warp back to target frame; (L1)
		- Explanability mask \* photometric loss
		- Regularization: multi-scale smoothness loss;
	<img src="/CV/images/low-level/ssl-depth1.png" alt="drawing" width="600"/>
	<img src="/CV/images/low-level/ssl-depth2.png" alt="drawing" width="600"/>
	<img src="/CV/images/low-level/ssl-depth3.png" alt="drawing" width="400"/>

- Google: Depth from Videos in the Wild: Unsupervised Monocular Depth Learning from Unknown Cameras. ICCV'19
	- https://github.com/google-research/google-research/tree/master/depth_from_video_in_the_wild
	- Improve on T. Zhou
	- Output: depth, egomtion, object motion, camera intrinsic;
	- Supervision:
		- Consistency 
- DeMoN: Depth and Motion Network for Learning Monocular Stereo. CVPR'17
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
	- **DeMon dataset**: real-world datasets (SUN3D [40], RGB-D SLAM [36], CITYWALL and ACHTECK-TURM [6]) of outdoor and indoor scenes and a synthesized dataset (SCENES 11 [37, 2]) with random objects flying in the air.
	- Insight: mixing synthetic and real-world is important;
- Learning structure-from-motion from motion. ECCV'18
	- Input: pair of frames (Ir, It)
	- Estimate camera pose (R, t), compensate rotation for Ir (stablization)
	- DepthNet(Ir-stab, It): **key difference: depth-net has two inputs**
	- Normalize traslation tr;

## MVS
- DeepMVS: Learning Multi-view Stereopsis. CVPR'18
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
- Patch Similarity for stereo:
	- S. Zagoruyko and N. Komodakis. Learning to compare image patches via convolutional neural networks. CVPR'15
	- J. Zbontar and Y. LeCun. Stereo matching by training a convolutional neural network to compare image patches. JMLR'16
	- W. Luo, A. G. Schwing, and R. Urtasun. Efficient deep learning for stereo matching. CVPR'16
	- W. Hartmann, S. Galliani, M. Havlena, K. Schindler, and L. Van Gool. Learned multi-patch similarity. ICCV'17
- Plane-sweep volume as input:
	- J. Flynn, I. Neulander, J. Philbin, and N. Snavely. Deep-Stereo: Learning to predict new views from the world's imagery. CVPR'16
	- A. Kendall, H. Martirosyan, S. Dasgupta, P. Henry, R. Kennedy, A. Bachrach, and A. Bry. End-to-end learning of geometry and context for deep stereo regression. ICCV'17
	- DeMoN: Depth and Motion Network for Learning Monocular Stereo. CVPR'17
- Stereo-misc:
	- X Cheng, P Wang and R Yang. Learning Depth with Convolutional Spatial Propagation Network. PAMI'18
	<img src="/CV/images/low-level/cspn.png" alt="drawing" width="600"/>

	- **SOA**: F Zhang, V Prisacariu, R Yang, Philip H.S. Torr. GA-Net: Guided Aggregation Net for End-to-end Stereo Matching. CVPR'19
		- https://github.com/feihuzhang/GANet
	- X Du, M El-Khamy, J Lee. AMNet: Deep Atrous Multiscale Stereo Disparity Estimation Networks. 2019
	- **SOA**: X. Cheng, P. Wang and R. Yang: Learning Depth with Convolutional Spatial Propagation Network.
		- https://github.com/XinJCheng/CSPN
	- **HD3**: Z. Yin, T. Darrell and F. Yu: Hierarchical Discrete Distribution Decomposition for Match Density Estimation. CVPR 2019.
		- https://github.com/ucbdrive/hd3

## Video
- J. Xie, R. B. Girshick, and A. Farhadi. Deep3D: Fully automatic 2D-to-3D video conversion with deep convolutional neural networks. ECCV'16