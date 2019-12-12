# Classification

## Classification, Network Design
- **AlexNet** A. Krizhevsky, I. Sutskever, and G. Hinton. ImageNet classification with deep convolutional neural networks. NIPS 2012.
- **VGGNet** K. Simonyan and A. Zisserman. Very deep convolutional networks for large-scale image recognition (VGGNet): arXiv:1409.1556, 2014
- **NIN** M Lin, Q Chen, and S Yan (NIN): Network in network. Arxiv, 1312.4400, 2013.
- **FAIR**:
	- **ResNet**: K He, X Zhang, S Ren, J Sun. Deep Residual Learning for Image Recognition. CVPR 2016
		- downample: conv1x1 (stride=2) - BN
		- Basic block:
			- x -> Conv3x3 - BN - ReLU - Conv3x3 - BN -> out
			- x = ReLU(x + out)
		- Basic block (downsample):
			- x -> Conv (stride=2) - BN - ReLU - conv - BN -> out
			- x = ReLU(downsample(x) + out)
		- Bottleneck block
			- x -> Conv1x1 (BN, ReLU) - Conv3x3 (BN, ReLU) - Conv (BN) -> out
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
	- **ResNext**: S Xie, R Girshick, P Dollár, Z Tu, K He. Aggregated Residual Transformations for Deep Neural Networks. CVPR 2017
		- ImageNet 2nd 2016
		- **Grouped-Convolution**
		- i. same spatial size: same hyper-parameter;
		- ii. down-sample by 2, width increase by 2; (each layer similar computation)
		- Conv - Batch-Norm - ReLU;
		- Short-cut: ReLU after adding shortcut;
	- **DenseNet**: G Huang, Z Liu, L v d Maaten, K Q. Weinberger. Densely Connected Convolutional Networks. CVPR 2018
		- https://github.com/bamos/densenet.pytorch.
	- K He, R Girshick, P Dollar. Rethinking ImageNet Pre-training. CVPR'19
- **Google-Vision**:
	- **GoogleNet**: C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan, V. Vanhoucke, and A. Rabinovich (GoogleNet): Going deeper with convolutions. CVPR, 2015
		- Inception-V1
		- Winner-of-ILSVRC-2014;
		- https://medium.com/coinmonks/paper-review-of-googlenet-inception-v1-winner-of-ilsvlc-2014-image-classification-c2b3565a64e7
	- **Incpetion-V2**: Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. ICML 2015
	- **Inception-V3**: Rethinking the Inception Architecture for Computer Vision; CVPR 2016
	- **Inception-V4**: Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning;

## Fine-Grained
- **Bilinear**: T Lin, A RoyChowdhury, S Maji. Bilinear CNN Models for Fine-grained Visual Recognition. ICCV 2015
	- https://github.com/HaoMood/bilinear-cnn

## Pooling, Aggregation
- R Arandjelovic, P Gronat, A Torii, T Pajdla, J Sivic. NetVLAD: CNN architecture for weakly supervised place recognition. 2016

## Attention
- V Mnih, N Heess, A Graves, et al. Recurrent models of visual attention. NIPS'14
- J Ba, V Mnih, and K Kavukcuoglu. Multiple object recognition with visual attention. arxiv'14
- T Xiao, Y Xu, K Yang, J Zhang, Y Peng, and Z Zhang. The application of two-level attention models in deep convolutional neural network for fine-grained image classification. CVPR'15
- M Chung, S Cho. Cram: Clued recurrent attention model. arxiv'18
- J Fu, H Zheng, and T Mei. Look closer to see better: Recurrent attention convolutional neural network for fine-grained image recognition. CVPR'17
- A Ablavatski, S Lu, and J Cai. Enriched deep recurrent visual attention model for multiple object recognition. WACV'17
- H Zheng, J Fu, T Mei, and J Luo. Learning multi-attention convolutional neural network for fine-grained image recognition. ICCV'17
- F Wang, M Jiang, C Qian, S Yang, C Li, H Zhang, X Wang, and X Tang. Residual attention network for image classification. arxiv'17