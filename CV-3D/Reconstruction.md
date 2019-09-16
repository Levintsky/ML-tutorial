# 3D Reconstruction

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
- Google: Depth from Videos in the Wild: Unsupervised Monocular Depth Learning from Unknown Cameras. ICCV'19
	- https://github.com/google-research/google-research/tree/master/depth_from_video_in_the_wild
	- Improve on T. Zhou
	- Output: depth, egomtion, object motion, camera intrinsic;
	- Supervision:
		- Consistency 
- DeMoN: Depth and Motion Network for Learning Monocular Stereo. CVPR'17
	- https://github.com/lmb-freiburg/demon (TF)
	- Input: two images;
	- Output: depth, camera motion
	- Bootstrap net: initial depth and camera;
	- Iterative net x 3:
	- Refinement net;
- Learning structure-from-motion from motion. ECCV'18
	- Input: pair of frames (Ir, It)
	- Estimate camera pose (R, t), compensate rotation for Ir (stablization)
	- DepthNet(Ir-stab, It): **key difference: depth-net has two inputs**
	- Normalize traslation tr;

## Video
- J. Xie, R. B. Girshick, and A. Farhadi. Deep3D: Fully automatic 2D-to-3D video conversion with deep convolutional neural networks. ECCV'16