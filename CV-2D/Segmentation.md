# Segmentation

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

## Level Set
- Tutorial: 
	- Daniel Cremers. Level Set Methods in Computer Vision. ECCV'06
- D Cremers, M Rousson, R Deriche. A Review of Statistical Approaches to Level Set Segmentation: Integrating color, texture, motion and shape. IJCV'06
- Ping Hu, Bing Shuai, Jun Liu, Gang Wang. Deep Level Sets for Salient Object Detection. CVPR'17