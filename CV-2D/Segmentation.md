# Segmentation

## Benchmarks
- German Ros, Laura Sellart, Joanna Materzynska, David Vazquez, and Antonio M. Lopez. The synthia dataset: A large collection of synthetic images for semantic segmentation of urban scenes. CVPR'16

## Basics
- Rick Szeliski (Chap 5)
- Active contours;
	- Snakes;
	- Dynamic snakes and CONDENSATION;
	- Scissors;
	- Level Sets;
		- Assume that the embedding function φ is a sdf away from the curve, in which case |φ| = 1
		- The first term in Equation moves the curve in the direction of its curvature, i.e., it acts to straighten the curve, under the influence of the modulation function g(I).
		- The second term moves the curve down the gradient of g(I), encouraging the curve to migrate towards minima of g(I)
		<img src="/CV-2D/images/segmentation/level-set.png" alt="drawing" width="500"/>
	- Application: Contour tracking and rotoscoping;
- Split and merge;
	- Watershed;
	- Region splitting (divisive clustering);
	- Region merging (agglomerative clustering);
	- Graph-based segmentation;
	- Probabilistic aggregation;
- Mean shift and mode finding
	- K-means and mixtures of Gaussians
	- Mean shift
- Normalized cuts
- Graph cuts and energy-based methods;

## Semantic Segmentation
- **SegNet**: V. Badrinarayanan, A. Kendall, and R. Cipolla. SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation. 2015
-  A. Kendall, V. Badrinarayanan, and R. Cipolla. Bayesian Segnet: Model Uncertainty in Deep Convolutional EncoderDecoder Architectures for Scene Understanding. 2015
- **U-Net**: O Ronneberger, P Fischer, T Brox: Convolutional Networks for Biomedical Image Segmentation, MICCAI'15
- **FCN**: J. Long, E. Shelhamer, and T. Darrell. Fully convolutional networks for semantic segmentation. CVPR'15
	- https://github.com/wkentaro/pytorch-fcn
	- https://github.com/shelhamer/fcn.berkeleyvision.org
	- Pyramid (like SSD)
- **DeepLab v3**: L Chen, G Papandreou, F Schroff, H Adam. Rethinking Atrous Convolution for Semantic Image Segmentation. 2017
	- https://github.com/tensorflow/models/tree/master/research/deeplab
- **PSP**: H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia. Pyramid Scene Parsing Network. CVPR'17
- ResNet-DUC: P Wang, P Chen, Y Yuan, D Liu, Z Huang, X Hou, G Cottrell. Understanding Convolution for Semantic Segmentation. WAVC'18
	- **Dilated Conv**
- Z Cheng, Y Wu, Z Xu, T Lukasiewicz, W Wang. Segmentation Is All You Need. 2019
	- No bounding-box, NMS, anchor;
- A Probabilistic U-Net for Segmentation of Ambiguous Images. NIPS'18

## Instance Segmentation
- Proposals:
	- **DeepMask**: Pedro H. O. Pinheiro, Ronan Collobert, and Piotr Dollar. Learning to segment object candidates. NIPS'15
	- Trained jointly with two objectives:
		- Given an image patch, outputs a class-agnostic segmentation mask;
		- the likelihood of the patch being centered on a full object
	- **SharpMask**: Pedro O. Pinheiro, Tsung-Yi Lin, Ronan Collobert, Piotr Dollar. Learning to refine object segments. ECCV'16
- Top down (prior bounding box):
	- **FCIS**: Yi Li, Haozhi Qi, Jifeng Dai, Xiangyang Ji, and Yichen Wei. Fully convolutional instance-aware semantic segmentation. CVPR'17
	- Mask R-CNN: ICCV'17
	- **PANet**: Shu Liu, Lu Qi, Haifang Qin, Jianping Shi, and Jiaya Jia. Path aggregation network for instance segmentation. CVPR'18
	- **Mask Scoring R-CNN**: Zhaojin Huang, Lichao Huang, Yongchao Gong, Chang Huang, and Xinggang Wang. Mask scoring R-CNN. CVPR'19
	- **Tensormask**: Xinlei Chen, Ross Girshick, Kaiming He, and Piotr Dollar. Tensormask: A foundation for dense object segmentation. ICCV'19
		- https://github.com/facebookresearch/detectron2/tree/master/projects/TensorMask
		- Insight: first one-stage instance segmentation;
		- Similar to instanceFCN, but generalize to UxV;\
			<img src="/CV-2D/images/segmentation/tensormask.png" alt="drawing" width="400"/>
- Bottom-up (grouping):
	- Alejandro Newell, Zhiao Huang, and Jia Deng. Associative embedding: End-to-end learning for joint detection and grouping. NIPS'17
	- Bert De Brabandere, Davy Neven, and Luc Van Gool. Semantic instance segmentation with a discriminative loss function. 2017
	- **SGN**: Shu Liu, Jiaya Jia, Sanja Fidler, and Raquel Urtasun. Sgn: Sequential grouping networks for instance segmentation. ICCV'17
	- **SSAP**: Naiyu Gao, Yanhu Shan, Yupei Wang, Xin Zhao, Yinan Yu, Ming Yang, and Kaiqi Huang. Ssap: Single-shot instance segmentation with affinity pyramid. ICCV'19
- J Dai, K He, and J Sun. Instance-aware semantic segmentation via multi-task network cascades. CVPR'16
- Y Li, H Qi, J Dai, X Ji, and Y Wei. Fully Convolutional Instance-aware Semantic Segmentation. CVPR'17
- **SOLO**: Xinlong Wang, Tao Kong, Chunhua Shen, Yuning Jiang, Lei Li. SOLO: Segmenting Objects by Locations. 2020
	- S x S cells, each object instance assigned to one cell;
	- Model:\
		<img src="/CV-2D/images/segmentation/solo.png" alt="drawing" width="500"/>
	- Supervision: category (focal loss) + mask (Dice Loss)

## Panoptic
- Problem definition:
	- Things: countable (instance-level)
	- Stuff: semantic (sky, grassland, road)
	- Metric: PQ (panoptic quality):\
		<img src="/CV-2D/images/segmentation/pq.png" alt="drawing" width="350"/>
- Dataset:
	- Cityscapes: 5000 street view images;
	- ADE20k:
	- Mapillary Vistas;
	- COCO:
- Alexander Kirillov, Kaiming He, Ross Girshick, Carsten Rother, Piotr Dollár. Panoptic Segmentation. CVPR'19
	- Mask-RCNN for instance and semantic for stuff;
		<img src="/CV-2D/images/segmentation/panoptic-fpn.png" alt="drawing" width="500"/>

## Level Set
- Resources:
	- https://www.cnblogs.com/avin/p/6713660.html
	- https://www.zhihu.com/question/22608763
- Tutorial: 
	- Daniel Cremers. Level Set Methods in Computer Vision. ECCV'06
- D Cremers, M Rousson, R Deriche. A Review of Statistical Approaches to Level Set Segmentation: Integrating color, texture, motion and shape. IJCV'06
- Ping Hu, Bing Shuai, Jun Liu, Gang Wang. Deep Level Sets for Salient Object Detection. CVPR'17