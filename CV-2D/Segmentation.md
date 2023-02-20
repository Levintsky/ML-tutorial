# Segmentation

## Benchmarks
- G Ros, L Sellart, J Materzynska, D Vazquez, and A Lopez. The synthia dataset: A large collection of synthetic images for semantic segmentation of urban scenes. CVPR'16
- Panoptic:
	- Cityscapes: 5000 street view images;
	- ADE20k:
		- B Zhou, H Zhao, X Puig, S Fidler, A Barriuso and A Torralba. Scene Parsing through ADE20K Dataset. CVPR'17
		- B Zhou, H Zhao, X Puig, T Xiao, Sanja Fidler, A Barriuso and A Torralba. Semantic Understanding of Scenes through ADE20K Dataset. IJCV
		- http://groups.csail.mit.edu/vision/datasets/ADE20K/
		- 25k images, 19.6 instances, 10.6 object classes each image;
	- Mapillary Vistas;
	- COCO:

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
- A. Kendall, V. Badrinarayanan, and R. Cipolla. Bayesian Segnet: Model Uncertainty in Deep Convolutional EncoderDecoder Architectures for Scene Understanding. 2015
- **U-Net**: O Ronneberger, P Fischer, T Brox: Convolutional Networks for Biomedical Image Segmentation, MICCAI'15
- **FCN**: J. Long, E. Shelhamer, and T. Darrell. Fully convolutional networks for semantic segmentation. CVPR'15
	- https://github.com/wkentaro/pytorch-fcn
	- https://github.com/shelhamer/fcn.berkeleyvision.org
	- Pyramid (like SSD)
- DeepLab series:
	- **DeepLab-v1**: L Chen, G Papandreou, I Kokkinos, K Murphy, and A Yuille. Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs. ICLR'15
		- VGG-16 + dilated-conv + 8x bilinear upsampling + CRF + FCN (multi-scale)
		- https://github.com/kazuto1011/deeplab-pytorch/tree/master/libs/models
	- **DeepLab-v2**: L Chen, G Papandreou, I Kokkinos, K Murphy, A Yuille. DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs. 2017
		- ASPP（Atrous Spacial Pyramid Pooling
		- ResNet;
	- **DeepLab-v3**: L Chen, G Papandreou, F Schroff, H Adam. Rethinking Atrous Convolution for Semantic Image Segmentation. 2017
		- https://github.com/tensorflow/models/tree/master/research/deeplab
		- Multigrid;
	- **DeepLab-v3+**: L Chen, Y Zhu, G Papandreou, F Schroff, H Adam. Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation. ECCV'18
- **PSP**: H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia. Pyramid Scene Parsing Network. CVPR'17
- ResNet-DUC: P Wang, P Chen, Y Yuan, D Liu, Z Huang, X Hou, G Cottrell. Understanding Convolution for Semantic Segmentation. WAVC'18
	- **Dilated Conv**
- A Probabilistic U-Net for Segmentation of Ambiguous Images. NIPS'18
- Z Cheng, Y Wu, Z Xu, T Lukasiewicz, W Wang. Segmentation Is All You Need. 2019
	- No bounding-box, NMS, anchor;
- T He, C Shen, Z Tian, D Gong, C Sun, and Y Yan. Knowledge adaptation for efficient semantic segmentation. CVPR'19
- Y Liu, K Chen, C Liu, Z Qin, Z Luo, and J Wang. Structured knowledge distillation for semantic segmentation. CVPR'19

## Instance Segmentation
- Proposals:
	- **DeepMask**: P Pinheiro, R Collobert, and P Dollar. Learning to segment object candidates. NIPS'15
	- Trained jointly with two objectives:
		- Given an image patch, outputs a class-agnostic segmentation mask;
		- the likelihood of the patch being centered on a full object
	- **SharpMask**: P Pinheiro, T Lin, R Collobert, P Dollar. Learning to refine object segments. ECCV'16
- Top down (prior bounding box):
	- **FCIS**: Y Li, H Qi, J Dai, X Ji, and Y Wei. Fully convolutional instance-aware semantic segmentation. CVPR'17
	- Mask R-CNN: ICCV'17
	- **PANet**: S Liu, L Qi, H Qin, J Shi, and J Jia. Path aggregation network for instance segmentation. CVPR'18
	- **Mask Scoring R-CNN**: Z Huang, L Huang, Y Gong, C Huang, and X Wang. Mask scoring R-CNN. CVPR'19
	- **Tensormask**:  Chen, R Girshick, K He, and P Dollar. Tensormask: A foundation for dense object segmentation. ICCV'19
		- https://github.com/facebookresearch/detectron2/tree/master/projects/TensorMask
		- Insight: first one-stage instance segmentation;
		- Similar to instanceFCN, but generalize to UxV;\
			<img src="/CV-2D/images/segmentation/tensormask.png" alt="drawing" width="400"/>
- Bottom-up (grouping):
	- A Newell, Z Huang, and J Deng. Associative embedding: End-to-end learning for joint detection and grouping. NIPS'17
	- B Brabandere, D Neven, and L V Gool. Semantic instance segmentation with a discriminative loss function. 2017
	- **SGN**: S Liu, J Jia, S Fidler, and R Urtasun. Sgn: Sequential grouping networks for instance segmentation. ICCV'17
	- **SSAP**: N Gao, Y Shan, Y Wang, X Zhao, Y Yu, M Yang, and K Huang. Ssap: Single-shot instance segmentation with affinity pyramid. ICCV'19
- J Dai, K He, and J Sun. Instance-aware semantic segmentation via multi-task network cascades. CVPR'16
- Y Li, H Qi, J Dai, X Ji, and Y Wei. Fully Convolutional Instance-aware Semantic Segmentation. CVPR'17
- **SOLO**: X Wang, T Kong, C Shen, Y Jiang, L Li. SOLO: Segmenting Objects by Locations. 2020
	- S x S cells, each object instance assigned to one cell;
	- Model:\
		<img src="/CV-2D/images/segmentation/solo.png" alt="drawing" width="500"/>
	- Supervision: category (focal loss) + mask (Dice Loss)
- PointRend: A Kirillov, Y Wu, K He, R Girshick. PointRend: Image Segmentation as Rendering. CVPR'20
	- Insight: coarse-to-fine and focus on undecided points (with MLP);
		<img src="/CV-2D/images/segmentation/pointrend.png" alt="drawing" width="500"/>

## Panoptic
- Problem definition:
	- Things: countable (instance-level)
	- Stuff: semantic (sky, grassland, road)
	- Metric: PQ (panoptic quality):\
		<img src="/CV-2D/images/segmentation/pq.png" alt="drawing" width="350"/>
- Alexander Kirillov, Kaiming He, Ross Girshick, Carsten Rother, Piotr Dollár. Panoptic Segmentation. CVPR'19
	- Mask-RCNN for instance and semantic for stuff;\
		<img src="/CV-2D/images/segmentation/panoptic-fpn.png" alt="drawing" width="500"/>

## Level Set
- Resources:
	- https://www.cnblogs.com/avin/p/6713660.html
	- https://www.zhihu.com/question/22608763
- Tutorial: 
	- Daniel Cremers. Level Set Methods in Computer Vision. ECCV'06
- D Cremers, M Rousson, R Deriche. A Review of Statistical Approaches to Level Set Segmentation: Integrating color, texture, motion and shape. IJCV'06
- P Hu, B Shuai, J Liu, G Wang. Deep Level Sets for Salient Object Detection. CVPR'17