# People/Pedestrian/Face...

## Basics
- Recognition:
	- Re-identification;
- Detection:
	- Pose: skeleton joint keypoints;

## Human Pose
- Benchmarks:
	- T Berg. Parsing clothing in fashion photographs. CVPR'12
	- R. Urtasun, and A. Yuille. Detect what you can: Detecting and representing objects using holistic models and body parts. CVPR'14
	- M Andriluka, L Pishchulin, P Gehler, and B Schiele. 2d human pose estimation: New benchmark and state of the art analysis. CVPR'14
	- MPII-Pose: 2d human pose estimation: New benchmark and state of the art analysis. CVPR'14
		- 25k images, 40k people
		- 410 human activities
	- COCO keypoint detection dataset.
	- CMU Mocap: http://mocap.cs.cmu.edu/
	- Human3.6M: http://vision.imar.ro/human3.6m/description.php
	- MOT16: CoRR'16
	- Look into person: '17
	- Posetrack: CVPR'18
- Legacy:
	- Y Yang and D Ramanan. Articulated pose estimation with flexible mixtures-of-parts. CVPR'11
	- L Pishchulin, M Andriluka, P Gehler, and B Schiele. Poselet conditioned pictorial structures. CVPR'13
- OpenPose: realtime multi-person 2D pose estimation using Part Affinity Field. 2018
	- https://github.com/CMU-Perceptual-Computing-Lab/openpose
- **DensePose**: FAIR.
	- DensePose: Dense Human Pose Estimation In The Wild. CVPR'18
	- http://densepose.org/
	- https://github.com/facebookresearch/Densepose
	- Dataset: match SMPL to COCO;
	- Insight: RPN-style (mask-RCNN) better than FCN; cascade helps;
	- N Neverova, D Novotny, A Vedaldi. Correlated Uncertainty for Learning Dense Correspondences from Noisy Labels. NeurIPS'19

## Re-Identification
- Tasks:
	- Re-id: the person retrieval problem under a multi-camera setup;
- Benchmark
	- Market-1501;
	- DukeMTMC-reID;
	- MSMT17;

## People Couting
- L Boominathan, S Kruthiventi, and R Babu. Crowdnet: A deep convolutional network for dense crowd counting. 
	- Task: counting;

## Face Detection and Recognition
- Y Taigman, M Yang, M Ranzato, L Wolf. DeepFace: Closing the Gap to Human-Level Performance in Face Verification. CVPR'14
- F Schroff, D Kalenichenko, J Philbin. FaceNet: A Unified Embedding for Face Recognition and Clustering. CVPR'15
- **Unitbox**: J Yu, Y Jiang, Z Wang, Z Cao, and T Huang. Unitbox: An advanced object detection network. ACMMM'16

## Gaze Estimation
- Task:
	- Estimate pupil or gaze direction?
	- Active, passive;
- Dataset:
	- **PupilNet**: W Fuhl, T Santini, G Kasneci, E Kasneci. PupilNet: Convolutional Neural Networks for Robust Pupil Detection. 2015
	- **NVGaze**: NVGaze: An Anatomically-Informed Dataset for Low-Latency, Near-Eye Gaze Estimation. ACM-CHI'19
		- Rendered image;
		- Neural net for estimation;
- Software:
	- Tobii
	- Pupil-labs: https://pupil-labs.com/
