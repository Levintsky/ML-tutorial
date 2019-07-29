# Planning

## Neural Planning
- W Zeng, W Luo, S Suo, A Sadat, B Yang, S Casas, R Urtasun. End-to-end Interpretable Neural Motion Planner. CVPR'19
	- Input: raw Lidar, HD map;

## Imitation Learning
- Dean A Pomerleau. Alvinn: An autonomous land vehicle in a neural network. NIPS'89
- NVIDIA:
	- **PilotNet**: M Bojarski, D Del Testa, D Dworakowski, B Firner, B Flepp, P Goyal, L D. Jackel, M Monfort, U Muller, J Zhang, X Zhang, J Zhao, K Zieba. End to End Learning for Self-Driving Cars. 2016
		- Imitation learning from human data; trained just for bc; drift (1m from center) reset in simulator;
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
	- X Pan, Y You, Z Wang, and C Lu. Virtual to real reinforcement learning for autonomous driving. 17
- Intel:
	- **CarLA**: F Codevilla, M Muller, A Lopez, V Koltun, and A Dosovitskiy. End-to-end driving via conditional imitation learning. ICRA'18
	- M Muller, A Dosovitskiy, B Ghanem, and V Koltun. Driving policy transfer via modularity and abstraction.
		- Input: semantic segmentation
		- Output: high-level control
- **GAIL**: A Kuefler, J Morton, T Wheeler, and M Kochenderfer. Imitating driver behavior with generative adversarial networks. IV'17

## RL
- X Pan, Y You, Z Wang, and C Lu. Virtual to real reinforcement learning for autonomous driving. 2017
- A Kendall, J Hawke, D Janz, P Mazur, D Reda, J Allen, V Lam, A Bewley, and A Shah. Learning to drive in a day. 2018

## IRL
- Nicholas Rhinehart, Kris M Kitani, and Paul Vernaza. R2p2: A reparameterized pushforward policy for diverse, precise generative path forecasting. ECCV'18
	- Brian D Ziebart, Andrew L Maas, J Andrew Bagnell, and Anind K Dey. Maximum entropy inverse reinforcement learning. AAAI'08
	- Markus Wulfmeier, Peter Ondruska, and Ingmar Posner. Maximum entropy deep inverse reinforcement learning. 2015