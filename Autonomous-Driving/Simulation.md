# Simulation and Simulator

## Simulation: to generate data looks new
- Lidar Simulation:
	- Mini-conference
	- Baidu AADS;
	- L Caccia, H v Hoof, A Courville, J Pineau. Deep Generative Modeling of LiDAR Data. 2019
- Image simulation
- Radar simulation
- Mesh generation:
	- Real-to-Sim Object Texture Transfer. Mini-34

## General Data Generation
- **Virtual-Kitti**: A. Gaidon, Q. Wang, Y. Cabon, and E. Vig. Virtual worlds as proxy for multi-object tracking analysis. CVPR'16
- M. Johnson-Roberson et al., Driving in the matrix: Can virtual worlds replace human-generated annotations for real world tasks? 2016
- H. A. Alhaija, S. K. Mustikovela, L. Mescheder, A. Geiger, C. Rother, Augmented reality meets computer vision: Efficient data generation for urban driving scenes. IJCV'18
- **Meta-Sim**: A Kar, A Prakash, M Liu, E Cameracci, J Yuan, M Rusiniak, D Acuna, A Torralba, S Fidler. Meta-Sim: Learning to Generate Synthetic Datasets. ICCV'19
	- https://nv-tlabs.github.io/meta-sim/
	- Input: read data XR, task T
	- Output: synthesize DT=(XT, YT)
	- Notation: P, grammar; s\~P, scene graph; R(s)=(x,y), renderer to generate image and ground truth; G, distribution transformer, modify attributes of nodes;
	- 1. Pretrain autoencoder; G(s)=s, s is attribute set;
	- 2. MMD for distribution matching; InceptionV3, kernel trick [2,29,41]
	- 3. Backprop from Renderer R [20,28];
	- Supervision: MMD cost; TaskNet for validation performance, trained by REINFORCE;

## Domain-Adaptation
- J. Tobin, R. Fong, A. Ray, J. Schneider, W. Zaremba, and P. Abbeel. Domain randomization for transferring deep neural networks from simulation to the real world. IROS'17
- Y.-H. Tsai, W.-C. Hung, S. Schulter, K. Sohn, M.-H. Yang, and M. Chandraker. Learning to adapt structured output space for semantic segmentation. CVPR'18
- G. French, M. Mackiewicz, and M. Fisher. Self-ensembling for visual domain adaptation. ICLR'18.
- J. Hoffman, E. Tzeng, T. Park, J.-Y. Zhu, P. Isola, A Efros, and T. Darrell. Cycada: Cycle-consistent adversarial
domain adaptation. ICML'18.
- P. Li, X. Liang, D. Jia, and E. P. Xing. Semantic-aware grad-gan for virtual-to-real urban scene adaption. BMVC'18
- A. Prakash, S. Boochoon, M. Brophy, D. Acuna, E. Cameracci, G. State, O. Shapira, and S. Birchfield. Structured domain randomization: Bridging the reality gap by context-aware synthetic data. 2018
- Y. Zou, Z. Yu, B. V. K. V. Kumar, and J. Wang. Domain adaptation for semantic segmentation via class-balanced self- training. ECCV'18 

## Car Simulators
- Baidu:
	- **AADS**: W. Li, C. W. Pan, R. Zhang, J. P. Ren, Y. X. Ma, J. Fang, F. L. Yan, Q. C. Geng, X. Y. Huang, H. J. Gong, W. W. Xu, G. P. Wang, D. Manocha, R. G. Yang. AADS: Augmented Autonomous Driving Simulation using Data-driven Algorithms. Science'19
		- Input: RGB images, point cloud, semantic labels, trajectories
		- **AADS-RGB**: Background image Synthesis, MVS (multi-view stereo), 4-refereces-images (input) -> depth map (output); [22,23] content-aware warping;
			- Background: Median filter; guided filter; Poisson editting for completion;
			- Moving objects: randomly initialize object in lanes with direction consistent;
		- **AADS-PC**: simulate the Velodyne outputs with ApolloScape-PC;
		- **Trajectories Synthesis**:
		<img src="/Autonomous-Driving/images/simulator/aads1.png" alt="drawing" width="600"/>
		<img src="/Autonomous-Driving/images/simulator/aads2.png" alt="drawing" width="600"/>
- Intel:
	- S. R. Richter, V. Vineet, S. Roth, V. Koltun, Playing for data: Ground truth from computer games. ECCV'16
	- **CARLA**: A. Dosovitskiy, G. Ros, F. Codevilla, A. Lopez, V. Koltun, CARLA: An Open Urban Driving Simulator. CoRL'17
		- VR
- Microsoft
	- **AirSim**: S. Shah, D. Dey, C. Lovett, A. Kapoor, AirSim: High-fidelity visual and physical simulation for autonomous vehicles. Field and Service Robotics. 5, 621–635 (2018).
- NVIDIA:
	- Drive Constellation: NVIDIA drive constellation: virtual reality autonomous vehicle simulator. 2017
- Waymo:
	- CarCraft: A. C. Madrigal, Inside Waymo’s Secret World for Training Self-Driving Cars. the Altantis 2017
