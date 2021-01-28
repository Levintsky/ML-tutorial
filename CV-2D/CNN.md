# CNN (with focus on Classification)

## Layer Design
- **CoordConv**: Rosanne Liu, Joel Lehman, Piero Molino, Felipe Petroski Such, Eric Frank, Alex Sergeev, Jason Yosinski. An intriguing failing of convolutional neural networks and the CoordConv solution. NIPS'18
- Pooling, Aggregation
	- R Arandjelovic, P Gronat, A Torii, T Pajdla, J Sivic. NetVLAD: CNN architecture for weakly supervised place recognition. 2016
- Conv:
	- Dilated: increase receptive field;

## Network Design
- **AlexNet**: A. Krizhevsky, I. Sutskever, and G. Hinton. ImageNet classification with deep convolutional neural networks. NIPS'12
- **NIN**: M Lin, Q Chen, and S Yan (NIN): Network in network. Arxiv, 1312.4400, 2013.
- **SPP**: K. He, X. Zhang, S. Ren, and J. Sun. Spatial pyramid pooling in deep convolutional networks for visual recognition. ECCV'14
- **VGGNet**: K. Simonyan and A. Zisserman. Very deep convolutional networks for large-scale image recognition. ICLR'15
- **GoogleNet**: C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan, V. Vanhoucke, and A. Rabinovich (GoogleNet): Going deeper with convolutions. CVPR'15
	- Inception-V1
	- Winner-of-ILSVRC-2014;
	- https://medium.com/coinmonks/paper-review-of-googlenet-inception-v1-winner-of-ilsvlc-2014-image-classification-c2b3565a64e7
- **Incpetion-V2**: Sergey Ioffe, Christian Szegedy. Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift. ICML'15
- **Inception-V3**: Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, Zbigniew Wojna. Rethinking the Inception Architecture for Computer Vision. CVPR'16
- **ResNet**: K He, X Zhang, S Ren, J Sun. Deep Residual Learning for Image Recognition. CVPR'16
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
- **Inception-V4**: Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi. Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning; 2016
- **Hourglass**: Newell, A., Yang, K., and Deng, J. Stacked hourglass networks for human pose estimation. ECCV'16
- **ResNext**: S Xie, R Girshick, P Dollár, Z Tu, K He. Aggregated Residual Transformations for Deep Neural Networks. CVPR'17
	- Insight: **Grouped-Convolution**
	- 2nd of ILSVR'16
	- i. same spatial size: same hyper-parameter;
	- ii. down-sample by 2, width increase by 2; (each layer similar computation)
	- Conv - Batch-Norm - ReLU;
	- Short-cut: ReLU after adding shortcut;
- **DenseNet**: G Huang, Z Liu, L v d Maaten, K Q. Weinberger. Densely Connected Convolutional Networks. CVPR'18
	- https://github.com/bamos/densenet.pytorch
- **SENet**: Jie Hu, Li Shen, Gang Sun. Squeeze-and-Excitation Networks. CVPR'18
	- Insight: channel-wise scaling (learn by MLP);
	- https://github.com/hujie-frank/SENet
	- Winner of ILSVR'17
	- Model:\
		<img src="/CV-2D/images/cnn/senet-1.png" alt="drawing" width="400"/>
	- Module:\
		<img src="/CV-2D/images/cnn/senet-2.png" alt="drawing" width="300"/>
		<img src="/CV-2D/images/cnn/senet-3.png" alt="drawing" width="300"/>
- K He, R Girshick, P Dollar. Rethinking ImageNet Pre-training. CVPR'19

## Fine-Grained
- **Bilinear**: T Lin, A RoyChowdhury, S Maji. Bilinear CNN Models for Fine-grained Visual Recognition. ICCV'15
	- https://github.com/HaoMood/bilinear-cnn
- Kaiyu Yue, Ming Sun, Yuchen Yuan, Feng Zhou, Errui Ding, Fuxin Xu. Compact Generalized Non-local Network. NIPS'18
	- https://github.com/KaiyuYue/cgnl-network.pytorch
