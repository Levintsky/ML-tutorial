# 3D Data as Output (Objects)

## Basics
- Representations:
	- Point clouds;
	- Voxel;
	- Mesh;
	- Oct-tree;
	- Templates: Primitives; Implicit functions;
	- Depth; 2.5D;
	- Important task: fusion; (KinectFusion, ...)
- Supervision and Evaluation:
	- Geometry:
		- **Chamfer distance**: H. G. Barrow, J. M. Tenenbaum, R. C. Bolles, and H. C. Wolf. Parametric Correspondence and Chamfer Matching: Two New Techniques for Image Matching. IJCAI'77
			- Sum of closest point distances
			- Asymmetric
			- For Hausdorff distance, simply a distance transform?
		- EMD;
	- Photometric;
- 3D reconstruction:
	- Direct 3D reconstruction for whole object;
	- Scene: depth map;
	- Infer cues:
		- 2.5-D: - H. G. Barrow and J. M. Tenenbaum, Recovering intrinsic scene characteristics from images, Computer Vision Systems, 1978

## Floor Plan
- A. X. Chang, M. Savva, and C. D. Manning. Learning spatial knowledge for text to 3d scene generation. EMNLP'14
- A. Chang, W. Monroe, M. Savva, C. Potts, and C. D. Manning. Text to 3d scene generation with rich lexical grounding. ACL'15

## Shape Analysis
- Manual templates:
	- V. Ganapathi-Subramanian, O. Diamanti, S. Pirk, C. Tang, M. Nießner, and L. Guibas. Parsing geometry using structure-aware shape templates. 3DV'18
- Igarashi, T., Matsuoka, S., Tanaka, H.: Teddy: a sketching interface for 3d freeform design. SIGGRAPH'99
- N Mitra, M Wand, H Zhang, D Cohen-Or, V Kim, and Q Huang. Structure-aware shape processing. In SIGGRAPH Asia Courses, 2013
	- regularity, structure
- R Hu, M Savva, and O van Kaick. Functionality representations and applications for shape analysis. CGF'18
- R Hu, O v Kaick, Y Zheng, and M Savva. Siggraph asia 2016: course notes directions in shape analysis towards functionality. In SIGGRAPH Asia 2016 Courses, page 8. ACM, 2016
- H Laga, Y Guo, Hedi Tabia, R Fisher, and M Bennamoun. 3D Shape Analysis: Fundamentals, Theory, and Applications. 2018
- K Xu, V Kim, Q Huang, and E Kalogerakis. Data-driven shape analysis and processing. CGF'17
- Deep Structured 3D Estimation. Mini-12
	- Input: stereo image, LiDAR; Output: pose, shape;
	- Supervision:
		- Multi-view geometry;
		- Intuitive physics;
		- Photo consistency;
		- Silhouette;
		- Consistency;
		- Intuitive physics;
		- Symmetry;
	- Metrics: shape; (Chamfer distance) pose;
	- Exp: ShapeNet, Tor4D, Kitti;

## 2.5D, Depth, Skeleton, 3D-Aware 2D Cues...
- Depth:
	- G. Riegler, A. O. Ulusoy, H. Bischof, and A. Geiger. OctNetFusion: Learning depth fusion from data. 3DV'17
	- Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. Enforcing geometric constraints of virtual normal for depth prediction. ICCV'19
- Amir Arsalan Soltani, Haibin Huang, Jiajun Wu, Tejas D. Kulkarni, Joshua B. Tenenbaum. Synthesizing 3D Shapes via Modeling Multi-View Depth Maps and Silhouettes with Deep Generative Networks. CVPR'17
	- https://github.com/Amir-Arsalan/Synthesize3DviaDepthOrSil
- S. Galliani and K. Schindler. Just look at the image: Viewpoint-specific surface normal prediction for improved multi-view reconstruction. CVPR'16
	- Estimate **normal** of depth map; then improve depth map fusion;
- **3D-INN**: J Wu, T Xue, J Lim, Y Tian, J Tenenbaum, A Torralba, and W Freeman. Single Image 3D Interpreter Network, ECCV'16, IJCV'18
	- Key insight: skeleton representation for 3D objects (so keypoints infers 3D);
	- Input: single image; output: 2d keypoints as well as 3d structure;
	- Keypoint detection (CNN) -> keypoint refinement (mini-network like auto-encoder) -> 3D interpreter -> Projection Layer;\
	<img src="/CV-3D/images/3d_output/3d-inn.png" alt="drawing" width="600"/>
- **MarrNet**: J Wu, Y Wang, T Xue, X Sun, W Freeman, and J Tenenbaum. MarrNet: 3D Shape Reconstruction via 2.5D Sketches. NIPS'17
	- Key insight: 3D-cues first (2.5-D: normal, depth, silhouette), then 3D shape
	- http://marrnet.csail.mit.edu/
	- https://github.com/jiajunwu/marrnet
	- Input: image; output: voxel;
	- Network: encoder (ResNet-18) - decoder (input normal image + depth image masked by silhouette);
	- Supervision: (2D-3D Reprojection consistency)
		- Depth map with voxel: L2;
		- Surface normal; (surface orthogonal to normal should be 1)
	<img src="/CV-3D/images/3d_output/marrnet.png" alt="drawing" width="600"/>
- Wilfried Hartmann, Silvano Galliani, Michal Havlena, Luc Van Gool, and Konrad Schindler. Learned multi-patch similarity. ICCV'17
- **DeepMVS**: P Huang, K Matzen, J Kopf, N Ahuja, and J Huang. DeepMVS: Learning Multi-view Stereopsis. CVPR'18
- **ShapeHD**: J. Wu, C. Zhang, X. Zhang, Z. Zhang, W. T. Freeman, and J. B. Tenenbaum. Learning shape priors for single-view 3D completion and reconstruction. ECCV'18
	- Key insigth: improve on MarrNet with naturalness (pretrained discriminator) to solve ambiguity, with Wasserstein-GAN loss;
	- https://github.com/xiumingzhang/GenRe-ShapeHD
	- Input: single view; Output: 3D voxel completion/reconstruction; \
	<img src="/CV-3D/images/3d_output/shapehd.png" alt="drawing" width="600"/>
- Simon Donne and Andreas Geiger. Learning non-volumetric depth fusion using successive reprojections. CVPR'19