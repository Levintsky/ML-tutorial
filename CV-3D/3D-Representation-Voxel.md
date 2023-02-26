# Voxel

## Basics:
- Input: 3D (AE), image (reconstruction), partial (inpainting), ... encoder to z;
- Then z back to complete shape;
- With camera parameter: unproject/ray tracing in 3D-Conv;
- Supervision:
	- Strong: Direct 3D occupancy;
	- Weak: Indirect 2D rendering consistency, or Inverse Graphics;
- Handle multiple inputs:
	- Carving to satisfy multiple constraint;
	- CNN-RNN (problem: not order-invariant);
	- Fusion network;

## Misc
- A. Dai, C. R. Qi, and M. Nießner. Shape completion using 3D-encoder-predictor CNNs and shape synthesis. CVPR'17
	- https://github.com/angeladai/cnncomplete

## Legacy (Non-DL)
- Voxlet: M Firman, O M Aodha, S Julier, G Brostow. Structured Prediction of Unobserved Voxels From a Single Depth Image. CVPR'16
	- https://github.com/mdfirman/voxlets
	- Input depth image (no-rgbd), output voxel binary occupancy;
	- Model: structured random forest;

## Backbone
- 3D-Deconv:
	- Z Wu, S Song, A Khosla, F Yu, L Zhang, X Tang, and J Xiao. 3d shapenets: A deep representation for volumetric shapes. CVPR'15
- 3D-Conv/Deconv: [Jiajun NeurIPS'16]; [Andrew Brock, NeurIPSW'16]
	- Interactive 3D modeling with a generative adversarial network, 3DV'17		
	- D Stutz and A Geiger. Learning 3D shape completion from laser scan data with weak supervision. CVPR'18
- 3D-Conv + RNN/LSTM + Deconv: 3D-R2N2 [Savarese, ECCV'16]
	- Z Wu, X Wang, D Lin, D Lischinski, D Cohen-Or, and H Huang. SAGNet: Structure-aware generative network for 3d-shape modeling. TOG'19
- Recursive/Oc-tree/Hierarchical/Coarse2Fine/...:
	- OGN: [Maxim Tatarchenko, Alexey Dosovitskiy, and Thomas Brox ICCV'17]
	- HSP: C Hane, S Tulsiani, J Malik. 3DV'17
	- Octnetfusion: [A. Geiger, 3DV'17]
	- Adaptive O-CNN: Xin Tong. [SIGGRAPH Asia'18]
- Other-latent space:
	- GenRe: MIT. Learning to Reconstruct Shapes from Unseen Classes. NeurIPS'18
		- Insight: project to spherical map;
		- https://github.com/xiumingzhang/GenRe-ShapeHD

## Supervision
- Pixel/pointwise binary: 3D-R2N2;
- GAN on whole object: [Jiajun NeurIPS'16];
	- PrGAN: M Gadelha, S Maji and R Wang. 3D Shape Induction from 2D Views of Multiple Objects. 3DV'17
		- Discriminator on projected 2D;
- VAE: [Andrew Brock, NeurIPSW'16]
	- DeepMind. Unsupervised learning of 3d structure from images. NeurIPS'16
		- cVAE: based on images/class;
	- SAGNet [TOG'19]
	- D. Stutz and A. Geiger. Learning 3D shape completion from laser scan data with weak supervision. CVPR'18
		- Phase 1: VAE y -> y'
		- Phase 2: keep the decoder, train an encoder to map partial data to the same latent space;
- AE:
	- R Girdhar, D F Fouhey, M Rodriguez, and A Gupta. Learning a predictable and generative vector representation for objects. ECCV'16
- 3D-ray-tracing:
	- DRC. S Tulsiani, et. al. Multi-view Supervision for Single-view Reconstruction via Differentiable Ray Consistency. CVPR'17
- 2D-rendering-loss:
	- DeepMind. Unsupervised learning of 3d structure from images. NeurIPS'16
		- REINFORCE to bypass back-prop through black-box renderer;
	- PTN: X Yan, et. al. Perspective transformer nets: Learning single-view 3d object reconstruction without 3d supervision. NIPS'16
		- Supervision: silhouette-based volumetric loss from space carving;
	- PrGAN [3DV'17]
- Multi-images consistency (Stereo-like, known camera pose):
	- Ray-tracing in 3D space for consistency;
	- Or projection in 2D image;
	- Surfacenet: An end-to-end 3d neural network for multiview stereopsis. ICCV'17
		- Unproject -> voxel + color;
		- https://github.com/mjiUST/SurfaceNet
		- Output/Supervision: 0/1 for on surface or not;
	- LSM: A. Kar, C. Häne, J. Malik. Learning a multi-view stereo machine. NeurIPS'17
		- https://github.com/akar43/lsm
	- MVC: S Tulsiani, A Efros, J Malik. Multi-view Consistency as Supervisory Signal for Learning Shape and Pose Prediction. CVPR'18
		- https://github.com/shubhtuls/mvcSnP
		- Input: single image; output: camera pose, 3D-shape;
		- Im1 -> [Shape-CNN] -> shape (conanical view)
		- Im2 -> [Pose-CNN] -> pose;
		- Supervision: L(shape1 + pose2, im2)

## Unproject from 2D (assume known camera pose?):
- A Ulusoy, A Geiger, and M Black. Towards probabilistic volumetric reconstruction using ray potentials. 3DV'15
- J. Gwak, C. B. Choy, M. Chandraker, A. Garg, and S. Savarese. Weakly supervised 3d reconstruction with adversarial constraint. 3DV'17
	- Input: multiple images;
	- Backbone: CNN-RNN;
	- Final output ray-trace pooling to get 2D projection;
	- Supervision: adversarial with 3d shapes;
- S Richter and S Roth. Matryoshka networks: Predicting 3d geometry via nested shape layers. CVPR'18
	- Input: image, camera pose;
	- Voxel tube: input 2D feat nt x nt x f, finally get 3D no x no x no;
	- Shape layer: efficiently compress voxel tubes: record enter and exit shape;
	- Nested shape layers: similar to CSG? (handle image input one by one like Matryoshka doll)
- E Smith, S Fujimoto, D Meger. Multi-View Silhouette and Depth Decomposition for High Resolution 3D Object Representation. NIPS'18
	- https://github.com/EdwardSmith1884/Multi-View-Silhouette-and-Depth-Decomposition-for-High-Resolution-3D-Object-Representation
	- Main insight: high-resolution (512 x 512 x 512);
	- Input: 2D image or 3D low-res voxel;
	- Model:
		- Representation: six axis-aligned orthographic depth maps (ODM);
			- Super-resolve the ODM;
		- 3D model carving: use high-res ODM to update 3D-voxel;
- **SATNet**: S Liu, Y HU, Y Zeng, Q Tang, B Jin, Y Han, X Li. See and Think: Disentangling Semantic Scene Completion. NIPS'18
	- https://github.com/ShiceLiu/SATNet
	- Input: 2D image/depth map;
	- Model: 3 components;
		- SNet: 2D Semantic Segmentation
		- 2D-3D Reprojection Layer: given depth, sem label, intrinsic, extrinsic, unproject to get voxel as D x Sx x Sy x Sz;
		- TNet: 3D Semantic Scene Completion;
- H Xie, H Yao, X Sun, S Zhou, and S Zhang. Pix2vox: Context-aware 3d reconstruction from single and multi-view images. ICCV'19
	- https://infinitescript.com/project/pix2vox/
	- Insight: Fusion of different 3D voxel with **context-aware-fusion network**;
		- Select confident (seen) parts from each image;
	- Refiner net to super-resolve;