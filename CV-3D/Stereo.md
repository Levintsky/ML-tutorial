# Stereo

## Misc
- C Lin, O Wang, B Russell, E Shechtman, V Kim, M Fisher, and S Lucey. Photometric mesh optimization for video-aligned 3d object reconstruction. CVPR'19

## Patch Similarity for Stereo
- S. Zagoruyko and N. Komodakis. Learning to compare image patches via convolutional neural networks. CVPR'15
- J. Zbontar and Y. LeCun. Stereo matching by training a convolutional neural network to compare image patches. JMLR'16
- W. Luo, A. G. Schwing, and R. Urtasun. Efficient deep learning for stereo matching. CVPR'16
- P Knobelreiter, C Reinbacher, A Shekhovtsov, and T Pock. End-to-end training of hybrid cnn-crf models for stereo. CVPR'17
- W. Hartmann, S. Galliani, M. Havlena, L. V. Gool, K. Schindler. Learned multi-patch similarity. ICCV'17.
	- Input: **> 2** image patches (32 x 32);
	- Output: potential depth (discretized);
	<img src="/CV-3D/images/stereo/multi-patch-sim.png" alt="drawing" width="600"/>

	- Application in MVS (plane-sweep): discretize depth and iterate over all;
- **GC-Net**: A. Kendall, H. Martirosyan, S. Dasgupta, P. Henry, R. Kennedy, A. Bachrach, and A. Bry. End-to-end learning of geometry and context for deep stereo regression. ICCV'17
	- Input: rectified stereo pair;
	- Output: stereo;
	- Cost volume;
	- Conv-Deconv on cost volume;
	- Differentiable arg-max;
	<img src="/CV-3D/images/stereo/gc-net.png" alt="drawing" width="500"/>
- S Duggal, S Wang, W Ma, Rui Hu, and R Urtasun. Deeppruner: Learning efficient stereo matching via differentiable patchmatch. 2019

## PSV-based
- J. Flynn, I. Neulander, J. Philbin, and N. Snavely. Deep-Stereo: Learning to predict new views from the world's imagery. CVPR'16
	- Problem: new view synthesis
	- Input images with camera poses;
	- Output: new 2d synthesized view;
	- Preprocess: PSV (Plane-Sweep Volume)
	<img src="/CV-3D/images/stereo/deep-stereo.png" alt="drawing" width="500"/>

- **DeepMVS**: P Huang, K Matzen, J Kopf, N Ahuja, and J Huang. DeepMVS: Learning Multi-view Stereopsis. CVPR'18
	- https://github.com/phuang17/DeepMVS
	- Input: an **arbitrary number** of images with known camera poses and calibration;
	- Steps:
		- 0. Images, camera pose and calibration (**COLMAP** to estimate);
		- 1. Produce plane-sweep volumes;
		- 2.1 Patch Matching
		- 2.2 Encoder-decoder intra-volume feature aggregation;
		- 2.3 Max-pooling to aggregate inter-volume and produce disparity map;
		- 3. Refinement: dense-crf
	- Dataset:
		- DeMoN dataset: 640 x 480 resolution;
		- **MVS-SYNTH**: 120 sequences synthetic (greatly helpful), each seq contains 100 images of 1920 x 1080 resolution, ground truth disparity map, extrinsic and intrinsic camera;
		- ETH3D
- **DPSNet**: Sunghoon Im, Hae-Gon Jeon, Stephen Lin, In So Kweon. DPSNet: End-to-end Deep Plane Sweep Stereo, ICLR'19.
	- Assume: intrinsic K; extrinsic (R, t) known
	<img src="/CV-3D/images/stereo/dpsnet.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/stereo/dpsnet2.png" alt="drawing" width="500"/>

## Multi-View
- S Sun, M Huh, Y Liao, N Zhang, and J Lim. Multi-view to Novel view: Synthesizing Novel Views with Self-Learned Confidence. ECCV'18
	- Problem: novel view synthesis
	- Input: many images;
	- https://github.com/shaohua0116/Multiview2Novelview	
- **MVSNet**: Y. Yao, Z. Luo, S. Li, T. Fang, L. Quan. MVSNet: Depth Inference for Unstructured Multi-view Stereo. ECCV'18.
- **Point-MVSNet**: R Chen, S Han, J Xu, H Su. Point-based Multi-view Stereo Network. ICCV'19.
	- https://github.com/callmeray/PointMVSNet
	- MVSNet for a low-resolution depth; 1/4 resolution, 48 or 96 depth plane;
	- Cost metric based on variance;
	- Dynamic feature fetching (extracted at different location after iterative refine);
	- PointFlow for iterative refine;
		- Edge conv: with kNN
	- Supervision: L1-loss with ground truth for regression;
	- Experiments: DTU; 
	<img src="/CV-3D/images/stereo/point-mvs-net.png" alt="drawing" width="600"/>

## Affinity, Aggregation
- **Sgm-net**: A Seki and M Pollefeys. Sgm-nets: Semi-global matching with neural networks. CVPR'17
- **SPN**: S. Liu, S. De Mello, J. Gu, G. Zhong, M.-H. Yang, and J. Kautz, Learning affinity via spatial propagation networks. NIPS'17
	- https://github.com/danieltan07/spatialaffinitynetwork
	- https://github.com/Liusifei/caffe-spn
- **CSPN (SOA)**: X Cheng, P Wang and R Yang. Learning Depth with Convolutional Spatial Propagation Network. PAMI'18
	- https://github.com/XinJCheng/CSPN
	<img src="/CV-3D/images/stereo/cspn.png" alt="drawing" width="600"/>

- **GA-Net (SOA)**: F Zhang, V Prisacariu, R Yang, Philip H.S. Torr. GA-Net: Guided Aggregation Net for End-to-end Stereo Matching. CVPR'19
	- https://github.com/feihuzhang/GANet

	- X Du, M El-Khamy, J Lee. AMNet: Deep Atrous Multiscale Stereo Disparity Estimation Networks. 2019
	- **HD3**: Z. Yin, T. Darrell and F. Yu: Hierarchical Discrete Distribution Decomposition for Match Density Estimation. CVPR 2019.
		- https://github.com/ucbdrive/hd3
	- **PSM-Net**: J Chang and Y Chen. Pyramid stereo matching network. CVPR'18

- Learning Unsupervised Multi-View Stereopsis via Robust Photometric Consistency, T. Khot, S. Agrawal, S. Tulsiani, C. Mertz, S. Lucey, M. Hebert. 2019.
- Chengzhou Tang and Ping Tan. BA-Net: Dense Bundle Adjustment Network. 2018
- **Unsupervised-Deep-VO**: Ruihao Li, Sen Wang, Zhiqiang Long, and Dongbing Gu. Undeepvo: Monocular visual odometry through unsupervised deep learning. In ICRA, 2018.

## Legacy
- Descriptors:
	- CENSUS, BRIEF
- SGM;
- MVS:
	- Voxel-based: (space-carving)
		- K. N. Kutulakos and S. M. Seitz. A theory of shape by space carving. ICCV'99
		- S. M. Seitz and C. R. Dyer. Photorealistic scene reconstruction by voxel coloring. IJCV'99
	- Fusion-based:
		- N. D. Campbell, G. Vogiatzis, C. Hernández, and R. Cipolla. Using multiple hypotheses to improve depth-maps for multiview stereo. ECCV'08
		- E. Tola, C. Strecha, and P. Fua. Efficient large-scale multi-view stereo for ultra high-resolution image sets. MVA'12
		- S. Galliani, K. Lasinger, and K. Schindler. Massively parallel multiview stereopsis by surface normal diffusion. ICCV'15