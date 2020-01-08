# Detection, Semantic-Segmentation

## Metrics
- mAP (average of the maximum precisions at different recall values)

## Benchmarks
- **PASCAL-VOC**: M. Everingham, L. Van Gool, C. K. Williams, J. Winn, and A. Zisserman. The pascal visual object classes (voc) challenge. IJCV'10
- **COCO**: T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollar, and C. L. Zitnick. Microsoft coco: Common objects in context. ECCV'14

## Summaries
- A very good blog (Lilian Weng, OpenAI): https://lilianweng.github.io/lil-log/2017/10/29/object-recognition-for-dummies-part-1.html
- One stage: https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html

## Detection
- Two-stages:
	- RCNN family:
		<img src="/CV-2D/images/detection/rcnn-family-summary.png" alt="drawing" width="650"/>
	- **R-CNN**: R. Girshick, J. Donahue, T. Darrell, and J. Malik. Rich feature hierarchies for accurate object detection and semantic segmentation. CVPR'14
		- Pretrain CNN;
		- **Selective search**: 2000 proposals;
		- Warp, CNN-preprocessing, K+1 classes (bg);
		- Binary-SVM for each class
		- Regression loss: bbox for delta, (x, y, h, w)
		- **NMS**: In IoU > 0.5 regions, select highest score;
	    - **Hard Negative Mining**;
		- **PASCAL-VOC: 54.2% (2007), 50.2% (2010), 49.6% (2012)**
		- **ImageNet 200: 31.4%**
		<img src="/CV-2D/images/detection/RCNN.png" alt="drawing" width="600"/>
		<img src="/CV-2D/images/detection/RCNN-eqn.png" alt="drawing" width="400"/>
	- **Fast R-CNN**: R. Girshick. Fast R-CNN. ICCV'15
		- **Selective search**
		- Backbone CNN, last max-pooling to RoIPooling;
		- RoIPool to a fixed spatial extent W x H (7x7);
		- Faster, better accuracy;
		- Loss 1: (K+1) class on each RoI;
		- Loss 2: L1-loss; bounding-box regression (x, y, w, h);
		- **PASCAL-VOC: 66.9% (2007), 66.1% (2010), 65.7% (2012)**
		- **COCO: mAP 35.9%**
		<img src="/CV-2D/images/detection/fast-RCNN.png" alt="drawing" width="600"/>
		<img src="/CV-2D/images/detection/fast-RCNN-eqn.png" alt="drawing" width="500"/>
	- **Faster R-CNN**: S. Ren, K. He, R. Girshick, and J. Sun. Faster r-cnn: Towards real-time object detection with region proposal networks. NIPS 2015 
		- https://github.com/mahyarnajibi/fast-rcnn-torch
		- https://github.com/chenyuntc/simple-faster-rcnn-pytorch
		- Two stages:
		- Stage 0: Pretrain CNN
		- Stage 0.1: backbone CNN (VGG, ResNet, conv1, 2, 3), output 14 x 14 feature map
		- Stage 1: Train **RPN** (binary attention)
			- Two heads classification (3 scales x 3 ratios);
			- IoU > 0.7: positive; < 0.3: negative;
			- Bbox Regression loss for delta: Anchor k -> 4k; (x, y, w, h), WHk anchors in total;
		- Stage 2: Train R-CNN with the proposals generated
			- RPN step:
				- for each i in (H, W), generate anchor-boxes -> Apply delta -> clip -> remove too small boxes (w, h) -> sort by score, choose top-N -> NMS (IoU > 0.7, select highest) -> return ROIs, Scores
			- Finetune R-CNN;
				- Apply cascaded removal;
				- base-feature -> [ROI-crop or ROI-pool or ROI-align] -> pooled feature;
				- Apply conv4/5 (backbone only has conv1/2/3)
		- Iterate 1 and 2;
		- **PASCAL-VOC mAP: 73.2% (2007), 73.2% (2012)**
		<img src="/CV-2D/images/detection/faster-RCNN.png" alt="drawing" width="600"/>
		<img src="/CV-2D/images/detection/faster-RCNN-eqn.png" alt="drawing" width="500"/>
	- **R-FCN**: J. Dai, Y. Li, K. He, and J. Sun. R-fcn: Object detection via region-based fully convolutional networks. NIPS'16
	- **FPN**: T.-Y. Lin, P. Dollar, R. Girshick, K. He, B. Hariharan, and S. Belongie. Feature pyramid networks for object detection. CVPR'17
	- **Mask R-CNN**: Kaiming He, Georgia Gkioxari, Piotr Dollár, Ross Girshick. Mask R-CNN. ICCV'17
		- ROI-Align (improves mask accuracy by 10%-15%): solved quantization error
		- Decouple mask and class
		- Loss: cls + box + mask
			- cls, box (same as faster R-CNN)
			- mask: K * m^2 (K class, m resolution)
		- Experiments:
			- COCO instance segmentation
			- COCO keypoint
		- Speed: 5fps
		<img src="/CV-2D/images/detection/mask-rcnn.png" alt="drawing" width="600"/>
		<img src="/CV-2D/images/detection/mask-rcnn-eqn.png" alt="drawing" width="500"/>
	- **Detectron**: https://github.com/facebookresearch/Detectron
	- **RetinaNet**: Tsung-Yi Lin Priya Goyal Ross Girshick Kaiming He Piotr Dollar. Focal Loss for Dense Object Detection. ICCV 2017
		- Reduce loss for well-classified classes; focus on harder classes;
		- Foreground/background imbalance;
		- gamma=1: normal Cross-Entropy, in paper, alpha=0.25, gamma=2 is used.
		<img src="/CV-2D/images/detection/focal-loss.png" alt="drawing" width="500"/>
- One-stage detector:
	- SSD:
		- W. Liu, D. Anguelov, D. Erhan, C. Szegedy, and S. Reed. SSD: Single shot multibox detector. ECCV'16
			<img src="/CV-2D/images/detection/ssd.png" alt="drawing" width="600"/>
			<img src="/CV-2D/images/detection/ssd-eqn.png" alt="drawing" width="600"/>
		- Improves YOLO by using default k bounding boxes: each cell output (c+4)k, c classes + 4 offsets
		- Multiscalex
		- **DSSD**: C.-Y. Fu, W. Liu, A. Ranga, A. Tyagi, and A. C. Berg. DSSD: Deconvolutional single shot detector. 2016
	- YOLO:
		- **Darknet**: J. Redmon. Darknet: Open source neural networks in c.
			- http://pjreddie.com/darknet/
		- **YOLO**: J. Redmon, S. Divvala, R. Girshick, and A. Farhadi. You only look once: Unified, real-time object detection. CVPR 2016
			- https://pjreddie.com/darknet/yolo/
			- Pretrain CNN.
			- S x S cells, each cell predict the object if the object center is in the cell. (S=7, B=2, C=20 in Yolo-v1)
			- Each cell:
				- Location of B Bboxes: 5 predictions (x, y, w, h, confidence)
				- Confidence score: p = p(object) * IoU(pred, truth)
				- Each grid cell makes 1 prediction: p(class = ci | contains an object). Regardless of bounding boxes number b.
			- Final output: 7 x 7 x 30
			<img src="/CV-2D/images/detection/yolo1.png" alt="drawing" width="500"/>
			<img src="/CV-2D/images/detection/yolo1-2.png" alt="drawing" width="500"/>
		- **YOLO9000**: J. Redmon and A. Farhadi. YOLO9000: Better, faster, stronger. CVPR 2017
			- Better:
				- Batch normalization
				- Multi-scale training: finetune on 448 x 448
				- Anchor boxes: input 416 x 416, 32 downsampling, output 13 x 13
				- Dimension Clusters
				- Direct location prediction
				- Multi-Scale training
			- Faster:
				- VGG-16, DarkNet-19
			- Stronger
				- Hierarchical classification
			<img src="/CV-2D/images/detection/yolo2.png" alt="drawing" width="400"/>
		- **YOLOv3**: J. Redmon and A. Farhadi. Yolov3: An incremental improvement. 2018
			- 320 x 320: 22ms
			- Logistic regression:
			- Class prediction:
			- No hard negative mining;
			- Things do not work: Anchor box x,y offset; Linear x,y instead of logistic; focal loss; dual IoU threshold;
			<img src="/CV-2D/images/detection/yolo3.png" alt="drawing" width="200"/>
	- Mingxing Tan, Ruoming Pang, Quoc V. Le. EfficientDet: Scalable and Efficient Object Detection. 2019
- Proposals:
	- **Selective Search**: J. R. Uijlings, K. E. van de Sande, T. Gevers, and A. W. Smeulders. Selective search for object recognition. IJCV 2013
	- **EdgeBoxes**:  C. L. Zitnick and P. Dollar. Edge boxes: Locating object proposals from edges. ECCV 2014
	- **DeepMask**:
		- P. O. Pinheiro, R. Collobert, and P. Dollar. Learning to segment object candidates. NIPS 2015
		- P. O. Pinheiro, T.-Y. Lin, R. Collobert, and P. Dollar. Learning to refine object segments. ECCV 2016
	- **RPN**
- MSRA:
	- H Hu, J Gu, Z Zhang, J Dai, and Y Wei. Relation Networks for Object Detection. CVPR'18

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
- J Dai, K He, and J Sun. Instance-aware semantic segmentation via multi-task network cascades. CVPR'16
- Y Li, H Qi, J Dai, X Ji, and Y Wei. Fully Convolutional Instance-aware Semantic Segmentation. CVPR'17
- Shu Liu, Jiaya Jia, Sanja Fidler, and Raquel Urtasun. Sgn: Sequential grouping networks for instance segmentation. ICCV'17
- Alexander Kirillov, Kaiming He, Ross Girshick, Carsten Rother, Piotr Dollár. Panoptic Segmentation. 2019

## Face Detection and Recognition
- Y Taigman, M Yang, M Ranzato, L Wolf. DeepFace: Closing the Gap to Human-Level Performance in Face Verification. CVPR'14
- F Schroff, D Kalenichenko, J Philbin. FaceNet: A Unified Embedding for Face Recognition and Clustering. CVPR'15
