# Parts/Primitives

## Problem Setup
- Cosegmentation/part/dictionary: always unsupervised;
	- Segment a set of models consistently; (fully unsup)
	- Given segmentation of a reference model, segment other shape; (low shot)
- Supervised:
	- Known templates (with parts)
- Fitting of each part (differentiable or non-)
- Assembly: given each part, predict placement;
- Part representation;
- Tutorials:
	- Hao Su: http://cseweb.ucsd.edu/~haosu/slides/PartInduction.pdf
		- Part: Descriptive; Concise; Interpretable
		- Supervision:
			- Unsupervised: Shape-Abstract (Shubham), CSGNet;
			- Weak-supervised: deep-functional-dictionaries (Sung);
			- SSL: deep-part-induction (Yi Li);

## Unclassified
- Z Liu, W Freeman, J Tenenbaum, and J Wu. Physical Primitive Decomposition. ECCV'18

## Legacy
- Ideas legacy;
	- L Roberts. Machine perception of three-dimensional solids. PhD thesis, MIT, 1963
	- D Hoffman and W Richards. Parts of recognition. Cognition, 18(1-3):65–96, 1984
	- A Pentland. Parts: Structured descriptions of shape. AAAI'86
	- **geon**: I. Biederman. Recognition-by-components: a theory of human image understanding. Psychological review, 94(2):115, 1987
- R. Schnabel, P. Degener, and R. Klein. Completion and reconstruction with primitive shapes. CGF/Eurographics'09
	- Problem: completion and reconstruction;
	- primitives as guidance, energy-based optimization;

## Ransac and fitting (Legacy)
- Attene, M., Falcidieno, B., Spagnuolo, M.: Hierarchical mesh segmentation based on fitting primitives. VC'06
- R. Schnabel, R. Wahl, and R. Klein. Efficient ransac for point-cloud shape detection. CGF'07
- **Globfit**: Y Li, X Wu, Y Chrysanthou, A Sharf, D Cohen-Or, and Niloy J. Mitra. Globfit: consistently fitting primitives by discovering global relations. TOG'11
- **Fitting**: N Vaskevicius and A Birk. Revisiting superquadric fitting: A numerically stable formulation. PAMI'17
- A Kaiser, J Zepeda, and T Boubekeur. A survey of simple geometric primitives detection methods for captured 3d data. CGF'19
	- Primitives:
		- Size, orientation, position, convex, symmetric, assembles;
		- Primitives: planes, cuboids/boxes, spheres/cylinders/cones, ellipsoids/tori/...
	- Approaches: Ransac, Hough Transform, Clustering; (region growing, ...), Assembling Primitives;

## Backbone
- Framework: decompose into part, then compose together;
	- Non-DL: Non-DL graphical models
		- 1. proposals as graph nodes: superpixels, clusters, ...;
		- 2. energy-based pgm: energy-based, cross-shape consisstency; (**template** prior from reference shape, or manual set, or learned)
			- Unary: template fitting of each segment;
		- 3. Joint seg, post processing;
	- DL: BAE-Net;
	- PlaneRCNN: C Liu, K Kim, J Gu, Y Furukawa, J Kautz. PlaneRCNN: 3D Plane Detection and Reconstruction from a Single Image. CVPR'19
- Framework: Active learning:
	- L Yi, L. Guibas. A Scalable Active Framework for Region Annotation in 3D Shape Collections. SIGGRAPH Asia'16
		- Select annotation set;
		- Annotate (human);
		- Propagate labels to other shapes;
		- Select verification set;
- MLP:
	- H Huang, E Kalogerakis, B Marlin. Analysis and synthesis of 3D shape families via deep-learned generative models of surfaces. EG'15
	- S Tulsiani, H Su, L Guibas, A Efros, J Malik. Learning Shape Abstractions by Assembling Volumetric Primitives. CVPR'17
	- AtlasNetV2, NeurIPS'19;
	- SFPN. Li Yi. CVPR'19
- PointNet/set:
	- L Yi, H Huang, D Liu, E Kalogerakis, H Su, L Guibas. Deep Part Induction from Articulated Object Pairs. SIGGRAPH Asia'18
		- https://github.com/ericyi/articulated-part-induction
		- 1. Seg+feat: Shape s1, s2 -> PointNet++ -> f1, f2;
		- 2. Proposal: pairwise feature similarity;
		- 3. Flow-model: pairwise -> PointNet++ -> deformation flow;
	- M. Sung, H. Su, R. Yu, and L. Guibas. Deep functional dictionaries: Learning consistent semantic structures on 3D models from functions. NeurIPS'18
		- https://github.com/mhsung/deep-functional-dictionaries
		- Input pc X to basis: At = A(X; θ)
		- Solve fitting: x = argmin||A'x - f||^2 s.t. C(x)
		- Update θ = θ - η ∂L(A(X, θ); f, x)/∂x
- Conv:
	- **BAE-Net**: Z Chen, K Yin, M Fisher, S Chaudhuri, and H Zhang. BAE-Net: Branched autoencoder for shape co-segmentation. CVPR'19
		- https://github.com/czq142857/BAE-NET
	- SDMNet. Gao Lin, Hao Zhang. TOG'19
	- TM-NET: Deep Generative Networks for Textured Meshes.
		- Extend SDMNet:
			- Each part = geometry + textured mesh
			- Textured mesh: uv coord + AutoRegressive PixelSNAIL;
- Conv + RNN/LSTM/GRU:
	- **3d-prnn**: C Zou, D Hoiem. ICCV'17
	- CSGNet. Gopal Sharma. CVPR'18
	- Y Tian, A Luo, X Sun, K Ellis, W Freeman, J Tenenbaum, J Wu. Learning to Infer and Execute 3D Shape Programs. ICLR'19
		- Require a lot of pretrain;
	- PQ-NET: Hao Zhang. CVPR'20
		- https://github.com/ChrisWu1997/PQ-NET
- Hierarchical/Recursive: (recursively predict part)
	- J Foley, F D Van, A Dam, S Feiner, J Hughes, J Hughes, and E Angel. Computer graphics: principles and practice. 1996
	- Y Wang, K Xu, J Li, H Zhang, A Shamir, L Liu, Z Cheng, and Y Xiong. Symmetry Hierarchy of Man-Made Objects. CGF'11
	- GRASS. J. Li, L. Guibas. SIGGRAPH'17
	- **Im2Struct**: C Niu, J Li, K Xu. CVPR'18
		- https://github.com/chengjieniu/Im2Struct
		- Recursive NN to iteratively predict primitives;
	- Scores: H. Zhang. SIGGRAPH Asia'18
	- GRAINS: H. Zhang. TOG'19
	- H-Primitives: D Paschalidou, L Gool, and A Geiger. CVPR'20
		- https://github.com/paschalidoud/hierarchical_primitives
		- 3 networks: partition + structure + superquadratics fitting;
- GNN:
	- **PlanIT**: Kai Wang, Daniel Ritchie. SIGGRAPH'19
	- **StructureNet**: Kaichun Mo. SIGGRPAH Asia'19
		- Graph-VAE: graph - z - graph; (embed image/3d into the same z space);
	- **StructEdit**: Kaichun Mo, 2019
	- **DSM-Net**: Kaichun Mo. 2020
		- Graph-VAE.
	- S Chaudhuri, D Ritchie, J Wu, K Xu, and H Zhang. Learning to generate 3D structure. EG STAR'20.
- MRF:
	- A. Jain, T. Thormahlen, T. Ritschel, and H.-P. Seidel. Exploring shape variations by 3d-model decomposition and part-based recombination. CGF'12
	- L Yi, L Guibas. Learning Hierarchical Shape Segmentation and Labeling from Online Repositories. SIGGRAPH'17

## Supervision
- Unsupervised part discovery always rely on shape similarity (CD/EMD);
- Supervised will have extra part-assignment loss;
- Part-assignment:
	- SFPN. Li Yi. CVPR'19
- Part-fitting (differentiable for e2e):
	- SFPN. Li Yi. CVPR'19	
- Shape similarity (CD/EMD):
	- Train with REINFORCE [S Tulsiani, CVPR'17]; [CSGNet, CVPR'18]
	- AtlasNetV2
- VAE:
	- SDMNet. Gao Lin, Hao Zhang. TOG'19
		- http://geometrylearning.com/sdm-net/
		- Part-VAE + SP-VAE;
	- GRAINS;
	- StructureNet (Graph-VAE);
	- Part-AE/VAE: a z to encode/decode with each part;
		- C Nash and C Williams. The shape variational autoencoder: A deep generative model of part-segmented 3d objects. CGF'17, SGP'17
		- D Cohen-Or. Global-to-local generative model for 3d shapes. SIGGRAPH Asia'18
- Predict one obj at a time:
	- PlanIT; PQ-Net (Hao Zhang);
- Energy-based PGM (always used together with MRF backbone):
	- A. Golovinskiy and T. Funkhouser. Learning Consistent Segmentation of 3D Models. CG'09
	- Q Huang, V Koltun, and L Guibas. Joint-Shape Segmentation with Linear Programming. TOG'11
	- R. Hu, L. Fan, and L. Liu. Co-segmentation of 3D shapes via subspace clustering. CGF'12
	- E Yümer and L Kara. Co-abstraction of shape collections. TOG'12
	- Y. Wang, S. Asafi, O. Van Kaick, H. Zhang, D. Cohen-Or, and B. Chen. Active co-analysis of a set of shapes. TOG'12
	- V Kim, W Li, Mitra N, S Chaudhuri, S DiVerdi, and T Funkhouser. Learning part-based templates from large collections of 3d shapes. TOG'13
	- R. Hu, O. van Kaick, B. Wu, H. Huang, A. Shamir, and H. Zhang. Learning how objects function via co-analysis of interactions. TOG'16

## Unsupervised part discovery
- L Yi, H Huang, D Liu, E Kalogerakis, H Su, L Guibas. Deep Part Induction from Articulated Object Pairs. SIGGRAPH Asia'18
	- Deep Matching (Point Net)
	- Motion Discovery, Part Co-segmentation
- **Superquadrics**: D Paschalidou, A Ulusoy, and A Geiger. Superquadrics revisited: Learning 3d shape parsing beyond cuboids. CVPR'19
	- https://github.com/paschalidoud/superquadric_parsing
- T Luo, K Mo, Z Huang, J Xu, S Hu, L Wang, H Su. Learning to Group: A Bottom-Up Framework for 3D Part Discovery in Unseen Categories. ICLR'20
- **Neural Parts**: D Paschalidou, A Katharopoulos, A Geiger, S Fidler. Neural Parts: Learning Expressive 3D Shape Abstractions With Invertible Neural Networks. CVPR'21
	- https://paschalidoud.github.io/neural_parts
	- https://github.com/paschalidoud/neural_parts
	- Task: input image + 3D mesh, output a part template;
	- each part: a learned homeomorphism learned by INN;
	- Insight: part emerge without labels, temporal consistency;
- F Yu, Z Chen, M Li, A Sanghi, H Shayani, A Mahdavi-Amiri, H Zhang. CAPRI-Net: Learning Compact CAD Shapes with Adaptive Primitive Assembly. 2021

## Supervised
- Compose/Assembly/Placement:
	- S Chaudhuri, E Kalogerakis, L Guibas, and V Koltun. Probabilistic reasoning for assembly-based 3d modeling. TOG'11
		- Bayesian Network with a library of things;
	- E Kalogerakis, S Chaudhuri, D Koller, V Koltun: A probabilistic model for component-based shape synthesis. TOG'12
	- Zheng, Y., Cohen-Or, D., Averkiou, M., Mitra, N.J.: Recurring part arrangements in shape collections. CGF'14
	- A Dubrovina, F Xia, P Achlioptas, M Shalah, R Groscot, L Guibas. Composite Shape Modeling via Latent Space Factorization. ICCV'19
		- Input: 3D;
		- Output: editable object by manipulating semantic space;
		- Backbone:
			- Input 3D voxel -> 3D-CNN -> partition unity to 1;
			- Each part feature -> decoder -> STN -> obj;
	- **CompoNet**: N Schor, O Katzir, H Zhang, and D Cohen-Or. CompoNet: Learning to generate the unseen by part synthesis and composition. ICCV'19
		- https://github.com/nschor/CompoNet
		- Model:
			- Part synthesis unit: VAE for each part separately;
			- Part composition unit: compose the part;
	- J Huang, G Zhan, Q Fan, K Mo, L Shao, B Chen, L Guibas, H Dong. Generative 3D Part Assembly via Dynamic Graph Learning. NeurIPS'20
		- https://hyperplane-lab.github.io/Generative-3D-Part-Assembly/
		- https://github.com/hyperplane-lab/Generative-3D-Part-Assembly
		- Task: given part point cloud, predict assembly;
		- GNN for relation reasoning, pooling for equivalent parts (4 legs)...
- **Sagnet**: Z Wu, X Wang, D Lin, D Lischinski, D Cohen-Or, and H Huang. Sagnet: Structure-aware generative network for 3d-shape modeling. SIGGRAPH'19
	- https://github.com/zhijieW94/SAGNet
	- Model:
		- k voxel maps;
		- K pairwise relationship;
		- GRU (RNN)
	- Training:
		- First phase: 2-way VAE for reconstruction loss;

## Applications
- S Chaudhuri and V Koltun. Data-driven suggestions for creativity support in 3d modeling. ACM SIGGRAPH Asia'10
	- Given a query simple shape, suggest creativity (interactive generative model)
	- Fast match by signature;
	- Search and suggest parts with low correspondence;
- Functionality:
	- R. Hu, W. Li, O. Van Kaick, A. Shamir, H. Zhang, and H. Huang. Learning to predict part mobility from a single static snapshot. TOG 2017
	- R. Hu, Z. Yan, J. Zhang, O. van Kaick, A. Shamir, H. Zhang, and H. Huang. Predictive and generative neural networks for object functionality. CGF 2018
- Physics:
	- MIT. Learning to Exploit Stability for 3D Scene Parsing. NeurIPS'18

## Procedural
- **CSG**:
	- CSG-Trees: J Foley, F Van, A Dam, S Feiner, J Hughes, J Hughes, and E Angel. Computer graphics: principles and practice. 1996
- **Chart**: H Ben-Hamu, H Maron, I Kezurer, G Avineri, and Y Lipman. Multi-chart generative surface modeling. TOG'18
