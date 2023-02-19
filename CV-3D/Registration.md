# Registration

## Benchmarks
- **FlyingThings3D**: N. Mayer, E. Ilg, P. Husser, P. Fischer, D. Cremers, A. Dosovitskiy, and T. Brox. A large dataset to train convolutional networks for disparity, optical flow, and scene flow estimation. CVPR'16

## Legacy
- ICP (Iterative closest point)

## Scene-Flow
- Problem definition: 3D motion field of points in the scene;
- General assumption:
	- Regularizations for smoothness of motion and structure;
	- Rigidity of the local structure;
- S. Vedula, S. Baker, P. Rander, R. Collins, and T. Kanade. Three-dimensional scene flow. ICCV'99
- Optical flow and disparity map separately:
	- J.-P. Pons, R. Keriven, and O. Faugeras. Multi-view stereo reconstruction and scene flow estimation with a global image-based matching score. IJCV'07
	- F. Huguet and F. Devernay. A variational method for scene flow estimation from stereo sequences. ICCV'07
	- L. Valgaerts, A. Bruhn, H. Zimmer, J. Weickert, C. Stoll, and C. Theobalt. Joint estimation of motion, structure and geometry from stereo sequences. ECCV'10
	- A. Wedel, C. Rabe, T. Vaudrey, T. Brox, U. Franke, and D. Cremers. Efficient dense scene flow from sparse or dense stereo data. ECCV'08
	- A. Wedel, T. Brox, T. Vaudrey, C. Rabe, U. Franke, and D. Cremers. Stereoscopic scene flow computation for 3d motion understanding. IJCV'11
	- J. Cech, J. Sanchez-Riera, and R. Horaud. Scene flow estimation by growing correspondence seeds. CVPR'11
	- C. Vogel, K. Schindler, and S. Roth. 3d scene flow estimation with a rigid motion prior. ICCV'11
	- C. Vogel, K. Schindler, and S. Roth. Piecewise rigid scene flow. ICCV'13
	- T. Basha, Y. Moses, and N. Kiryati. Multi-view scene flow estimation: A view centered variational approach. IJCV'13
	- C. Vogel, K. Schindler, and S. Roth. 3d scene flow estimation with a piecewise rigid scene model. IJCV'15
	- M. Menze and A. Geiger. Object scene flow for autonomous vehicles. CVPR'15
- 3D point clouds:
	- A. Dewan, T. Caselitz, G. D. Tipaldi, and W. Burgard. Rigid scene flow for 3d lidar scans. In IROS'16
		- Energy minimization with hand-crafted SHOT descriptors
	-  A. K. Ushani, R. W. Wolcott, J. M. Walls, and R. M. Eustice. A learning approach for real-time temporal scene flow estimation from lidar data. ICRA'17
	- A. Behl, D. Paschalidou, S. Donne, and A. Geiger. Pointflownet: Learning representations for 3d scene flow estimation from point clouds. 2018
	- L. Shao, P. Shah, V. Dwaracherla, and J. Bohg. Motion-based object segmentation based on dense rgb-d scene flow. 2018
	- **FlowNet3D**: X Liu, C Qi, L Guibas. FlowNet3D: Learning Scene Flow in 3D Point Clouds. CVPR'19
		- Insight: PointNet++ for feature, embedding + matching, upconv for refinement;
		- https://github.com/xingyul/flownet3d
		<img src="/CV-3D/images/registration/flownet3d.png" alt="drawing" width="600"/>

## Learning-Based
- https://github.com/shubhamag/non_rigid_icp
- S Ge, G Fan and M Ding. Non-rigid Point Set Registration with Global-Local Topology Preservation. CVPRW'14
- Q Chen, V Koltun. Robust Nonrigid Registration by Convex Optimization. ICCV'15
- J Ma, J Zhao, J Jiang, H Zhou. Non-Rigid Point Set Registration with Robust Transformation Estimation under Manifold Regularization. AAAI'17

## DL-Based
- Non-trainable:
	- J Roufosse, A Sharma, M Ovsjanikov. Unsupervised Deep Learning for Structured Shape Matching. 2018 
	- O Litany, T Remez, E Rodolà, A Bronstein, M Bronstein. Deep Functional Maps: Structured Prediction for Dense Shape Correspondence. ICCV'17
- Semantic-aware:
	- Semantic Iterative Closest Point through Expectation-Maximization. BMVC'18
		- Assumes both source and target PC have semantic labels
		- Doesn't use NN features
	- F Lawin, M Danelljan, F Khan, P Forssen, M Felsberg. Density Adaptive Point Set Registration. CVPR'18
	- 3D Local Features for Direct Pairwise Registration. CVPR'19
	- **DCP**: Y Wang, J Solomon. Deep Closest Point: Learning Representations for Point Cloud Registration. 2019
		- https://github.com/WangYueFt/dcp
- T Groueix, M Fisher, V Kim, B Russell, M Aubry. 3D-CODED: 3D Correspondences by Deep Deformation. ECCV'18
- **PointNetLK**: Y Aoki, H Goforth, R Srivatsan, S Lucey. PointNetLK: Robust & Efficient Point Cloud Registration using PointNet. CVPR'19
	- https://github.com/hmgoforth/PointNetLK
- Real-to-Sim Object Texture Transfer. Mini-34
	- Input: images, LiDAR point clouds
	- Output: Texture on games
	- Soft
