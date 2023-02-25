# Planning

## Summary
- Problem:
	- Input: current status and context (self, every actor else, traffic light, ...)
	- Output: a feasible trajectory
- Levels:
	- Behavior level;
	- Path-level; (only path, how to follow?)
- Formulation: IRL/loss-learning;
	- Cost-learning: learn a cost c(τ), s.t. trajectory minimize c(τ) to imitate expert;
		- Sampling/optimization based optimizer;
	- Imitation learning/supervised learning
		- Similar to cost learning, with explicit policy;
	- MPC (model-predictive control, solutions first); use model to propose a lot of solutions, pick the one with the lowest cost
	- End-to-end: ALVINN; NVIDIA; EndRun;
- Planning/inference:
	- A∗, variational, graph-bases;
	- Behavior cloning;
- Dataset for Imitation Learning
	- J. Colyar and J. Halkias, US highway 80 dataset, Federal Highway Administration (FHWA), 2006
	- J. Colyar and J. Halkias, US highway 101 dataset, Federal Highway Administration (FHWA), 2007
- Survey:
	- B Paden, M Čáp, S Yong, D Yershov, and E Frazzoli. A Survey of Motion Planning and Control Techniques for Self-driving Urban Vehicles. 2016

## Cost/Reward-Learning
- Insight: learn a cost/reward s.t. expert demo gets high score, other traj got low score;
- IRL:
	- Alvinn: D Pomerleau. Alvinn: An autonomous land vehicle in a neural network. NIPS'89
	- GAIL: A Kuefler, J Morton, T Wheeler, and M Kochenderfer. Imitating driver behavior with generative adversarial networks. IV'17
		- RNN planner: GRU with ELU; (GAIL GRU, GAIL MLP, BC GRU, and BC MLP)
		- Policy optimizer: TRPO;
		- NGSIM dataset
- Stanford. Junior: The stanford entry in the urban challenge. Journal of field Robotics. 2008
- M Buehler, K Iagnemma, and S Singh. The DARPA urban challenge: autonomous vehicles in city traffic. 2009
- J Ziegler, P Bender, T Dang, and C Stiller. Trajectory planning for bertha—a local, continuous method. IV'14
- P Bender, O Tas, J Ziegler, and C Stiller. The combinatorial aspect of motion planning: Maneuver variants in structured environments. IV'15
- Framework:
	- E2E: learn the states, and plan/loss from learned states;
		- NMP: Uber-ATG. End-to-end Interpretable Neural Motion Planner. CVPR'19
			- Detection + prediction + plan-cost-volume;
			- Backbone: IntentNet + Pixor
		- DSDNet: Uber-ATG. DSDNet: Deep Structured self-Driving Network. arxiv'20
	- Direct state:
		- PLT-Planner: Uber-ATG. Jointly Learnable Behavior and Trajectory Planning for Self-Driving Vehicles. IROS'19
			- Hardcoded feature: collision, ...
			- Only learn linear weight to combine them;
- Supervision:
	- NMP [CVPR'19]: max-margin loss (sampling);
- Uber-ATG: Neural-Planner

## Prediction + Planning Together
- Waymo. ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst. 2018
	- Inputs (mid-level): map + past/future agent poses;
	- Output: driving trajectory (consumed by controler)
	- Backbone: 
		- Agent-RNN: other agents prediction;
		- RNN: Self;
	- System Design: inference time rollout for planning;
	- Imitation Learning: direct: hard; reward shaping;
	- Loss design:
		- Agent position, heading and box prediction;
		- Meta prediction: speed, subpixel
	- Loss: Beyond pure imitation;
		- avoid drift, bad behavior (collisions and off-road driving)
		- Loss design: collision loss; on-road loss; geometry loss (always follows geometry independent of speed)

## Search/Inference Given Cost
- Insight: search a path with low cost;
- A. Route planning: Dijkstra, A∗;
- B. Behavior decision making;
- C. Motion planning; (exact solution intractable)
- D. Control;
- Variational methods; (optimization-based)
- Graph-search; (discretization required)
- A-star search: Z Ajanovic, B Lacevic, B Shyrokau, M Stolz, and M Horn. Search-based optimal motion planning for automated driving. IROS'18	
- Continuous:
	- **LQG-Robust**: S Dean, N Matni, B Recht, and V Ye. Robust Guarantees for Perception-Based Control. 2019
		- https://github.com/modestyachts/robust-control-from-vision
		- Affine error-profile model;
		- Model: MBRL (LQR)
		- Evaluated on synthetic example CARLA

## Behavior Cloning
- Insight: just supervised learning;
- PilotNet: NVIDIA. End to End Learning for Self-Driving Cars. 2016
	- Imitation learning from human data; trained just for bc; drift (1m from center) reset in simulator;
	- Good for path following for a few seconds; not able to make turns;
- NVIDIA. Explaining how a deep neural network trained with end-to-end learning steers a car. 2017
	- Visualize salient object for pilotnet
- H Xu, Y Gao, F Yu, and T Darrell. End-to-end learning of driving models from large-scale video datasets. CVPR'17
	- Input: camera
	- Output: action
	- Dataset: Berkeley DeepDrive Video dataset (BDDV)
- Intel. End-to-end driving via conditional imitation learning. ICRA'18
	- Intention/goal-based (straight/turn)
	- https://github.com/carla-simulator/imitation-learning
- Intel. Driving policy transfer via modularity and abstraction. CoRL'18
	- Output: high-level control
- Waymo. Urban Driving with Conditional Imitation Learning. 2019
	- Input three images x 2 frames; no LiDAR;

## Misc
- Behavior planning:
	- T Gu, J Dolan, and J Lee. On-road trajectory planning for general autonomous driving with enhanced tunability. Intelligent Autonomous Systems'16
		- Multi-phase decision making: long range traffic-free first;
		- Traffic-based refinement, other actors taken into account;
		- Last local trajectory planning, short term;
	- Baidu: Baidu apollo em motion planner. 2018
		- Dynamic programming for approximate path and speed profile in EM scheme;
		- Quadratic programming of cost function;
		- Manually designed cost for lane boundaries, collision, traffic lights, and other driving conditions;
- Trajectory planning:
	- J Ziegler and C Stiller. Spatiotemporal state lattices for fast trajectory planning in dynamic on-road driving scenarios. IROS'09
	- M Pivtoraiko, R Knepper, and A Kelly. Differentially constrained mobile robot motion planning in state lattices. 2009
	- M Werling, J Ziegler, S Kammel, and S Thrun. Optimal trajectory generation for dynamic street scenarios in a frenet frame. ICRA'10
		- Parallel sampling:

## Imitation Learning
- N Ratliff, A Bagnell, and M Zinkevich. Maximum margin planning. ICML'06
- Predicting the Way by Learning to Sample and Learning the Cost: Urban Self-Driving without HD Maps. Mini-27
	- No HD-Maps
	- With HD-Maps as supervision;	
- K Refaat, K Ding, N Ponomareva and S Ross. Agent Prioritization for Autonomous Navigation. 2019
	- Input: ROI 80 x 80 centered on AV;
	- **Data Generation**: automatic; simulation on real-world logged data;
	- **Data representation**:
	- **Hybrid approach**: CNN + GBDT
	- Ranking CNN;
	- Rank loss: log(1+exp(sj-si)) to rank agent j and i;
	- Ranking model:
		- 1. GBDT: with Engineered or CNN features;
		- 2. Pairwise loss function from CNN;
	- Evalution: Normalized Discounted Cumulative Gain (NDCG);
	- Best performer: **Pairwise CNN + Pairwise GBDT**;
- Berkeley:
	- J Chen, B Yuan and M Tomizuka. Deep Imitation Learning for Autonomous Driving in Generic Urban Scenarios with Enhanced Safety. 2019
		- https://docs.google.com/presentation/d/1xU-ue8R2XlppgBM0qIpsPjoqI5zfZ23OUoRonJhX20w/edit#slide=id.g653e76e7ff_0_3
		- Input: HD map; Routing information; Traffic light state; Historical detections; Historical ego-car state;
		- Output: waypoints; control;
		- Model architecture;
		- Experiments: CarLA;
- C Chen, A Seff, A Kornhauser, and J Xiao. DeepDriving: Learning Affordance for Direct Perception in Autonomous Driving. ICCV'15
- A Sauer, N Savinov, and A Geiger. Conditional affordance learning for driving in urban environments. arxiv'18

## RL
- X Pan, Y You, Z Wang, and C Lu. Virtual to real reinforcement learning for autonomous driving. 2017
	- Transfer from simulator to real
	- Simulator: TORCS
	- **Image translation** for transfer!
	- Sim: Virtual-im -> [sem] -> trans -> [fake-real-im]
	- Policy: fake-real-im -> [conv] -> π
- C Paxton, V Raman, G D Hager, and M Kobilarov. Combining neural networks and tree search for task and motion planning in challenging environments. IROS'17
- A Kendall, J Hawke, D Janz, P Mazur, D Reda, J Allen, V Lam, A Bewley, and A Shah. Learning to drive in a day. 2018
	- Task: lane following
	- MDP, input: monocular camera; VAE;
	- State: Conv(im)
	- Action space: throttle, brake, signal, ...
	- Reward: speed, infraction of traffic rules
	- Algorithm: DDPG
- Uber-ATG. Multi-Agent Value Iteration Network for Scalable Route Planning. Mini-38
	- Input: map graph
	- Task: Coordinated traversal of the graph
	- Graph-VIN
	- Communication;
	- Experiment: Sumo

## IRL
- D Gonzalez, J Dibangoye, and C Laugier, High-speed highway scene prediction based on driver models learned from demonstrations. ITSC'16
- D Sadigh, S Sastry, S Seshia, and A Dragan, Planning for autonomous cars that leverages effects on human actions. 2016

## Planning under Uncertainty
- T Bandyopadhyay, K S Won, E Frazzoli, D Hsu, W S Lee, and D Rus. Intention-aware motion planning. Algorithmic foundations of robotics X'13
- J Hardy and M Campbell. Contingency planning over probabilistic obstacle predictions for autonomous road vehicles. 2013
- W Zhan, C Liu, C Chan, and M Tomizuka. A non-conservatively defensive strategy for urban autonomous driving. ITSC'16