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
- **Voxlet**: Michael Firman, Oisin Mac Aodha, Simon Julier, Gabriel J. Brostow. Structured Prediction of Unobserved Voxels From a Single Depth Image. CVPR'16
	- https://github.com/mdfirman/voxlets
	- Input depth image (no-rgbd), output voxel binary occupancy;
	- Model: structured random forest;

## Backbone
- 3D-Conv/Deconv: [Jiajun NeurIPS'16]; [Andrew Brock, NeurIPSW'16]
- 3D-Conv + RNN/LSTM: 3D-R2N2 [Savarese, ECCV'16]
- Recursive/Oc-tree/Hierarchical/Coarse2Fine/...:
	- **OGN**: [Maxim Tatarchenko, Alexey Dosovitskiy, and Thomas Brox ICCV'17]
	- **HSP**: C Hane, S Tulsiani, J Malik. 3DV'17
	- Octnetfusion: [A. Geiger, 3DV'17]
	- **Adaptive O-CNN**: Xin Tong. [SIGGRAPH Asia'18]

## Supervision
- Pixel/pointwise binary: 3D-R2N2;
- GAN on whole object: [Jiajun NeurIPS'16];
- VAE: [Andrew Brock, NeurIPSW'16]

## 3D-Deconv from latent space
- Zhirong Wu, Shuran Song, Aditya Khosla, Fisher Yu, Linguang Zhang, Xiaoou Tang, and Jianxiong Xiao. 3d shapenets: A deep representation for volumetric shapes. CVPR'15
	- Input: image; output: voxel;
- R Girdhar, D F Fouhey, M Rodriguez, and A Gupta. Learning a predictable and generative vector representation for objects. ECCV'16
	- Problem definition: AE
	- Input: Voxel, image; Output: voxel;
	- Model:
		- Encoder: concatenate of features conv3d for voxel, conv2d for image;
		- Decoder: 3D-deconv;
- Danilo Jimenez Rezende, SM Eslami, Shakir Mohamed, Peter Battaglia, Max Jaderberg, and Nicolas Heess. Unsupervised learning of 3d structure from images. NIPS'16
	- Key insight: **c-VAE** style;
	- Input: single image/voxel;
	- Supervision: 2D-weak-sup; REINFORCE to bypass back-prop through black-box renderer;
	- Experiment: ShapeNet;
	<img src="/CV-3D/images/3d_output/unsup-3d.png" alt="drawing" width="600"/>
- Interactive 3D modeling with a generative adversarial network, 3D Vision 2017
- **PrGAN**: Matheus Gadelha, Subhransu Maji and Rui Wang. 3D Shape Induction from 2D Views of Multiple Objects. 3DV'17
	- https://github.com/matheusgadelha/PrGAN
	- Input: latent code 200-dim;
	- Backbone: 3d-deconv;
	- Supervision: weak-supervised, project to 2D then a discriminator;
- D. Stutz and A. Geiger. Learning 3D shape completion from laser scan data with weak supervision. CVPR'18
	- Problem: 3D completion;
	- Model:
		- Step 1: VAE y -> y'
		- Step 2: keep the decoder, train an encoder to map partial data to the same latent space;
- Z. Wu, X. Wang, D. Lin, D. Lischinski, D. Cohen-Or, and H. Huang. SAGNet: Structure-aware generative network for 3d-shape modeling. TOG'19
	- GRU + VAE;

## Unproject from 2D (assume known camera pose?):
- A. O. Ulusoy, A. Geiger, and M. J. Black. Towards probabilistic volumetric reconstruction using ray potentials. 3DV'15
- **PTN**: X Yan, J Yang, E Yumer, Y Guo, and H Lee. Perspective transformer nets: Learning single-view 3d object reconstruction without 3d supervision. NIPS'16
	- Insight: encoder-decoder for 2d-3d, no 3d supervision, silhouette supervision from different views instead of gt;
	- https://github.com/xcyan/ptnbhwd
	- Input: image; output: voxel;
	- Assumption: clean background;
	- Encoder-decoder: view-invariant encoder for image h(I), decoder generates 3d v=g(h(I));
	- Supervision: silhouette-based volumetric loss from space carving;
	<img src="/CV-3D/images/3d_output/per-trans-net.png" alt="drawing" width="600"/>
- J. Gwak, C. B. Choy, M. Chandraker, A. Garg, and S. Savarese. Weakly supervised 3d reconstruction with adversarial constraint. 3DV'17
	- Input: multiple images;
	- Backbone: CNN-RNN;
	- Final output ray-trace pooling to get 2D projection;
	- Supervision: adversarial with 3d shapes;
- **Surfacenet**: Ji, M., Gall, J., Zheng, H., Liu, Y., Fang, L. Surfacenet: An end-to-end 3d neural network for multiview stereopsis. ICCV'17
	- Insight: end-to-end multi-view stereo; geometry with color encoded in voxel with **unproject**;
	- https://github.com/mjiUST/SurfaceNet
	- Input: images with camera pose; Output: 3D voxel, with [0,1] for on surface or not;
	- Turn images to CVC (color voxel cube)\
	<img src="/CV-3D/images/3d_output/surface-net1.png" alt="drawing" width="350"/>
	<img src="/CV-3D/images/3d_output/surface-net2.png" alt="drawing" width="350"/>
- **LSM**: A. Kar, C. Häne, J. Malik. Learning a multi-view stereo machine. NIPS'17
	- https://github.com/akar43/lsm
	- Input: multiple images; Output: 32^3 Voxel 3D;
	- Assumption: **camera pose known**;
	- Cost volume; \
	<img src="/CV-3D/images/stereo/lsm1.png" alt="drawing" width="500"/>
	<img src="/CV-3D/images/stereo/lsm2.png" alt="drawing" width="500"/>
- **MVC**: S Tulsiani, A Efros, J Malik. Multi-view Consistency as Supervisory Signal for Learning Shape and Pose Prediction. CVPR'18
	- Key insight: **unknown-shape**, 
	- https://github.com/shubhtuls/mvcSnP
	- Input: single image; output: camera pose, 3D-shape;
	- Training mode: (two images of an object as input)
		- Shape from first view; (conanical view?)
		- Pose from second view;
	- Test mode: independent shape and pose;
	<img src="/CV-3D/images/3d_output/mvc.png" alt="drawing" width="600"/>
- Stephan R. Richter and Stefan Roth. Matryoshka networks: Predicting 3d geometry via nested shape layers. CVPR'18
	- Input: image, camera pose;
	- Voxel tube: input 2D feat nt x nt x f, finally get 3D no x no x no;
	- Shape layer: efficiently compress voxel tubes: record enter and exit shape;
	- Nested shape layers: similar to CSG? (handle image input one by one like Matryoshka doll)
- **DRC**: S Tulsiani, T Zhou, A Efros, J Malik. Multi-view Supervision for Single-view Reconstruction via Differentiable Ray Consistency.  PAMI'19
	- Key insight: relax 3D GT requirement to 2D consistency!
	- https://github.com/shubhtuls/drc (torch);
	- Input: image (model) + multiple images (refine?); Output: voxel for 3d;
	- Model: ray termination event;	Event: a ray intersect a voxel, previous voxels are all unoccupied
	- Supervision:
		- Depth, Foreground mask
		- Per-ray consistency loss
	- Experiment: ShapeNet; PASCAL 3D
	<img src="/CV-3D/images/3d_output/drc.png" alt="drawing" width="600"/>
- Edward Smith, Scott Fujimoto, David Meger. Multi-View Silhouette and Depth Decomposition for High Resolution 3D Object Representation. NIPS'18
	- https://github.com/EdwardSmith1884/Multi-View-Silhouette-and-Depth-Decomposition-for-High-Resolution-3D-Object-Representation
	- Main insight: high-resolution (512 x 512 x 512);
	- Input: 2D image or 3D low-res voxel;
	- Model:
		- Representation: six axis-aligned orthographic depth maps (ODM);
			- Super-resolve the ODM;
		- 3D model carving: use high-res ODM to update 3D-voxel;
- **SATNet**: Shice Liu, YU HU, Yiming Zeng, Qiankun Tang, Beibei Jin, Yinhe Han, Xiaowei Li. See and Think: Disentangling Semantic Scene Completion. NIPS'18
	- https://github.com/ShiceLiu/SATNet
	- Input: 2D image/depth map;
	- Model: 3 components;
		- SNet: 2D Semantic Segmentation
		- 2D-3D Reprojection Layer: given depth, sem label, intrinsic, extrinsic, unproject to get voxel as D x Sx x Sy x Sz;
		- TNet: 3D Semantic Scene Completion;
- Haozhe Xie, Hongxun Yao, Xiaoshuai Sun, Shangchen Zhou, and Shengping Zhang. Pix2vox: Context-aware 3d reconstruction from single and multi-view images. ICCV'19
	- https://infinitescript.com/project/pix2vox/
	- Insight: Fusion of different 3D voxel with **context-aware-fusion network**;
		- Select confident (seen) parts from each image;
	- Refiner net to super-resolve;
- From other info:
	- **GenRe**: X Zhang, Z Zhang, C Zhang, J Tenenbaum, W Freeman and J Wu. Learning to Reconstruct Shapes from Unseen Classes. NIPS'18
		- Insight: project to spherical map;
		- Input: single image;
		- https://github.com/xiumingzhang/GenRe-ShapeHD
		<img src="/CV-3D/images/3d_output/genre.png" alt="drawing" width="600"/>
