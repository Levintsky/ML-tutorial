# Planning

## Dataset for Imitation Learning
- J. Colyar and J. Halkias, US highway 80 dataset, Federal Highway Administration (FHWA), 2006
- J. Colyar and J. Halkias, US highway 101 dataset, Federal Highway Administration (FHWA), 2007

## Neural Planning
- Dean A Pomerleau. Alvinn: An autonomous land vehicle in a neural network. NIPS'89
- W Zeng, W Luo, S Suo, A Sadat, B Yang, S Casas, R Urtasun. End-to-end Interpretable Neural Motion Planner. CVPR'19
	- Input: raw LiDAR, HD map; H x W x (ZT' + M)
		- LiDAR: past 10 frames; compensate ego-motion; (follow **IntentNet**) H x W x ZT'
		- HD map: H x W x M (M channels: road, intersection, lanes, ...)
	- Output: 3D detections and their future trajectories;
	- Output: space-time cost volume that represents the goodness
	- Network:
		- Backbone: {2, 2, 3, 6, 5} Conv2D layers with filter number {32, 64, 128. 256, 256}, filter size 3x3 and stride 1. (follow **Pixor**)
		- Perception Head: follow SSD, 12 anchors each location;
		- Cost Volume Head: same resolution as BEV,
		- Efficient Inference: NP-hard, sampling;
	- Learning:
		- Perception loss: bounding box, regression,
		- planning loss: max-margin loss (ground truth v.s. randomly sampled negative)
	- Output Parameterization: Clothoid curve; sampling;
	<img src="/Autonomous-Driving/images/e2e-planner.png" alt="drawing" width="600"/>

- NVIDIA:
	- **PilotNet**: M Bojarski, D Del Testa, D Dworakowski, B Firner, B Flepp, P Goyal, L D. Jackel, M Monfort, U Muller, J Zhang, X Zhang, J Zhao, K Zieba. End to End Learning for Self-Driving Cars. 2016
		- Imitation learning from human data; trained just for bc; drift (1m from center) reset in simulator;
		- Good for path following for a few seconds; not able to make turns;
		<img src="/Autonomous-Driving/images/e2e-ad1.png" alt="drawing" width="500"/>
		<img src="/Autonomous-Driving/images/e2e-ad2.png" alt="drawing" width="500"/>

	- M Bojarski, P Yeres, A Choromanska, K Choromanski, B Firner, L Jackel, and U Muller. Explaining how a deep neural network trained with end-to-end learning steers a car. 2017
		- Visualize salient object for pilotnet
		<img src="/Autonomous-Driving/images/e2e-ad3.png" alt="drawing" width="500"/>

- **ChauffeurNet**: M Bansal, A Krizhevsky, A Ogale. ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst. 2018
	- Inputs (mid-level): W x H roadmap, traffic lights, speed limit, route (google map style), current agent box, dynamic boxes, past agent poses, future agent poses
	<img src="/Autonomous-Driving/images/chauffeurnet1.png" alt="drawing" width="600"/>

	- Net: RNN for planning; p(t+dt) = ChauffeurNet(I, p(t)), p: points on trajectory; and 1-step of RNN: pk,Bk = AgentRNN(k,F,Mk−1,Bk−1)
	<img src="/Autonomous-Driving/images/chauffeurnet2.png" alt="drawing" width="600"/>
	<img src="/Autonomous-Driving/images/chauffeurnet3.png" alt="drawing" width="600"/>

	- System Design
	<img src="/Autonomous-Driving/images/chauffeurnet4.png" alt="drawing" width="600"/>

	- Output: driving trajectory (consumed by controler)
	- **Imitation Learning**: direct: hard; reward shaping;
	- Loss design:
		- Agent position, heading and box prediction;
		- Meta prediction: speed, subpixel
		- Collision Loss: overlap of the predicted agent box with all scene objects
		- On road loss
		- Geometry loss
	- Beyond pure imitation: avoid drift, bad behavior (collisions and off-road driving)
		- Loss design: collision loss; on-road loss; geometry loss (always follows geometry independent of speed)
- Berkeley:
	- H Xu, Y Gao, F Yu, and T Darrell. End-to-end learning of driving models from large-scale video datasets. CVPR'17
		- Input: camera
		- Output: action
		- Dataset: Berkeley DeepDrive Video dataset (BDDV)
		<img src="/Autonomous-Driving/images/fcn-lstm.png" alt="drawing" width="400"/>

- Intel:
	- **CarLA**: F Codevilla, M Muller, A Lopez, V Koltun, and A Dosovitskiy. End-to-end driving via conditional imitation learning. ICRA'18
		- Same input, different intention (straight/turn) different action
		- Conditioned on internal state
		- Trained on Carla
		- https://github.com/carla-simulator/imitation-learning.
		<img src="/Autonomous-Driving/images/cil1.png" alt="drawing" width="400"/>
		<img src="/Autonomous-Driving/images/cil2.png" alt="drawing" width="600"/>

	- M Muller, A Dosovitskiy, B Ghanem, and V Koltun. Driving policy transfer via modularity and abstraction. CoRL'18
		- Input: semantic segmentation
		- Output: high-level control
		<img src="/Autonomous-Driving/images/cil3.png" alt="drawing" width="500"/>
		<img src="/Autonomous-Driving/images/cil4.png" alt="drawing" width="500"/>
- C Chen, A Seff, A Kornhauser, and J Xiao. DeepDriving: Learning Affordance for Direct Perception in Autonomous Driving. ICCV'15
- A Sauer, N Savinov, and A Geiger. Conditional affordance learning for driving in urban environments. arxiv'18

## RL
- X Pan, Y You, Z Wang, and C Lu. Virtual to real reinforcement learning for autonomous driving. 2017
	- Transfer from simulator to real
	- Simulator: TORCS
	- Image translation
	<img src="/Autonomous-Driving/images/visri1.png" alt="drawing" width="600"/>
	<img src="/Autonomous-Driving/images/visri1.png" alt="drawing" width="600"/>

- A Kendall, J Hawke, D Janz, P Mazur, D Reda, J Allen, V Lam, A Bewley, and A Shah. Learning to drive in a day. 2018

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
	<img src="/Autonomous-Driving/images/gail-ad1.png" alt="drawing" width="400"/>
	<img src="/Autonomous-Driving/images/gail-ad2.png" alt="drawing" width="400"/>
	<img src="/Autonomous-Driving/images/gail-ad3.png" alt="drawing" width="400"/>

	- NGSIM dataset

## Optimization Based Planners (Manual)
- M Buehler, K Iagnemma, and S Singh. The DARPA urban challenge: autonomous vehicles in city traffic. 2009
- H Fan, F Zhu, C Liu, L Zhang, L Zhuang, D Li, W Zhu, J Hu, H Li, and Q Kong. Baidu apollo em motion planner. 2018
- M Montemerlo, J Becker, S Bhat, H Dahlkamp, D Dolgov, S Ettinger, D Haehnel, T Hilden, G Hoffmann, B Huhnke, et al. Junior: The stanford entry in the urban challenge. Journal of field Robotics. 2008
- J Ziegler, P Bender, T Dang, and C Stiller. Trajectory planning for bertha—a local, continuous method. IV'14

## Planning under Uncertainty
- T Bandyopadhyay, K S Won, E Frazzoli, D Hsu, W S Lee, and D Rus. Intention-aware motion planning. Algorithmic foundations of robotics X'13
- J Hardy and M Campbell. Contingency planning over probabilistic obstacle predictions for autonomous road vehicles. 2013
- W Zhan, C Liu, C Chan, and M Tomizuka. A non-conservatively defensive strategy for urban autonomous driving. ITSC'16