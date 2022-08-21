# Parts/Primitives

## Unclassified
- A. Jain, T. Thormahlen, T. Ritschel, and H.-P. Seidel. Exploring shape variations by 3d-model decomposition and part-based recombination. CGF'12
- Haibin Huang, Evangelos Kalogerakis, Benjamin Marlin. Analysis and synthesis of 3D shape families via deep-learned generative models of surfaces. Eurographics 2015
- Siddhartha Chaudhuri, Daniel Ritchie, Jiajun Wu, Kai Xu, and Hao Zhang. Learning to generate 3D structure. Eurographics State-of-the-Art Reports (STAR), 2020.

## Legacy
- L. G. Roberts. Machine perception of three-dimensional solids. PhD thesis, Massachusetts Institute of Technology, 1963
- Donald D Hoffman and Whitman A Richards. Parts of recognition. Cognition, 18(1-3):65–96, 1984
- Alex Pentland. Parts: Structured descriptions of shape. AAAI'86
- **geon**: I. Biederman. Recognition-by-components: a theory of human image understanding. Psychological review, 94(2):115, 1987
- R. Schnabel, P. Degener, and R. Klein. Completion and reconstruction with primitive shapes. CGF/Eurographics'09
	- Problem: completion and reconstruction;
	- primitives as guidance, energy-based optimization;

## Ransac and fitting (Legacy)
- Attene, M., Falcidieno, B., Spagnuolo, M.: Hierarchical mesh segmentation based on fitting primitives. VC'06
- R. Schnabel, R. Wahl, and R. Klein. Efficient ransac for point-cloud shape detection. CGF'07
- **Fitting**: Narunas Vaskevicius and Andreas Birk. Revisiting superquadric fitting: A numerically stable formulation. PAMI'17
- **Globfit**: Yangyan Li, Xiaokun Wu, Yiorgos Chrysanthou, Andrei Sharf, Daniel Cohen-Or, and Niloy J. Mitra. Globfit: consistently fitting primitives by discovering global relations. TOG'11
- Adrien Kaiser, José Alonso Ybáñez Zepeda, and Tamy Boubekeur. A survey of simple geometric primitives detection methods for captured 3d data. CGF'19
	- Primitives:
		- Size, orientation, position, convex, symmetric, assembles;
		- Primitives: planes, cuboids/boxes, spheres/cylinders/cones, ellipsoids/tori/...
	- Approaches: Ransac, Hough Transform, Clustering; (region growing, ...), Assembling Primitives;

## Cosegmentation: cross-shape consistency
- A. Golovinskiy and T. Funkhouser. Learning Consistent Segmentation of 3D Models. CG'09
	- Problem: segment a set of models;
	- Energy based: a graph, similar parts **across shapes** should have consistent assignment;
- Qi-Xing Huang, Vladlen Koltun, and Leonidas J. Guibas. Joint-Shape Segmentation with Linear Programming. TOG'11
	- Unsupervised cosegmentation;
	- Stage 1: initial segment on each shape; (superpixels or clustering)
	- Stage 2: pairwise segmentation: energy-based, seg(S1)+seg(S2)+consistency(S1, S2);
	- Stage 3: multiway joint segmentation;
- R. Hu, L. Fan, and L. Liu. Co-segmentation of 3D shapes via subspace clustering. CGF'12
- Mehmet Ersin Yümer and Levent Burak Kara. Co-abstraction of shape collections. TOG'12
	- Problem definition: abstract (lower-res) of a set of shapes;
- Y. Wang, S. Asafi, O. Van Kaick, H. Zhang, D. Cohen-Or, and B. Chen. Active co-analysis of a set of shapes. TOG 2012
- Vladimir G. Kim, Wilmot Li, Niloy J. Mitra, Siddhartha Chaudhuri, Stephen DiVerdi, and Thomas A. Funkhouser. Learning part-based templates from large collections of 3d shapes. TOG'13
	- Task: given a template with gt segmentation labels, segment other shapes;
	- Jointly solving for model deformations, part segmentation, and inter-model correspondence;
	- 1. if no template provided, create auto template;
	- 2. Fit each shape with each template;
	- 3. Refine template;
- R. Hu, O. van Kaick, B. Wu, H. Huang, A. Shamir, and H. Zhang. Learning how objects function via co-analysis of interactions. TOG 2016
- Li Yi, Haibin Huang, Difan Liu, Evangelos Kalogerakis, Hao Su, Leonidas Guibas. Deep Part Induction from Articulated Object Pairs. SIGGRAPH Asia'18
	- https://github.com/ericyi/articulated-part-induction
- M. Sung, H. Su, R. Yu, and L. Guibas. Deep functional dictionaries: Learning consistent semantic structures on 3D models from functions. NeurIPS'18
	- Input n points; output: n x k dictionary; weak annotation (inconsistent/unnamed annotation);
	- Structured sparsity;
	- https://github.com/mhsung/deep-functional-dictionaries
	- Different deep dictionaries;
	- Applications with adaptation in co-segmentation, keypoint correspondence, smooth functional approximation (modeled as constraint);
	- Given an input X, At = A(X; theta) to get basis
	- Solve x = argmin||At x - f||^2 s.t. C(x)
	- Update theta = theta - eta * d L(A(X, theta); f, x) / dx
- **BAE-Net**: Zhiqin Chen, Kangxue Yin, Matthew Fisher, Siddhartha Chaudhuri, and Hao Zhang. BAE-Net: Branched autoencoder for shape co-segmentation. CVPR'19
	- https://github.com/czq142857/BAE-NET
	- Task: unsupervised co-segmentation;

## Unsupervised part discovery
- Li Yi, Haibin Huang, Difan Liu, Evangelos Kalogerakis, Hao Su, Leonidas Guibas. Deep Part Induction from Articulated Object Pairs. SIGGRAPH Asia 2018
	- Deep Matching (Point Net)
	- Motion Discovery, Part Co-segmentation
- Shubham Tulsiani, Hao Su, Leonidas J. Guibas, Alexei A. Efros, Jitendra Malik. Learning Shape Abstractions by Assembling Volumetric Primitives. CVPR'17
	- Supervision: unsupervised, reconstruction loss;
	- Each part (z, q, t): z, shape; q rotation; t translation;
	- REINFORCE; parsimony reward for fewer parts;
	- Experiment: ShapeNet, 32x32x32, ADAM;
- **CSGNet**: Gopal Sharma, Rishabh Goyal, Difan Liu, Evangelos Kalogerakis, Subhransu Maji. CSGNet: Neural Shape Parser for Constructive Solid Geometry. CVPR'18
	- https://github.com/hippogriff/CSGNet
- Yonglong Tian, Andrew Luo, Xingyuan Sun, Kevin Ellis, William T. Freeman, Joshua B. Tenenbaum, Jiajun Wu. Learning to Infer and Execute 3D Shape Programs. ICLR'19
	- http://shape2prog.csail.mit.edu/
	- https://github.com/HobbitLong/shape2prog
	- Problem setup: input voxels; output programs;
	- Program generator: Block-LSTM + step-LSTM;
	- Program executor: NPI at block-level, trained with large amount of synthetic;
	- Supervision: reconstruction;
	- Key 1: program generator needed a lot of pretrain on large synthetic (block-level LSTM); manually designed program to generate, 
	- Key 2: executor trained on part-level separately; to make generator-executor differentiable;
	- Key 3: the domain gap between the synthetic and ShapeNet is still large;
- **Superquadrics**: Despoina Paschalidou, Ali Osman Ulusoy, and Andreas Geiger. Superquadrics revisited: Learning 3d shape parsing beyond cuboids. CVPR'19
	- https://github.com/paschalidoud/superquadric_parsing
- **AtlasNetV2**: Theo Deprelle, Thibault Groueix, Matthew Fisher, Vladimir Kim, Bryan Russell, and Mathieu Aubry. Learning elementary structures for 3d shape generation and matching. NeurIPS'19
	- https://github.com/TheoDEPRELLE/AtlasNetV2
	- Assume all 3D data similar to a common template (also a.k.a. elemental structures);
		- Assume each shape made up of elem-struct E1, E2, ... with shape-dependent adjustment modules p1, p2, ...;
		- **if E1, E2, ... are squares or sphere: AtlasNet**
		- **if an instance shape Z as elem-struct: 3D-CODED**
	- Initial template from sampling on surface;
	- Learn to MLP-mapping or translate;
	- Supervision:
		- Correspondence error if gt deformation available and all points aligned;
		- otherwise CD;
- **Neural Parts**: Despoina Paschalidou, Angelos Katharopoulos, Andreas Geiger, Sanja Fidler. Neural Parts: Learning Expressive 3D Shape Abstractions With Invertible Neural Networks. CVPR'21
	- https://paschalidoud.github.io/neural_parts
	- https://github.com/paschalidoud/neural_parts
	- Task: input image + 3D mesh, output a part template;
	- each part: a learned homeomorphism learned by INN;
	- Insight: part emerge without labels, temporal consistency;
- Fenggen Yu, Zhiqin Chen, Manyi Li, Aditya Sanghi, Hooman Shayani, Ali Mahdavi-Amiri, Hao Zhang. CAPRI-Net: Learning Compact CAD Shapes with Adaptive Primitive Assembly. 2021

## Supervised
- Generative: given shapes with part labels, learn space to sample new shapes;
	- Charlie Nash and Chris KI Williams. The shape variational autoencoder: A deep generative model of part-segmented 3d objects. CGF'17, SGP'17
		- Task: given shapes with part labels, learn latent z;
	- Hao Wang, Nadav Schor, Ruizhen Hu, Haibin Huang, Daniel Cohen-Or, and Hui Huang. Global-to-local generative model for 3d shapes. SIGGRAPH Asia'18
	- **SDM-NET**: Lin Gao, Jie Yang, Tong Wu, Yu-Jie Yuan, Hongbo Fu, Yu-Kun Lai, and Hao(Richard) Zhang. SDM-NET: Deep generative network for structured deformable mesh. TOG'19
		- http://geometrylearning.com/sdm-net/
		- http://geometrylearning.com/sdm-net/file/sdm-code.zip
		- Two level:
			- Part level: part VAE;
			- Structure level: SP VAE; concatenate part feature in a consistent order; decode as part;
	- Rundi Wu, Yixin Zhuang, Kai Xu, Hao Zhang, and Baoquan Chen. PQ-NET: A generative part seq2seq network for 3D shapes. CVPR'20
		- https://github.com/ChrisWu1997/PQ-NET
		- Sequentially, one part at a time by GRU;
- Compose/Assembly/Placement:
	- Siddhartha Chaudhuri, Evangelos Kalogerakis, Leonidas Guibas, and Vladlen Koltun. Probabilistic reasoning for assembly-based 3d modeling. TOG'11
		- Bayesian Network with a library of things;
	- Kalogerakis, E., Chaudhuri, S., Koller, D., Koltun, V.: A probabilistic model for component-based shape synthesis. TOG'12
	- Zheng, Y., Cohen-Or, D., Averkiou, M., Mitra, N.J.: Recurring part arrangements in shape collections. CGF'14
	- Anastasia Dubrovina, Fei Xia, Panos Achlioptas, Mira Shalah, Raphael Groscot, Leonidas Guibas. Composite Shape Modeling via Latent Space Factorization. ICCV'19
		- Input: 3D;
		- Output: editable object by manipulating semantic space;
		- Backbone:
			- Input 3D voxel -> 3D-CNN -> partition unity to 1;
			- Each part feature -> decoder -> STN -> obj;
	- **CompoNet**: Nadav Schor, Oren Katzir, Hao Zhang, and Daniel Cohen-Or. CompoNet: Learning to generate the unseen by part synthesis and composition. ICCV'19
		- https://github.com/nschor/CompoNet
		- Model:
			- Part synthesis unit: VAE for each part separately;
			- Part composition unit: compose the part;
	- Jialei Huang, Guanqi Zhan, Qingnan Fan, Kaichun Mo, Lin Shao, Baoquan Chen, Leonidas J. Guibas, Hao Dong. Generative 3D Part Assembly via Dynamic Graph Learning. NeurIPS'20
		- https://hyperplane-lab.github.io/Generative-3D-Part-Assembly/
		- https://github.com/hyperplane-lab/Generative-3D-Part-Assembly
		- Task: given part point cloud, predict assembly;
		- GNN for relation reasoning, pooling for equivalent parts (4 legs)...
- **3d-prnn**: Chuhang Zou, Ersin Yumer, Jimei Yang, Duygu Ceylan,and Derek Hoiem. 3d-prnn: Generating shape primitives with recurrent neural networks. ICCV'17
	- https://github.com/zouchuhang/3D-PRNN
- **SFPN**: Lingxiao Li, Minhyuk Sung, Anastasia Dubrovina, Li Yi, and Leonidas J. Guibas. Supervised fitting of geometric primitives to 3d point clouds. CVPR'19
	- Input: N x 3 point clouds; output: K (24 at maximum) primitives, (4 types: plane, cylinder, sphere, cone);
	- Key 1: membership reordering with Hungarian Matching;
	- Key 2: make RANSAC and Least-Square differentiable; separate models for each primitive;
- **Sagnet**: Zhijie Wu, Xiang Wang, Di Lin, Dani Lischinski, Daniel Cohen-Or, and Hui Huang. Sagnet: Structure-aware generative network for 3d-shape modeling. SIGGRAPH'19
	- https://github.com/zhijieW94/SAGNet
	- Model:
		- k voxel maps;
		- K pairwise relationship;
		- GRU (RNN)
	- Training:
		- First phase: 2-way VAE for reconstruction loss;

## Hierarchical/Recursive/Graph/Scene-graph
- James D Foley, Foley Dan Van, Andries Van Dam, Steven K Feiner, John F Hughes, J Hughes, and Edward Angel. Computer graphics: principles and practice. 1996
- Yanzhen Wang, Kai Xu, Jun Li, Hao Zhang, Ariel Shamir, Ligang Liu, Zhi-Quan Cheng, and Yueshan Xiong. Symmetry Hierarchy of Man-Made Objects. CGF'11
	- Symmetry hierarchy: 3D geometry is hierarchically grouped by either attachment or symmetric relationships;
- Recursive NN:
	- **GRASS**. Jun Li, Kai Xu, Siddhartha Chaudhuri, Ersin Yumer, Hao Zhang, Leonidas Guibas. GRASS: Generative Recursive Autoencoders for Shape Structures. SIGGRAPH 2017
		- Regularity/symmetry;
		- https://github.com/kevin-kaixu/grass_pytorch
	- **Im2Struct**: Chengjie Niu, Jun Li, Kai Xu. Im2Struct: Recovering 3D Shape Structure from a Single RGB Image. CVPR'18
		- https://github.com/chengjieniu/Im2Struct
		- Recursive NN to iteratively predict primitives;
	- **SCORES**: Chenyang Zhu, Kai Xu, Siddhartha Chaudhuri, Renjiao Yi, Hao Zhang. SCORES: Shape Composition with Recursive Substructure Priors. SIGGRAPH Asia'18
		- https://github.com/BigkoalaZhu/SCORES
		- Problem setup: input two source shapes a,b, rough placement c; output optimized structure d;
	- **GRAINS**: Manyi Li, Akshay Gadi Patil, Kai Xu, Siddhartha Chaudhuri, Owais Khan, Ariel Shamir, ChangheTu, Baoquan Chen, Daniel Cohen-Or, and Hao Zhang. GRAINS: Generative recursive autoencoders for indoor scenes. TOG'19
		- https://github.com/ManyiLi12345/GRAINS
		- Tree-VAE;
- GNN:
	- **StructureNet**: Kaichun Mo, Paul Guerrero, Li Yi, Hao Su, Peter Wonka, Niloy Mitra, Leonidas J. Guibas. StructureNet: Hierarchical Graph Networks for 3D Shape Generation. SIGGRPAH Asia'19
		- Train a graph-VAE s.t. graph -> z -> graph
		- Embed image/3d to same space as z;
	- **StructEdit**: Kaichun Mo, Paul Guerrero, Li Yi, Hao Su, Peter Wonka, Niloy J. Mitra, Leonidas Guibas. StructEdit: Learning Structural Shape Variations. 2019
		- https://github.com/daerduoCarey/structedit
		- Problem setup: 3D shape analogy; Source Si, target Sj;
		- Insight: extension of StructureNet;
	- Kai Wang, Yu-an Lin, Ben Weissmann, Manolis Savva, Angel X. Chang, and Daniel Ritchie. PlanIT: Planning and Instantiating Indoor Scenes with Relation Graph and Spatial Prior Networks. SIGGRAPH'19
		- https://github.com/brownvc/planit
		- GNN: edge defined by spatial locality of each indoor scene obj;
		- Sequential generative model: Predict one new obj at a time;
	- **DSM-Net**: Jie Yang, Kaichun Mo, Yu-Kun Lai, Leonidas J. Guibas, and Lin Gao. DSM-Net: Disentangled structured mesh net for controllable generation of fine geometry, 2020.
		- http://geometrylearning.com/dsg-net/
		- Graph-VAE;
- Despoina Paschalidou, Luc Gool, and Andreas Geiger. Learning unsupervised hierarchical part decomposition of 3d objects from a single rgb image. CVPR'20
	- https://github.com/paschalidoud/hierarchical_primitives
	- 3 Networks:
		- Partition network: **binary** partition, each part with feature;
		- Structure network: inside/outside assignment;
		- Geometry network: superquadratics fitting;

## Applications:
- Siddhartha Chaudhuri and Vladlen Koltun. Data-driven suggestions for creativity support in 3d modeling. ACM SIGGRAPH Asia'10
	- Given a query simple shape, suggest creativity (interactive generative model)
	- Fast match by signature;
	- Search and suggest parts with low correspondence;
- Functionality:
	- R. Hu, W. Li, O. Van Kaick, A. Shamir, H. Zhang, and H. Huang. Learning to predict part mobility from a single static snapshot. TOG 2017
	- R. Hu, Z. Yan, J. Zhang, O. van Kaick, A. Shamir, H. Zhang, and H. Huang. Predictive and generative neural networks for object functionality. CGF 2018
- Physics:
	- Yilun Du, Zhijian Liu, Hector Basevi, Aleš Leonardis, William T. Freeman, Joshua B. Tenenbaum, Jiajun Wu. Learning to Exploit Stability for 3D Scene Parsing. NIPS'18

## Procedural:
- **CSG**:
	- CSG-Trees: James D Foley, Foley Dan Van, Andries Van Dam, Steven K Feiner, John F Hughes, J Hughes, and Edward Angel. Computer graphics: principles and practice. 1996

## **Chart**: Heli Ben-Hamu, Haggai Maron, Itay Kezurer, Gal Avineri, and Yaron Lipman. Multi-chart generative surface modeling. TOG'18
