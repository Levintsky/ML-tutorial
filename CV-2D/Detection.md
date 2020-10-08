# Detection

## Basics
- Evaluation:
	- Average Precision (AP):
		- PR-curve: Precision against recall;
		- ROC: true positive rate (TPR) against the false positive rate (FPR)\
			<img src="/CV-2D/images/detection/Roccurves.png" alt="drawing" width="350"/>
			<img src="/CV-2D/images/detection/precision-recall.png" alt="drawing" width="350"/>
	- mAP (average of the maximum precisions at different recall values)
		- PR-Curve by averaging IOU of 0.5 to 0.95:\
			<img src="/CV-2D/images/detection/pr-curve.png" alt="drawing" width="350"/>
- Benchmarks
	- **PASCAL-VOC**: M. Everingham, L. Van Gool, C. K. Williams, J. Winn, and A. Zisserman. The pascal visual object classes (voc) challenge. IJCV'10
	- **COCO**: T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollar, and C. L. Zitnick. Microsoft coco: Common objects in context. ECCV'14

## Summaries
- A very good blog (Lilian Weng, OpenAI): https://lilianweng.github.io/lil-log/2017/10/29/object-recognition-for-dummies-part-1.html
- One stage: https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html

## Detectron
- Detectron v1: https://github.com/facebookresearch/Detectron
	- Fast R-CNN;
	- Faster R-CNN;
	- Residual-Net;
	- R-FCN;
	- ResNext;
	- FPN CVPR'17;
	- Georgia Gkioxari, Ross Girshick, Piotr Dollár, and Kaiming He. Detecting and Recognizing Human-Object Interactions. Tech report, arXiv'17
	- Priya Goyal, Piotr Dollár, Ross Girshick, Pieter Noordhuis, Lukasz Wesolowski, Aapo Kyrola, Andrew Tulloch, Yangqing Jia, and Kaiming He. Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour. Tech report, arXiv'17
	- Focal-loss ICCV'17;
	- Mask R-CNN;
	- Non-Local Neural Networks;
	- Ronghang Hu, Piotr Dollár, Kaiming He, Trevor Darrell, and Ross Girshick. Learning to Segment Every Thing. Tech report, arXiv'17.
	- Ilija Radosavovic, Piotr Dollár, Ross Girshick, Georgia Gkioxari, and Kaiming He. Data Distillation: Towards Omni-Supervised Learning. Tech report, arXiv, Dec. 2017.
- Detectron v2: https://github.com/facebookresearch/detectron2
	- DensePose: Dense Human Pose Estimation In The Wild
	- Scale-Aware Trident Networks for Object Detection
	- TensorMask: A Foundation for Dense Object Segmentation
	- Mesh R-CNN
	- PointRend: Image Segmentation as Rendering
	- Momentum Contrast for Unsupervised Visual Representation Learning

## Two-Stage
- RCNN family:\
	<img src="/CV-2D/images/detection/rcnn-family-summary.png" alt="drawing" width="650"/>
- D. Erhan, C. Szegedy, A. Toshev, and D. Anguelov. Scalable object detection using deep neural networks. CVPR'14
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
- **SPP**: K. He, X. Zhang, S. Ren, and J. Sun. Spatial pyramid pooling in deep convolutional networks for visual recognition. ECCV'14
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
- **Faster R-CNN**: S. Ren, K. He, R. Girshick, and J. Sun. Faster r-cnn: Towards real-time object detection with region proposal networks. NIPS'15 
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
- A. Shrivastava, R. Sukthankar, J. Malik, and A. Gupta. Beyond skip connections: Top-down modulation for object detection. arxiv'16
- **FPN**: T.-Y. Lin, P. Dollar, R. Girshick, K. He, B. Hariharan, and S. Belongie. Feature pyramid networks for object detection. CVPR'17
	<img src="/CV-2D/images/detection/fpn.png" alt="drawing" width="500"/>
- **Mask R-CNN**: Kaiming He, Georgia Gkioxari, Piotr Dollár, Ross Girshick. Mask R-CNN. ICCV'17
	- ROI-Align (improves mask accuracy by 10%-15%): solved quantization error
	- Decouple mask and class
	- Loss: cls + box + mask
		- cls, box (same as faster R-CNN)
		- mask: K * m^2 (K class, m resolution)
	- Experiments:
		- COCO instance segmentation
		- COCO keypoint
	- Speed: 5fps\
	<img src="/CV-2D/images/detection/mask-rcnn.png" alt="drawing" width="500"/>
	<img src="/CV-2D/images/detection/mask-rcnn-eqn.png" alt="drawing" width="500"/>

## One-stage detector
- J. Huang, V. Rathod, C. Sun, M. Zhu, A. Korattikara, A. Fathi, I. Fischer, Z. Wojna, Y. Song, S. Guadarrama, and K. Murphy. Speed/accuracy trade-offs for modern convolutional object detectors. CVPR'17
- **RetinaNet**: Tsung-Yi Lin Priya Goyal Ross Girshick Kaiming He Piotr Dollar. Focal Loss for Dense Object Detection. ICCV'17
	- Insight: solve difficulty imbalance;
	- Reduce loss for well-classified classes; focus on harder classes;
	- Foreground/background imbalance;
	- gamma=1: normal Cross-Entropy, in paper, alpha=0.25, gamma=2 is used;
	<img src="/CV-2D/images/detection/focal-loss.png" alt="drawing" width="500"/>
- SSD:
	- **SSD**: W. Liu, D. Anguelov, D. Erhan, C. Szegedy, and S. Reed. SSD: Single shot multibox detector. ECCV'16
		- Default k bounding boxes: each cell output (c+4)k, c classes + 4 offsets
		- Multiscale: FPN;
			<img src="/CV-2D/images/detection/ssd.png" alt="drawing" width="500"/>\
			<img src="/CV-2D/images/detection/ssd-eqn.png" alt="drawing" width="500"/>
	- **DSSD**: C.-Y. Fu, W. Liu, A. Ranga, A. Tyagi, and A. C. Berg. DSSD: Deconvolutional single shot detector. 2016
- YOLO:
	- Summaries:
		- https://zhuanlan.zhihu.com/p/136382095
		- https://zhuanlan.zhihu.com/p/94986199
	- **Darknet**: J. Redmon. Darknet: Open source neural networks in c.
		- http://pjreddie.com/darknet/
	- **YOLOv1**: J. Redmon, S. Divvala, R. Girshick, and A. Farhadi. You only look once: Unified, real-time object detection. CVPR 2016
		- https://pjreddie.com/darknet/yolo/
		- Pretrain CNN.
		- S x S cells, each cell predict the object if the object center is in the cell. (S=7, B=2, C=20 in Yolo-v1)
		- Each cell:
			- Location of B Bboxes: B=5 predictions (x, y, w, h, confidence)
			- Confidence score: p = p(object) * IoU(pred, truth)
			- Each grid cell makes 1 prediction: p(class = ci | contains an object). Regardless of bounding boxes number b.
		- Final output: S x S x B bounding boxes; each box 4 coord-prediction, 1 confidence, 1 confidence (7 x 7 x 30);
		- Model:\
			<img src="/CV-2D/images/detection/yolo1-1.png" alt="drawing" width="500"/>
			<img src="/CV-2D/images/detection/yolo1-2.png" alt="drawing" width="500"/>
		- Learning:\
			<img src="/CV-2D/images/detection/yolo1-3.png" alt="drawing" width="500"/>
	- **YOLOv2** (YOLO9000): J. Redmon and A. Farhadi. YOLO9000: Better, faster, stronger. CVPR 2017
		- Improves over v1:\
			<img src="/CV-2D/images/detection/yolo-v2.jpg" alt="drawing" width="400"/>	
		- Better:
			- Batch normalization: mAP +2.4
			- High-resolution: mAP +3.7
			- Multi-scale training (finetune on 448 x 448): 
			- Anchor boxes: recall to 88%, mAP -0.2
				- Input 416 x 416, 32 downsampling, output 13 x 13
			- Dimension Clusters (K=5): IoU from 58.7 (K=5) to 67.2 K=9);
			- Direct location prediction
			- Fine-grained features (passthrough layer): mAP +1.0\
				<img src="/CV-2D/images/detection/pass-through-1.jpg" alt="drawing" width="300"/>\
				<img src="/CV-2D/images/detection/pass-through-2.jpg" alt="drawing" width="300"/>
		- Faster:
			- VGG-16, DarkNet-19
		- Stronger
			- Hierarchical classification\
		<img src="/CV-2D/images/detection/yolo2.png" alt="drawing" width="400"/>
	- **YOLOv3**: J. Redmon and A. Farhadi. Yolov3: An incremental improvement. 2018
		- Insight: add FPN, ResNet, binary cross-entropy;
		- 320 x 320: 22ms
		- Logistic regression:
		- Class prediction:
		- No hard negative mining;
		- Things do not work: Anchor box x,y offset; Linear x,y instead of logistic; focal loss; dual IoU threshold;
		<img src="/CV-2D/images/detection/yolo3.png" alt="drawing" width="150"/>
	- **YOLOv4**: Alexey Bochkovskiy, Chien-Yao Wang, Hong-Yuan Mark Liao. YOLOv4: Optimal Speed and Accuracy of Object Detection. 2020
		- https://github.com/AlexeyAB/darknet
- Mingxing Tan, Ruoming Pang, Quoc V. Le. EfficientDet: Scalable and Efficient Object Detection. 2019

## Proposals, Hard Negative Mining, ...
- Proposals:
	- K.-K. Sung and T. Poggio. Learning and Example Selection for Object and Pattern Detection. 1994
	- **Selective Search**: J. R. Uijlings, K. E. van de Sande, T. Gevers, and A. W. Smeulders. Selective search for object recognition. IJCV 2013
	- **EdgeBoxes**: C. L. Zitnick and P. Dollar. Edge boxes: Locating object proposals from edges. ECCV 2014
	- **DeepMask**:
		- P. O. Pinheiro, R. Collobert, and P. Dollar. Learning to segment object candidates. NIPS'15
		- P. O. Pinheiro, T.-Y. Lin, R. Collobert, and P. Dollar. Learning to refine object segments. ECCV'16
- Hard negative mining:
	- P. F. Felzenszwalb, R. B. Girshick, and D. McAllester. Cascade object detection with deformable part models. CVPR'10
	- S. Bell, C. L. Zitnick, K. Bala, and R. Girshick. Inside-outside net: Detecting objects in context with skip pooling and recurrent neural networks. CVPR'16
	- A. Shrivastava, A. Gupta, and R. Girshick. Training region-based object detectors with online hard example mining. CVPR'16
- Loss design:
	- Focal loss (RetinaNet);

## Between Object
- H Hu, J Gu, Z Zhang, J Dai, and Y Wei. Relation Networks for Object Detection. CVPR'18

## Legacy Features
- **HOG**: N. Dalal and B. Triggs. Histograms of oriented gradients for human detection. CVPR'05
- P. Dollar, Z. Tu, P. Perona, and S. Belongie. Integral channel features. BMVC'09
