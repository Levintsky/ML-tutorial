# Simulation and Simulator

## Basics
- Problem setup:
	- Edit background;
	- Add/remove object;
	- Trajectory synthesis;
- Downstream tasks:
	- detection/seg/tracking;
- Domain: as real as possible;
	- Image: AADS
	- Lidar: AADS;
	- Video: 
	- Trajectory: AADS;
- Physical-Based: ray-tracing + rendering;
	- Traditional geometry;
	- Baidu: AADS
	- Uber-ATG: Lidar-Sim;
	- Uber-ATG: add-obj [F Rong, S Wang], traditional + warping/synth;
	- Uber-ATG: remove-obj [Ricson];
- Generative Modeling;
	- Conditional generative modeling;
	- GAN: Surfel-GAN;
	- VAE:
	- Image/Video-translation: pix2pix, vid2vid, CRN, SPADE;

## Lidar Simulation
- Baidu. AADS: Augmented Autonomous Driving Simulation using Data-driven Algorithms. Science'19
	- Insight: real background + 3D assets
	- Input: 2D + PC + Sem + traj;
	- AADS-RGB: BG image Synthesis:
		- MVS -> depth map (output); [22,23] warping;
		- BG filter: Median/guided/Poisson editting for completion;
		- Moving objects: randomly initialize object in lanes with direction consistent;
	- AADS-PC: simulate the Velodyne outputs with ApolloScape-PC;
	- Trajectories Synthesis:
- Off-Road Lidar Simulation with Data-Driven Terrain Primitives. ICRA'18
- L Caccia, H v Hoof, A Courville, J Pineau. Deep Generative Modeling of LiDAR Data. 2019
	- Unravel into 2D; GAN/VAE/...
	- https://github.com/pclucas14/lidar_generation
- Uber. LidarSim: Realistic LiDAR Simulation by leveraging the Real-World. CVPR'20
	- 1. Background surfel (dynamic removed);
	- 2. Dynamic 3D asset;
	- 3. Simulated Lidar rendering;
	- 4. ML/Neural-Net to learn to drop;

## Image simulation:
- Translation in Urban Scenes:
	- pix2pixHD: NVIDIA. High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs. CVPR'17
	- CRN: Q Chen, V Koltun. Photographic Image Synthesis with Cascaded Refinement Networks. ICCV'17
	- vid2vid: NVIDIA. Video-to-Video Synthesis. NeurIPS'18
	- SPADE: T Park, M Liu, T Wang, J Zhu. Semantic Image Synthesis with Spatially-Adaptive Normalization. CVPR'19
		- Key: different scale and bias for different semantic layer!
		- https://github.com/NVLabs/SPADE
- Domain Adaptation:
	- **UNIT**: M Liu, T Breuel, J Kautz. Unsupervised Image-to-Image Translation Networks. NIPS'17
	- **CyCADA**: J Hoffman, E Tzeng, T Park, J Zhu, P Isola, K Saenko, A Efros, T Darrell. CyCADA: Cycle-Consistent Adversarial Domain Adaptation. ICML'18
- ATG: Camera-Sim [F Rong, 20]
- Removing objects: Ricson. Learning Dynamic Object removal in the wild via geometry-aware multi-model representation. arxiv'20
- Adding objects: F Rong, S Wang. GeoSim: Photorealistic Image Simulation by Geometry-Aware Composition for Self-Driving. arxiv'20
	- Model:
	- Separate static and dynamic modeling;
	- Input: 2Dxn + BEV + Sem + Ins-seg + LiDAR;
	- Object bank: precise geometry; from RGB images with semantic and instance segmentation;
	- 1. Placement Sampling;
	- 2. Segment Retrieval;
	- 3. Novel View Warping;
	- 4. Final image synthesis;
	- Geometry refinement: optimize Nx3 mesh with energy with silhoutte, lidar and symmetry;
- GAN:
	- Waymo. SurfelGAN: Synthesizing Realistic Sensor Data for Autonomous Driving. CVPR'20
		- Problem setup: input surfel; output image;
		- Model: Cycle-GAN with supervised pair and unpaired data;
		- Loss: paired supervision + Generative + discriminative:
- Radar simulation:
	- Charlie Hou. Pix2Pix, GAN, ...
- Mesh generation?
- Lane graph: Ricson, Xinchen;
- Traffic generation: Simon, Shenlong;
- Pedestrian-Sim: Alyssa;
- 3D-3D Style Transfer [Kibok];
- 3D Reconstruction (objects): Weakly supervised shape completion [Jiayuan, Mini-Conf] Full shape from partial observation;

## General Data Generation
- M. Johnson-Roberson et al., Driving in the matrix: Can virtual worlds replace human-generated annotations for real world tasks? 2016
- H Alhaija, S Mustikovela, L. Mescheder, A. Geiger, C. Rother. Augmented reality meets computer vision: Efficient data generation for urban driving scenes. IJCV'18
- NVIDIA. Meta-Sim: Learning to Generate Synthetic Datasets. ICCV'19
	- https://nv-tlabs.github.io/meta-sim/
	- Input: read data XR, task T
	- Output: synthesize DT=(XT, YT)
	- Notation: P, grammar; s~ P, scene graph; R(s)=(x,y), renderer to generate image and ground truth; G, distribution transformer, modify attributes of nodes;
	- 1. Pretrain autoencoder; G(s)=s, s is attribute set;
	- 2. MMD for distribution matching; InceptionV3, kernel trick [2,29,41]
	- 3. Backprop from Renderer R [20,28];
	- Supervision: MMD cost; TaskNet for validation performance, trained by REINFORCE;

## Domain-Adaptation
- Y.-H. Tsai, W.-C. Hung, S. Schulter, K. Sohn, M.-H. Yang, and M. Chandraker. Learning to adapt structured output space for semantic segmentation. CVPR'18
- G. French, M. Mackiewicz, and M. Fisher. Self-ensembling for visual domain adaptation. ICLR'18.
- P. Li, X. Liang, D. Jia, and E. P. Xing. Semantic-aware grad-gan for virtual-to-real urban scene adaption. BMVC'18
- A. Prakash, S. Boochoon, M. Brophy, D. Acuna, E. Cameracci, G. State, O. Shapira, and S. Birchfield. Structured domain randomization: Bridging the reality gap by context-aware synthetic data. 2018
