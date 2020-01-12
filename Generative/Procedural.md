# Procedural Modeling (PM)

## Brief Overview
- Problem Definition: Generate something with grammars/programs/templates
- Surveys and books:
	- DS Ebert, FK Musgrave, D Peachey, K Perlin, S Worley. Texturing & Modeling, a Procedural Approach, 3rd ed. Elsevier, 2003.
	- Lagae, Ares; Lefebvre, Sylvain; Cook, Rob; DeRose, Tony; Drettakis, George; Ebert, DS; Lewis, JP ; Perlin, Ken ; Zwicker, Matthias. State of the art in procedural noise function. EG'10
	- Ruben M. Smelik, Tim Tutenel, Rafael Bidarra, and Bedrich Benes. 2014. A Survey on Procedural Modelling for Virtual Worlds. Computer Graphics Forum'14\
		<img src = '/Generative/images/pm/survey.png' width = '600'>

## Legacy
- **L-System**: Aristid Lindenmayer. Mathematical models for cellular interactions in development. Journal of theoretical biology 1968
	- First PM paper;
- K Perlin. An image synthesizer. SIGGRAPH'85
- Przemyslaw Prusinkiewicz. Graphical applications of L-systems. In Proceedings of graphics interface. 1986
- Terrain: noise-based, physics-based;
	- Fractal: BB Mandelbrot. The Fractal Geometry of Nature. W. H. Freeman, 1982
		- Height (limitation: can't handle overhangs and caves)
	- FK Musgrave, CE Kolb, RS Mace. The synthesis and rendering of eroded fractal terrains. SIGGRAPH'89
		- Physics-based: Erosion;
	- B Benes, R Forsbach. Layered data representation for visual simulation of terrain erosion. SCCG'01
	- RL Saunders. Terrainosaurus: Realistic Terrain Synthesis Using Genetic Algorithms. 06
		- AI-based? DEM-based
	- A Peytavie, E Galin, J Grosjean. Arches: a framework for modeling complex terrains. CGF'09
- Vegetation, Plant:
	- Problem: individual plant organs, plants, complete plant ecosystems;
	- **L-system**
	- Przemyslaw Prusinkiewicz and Aristid Lindenmayer. The Algorithmic Beauty of Plants. 1990
	- Przemyslaw Prusinkiewicz, Mark James, and Radomir Mech. Synthetic topiary. SIGGRAPH'94
	- Radomir Mech and Przemyslaw Prusinkiewicz. Visual models of plants interacting with their environment. SIGGRAPH'96
	- Michael T. Wong, Douglas E. Zongker, and David H. Salesin. Computer-generated Floral Ornament. SIGGRAPH'98
	- **Xfrog**: D Lintermann, O Deussen. Interactive Modeling of Plants. CGA'99
	- T Ijiri, S Owada, T Igarashi. Seamless integration of initial sketching and subsequent detail editing in flower modeling. CGF'06 
	- S Longay, A Runions, F Boudon, Przemyslaw Prusinkiewicz. Treesketch: Interactive modeling of trees on a tablet. EG'12
	- T Ijiri, S Owada, T Igarashi. The sketch L-System: Global control of tree modeling using free-form strokes. Smart Graphics'06
	- Yotam Livny, Feilong Yan, Matt Olson, Baoquan Chen, Hao Zhang, Jihad El-Sana. Automatic reconstruction of tree skeletal structures from point clouds. TOG'10
	- **SpeedTree**: INTERACTIVE DATA VISUALIZATION , I NC .: SpeedTree. 13
		- http://www.speedtree.com/
	- **plastic trees**: Pirk, Sören; Stava, Ondrej; Kratt, Julian; Massih Said, Michel Abdul; Neubert, Boris; Mech, Randomir; Benes, Bedrich; Deussen, Oliver. Plastic trees: interactive self-adapting botanical tree models. SIGGRAPH'12
- Water bodies: 
	- Problem setup: rivers, lakes, streams, oceans, waterfalls...
- Roads:
	- Problem: in the context of procedural cities;
	- a) user-assisted, where road 3D splines that minimize local elevation changes are fitted in between sketch strokes or control points, or b) based on path finding techniques from AI research, such as A\*
	- **DEM**: E Bruneton, F Neyret. Real-time rendering and editing of vector-based terrains. CGF'08
	- J McCrae, K Singh. Sketch-based path design. GI'09: Proceedings of Graphics Interface 2009
- City:
	- A complex and often hierarchically structured model;
	- PM: typically top-down;
	- Yoav IH Parish and Pascal Muller. Procedural modeling of cities. SIGGRAPH'01
		- An extended Open L-system to grow a road network;
		- The L-system is goal-driven: its goals are population density (roads try to connect population centers) and specific road patterns, for example the raster or the radial pattern;
	- J Sun, X Yu, G Baciu, M Green. Template-based generation of road networks for virtual city modeling. VRST'02
		- Several frequent patterns in real road networks and use them as basic building blocks;
	- T Lechner, B Watson, U Wilensky. Procedural city modeling. Midwestern Graphics Conference'03
		- Not only residential, commercial and industrial areas;
		- But also special areas like government buildings, squares, and monuments
	- G Kelly, H McCabe. A survey of procedural techniques for city generation. ITB'06
	- Sinha, S.N., Steedly, D., Szeliski, R., Agrawala, M., Pollefeys, M. Interactive 3d architectural modeling from unordered photo collections. TOG'08
	- Guoning Chen, Gregory Esch, Peter Wonka, Pascal Mueller, Eugene Zhang. Interactive procedural street modeling. SIGGRAPH'08
		- Interactive modeling method for road networks by the use of tensor field;
	- Xiao, J., Fang, T., Zhao, P., Lhuillier, M., Quan, L. Image-based street-side city modeling. TOG'09
	- Paul Merrell, Eric Schkufza, and Vladlen Koltun. 2010. Computer-generated residential building layouts. TOG'10
	- Pylvanainen, T., Berclaz, J., Korah, T., Hedau, V., Aanjaneya, M., Grzeszczuk, R.: 3d city modeling from street-level data for augmented reality applications. 3DIM/3DPVT'12
	- Inverse: Gen Nishida, Ignacio Garcia-Dorado, Daniel G. Aliaga, Bedrich Benes, Adrien Bousseau. Interactive Sketching of Urban Procedural Models. TOG'16
		- Inverse PM: Our interactive sketching tool allows the user to quickly and easily author procedural 3D building models. The user only performs interactive sketching and our system automatically generates the procedural model and its parameters yielding the sketched shape.
- Buildings:
	- One of the best-developed PM areas
	- **Context-free Split-Grammar**: Peter Wonka, Michael Wimmer, Francois Sillion, and William Ribarsky. 2003. Instant architecture. TOG'03
	- L Yong, XU Congfu, P Zhigeng, P Yunhe. Semantic modeling project: Building vernacular house of southeast china. VRCAI'04
		- create vernacular-style Southeast Chinese houses using an extended shape grammar
	- **CGA**: Pascal Müller, Peter Wonka, Simon Haegler, Andreas Ulmer, Luc Van Gool. Procedural Modeling of Buildings. SIGGRAPH'06
		- CGA: specifically designed for building facades
	- D Finkenzeller, J Bender. Semantic representation of complex building structures. CGV'08
	- D Finkenzeller. Detailed building façades. CGA'08
	- G Patow. User-friendly graph editing for procedural modeling of buildings. CGA'12
	- P Merrell, E Schkufza, V Koltun. Computer-generated residential building layouts. TOG'10
		- **Bayesian Network** for generation;
	- Facade generation: 2D-split grammar;
		- P Müller, G Zeng, P Wonka, L Van Gool. Image-based procedural modeling of facades. SIGGRAPH'07
		- Forward: J Xiao, T Fang, P Tan, P Zhao, E Ofek, Q Long. Image-based facade modeling. TOG'08
		- Inverse: F Bao, M Schwarz, P Wonka. Procedural facade variations from a single layout. TOG'13
		- H Zhang, K Xu, W Jiang, J Lin, D Cohen-Or, B Chen. Layered analysis of irregular facades via symmetry. TOG'13
		- parametric context-free split grammar:
- Furniture, building interior:
	- Problem: floor Plan; furniture layouts; room subdivision;
	- A Rau-Chaplin, B MacKay-Lyons, P Spierenburg. The lahave house project: Towards an automated architectural design service. CADEX'96
		- Floor plan: create a plan schema containing basic room units that are grouped into functional zones like public, private, or semi-private spaces;
	- E Hahn, P Bose, A Whitehead. Persistent real-time building interior generation. SIGGRAPH'06
		- The initial building structure is split into a number of floors and further subdivisions create a hallway zone and individual rooms;
	- **squarified treemaps**: F Marson, SR Musse. Automatic generation of floor plans based on squarified treemaps algorithm. 2010
		- a different room subdivision method;
	- T Germer and M Schwarz. Procedural Arrangement of Furniture for Real-Time Walkthroughs. CGF'09
	- SpeedTree: large amount of procedural vegetation;
	- Flant Factory: e-on software, tool to model and render 3D vegetation;
	- VUE;
	- CityEngine;
	- Houdini: Side Effects Software. Available from http://www.sidefx.com/
- Light:
	- Michael Schwarz and Peter Wonka. Procedural Design of Exterior Lighting for Buildings with Complex Constraints. TOG'2014
- Jerry O. Talton, Yu Lou, Jared Duke, Steve Lesser, Radomir Mech, and Vladlen Koltun.  Metropolis Procedural Modeling. TOG'11
	- http://vladlen.info/publications/metropolis-procedural-modeling/
	- https://code.google.com/archive/p/metropolis-procedural-modeling/source
- Inverse PM:
	- Carlos A Vanegas, Ignacio Garcia-Dorado, Daniel G Aliaga, Bedrich Benes, and Paul Waddell. Inverse design of urban procedural model. TOG'12
	- O Stava, S Pirk, J Kratt, B Chen, R Mech, O Deussen, and B Benes. Inverse Procedural Modelling of Trees. CGF'14
- Bedrich Beneš, Ondrej Štava, Radomir Mech, and Gavin Miller. Guided Procedural Modeling. EG'11

## 3D PM/Template
- Siddhartha Chaudhuri, Evangelos Kalogerakis, Leonidas Guibas, and Vladlen Koltun. Probabilistic reasoning for assembly-based 3d modeling. TOG'11
	- Bayesian Network with a library of things;\
		<img src = '/Generative/images/pm/3d-bnn.png' width = '500'>
- Ersin Yumer, Paul Asente, Radomir Mech, Levent Burak Kara. Procedural Modeling Using Autoencoder Networks. UIST'15
	- Preprocess: categorization tree;
	- Autoencoder on PM parameters space;\
		<img src = '/Generative/images/pm/pm-ae.png' width = '400'>
- Hang Chu, Shenlong Wang, Raquel Urtasun, Sanja Fidler. HouseCraft- Building Houses from Rental Ads and Street Views. ECCV'16
	- http://www.cs.toronto.edu/housecraft
	- https://github.com/chuhang/HouseCraft (Matlab)
	- Problem setup: input approximate address, several geo-tagged StreetView images, floor plan; output geometry and location;\
		<img src = '/Generative/images/pm/house-craft1.png' width = '450'>
	- Dataset collection: 174 houses (The SydneyHouse Dataset from http://www.domain.com.au)
	- Assumption: h foundation height (h=0 means same as camera); all floors at the same height f; all doors including garage gate same height d; a=(au, al) as window's vertical starting and ending;
	- Estimate (x, y, h, f, d, a);
	- Formulation: estimation problem:\
		<img src = '/Generative/images/pm/house-craft2.png' width = '300'>
- Haibin Huang, Evangelos Kalogerakis, Ersin Yumer, Radomir Mech. Shape Synthesis from Sketches via Procedural Models and Convolutional Networks. TVCG'16
	- https://github.com/dritchie/adnn
	- Improved version of UIST'15\
		<img src = '/Generative/images/pm/sketch-pm.png' width = '500'>
- SMPL for Human:
	- **SMPL**: M. Loper, N. Mahmood, J. Romero, G. Pons-Moll, and M. J. Black. SMPL: A skinned multi-person linear model. TOG'15
		- Key idea: Template mesh **T** (6,890 x 3) with 6,890 vertices (23 joints + 1 whole) with blended weight **W** (6,890 x 24, influence of rotation joint k on vertex i), joint **J** (24 x 6,890, rest vertices to rest joints), shape-blended shapes **S** (6,890 x 3 x 10), pose blended shapes **P** (6,890 x 3 x 207);
		- https://smpl.is.tue.mpg.de/ (python code available)
		- https://github.com/CalciferZh/SMPL (pytorch version)
		- Model:\
			<img src = '/Generative/images/pm/smpl-full.png' width = '400'>
		- Given new pose theta (24, 3), beta (10,), global translation (3,), a new mesh is generated as:
			- 1. shape blending: v-shaped = S x beta + template (6,890 x 3)
			- 2. map to joint: J = J x v_shaped (24 x 3)
			- 3. Pose: R = Rodrigues(theta) (24 x 3 x 3)
			- 4. Pose: v_posed = v_shaped + P x (R-I), where (R-I) of shape 207 (23 x 3 x 3, first dim global so skipped?)
			- 5. Kinematic tree (parent joint on child joint) 24 x 2 integer matrix; apply chain rotation to get results (24 x 4 x 4); obtain T = W x results (6,890 x 4 x 4) 
			- 6. Rest shapes: cat(v_posed, ones) (6,890 x 4)
			- 7. Final: v = T x v_posed + translation (6,890 x 3)
		- Parametrized model of 3D human shape: yaw, pitch, roll of human body joints; parameters control deformation of body skin; a fixed number of n=6,890 3D mesh vertex coordinates:\
			<img src = '/Generative/images/pm/smpl.png' width = '400'>
		- where the 3D point Xi equals the normalized bar(Xi), beta mixture of skin s(m,i) and skeleton pose p(n,i);
	- Hsiao-Yu Fish Tung, Hsiao-Wei Tung, Ersin Yumer, Katerina Fragkiadaki. Self-supervised Learning of Motion Capture. NIPS'17
		- https://github.com/htung0101/3d_smpl (Tensorflow)
		- Input: a video sequence, 2D body joint heatmaps; output a neural net predicts body parameters for SMPL 3D human mesh;
		- Training: 1. pretrained with synthetic data; 2. finetuned with self-supervised loss (keypoints, 2D segmentation, 2D optical flow);\
			<img src = '/Generative/images/pm/ssl-mocap.png' width = '500'>
		- Evaluation: 3D dense human shape tracking in SURREAL, H3.6M;
	- Meysam Madadi, Hugo Bertiche and Sergio Escalera. SMPLR: Deep SMPL reverse for 3D human pose and shape recovery. 2019
- All objects/primitives at once (regularity, structure):
	- Niloy Mitra, Michael Wand, Hao Richard Zhang, Daniel Cohen-Or, Vladimir Kim, and Qi-Xing Huang. Structure-aware shape processing. In SIGGRAPH Asia Courses, 2013
	- Shubham Tulsiani, Hao Su, Leonidas J. Guibas, Alexei A. Efros, Jitendra Malik. Learning Shape Abstractions by Assembling Volumetric Primitives. CVPR'17
- Progressive (CNN or RNN):
	- **3D-PRNN**: Chuhang Zou, Ersin Yumer, Jimei Yang, Duygu Ceylan, Derek Hoiem. 3D-PRNN: Generating Shape Primitives with Recurrent Neural Networks. ICCV'17
		- https://github.com/zouchuhang/3D-PRNN
		- Ground truth given!
	- Yonglong Tian, Andrew Luo, Xingyuan Sun, Kevin Ellis, William T. Freeman, Joshua B. Tenenbaum, Jiajun Wu. Learning to Infer and Execute 3D Shape Programs. ICLR'19
		- http://shape2prog.csail.mit.edu/
		- https://github.com/HobbitLong/shape2prog
		- Key take-aways: bottom-up recognition + top-down symbolic program;
		- Problem setup: input voxels; output programs;\
			<img src = '/Generative/images/pm/exe-3d-1.png' width = '500'>
		- Program generator: Block-LSTM + step-LSTM\
			<img src = '/Generative/images/pm/exe-3d-2.png' width = '500'>
		- Program executor: NPI at block-level, trained with large amount of synthetic\
			<img src = '/Generative/images/pm/exe-3d-3.png' width = '500'>
		- Loss: reconstruction\
			<img src = '/Generative/images/pm/exe-3d-4.png' width = '500'>
		- Key 1: program generator needed a lot of pretrain on large synthetic (block-level LSTM); manually designed program to generate, 
		- Key 2: executor trained on part-level separately; to make generator-executor differentiable;
		- Key 3: the domain gap between the synthetic and ShapeNet is still large;
- Hierarchical (RvNN/Tree/Graph):
	- Yanzhen Wang, Kai Xu, Jun Li, Hao Zhang, Ariel Shamir, Ligang Liu, Zhi-Quan Cheng, and Yueshan Xiong. Symmetry Hierarchy of Man-Made Objects. CGF'11
		- Symmetry hierarchy: 3D geometry is hierarchically grouped by either attachment or symmetric relationships;
	- **GRASS**. Jun Li, Kai Xu, Siddhartha Chaudhuri, Ersin Yumer, Hao Zhang, Leonidas Guibas. GRASS: Generative Recursive Autoencoders for Shape Structures. SIGGRAPH 2017
		- Regularity/symmetry;
		- https://github.com/kevin-kaixu/grass_pytorch
	- **StructureNet**: Kaichun Mo, Paul Guerrero, Li Yi, Hao Su, Peter Wonka, Niloy Mitra, Leonidas J. Guibas. StructureNet: Hierarchical Graph Networks for 3D Shape Generation. 2019
		- https://cs.stanford.edu/~kaichun/structurenet/
		- https://github.com/daerduoCarey/structurenet
		- **GNN** applied;
		- Problem setup: latent manipulation from point clouds and images;\
			<img src = '/Generative/images/pm/structure-net1.png' width = '500'>
		- VAE:\
			<img src = '/Generative/images/pm/structure-net2.png' width = '500'>
	- **SCORES**: Chenyang Zhu, Kai Xu, Siddhartha Chaudhuri, Renjiao Yi, Hao Zhang. SCORES: Shape Composition with Recursive Substructure Priors. SIGGRAPH Asia'18
		- https://github.com/BigkoalaZhu/SCORES
	- **GRAINS**: Manyi Li, Akshay Gadi Patil, Kai Xu, Siddhartha Chaudhuri, Owais Khan, Ariel Shamir, ChangheTu, Baoquan Chen, Daniel Cohen-Or, and Hao Zhang. GRAINS: Generative recursive autoencoders for indoor scenes. TOG'19
		- https://github.com/ManyiLi12345/GRAINS
		- Tree-VAE:\
			<img src = '/Generative/images/pm/grains1.png' width = '450'>
		- Inference mode:\
			<img src = '/Generative/images/pm/grains2.png' width = '450'>
	- **StructEdit**: Kaichun Mo, Paul Guerrero, Li Yi, Hao Su, Peter Wonka, Niloy J. Mitra, Leonidas Guibas. StructEdit: Learning Structural Shape Variations. 2019
		- https://github.com/daerduoCarey/structedit
	- **Im2Struct**: Chengjie Niu, Jun Li, and Kai Xu. Im2Struct: Recovering 3D Shape Structure from a Single RGB Image. CVPR'18
		- Infer a hierarchical bounding box structure from a single image of a 3D shape;
		- https://github.com/chengjieniu/Im2Struct
	- **GNN**: Kai Wang, Yu-an Lin, Ben Weissmann, Manolis Savva, Angel X. Chang, and Daniel Ritchie. PlanIT: Planning and Instantiating Indoor Scenes with Relation Graph and Spatial Prior Networks. SIGGRAPH'19
		- https://github.com/brownvc/planit
		- Indoor scene graph with GNN, then based on the graph, one-object at a time;\
			<img src = '/Generative/images/pm/indoor-scene-graph.png' width = '400'>
- **CSGNet**: Gopal Sharma Rishabh Goyal Difan Liu Evangelos Kalogerakis Subhransu Maji. CSGNet: Neural Shape Parser for Constructive Solid Geometry. 2018
	- https://github.com/hippogriff/CSGNet
	- Problem definition: **boolean** operation, include **minus**;\
		<img src = '/Generative/images/pm/csgnet1.png' width = '450'>
	- Algorithm:\
		<img src = '/Generative/images/pm/csgnet2.png' width = '450'>
- **SPFN**: Lingxiao Li, Minhyuk Sung, Anastasia Dubrovina, Li Yi, Leonidas Guiba. Supervised Fitting of Geometric Primitives to 3D Point Clouds. CVPR'19
	- https://github.com/lingxiaoli94/SPFN

## 2D PM
- Stroke:
	- **SPRIAL**. Y. Ganin, T. Kulkarni, Igor Babuschkin, S. M. Ali Eslami, Oriol Vinyals. SPIRAL: Synthesizing Programs for Images using Reinforced Adversarial Learning. ICML'18
		- https://github.com/deepmind/spiral
- Template/primitives:
	- Kevin Ellis, Armando Solar-Lezama, Joshua B. Tenenbaum. Unsupervised Learning by Program Synthesis. NIPS'15
		- https://github.com/ellisk42/sasquatch
- Physics:
	- Zhijian Liu, William T. Freeman, Joshua B. Tenenbaum, and Jiajun Wu. Physical Primitive Decomposition. ECCV'18
		- http://ppd.csail.mit.edu/
- Neural-Symbolic Reasoning:
	- **NMN**: J Andreas, M Rohrbach, T Darrell, D Klein. Neural Module Networks. CVPR'16
	- **clevr-iep**: Justin Johnson, Judy Hoffman, Bharath Hariharan, Laurens van der Maaten, Li Fei-Fei, C. Lawrence Zitnick, Ross Girshick. Inferring and Executing Programs for Visual Reasoning. ICCV'17
		- https://github.com/facebookresearch/clevr-iep
	- **sg2im**: Justin Johnson, Agrim Gupta, Li Fei-Fei. Image Generation from Scene Graphs. CVPR'18
		- https://github.com/google/sg2im
	- **Neural-Symbolic VQA**: Kexin Yi, Jiajun Wu, Chuang Gan, Antonio Torralba, Pushmeet Kohli, Joshua B. Tenenbaum. Neural-Symbolic VQA: Disentangling Reasoning from Vision and Language Understanding. NeurIPS 2018
		- http://nsvqa.csail.mit.edu/
		- An interpretable VQA model that disentangles language reasoning from visual understanding
		- For visual understanding, first perform objects segmentation and then learn to obtain structural scene representation (with supervision) such as color, size, shape, position.
		- For language reasoning, they learn to translate natural language question into a deterministic program such as filter_shape(scene, large) or count(scene). 
		- Finally, they execute the program on the structural scene representation to obtain the final answer
		- 99.8% on CLEVR
	- Yunchao Liu, Zheng Wu, Daniel Ritchie, William T Freeman, Joshua B Tenenbaum, and Jiajun Wu. Learning to describe scenes with programs. ICLR'19
		- Problem definition: focus on learning the high-level scene regularities described by loop structures:\
			<img src="/Generative/images/pm/learn-to-describe.png" alt="drawing" width="500"/>
		- An object parser predicts the segmentation mask and attributes for each object in the image; (Mask-RCNN, ResNet-34)
		- A group recognizer predicts the group that each object belongs to; concatenate original, mask of self, mask of objects, then ResNet + fc output two heads (same group and category?)
		- DSL; learn with seq2seq LSTM, each step output a token t and a parameter matrix P;\
			<img src="/Generative/images/pm/learn-to-describe-dsl.png" alt="drawing" width="450"/>
		- Algorithm:\
			<img src="/Generative/images/pm/learn-to-describe-alg.png" alt="drawing" width="450"/>
	- **NSCL**: Jiayuan Mao, Chuang Gan, Pushmeet Kohli, Joshua B. Tenenbaum, Jiajun Wu. The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences from Natural Supervision. ICLR'19
		- http://nscl.csail.mit.edu/
	- **NGSI**: Sidi Lu, Jiayuan Mao, Joshua B. Tenenbaum, Jiajun Wu. Neurally-Guided Structure Inference. ICML'19
		- https://github.com/desire2020/NGSI
	- **PGIM**: Jiayuan Mao, Xiuming Zhang, Yikai Li, William T. Freeman, Joshua B. Tenenbaum, Jiajun Wu. Program-Guided Image Manipulators. ICCV'19
		- http://pgim.csail.mit.edu
	- Chi Han, Jiayuan Mao, Chuang Gan, Joshua B. Tenenbaum, Jiajun Wu. Visual Concept-Metaconcept Learning. NIPS'19
		- http://vcml.csail.mit.edu/
		- https://github.com/Glaciohound/VCML
- De-render, Inverse Graphics:
	- **Picture**: Kulkarni, T. D., Kohli, P., Tenenbaum, J. B., and Mansinghka, V. Picture: A probabilistic programming language for scene perception. CVPR'15
	- **DC-IGN**: Kulkarni, T. D., Whitney, W. F., Kohli, P., and Tenenbaum, J. Deep convolutional inverse graphics network. NIPS'15
		- Probabilistic programming:\
			<img src="/Graphics/images/dc_ign.png" alt="drawing" width="600"/>
	- **NGPM**: Daniel Ritchie, Anna Thomas, Pat Hanrahan, Noah Goodman. Neurally-Guided Procedural Models: Amortized Inference for Procedural Graphics Programs using Neural Networks. NIPS'16
		- Problem setup: for a shape, generate particles to cover;
		- Probabilistic Programming with NN;\
			<img src = '/Generative/images/pm/ngpm1.png' width = '500'>
		- Minimize KL divergence PCM and PGM;\
			<img src = '/Generative/images/pm/ngpm2.png' width = '400'>
	- **R3NN**: Emilio Parisotto, Abdel-rahman Mohamed, Rishabh Singh, Lihong Li, Dengyong Zhou, and Pushmeet Kohli. Neuro-symbolic program synthesis. ICLR'17
	- Tony Beltramelli. Pix2code: Generating code from a graphical user interface screenshot. EICA'18
		- GUI image to markup-like code;
	- Rudy Bunel, Matthew Hausknecht, Jacob Devlin, Rishabh Singh, and Pushmeet Kohli. Leveraging grammar and reinforcement learning for neural program synthesis. ICLR'18
		- goes beyond the pure supervised learning setting and improves performance on diversity and syntax by leveraging grammar and reinforcement learning;
- Progressive CNN:
	- J Wu, JB Tenenbaum, P Kohli. Neural scene de-rendering. CVPR'17
		- Problem setup: image to xml;\
			<img src = '/Generative/images/pm/derender1.png' width='350'>
		- Approach: add element one by one;\
			<img src = '/Generative/images/pm/derender2.png' width='500'>
	- **Deep-Synth**: Kai Wang, Manolis Savva, Angel X. Chang, and Daniel Ritchie. Deep Convolutional Priors for Indoor Scene Synthesis. SIGGRAPH'18
		- https://github.com/brownvc/deep-synth
		- PM: add object one by one; BEV;\
			<img src = '/Generative/images/pm/indoor-prior.png' width = '400'>
	- Kevin Ellis, Daniel Ritchie, Armando Solar-Lezama, Josh Tenenbaum. Learning to Infer Graphics Programs from Hand-Drawn Images, NIPS'18
		- Problem: Noisy input (data augmentation); output program;
		- One at a time:\
			<img src = '/Generative/images/pm/latex.png' width = '450'>
		- Combining NGPM [4] and Attend-Infer-Repeat [5]
		- Learn a loss function?
		- DSL [11]
		- Prefer shorter program (with explicit reward)
		- Sketch-tool [1] to refine program: constraint-based SAT solver to perform program search and is much slower
	- Daniel Ritchie, Kai Wang, and Yu-an Lin. Fast and Flexible Indoor Scene Synthesis via Deep Convolutional Generative Models. CVPR'19
		- Problem setup: generative model with empty canvas and object count, one at a time;\
			<img src = '/Generative/images/pm/indoor-synth1.png' width = '400'>
		- Next object category: auxiliary STOP;
		- Object location: FCN, heat map;
		- Object orientation: cVAE for multi-modality;
		- Object dimension: cVAE;
- All objects/primitives at once:
	- **3D-SDN**: Shunyu Yao, Tzu Ming Harry Hsu, Jun-Yan Zhu, Jiajun Wu, Antonio Torralba, William T. Freeman, Joshua B. Tenenbaum. 3D-Aware Scene Manipulation via Inverse Graphics. NIPS'18
		- http://3dsdn.csail.mit.edu/
		- https://github.com/ysymyth/3D-SDN
		- Algorithm:\
			<img src = '/Generative/images/pm/3d-sdn.png' width = '400'>

## Unclassified
- Daniel J. Fremont, Tommaso Dreossi, Shromona Ghosh, Xiangyu Yue, Alberto L. Sangiovanni-Vincentelli, Sanjit A. Seshia. Scenic: A Language for Scenario Specification and Scene Generation. Scenic: a language for scenario specification and scene generation. PLDI'19
	- https://github.com/BerkeleyLearnVerify/Scenic
- Ennafii, Oussama; Le Bris, Arnaud; Lafarge, Florent; Mallet, Clément. A learning approach to evaluate the quality of 3D city models. Engineering & Remote Sensing'19
- Tao Du, Jeevana Priya Inala, Yewen Pu, Andrew Spielberg, Adriana Schulz, Daniela Rus, Armando Solar-Lezama, Wojciech Matusik. InverseCSG: automatic conversion of 3D models to CSG trees. SIGGRAPH Asia'18
	- http://cfg.mit.edu/content/inversecsg-automatic-conversion-3d-models-csg-trees
- Theo Deprelle, Thibault Groueix, Matthew Fisher, Vladimir Kim, Bryan Russell, Mathieu Aubry. Learning elementary structures for 3D shape generation and matching. NIPS'19
