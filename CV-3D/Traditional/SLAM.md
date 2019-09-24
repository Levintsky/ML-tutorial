# SLAM

## SLAM (Simultaneous Localization And Mapping)
- LiDAR SLAM
	- Step 1. Map initialization
	- Step 2. Pose Tracking: ICP (Iterative closest point), optimize for camera pose;
	- Step 3. Map optimization: occupancy grid map;
	- Iterate 2 and 3.
	<img src="/CV/images/low-level/icp.png" alt="drawing" width="450"/>

- Visual SLAM
	- Step 1. Initialization; (essential matrix, triangulation)
	- Step 2. Pose estimation: (feature tracking, pose-only BA)
	- Visual SLAM by SfM
	- PTAM (Parallel Tracking and Mapping)
		- Real time camera pose tracking
		- An offline thread for map maintenance: when key frame comes, do a BA
- Relocalization
	- Tracking can lose due to various reasons
- Robustness Techniques
	- Drifting

## Direct Methods
- Classical:
	- feat, feat-match, motion-est, dense reconstruction
	- suboptimal, lack robustness
- Direct:
	- No feat abstraction;
	- Steinbrücker, Sturm, Cremers, 2011 and Kerl, Sturm, Cremers, 2013 the camera motion of an RGB-D camera without feature extraction;
	- Newcombe, Lovegrove, Davison, ICCV 2011; dense geometry + motion;
	
## Realtime Dense Geometry
- Stühmer, Gumhold, Cremers, DAGM 2010

## Dense RGB-D Tracking
- Benchmark: Sturm, Engelhard, Endres, Burgard, Cremers, IROS 2012
- Steinbrücker, Sturm, Cremers (2011)
- Direct stereo: Comport, Malis, Rives, ICRA 2007
- Non-quadratic penalizers; Kerl, Sturm, Cremers, ICRA 2013
	- Combines color consistency and geometry consistency

## Loop Closure and Global Consistency

## Dense Tracking and Mapping

## Large Scale Direct Monocular SLAM
- Engel, Sturm, Cremers ICCV 2013 and Engel, Schöps, Cremers ECCV 2014; camera motion + semi-dense geometry;