# Optimize on Device

## Basics
- AutoML: most succesfful for mobile vision;

## Mobile
- MobileNet Series:
	- **MobileNet**: A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko, W. Wang, T. Weyand, M. Andreetto, and H. Adam. Mobilenets: Efficient convolutional neural networks for mobile vision applications. CoRR 2017
		- Depthwise separable
		- Input: DF x DF x M, output: DF x DF x N, kernel size: DK
		- Traditional: DK^2 * M * N * DF^2
		- DS:
			- DK x DK x 1 kernel: DK^2 * M * DF^2
			- 1 x 1 x N kernel: M * N * DF^2
	- **MobileNet-V2**: M. Sandler, A. G. Howard, M. Zhu, A. Zhmoginov, and L. Chen. Inverted residuals and linear bottlenecks: Mobile networks for classification, detection and segmentation. CVPR 2018
		- SSDLite, Mobile DeepLabv3
		- Linear bottlenecks
		- Inverted Residuals
	- **MobileNet-V2**: Andrew Howard, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang, Yukun Zhu, Ruoming Pang, Vijay Vasudevan, Quoc V. Le, Hartwig Adam. Searching for MobileNetV3. 2019
- MNas:
	- Mingxing Tan, Bo Chen, Ruoming Pang, Vijay Vasudevan, Mark Sandler, Andrew Howard, Quoc V. Le. MnasNet: Platform-Aware Neural Architecture Search for Mobile. 2019
	- Bo Chen, Golnaz Ghiasi, Hanxiao Liu, Tsung-Yi Lin, Dmitry Kalenichenko, Hartwig Adams, Quoc V Le. MnasFPN: Learning Latency-aware Pyramid Architecture for Object Detection on Mobile Devices. 2019
- Azalia Mirhoseini, Hieu Pham, Quoc V. Le, Benoit Steiner, Rasmus Larsen, Yuefeng Zhou, Naveen Kumar, Mohammad Norouzi, Samy Bengio, and Jeff Dean. Device placement optimization with reinforcement learning. ICML 2017
- **ShuffleNet**: X. Zhang, X. Zhou, M. Lin, and J. Sun. ShuffleNet: An extremely efficient convolutional neural network for mobile devices. CVPR 2018
	- Traditional Bottleneck: ReLU[x + (conv1x1 BN-ReLU DWconv3x3 BN-ReLU conv1x1 BN)]
	- ShuffleNet: ReLU[x + (**Gconv**1x1 BN-ReLU **Channel-Shuffle** DWconv3x3 BN-ReLU **Gconv**1x1 BN)]
- **FBNet**: Bichen Wu, Xiaoliang Dai, Peizhao Zhang, Yanghan Wang, Fei Sun, Yiming Wu, Yuandong Tian, Peter Vajda, Yangqing Jia, Kurt Keutzer. FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable Neural Architecture Search. 2019

## Brain
- RL:

## Misc
- Jin-Dong Dong, An-Chieh Cheng, Da-Cheng Juan, Wei Wei, and Min Sun. Dpp-net: Device-aware progressive search for pareto-optimal neural architectures. ECCV'18
	- Cell-based search
- Post: Device Placement with Cross-Entropy Minimization and Proximal Policy Optimization. NIPS'18
	- Place different OPs on different GPUs
	- Cross Entropy
	- RL with PPO
- Multiple Instance Learning for Efficient Sequential Data Classification on Resource-constrained Devices. NIPS'18
