# Scene Flow

## Problem Definition
- Input: two stereo pairs
- Output: 3D motion (mostly from ego-car, dynamic objects)
- Assume: all cameras calibrated with known intrinsics;

## Papers
- **ISF**: A. Behl, O. Jafari, S. Mustikovela, H. Alhaija, C. Rother and A. Geiger: Bounding Boxes, Segmentations and Object Coordinates: How Important is Recognition for 3D Scene Flow Estimation in Autonomous Driving Scenarios?. ICCV'17
- Z Ren, D Sun, J Kautz, and E Sudderth. Cascaded scene flow prediction using semantic segmentation. 3DV'17
- **UberATG-DRISF**: W Ma, S Wang, R Hu, Y Xiong, R Urtasun. Deep Rigid Instance Scene Flow. ICCV'19
	- Network design: three streams; then combined;
	- 1. Optical flow: Pwc-Net (pyramid, warping, cost-volume)
	- 2. Stereo: PSM-Net
	- 3. Segmentation: Mask R-CNN
	<img src="/Autonomous-Driving/images/scene-flow/deep-rigid-scene-flow.png" alt="drawing" width="500"/>

- **HD^3-Flow**: Z Yin, T Darrell, F Yu. Hierarchical Discrete Distribution Decomposition for Match Density Estimation. CVPR'19
	- https://github.com/ucbdrive/hd3
	<img src="/Autonomous-Driving/images/scene-flow/hier-matching.png" alt="drawing" width="600"/>
	