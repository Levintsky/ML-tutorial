# Simulator

## Simulation: to generate data looks new
- Lidar Simulation:
	- Mini-conference
	- Baidu AADS;
	- L Caccia, H v Hoof, A Courville, J Pineau. Deep Generative Modeling of LiDAR Data. 2019
- Image simulation
- Radar simulation
- Mesh generation:
	- Real-to-Sim Object Texture Transfer. Mini-34

## Baidu
- **AADS**: W. Li, C. W. Pan, R. Zhang, J. P. Ren, Y. X. Ma, J. Fang, F. L. Yan, Q. C. Geng, X. Y. Huang, H. J. Gong, W. W. Xu, G. P. Wang, D. Manocha, R. G. Yang. AADS: Augmented Autonomous Driving Simulation using Data-driven Algorithms. Science'19
	- Input: RGB images, point cloud, semantic labels, trajectories
	- **AADS-RGB**: Background image Synthesis, MVS (multi-view stereo), 4-refereces-images (input) -> depth map (output); [22,23] content-aware warping;
		- Background: Median filter; guided filter; Poisson editting for completion;
		- Moving objects: randomly initialize object in lanes with direction consistent;
	- **AADS-PC**: simulate the Velodyne outputs with ApolloScape-PC;
	- **Trajectories Synthesis**:
	<img src="/Autonomous-Driving/images/simulator/aads1.png" alt="drawing" width="600"/>
	<img src="/Autonomous-Driving/images/simulator/aads2.png" alt="drawing" width="600"/>

## Intel
- S. R. Richter, V. Vineet, S. Roth, V. Koltun, Playing for data: Ground truth from computer games. ECCV'16
- **CARLA**: A. Dosovitskiy, G. Ros, F. Codevilla, A. Lopez, V. Koltun, CARLA: An Open Urban Driving Simulator. CoRL'17
	- VR

## Microsoft
- **AirSim**: S. Shah, D. Dey, C. Lovett, A. Kapoor, AirSim: High-fidelity visual and physical simulation for autonomous vehicles. Field and Service Robotics. 5, 621–635 (2018).

## NVIDIA
- Drive Constellation: NVIDIA drive constellation: virtual reality autonomous vehicle simulator. 2017

## Waymo
- CarCraft: A. C. Madrigal, Inside Waymo’s Secret World for Training Self-Driving Cars. the Altantis 2017

## Others
-  M. Johnson-Roberson et al., Driving in the matrix: Can virtual worlds replace human-generated annotations for real world tasks? 2016
- H. A. Alhaija, S. K. Mustikovela, L. Mescheder, A. Geiger, C. Rother, Augmented reality meets computer vision: Efficient data generation for urban driving scenes. IJCV'18
