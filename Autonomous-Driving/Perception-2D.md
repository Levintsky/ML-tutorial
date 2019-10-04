# Perception 2D

## Detection
- **MultiBin**: A Mousavian, D Anguelov, J Flynn, and J Kosecka. 3d bounding box estimation using deep learning and geometry. CVPR'17
	- **Geometry constraint**: Perspective projection of a 3D bounding box should fit tightly within its 2D detection window
	- Detect 2D bounding box first;
	- Estimate: center T = (tx,ty,tz), dimension D = (dx,dy,dz), rotation R, (R, T) in SE(3), Regress the box dimensions D rather than translation T
	- Point-to-point correspondence constraint:
	- Network structure: backbone CNN outputs feature 512 x 7 x 7, then three heads:
		- orientation: MLP -> bins x 2 for sin, cos
		- confidence: MLP -> bins, loss: cross-entropy
		- dimension: MLP -> 3, loss: MSE
	- Experiments: Kitti, PASCAL-3D;
	<img src="/Autonomous-Driving/images/detection/waymo-multibin1.png" alt="drawing" width="400"/>
	<img src="/Autonomous-Driving/images/detection/waymo-multibin2.png" alt="drawing" width="400"/>
	<img src="/Autonomous-Driving/images/detection/waymo-multibin3.png" alt="drawing" width="400"/>

## Semantic Segmentation
- **UPSNet**: Y Xiong, R Liao, H Zhao, R Hu, M Bai, E Yumer, R Urtasun. UPSNet: A Unified Panoptic Segmentation Network. CVPR'19
	- Problem setup: semantic seg + instance seg;
	- https://github.com/uber-research/UPSNet
	- Cityscapes, COCO

## Misc
- SBNet: Leveraging Activation Block Sparsity for Speeding up Convolutional Neural Networks. Mengye Ren, Andrei Pokrovsky, Bin Yang, and Raquel Urtasun

## Lane Detection
- M. Bai, G. Mattyus, N. Homayounfar, S. Wang, S. K. Lakshmikanth, R. Urtasun. Deep Multi-Sensor Lane Detection. IROS'18
- J Liang, N Homayounfar, WC Ma, S Wang, R Urtasun. Convolutional Recurrent Network for Road Boundary Extraction. CVPR'19