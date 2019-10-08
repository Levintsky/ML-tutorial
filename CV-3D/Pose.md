# 3D Pose Estimation

## Tutorials
- S. Savarese and L. Fei-Fei. 3d generic object categorization, localization and pose estimation, ICCV 2017

## Geometry-based
- Keypoint matching:
	- M. Aubry, D. Maturana, A. A. Efros, B. C. Russell, and J. Sivic. Seeing 3d chairs: exemplar part-based 2d-3d alignment using a large dataset of cad models. CVPR'14
	- A. Collet, M. Martinez, and S. S. Srinivasa. The moped framework: Object recognition and pose estimation for manipulation. IJRS'11
	- M.Zhu,K.G.Derpanis,Y.Yang,S.Brahmbhatt,M.Zhang, C. Phillips, M. Lecce, and K. Daniilidis. Single image 3d object detection and pose estimation for grasping. ICRA'14
- Align with ground truth:
	- V. Ferrari, T. Tuytelaars, and L. Van Gool. Simultaneous object recognition and segmentation from single or multiple model views. IJCV'06
	- F. Rothganger, S. Lazebnik, C. Schmid, and J. Ponce. 3d object modeling and recognition using local affine-invariant image descriptors and multi-view spatial constraints. IJCV'06
- ICP:
	- S. Gupta, P. Arbelaez, R. Girshick, and J. Malik. Aligning 3d models to rgb-d images of cluttered scenes. CVPR'15

## Learning-based
- A. Kendall, M. Grimes, and R. Cipolla. PoseNet: A convolutional network for real-time 6-DOF camera relocalization. ICCV'15
- Shubham Tulsiani, Joao Carreira and Jitendra Malik. Pose Induction for Novel Object Categories. ICCV 2015
	- Input: images, output three Euler Angles
	- SCT (Similar Class Transfer): 
		- Train a CNN for each class (shared base layers, output heads)
		- |C| x Na x Nθ, class, euler angle, angle bin
		- For an unknown class c', find most similar class known
	- GC (Generalized Classifier):
		- VGG, Na x Nθ
- A Handa, M Bloesch, V Pătrăucean, S Stent, J McCormac, and A Davison. gvnn: Neural network library for geometric computer vision. ECCVW'16
- C Wang, Buenaposada, M Jose, R Zhu, and S Lucey. Learning depth from monocular videos using direct methods. CVPR'18
	- Make direct method differentiable.
- R Clark, M Bloesch, J Czarnowski, S Leutenegger, and A Davison. Learning to solve nonlinear least squares for monocular stereo. ECCV'18
	- solve nonlinear least squares in two-view SfM using a LSTM-RNN
- Z Lv, F Dellaert, J Rehg, A Geiger. Taking a Deeper Look at the Inverse Compositional Algorithm. 2019