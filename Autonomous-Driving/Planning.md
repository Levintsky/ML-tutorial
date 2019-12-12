# Planning

## Survey
- B Paden, M Čáp, S Yong, D Yershov, and E Frazzoli. A Survey of Motion Planning and Control Techniques for Self-driving Urban Vehicles. 2016

## Dataset for Imitation Learning
- J. Colyar and J. Halkias, US highway 80 dataset, Federal Highway Administration (FHWA), 2006
- J. Colyar and J. Halkias, US highway 101 dataset, Federal Highway Administration (FHWA), 2007

## Misc
- A-star search:
	- Z Ajanovic, B Lacevic, B Shyrokau, M Stolz, and M Horn. Search-based optimal motion planning for automated driving. IROS'18
- Optimization:
	- P Bender, O Tas, J Ziegler, and C Stiller. The combinatorial aspect of motion planning: Maneuver variants in structured environments. IV'15
	- M Buehler, K Iagnemma, and S Singh. The DARPA urban challenge: autonomous vehicles in city traffic. 2009
	- M Montemerlo, J Becker, S Bhat, H Dahlkamp, D Dolgov, S Ettinger, D Haehnel, T Hilden, G Hoffmann, B Huhnke, et al. Junior: The stanford entry in the urban challenge. Journal of field Robotics. 2008
	- J Ziegler, P Bender, T Dang, and C Stiller. Trajectory planning for bertha—a local, continuous method. IV'14
- Behavior planning:
	- T Gu, J Dolan, and J Lee. On-road trajectory planning for general autonomous driving with enhanced tunability. Intelligent Autonomous Systems'16
		- Multi-phase decision making: long range traffic-free first;
		- Traffic-based refinement, other actors taken into account;
		- Last local trajectory planning, short term;
	- **Baidu**: H Fan, F Zhu, C Liu, L Zhang, L Zhuang, D Li, W Zhu, J Hu, H Li, and Q Kong. Baidu apollo em motion planner. 2018
		- Dynamic programming for approximate path and speed profile in EM scheme;
		- Quadratic programming of cost function;
		- Manually designed cost for lane boundaries, collision, traffic lights, and other driving conditions;
- Trajectory planning:
	- J Ziegler and C Stiller. Spatiotemporal state lattices for fast trajectory planning in dynamic on-road driving scenarios. IROS'09
	- M Pivtoraiko, R Knepper, and A Kelly. Differentially constrained mobile robot motion planning in state lattices. 2009
	- M Werling, J Ziegler, S Kammel, and S Thrun. Optimal trajectory generation for dynamic street scenarios in a frenet frame. ICRA'10
		- Parallel sampling:

## Imitation Learning
- **Alvinn**: Dean A Pomerleau. Alvinn: An autonomous land vehicle in a neural network. NIPS'89
- Nathan D Ratliff, J Andrew Bagnell, and Martin A Zinkevich. Maximum margin planning. ICML'06
- Uber:
	- W Zeng, W Luo, S Suo, A Sadat, B Yang, S Casas, R Urtasun. End-to-end Interpretable Neural Motion Planner. CVPR'19
		- Idea: holistic model, combine detection and planning;
		- Input: raw LiDAR, HD map; H x W x (ZT' + M)
			- LiDAR: past 10 frames; compensate ego-motion; (follow **IntentNet**) H x W x ZT'
			- HD map: H x W x M (M channels: road, intersection, lanes, ...)
		- Output: 3D detections and their future trajectories;
		- Output: space-time cost volume that represents the goodness
		- Network:
			- Backbone: {2, 2, 3, 6, 5} Conv2D layers with filter number {32, 64, 128, 256, 256}, filter size 3x3 and stride 1. (follow **Pixor** detection)
			- Perception Head: follow SSD, 12 anchors each location;
			- Cost Volume Head: same resolution as BEV,
			- Efficient Inference: NP-hard, sampling;
		- Learning:
			- Perception loss: bounding box, regression,
			- Planning loss: max-margin loss (ground truth v.s. randomly sampled negative)
		- Output Parameterization: Clothoid curve; sampling;
		- Sampling: sample a set of diverse physically possible trajectories and choose the one with the minimum learned cost;
		<img src="/Autonomous-Driving/images/plan/e2e-planner.png" alt="drawing" width="600"/>
	- **PLT-Planner**: PLT (Path, Lateral, Time)
		- https://drive.google.com/open?id=1F9Yv2fwNGxuTboE8aSHue_gCaSssXu0I
		- https://docs.google.com/presentation/d/1fRycSFv1boK-9WLR7mxUdNy6V0Ug8ylrDjUs5ww7A80/edit#slide=id.p
		- Improves upon PT solver;
		- Largely a framework: sample rollouts - cost rollouts - pick minimum cost;
		- Rollout generation:
			- Spatial path + velocity profile + steering quantities; exectubale
		- Interactive: (policy + cost); intelligent mode for driver, constant for pedestrains;
			- Actors react to accomodate for av's action (policy): retimed waypoints (only consider them changing velocity)
			- Actions induce burden;
		- Ignore rules: filter out actors following behind AV;
			- Failure in lane changes and merges;
	- A Sadat, M Ren, A Pokrovsky, Y Lin, E Yumer, R Urtasun. Jointly Learnable Behavior and Trajectory Planning for Self-Driving Vehicles. 2019
		- Behavior planning, Trajectory planning;
		- Input: desired route, state of the world (av state, map, detected object);
		- Output: high-level behavior b; trajectory tau;
		- Unified cost function: a weighted combination of manual designed cost:
			- Obstacle: safety-distance, weighted by speed (if AV stopps, ok to be close);
			- Driving-path and lane boundary (should not go out of the lane boundary and should stay close to the center of the lane)
			- Headway: keep a safe longitudinal distance from leading car, depending on speed;
			- Yield: penalizes the squared longitudinal violation distance weighted by the pedestrian prediction probability.
			- Route: penalize the number of lane-changes that is required to converge to the route
			- Cost-to-go: he deceleration needed for slowing-down to possible upcomming speed-limits and use the square of the violation of the comfortable deceleration as cost-to-go.
			- Speed limit, travel distance and dynamics;
		- Inference:
			- Behabioral planner (tau, b): Frenet frame; position s and lateral offset d separately; (not very precise)
			- Trajectory planner (u): BFGS solver;
		- Learning:
			- Max-margin loss: penalizes trajectories that have small cost and are different from the human driving trajectory; learn linear weight with structured SVM;
			- Imitation loss
			- Weight decay (L2 regularizer)
		- Experiments:
			- Datasets: ManualDrive, TOR-4D;
			- Evaluation: similarity to human; passenger comfort (average jerk and lateral acceleration); spatiotemporal overlap;
			- Baselines: Oracle ACC; PT;
	- Predicting the Way by Learning to Sample and Learning the Cost: Urban Self-Driving without HD Maps. Mini-27
		- No HD-Maps
		- With HD-Maps as supervision;
- NVIDIA:
	- **PilotNet**: M Bojarski, D Del Testa, D Dworakowski, B Firner, B Flepp, P Goyal, L D. Jackel, M Monfort, U Muller, J Zhang, X Zhang, J Zhao, K Zieba. End to End Learning for Self-Driving Cars. 2016
		- Imitation learning from human data; trained just for bc; drift (1m from center) reset in simulator;
		- Good for path following for a few seconds; not able to make turns;
		<img src="/Autonomous-Driving/images/plan/e2e-ad1.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/plan/e2e-ad2.png" alt="drawing" width="400"/>
	- M Bojarski, P Yeres, A Choromanska, K Choromanski, B Firner, L Jackel, and U Muller. Explaining how a deep neural network trained with end-to-end learning steers a car. 2017
		- Visualize salient object for pilotnet
		<img src="/Autonomous-Driving/images/plan/e2e-ad3.png" alt="drawing" width="500"/>
- Waymo:
	- **ChauffeurNet**: M Bansal, A Krizhevsky, A Ogale. ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst. 2018
		- Inputs (mid-level): W x H roadmap, traffic lights, speed limit, route (google map style), current agent box, dynamic boxes, past agent poses, future agent poses
		<img src="/Autonomous-Driving/images/plan/chauffeurnet1.png" alt="drawing" width="600"/>

		- Net: RNN for planning; p(t+dt) = ChauffeurNet(I, p(t)), p: points on trajectory; and 1-step of RNN: pk,Bk = AgentRNN(k,F,Mk−1,Bk−1)
		<img src="/Autonomous-Driving/images/plan/chauffeurnet2.png" alt="drawing" width="600"/>
		<img src="/Autonomous-Driving/images/plan/chauffeurnet3.png" alt="drawing" width="600"/>

		- System Design
		<img src="/Autonomous-Driving/images/plan/chauffeurnet4.png" alt="drawing" width="600"/>

		- Output: driving trajectory (consumed by controler)
		- **Imitation Learning**: direct: hard; reward shaping;
		- Loss design:
			- Agent position, heading and box prediction;
			- Meta prediction: speed, subpixel
		- Beyond pure imitation: avoid drift, bad behavior (collisions and off-road driving)
			- Loss design: collision loss; on-road loss; geometry loss (always follows geometry independent of speed)
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
	- H Xu, Y Gao, F Yu, and T Darrell. End-to-end learning of driving models from large-scale video datasets. CVPR'17
		- Input: camera
		- Output: action
		- Dataset: Berkeley DeepDrive Video dataset (BDDV)
		<img src="/Autonomous-Driving/images/fcn-lstm.png" alt="drawing" width="400"/>
	- J Chen, B Yuan and M Tomizuka. Deep Imitation Learning for Autonomous Driving in Generic Urban Scenarios with Enhanced Safety. 2019
		- https://docs.google.com/presentation/d/1xU-ue8R2XlppgBM0qIpsPjoqI5zfZ23OUoRonJhX20w/edit#slide=id.g653e76e7ff_0_3
		- Input: HD map; Routing information; Traffic light state; Historical detections; Historical ego-car state;
		- Output: waypoints; control;
		- Model architecture;
		- Experiments: CarLA;
		<img src="/Autonomous-Driving/images/plan/deep-il.png" alt="drawing" width="500"/>
		<img src="/Autonomous-Driving/images/plan/deep-il-planner.png" alt="drawing" width="500"/>
		<img src="/Autonomous-Driving/images/plan/deep-il-track-control.png" alt="drawing" width="500"/>
		<img src="/Autonomous-Driving/images/plan/deep-il-safety-control.png" alt="drawing" width="500"/>
- Intel:
	- **CarLA**: F Codevilla, M Muller, A Lopez, V Koltun, and A Dosovitskiy. End-to-end driving via conditional imitation learning. ICRA'18
		- Same input, different intention (straight/turn) different action
		- Conditioned on internal state
		- Trained on Carla
		- https://github.com/carla-simulator/imitation-learning.
		<img src="/Autonomous-Driving/images/plan/cil1.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/plan/cil2.png" alt="drawing" width="600"/>
	- Felipe Codevilla, Matthias Miiller, Antonio López, Vladlen Koltun, and Alexey Dosovitskiy. End-to-end driving via conditional imitation learning. ICRA'18
	- M Muller, A Dosovitskiy, B Ghanem, and V Koltun. Driving policy transfer via modularity and abstraction. CoRL'18
		- Input: semantic segmentation
		- Output: high-level control
		<img src="/Autonomous-Driving/images/plan/cil3.png" alt="drawing" width="500"/>
		<img src="/Autonomous-Driving/images/plan/cil4.png" alt="drawing" width="500"/>
- C Chen, A Seff, A Kornhauser, and J Xiao. DeepDriving: Learning Affordance for Direct Perception in Autonomous Driving. ICCV'15
- A Sauer, N Savinov, and A Geiger. Conditional affordance learning for driving in urban environments. arxiv'18
- Jeffrey Hawke, Richard Shen, Corina Gurau, Siddharth Sharma, Daniele Reda, Nikolay Nikolov
Przemysław Mazur, Sean Micklethwaite, Nicolas Griffiths, Amar Shah, Alex Kendall. Urban Driving with Conditional Imitation Learning. 2019
	- Input three images x 2 frames; no LiDAR;\
		<img src="/Autonomous-Driving/images/plan/wayve-cil.png" alt="drawing" width="500"/>

## RL
- X Pan, Y You, Z Wang, and C Lu. Virtual to real reinforcement learning for autonomous driving. 2017
	- Transfer from simulator to real
	- Simulator: TORCS
	- **Image translation** for transfer!
	<img src="/Autonomous-Driving/images/plan/visri1.png" alt="drawing" width="600"/>
	<img src="/Autonomous-Driving/images/plan/visri1.png" alt="drawing" width="600"/>
- C Paxton, V Raman, G D Hager, and M Kobilarov. Combining neural networks and tree search for task and motion planning in challenging environments. IROS'17
- A Kendall, J Hawke, D Janz, P Mazur, D Reda, J Allen, V Lam, A Bewley, and A Shah. Learning to drive in a day. 2018
	- Task: lane following
	- MDP, input: monocular camera; VAE;
	- Action space: throttle, brake, signal, ...
	- Reward: speed, infraction of traffic rules
	- Algorithm: DDPG
	<img src="/Autonomous-Driving/images/rl-in-a-day.png" alt="drawing" width="450"/>
- Q Sykora, M Ren, S Manivasagam, A Sadat, G Mattyus, R Urtasun. Multi-Agent Value Iteration Network for Scalable Route Planning. Mini-38
	- Input: map graph
	- Task: Coordinated traversal of the graph
	- Graph-VIN
	- Communication;
	- Experiment: Sumo

## IRL
- D. S. Gonzalez, J. Dibangoye, and C. Laugier, High-speed highway scene prediction based on driver models learned from demonstrations. ITSC'16
- D. Sadigh, S. Sastry, S. A. Seshia, and A. D. Dragan, Planning for autonomous cars that leverages effects on human actions. 2016
- N Rhinehart, K M Kitani, and P Vernaza. R2p2: A reparameterized pushforward policy for diverse, precise generative path forecasting. ECCV'18
- Brian D Ziebart, Andrew L Maas, J Andrew Bagnell, and Anind K Dey. Maximum entropy inverse reinforcement learning. AAAI'08
- Markus Wulfmeier, Peter Ondruska, and Ingmar Posner. Maximum entropy deep inverse reinforcement learning. 2015
- **GAIL**: A Kuefler, J Morton, T Wheeler, and M Kochenderfer. Imitating driver behavior with generative adversarial networks. IV'17
	- RNN planner: GRU with ELU; (GAIL GRU, GAIL MLP, BC GRU, and BC MLP)
	- Policy optimizer: TRPO;
	- Given (s1, a1), (s2, a2),..., (sT, aT) sampled from real/fake for discriminator D, D as reward
	<img src="/Autonomous-Driving/images/plan/gail-ad1.png" alt="drawing" width="400"/>
	<img src="/Autonomous-Driving/images/plan/gail-ad2.png" alt="drawing" width="400"/>
	<img src="/Autonomous-Driving/images/plan/gail-ad3.png" alt="drawing" width="400"/>

	- NGSIM dataset

## Planning under Uncertainty
- T Bandyopadhyay, K S Won, E Frazzoli, D Hsu, W S Lee, and D Rus. Intention-aware motion planning. Algorithmic foundations of robotics X'13
- J Hardy and M Campbell. Contingency planning over probabilistic obstacle predictions for autonomous road vehicles. 2013
- W Zhan, C Liu, C Chan, and M Tomizuka. A non-conservatively defensive strategy for urban autonomous driving. ITSC'16