# Prediction

## 2D-Vision
- SBNet: Leveraging Activation Block Sparsity for Speeding up Convolutional Neural Networks. Mengye Ren, Andrei Pokrovsky, Bin Yang, and Raquel Urtasun

## Map-Automation
- G Mattyus, W Luo and R Urtasun. DeepRoadMapper: Extracting Road Topology From Aerial Images. ICCV'17
- J. Liang, R. Urtasun. End-to-End Deep Structured Models for Drawing Crosswalks. ECCV'18

## 3D-Detection
- HDNET: Exploiting HD Maps for 3D Object Detection. B. Yang, M. Liang, R. Urtasun. CoRL'18

## Tracking
- D. Frossard, R. Urtasun. End-to-end Learning of Multi-sensor 3D Tracking by Detection. ICRA'18

## Lane Detection
- M. Bai, G. Mattyus, N. Homayounfar, S. Wang, S. K. Lakshmikanth, R. Urtasun. Deep Multi-Sensor Lane Detection. IROS'18
- J Liang, N Homayounfar, WC Ma, S Wang, R Urtasun. Convolutional Recurrent Network for Road Boundary Extraction. CVPR'19

## Uber
- **FaF**: W. Luo, B. Yang, and R. Urtasun. Fast and furious: Real time end-to-end 3d detection, tracking and motion forecasting with a single convolutional net. CVPR'18
	- 1. 3D detection; 2. tracking; 3. motion forecasting;
	- predict next 1 sec; no intent;
	<img src="/Autonomous-Driving/images/faf.png" alt="drawing" width="500"/>

- **IntentNet**: S Casas, W Luo, R Urtasun. IntentNet: Learning to Predict Intention from Raw Sensor Data. CoRL'18
	- Input: 1. 3D point cloud; (BEV) stack time on height; 2. dynamic maps;
	- Output: 1. trajectory regression; (a sequence of bounding boxes); 2. high level actions (keep lane, turn left/right, left/right lane change, stopping, stopped, parked)
	- Output head: 1. detection branch; (anchors) 2. intention branch; 3. intention as an embedding for motion estimation/regression;
	- **Two-stream + Late fusion**;
	- Predicts: detection scores for vehicle and background classes, high level action probabilities corresponding to discrete intention, and bounding box regressions in the current and future time steps to represent the intended trajectory;
	<img src="/Autonomous-Driving/images/intentnet.png" alt="drawing" width="600"/>

## Trajectories, Multi-Agent
- **TrafficPredict**: Y. Ma et al., TrafficPredict: Trajectory Prediction for Heterogeneous Traffic-Agents. 2018
- J. Ren et al., Heter-Sim: Interactive data-driven optimization for simulating heterogeneous multi-agent systems. arxiv'18
- Q. Chao, Z. Deng, J. Ren, Q. Ye, X. Jin, Realistic Data-Driven Traffic Flow Animation Using Texture Synthesis. TVCG'18

## Misc
- T. Streubel and K. H. Hoffmann. Prediction of driver intended path at intersections. 2014
- D. J. Phillips, T. A. Wheeler, and M. J. Kochenderfer. Generalizable intention prediction of human drivers at intersections. IV'17
- Y. Hu, W. Zhan, and M. Tomizuka. Probabilistic prediction of vehicle semantic intention and motion. arxiv'18