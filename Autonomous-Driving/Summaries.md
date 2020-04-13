# Summaries

## Perception (& Prediction)
- Input: BEV, front view Lidar, images, HD-map;
- Output/task: detection, tracking, prediction? planning?
- Baidu:
	- VeloFCN [Tian Xia]	
	- MV3D: BEV detection;
- Uber:
	- Pixor [Bin, CVPR'18]: 1-stage detection;
		- BEV, resnet, output 2d orientated bbox;
	- FaF [Wenjie, CVPR'18]: detection + tracking + prediction;
	- IntentNet [S Casas, ICRA'18]:
		- Improve on FaF with HD Map input, two-stream;
	- Deep continuous fusion [Ming, ECCV'18]: detection;
		- BEV + image, image result unproject to Lidar
	- Multi-Task Multi-censor [Ming, CVPR'19]: 2D, 3D detection, ground, depth-completion;
	- LaserNet [CVPR'19]: range view; FCN + adaptive-NMS;
	- DeepSignals [ICRA’19, D Frossard]: image to prediction;
		- CNN + LSTM;
	- SPAGNN [19]: stage-1 detection + stage-2 GNN-prediction;
	- Discrete residual flow [Jain, A.]: Pedestrian prediction;
		- Occupancy based (generally bbox + trajectory are more popular);
- Waymo:
	- MultiPath ['19]
- Apple:
	- VoxelNet [Yin Zhou, CVPR'18]: 2-stage detection;
		- Key idea: voxel; within each voxel: VFE; RPN-based detection;
	- Multiple Futures Prediction. [NIPS'19]
- PointRCNN [X Wang, CVPR'19]

## Segmentation
- LidarSeg:
	- C. Zhang,W. Luo, and R. Urtasun. Efficient convolutions for real-time semantic segmentation of 3d point clouds. 3DV'18
- ImageSeg:
	- UPSNet;

## Planning
- End-to-end:
	- ALVINN: 1989
	- NVIDIA:
		- End to end learning for self-driving cars ['16]
			- Image to control with CNN
		- Learning to drive in a day. ['18]
	- Intel:
		- End-to-end driving via conditional imitation learning. [ICRA'18]
			- Conditioned on goal
	- Uber:
		- Neural motion planner [Wenyuan, CVPR'19]
	- Exploring the limitations of behavior cloning for autonomous driving. [ICCV'19]
		- Problem of E2E;
- Regress the control:
	- Waymo:
		- Chauffeurnet:
			- Take as input mid-level feature from perception;
			- AgentRNN for self and PerceptionRNN for predicting others;
	- Lates: Latent space distillation for teacher-student driving policy learning. [Soatto'19]
	- Urban driving with conditional imitation. arxiv'19
- Cost, max-margin (then evaluate):
	- An auto-tuning framework for autonomous vehicles. arxiv'18
	- Towards navigation without precise localization: Weakly supervised learning of goal-directed navigation cost map. arxiv'19
	- Learning to predict ego-vehicle poses for sampling-based nonholonomic motion planning.
	- Uber:
		- PLT Jointly learnable behavior and trajectory planning for self-driving vehicles. [ICRA'18]
		- Neural Planner [Wenyuan, 19];
		- Percept, Predict, Plan [, 20]
