# 3D Data as Output (Objects)

## Basics
- Representations:
	- Point clouds;
	- Voxel;
	- Mesh;
	- Oct-tree;
	- Templates: Primitives; Implicit functions;
	- Depth; 2.5D;
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

## Unclassified
- Stephan R. Richter and Stefan Roth. Matryoshka networks: Predicting 3d geometry via nested shape layers. CVPR'18
- Peng-Shuai Wang, Chun-Yu Sun, Yang Liu, and Xin Tong. Adaptive O-CNN: a patch-based deep representation of 3d shapes. SIGGRAPH Asia'18
- Edward Smith, Scott Fujimoto, David Meger. Multi-View Silhouette and Depth Decomposition for High Resolution 3D Object Representation. NIPS'18
	- https://github.com/EdwardSmith1884/Multi-View-Silhouette-and-Depth-Decomposition-for-High-Resolution-3D-Object-Representation
- **SRN**: Vincent Sitzmann, Michael Zollhofer, and Gordon Wetzstein. Scene representation networks: Continuous 3d-structure-aware neural scene representations. NeurIPS'19
- **NERF**: Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik, Jonathan T. Barron, Ravi Ramamoorthi, and Ren Ng. NeRF: Representing scenes as neural radiance fields for view synthesis. ECCV'20

## Legacy (Non-DL)
- Jason Rock, Tanmay Gupta, Justin Thorsen, JunYoung Gwak, Daeyun Shin, and Derek Hoiem. Completing 3d object shape from one depth image. CVPR'15
- A Kar, S Tulsiani, J Carreira, J Malik. Category-Specific Object Reconstruction from a Single Image. CVPR'15
	- https://github.com/akar43/CategoryShapes
- Georgios Pavlakos, Xiaowei Zhou, Aaron Chan, Konstantinos G. Derpanis, and Kostas Daniilidis. 6-dof object pose from semantic keypoints. ICRA'17

## Depth Prediction
- Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. Enforcing geometric constraints of virtual normal for depth prediction. ICCV'19

## 1. Point Cloud
- H Fan, H Su, and L Guibas. A point set generation network for 3d object reconstruction from a single image. CVPR'17
	- Key insight: hourglass better; random variable;
	- https://github.com/fanhqme/PointSetGeneration
	- Input: image, random variable r; output: point cloud;
	- Net-structure: encoder, predictor;
	- Supervision: 1. Chamfer distance; 2. EMD with approximation;
	<img src="/CV-3D/images/3d_output/point-set-gen.png" alt="drawing" width="600"/>
- **AAE**: Maciej Zamorski, Maciej Zieba, Rafał Nowak, Wojciech Stokowiec, and Tomasz Trzciński. Adversarial autoencoders for generating 3d point clouds. 2018
	- Build on Alireza Makhzani, Jonathon Shlens, Navdeep Jaitly, Ian Goodfellow, and Brendan Frey. Adversarial autoencoders. 2015
- Chen-Hsuan Lin, Chen Kong, and Simon Lucey. Learning efficient point cloud generation for dense 3d object reconstruction. AAAI'18
- Panos Achlioptas, Olga Diamanti, Ioannis Mitliagkas, and Leonidas Guibas. Learning representations and generative models for 3d point clouds. ICML'18
- **FoldingNet**: Y. Yang, C. Feng, Y. Shen, and D. Tian. Foldingnet: Interpretable unsupervised learning on 3d point clouds. CVPR'18
	- https://www.merl.com/research/license#FoldingNet
- Matheus Gadelha, Rui Wang, and Subhransu Maji. Multiresolution tree networks for 3d point cloud processing. ECCV'18
	- VAE
- Chun-Liang Li, Manzil Zaheer, Yang Zhang, Barnabas Poczos, and Ruslan Salakhutdinov. Point cloud gan. ICLR'19
- **Pointflow**: Guandao Yang, Xun Huang, Zekun Hao, Ming-Yu Liu, Serge Belongie, and Bharath Hariharan. Pointflow: 3d point cloud generation with continuous normalizing flows. ICCV'19
	- CNF based model;
- Ruihui Li, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. PU-GAN: A point cloud upsampling adversarial network. ICCV'19

## 2. Voxel
- Completion:
	- D. Stutz and A. Geiger. Learning 3D shape completion from laser scan data with weak supervision. CVPR'18
- Oct-Tree:
	- Gernot Riegler, Ali Osman Ulusoy, and Andreas Geiger. Octnet: Learning deep 3d representations at high resolutions. CVPR'17
	- **OGN**: Maxim Tatarchenko, Alexey Dosovitskiy, and Thomas Brox. Octree generating networks: Efficient convolutional architectures for high-resolution 3d outputs. ICCV'17
		- Key: **Coarse to fine**;
		- https://github.com/lmb-freiburg/ogn
		- Input: image; output: voxel;
		<img src="/CV-3D/images/3d_output/ogn.png" alt="drawing" width="600"/>
	- Gernot Riegler, Ali Osman Ulusoy, Horst Bischof, and Andreas Geiger. Octnetfusion: Learning depth fusion from data. 3DV'17
- Zhirong Wu, Shuran Song, Aditya Khosla, Fisher Yu, Linguang Zhang, Xiaoou Tang, and Jianxiong Xiao. 3d shapenets: A deep representation for volumetric shapes. CVPR'15
	- Input: image; output: voxel;
- A. O. Ulusoy, A. Geiger, and M. J. Black. Towards probabilistic volumetric reconstruction using ray potentials. 3DV'15
- **Voxlet**: Michael Firman, Oisin Mac Aodha, Simon Julier, Gabriel J. Brostow. Structured Prediction of Unobserved Voxels From a Single Depth Image. CVPR'16
	- https://github.com/mdfirman/voxlets
	- Input depth image (no-rgbd), output voxel binary occupancy;
	- Model: structured random forest;
- R Girdhar, D F Fouhey, M Rodriguez, and A Gupta. Learning a predictable and generative vector representation for objects. ECCV'16
- **3D-R2N2**: Christopher B. Choy, Danfei Xu, JunYoung Gwak, Kevin Chen, Silvio Savarese. 3D-R2N2: A Unified Approach for Single and Multi-view 3D Object Reconstruction. ECCV'16
	- https://github.com/chrischoy/3D-R2N2
	- Input: single/multiple images; output: voxel;
	- Update model with RNN each time with a new image;
	<img src="/CV-3D/images/3d_output/3d-r2n2.png" alt="drawing" width="500"/>
- Danilo Jimenez Rezende, SM Eslami, Shakir Mohamed, Peter Battaglia, Max Jaderberg, and Nicolas Heess. Unsupervised learning of 3d structure from images. NIPS'16
	- Key insight: **VAE** style; SSL; REINFORCE to back-prop through black-box renderer;
	- Input: single image;
	- Experiment: ShapeNet;
	<img src="/CV-3D/images/3d_output/unsup-3d.png" alt="drawing" width="600"/>
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
- Y. Liao, S. Donne, and A. Geiger. Deep marching cubes: Learning explicit surface representations. CVPR'18
- **SATNet**: Shice Liu, YU HU, Yiming Zeng, Qiankun Tang, Beibei Jin, Yinhe Han, Xiaowei Li. See and Think: Disentangling Semantic Scene Completion. NIPS'18
	- https://github.com/ShiceLiu/SATNet
- Haozhe Xie, Hongxun Yao, Xiaoshuai Sun, Shangchen Zhou, and Shengping Zhang. Pix2vox: Context-aware 3d reconstruction from single and multi-view images. ICCV'19
- Z. Wu, X. Wang, D. Lin, D. Lischinski, D. Cohen-Or, and H. Huang. Structure-aware generative network for 3d-shape modeling. TOG'19
	- GRU + VAE;

## 3. Mesh
- Legacy: Marching Cubes;
	- Given function defining +/- as outside inside, output the surface (mesh);
	- Insight: go through each cube independently, lookup table (2 ^ 8 = 256 cases), handle the surface accordingly by lookup, adapt to find a better surface;
	- http://www.cs.carleton.edu/cs_comps/0405/shape/marching_cubes.html
	- **Marching cubes**: W. E. Lorensen and H. E. Cline. Marching cubes: A high resolution 3d surface construction algorithm. SIGGRAPH'87
		- Input: mask; output: mesh triangulation;
	- https://www.boristhebrave.com/2018/04/15/marching-cubes-tutorial/
	- https://www.boristhebrave.com/2018/04/15/marching-cubes-3d-tutorial/
	- https://github.com/BorisTheBrave/mc-dc
- Legacy: **Poisson Surface Reconstruction**
	- Assumption: known **oriented normals**;
	- M. M. Kazhdan, M. Bolitho, and H. Hoppe. Poisson surface reconstruction. SGP'06
	- M. M. Kazhdan and H. Hoppe. Screened poisson surface reconstruction. SIGGRAPH'13
- Legacy: deform an initial mesh;
	- Similar to active-contour, leads to local minima;
	- Andrei Sharf, Thomas Lewiner, Ariel Shamir, Leif Kobbelt, and Daniel Cohen-Or. 2006. Competing fronts for coarse–to–fine surface reconstruction. CGF'06
- Legacy:
	- Hugues Hoppe. Progressive meshes. SIGGRAPH'96
	- F. Bernardini, J. Mittleman, H. Rushmeier, C. Silva, and G. Taubin. The ball-pivoting algorithm for surface reconstruction. TVCG'99
	- F. Calakli and G. Taubin. SSD: smooth signed distance surface reconstruction. CGF'11
- DeformNet: A Kuryenkov, J Ji, A Garg, V Mehta, J Gwak, C Choy, S Savarese. DeformNet: Free-Form Deformation Network for 3D Shape Reconstruction from a Single Image. 2017
	- Insight: first CNN retrive a **prototype**, then CNN to deform
	- https://deformnet-site.github.io/DeformNet-website/
	- Input: single image; output: point clouds;
- Q Tan, L Gao, Y Lai, J Yang and S Xia. Mesh-based Autoencoders for Localized Deformation Component Analysis. 2017
	- AutoEncoder;
	- Input: multiple mesh; output: new mesh synthesis (deformation);
- C. Kong, C.-H. Lin, and S. Lucey. Using locally corresponding CAD models for dense 3D reconstructions from a single image. CVPR'17
	- Assumption: template provided;
- Nobuyuki Umetani. Exploring Generative 3D Shapes Using Autoencoder Networks. SIGGRAPH Asia'17
	- AutoEncoder;
- **AtlasNet**. T. Groueix, M. Fisher, V. G. Kim, B. C. Russell, and M. Aubry. Atlasnet: A papier-mache approach to learning 3d surface generation. CVPR'18
	- https://github.com/ThibaultGROUEIX/AtlasNet
	- Input point cloud or image encoded by a NN as feature f(x)
	- Then, f(x) and points sampled on a rectangle reconstruct an atlas on shape x;
		- Multiple MLP for multiple patches (Atlas);
- **Chart**: Heli Ben-Hamu, Haggai Maron, Itay Kezurer, Gal Avineri, and Yaron Lipman. Multi-chart generative surface modeling. TOG'18
	- https://github.com/helibenhamu/multichart3dgans
- **cmr**: Angjoo Kanazawa, Shubham Tulsiani, Alexei A Efros, and Jitendra Malik. Learning category-specific mesh reconstruction from image collections. ECCV'18
	- https://github.com/akanazawa/cmr
	<img src="/CV-3D/images/3d_output/cmr.png" alt="drawing" width="550"/>
- **Pixel2mesh**: Nanyang Wang, Yinda Zhang, Zhuwen Li, Yanwei Fu, Wei Liu, and Yu-Gang Jiang. Pixel2mesh: Generating 3d mesh models from single rgb images. ECCV'18
	- GNN to deform a ball; unpool to add more nodes and edges;
	- CD for supervision;
	- https://github.com/nywang16/Pixel2Mesh
	<img src="/CV-3D/images/3d_output/pixel2mesh-1.png" alt="drawing" width="500"/>
	<img src="/CV-3D/images/3d_output/pixel2mesh-2.png" alt="drawing" width="500"/>
- A. Ranjan, T. Bolkart, S. Sanyal, and M. J. Black. Generating 3D faces using convolutional mesh autoencoders. ECCV'18
- **GenRe**: X Zhang, Z Zhang, C Zhang, J Tenenbaum, W Freeman and J Wu. Learning to Reconstruct Shapes from Unseen Classes. NIPS'18
	- Insight: project to spherical map;
	- Input: single image;
	- https://github.com/xiumingzhang/GenRe-ShapeHD
	<img src="/CV-3D/images/3d_output/genre.png" alt="drawing" width="600"/>
- Edward Smith, Scott Fujimoto, and David Meger. Multiview silhouette and depth decomposition for high resolution 3d object representation. NeurIPS'18
- **Geometrics**: Edward J Smith, Scott Fujimoto, Adriana Romero, and David Meger. Geometrics: Exploiting geometric structure for graph-encoded objects. ICML'19
	- https://github.com/EdwardSmith1884/GEOMetrics
- **DGP**: Francis Williams, Teseo Schneider, Claudio Silva, Denis Zorin, Joan Bruna, and Daniele
Panozzo. 2019. Deep geometric prior for surface reconstruction. CVPR'19
- **MeshCNN**: Rana Hanocka, Amir Hertz, Noa Fish, Raja Giryes, Shachar Fleishman, Daniel Cohen-Or. MeshCNN: A Network with an Edge. SIGGRAPH'19
	- https://ranahanocka.github.io/MeshCNN/
	- https://github.com/ranahanocka/MeshCNN/
	- https://docs.google.com/presentation/d/1yLZ6uyAujyF0MtFWofAMFgWQpWaDYqS8vkdge_lzk6g/edit#slide=id.g35f391192_00
	- Insight: edges + affinity from meshes;
	- Mesh-Conv:\
		<img src="/CV-3D/images/3d_output/mesh-conv.png" alt="drawing" width="400"/>
	- Mesh-Pool: remove edges to collapse (5 edges -> 2)\
		<img src="/CV-3D/images/3d_output/mesh-pool-1.png" alt="drawing" width="400"/>
		<img src="/CV-3D/images/3d_output/mesh-pool-2.png" alt="drawing" width="400"/>
	- Mesh-Unpool:\
		<img src="/CV-3D/images/3d_output/mesh-unpool.png" alt="drawing" width="400"/>
- **Mesh R-CNN**: Georgia Gkioxari, Jitendra Malik, and Justin Johnson. Mesh R-CNN. ICCV'19
	- https://gkioxari.github.io/meshrcnn/
	- https://github.com/facebookresearch/meshrcnn
	- Problem setup: input single image, output a set of detected object instances, with a triangle mesh for each object.
	- Approach: Mask R-CNN, coarse voxel (initial mesh), mesh refinement;
		<img src="/CV-3D/images/3d_output/mesh-rcnn.png" alt="drawing" width="600"/>
	- Lift to 3D: w x h G-channel;
	- Cubify: voxel to triangular mesh (8 vertices, 18 edges, 12 faces); merge shared edges and vertices; eliminate interior ones;
	- Mesh refinement (similar to **Pixel2mesh**):
		- 1. vertex alignment, which extracts image features for vertices; (with camera intrinsic)
		- 2. graph convolution, which propagates information along mesh edges;
		- 3. vertex refinement， which updates vertex positions.
	- Supevision: similar to **Geometrics**; sample points, Chamfer-Distance;
- Thiemo Alldieck, Gerard Pons-Moll, Christian Theobalt, and Marcus Magnor. Tex2shape: Detailed full human body geometry from a single image. ICCV'19
- **Pixel2mesh++**: Chao Wen, Yinda Zhang, Zhuwen Li, and Yanwei Fu. Pixel2mesh++: Multi-view 3d mesh generation via deformation. ICCV'19
- Rana Hanocka, Gal Metzer, Raja Giryes, Daniel Cohen-Or. Point2Mesh: A Neural Self-Prior for Deformable Meshes. SIGGRAPH'20
	- Insight: coarse-to-fine MeshCNN:
		<img src="/CV-3D/images/3d_output/point2mesh.png" alt="drawing" width="500"/>
	- Loss: Mesh to Point Cloud Distance: Chamfer + differentiable sampler;
	- Loss: Beam-gap loss: to handle narrow deep cavity;
	- Implementation: iterative for K=1000 iterations by network, then pass to RWM [Huang'18] to generate manifold, watertight and non-interscting surface;
	- Runtime (per iteration): 0.23/0.59/4.7 sec on 2k/6k/40k faces;

## 4. Templates/Primitives (Also check composition folder)
- Legacy:
	- S. N. Sinha, D. Steedly, R. Szeliski, M. Agrawala, and M. Pollefeys. Interactive 3d architectural modeling from unordered photo collections. TOG'08
	- A.-L. Chauve, P. Labatut, and J.-P. Pons. Robust piecewise planar 3d reconstruction and completion from large-scale unstructured point data. CVPR'10
	- Sanja Fidler, Sven Dickinson, and Raquel Urtasun. 3d object detection and viewpoint estimation with a deformable 3d cuboid model. NIPS'12
	- F. Lafarge and P. Alliez. Surface reconstruction through point set structuring. CGF'13
	- Mehmet Ersin Yümer and Levent Burak Kara. Co-abstraction of shape collections. TOG'12
	- A. Bodis-Szomoru, H. Riemenschneider, and L. Van Gool. Fast, approximate piecewise-planar modeling based on sparse structure-from-motion and superpixels. CVPR'14
	- Noa Fish, Melinos Averkiou, Oliver van Kaick, Olga Sorkine-Hornung, Daniel Cohen-Or, and Niloy J. Mitra. Meta-representation of shape families. TOG'14
	- Adrien Kaiser, José Alonso Ybáñez Zepeda, and Tamy Boubekeur. A survey of simple geometric primitives detection methods for captured 3d data. CGF'19
- Parts:
	- L. G. Roberts. Machine perception of three-dimensional solids. PhD thesis, Massachusetts Institute of Technology, 1963
	- Donald D Hoffman and Whitman A Richards. Parts of recognition. Cognition, 18(1-3):65–96, 1984
	- **geon**: I. Biederman. Recognition-by-components: a theory of human image understanding. Psychological review, 94(2):115, 1987
	- A. Golovinskiy and T. Funkhouser. Learning Consistent Segmentation of 3D Models. CG'09
	- Siddhartha Chaudhuri and Vladlen Koltun. Data-driven suggestions for creativity support in 3d modeling. ACM SIGGRAPH Asia'10
	- Qi-Xing Huang, Vladlen Koltun, and Leonidas J. Guibas. Joint shape segmentation with linear programming. TOG'11
	- Vladimir G. Kim, Wilmot Li, Niloy J. Mitra, Siddhartha Chaudhuri, Stephen DiVerdi, and Thomas A. Funkhouser. Learning part-based templates from large collections of 3d shapes. TOG'13
		- Jointly learn parts from multiple shapes
	- Jialei Huang, Guanqi Zhan, Qingnan Fan, Kaichun Mo, Lin Shao, Baoquan Chen, Leonidas J. Guibas, Hao Dong. Generative 3D Part Assembly via Dynamic Graph Learning. NeurIPS'20
		- https://hyperplane-lab.github.io/Generative-3D-Part-Assembly/
		- https://github.com/hyperplane-lab/Generative-3D-Part-Assembly
		- Task: given part point cloud, predict assembly;
		- GNN for relation reasoning, pooling for equivalent parts (4 legs)...
- Articulated objects (Human):
	- Allen, B., Curless, B., Popovic, Z.: Articulated body deformation from range scan data. SIGGRAPH'02
	- Brett Allen, Brian Curless, Zoran Popovic. The space of human body shapes: reconstruction and parameterization from range scans. TOG'03
	- Dragomir Anguelov, Praveen Srinivasan,Daphne Koller, Sebastian Thrun, Jim Rodgers, and James Davis. SCAPE: shape completion and animation of people. TOG'05
	- Allen, B., Curless, B., Popovic, Z.: Learning a correlated model of identity and pose-dependent body shape variation for real-time synthesis. Symposium on Computer Animation'06
	- Silvia Zuffi and Michael J. Black. The stitched puppet: A graphical model of 3d human shape and pose. CVPR'15
	- Matthew Loper, Naureen Mahmood, Javier Romero, Gerard Pons-Moll, and Michael J. Black. SMPL: a skinned multi-person linear model. TOG'15
	- A. Kanazawa, M. J. Black, D. W. Jacobs, and J. Malik. End-to-end recovery of human shape and pose. CVPR'18
	- **3d-coded**: Thibault Groueix, Matthew Fisher, Vladimir G. Kim, Bryan C. Russell, and Mathieu Aubry. 3d-coded: 3d correspondences by deep deformation. ECCV'18
		- http://imagine.enpc.fr/~groueixt/3D-CODED/
		- https://github.com/ThibaultGROUEIX/3D-CODED
- **Primitives**:
	- R. Schnabel, R. Wahl, and R. Klein. Efficient ransac for point-cloud shape detection. CGF'07
	- R. Schnabel, P. Degener, and R. Klein. Completion and reconstruction with primitive shapes. Eurographics'09
	- Ruwen Schnabel, Patrick Degener, and Reinhard Klein. Completion and reconstruction with primitive shapes. CGF'09
	- **Globfit**: Yangyan Li, Xiaokun Wu, Yiorgos Chrysanthou, Andrei Sharf, Daniel Cohen-Or, and Niloy J. Mitra. Globfit: consistently fitting primitives by discovering global relations. TOG'11
	- Shubham Tulsiani, Hao Su, Leonidas J. Guibas, Alexei A. Efros, Jitendra Malik. Learning Shape Abstractions by Assembling Volumetric Primitives. CVPR'17
		- Supervision: unsupervised, reconstruction loss;
	- Adrien Kaiser, José Alonso Ybáñez Zepeda, and Tamy Boubekeur. A survey of simple geometric primitives detection methods for captured 3d data. CGF'19
		- Primitives:
			- Size, orientation, position, convex, symmetric, assembles;
			- Primitives: planes, cuboids/boxes, spheres/cylinders/cones, ellipsoids/tori/...
		- Approaches;
			- Ransac;
			- Hough Transform;
			- Clustering; (region growing, ...)
			- Assembling Primitives;
	- **3d-prnn**: Chuhang Zou,Ersin Yumer, Jimei Yang, Duygu Ceylan,and Derek Hoiem. 3d-prnn: Generating shape primitives with recurrent neural networks. ICCV'17
	- **SFPN**: Lingxiao Li, Minhyuk Sung, Anastasia Dubrovina, Li Yi, and Leonidas J. Guibas. Supervised fitting of geometric primitives to 3d point clouds. CVPR'19
	- Theo Deprelle, Thibault Groueix, Matthew Fisher, Vladimir Kim, Bryan Russell, and Mathieu Aubry. Learning elementary structures for 3d shape generation and matching. NeurIPS'19
		- Assume all 3D data similar to a common template;
		- Learn to MLP-mapping or translate;
		- correspondence error if gt available, otherwise CD;
- **CAD**, memory-retrieval:
	- C. Kong, C.-H. Lin, and S. Lucey. Using locally corresponding CAD models for dense 3D reconstructions from a single image. CVPR'17
	- A. Kanazawa, S. Tulsiani, A. A. Efros, and J. Malik. Learning category-specific mesh reconstruction from image collections. ECCV'18
		- Morphable mesh;
	- Shuo Yang, Min Xu, Haozhe Xie, Stuart Perry, Jiahao Xia. Single-View 3D Object Reconstruction From Shape Priors in Memory. CVPR'21
- Hierarchical/Recursive/Graph/Scene-graph:
	- James D Foley, Foley Dan Van, Andries Van Dam, Steven K Feiner, John F Hughes, J Hughes, and Edward Angel. Computer graphics: principles and practice. 1996
	- Yanzhen Wang, Kai Xu, Jun Li, Hao Zhang, Ariel Shamir, Ligang Liu, Zhi-Quan Cheng, and Yueshan Xiong. Symmetry Hierarchy of Man-Made Objects. CGF'11
	- Symmetry hierarchy: 3D geometry is hierarchically grouped by either attachment or symmetric relationships;
	- **GRASS**. Jun Li, Kai Xu, Siddhartha Chaudhuri, Ersin Yumer, Hao Zhang, Leonidas Guibas. GRASS: Generative Recursive Autoencoders for Shape Structures. SIGGRAPH 2017
		- Regularity/symmetry;
		- https://github.com/kevin-kaixu/grass_pytorch
	- Chengjie Niu, Jun Li, Kai Xu. Im2Struct: Recovering 3D Shape Structure from a Single RGB Image. CVPR'18
	- **SCORES**: Chenyang Zhu, Kai Xu, Siddhartha Chaudhuri, Renjiao Yi, Hao Zhang. SCORES: Shape Composition with Recursive Substructure Priors. SIGGRAPH Asia'18
	- **StructureNet**: Kaichun Mo, Paul Guerrero, Li Yi, Hao Su, Peter Wonka, Niloy Mitra, Leonidas J. Guibas. StructureNet: Hierarchical Graph Networks for 3D Shape Generation. 2019
	- **GRAINS**: Manyi Li, Akshay Gadi Patil, Kai Xu, Siddhartha Chaudhuri, Owais Khan, Ariel Shamir, ChangheTu, Baoquan Chen, Daniel Cohen-Or, and Hao Zhang. GRAINS: Generative recursive autoencoders for indoor scenes. TOG'19
	- **StructEdit**: Kaichun Mo, Paul Guerrero, Li Yi, Hao Su, Peter Wonka, Niloy J. Mitra, Leonidas Guibas. StructEdit: Learning Structural Shape Variations. 2019
	- **GNN**: Kai Wang, Yu-an Lin, Ben Weissmann, Manolis Savva, Angel X. Chang, and Daniel Ritchie. PlanIT: Planning and Instantiating Indoor Scenes with Relation Graph and Spatial Prior Networks. SIGGRAPH'19
	- Despoina Paschalidou, Luc Gool, and Andreas Geiger. Learning unsupervised hierarchical part decomposition of 3d objects from a single rgb image. CVPR'20
		- https://github.com/paschalidoud/hierarchical_primitives
		- 3 Networks:
			- Partition network: binary partition, each part with feature;
			- Structure network: inside/outside assignment;
			- Geometry network: superquadratics fitting;
- **CSG**:
	- CSG-Tres: James D Foley, Foley Dan Van, Andries Van Dam, Steven K Feiner, John F Hughes, J Hughes, and Edward Angel. Computer graphics: principles and practice. 1996
	- **CSGNet**: Gopal Sharma, Rishabh Goyal, Difan Liu, Evangelos Kalogerakis, Subhransu Maji. CSGNet: Neural Shape Parser for Constructive Solid Geometry. CVPR'18
- **Chart**: Heli Ben-Hamu, Haggai Maron, Itay Kezurer, Gal Avineri, and Yaron Lipman. Multi-chart generative surface modeling. TOG'18
- Despoina Paschalidou, Ali Osman Ulusoy, and Andreas Geiger. Superquadrics revisited: Learning 3d shape parsing beyond cuboids. CVPR'19
- Lin Gao, Jie Yang, Tong Wu, Yu-Jie Yuan, Hongbo Fu, Yu-Kun Lai, and Hao(Richard) Zhang. SDM-NET: Deep generative network for structured deformable mesh. TOG'19
- **SIF**: Kyle Genova, Forrester Cole, Daniel Vlasic, Aaron Sarna, William T Freeman, and Thomas Funkhouser. Learning shape templates with structured implicit functions. ICCV'19
- Latest:
	- Zerong Zheng, Tao Yu, Qionghai Dai, Yebin Liu. Deep Implicit Templates for 3D Shape Representation. CVPR'21

## 5. Implicit Functions (N-SDF)
- Legacy:
	- B. Curless and M. Levoy. A volumetric method for building complex models from range images. SIGGRAPH'96
	- **RBF**: Jonathan C. Carr, Richard K. Beatson, Jon B. Cherrie, Tim J. Mitchell, W. Richard Fright, Bruce C. McCallum, and Tim R. Evans. Reconstruction and representation of 3d objects with radial basis functions. SIGGRAPH'01
	- Greg Turk and James F. O’Brien. Modelling with implicit surfaces that interpolate. TOG'02
	- **Unity implicits**: Yutaka Ohtake, Alexander Belyaev, Marc Alexa, Greg Turk, and Hans-Peter Seidel. Multi-level partition of unity implicits, volume 22. ACM, 2003
	- Chen Shen, James F. O'Brien, and Jonathan Richard Shewchuk. Interpolating and approximating implicit surfaces from polygon soup. TOG'04
- Render for implicit models:
	- Marching Cube;
	- John C. Hart. Sphere tracing: A geometric method for the antialiased ray tracing of implicit surfaces. 1996
	- **Surface-Finding**: Sarah F. Frisken, Ronald N. Perry, Alyn P. Rockwood, and Thouis R. Jones. Adaptively sampled distance fields: A general representation of shape for computer graphics. 2000
- Zhiqin Chen and Hao Zhang. Learning implicit fields for generative shape modeling. CVPR'19
- Generalized Neural-SDF:
	- **OccNet**: Lars Mescheder, Michael Oechsle, Michael Niemeyer, Sebastian 
	Nowozin, and Andreas Geiger. Occupancy networks: Learning 3d reconstruction in function space. CVPR'19
		- Insight: new 3D representation, could generate mesh at any resoltuion;
		- https://github.com/autonomousvision/occupancy_networks
		- Input image; output: **continuous decision boundary of a deep-NN**;
		- Learn an occupancy function: R3 to [0,1];
		- Surface at inference time: Multiresolution IsoSurface Extraction (MISE) or Marching Cube;
- **DeepSDF**: Jeong Joon Park, Peter Florence, Julian Straub, Richard Newcombe, and Steven Lovegrove. DeepSDF: Learning continuous signed distance functions for shape representation. CVPR'19
	- Insight: point-based SDF;
	- https://github.com/facebookresearch/DeepSDF
	- Formulation: given a point x, a NN with latent code z as a classifier \
		<img src="/CV-3D/images/3d_output/deepsdf-1.png" alt="drawing" width="350"/>
	- Autoencoder: \
		<img src="/CV-3D/images/3d_output/deepsdf-2.png" alt="drawing" width="400"/>
	- Auto-decoder (encoder-less) training and inference: \
		<img src="/CV-3D/images/3d_output/deepsdf-3.png" alt="drawing" width="400"/>
		<img src="/CV-3D/images/3d_output/deepsdf-4.png" alt="drawing" width="400"/>
- **DISN**: Qiangeng Xu, Weiyue Wang, Duygu Ceylan, Radomir Mech, and Ulrich Neumann. Disn: Deep implicit surface network for high-quality single-view 3d reconstruction. 2019
- **DSIF**: Kyle Genova, Forrester Cole, Avneesh Sud, Aaron Sarna, and Thomas A. Funkhouser. Deep structured implicit functions. CoRR, abs/1912.06126, 2019
- **Pifu**: Shunsuke Saito, , Zeng Huang, Ryota Natsume, Shigeo Morishima, Angjoo Kanazawa, and Hao Li. Pifu: Pixel-aligned implicit function for high-resolution clothed human digitization. ICCV'19
- **PIFuHD**: Shunsuke Saito, Tomas Simon, Jason Saragih, and Hanbyul Joo. PIFuHD: Multi-level pixel-aligned implicit function for high-resolution 3D human digitization. CVPR'20
- Michael Niemeyer, Lars M. Mescheder, Michael Oechsle, and Andreas Geiger. Occupancy flow: 4d reconstruction by learning particle dynamics. ICCV'19
- Boyang Deng, Kyle Genova, Soroosh Yazdani, Sofien Bouaziz, Geoffrey Hinton, Andrea Tagliasacchi. CvxNet: Learnable Convex Decomposition. 2020
- Amos Gropp, Lior Yariv, Niv Haim, Matan Atzmon, and Yaron Lipman. Implicit geometric regularization for learning shapes. CoRR'20
- Yueqi Duan, Haidong Zhu, He Wang, Li Yi, Ram Nevatia, and Leonidas J. Guibas. Curriculum deepsdf, 2020
- Yu Deng, Jiaolong Yang, and Xin Tong. Deformed implicit field: Modeling 3d shapes with learned dense correspondence, 2020
	- Can do matching!
- Chiyu Max Jiang, Avneesh Sud, Ameesh Makadia, Jingwei Huang, Matthias Nießner, and Thomas A. Funkhouser. Local implicit grid representations for 3d scenes. 2020
- Zekun Hao, Hadar Averbuch-Elor, Noah Snavely, and Serge Belongie. Dualsdf: Semantic shape manipulation using a two-level representation. arXiv, 2020.
- Rohan Chabra, Jan Eric Lenssen, Eddy Ilg, Tanner Schmidt, Julian Straub, Steven Lovegrove, and Richard Newcombe. Deep local shapes: Learning local SDF priors for detailed 3d reconstruction. CoRR'20
- Thomas Davies, Derek Nowrouzezahrai, and Alec Jacobson. On the effectiveness of weight-encoded neural implicit 3D shapes. arxiv'20
- **BSPNet**: Zhiqin Chen, Andrea Tagliasacchi, and Hao Zhang. BSPNet: Generating compact meshes via binary space partitioning. CVPR'20
- Michael Niemeyer, Lars Mescheder, Michael Oechsle, and Andreas Geiger. Differentiable volumetric rendering: Learning implicit 3D representations without 3D supervision. CVPR'20
- Saurabh Singh, Danhang Danny Tang, Phil Chou, Christian Haene, Mingsong Dou, Sean Fanello, Jonathan Taylor, Onur Gonen Guleryuz, Yinda Zhang, Shahram Izadi, Andrea Tagliasacchi, Sofien Bouaziz, and Cem Keskin. Deep implicit volume compression. CVPR'20
- Edgar Tretschk, Ayush Tewari, Vladislav Golyanik, Michael Zollhöfer, Carsten Stoll, and Christian Theobalt. PatchNets: Patch-Based Generalizable Deep Implicit 3D Shape Representations. ECCV'20
- Feng Liu and Xiaoming Liu. Learning implicit functions for topology-varying dense 3d shape correspondence. NeurIPS'20
- Matthew Tancik, Pratul P. Srinivasan, Ben Mildenhall, Sara Fridovich-Keil, Nithin Raghavan, Utkarsh Singhal, Ravi Ramamoorthi, Jonathan T. Barron, and Ren Ng. Fourier features let networks learn high frequency functions in low dimensional domains. NeurIPS'20
- Latest:
	- Despoina Paschalidou, Angelos Katharopoulos, Andreas Geiger, Sanja Fidler. Neural Parts: Learning Expressive 3D Shape Abstractions With Invertible Neural Networks. CVPR'21
	- Wang Yifan, Shihao Wu, Cengiz Öztireli, Olga Sorkine-Hornung. Iso-Points: Optimizing Neural Implicit Surfaces With Hybrid Representations. CVPR'21
	- Moritz Ibing, Isaak Lim, Leif Kobbelt. 3D Shape Generation With Grid-Based Implicit Functions. CVPR'21

## 2.5D, Depth, Skeleton, 3D-Aware 2D Cues...
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
- Wilfried Hartmann, Silvano Galliani, Michal Havlena, Luc Van Gool, and Konrad Schindler. Learned multi-patch similarity. ICCV'17
- **ShapeHD**: J. Wu, C. Zhang, X. Zhang, Z. Zhang, W. T. Freeman, and J. B. Tenenbaum. Learning shape priors for single-view 3D completion and reconstruction. ECCV'18
	- Key insigth: improve on MarrNet with naturalness (pretrained discriminator) to solve ambiguity, with Wasserstein-GAN loss;
	- https://github.com/xiumingzhang/GenRe-ShapeHD
	- Input: single view; Output: 3D voxel completion/reconstruction; \
	<img src="/CV-3D/images/3d_output/shapehd.png" alt="drawing" width="600"/>
- Simon Donne and Andreas Geiger. Learningnon-volumetric depth fusion using successive reprojections. CVPR'19