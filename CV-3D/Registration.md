# Registration

## Legacy
- ICP

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
- **PointNetLK**: Y Aoki, H Goforth, R Srivatsan, S Lucey. PointNetLK: Robust & Efficient Point Cloud Registration using PointNet
	- https://github.com/hmgoforth/PointNetLK
- Real-to-Sim Object Texture Transfer. Mini-34
	- Input: images, LiDAR point clouds
	- Output: Texture on games
	- Soft
