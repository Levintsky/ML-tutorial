# Prediction

## Basics
- Problems:
	- Trajectory forecast;
	- Video/3D-scene prediction;
- Main challenges:
	- What metric? L2? deviation in lane and across lane is very different! Requires customized loss; (traffic-rule, behavior, ...)
	- Multi-modality;
- Model: 
	- GNN: Agent feature + map feature;
	- Behavior/activity forecast (walk/run, left turn/straight);
	- Map feature important!
		- Larger receptive field (red light xx m away!)
		- Rasterization: different lane with different color;
	- SOTA on public dataset: lane-graph;
	- Generative modeling;
- How to solve multi-modality?
	- K-mode output: loss for with the closest to ground truth;

## Task-setup/Framework
- Uber:
	- FaF [cvpr'18]: detection + tracking + prediction;
	- IntentNet [CoRL'18]: detection + trajectory + high-level action;
	- SPAGNN [ICRA'20]: GNN for interaction;
	- DeepSignals: [CoRL'18, ICRA'19]
	- PnP with Radar [Benson Guo];
- Waymo:
	- Pedestrian: [STINet: CVPR'20] detection + tracking + prediction;
- Perception + Prediction:
	- Uber-ATG. SPAGNN: Spatially-Aware Graph Neural Networks for Relational Behavior Forecasting from Sensor Data. ICRA'20
	- Lane-graph: Uber-ATG. Learning Lane Graph Representations for Structured Prediction.
		- Extra input of lane-graph;
	- Uber-ATG. Predicting Motion of Vulnerable Road Users using High-Definition Maps and Efficient ConvNets [NeurIPS'18]
- Raw-scene-detection: (not state)
	- SPCSFNet: N Rhinehart. Unsupervised Sequence Forecasting of 100,000 Points for Unsupervised Trajectory Forecasting. ECCV'20
		- Predict Scene Point Cloud Sequence Forecasting;
		- https://github.com/xinshuoweng/SPCSF
- High-level, predict intention:
	- T Streubel and K Hoffmann. Prediction of driver intended path at intersections. 2014
	- D Phillips, T Wheeler, and M Kochenderfer. Generalizable intention prediction of human drivers at intersections. IV'17
	- Y. Hu, W. Zhan, and M. Tomizuka. Probabilistic prediction of vehicle semantic intention and motion. arxiv'18

## Backbone
- BEV-CNN:
	- FaF: PIXOR-conv + ssd + tracking-by-detection (tracklet)
	- Intent: 2-stream + late fusion;
- CNN + LSTM:
	- DeepSignals;
	- SPCSFNet: CNN + LSTM + decoder;
- CNN + GNN:
	- SPAGNN;
	- Lane-graph: Graph UNet for lane;
	- STINet: Res-UNet + T-RPN + GNN;
- Transformer:
	- L Li, B Yang, M Liang, M Ren, W Zeng, S Segal, R Urtasun. End-to-end Contextual Perception and Prediction with Interaction Transformer. IROS'20
- Gaussian Process:
	- GPRF: K Kim, D Lee, I Essa. Gaussian Process Regression Flow for Analysis of Motion Trajectories. ICCV'11
		- http://www.cc.gatech.edu/cpl/projects/gprf/
		- Task: tracks from video -> GPR -> vector + conf
		- Input space x position (u, v, t);
		- output y (yu, yv, yt) (yt: frame diff)
		- Train k GPRF for each class;
		- Classification of Traj: Similarity for Complete Traj;
			- Pick the one with highest MLE;
		- Prediction of Traj: Similarity for Complete Traj;

## Representation/Supervision
- Flow-based generative model:
	- N. Rhinehart, et. al. R2P2: A reparameterized pushforward policy for diverse, precise generative path forecasting. ECCV'18
		- Insight: Deep Generative Imitation Learning (like GAIL)
		- Diversity-precision tradeoff:
			- H(p,q) for mode coverage
			- H(q,p) for precision
			- loss = H(p,q)+β H(q,p);
		- Pushforward parameterization to render inference and learning in this model efficient;
			- q(x) = q(z) |det(J)|^(-1)
		- Prior approximation;
		- CNN - RNN; Verlet prediction;
	- N Rhinehart. PRECOG: prediction conditioned on goals in visual multi-agent settings. CoRR'19
		- https://sites.google.com/view/precog
		- Insight: extend R2P2 1-step 1-agent to multi;
		- Problem setup: input lidar; goal
		- output: future trajectory;
		- Model: ESP-forcasting + Precog-planning;
			- ESP: Estimating Social-forecast Probabilities;
			- POMDP, A-agents, T-steps, Dim=2 (x, y);
		- Gaussian for each agent:
			- S.t,a = μ.θ(S.1:t-1, φ) + σ(S.1:t-1,φ)Z
		- Planning: learn a prior for latent z;

## Multimodality/Multi-Future
- Insight:
	- Extra reward/supervision for diversity;
	- Multimodality: naive RNN + BPTT will cause mode averaging;
		- solution: latent z;
- N Deo and M Trivedi. Convolutional social pooling for vehicle trajectory prediction. CoRR'18
- N Djuric, V Radosavljevic, H Cui, T Nguyen, F Chou, T Lin, and J Schneider. Motion prediction of traffic actors for autonomous driving using deep convolutional networks. 2018
- Uber-ATG. Multimodal trajectory predictions for autonomous driving using deep convolutional networks. ICRA'19
- DSF: Y Yuan, K Kitani. Diverse Trajectory Forecasting with Determinantal Point Processes. ICLR'20
	- cVAE + DPP;
- MFP: Y Tang, R Salakhutdinov. Multiple Futures Prediction. NIPS'19
	- Insight: semantically meaningful latent variables for multimodality; interactive and step-wise rollouts; hypothetical inference;
	- Input: X (past), I(context); output: Y; P(Y|X, I)
	- Model: past x..t, future y.t+1..., latent zi;
		- Agent i: xt,i; zi -> [RNN] -> y.t+1,i, y.t+2,i, ...
		- Agent i has access to its own latent Zi and others' observed Yj
		- latent Z: discrete with small cardinality (< 10)
	- ELBO: q(Z) to approximate p(Z|Y, X, θ)
	- Brute-force to minimize KL(q,p)
	- Tricks: classmate forcing; Hypothetical rollouts:
	- Experiments: CARLA PRECOG; NGSIM;
- Waymo. Multipath: Multiple probabilistic anchor trajectory hypotheses for behavior prediction. 2019

## Pedestrian
- Legacy:
	- B Ziebart, N Ratliff, G Gallagher, C Mertz, K Peterson, J Bagnell, M Hebert, A Dey, and S Srinivasa. Planning-based prediction for pedestrians. IROS'09
- A. Alahi, K. Goel, V. Ramanathan, A. Robicquet, L. Fei-Fei, and S. Savarese. Social LSTM: Human Trajectory Prediction in Crowded Spaces. CVPR'16
- S. Yi, H. Li, and X. Wang. Pedestrian Behavior Understanding and Prediction with Deep Neural Networks. ECCV'16
- S. Hoermann, M. Bach, and K. Dietmayer. Dynamic Occupancy Grid Prediction for Urban Autonomous Driving: A Deep Learning Approach with Fully Automatic Labeling. IV'17
- W Ma, D Huang, N Lee, and K Kitani. Forecasting interactive dynamics of pedestrians with fictitious play. CVPR'17
- S. Becker, R. Hug, W. Hubner, and M. Arens. An Evaluation of Trajectory Prediction Approaches and Notes on the TrajNet Benchmark. CoRR'18
- Social-GAN: A. Gupta, J. Johnson, L. Fei-Fei, S. Savarese, and A. Alahi. Social GAN: Socially Acceptable Trajectories with Generative Adversarial Networks. CVPR'18
- D. Ridel, E. Rehder, M. Lauer, C. Stiller, and D. Wolf. A literature review on the prediction of pedestrian behavior in urban scenarios. 2018
- A Rudenko, L Palmieri, M Herman, K Kitani, D Gavrila, and K Arras. Human motion trajectory prediction: A survey. arxiv'19
- **DRF-Net**: Uber-ATG. Discrete Residual Flow for Probabilistic Pedestrian Behavior Prediction. CoRL'19

## Pure Prediction
- T Zhao, Y Xu, M Monfort, W Choi, C Baker, Y Zhao, Y Wang, and Y Wu. Multi-agent tensor fusion for contextual trajectory prediction. CoRR'19

## Trajectories, Multi-Agent
- **TrafficPredict**: Y. Ma et al., TrafficPredict: Trajectory Prediction for Heterogeneous Traffic-Agents. 2018
- J. Ren et al., Heter-Sim: Interactive data-driven optimization for simulating heterogeneous multi-agent systems. arxiv'18
- Q. Chao, Z. Deng, J. Ren, Q. Ye, X. Jin, Realistic Data-Driven Traffic Flow Animation Using Texture Synthesis. TVCG'18
- C Sun, P Karlsson, J Wu, J Tenenbaum, and K Murphy. Stochastic prediction of multi-agent interactions from partial observations. CoRR'19
	- Multi-modality
- N Watters, D Zoran, T Weber, P Battaglia, R Pascanu, and A Tacchetti. Visual interaction networks: Learning a physics simulator from video. NIPS'17
- RL-like, Imitation:
	- N. Deoand, M. M. Trivedi. Multi-modal trajectory prediction of surrounding vehicles with maneuver based LSTMs. 2018
	- Desire: N Lee, W Choi, P Vernaza, C Choy, P Torr, and M Chandraker. Desire: Distant future prediction in dynamic scenes with interacting agents. 2017
		- Multi future;
	- S Park, B Kim, C Kang, C Chung, and J Choi. Sequence-to-sequence prediction of vehicle trajectory via LSTM encoder-decoder architecture. arxiv'18
- Game Theory
	- M Tan. Multi-agent reinforcement learning: Independent vs. cooperative agents. ICML'93
	- C Claus and C Boutilier. The dynamics of reinforcement learning in cooperative multiagent systems. AAAI'98
	- F Melo and M Veloso. Decentralized MDPs with sparse interactions. AI'11
	- J Fisac, E Bronstein, E Stefansson, D Sadigh, S Sastry, and A Dragan. Hierarchical game-theoretic planning for autonomous vehicles. arxiv'18
- Interaction
	- V2VNet: Vehicle-to-vehicle communication to improve PnP performance [Johnson Wang]
		- Sender SDV: CNN, compress send; Receiver SDV: GNN;
	- Interaction Transformer for Prediction [Luke Li]
		- Recurrent interaction process;

## Physics
- G Welch, G Bishop, et al. An introduction to the kalman filter. 1995
- T Haarnoja, A Ajay, S Levine, and P Abbeel. Backprop KF: learning discriminative deterministic state estimators. CoRR'16
- S Lefèvre, D Vasquez, and C Laugier. A survey on motion prediction and risk assessment for intelligent vehicles. 2014
