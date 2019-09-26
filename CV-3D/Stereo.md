# Stereo

## Patch Similarity for Stereo
- S. Zagoruyko and N. Komodakis. Learning to compare image patches via convolutional neural networks. CVPR'15
- J. Zbontar and Y. LeCun. Stereo matching by training a convolutional neural network to compare image patches. JMLR'16
- W. Luo, A. G. Schwing, and R. Urtasun. Efficient deep learning for stereo matching. CVPR'16
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

## PSV-based
- J. Flynn, I. Neulander, J. Philbin, and N. Snavely. Deep-Stereo: Learning to predict new views from the world's imagery. CVPR'16
	- Problem: new view synthesis
	- Input images with camera poses;
	- Output: new 2d synthesized view;
	- Preprocess: PSV (Plane-Sweep Volume)
	<img src="/CV-3D/images/stereo/deep-stereo.png" alt="drawing" width="500"/>

- DeepMVS: Learning Multi-view Stereopsis. CVPR'18
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

## Multi-View
- **LSM**: A. Kar, C. Häne, J. Malik. Learning a multi-view stereo machine, NIPS 2017.
	- Input: multiple images;
	- Output: Voxel 3D;
	- Assumption: **camera pose known**;
	<img src="/CV-3D/images/reconstruction/lsm1.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/reconstruction/lsm2.png" alt="drawing" width="600"/>

## Affinity, Aggregation
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
	- Jia-Ren Chang and Yong-Sheng Chen. Pyramid stereo matching network. CVPR'18

- Surfacenet: An end-to-end 3d neural network for multiview stereopsis, Ji, M., Gall, J., Zheng, H., Liu, Y., Fang, L. ICCV'17.
- RayNet: Learning Volumetric 3D Reconstruction with Ray Potentials, D. Paschalidou and A. O. Ulusoy and C. Schmitt and L. Gool and A. Geiger. CVPR'18.
- MVSNet: Depth Inference for Unstructured Multi-view Stereo, Y. Yao, Z. Luo, S. Li, T. Fang, L. Quan. ECCV 2018.
- Learning Unsupervised Multi-View Stereopsis via Robust Photometric Consistency, T. Khot, S. Agrawal, S. Tulsiani, C. Mertz, S. Lucey, M. Hebert. 2019.
- DPSNET: END-TO-END DEEP PLANE SWEEP STEREO, Sunghoon Im, Hae-Gon Jeon, Stephen Lin, In So Kweon. 2019.
- Point-based Multi-view Stereo Network, Rui Chen, Songfang Han, Jing Xu, Hao Su. ICCV 2019.

## Legacy
- Descriptors:
	- CENSUS, BRIEF
- SGM;