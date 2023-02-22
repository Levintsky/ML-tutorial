# Detection

## Basics
- Problem setup:
	- Input: 2D image;
	- Output: bounding box/key-point;
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
		- 80 categories;
		- 115K training/val, 5k test;
	- **ILSVRC2012**: ImageNet
	- **COCO**: T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollar, and C. L. Zitnick. Microsoft coco: Common objects in context. ECCV'14
- Downstream tasks:
	- People/pedestrian detection/counting;
	- Text detection, OCR;
- Popular approaches:
	- Backbone: ResNet, ResNeXt, VGG, HRNet, RegNet, Res2Net, ResNeSt
		- Group Normalization, Weight Standardization, Mixed Precision (FP16) Training
	- Detectors:
		- Two-stage: RPN, Fast R-CNN, Faster R-CNN, Mask R-CNN, Cascade R-CNN, Cascade Mask R-CNN, Mask Scoring R-CNN, Double-Head R-CNN, Libra R-CNN, Dynamic R-CNN, CascadeRPN
		- Single-stage: Generalized Focal Loss
			- Anchor-based: SSD, RetinaNet,
			- Anchor-free: YOLO-series, FCOS, 
			- Mixture: ATSS,
	- Loss Design:
		- **GIoU**: Rezatofighi, H., Tsoi, N., Gwak, J., Sadeghian, A., Reid, I., Savarese, S.: Generalized intersection over union. CVPR'19
	- Unknown: GHM, Hybrid Task Cascade, Guided Anchoring, RepPoints, Foveabox, FreeAnchor, NAS-FPN, FSAF, PAFPN, PointRend, CARAFE, DCNv2, OHEM, Soft-NMS, Generalized Attention, GCNet, InstaBoost, GRoIE, DetectoRS, CornerNet, Side-Aware Boundary Localization, PAA, YOLACT, CentripetalNet, VFNet, DETR, SCNet
- Good repos:
	- https://github.com/open-mmlab/mmdetection
	- A very good blog (Lilian Weng, OpenAI): https://lilianweng.github.io/lil-log/2017/10/29/object-recognition-for-dummies-part-1.html
	- One stage: https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html

## Misc
- Y. Zhu, C. Zhao, J. Wang, X. Zhao, Y. Wu, and H. Lu. Couplenet: Coupling global structure with local parts for object detection. ICCV'17
- Z Ge, S Liu, F Wang, Z Li, J Sun. YOLOX: Exceeding YOLO Series in 2021. CVPR'21
	- https://github.com/Megvii-BaseDetection/YOLOX

## Perf
- COCO-val2017: mAP
	- Faster-RCNN:
		- resnet50-fpn: (41M/134B): 37.0
		- resnet50-fpn-v2: (43.7M/280B): 46.7
		- mobilenet-v3-large-fpn: (19.4M/4.5B): 32.8
		- mobilenet-v3-320-fpn: (19.4M/0.7B): 22.8
	- Mask-RCNN:
		- resnet50-fpn: (44.4M/134B): 37.9
		- resnet50-fpn-v2: (46.3M/333B): 47.4
	- RetinaNet:
		- resnet50-fpn: (34M/151B): 36.4
		- resnet50-fpn-v2: (38.2M/152B): 41.5
	- FCOS-resnet50-fpn: (32M/128B): 39.2
	- KeypointRcnn (59.1M/137B): 54.6
	- SSD300-VGG16 (35.6M/34.8B): 25.1
	- SSDLite-MobileNet-v3 (34M/0.6B): 21.3

## Backbone
- Legacy:
	- **HOG**: N. Dalal and B. Triggs. Histograms of oriented gradients for human detection. CVPR'05
	- P. Dollar, Z. Tu, P. Perona, and S. Belongie. Integral channel features. BMVC'09
- **ResNet**:
- ResNeXt
- VGG
- HRNet
- RegNet
- Res2Net
- ResNeSt

## Loss Function
- Focal-loss (**RetinaNet**): T Lin, P Goyal, R Girshick, K He, P Dollar. Focal Loss for Dense Object Detection. ICCV'17
	- Insight: solve difficulty imbalance;
	- Reduce loss for well-classified classes; focus on harder classes;
	- Foreground/background imbalance;
	- γ=1: normal Cross-Entropy, in paper, α=0.25, γ=2 is used;
	<img src="/CV-2D/images/detection/focal-loss.png" alt="drawing" width="500"/>
- **GIoU**: H Rezatofighi, N Tsoi, J Gwak, A Sadeghian, I Reid, and S Savarese. Generalized intersection over union: A metric and a loss for bounding box regression. CVPR'19

## One-stage detector
- **Anchor-based**:
	- RetinaNet ICCV'17
	- **SSD**: W. Liu, D. Anguelov, D. Erhan, C. Szegedy, and S. Reed. SSD: Single shot multibox detector. ECCV'16
		- Default k bounding boxes: each cell output (c+4)k, c classes + 4 offsets
		- Multiscale: FPN;
	- **DSSD**: C.-Y. Fu, W. Liu, A. Ranga, A. Tyagi, and A. C. Berg. DSSD: Deconvolutional single shot detector. 2016
		- Use deconv op
	- **R-SSD**: J. Jeong, H. Park, and N. Kwak. Enhancement of ssd by concatenating feature maps for object detection. arxiv'17
		- Pooling + Deconv to combine low/high level features;
- **Anchor-free**
	- keypoint-based:
		- **DeNet**: L. Tychsen-Smith and L. Petersson. Denet: Scalable real-time object detection with directed sparse sampling. ICCV'17
			- 2-stage detector without ROI;
			- Detect: top-left, top-right, bottom-left, bottom-right;
			- Enumerate combinations;
		- Newell, A., Huang, Z., and Deng, J. Associative embedding: End-to-end learning for joint detection and grouping. NIPS'17
			- Embedding to decide which joint belongs to which person;
		- **PLN**: Wang, X., Chen, K., Huang, Z., Yao, C., and Liu, W. Point linking network for object detection. arxiv'17
		- X. Lu, B. Li, Y. Yue, Q. Li, and J. Yan. Grid r-cnn. 2018.
		- **Cornernet**: H. Law and J. Deng. Cornernet: Detecting objects as paired keypoints. ECCV'18
			- https://github.com/princeton-vl/CornerNet
			- Two heatmaps for top-left and bottom-right corners;
			- Embedding decides if two corners belong to the same obj;
			- Corner pooling: max along border;
		- **Cornernet-lite**: H Law, Y Teng, O Russakovsky, and J Deng. Cornernet-lite: Efficient keypoint based object detection. CoRR'19
		- **ExtremeNet**: X Zhou, J Zhuo, and P Krahenbuhl. Bottom-up object detection by grouping extreme and center points. CVPR'19
			- Detect top-most, left-most, bottom-most, right-most and center;
	- Center-based:
		- **Densebox**: L Huang, Y Yang, Y Deng, and Y Yu. Densebox: Unifying landmark localization with end to end object detection. CoRR'15
		- **Foveabox**: T Kong, F Sun, H Liu, Y Jiang, and J Shi. Foveabox: Beyond anchor-based object detector. CoRR'19
		- **GA-RPN**: J Wang, K Chen, S Yang, C C Loy, and D Lin. Region proposal by guided anchoring. CVPR'19
		- **CSP**: Wei Liu, Shengcai Liao, Weiqiang Ren, Weidong Hu, and Yinan Yu. High-level semantic feature detection: A new perspective for pedestrian detection. CVPR'19
		- **FSAF**: Chenchen Zhu, Yihui He, and Marios Savvides. Feature selective anchor-free module for single-shot object detection. CVPR'19
		- **FCOS**: Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS: fully convolutional one-stage object detection. ICCV'19
			- https://github.com/tianzhi0549/FCOS/
			- FCN as backbone + feature-pyramid neck;
			- Anchor-free: every pixel in a gt-box only predict 4d distance to edges (l, r, t, b) and class c;
			- Overlapping boxes: always choose smallest as positive;
			- Centerness + nms to tackle low-quality boxes predicted from edge pixels?
		- **YOLO**-series;
			- YOLO. CVPR'16
			- YOLO9000: CVPR'17
		- **CenterNet**: Kaiwen Duan, Song Bai, Lingxi Xie, Honggang Qi, Qingming Huang, Qi Tian. CenterNet: Keypoint Triplets for Object Detection. ICCV'19
			- A very good summary: https://zhuanlan.zhihu.com/p/66048276
			- Improve on CornerNet by Triplet instead of pair;
			- Generate top-k bounding boxes similar to CornerNet;
			- Size matters:
				- Smaller central regions: low recall for small boxes;
				- Larger central regions: low precision for large boxes;
			- Center pooling: max-pool both direction;
- Mix:
	- **ATSS**: S Zhang, C Chi, Y Yao, Z Lei, S Li. Bridging the Gap Between Anchor-based and Anchor-free Detection via Adaptive Training Sample Selection. CVPR'19
		- Adding group-norm, GIoU-loss, GT Box, Centerness, Scalar bring RetinaNet from mAP=32.5to 37.0 (FCOS=37.8);
		- Way to select positive matters!
			- RetinaNet: IoU;
			- FCOS: first spatial, then scale;
- J. Huang, V. Rathod, C. Sun, M. Zhu, A. Korattikara, A. Fathi, I. Fischer, Z. Wojna, Y. Song, S. Guadarrama, and K. Murphy. Speed/accuracy trade-offs for modern convolutional object detectors. CVPR'17
	- Faster R-CNN by G-RMI?
- **RON**: T. Kong, F. Sun, A. Yao, H. Liu, M. Lu, and Y. Chen. Ron: Reverse connection with objectness prior networks for object detection. CVPR'17
	- Reverse connection + objectness prior;
- SSD (anchor-based):
	- **SSD**: W. Liu, D. Anguelov, D. Erhan, C. Szegedy, and S. Reed. SSD: Single shot multibox detector. ECCV'16
		- Default k bounding boxes: each cell output (c+4)k, c classes + 4 offsets
		- Multiscale: FPN;
			<img src="/CV-2D/images/detection/ssd.png" alt="drawing" width="500"/>\
			<img src="/CV-2D/images/detection/ssd-eqn.png" alt="drawing" width="500"/>
- YOLO (anchor-free):
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
- **RefineDet**: S. Zhang, L. Wen, X. Bian, Z. Lei, and S. Z. Li. Single-shot refinement neural network for object detection. CVPR'18
	- Refine bbox twice
- **EfficientDet**: M Tan, R Pang, Quoc V. Le. EfficientDet: Scalable and Efficient Object Detection. 2019
- One-shot:
	- **OS2D**: OS2D: One-Stage One-Shot Object Detection by Matching Anchor Features
		- https://github.com/aosokin/os2d

## Two-Stage
- RCNN family:\
	<img src="/CV-2D/images/detection/rcnn-family-summary.png" alt="drawing" width="650"/>
- Proposals/1st-stage:
	- Selective Search: RCNN [cvpr'14], Fast-RCNN [iccv'15]
	- E2E/Trained: first by Faster-RCNN [nips'15]
- Refinement/2nd-stage
	- HNM (Hard negative mining): RCNN [cvpr'14], ...
	- Pooling:
		- RPN (proposed in Fast-RCNN [iccv'15]) 
	- Separate: RCNN [cvpr'14]
	- Supervision:
		- RCNN [cvpr'14]\
			<img src="/CV-2D/images/detection/RCNN-eqn.png" alt="drawing" width="400"/>
		- Segmentation: Mask-RCNN [iccv'17]
- Perf:
	- Pascal-VOC: rcnn 54.2%, fast-rcnn 66.9%, faster-rcnn 73.2%
- **MultiBox**: D. Erhan, C. Szegedy, A. Toshev, and D. Anguelov. Scalable object detection using deep neural networks. CVPR'14
	- Bounding box: normalized w.r.t. image dimension to achieve invariance;
	- Confidence:
	- Propose K boxes for M gt, K >> M; assignment;
	- K clusters/centroids by clustering, only predict residual;
- **R-FCN**: J. Dai, Y. Li, K. He, and J. Sun. R-fcn: Object detection via region-based fully convolutional networks. NIPS'16
	- https://github.com/daijifeng001/r-fcn
	- Position-sensitive score maps; k x k (3 x 3);
		- per-ROI-pooling on each k x k;
	- Backbone: resnet-101;
	- Model:\
		<img src="/CV-2D/images/detection/r-fcn.png" alt="drawing" width="450"/>
	- Pascal-VOC: 83.6% mAP
- **TDM**: A. Shrivastava, R. Sukthankar, J. Malik, and A. Gupta. Beyond skip connections: Top-down modulation for object detection. arxiv'16
	- Insight: very similar to FPN;
	- Model:\
		<img src="/CV-2D/images/detection/tdm.png" alt="drawing" width="450"/>
- **FPN**: T.-Y. Lin, P. Dollar, R. Girshick, K. He, B. Hariharan, and S. Belongie. Feature pyramid networks for object detection. CVPR'17
	<img src="/CV-2D/images/detection/fpn.png" alt="drawing" width="500"/>
- H. Lee, S. Eum, and H. Kwon. Me r-cnn: Multi-expert r-cnn for object detection. arxiv'17
- **Light-head r-cnn**: Li, Z., Peng, C., Yu, G., Zhang, X., Deng, Y., and Sun, J. Light-head r-cnn: In defense of two-stage object detector. arxiv'17
- **Cascade r-cnn**: Z. Cai and N. Vasconcelos. Cascader-cnn: Delving into high quality object detection. CVPR'18
	- Sequence of detectors with increasing IOU threshold;
- **RepMet**: L Karlinsky, J Shtok, S Harary, E Schwartz, A Aides, R Feris, R Giryes, A Bronstein. RepMet: Representative-based metric learning for classification and one-shot object detection. CVPR'19
	- SOTA performance;
- **CoAE**: Ting-I Hsieh, Yi-Chen Lo, Hwann-Tzong Chen, Tyng-Luh Liu. One-Shot Object Detection with Co-Attention and Co-Excitation. NuerIPS'19

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
	- Tychsen-Smith, L. and Petersson, L. Improving object localization with fitness nms and bounded iou loss. arxiv'17
	- **Ranked List Loss**: X Wang, Y Hua, E Kodirov, N Robertson. Ranked List Loss for Deep Metric Learning. CVPR'19

## Context, Between Object
- Context:
	- S. Gidaris and N. Komodakis. Object detection via a multi-region and semantic segmentation-aware cnn model. ICCV'15
	- S. Bell, C. Lawrence Zitnick, K. Bala, and R. Girshick. Inside-outside net: Detecting objects in context with skip pooling and recurrent neural networks. CVPR'16
	- A. Shrivastava and A. Gupta. Contextual priming and feedback for faster r-cnn. ECCV'16
	- X. Zeng, W. Ouyang, B. Yang, J. Yan, and X. Wang. Gated bi-directional cnn for object detection. ECCV'16
- H Hu, J Gu, Z Zhang, J Dai, and Y Wei. Relation Networks for Object Detection. CVPR'18

## Text Detection
- X Zhou, C Yao, H Wen, Y Wang, S Zhou, W He, and J Liang. EAST: an efficient and accurate scene text detector. CVPR'17
- T He, Z Tian, W Huang, C Shen, Y Qiao, and C Sun. An end-to-end textspotter with explicit alignment and attention. CVPR'18

## Toolboxes
- Detectron v1: https://github.com/facebookresearch/Detectron
	- Fast R-CNN;
	- Faster R-CNN;
	- Residual-Net;
	- R-FCN;
	- ResNext;
	- FPN CVPR'17;
	- Georgia Gkioxari, Ross Girshick, Piotr Dollár, and Kaiming He. Detecting and Recognizing Human-Object Interactions. Tech report, arXiv'17
	- P Goyal, P Dollár, R Girshick, P Noordhuis, L Wesolowski, A Kyrola, A Tulloch, Y Jia, and K He. Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour. Tech report, arXiv'17
	- Focal-loss ICCV'17;
	- Mask R-CNN;
	- Non-Local Neural Networks;
	- R Hu, P Dollár, K He, T Darrell, and R Girshick. Learning to Segment Every Thing. Tech report, arXiv'17.
	- I Radosavovic, P Dollár, R Girshick, G Gkioxari, and K He. Data Distillation: Towards Omni-Supervised Learning. Tech report, arXiv, Dec. 2017.
- Detectron v2: https://github.com/facebookresearch/detectron2
	- DensePose: Dense Human Pose Estimation In The Wild
	- Scale-Aware Trident Networks for Object Detection
	- TensorMask: A Foundation for Dense Object Segmentation
	- Mesh R-CNN
	- PointRend: Image Segmentation as Rendering
	- Momentum Contrast for Unsupervised Visual Representation Learning
- OpenMMLab: