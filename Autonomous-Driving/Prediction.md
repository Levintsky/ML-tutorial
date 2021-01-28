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

## PnP Together
- **FaF**
- **IntentNet**
- **SPAGNN**
- M Liang, B Yang, R Hu, Y Chen, R Urtasun. Learning Lane Graph Representations for Structured Prediction.
	- Main take-away: use lane graph rather than rasterize;
	- Input: lane graph, BEV Lidar, camera images;
	- Output: prediction;
	- 1. Perception: BEV + camera, fusion + detection;
	- 2. Lane-graph: Graph U-Net;
		- Lane graph connection: predecessor, successor, left/right neighbor;
		- Lane graph op: parametric conv, pool, unpool;
	- Combine 1, 2 for structured prediction;
- Davi Frossard, Eric Kee Raquel Urtasun. DeepSignals: Predicting Intent of Drivers Through Visual Attributes. CoRL'18, ICRA'19
	- Insight: detect turn signals to predict turn;
	- Signal: left/right/flashers/off/unknown;
	- Model: CNN + LSTM;
- Predicting Motion of Vulnerable Road Users using High-Definition Maps and Efficient ConvNets [NIPS'18, Pitts]
- PnP with Radar [Benson Guo];

## Pedestrian
- A. Alahi, K. Goel, V. Ramanathan, A. Robicquet, L. Fei-Fei, and S. Savarese. Social LSTM: Human Trajectory Prediction in Crowded Spaces. CVPR'16
- S. Yi, H. Li, and X. Wang. Pedestrian Behavior Understanding and Prediction with Deep Neural Networks. ECCV'16
- S. Hoermann, M. Bach, and K. Dietmayer. Dynamic Occupancy Grid Prediction for Urban Autonomous Driving: A Deep Learning Approach with Fully Automatic Labeling. IV'17
- S. Becker, R. Hug, W. Hubner, and M. Arens. An Evaluation of Trajectory Prediction Approaches and Notes on the TrajNet Benchmark. CoRR'18
- **Social GAN**: A. Gupta, J. Johnson, L. Fei-Fei, S. Savarese, and A. Alahi. Social GAN: Socially Acceptable Trajectories with Generative Adversarial Networks. CVPR'18
- D. Ridel, E. Rehder, M. Lauer, C. Stiller, and D. Wolf. A literature review on the prediction of pedestrian behavior in urban scenarios. In Proceedings of the International Conference on Intelligent Transportation Systems, November 2018.
- A. Rudenko, L. Palmieri, M. Herman, K. M. Kitani, D. M. Gavrila, and K. O. Arras. Human
motion trajectory prediction: A survey. ArXiv, abs/1905.06113, 2019.
- W.-C. Ma, D.-A. Huang, N. Lee, and K. M. Kitani. Forecasting interactive dynamics of pedestrians with fictitious play. CVPR'17
- History:
	- B. D. Ziebart, N. Ratliff, G. Gallagher, C. Mertz, K. Peterson, J. A. Bagnell, M. Hebert, A. K. Dey, and S. Srinivasa. Planning-based prediction for pedestrians. IROS'09
- **DRF-Net**: Ajay Jain, Sergio Casas, Renjie Liao, Yuwen Xiong, Song Feng, Sean Segal, Raquel Urtasun. Discrete Residual Flow for Probabilistic Pedestrian Behavior Prediction. CoRL'19

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

## Scene Prediction
- **SPCSFNet**: Xinshuo Weng, Jianren Wang, Sergey Levine, Kris Kitani, Nicholas Rhinehart. Unsupervised Sequence Forecasting of 100,000 Points for Unsupervised Trajectory Forecasting. ECCV'20
	- Insight: Define a new task, Scene Point Cloud Sequence Forecasting;
	- https://github.com/xinshuoweng/SPCSF
	- Problem: input M frames, output N frames; i.e., predict a new point cloud for whole scene;
	- Model:
		- Encoder-LSTM-decoder;
		- Encoder: pointnet for point clouds; transformer + 2D-CNN for HxW range map;
		- Decoder: K x 3 MLP, 2D-CNN;
		- Losses: Chamfer for points, L1 for range image, 
	- Prediction as detection (Point RCNN);
	- Tracking with Kalman Filter;
	- Prediction metrics: Hungarian matching with ground truth;
	- Experiments: Kitti, nuScenes;

## Trajectories, Multi-Agent
- **TrafficPredict**: Y. Ma et al., TrafficPredict: Trajectory Prediction for Heterogeneous Traffic-Agents. 2018
- J. Ren et al., Heter-Sim: Interactive data-driven optimization for simulating heterogeneous multi-agent systems. arxiv'18
- Q. Chao, Z. Deng, J. Ren, Q. Ye, X. Jin, Realistic Data-Driven Traffic Flow Animation Using Texture Synthesis. TVCG'18
- Chen Sun, Per Karlsson, Jiajun Wu, Joshua B. Tenenbaum, and Kevin Murphy. Stochastic prediction of multi-agent interactions from partial observations. CoRR'19
	- Multi-modality
- Nicholas Watters, Daniel Zoran, Theophane Weber, Peter Battaglia, Razvan Pascanu, and Andrea Tacchetti. Visual interaction networks: Learning a physics simulator from video. NIPS'17
- **R2P2**: N. Rhinehart, K. M. Kitani, and P. Vernaza. R2P2: A reparameterized pushforward policy for diverse, precise generative path forecasting. ECCV'18
	- Insight: Deep Generative Imitation Learning (like GAIL)
	- Diversity-precision tradeoff with **symmetric cross-entropy** H(p,q) for mode coverage, H(q,p) for precision; loss = H(p,q)+beta H(q,p);
	- Pushforward parameterization to render inference and learning in this model efficient;
		- q(x) = q(z) |det(J)|^(-1)
	- Prior approximation;
	- CNN - RNN; Verlet prediction;
- **PRECOG**: Nicholas Rhinehart, Rowan McAllister, Kris M. Kitani, and Sergey Levine. PRECOG: prediction conditioned on goals in visual multi-agent settings. CoRR'19
	- https://sites.google.com/view/precog
	- Insight: extend R2P2 one-step single-agent;
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

## Interaction
- V2VNet: Vehicle-to-vehicle communication to improve PnP performance [Johnson Wang]
	- Sender SDV: CNN, compress send; Receiver SDV: GNN;
- Interaction Transformer for Prediction [Luke Li]
	- Recurrent interaction process;

## Game Theory
- M. Tan. Multi-agent reinforcement learning: Independent vs. cooperative agents. ICML'93
- C. Claus and C. Boutilier. The dynamics of reinforcement learning in cooperative multiagent systems. AAAI'98
- F. S. Melo and M. Veloso. with sparse interactions. AI'11
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