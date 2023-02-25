# Perception 2D

## Detection
- MultiBin: Waymo 3d bounding box estimation using deep learning and geometry. CVPR'17
	- Insight: (Geometry constraint) Perspective projection of a 3D bounding box should fit tightly within its 2D detection window
	- Estimate: center T = (tx,ty,tz), D = (dx,dy,dz), rotation R, (R, T) in SE(3), Regress the box dimensions D rather than translation T
	- Detect 2D bounding box first;
	- Point-to-point correspondence constraint:
	- Network structure: backbone CNN outputs feature 512 x 7 x 7, then three heads:
		- orientation: MLP -> bins x 2 for sin, cos
		- confidence: MLP -> bins, loss: cross-entropy
		- dimension: MLP -> 3, loss: MSE
	- Experiments: Kitti, PASCAL-3D;

## Segmentation
- MultiNet: Uber-ATG. MultiNet: Real-time Joint Semantic Reasoning for Autonomous Driving. IV'18
	- https://github.com/MarvinTeichmann/MultiNet
	- The encoder is shared amongst the three tasks
	- Joint classification, detection and semantic segmentation via a unified architecture;
- DARNet: Uber-ATG. DARNet: Deep Active Ray Network for Building Segmentation. CVPR'19
- UPSNet: Uber-ATG. UPSNet: A Unified Panoptic Segmentation Network. CVPR'19
	- Problem setup: semantic seg + instance seg (Mask R-CNN);
		- Countable things: people, bicycle, car (thing);
		- Uncountable: skye, grass (stuff);
	- Backbone: ResNet + FPN;
	- Segmentation head: Deformable Conv [J. Dai] takes multi-scale FPN as input, 1x1 conv, softmax;
		- As good as a separate model (PSPNet);
	- Panoptic head: (N-stuff + N-thing) channel x H x W;
	- https://github.com/uber-research/UPSNet
	- Cityscapes, COCO
- K Lis, K Nakka, P Fua, M Salzmann. Detecting the Unexpected via Image Resynthesis. 2019
	- Framework:
		- Image -> [Seg] -> semantic-seg
		- sem-seg -> [GAN] -> Fake-img
		- Fake-im - Real-im -> Anomaly
	- Segmentation model: SegNet or PSP;
- Uber-ATG. PolyTransform: Deep Polygon Transformer for Instance Segmentation. CVPR'20
- Level-Set R-CNN [Namdar];
- DSAC: Uber-ATG. Learning deep structured active contours end-to-end. CVPR'18
	- Check mapping for details;
- Deep Parametric Continuous Convolutional Neural Networks [CVPR’18, Shenlong]
- SurfConv: Bridging 3D and 2D Convolution for RGBD Images [CVPR’18, H Chu]

## Misc
- Uber-ATG. SBNet: Leveraging Activation Block Sparsity for Speeding up Convolutional Neural Networks. 
