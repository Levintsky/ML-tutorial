# Human Pose/Parsing

## Problem Definition
- Skeleton joint prediction from images;

## Benchmakrs
- K. Yamaguchi, M. H. Kiapour, L. E. Ortiz, and T. L. Berg. Parsing clothing in fashion photographs. CVPR'12
- X. Chen, R. Mottaghi, X. Liu, S. Fidler, R. Urtasun, and A. Yuille. Detect what you can: Detecting and representing objects using holistic models and body parts. CVPR'14
- CMU Mocap:
	- http://mocap.cs.cmu.edu/
- **Human3.6M**: Catalin Ionescu, Dragos Papava, Vlad Olaru, Cristian Sminchisescu. Large Scale Datasets and Predictive Methods for 3D Human Sensing in Natural Environments. PAMI'14
	- http://vision.imar.ro/human3.6m/description.php
- M. Andriluka, L. Pishchulin, P. V. Gehler, and B. Schiele. 2d human pose estimation: New benchmark and state of the art analysis. CVPR'14
- COCO keypoint detection dataset.
- **MOT16**: A. Milan, L. Leal-Taixe, I. D. Reid, S. Roth, and K. Schindler. MOT16: A benchmark for multi-object tracking. CoRR'16
- K. Gong, X. Liang, X. Shen, and L. Lin. Look into person: Self-supervised structure-sensitive learning and a new benchmark for human parsing. arxiv'17
- M. Andriluka, U. Iqbal, A. Milan, E. Insafutdinov,
L. Pishchulin, J. Gall, and B. Schiele. Posetrack: A benchmark for human pose estimation and tracking. CVPR'18

## Legacy
- Y. Yang and D. Ramanan. Articulated pose estimation with flexible mixtures-of-parts. CVPR'11
- L. Pishchulin, M. Andriluka, P. V. Gehler, and B. Schiele. Poselet conditioned pictorial structures. CVPR'13

## Deep Learning
- Two mainstream methods:
	- Regress position;
	- Heatmap;
- Position regression:
	- **DeepPose**: A Toshev, C Szegedy. DeepPose: Human Pose Estimation via Deep Neural Networks. CVPR'14
	- J. Carreira, P. Agrawal, K. Fragkiadaki, and J. Malik. Human pose estimation with iterative error feedback. CVPR'16
- Heatmap:
	- X. Chu, W. Ouyang, H. Li, and X. Wang. Structured feature learning for pose estimation. CVPR'16
		- Iterative inference process;
	- W. Yang, W. Ouyang, H. Li, and X. Wang. End-to-end learning of deformable mixture of parts and deep convolutional neural networks for human pose estimation. CVPR'16
	- X. Chu, W. Yang, W. Ouyang, C. Ma, A. L. Yuille, and X. Wang. Multi-context attention for human pose estimation. CVPR'17
- J. J. Tompson, A. Jain, Y. LeCun, and C. Bregler. Joint training of a convolutional network and a graphical model for human pose estimation. NIPS'14
- W. Ouyang, X. Chu, and X. Wang. Multi-source deep learning for human pose estimation. CVPR'14
- A. Bulat and G. Tzimiropoulos. Human pose estimation via convolutional part heatmap regression. ECCV'16
- E. Insafutdinov, L. Pishchulin, B. Andres, M. Andriluka, and B. Schiele. Deepercut: A deeper, stronger, and faster multiperson pose estimation model. ECCV'16
- S Wei and V Ramakrishna, T Kanade and Y Sheikh. Convolutional pose machines. CVPR'16
- Z Cao, T Simon, S Wei, Y Sheikh. Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields. CVPR'17
	- Key idea: bottom-up, part affinity fields (PAFs)
- T Simon and H Joo and I Matthews and Y Sheikh. Hand Keypoint Detection in Single Images using Multiview Bootstrapping. CVPR'17
- **OpenPose**: OpenPose: realtime multi-person 2D pose estimation using Part Affinity Field. 2018
	- https://github.com/CMU-Perceptual-Computing-Lab/openpose
- H Joo, T Simon, Y Sheikh. Total Capture: A 3D Deformation Model for Tracking Faces, Hands, and Bodies. CVPR'18
- Y. Xiu, J. Li, H. Wang, Y. Fang, and C. Lu. Pose flow: Efficient online pose tracking. BMVC'18
- **DensePose**:
	- http://densepose.org/
	- Riza Alp Güler, Natalia Neverova, Iasonas Kokkinos. DensePose: Dense Human Pose Estimation In The Wild. CVPR'18
		- https://github.com/facebookresearch/Densepose
		- Dataset: match SMPL to COCO;\
		- Insight: RPN-style (mask-RCNN) better than FCN; cascade helps;\
			<img src="/CV-2D/images/detection/densepose.png" alt="drawing" width="400"/>
	- Natalia Neverova, David Novotny, Andrea Vedaldi. Correlated Uncertainty for Learning Dense Correspondences from Noisy Labels. NeurIPS'19
- M. Kocabas, S. Karagoz, and E. Akbas. Multiposenet: Fast multi-person pose estimation using pose residual network. ECCV'18
- HRNet:
	- https://github.com/leoxiaobin/deep-high-resolution-net.pytorch
