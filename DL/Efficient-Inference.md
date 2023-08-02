# Optimize on Device

## Basics
- AutoML: most successful for mobile vision;

## Auto-TVM:
- T Chen, et. al. TVM: An Automated End-to-End Optimizing Compiler for Deep Learning. OSDI'18
- T Chen, et. al. Learning to Optimize Tensor Programs. NIPS'18
	- Input: a program, output: an efficient execution;
	- Model 1: GBT (XGBoost);
	- Model 2: TreeGRU; (Kai Sheng Tai, Richard Socher, and Christopher D Manning. Improved semantic representations from tree-structured long short-term memory networks.)
	- Loss: ranking loss;
	- Optimization process (Sub-Modular): simulated annealing to collect candidates; diversity-aware optimization;
	- Transfer Learning;

## Polyhedral
- U Bondhugula, A Hartono, J Ramanujam, and P. Sadayappan. A practical automatic polyhedral parallelizer and locality optimizer. SIGPLAN, PLDI'08
- S Verdoolaege, J Juega, A Cohen, J Gómez, C Tenllado, and F Catthoor. Polyhedral parallel code generation for cuda. ACM 2013
- **Halide**: J Ragan-Kelley, et. al. Halide: A language and compiler for optimizing parallelism, locality, and recomputation in image processing pipelines. PLDI'13
- **Tensor comprehension**: N Vasilache, et. al. Tensor comprehensions: Frameworkagnostic high-performance machine learning abstractions. CoRR'18

## Black box:
- **FFTW**: M. Frigo and S. G. Johnson. Fftw: an adaptive software architecture for the fft. ICASSP 1998
-  D Golovin, B Solnik, S Moitra, G Kochanski, J Karro, and D Sculley. Google vizier: A service for black-box optimization. KDD'17
- **Atlas**: R. Clint Whaley and Jack J. Dongarra. Automatically tuned linear algebra software. 1998

## DSL
- A Sujeeth, H Lee, K Brown, H Chafi, M Wu, A Atreya, K Olukotun, T Rompf, and M Odersky. Optiml: An implicitly parallel domain-specific language for machine learning. ICML'11
- F Kjolstad, S Kamil, S Chou, D Lugato, and S Amarasinghe. The tensor algebra compiler. OOPSLA'17
- **Weld**: S Palkar, et. al. M Zaharia. Weld: Rethinking the interface between data-intensive applications. PLDI CoRR'17
- M Steuwer, T Remmelg, and C Dubach. Lift: A functional data-parallel ir for high-performance gpu code generation. CGO'17

## Unclassified
- **Squeezenet**: F Iandola, M Moskewicz, K Ashraf, S Han, W Dally, and K Keutzer. Squeezenet: Alexnet-level accuracy with 50x fewer parameters and <1mb model size. CoRR'16
- G Huang, S Liu, L v d Maaten, and K Weinberger. Condensenet: An efficient densenet using learned group convolutions. CoRR'16
- B Wu, et. al. Kurt Keutzer. Shift: A zero flop, zero parameter alternative to spatial convolutions.
- A Mirhoseini, et. al. J Dean. Device placement optimization with reinforcement learning. ICML'17

## Mobile
- MobileNet Series:
	- MobileNet-V1: Google. Mobilenets: Efficient convolutional neural networks for mobile vision applications. CoRR'17
		- Insight: Depthwise separable + two hyper-parameters for tradeoff (width + resolution multiplier)
		- Input: DF x DF x M, output: DF x DF x N, kernel size: DK
		- Traditional: DK^2 x M x N x DF^2
		- DS computation:
			- DK x DK x 1 kernel: DK^2 x M x DF^2
			- 1 x 1 x N kernel: M x N x DF^2
		- DS parameters: DK x DK x M + M x N
		- Model:
			- Standard: 3x3-conv - BN - ReLU
			- Proposed: 3x3-dwise-conv - BN - ReLU6 - [1x1-conv - BN - ReLU]
		- Experiments: ~71% on ImageNet; (much lower op and params than GoogleNet and VGG)
	- MobileNet-V2: Google. Inverted residuals and linear bottlenecks: Mobile networks for classification, detection and segmentation. CVPR'18
		- Problem setup: classification, detection (SSDLite), segmentation (Mobile DeepLabv3);
		- Linear bottlenecks:
			- 3x3-dwise-conv - Relu6 - Relu6, 1x1 - 1
		- Inverted Residuals: PW - DW - PW
			- 1x1-ReLU6 - Dwise-3x3-Relu6 - 1x1-linear
		- Classification: ImageNet 74.7%
		- Detection (SSD-Lite): 75 mIOU compared to 80 ResNet with 30 times more ops;
	- **MobileNet-V3**: Searching for MobileNetV3. 2019
		- Similar to MNas: RNN-based controller and the same factorized hierarchical search space
		- 0. Backbone based on MnasNet;
			- Block-wise Search;
			- Layer-wise Search;
		- 1. Depthwise (as in V1);
		- 2. Linear bottleneck + inverted residual net;
		- 3. Lightweight attention SE based on squeeze and excitatin;
		- 4. h-swish;
		- 5. Platform-aware NAS and NetAdapt;
		- 6. Change V2 final layers:
			- 1x1-conv-BN-swish - Avg-pool - 1x1-conv-swish - 1x1-conv (Linear)
- MNas:
	- MnasNet: Platform-Aware Neural Architecture Search for Mobile. 2019
		- MobileNetV2 + swish
		- Steps:
			- Generate a set of new proposals with at least delta reduction in latency compared to the previous step;
			- Reuse the pre-trained model with randomly initializing missing weights as appropriate. Finetune each proposal for T steps;
			- Selected best proposal according to some metric;
		- Manually redesign expensive layers;
		- Activation: swish;
	- B Chen, et. al. MnasFPN: Learning Latency-aware Pyramid Architecture for Object Detection on Mobile Devices. 2019
- Efficient:
	- EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ICML'19
		- Baseline (MNAS): mobile inverted bottleneck convolution (MBConv)
		- Width scaling
		- Depth scaling
		- Resolution scaling
		- Compound scaling
- ShuffleNet: X. Zhang, X. Zhou, M. Lin, and J. Sun. ShuffleNet: An extremely efficient convolutional neural network for mobile devices. CVPR'18
	- Traditional Bottleneck: ReLU[x + (conv1x1 BN-ReLU DWconv3x3 BN-ReLU conv1x1 BN)]
	- ShuffleNet: ReLU[x + (Gconv-1x1 BN-ReLU Channel-Shuffle DWconv3x3 BN-ReLU **Gconv**1x1 BN)]
- FBNet:
	- ChamNet: Towards Efficient Network Design through Platform-Aware Model Adaptation. 2018
	- FBNet-v1: Hardware-Aware Efficient ConvNet Design via Differentiable Neural Architecture Search. 2019
	- FBNet-V2: Differentiable Neural Architecture Search for Spatial and Channel Dimensions
		- https://github.com/facebookresearch/mobile-vision
