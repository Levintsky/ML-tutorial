# People/Pedestrian/Face...

## Re-Identification
- Tasks:
	- Re-id: the person retrieval problem under a multi-camera setup;
- Benchmark
	- Market-1501;
	- DukeMTMC-reID;
	- MSMT17;

## Human Parsing
- Problem Definition
	- Skeleton joint prediction from images;
- Benchmakrs
	- K. Yamaguchi, M. H. Kiapour, L. E. Ortiz, and T. L. Berg. Parsing clothing in fashion photographs. CVPR'12
	- X. Chen, R. Mottaghi, X. Liu, S. Fidler, R. Urtasun, and A. Yuille. Detect what you can: Detecting and representing objects using holistic models and body parts. CVPR'14
	- CMU Mocap:
		- http://mocap.cs.cmu.edu/
	- **Human3.6M**: Catalin Ionescu, Dragos Papava, Vlad Olaru, Cristian Sminchisescu. Large Scale Datasets and Predictive Methods for 3D Human Sensing in Natural Environments. PAMI'14
		- http://vision.imar.ro/human3.6m/description.php
	- K. Gong, X. Liang, X. Shen, and L. Lin. Look into person: Self-supervised structure-sensitive learning and a new benchmark for human parsing. arxiv'17
	- **DensePose**: http://densepose.org/
- **DeepPose**: A Toshev, C Szegedy. DeepPose: Human Pose Estimation via Deep Neural Networks. CVPR'14
- S Wei and V Ramakrishna, T Kanade and Y Sheikh. Convolutional pose machines. CVPR'16
- Z Cao, T Simon, S Wei, Y Sheikh. Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields. CVPR'17
	- Key idea: bottom-up, part affinity fields (PAFs)
- T Simon and H Joo and I Matthews and Y Sheikh. Hand Keypoint Detection in Single Images using Multiview Bootstrapping. CVPR'17
- **OpenPose**: OpenPose: realtime multi-person 2D pose estimation using Part Affinity Field. 2018
	- https://github.com/CMU-Perceptual-Computing-Lab/openpose
- H Joo, T Simon, Y Sheikh. Total Capture: A 3D Deformation Model for Tracking Faces, Hands, and Bodies. CVPR'18
- **DensePose**:
	- http://densepose.org/
	- Riza Alp Güler, Natalia Neverova, Iasonas Kokkinos. DensePose: Dense Human Pose Estimation In The Wild. CVPR'18
		- https://github.com/facebookresearch/Densepose
		- Dataset: match SMPL to COCO;\
		- Insight: RPN-style (mask-RCNN) better than FCN; cascade helps;\
			<img src="/CV-2D/images/detection/densepose.png" alt="drawing" width="400"/>
	- Natalia Neverova, David Novotny, Andrea Vedaldi. Correlated Uncertainty for Learning Dense Correspondences from Noisy Labels. NeurIPS'19

## Face Detection and Recognition
- Y Taigman, M Yang, M Ranzato, L Wolf. DeepFace: Closing the Gap to Human-Level Performance in Face Verification. CVPR'14
- F Schroff, D Kalenichenko, J Philbin. FaceNet: A Unified Embedding for Face Recognition and Clustering. CVPR'15
