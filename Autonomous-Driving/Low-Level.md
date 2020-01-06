# Depth, Stereo, Scene Flow, Mapping, ...

## Scene Flow:
- Input: two stereo pairs
- Output: 3D motion (mostly from ego-car, dynamic objects)
- Assume: all cameras calibrated with known intrinsics;
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

## Depth
- Depth: Learning Joint 2D-3D Representations for Depth Completion [Yun Chen]

## Stereo
- Stereo: Differentiable Deep PatchMatch for  Efficient Stereo Matching [Shivam]

## Mapping
- Convolutional Recurrent Network for Road Boundary Extraction [Justin Liang]
- End-to-End Deep Structured Models for Drawing Crosswalks [ECCV’18, Justin Liang]
- Learning to Map by Discovering Lane Topology [Namdar]
- 3D-LaneNet: End-to-End 3D Multiple Lane Detection [ICCV’19, Namdar]
- Globally consistent map [Joey Yu];
- Deep structured 3D Estimation [Mini-Conf];
	- Input: stereo images, LiDAR; Output: Pose, Shape
- Robust Dense Mapping for Large-Scale Dynamic Environments [ICRA’18, Barsan]

## Localization:
- Image Localization [Julieta Martinez]
- Ground Intensity LiDAR Localization with Compressed Maps [Xinkai Wei]
- Learning to Map [Xinkai Wei]
- Learning to Localize through Compressed Binary Maps [Xinkai Wei]
