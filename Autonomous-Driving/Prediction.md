# Prediction

## PnP Together
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
	<img src="/Autonomous-Driving/images/prediction/faf.png" alt="drawing" width="500"/>
- **IntentNet**: S Casas, W Luo, R Urtasun. IntentNet: Learning to Predict Intention from Raw Sensor Data. CoRL'18
	- Input: 1. 3D point cloud; (BEV) stack time on height; 2. dynamic maps;
	- Output: 1. trajectory regression; (a sequence of bounding boxes); 2. high level actions (keep lane, turn left/right, left/right lane change, stopping, stopped, parked)
	- Output head: 1. detection branch; (anchors) 2. intention branch; 3. intention as an embedding for motion estimation/regression;
	- **Two-stream + Late fusion**: predict probability of being a vehicle; predict bounding box into the future;
	- Predicts: detection scores for vehicle and background classes, high level action probabilities corresponding to discrete intention, and bounding box regressions in the current and future time steps to represent the intended trajectory;\
		<img src="/Autonomous-Driving/images/prediction/intentnet.png" alt="drawing" width="600"/>
- Sergio Casas, Cole Gulino, Renjie Liao, Raquel Urtasun. SPAGNN: Spatially-Aware Graph Neural Networks for Relational Behavior Forecasting from Sensor Data. 2019
	- Insight: Improve on FaF and IntentNet with GraphNN + GaBP to handle interaction.\
		<img src="/Autonomous-Driving/images/prediction/spagnn.png" alt="drawing" width="600"/>
- M Liang, B Yang, R Hu, Y Chen, R Urtasun. Learning Lane Graph Representations for Structured Prediction.
	- Main take-away: use lane graph rather than rasterize;
	- Input: lane graph, BEV Lidar, camera images;
	- Output: prediction;
	- 1. Perception: BEV + camera, fusion + detection;
	- 2. Lane-graph: Graph U-Net;
		- Lane graph connection: predecessor, successor, left/right neighbor;
		- Lane graph op: parametric conv, pool, unpool;
	- Combine 1, 2 for structured prediction;
- Davi Frossard, Eric Kee Raquel Urtasun. DeepSignals: Predicting Intent of Drivers Through Visual Attributes. ICRA’19
	- CNN + LSTM
- Predicting Motion of Vulnerable Road Users using High-Definition Maps and Efficient ConvNets [NIPS'18, Pitts]
- PnP with Radar [Benson Guo];

## Pure Prediction
- **GPRF**: Kihwan Kim, Dongryeol Lee, Irfan Essa. Gaussian Process Regression Flow for Analysis of Motion Trajectories. ICCV'11
	- http://www.cc.gatech.edu/cpl/projects/gprf/
	- Framework:\
		<img src="/Autonomous-Driving/images/prediction/gprf-1.png" alt="drawing" width="400"/>
	- Input space x position (u, v, t); output y (yu, yv, yt) (yt: frame difference as a constant), with Gaussian process:\
		<img src="/Autonomous-Driving/images/prediction/gprf-2.png" alt="drawing" width="400"/>\
		<img src="/Autonomous-Driving/images/prediction/gprf-3.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/prediction/gprf-4.png" alt="drawing" width="400"/>
	- Train k GPRF for each class;
	- Classification of Trajectories: Similarity for Complete Trajectories;\
		<img src="/Autonomous-Driving/images/prediction/gprf-5.png" alt="drawing" width="400"/>
	- Prediction of Trajectories: Similarity for Complete Trajectories;\
		<img src="/Autonomous-Driving/images/prediction/gprf-6.png" alt="drawing" width="400"/>
- Mayank Bansal, Alex Krizhevsky, and Abhijit S. Ogale. Chauffeurnet: Learning to drive by imitating the best and synthesizing the worst. CoRR'18
- Multi future:
	- Nachiket Deo and Mohan M. Trivedi. Convolutional social pooling for vehicle trajectory prediction. CoRR'18
	- Henggang Cui, Vladan Radosavljevic, Fang-Chieh Chou, Tsung-Han Lin, Thi Nguyen, Tzu-Kuo Huang, Jeff Schneider, and Nemanja Djuric. Multimodal trajectory predictions for autonomous driving using deep convolutional networks. ICRA'19
	- **DSF**: Ye Yuan, Kris M. Kitani. Diverse Trajectory Forecasting with Determinantal Point Processes. ICLR'20 \
		<img src="/Autonomous-Driving/images/prediction/dsf.png" alt="drawing" width="400"/>
- **Multipath**: Yuning Chai, Benjamin Sapp, Mayank Bansal, and Dragomir Anguelov. Multipath: Multiple probabilistic anchor trajectory hypotheses for behavior prediction. 2019
- Tianyang Zhao, Yifei Xu, Mathew Monfort, Wongun Choi, Chris Baker, Yibiao Zhao, Yizhou Wang, and Ying Nian Wu. Multi-agent tensor fusion for contextual trajectory prediction. CoRR'19
- **MFP**: Yichuan Charlie Tang, Ruslan Salakhutdinov. Multiple Futures Prediction. NIPS'19
	- Insight: semantically meaningful latent variables for multimodality; interactive and step-wise rollouts; hypothetical inference;
	- Input: X (past), I (context); output: Y; P(Y|X, I)
	- Multimodality: naive RNN + BPTT will cause mode averaging; solution: latent z;
	- Assumptions:
		- One z (latent intention) remains consistent for all Y;
		- Agent i has access to its own latent Zi and others' observed Yj
	- ELBO: q(Z) to approximate p(Z|Y, X, theta), latent Z: discrete with small cardinality (< 10)
	- Classmate forcing:
	- State encoding:
	- Hypothetical rollouts:
	- Experiments: CARLA PRECOG; NGSIM;
	<img src="/Autonomous-Driving/images/prediction/mfp.png" alt="drawing" width="600"/>
	<img src="/Autonomous-Driving/images/prediction/mfp-elbo.png" alt="drawing" width="600"/>

## Trajectories, Multi-Agent
- **TrafficPredict**: Y. Ma et al., TrafficPredict: Trajectory Prediction for Heterogeneous Traffic-Agents. 2018
- J. Ren et al., Heter-Sim: Interactive data-driven optimization for simulating heterogeneous multi-agent systems. arxiv'18
- Q. Chao, Z. Deng, J. Ren, Q. Ye, X. Jin, Realistic Data-Driven Traffic Flow Animation Using Texture Synthesis. TVCG'18
- Chen Sun, Per Karlsson, Jiajun Wu, Joshua B. Tenenbaum, and Kevin Murphy. Stochastic prediction of multi-agent interactions from partial observations. CoRR'19
	- Multi-modality
- Nicholas Watters, Daniel Zoran, Theophane Weber, Peter Battaglia, Razvan Pascanu, and Andrea Tacchetti. Visual interaction networks: Learning a physics simulator from video. NIPS'17
- **R2P2**: N. Rhinehart, K. M. Kitani, and P. Vernaza. R2P2: A reparameterized pushforward policy for diverse, precise generative path forecasting. ECCV'18
- **PRECOG**: Nicholas Rhinehart, Rowan McAllister, Kris M. Kitani, and Sergey Levine. PRECOG: prediction conditioned on goals in visual multi-agent settings. CoRR'19
	- https://sites.google.com/view/precog
	- Key: a factorized flow-based generative model that forecasts the joint state of all agents; the use of factorized latent variables to model decoupled agent intentions even though agent dynamics are coupled;
	- Problem setup: input lidar; output: future trajectory based on **goal**;
		<img src="/Autonomous-Driving/images/prediction/precog1.png" alt="drawing" width="500"/>
	- Model: POMDP, A-agents, T-steps, D=2 (x, y); **flow-based method, invertible**;
	- **ESP**: Estimating Social-forecast Probabilities;
	- Gaussian for each agent;\
		<img src="/Autonomous-Driving/images/prediction/precog2.png" alt="drawing" width="250"/>
	- Model all together:\
		<img src="/Autonomous-Driving/images/prediction/precog2.png" alt="drawing" width="600"/>
	- Planning: learn a prior for latent z;
- RL-like, Imitation:
	- N. Deoand, M. M. Trivedi. Multi-modal trajectory prediction of surrounding vehicles with maneuver based LSTMs. 2018
	- **Desire**: Namhoon Lee, Wongun Choi, Paul Vernaza, Chris Choy, Philip H. S. Torr, and Manmohan Chandraker. Desire: Distant future prediction in dynamic scenes with interacting agents. 2017
		- Multi future;
	- S. Park, B. Kim, C. M. Kang, C. C. Chung, and J. W. Choi. Sequence-to-sequence prediction of vehicle trajectory via LSTM encoder-decoder architecture. arxiv'18

## Game Theory
- M. Tan. Multi-agent reinforcement learning: Independent vs. cooperative agents. ICML'93
- C. Claus and C. Boutilier. The dynamics of reinforcement learning in cooperative multiagent systems. AAAI'98
-  F. S. Melo and M. Veloso. with sparse interactions. AI'11
- J. F. Fisac, E. Bronstein, E. Stefansson, D. Sadigh, S. S. Sastry, and A. D. Dragan. Hierarchical game-theoretic planning for autonomous vehicles. arxiv'18

## Physics
- Greg Welch, Gary Bishop, et al. An introduction to the kalman filter. 1995
- Tuomas Haarnoja, Anurag Ajay, Sergey Levine, and Pieter Abbeel. Backprop KF: learning discriminative deterministic state estimators. CoRR'16
- Stéphanie Lefèvre, Dizan Vasquez, and Christian Laugier. A survey on motion prediction and risk assessment for intelligent vehicles. 2014

## Misc
- T. Streubel and K. H. Hoffmann. Prediction of driver intended path at intersections. 2014
- D. J. Phillips, T. A. Wheeler, and M. J. Kochenderfer. Generalizable intention prediction of human drivers at intersections. IV'17
- Y. Hu, W. Zhan, and M. Tomizuka. Probabilistic prediction of vehicle semantic intention and motion. arxiv'18
- N Djuric, V Radosavljevic, H Cui, T Nguyen, F Chou, T Lin, and J Schneider. Motion prediction of traffic actors for autonomous driving using deep convolutional networks. 2018