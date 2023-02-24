# Localization

## Problem Definition
- Point clouds + HD-map;
- HD-Map: map with lanes, road boundaries, traffic light, ...
- Problem setup:
	- Sensors (input):
		- GNSS (Global Navigation Satellite System)
		- Camera
		- IMU
	- State space (output): 3-dof;
		- Latitude, Longitude, yaw;
- Approaches:
	- GPS/RTK;
	- Geometric Alignment: ICP;
	- Place Recognition;

## Algorithms
- J Levinson, M Montemerlo, and S Thrun. Map-based precision vehicle localization in urban environments. RSS'07
- E Javanmardi, M Javanmardi, Y Gu, and S Kamijo. Autonomous vehicle self-localization based on probabilistic planar surface map and multi-channel LiDAR in urban area. ITSC'18
- GILL: Uber-ATG. Learning to localize using a lidar intensity map. CoRL'18
	- Real-time localization with centimeter level accuracy;
	- Intensity-Map -> [CNN] -> emb1;
	- Lidar-Sweeps -> [CNN] -> emb2;
	- emb1, emb2, gps, ... -> [⊗] -> 3-dof;
- Uber-ATG. Learning to Localize Through Compressed Binary Maps. CVPR'19
	- Motivation: HD-Map too large fro storage; (900G for LA, 168T for USA)
	- Learn to binarize the map features;
	- Run-length encoding on top of Huffman coding;
	- Image compression (DL-based): encoding - quantization - decoding;
- Retrieval-based localization at city scale: new dataset and simple baselines. Mini-1
	- Problem: localize SDV with single image/sweep
	- Image: SFM/SLAM for structure, PoseNets for regression, VLAD/NetVLAD/DenseVLAD/BoW for retrieval
	- LiDAR: HD-Map/ICP for structure, ? for regression, PointNetVLAD/PCAN/LPD-Net for retrieval

## SLAM
- Asynchronous Multi-View SLAM.
	- Extend SLAM to **asynchronous** multiple cameras;
	- Asynchronous BA;
	- New frame tracking;
	- Exp: comparison with orb-slam;

## Unclassified
- Image Localization [Julieta Martinez]
- Ground Intensity LiDAR Localization with Compressed Maps [Xinkai Wei]
- Learning to Map [Xinkai Wei]
