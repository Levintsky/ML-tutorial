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
	- Experiments: Kitti, PASCAL-3D;\
		<img src="/Autonomous-Driving/images/detection/waymo-multibin1.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/detection/waymo-multibin2.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/detection/waymo-multibin3.png" alt="drawing" width="400"/>

## Segmentation
- **MultiNet**: Marvin Teichmann, Michael Weber, Marius Zollner, Roberto Cipolla and Raquel Urtasun. MultiNet: Real-time Joint Semantic Reasoning for Autonomous Driving. IV'18
	- https://github.com/MarvinTeichmann/MultiNet
	- The encoder is shared amongst the three tasks
	- Joint classification, detection and semantic segmentation via a unified architecture;
- **DARNet**: Dominic Cheng, Renjie Liao, Sanja Fidler, Raquel Urtasun. DARNet: Deep Active Ray Network for Building Segmentation. CVPR'19
- **UPSNet**: Y Xiong, R Liao, H Zhao, R Hu, M Bai, E Yumer, R Urtasun. UPSNet: A Unified Panoptic Segmentation Network. CVPR'19
	- Problem setup: semantic seg + instance seg (Mask R-CNN);
		- Countable things: people, bicycle, car (thing);
		- Uncountable: skye, grass (stuff);
	- Overall:\
		<img src="/Autonomous-Driving/images/detection/upsnet.png" alt="drawing" width="500"/>
	- Backbone: resnet + FPN;
	- Segmentation head: Deformable Conv [J. Dai] takes multi-scale FPN as input, 1x1 conv, softmax;
		- As good as a separate model (PSPNet);\
		<img src="/Autonomous-Driving/images/detection/upsnet-sem.png" alt="drawing" width="400"/>
	- Panoptic head: (N-stuff + N-thing) channel x H x W;\
		<img src="/Autonomous-Driving/images/detection/upsnet-pan.png" alt="drawing" width="400"/>	
	- https://github.com/uber-research/UPSNet
	- Cityscapes, COCO
- K Lis, K Nakka, P Fua, M Salzmann. Detecting the Unexpected via Image Resynthesis. 2019
	- Segmentation model: SegNet or PSP;
	<img src="/Autonomous-Driving/images/vision2d/anomaly1.png" alt="drawing" width="450"/>
	<img src="/Autonomous-Driving/images/vision2d/anomaly2.png" alt="drawing" width="450"/>
- Justin Liang, Namdar Homayounfar, Wei-Chiu Ma, Yuwen Xiong, Rui Hu, Raquel Urtasun. PolyTransform: Deep Polygon Transformer for Instance Segmentation. CVPR'20
- Level-Set R-CNN [Namdar];
- Efficient Convolutions for Real-Time Semantic Segmentation of 3D Point Clouds [3DV’18, C Zhang]
- **DSAC**: D. Marcos, D. Tuia, B. Kellenberger, L. Zhang, M. Bai, R. Liao and R. Urtasun. Learning deep structured active contours end-to-end. CVPR'18
	- Check mapping for details;
- Deep Parametric Continuous Convolutional Neural Networks [CVPR’18, Shenlong]
- SurfConv: Bridging 3D and 2D Convolution for RGBD Images [CVPR’18, H Chu]

## Misc
- Mengye Ren, Andrei Pokrovsky, Bin Yang, and Raquel Urtasun. SBNet: Leveraging Activation Block Sparsity for Speeding up Convolutional Neural Networks. 
