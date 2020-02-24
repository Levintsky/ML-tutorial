# Low-Level Vision

## Optical Flow
- **FlowNet**: A Dosovitskiy, P Fischer, E Ilg, P Hausser, C Hazırbas, V Golkov. FlowNet: Learning Optical Flow with Convolutional Networks. ICCV'15
	- FlowNetS: stacks two images as input
	- FlowNetC: convolute separately, combine with correlation layer
- **FlowNet 2.0**: E Ilg, N Mayer, T Saikia, M Keuper, A Dosovitskiy, T Brox. FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks. CVPR'17
	- FlowNetC: explicit correlation
	- FlowNetS: a straightforward encoder-decoder architecture
	- FlowNetSD: small displacement
	- FlowNetFusion: fusion of different flows
	- Improvement over 1.0: smooth flow fields; preserve fine-motion detail; fast;
	<img src="/CV/images/low-level/flownet2.png" alt="drawing" width="600"/>
- **Pwc-Net**: D Sun, X Yang, M Liu, and J Kautz. Pwc-net: Cnns for optical flow using pyramid, warping, and cost volume. CVPR'18
- **MFF**: Z Ren, O Gallo, D Sun, M Yang, E Sudderth and J Kautz. A Fusion Approach for Multi-Frame Optical Flow Estimation. 2019
- **SelFlow**: P Liu, M R. Lyu, I King, J Xu. Self-Supervised Learning of Optical Flow. CVPR'19
	<img src="/CV/images/low-level/selflow1.png" alt="drawing" width="600"/>
	<img src="/CV/images/low-level/selflow2.png" alt="drawing" width="500"/>
- **HD3**: Z Yin, T Darrell, F Yu. Hierarchical Discrete Distribution Decomposition for Match Density Estimation. CVPR'19
	- https://github.com/ucbdrive/hd3

## Keypoints, Feature Matching
- X. Han, T. Leung, Y. Jia, R. Sukthankar, and A. C. Berg. MatchNet: Unifying feature and metric learning for patch-based matching. CVPR'15
- J Yang, S Wang, W Ma, A Barsan, J Martinez, R Urtasun. End-to-End Sparse Image Matching. Mini-18
- Law, H., & Deng, J. CornerNet: Detecting objects as paired keypoints. IJCV'19

## Deblur, Deconv
- Deep Non-Blind Deconvolution via Generalized Low-Rank Approximation. NIPS'18

## Legacy
- Structure from motion: simultaneous estimate structure and motion
	- R. A. Newcombe, S. J. Lovegrove, and A. J. Davison. DTAM: Dense tracking and mapping in real-time. ICCV'11
	- Failure: low-texture, occlusion, thin structure