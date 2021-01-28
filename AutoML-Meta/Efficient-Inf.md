# Optimize on Device

## Basics
- AutoML: most successful for mobile vision;

## Unclassified
- **Squeezenet**: Forrest N. Iandola, Matthew W. Moskewicz, Khalid Ashraf, Song Han, William J. Dally, and Kurt Keutzer. Squeezenet: Alexnet-level accuracy with 50x fewer parameters and <1mb model size. CoRR'16
- Gao Huang, Shichen Liu, Laurens van der Maaten, and Kilian Q. Weinberger. Condensenet: An efficient densenet using learned group convolutions. CoRR'16
- Bichen Wu, Alvin Wan, Xiangyu Yue, Peter H. Jin, Sicheng Zhao, Noah Golmant, Amir Gholaminejad, Joseph Gonzalez, and Kurt Keutzer. Shift: A zero flop, zero parameter alternative to spatial convolutions.
- Azalia Mirhoseini, Hieu Pham, Quoc V. Le, Benoit Steiner, Rasmus Larsen, Yuefeng Zhou, Naveen Kumar, Mohammad Norouzi, Samy Bengio, and Jeff Dean. Device placement optimization with reinforcement learning. ICML'17
- Jin-Dong Dong, An-Chieh Cheng, Da-Cheng Juan, Wei Wei, and Min Sun. Dpp-net: Device-aware progressive search for pareto-optimal neural architectures. ECCV'18
	- Cell-based search
- Post: Device Placement with Cross-Entropy Minimization and Proximal Policy Optimization. NIPS'18
	- Place different OPs on different GPUs
	- Cross Entropy
	- RL with PPO
- Multiple Instance Learning for Efficient Sequential Data Classification on Resource-constrained Devices. NIPS'18

## Mobile
- MobileNet Series:
	- **MobileNet-V1**: A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko, W. Wang, T. Weyand, M. Andreetto, and H. Adam. Mobilenets: Efficient convolutional neural networks for mobile vision applications. CoRR 2017
		- Insight: Depthwise separable + two hyper-parameters for tradeoff (width + resolution multiplier)
		- Input: DF x DF x M, output: DF x DF x N, kernel size: DK
		- Traditional: DK^2 x M x N x DF^2
		- DS computation:
			- DK x DK x 1 kernel: DK^2 x M x DF^2
			- 1 x 1 x N kernel: M x N x DF^2
		- DS parameters: DK x DK x M + M x N
		- Model:\
			<img src="/AutoML-Meta/images/mobile/m-v1.png" alt="drawing" width="500"/>
		- Experiments: ~71% on ImageNet; (much lower op and params than GoogleNet and VGG)
	- **MobileNet-V2**: M. Sandler, A. G. Howard, M. Zhu, A. Zhmoginov, and L. Chen. Inverted residuals and linear bottlenecks: Mobile networks for classification, detection and segmentation. CVPR 2018
		- Problem setup: classification, detection (SSDLite), segmentation (Mobile DeepLabv3);
		- Linear bottlenecks\
			<img src="/AutoML-Meta/images/mobile/m-v2-1.png" alt="drawing" width="350"/>
		- Inverted Residuals\
			<img src="/AutoML-Meta/images/mobile/m-v2-2.png" alt="drawing" width="350"/>
		- Model comparison:\
			<img src="/AutoML-Meta/images/mobile/m-v2-3.png" alt="drawing" width="500"/>
		- Classification: ImageNet 74.7%
		- Detection (SSD-Lite): 75 mIOU compared to 80 ResNet with 30 times more ops;
	- **MobileNet-V3**: Andrew Howard, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang, Yukun Zhu, Ruoming Pang, Vijay Vasudevan, Quoc V. Le, Hartwig Adam. Searching for MobileNetV3. 2019
		- Similar to MNas: RNN-based controller and the same factorized hierarchical search space
		- 0. Backbone based on MnasNet;
			- Block-wise Search;
			- Layer-wise Search;\
			<img src="/AutoML-Meta/images/mobile/m-v3-2.png" alt="drawing" width="400"/>
		- 1. Depthwise (as in V1);
		- 2. Linear bottleneck + inverted residual net;
		- 3. Lightweight attention SE based on squeeze and excitatin;
		- 4. h-swish;
		- 5. Platform-aware NAS and NetAdapt;
		- 6. Change V2 final layers;\
			<img src="/AutoML-Meta/images/mobile/m-v3-1.png" alt="drawing" width="400"/>
- MNas:
	- **MnasNet**: Mingxing Tan, Bo Chen, Ruoming Pang, Vijay Vasudevan, Mark Sandler, Andrew Howard, Quoc V. Le. MnasNet: Platform-Aware Neural Architecture Search for Mobile. 2019
		- Built upon the MobileNetV2 structure by introducing lightweight attention modules based on squeeze and excitation into the bottleneck structure
		- Steps:
			- Generate a set of new proposals with at least delta reduction in latency compared to the previous step;
			- Reuse the pre-trained model with randomly initializing missing weights as appropriate. Finetune each proposal for T steps;
			- Selected best proposal according to some metric;
		- Manually redesign expensive layers;
		- Activation: swish;
	- Bo Chen, Golnaz Ghiasi, Hanxiao Liu, Tsung-Yi Lin, Dmitry Kalenichenko, Hartwig Adams, Quoc V Le. MnasFPN: Learning Latency-aware Pyramid Architecture for Object Detection on Mobile Devices. 2019
- Efficient:
	- **EfficientNet**: Mingxing Tan, Quoc V. Le. EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ICML'19
		- Baseline (MNAS): mobile inverted bottleneck convolution (MBConv)
		- Width scaling
		- Depth scaling
		- Resolution scaling
		- Compound scaling
		<img src="/CV-2D/images/efficientnet-baseline.jpg" alt="drawing" width="500"/>
		<img src="/CV-2D/images/efficientnet-performance.jpg" alt="drawing" width="500"/>
- **ShuffleNet**: X. Zhang, X. Zhou, M. Lin, and J. Sun. ShuffleNet: An extremely efficient convolutional neural network for mobile devices. CVPR'18
	- Traditional Bottleneck: ReLU[x + (conv1x1 BN-ReLU DWconv3x3 BN-ReLU conv1x1 BN)]
	- ShuffleNet: ReLU[x + (**Gconv**1x1 BN-ReLU **Channel-Shuffle** DWconv3x3 BN-ReLU **Gconv**1x1 BN)]
- **FBNet**:
	- ChamNet: Towards Efficient Network Design through Platform-Aware Model Adaptation. 2018
	- V1: Bichen Wu, Xiaoliang Dai, Peizhao Zhang, Yanghan Wang, Fei Sun, Yiming Wu, Yuandong Tian, Peter Vajda, Yangqing Jia, Kurt Keutzer. FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable Neural Architecture Search. 2019
	- **FBNetV2**: Alvin Wan, Xiaoliang Dai, Peizhao Zhang, Zijian He, Yuandong Tian, Saining Xie, Bichen Wu, Matthew Yu, Tao Xu, Kan Chen, Peter Vajda, Joseph E. Gonzalez. FBNetV2: Differentiable Neural Architecture Search for Spatial and Channel Dimensions
		- https://github.com/facebookresearch/mobile-vision
