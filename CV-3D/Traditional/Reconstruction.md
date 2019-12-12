# 3D Reconstruction

## Resources
- https://github.com/openMVG/awesome_3DReconstruction_list

## Problem definition:
- Shape from X:
	- Shape from shading: Photometric stereo: control light sources;
	- Shape from texture: Assume: regular textures;
	- Shape from focus: from blur;
- SLAM:
	- Input: real-time ordered images;
	- Output: 6-DOF camera (localization); 3D-reconstruction (mapping);
- SfM:
	- Input: unordered images; no time constraint;
	- Output: camera pose; sparse 3D points;
- Visual Odometry:
	- Input: images from single/multiple cameras;
	- Output: camera path only (x, y, z, theta1, 2, 3) Euler Angles
	- L​ocal consistency, can be a building block of a V-SLAM;
- MVS:
	- Input: images, known camera poses;
	- Output: dense 3D reconstruction;

## Approaches
- SFM:
	- Build Rome in a Day (UW)
		- Feature extraction;
		- Feature matching, epipolar geometry: {f, h, R, t}
			- Matching efficiency (pairwise costly!): scalable recognition with a vocabulary tree (CVPR’06, David Nister);
			- Erroneous matches: Loop consistency: Christopher Zach CVPR’10: R12 * R23* R31 = I
		- Match graph construction; (camera poses {Pi}, tracks {pk})
		- Graph initialization; Start from a MST based on Vocabulary Tree;
		- Add edges to the match graph;
		- Expand with loop consistency guaranteed;
		- Find loop closures by community detection;
		- Bundle adjustment;
	- Software case study: OpenSfM (in Python)
		- Input: images; output: camera pose (para, position), sparse 3D points;
		- HA-HOG; (rgb2gray, cv2 -> features.extract_features, save at ./features);
		- Mask features? (a few hundreds out of 4000+)
		- Matching image pairs; Pair matching (8 processes)
		- Merge features onto tracks; (create_tracks.py, take matches, create ./tracks.csv)
		- Incremental reconstruction;
		- Triangulation;
		- Ceres solver;
		- Undistort the image;
		- Compute neighbors;
		- Clean/Prune/Merge depthmap;
		- Start a server to visualize;

## MVS:
- Y Furukawa, C Hernández. Multi-View Stereo: A Tutorial. 2015
	- Collect images;
	- Camera parameter for each image;
	- Reconstruct 3D geometry;
	- Bundle adjustment: fuse more info (GPS, IMU, ...) in your cost function;
	- Camera parameter known?
		- Known: 1D search, with epipolar constraint;
		- Unknown: 2D search, optical flow first?
	- Photo consistency: SSD, SAD, NCC, Census, Rank, MI;
	- Space Carving: remove all voxels not photo-consistent;
	- Visual hull?
	- Region growing MVS;
	- Depth-map fusion for MVS;
	- Fast multi-frame stereo scene flow with motion segmentation;
- Google Street View: Capturing the World at Street Level
	- Chevy van: side- and front facing laser scanner; 2 x high-speed video cameras; 8 x camera (Rosette configuration);
- Pose optimization: http://code.google.com/p/gpo/wiki/GPO
- Align the pose to the road network;
- **COLMAP** (SOA): Structure-from-Motion Revisited. CVPR'16
- **COLMAP** (SOA): Pixelwise View Selection for Unstructured Multi-View Stereo. ECCV'16
	- https://colmap.github.io/

## Depth Fusion (a specific technique):
- **KinectFusion**: R Newcombe, S Izadi, O Hilliges, D Molyneaux, D Kim, A Davison, P Kohli, J Shotton, S Hodges, A Fitzgibbon. KinectFusion: Real-Time Dense Surface Mapping and Tracking, ISMAR 2011;
	- Key novelty: 30Hz tracking;
	- https://blog.csdn.net/tanmengwen/article/details/9231297
	- https://docs.opencv.org/master/d8/d1f/classcv_1_1kinfu_1_1KinFu.html (opencv)
	- Real-time volumetric reconstruction; 6DOF pose;
	- Input: 640 x 480 depth maps; output voxels;
	- Steps:
		- 1. Surface measurement (pre-processing): depth map to dense vertex map, normal map;
		- 2. Sensor pose estimation: live sensor tracking with multi-scale ICP;
		- 3. Surface reconstruction update: global scene fusion, produce TSDF (truncated signed distance function);
		- 4. Surface prediction: ray-casting on new TSDF; close the loop between mapping and localisation;
	<img src="/CV-3D/images/reconstruction/kinect-fusion.png" alt="drawing" width="500"/>
- **Voxel-Block-Hashing**: M Nießner, M Zollhofer, S Izadi, M Stamminger. Real-time 3D Reconstruction at Scale using Voxel Hashing. SIGGRAPH'13
	<img src="/CV-3D/images/reconstruction/voxel-hashing1.png" alt="drawing" width="500"/>
	<img src="/CV-3D/images/reconstruction/voxel-hashing2.png" alt="drawing" width="500"/>
- **ElasticFusion**:
	- https://github.com/mp3guy/ElasticFusion
- **SemanticFusion**: SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks. 2016
	- Combine ElasticFusion and CNN;
	- https://github.com/seaun163/semanticfusion
	<img src="/CV-3D/images/reconstruction/semanticfusion.png" alt="drawing" width="500"/>

## Visual Odometry (VO):
- Estimate ego-motion of an agent with only single/multiple camera;
- L​ocal consistency, can be a building block of a V-SLAM;
- Quadrifocal VO: stereo pair at two subsequent time;

- SLAM:
	- SLAM: Orb-slam2, DSO as starting point for 3D reconstruction reading.
	- Filtering-based SLAM: Kalman/particle;
	- SSM (State-Space Method)
	- Key-frame based:
		- Bootstrap: an initial 3D map; (2-view geometry)
		- Normal mode: assume 3D map available, incremental camera motion; track points, PnP (Perspective n Points);
		- Recovery mode: assume 3D map available, but tracking failed; Relocalize camera pose w.r.t. Previously reconstructed map;
		- BA;
	- MonoFusion: real-time 3D reconstruction of small scene;
		- Dense 3D reconstruction by single camera;
		- Sparse feature tracking for 6DoF; (key frame based BA);
		- Dense stereo matching for each two key frames;
		- Depth fusion by SDF-based volumetric integration.
	- **PTAM** (Parallel Tracking and Mapping), Separate thread
		- Mapping thread: stereo-init; wait for key frames; add new map points; optimize map; map maintenance; (slow)
		- Tracking thread: Pre-process frame; project points; measure points; update camera pose; draw graphics (optional, only in fine stage);
	- DTAM (Dense tracking and mapping);
	- Semi-Dense SLAM;
	- LSD-SLAM;
	- S-LSD-SLAM;
	- MobileFusion:
		- Real-time volumetric surface reconstruction and dense 6DoF camera tracking running;
		- RGB camera, scan objects;
		- Point-based 3D models, 3D surface model;
		- Dense 6DoF tracking, key-frame selection, dense per-frame stereo matching;
		- Depth maps fused volumetrically akin to KinectFusion;
	- ORB-SLAM: real-time monocular SLAM;
		- Feature-based real-time mono SLAM;
		- Same feature for tracking/mapping/relocalization/loop-closing;
		- Robust to motion clutter, wide baseline, ...
		- Real-time loop closing based on optimization of pose graph called the Essential Graph;
	- ORB-SLAM2: stereo cameras (RGB-D); three threads
		- Tracking to localize the camera; minimize reprojection error by motion only BA;
		- Local mapping to manage local map and optimize it;
		- Loop closing by pose-graph optimization; launches 4th thread to perform full BA;
	- Application in AR/VR;
		- Project Tango (Google): Visual-inertial odometry; SLAM; RGB-D sensor;
		- Hololens (Microsoft); RGB-D sensor;
		- Magic Leap;
		- Voforia (Qualcomm); monocular SLAM;
		- Apple (Metaio)
		- Oculus;
