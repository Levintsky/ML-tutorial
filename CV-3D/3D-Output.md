# 3D Data as Output (Objects)

## Basics
- Representations:
	- Point clouds;
	- Voxel;
	- Oct-tree;
	- Mesh;
	- Primitives;
	- Implicit functions;
	- 2.5D;
- Supervision:
	- **Chamfer distance** (a strong baseline)
		- Sum of closest point distances
		- Asymmetric
		- For Hausdorff distance, simply a distance transform?

## Unclassified
- Danilo Jimenez Rezende, SM Eslami, Shakir Mohamed, Peter Battaglia, Max Jaderberg, and Nicolas Heess. Unsupervised learning of 3d structure from images. NIPS'16
	- Key insight: **VAE** style; SSL; REINFORCE to back-prop through black-box renderer;
	- Input: single image;
	- Experiment: ShapeNet;
	<img src="/CV-3D/images/3d_output/unsup-3d.png" alt="drawing" width="600"/>
- **Voxlet**: Michael Firman, Oisin Mac Aodha, Simon Julier, Gabriel J. Brostow. Structured Prediction of Unobserved Voxels From a Single Depth Image. CVPR 2016
	- Shape prior
	- https://github.com/mdfirman/voxlets

## Legacy (Non-DL)
- A Kar, S Tulsiani, J Carreira, J Malik. Category-Specific Object Reconstruction from a Single Image. CVPR'15
	- https://github.com/akar43/CategoryShapes

## Point Cloud
- GAN:
	- Chun-Liang Li, Manzil Zaheer, Yang Zhang, Barnabas Poczos, and Ruslan Salakhutdinov. Point cloud gan. ICLR'19
- H Fan, H Su, and L Guibas. A point set generation network for 3d object reconstruction from a single image. CVPR'17
	- Key insight: hourglass better; random variable;
	- https://github.com/fanhqme/PointSetGeneration
	- Input: image, random variable r; output: point cloud;
	- Net-structure: encoder, predictor;
	- Supervision: 1. Chamfer distance; 2. EMD with approximation;
	<img src="/CV-3D/images/3d_output/point-set-gen.png" alt="drawing" width="600"/>
- DeformNet: A Kuryenkov, J Ji, A Garg, V Mehta, J Gwak, C Choy, S Savarese. DeformNet: Free-Form Deformation Network for 3D Shape Reconstruction from a Single Image. 2017
	- Insight: first CNN retrive a **prototype**, then CNN to deform
	- https://deformnet-site.github.io/DeformNet-website/
	- Input: single image; output: point clouds;
- Chen-Hsuan Lin, Chen Kong, and Simon Lucey. Learning efficient point cloud generation for dense 3d object reconstruction. AAAI'18
- Panos Achlioptas, Olga Diamanti, Ioannis Mitliagkas, and Leonidas Guibas. Learning representations and generative models for 3d point clouds. ICML'18
- Matheus Gadelha, Rui Wang, and Subhransu Maji. Multiresolution tree networks for 3d point cloud processing. ECCV'18
	- VAE
- **AAE**: Maciej Zamorski, Maciej Zieba, Rafał Nowak, Wojciech Stokowiec, and Tomasz Trzciński. Adversarial autoen-coders for generating 3d point clouds. 2018
	- Build on Alireza Makhzani, Jonathon Shlens, Navdeep Jaitly, Ian Goodfellow, and Brendan Frey. Adversarial autoencoders. 2015
- Guandao Yang, Xun Huang, Zekun Hao, Ming-Yu Liu, Serge Belongie, and Bharath Hariharan. Pointflow: 3d point cloud generation with continuous normalizing flows. ICCV'19

## Voxel
- Zhirong Wu, Shuran Song, Aditya Khosla, Fisher Yu, Linguang Zhang, Xiaoou Tang, and Jianxiong Xiao. 3d shapenets: A deep representation for volumetric shapes. CVPR'15
	- Input: image; output: voxel;
- R Girdhar, D F Fouhey, M Rodriguez, and A Gupta. Learning a predictable and generative vector representation for objects. ECCV'16
- **3D-R2N2**: Christopher B. Choy, Danfei Xu, JunYoung Gwak, Kevin Chen, Silvio Savarese. 3D-R2N2: A Unified Approach for Single and Multi-view 3D Object Reconstruction. ECCV'16
	- https://github.com/chrischoy/3D-R2N2
	- Input: single/multiple images; output: voxel;
	- Update model with RNN each time with a new image;
	<img src="/CV-3D/images/3d_output/3d-r2n2.png" alt="drawing" width="500"/>
- Andrew Brock, Theodore Lim, James M Ritchie, and Nick Weston. Generative and discriminative voxel modeling with convolutional neural networks. 3D Deep Learning Workshop at NIPS'16
	- VAE;
	- https://github.com/ajbrock/Generative-and-Discriminative-Voxel-Modeling
- **PTN**: X Yan, J Yang, E Yumer, Y Guo, and H Lee. Perspective transformer nets: Learning single-view 3d object reconstruction without 3d supervision. NIPS'16
	- Insight: encoder-decoder for 2d-3d, no 3d supervision, silhouette supervision from different views instead of gt;
	- https://github.com/xcyan/ptnbhwd
	- Input: image; output: voxel;
	- Assumption: clean background;
	- Encoder-decoder: view-invariant encoder for image h(I), decoder generates 3d v=g(h(I));
	- Supervision: silhouette-based volumetric loss from space carving;
	<img src="/CV-3D/images/3d_output/per-trans-net.png" alt="drawing" width="600"/>
- Jiajun Wu, Chengkai Zhang, Tianfan Xue, Bill Freeman, and Josh Tenenbaum. Learning a probabilistic latent space of object shapes via 3d generative-adversarial modeling. NIPS'16
	- GAN / GAN-VAE;
	- Noisy / Blurry;
- **Surfacenet**: Ji, M., Gall, J., Zheng, H., Liu, Y., Fang, L. Surfacenet: An end-to-end 3d neural network for multiview stereopsis. ICCV'17
	- Insight: end-to-end multi-view stereo; geometry with color encoded in voxel with **unproject**;
	- https://github.com/mjiUST/SurfaceNet
	- Input: images with camera pose; Output: 3D voxel, with [0,1] for on surface or not;
	- Turn images to CVC (color voxel cube)\
	<img src="/CV-3D/images/3d_output/surface-net1.png" alt="drawing" width="350"/>
	<img src="/CV-3D/images/3d_output/surface-net2.png" alt="drawing" width="350"/>
- **PrGAN**: Matheus Gadelha, Subhransu Maji and Rui Wang. 3D Shape Induction from 2D Views of Multiple Objects. 3DV'17
	- https://github.com/matheusgadelha/PrGAN
- J. Gwak, C. B. Choy, M. Chandraker, A. Garg, and S. Savarese. Weakly supervised 3d reconstruction with adversarial constraint. 3DV'17
- **HSP**: C Hane, S Tulsiani, J Malik. Hierarchical Surface Prediction for 3D Object Reconstruction. 3DV'17
	- Insight: **coarse to fine**, 16^3 to 32^3 to ... 256^3; only nodes on boundary needs upsamplng;
	- https://github.com/chaene/hsp
	- Input: color, depth, partial volume; Ouptut: voxel (3 classes: free, **boundary**, occupied)
	- CNN with deep-supervision on different resolution
	- Most important part: predict layer l+1 based on layer l (e.g. from 16^3 to 32^3)
		- 1. Feature Cropping: (b/2+2p)^3 region with p padding;
		- 2. Upsampling: (b+2p)^3 region
		- 3. Output generation: max boundary prediction reponse; above threshold, expand child;
	<img src="/CV-3D/images/3d_output/factor3d.png" alt="drawing" width="600"/>
- **LSM**: A. Kar, C. Häne, J. Malik. Learning a multi-view stereo machine. NIPS'17
	- Key insight: **unproject**;
	- https://github.com/akar43/lsm
	- Input: multiple images; Output: 32^3 Voxel 3D;
	- Assumption: **camera pose known**;
	- Cost volume; \
	<img src="/CV-3D/images/stereo/lsm1.png" alt="drawing" width="500"/>
	<img src="/CV-3D/images/stereo/lsm2.png" alt="drawing" width="500"/>
- **DRC**: S Tulsiani, T Zhou, A Efros, J Malik. Multi-view Supervision for Single-view Reconstruction via Differentiable Ray Consistency.  PAMI'19
	- Key insight: relax 3D GT requirement to 2D consistency!
	- https://github.com/shubhtuls/drc (torch);
	- Input: image (model) + multiple images (refine?); Output: voxel for 3d;
	- Assume: camera poses known?
	- Model: ray termination event;	Event: a ray intersect a voxel, previous voxels are all unoccupied
	- Supervision:
		- Depth, Foreground mask
		- Per-ray consistency loss
	- Experiment: ShapeNet; PASCAL 3D
	<img src="/CV-3D/images/3d_output/drc.png" alt="drawing" width="600"/>
- **MVC**: S Tulsiani, A Efros, J Malik. Multi-view Consistency as Supervisory Signal for Learning Shape and Pose Prediction. CVPR'18
	- Key insight: **unknown-shape**, 
	- https://github.com/shubhtuls/mvcSnP
	- Input: single image; output: camera pose, 3D-shape;
	- Training mode: (two images of an object as input)
		- Shape from first view; (conanical view?)
		- Pose from second view;
	- Test mode: independent shape and pose;
	<img src="/CV-3D/images/3d_output/mvc.png" alt="drawing" width="600"/>
- Z. Wu, X. Wang, D. Lin, D. Lischinski, D. Cohen-Or, and H. Huang. Structure-aware generative network for 3d-shape modeling. TOG'19
	- GRU + VAE;

## Mesh
- Legacy- Marching Cubes:
	- Given function defining +/- as outside inside, output the surface (mesh);
	- Insight: go through each cube independently, lookup table (2 ^ 8 = 256 cases), handle the surface accordingly by lookup, adapt to find a better surface;
	- http://www.cs.carleton.edu/cs_comps/0405/shape/marching_cubes.html
	- **Marching cubes**: W. E. Lorensen and H. E. Cline. Marching cubes: A high resolution 3d surface construction algorithm. SIGGRAPH'87
		- Input: mask; output: mesh triangulation;
	- https://www.boristhebrave.com/2018/04/15/marching-cubes-tutorial/
	- https://www.boristhebrave.com/2018/04/15/marching-cubes-3d-tutorial/
	- https://github.com/BorisTheBrave/mc-dc
- Q Tan, L Gao, Y Lai, J Yang and S Xia. Mesh-based Autoencoders for Localized Deformation Component Analysis. 2017
	- AutoEncoder;
	- Input: multiple mesh; output: new mesh synthesis (deformation);
- Nobuyuki Umetani. Exploring Generative 3D Shapes Using Autoencoder Networks. SIGGRAPH Asia'17
	- AutoEncoder;
- **AtlasNet**. T. Groueix, M. Fisher, V. G. Kim, B. C. Russell, and M. Aubry. Atlasnet: A papier-mache approach to learning 3d surface generation. CVPR'18
	- https://github.com/ThibaultGROUEIX/AtlasNet
- Angjoo Kanazawa, Shubham Tulsiani, Alexei A Efros, and Jitendra Malik. Learning category-specific mesh reconstruction from image collections. ECCV'18
- Nanyang Wang, Yinda Zhang, Zhuwen Li, Yanwei Fu, Wei Liu, and Yu-Gang Jiang. Pixel2mesh: Generating 3d mesh models from single rgb images. ECCV'18
- **GenRe**: X Zhang, Z Zhang, C Zhang, J Tenenbaum, W Freeman and J Wu. Learning to Reconstruct Shapes from Unseen Classes. NIPS'18
	- Insight: project to spherical map;
	- Input: single image;
	- https://github.com/xiumingzhang/GenRe-ShapeHD
	<img src="/CV-3D/images/3d_output/genre.png" alt="drawing" width="600"/>
- Georgia Gkioxari, Jitendra Malik, and Justin Johnson. Mesh R-CNN. ICCV'19
- Edward J Smith, Scott Fujimoto, Adriana Romero, and David Meger. Geometrics: Exploiting geometric structure for graph-encoded objects. 2019

## Oct-Tree
- Gernot Riegler, Ali Osman Ulusoy, and Andreas Geiger. Octnet: Learning deep 3d representations at high resolutions. CVPR'17
- **OGN**: Maxim Tatarchenko, Alexey Dosovitskiy, and Thomas Brox. Octree generating networks: Efficient convolutional architectures for high-resolution 3d outputs. ICCV'17
	- Key: **Coarse to fine**;
	- https://github.com/lmb-freiburg/ogn
	- Input: image; output: voxel;
	<img src="/CV-3D/images/3d_output/ogn.png" alt="drawing" width="600"/>
- Gernot Riegler, Ali Osman Ulusoy, Horst Bischof, and Andreas Geiger. Octnetfusion: Learning depth fusion from data. 3DV'17

## Templates/Primitives (Also check composition folder)
- Legacy:
	- A.-L. Chauve, P. Labatut, and J.-P. Pons. Robust piecewise planar 3d reconstruction and completion from large-scale unstructured point data. CVPR'10
	- F. Lafarge and P. Alliez. Surface reconstruction through point set structuring. CGF'13
	- S. N. Sinha, D. Steedly, R. Szeliski, M. Agrawala, and M. Pollefeys. Interactive 3d architectural modeling from unordered photo collections. TOG'08
	- A. Bodis-Szomoru, H. Riemenschneider, and L. Van Gool. Fast, approximate piecewise-planar modeling based on sparse structure-from-motion and superpixels. CVPR'14
- Recursive:
	- Chengjie Niu, Jun Li, Kai Xu. Im2Struct: Recovering 3D Shape Structure from a Single RGB Image. CVPR'18
- Scene-graph: James D Foley, Foley Dan Van, Andries Van Dam, Steven K Feiner, John F Hughes, J Hughes, and Edward Angel. Computer graphics: principles and practice. 1996
- CSG-Trees: James D Foley, Foley Dan Van, Andries Van Dam, Steven K Feiner, John F Hughes, J Hughes, and Edward Angel. Computer graphics: principles and practice. 1996
- Unity implicits: Yutaka Ohtake, Alexander Belyaev, Marc Alexa, Greg Turk, and Hans-Peter Seidel. Multi-level partition of unity implicits, volume 22. ACM, 2003
- Shubham Tulsiani, Hao Su, Leonidas J Guibas, Alexei A Efros, and Jitendra Malik. Learning shape abstractions by assembling volumetric primitives. CVPR'17
- **CSGNet**: Gopal Sharma Rishabh Goyal Difan Liu Evangelos Kalogerakis Subhransu Maji. CSGNet: Neural Shape Parser for Constructive Solid Geometry. CVPR'18
- Despoina Paschalidou, Ali Osman Ulusoy, and Andreas Geiger. Superquadrics revisited: Learning 3d shape parsing beyond cuboids. CVPR'19
- **SIF**: Kyle Genova, Forrester Cole, Daniel Vlasic, Aaron Sarna, William T Freeman, and Thomas Funkhouser. Learning shape templates with structured implicit functions. ICCV'19

## Implicit Functions
- SDF:
	- **DeepSDF**: Jeong Joon Park, Peter Florence, Julian Straub, Richard Newcombe, and Steven Lovegrove. DeepSDF: Learning continuous signed distance functions for shape representation. CVPR'19
		- Insight: point-based SDF;
		- https://github.com/facebookresearch/DeepSDF
		- Formulation: given a point x, a NN with latent code z as a classifier \
			<img src="/CV-3D/images/3d_output/deep-sdf1.png" alt="drawing" width="350"/>
		- Autoencoder: \
			<img src="/CV-3D/images/3d_output/deep-sdf2.png" alt="drawing" width="400"/>
		- Auto-decoder (encoder-less) training and inference: \
			<img src="/CV-3D/images/3d_output/deep-sdf3.png" alt="drawing" width="400"/>
			<img src="/CV-3D/images/3d_output/deep-sdf4.png" alt="drawing" width="400"/>
- Indicator:
	- **OccNet**: Lars Mescheder, Michael Oechsle, Michael Niemeyer, Sebastian Nowozin, and Andreas Geiger. Occupancy networks: Learning 3d reconstruction in function space. CVPR'19
		- Insight: new 3D representation, could generate mesh at any resoltuion;
		- https://github.com/autonomousvision/occupancy_networks
		- Input image; output: **continuous decision boundary of a deep-NN**;
		- Learn an occupancy function: R3 to [0,1];
		- Surface at inference time: Multiresolution IsoSurface Extraction (MISE)
- Zhiqin Chen and Hao Zhang. Learning implicit fields for generative shape modeling. CoRR'18
- **DISN**: Qiangeng Xu, Weiyue Wang, Duygu Ceylan, Radomir Mech, and Ulrich Neumann. Disn: Deep implicit surface network for high-quality single-view 3d reconstruction. 2019

## 2.5D, Skeleton, 3D-Aware 2D Cues...
- S. Galliani and K. Schindler. Just look at the image: Viewpoint-specific surface normal prediction for improved multi-view reconstruction. CVPR'16
	- Estimate **normal** of depth map; then improve depth map fusion;
- **3D-INN**: J Wu, T Xue, J Lim, Y Tian, J Tenenbaum, A Torralba, and W Freeman. Single Image 3D Interpreter Network, ECCV'16, IJCV'18
	- Key insight: skeleton representation for 3D objects (so keypoints infers 3D);
	- Input: single image; output:	2d keypoints as well as 3d structure;
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
- **ShapeHD**: J. Wu, C. Zhang, X. Zhang, Z. Zhang, W. T. Freeman, and J. B. Tenenbaum. Learning shape priors for single-view 3D completion and reconstruction. ECCV'18
	- Key insigth: improve on MarrNet with naturalness (pretrained discriminator) to solve ambiguity, with Wasserstein-GAN loss;
	- https://github.com/xiumingzhang/GenRe-ShapeHD
	- Input: single view; Output: 3D completion/reconstruction; \
	<img src="/CV-3D/images/3d_output/shapehd.png" alt="drawing" width="600"/>
