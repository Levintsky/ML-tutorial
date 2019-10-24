# Prediction

## Map-Automation
- G Mattyus, W Luo and R Urtasun. DeepRoadMapper: Extracting Road Topology From Aerial Images. ICCV'17
- J. Liang, R. Urtasun. End-to-End Deep Structured Models for Drawing Crosswalks. ECCV'18

## PnP
- **FaF**: W. Luo, B. Yang, and R. Urtasun. Fast and furious: Real time end-to-end 3d detection, tracking and motion forecasting with a single convolutional net. CVPR'18
	- Input: 4D tensor from BEV 3D LiDAR (voxelized with height), temporal (all data changed to current frame coordinate system)
	- Output: 1. 3D detection; 2. tracking; 3. motion forecasting; (predict next 1 sec; no intent;)
	- Model:
		- Early/late fusion;
		- SSD-like one-stage detection: multi-boxes each location; different aspect ratio;
		- Tracking by detection: decoding tracklets;
	- Supervision:
		- Binary cross-entropy classification loss;
		- Regression-loss: find correspondence first (IoU > 0.4 with ground truth), 
	<img src="/Autonomous-Driving/images/pnp/faf.png" alt="drawing" width="500"/>
- **IntentNet**: S Casas, W Luo, R Urtasun. IntentNet: Learning to Predict Intention from Raw Sensor Data. CoRL'18
	- Input: 1. 3D point cloud; (BEV) stack time on height; 2. dynamic maps;
	- Output: 1. trajectory regression; (a sequence of bounding boxes); 2. high level actions (keep lane, turn left/right, left/right lane change, stopping, stopped, parked)
	- Output head: 1. detection branch; (anchors) 2. intention branch; 3. intention as an embedding for motion estimation/regression;
	- **Two-stream + Late fusion**: predict probability of being a vehicle; predict bounding box into the future;
	- Predicts: detection scores for vehicle and background classes, high level action probabilities corresponding to discrete intention, and bounding box regressions in the current and future time steps to represent the intended trajectory;
	<img src="/Autonomous-Driving/images/pnp/intentnet.png" alt="drawing" width="600"/>
- SPAGNN: Spatially-Aware Graph Neural Networks for Relational Behavior Forecasting from Sensor Data. 2019
	- Insight: Improve on FaF and IntentNet with GraphNN + GaBP to handle interaction.
	<img src="/Autonomous-Driving/images/pnp/spagnn.png" alt="drawing" width="600"/>
- M Liang, B Yang, R Hu, Y Chen, R Urtasun. Learning Lane Graph Representations for Structured Prediction.
	- Main take-away: use lane graph rather than rasterize;
	- Input: lane graph, BEV Lidar, camera images;
	- Output: prediction;
	- 1. Perception: BEV + camera, fusion + detection;
	- 2. Lane-graph: Graph U-Net;
		- Lane graph connection: predecessor, successor, left/right neighbor;
		- Lane graph op: parametric conv, pool, unpool;
	- Combine 1, 2 for structured prediction;

## Trajectories, Multi-Agent
- **TrafficPredict**: Y. Ma et al., TrafficPredict: Trajectory Prediction for Heterogeneous Traffic-Agents. 2018
- J. Ren et al., Heter-Sim: Interactive data-driven optimization for simulating heterogeneous multi-agent systems. arxiv'18
- Q. Chao, Z. Deng, J. Ren, Q. Ye, X. Jin, Realistic Data-Driven Traffic Flow Animation Using Texture Synthesis. TVCG'18

## Misc
- T. Streubel and K. H. Hoffmann. Prediction of driver intended path at intersections. 2014
- D. J. Phillips, T. A. Wheeler, and M. J. Kochenderfer. Generalizable intention prediction of human drivers at intersections. IV'17
- Y. Hu, W. Zhan, and M. Tomizuka. Probabilistic prediction of vehicle semantic intention and motion. arxiv'18
- N Djuric, V Radosavljevic, H Cui, T Nguyen, F Chou, T Lin, and J Schneider. Motion prediction of traffic actors for autonomous driving using deep convolutional networks. 2018