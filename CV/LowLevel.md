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
- **SelFlow**: P Liu, M R. Lyu, I 
King, J Xu. Self-Supervised Learning of Optical Flow. CVPR'19
<img src="/CV/images/low-level/selflow1.png" alt="drawing" width="600"/>
<img src="/CV/images/low-level/selflow2.png" alt="drawing" width="500"/>

## View Synthesis
- T. Zhou, S. Tulsiani, W. Sun, J. Malik and A. Efros. View synthesis by appearance flow. ECCV'16
- Legacy:
	- S. E. Chen and L. Williams. View interpolation for image synthesis. 1993
	- C. L. Zitnick, S. B. Kang, M. Uyttendaele, S. Winder, and R. Szeliski. High-quality video view interpolation using a layered representation. TOG'04
	- S. M. Seitz and C. R. Dyer. View morphing. 1996

## Keypoints, Feature Matching
- X. Han, T. Leung, Y. Jia, R. Sukthankar, and A. C. Berg. MatchNet: Unifying feature and metric learning for patch-based matching. CVPR'15

## Legacy
- Structure from motion: simultaneous estimate structure and motion
	- R. A. Newcombe, S. J. Lovegrove, and A. J. Davison. DTAM: Dense tracking and mapping in real-time. ICCV'11
	- Failure: low-texture, occlusion, thin structure