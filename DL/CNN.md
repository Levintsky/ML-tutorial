# CNN (with focus on Classification)

## Basics
- Activation: always used with BatchNorm

## Layer/Operator Design
- Strided-Conv;
- Dilated-Conv;
	- F Yu and V Koltun. Multi-scale context aggregation by dilated convolutions. arxiv'15
	- L. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille. Deeplab: Semantic image segmentation with deep convolutional. PAMI'18
	- H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia. Pyramid scene parsing network. CVPR'17
- CoordConv: R Liu, J Lehman, P Molino, F Such, E Frank, A Sergeev, J Yosinski. An intriguing failing of convolutional neural networks and the CoordConv solution. NIPS'18
- Pooling, Aggregation
	- R Arandjelovic, P Gronat, A Torii, T Pajdla, J Sivic. NetVLAD: CNN architecture for weakly supervised place recognition. 2016

## CNN for NLP
- Single layer for sentence cls:
	- Yoon Kim: Convolutional Neural Networks for Sentence Classification. EMNLP'14
- Zhang and Wallace. A Sensitivity Analysis of (and Practitioners' Guide to) Convolutional Neural Networks for Sentence Classification. 2015
- Very deep:
	- Conneau, Schwenk, Lecun, Barrault. EACL 2017.

## Network/Backbone Design
- **AlexNet**: A. Krizhevsky, I. Sutskever, and G. Hinton. ImageNet classification with deep convolutional neural networks. NIPS'12
- **NIN**: M Lin, Q Chen, and S Yan (NIN): Network in network. Arxiv, 1312.4400, 2013.
	- size-1 kernel, MLP in CNN;
- **SPP**: K. He, X. Zhang, S. Ren, and J. Sun. Spatial pyramid pooling in deep convolutional networks for visual recognition. ECCV'14
- **VGGNet**: K. Simonyan and A. Zisserman. Very deep convolutional networks for large-scale image recognition. ICLR'15
- **GoogleNet**: C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan, V. Vanhoucke, and A. Rabinovich (GoogleNet): Going deeper with convolutions. CVPR'15
	- Inception-V1
	- https://medium.com/coinmonks/paper-review-of-googlenet-inception-v1-winner-of-ilsvlc-2014-image-classification-c2b3565a64e7
- **Incpetion-V2**: S Ioffe, C Szegedy. Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. ICML'15
- **Inception-V3**: C Szegedy, V Vanhoucke, S Ioffe, J Shlens, Z Wojna. Rethinking the Inception Architecture for Computer Vision. CVPR'16
- **ResNet**: K He, X Zhang, S Ren, J Sun. Deep Residual Learning for Image Recognition. CVPR'16
	- downample: conv1x1 (stride=2) - BN
	- Basic block:
		- x -> Conv3x3 - BN - ReLU - Conv3x3 - BN -> out
		- x = ReLU(x + out)
	- Basic block (downsample):
		- x -> Conv (stride=2) - BN - ReLU - conv - BN -> out
		- x = ReLU(downsample(x) + out)
	- Bottleneck block
		- x -> Conv1x1 channel-large (BN, ReLU) - Conv3x3 channel-small (BN, ReLU) - Conv channel-large (BN) -> out
		- x = ReLU(x + out)
	- Bottleneck block (downsample)
		- x -> Conv1x1 (stride=2, BN, ReLU) - Conv3x3 (BN, ReLU) - Conv1x1 (BN) -> out
		- x = ReLU(downsample(x) + out)
	- Make a layer (Res1, ..., Res4)
		- Layer (downsample) - Layer - ...
	- Final structure:
		- **Initial Conv**: conv1 (stride=2, BN, ReLU) - Max-Pool -> 64 x 56 x 56
		- Res1 (64) - Res2 (down 112 x 28 x 28) - Res3 (down 256 x 14 x 14, down) - Res4 (down 512 x 7 x 7)
		- Average-pool (7x7) - fc1000
- **Inception-V4**: C Szegedy, S Ioffe, V Vanhoucke, A Alemi. Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning; 2016
- **ResNext**: S Xie, R Girshick, P Dollár, Z Tu, K He. Aggregated Residual Transformations for Deep Neural Networks. CVPR'17
	- Insight: **Grouped-Convolution**
	- i. same spatial size: same hyper-parameter;
	- ii. down-sample by 2, width increase by 2; (each layer similar computation)
	- Conv - Batch-Norm - ReLU;
	- Short-cut: ReLU after adding shortcut;
- **DenseNet**: G Huang, Z Liu, L v d Maaten, K Q. Weinberger. Densely Connected Convolutional Networks. CVPR'18
	- https://github.com/bamos/densenet.pytorch
- K He, R Girshick, P Dollar. Rethinking ImageNet Pre-training. CVPR'19
- J Wang, K Sun, T Cheng, B Jiang, C Deng, Y Zhao, D Liu, Y Mu, M Tan, X Wang, et al. Deep high-resolution representation learning for visual recognition. PAMI'20
	- High-resolution, multi-branch, fuse;
**EfficientNet**: M Tan, Quoc V. Le. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ICML'19
	- Check Efficient-Inf for details;
- **RegNet**: I Radosavovic, R Kosaraju, R Girshick, K He, P Dollar. Designing Network Design Spaces. CVPR'20
	- Check AutoML for details;

## Performance
- ImageNet: (params/flops) top-1
	- AlexNet: 63.5%, top-5 84.7%;
	- SPP: top-1 72.1%, top-5 90.8%
	- VGG: top-1 76.3%, top-5 93.2%
	- Inception-V1: top-5 93.3%; (1st of ILSVRC'14)
	- Inception-V2: 79.9%, top-5 95.0%;
	- ResNet: 80.6%; (1st of ILSVRC'15)
		- R-18 (12M/1.8B): 69.8%
		- R-34 (21M/3.7B): 73.3%
		- R-50 (25M/4.1B): 80.9%
		- R-101 (44M/7.8B): 81.9%
		- R-152 (60M/11B): 82.3% (78.3% old code)
	- Inception-V3: 82.7%, top-5 96.5%;
	- Inception-V4: 83.5%, top-5 96.9%;
	- ResNext-101 (32B): 80.9%, top-5 95.6%; (2nd of ILSVR'16)
	- SENet (42B): 82.7% (1st of ILSVR'17)
	- NASNet-A (24B): 82.9%
	- DenseNet: 79.2%, top-5 94.7%;
	- AmeobaNet-C (41B): 83.5%
	- EfficientNet:
		- B1 (0.7B): 79.1%
		- B3 (1.8B): 81.6%
		- B4 (4.2B): 82.9%
		- B5 (9.9B): 83.6%
		- B7: 84.3%;
	- MobileNet-v2: (/0.3B): 72.2%
	- MobileNet-v3:
		- Small (2M/0.06B): 67.7%
		- Large (5M/0.2B): 75.3%
	- RegNet: top-1 80.0%(4G), 81.7%(8G), 82.9%(16G);
	- ViT:
		- B-16 (86M/17B): 81.1% (85% SWAG)
		- B-32 (88M/4.4B): 75.9%
		- L-16 (304M/61B): 79.7% (88% SWAG)
		- L-32 (306M/15B): 77.0%
	- Swin:
		- T (28M/4.4B): 81.5%
		- Tv2 (28M/5.9B): 82.1%
		- S (49M/8.7B): 83.2%
		- Sv2 (50M/11.5B): 83.7%
		- B (88M/15.4B): 83.6%
		- Bv2 (88M/20B): 84.1%
- COCO:
	- ResNext: AP-at-0.5 51.9%, AP 30.0%;

## Multi-Scale Design
- Basics:
	- Required for position-sensitive tasks (semantic segmentation, human pose estimation, and object detection);
	- Low-resolution only: OverFeat, FCN;
- **FCN**: J. Long, E. Shelhamer, and T. Darrell. Fully convolutional networks for semantic segmentation. CVPR'15
- **U-Net**: O Ronneberger, P Fischer, T Brox: Convolutional Networks for Biomedical Image Segmentation, MICCAI'15
- **deconv-net**: H. Noh, S. Hong, and B. Han. Learning deconvolution network for semantic segmentation. ICCV'15
- **Hourglass**: Newell, A., Yang, K., and Deng, J. Stacked hourglass networks for human pose estimation. ECCV'16
- Encoder-decoder: X. Peng, R. S. Feris, X. Wang, and D. N. Metaxas. A recurrent encoder-decoder network for sequential face alignment. ECCV'16
- **Segnet**: V. Badrinarayanan, A. Kendall, and R. Cipolla. Segnet: A deep convolutional encoder-decoder architecture for image segmentation. PAMI'17
- **FPN**: T.-Y. Lin, P. Dollar, R. Girshick, K. He, B. Hariharan, and S. Belongie. Feature pyramid networks for object detection. CVPR'17
- **SimpleBaseline**: B. Xiao, H. Wu, and Y. Wei. Simple baselines for human pose estimation and tracking. ECCV'18
- **HRNet**:
	- J Wang, K Sun, T Cheng, B Jiang, C Deng, Y Zhao, D Liu, Y Mu, M Tan, X Wang, W Liu, and B Xiao. Deep High-Resolution Representation Learning for Visual Recognition. PAMI'20
	- K Sun, B Xiao, D Liu, J Wang. Deep High-Resolution Representation Learning for Human Pose Estimation. CVPR'19
		- https://github.com/HRNet
		- https://zhuanlan.zhihu.com/p/335333233
- Multi-scale fusion:
	- Y. Zhou, X. Hu, and B. Zhang. Interlinked convolutional neural networks for face parsing. ISNN'15
	- S. Saxena and J. Verbeek. Convolutional neural fabrics. NIPS'16
	- **PSPNet**: H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia. Pyramid scene parsing network. CVPR'17
	- DeepLab V2/V3: atrous spatial pyramid pooling;
