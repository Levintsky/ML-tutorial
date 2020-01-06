# Procedural Modeling (PM)

## Brief Overview
- Problem Definition: Generate something with grammars/programs/templates
- Surveys and books:
	- DS Ebert, FK Musgrave, D Peachey, K Perlin, S Worley. Texturing & Modeling, a Procedural Approach, 3rd ed. Elsevier, 2003.
	- Lagae, Ares; Lefebvre, Sylvain; Cook, Rob; DeRose, Tony; Drettakis, George; Ebert, DS; Lewis, JP ; Perlin, Ken ; Zwicker, Matthias. State of the art in procedural noise function. EG'10
	- Ruben M. Smelik, Tim Tutenel, Rafael Bidarra, and Bedrich Benes. 2014. A Survey on Procedural Modelling for Virtual Worlds. Computer Graphics Forum'14\
		<img src = '/Generative/images/pm/survey.png' width = '600'>

## Benchmarks
- Shenlong Wang, Min Bai, Gellert Mattyus, Hang Chu, Wenjie Luo, Bin Yang, Justin Liang, Joel Cheverie, Sanja Fidler, Raquel Urtasun. TorontoCity: Seeing the World with a Million Eyes. ICCV'17

## Legacy
- **L-System**: Aristid Lindenmayer. Mathematical models for cellular interactions in development. Journal of theoretical biology 1968
	- First PM paper;
- K Perlin. An image synthesizer. SIGGRAPH'85
- Przemyslaw Prusinkiewicz. 1986. Graphical applications of L-systems. In Proceedings of graphics interface. 1986
- Przemyslaw Prusinkiewicz and Aristid Lindenmayer. The Algorithmic Beauty of Plants. 1990
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
	- Przemyslaw Prusinkiewicz, Mark James, and Radomir Mech. Synthetic topiary. SIGGRAPH'94
	- Radomir Mech and Przemyslaw Prusinkiewicz. Visual models of plants interacting with their environment. SIGGRAPH'96
	- Michael T. Wong, Douglas E. Zongker, and David H. Salesin. Computer-generated Floral Ornament. SIGGRAPH'98
	- **Xfrog**: L INTERMANN B., D EUSSEN O.: Interactive Modeling of Plants. CGA'99
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
	- T Lechner, B Watson, U Wilensky. Procedural city modeling. 03
		- Not only residential, commercial and industrial areas;
		- But also special areas like government buildings, squares, and monuments
	- G Kelly, H McCabe. A survey of procedural techniques for city generation. 06
	- Sinha, S.N., Steedly, D., Szeliski, R., Agrawala, M., Pollefeys, M.: Interactive 3d architectural modeling from unordered photo collections. TOG'08
	- Guoning Chen, Gregory Esch, Peter Wonka, Pascal Mueller, Eugene Zhang. Interactive procedural street modeling. SIGGRAPH'08
		- Interactive modeling method for road networks by the use of tensor field;
	- Xiao, J., Fang, T., Zhao, P., Lhuillier, M., Quan, L. Image-based street-side city modeling. TOG'09
	- Paul Merrell, Eric Schkufza, and Vladlen Koltun. 2010. Computer-generated residential building layouts. TOG'10
	- Pylvanainen, T., Berclaz, J., Korah, T., Hedau, V., Aanjaneya, M., Grzeszczuk, R.: 3d city modeling from street-level data for augmented reality applications. 3DIM/3DPVT'12
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
	- Houdini: SIDE E FFECTS SOFTWARE : Houdini. Available from http://www.sidefx.com/
- Light:
	- Michael Schwarz and Peter Wonka. Procedural Design of Exterior Lighting for Buildings with Complex Constraints. TOG'2014
- Jerry O. Talton, Yu Lou, Jared Duke, Steve Lesser, Radomir Mech, and Vladlen Koltun.  Metropolis Procedural Modeling. TOG'11
	- http://vladlen.info/publications/metropolis-procedural-modeling/
	- https://code.google.com/archive/p/metropolis-procedural-modeling/source
- Inverse PM:
	- Carlos A Vanegas, Ignacio Garcia-Dorado, Daniel G Aliaga, Bedrich Benes, and Paul Waddell. Inverse design of urban procedural model. TOG'12
	- O Stava, S Pirk, J Kratt, B Chen, R Mech, O Deussen, and B Benes. Inverse Procedural Modelling of Trees. In Computer Graphics Forum. 2014
- Bedrich Beneš, Ondrej Štava, Radomir Mech, and Gavin Miller. Guided Procedural Modeling. In Eurographics 2011.

## 3D PM
- Ersin Yumer, Paul Asente, Radomir Mech, Levent Burak Kara. Procedural Modeling Using Autoencoder Networks. UIST'15
	- Preprocess: categorization tree;
	- Autoencoder on PM parameters space;\
		<img src = '/Generative/images/pm/pm-ae.png' width = '400'>
- **SMPL**: M. Loper, N. Mahmood, J. Romero, G. Pons-Moll, and M. J. Black. SMPL: A skinned multi-person linear model. TOG'15
	- Template mesh **T** with blended weight **W**, joint **J**;
	- Given new pose theta, generate new mesh;
	- https://smpl.is.tue.mpg.de/ (python code available)
	- https://github.com/CalciferZh/SMPL (pytorch version)
	- Parametrized model of 3D human shape: yaw, pitch, roll of human body joints; parameters control deformation of body skin; a fixed number of n=6,890 3D mesh vertex coordinates:\
		<img src = '/Generative/images/pm/smpl.png' width = '400'>
	- where the 3D point Xi equals the normalized bar(Xi), beta mixture of skin s(m,i) and skeleton pose p(n,i);
- Hang Chu, Shenlong Wang, Raquel Urtasun, Sanja Fidler. HouseCraft- Building Houses from Rental Ads and Street Views. ECCV'16
	- http://www.cs.toronto.edu/housecraft
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
- Hsiao-Yu Fish Tung, Hsiao-Wei Tung, Ersin Yumer, Katerina Fragkiadaki. Self-supervised Learning of Motion Capture. NIPS'17
	- Input: a video sequence, 2D body joint heatmaps; output a neural net predicts body parameters for SMPL 3D human mesh;
	- Training: 1. pretrained with synthetic data; 2. finetuned with self-supervised loss (keypoints, 2D segmentation, 2D optical flow);\
		<img src = '/Generative/images/pm/ssl-mocap.png' width = '500'>
	- Evaluation: 3D dense human shape tracking in SURREAL, H3.6M;
- Meysam Madadi, Hugo Bertiche and Sergio Escalera. SMPLR: Deep SMPL reverse for 3D human pose and shape recovery. 2019
- Yonglong Tian, Andrew Luo, Xingyuan Sun, Kevin Ellis, William T. Freeman, Joshua B. Tenenbaum, Jiajun Wu. Learning to Infer and Execute 3D Shape Programs. ICLR'19
	- http://shape2prog.csail.mit.edu/
	- https://github.com/HobbitLong/shape2prog
- Kaichun Mo, Paul Guerrero, Li Yi, Hao Su, Peter Wonka, Niloy Mitra, Leonidas J. Guibas. StructureNet: Hierarchical Graph Networks for 3D Shape Generation. 2019
	- https://cs.stanford.edu/~kaichun/structurenet/
	- https://github.com/daerduoCarey/structurenet

## 2D PM
- **NGPM**: Daniel Ritchie, Anna Thomas, Pat Hanrahan, Noah Goodman. Neurally-Guided Procedural Models: Amortized Inference for Procedural Graphics Programs using Neural Networks. NIPS'16
	- Problem setup: for a shape, generate particles to cover;
	- Probabilistic Programming with NN;\
		<img src = '/Generative/images/pm/ngpm1.png' width = '500'>
	- Minimize KL divergence PCM and PGM;\
		<img src = '/Generative/images/pm/ngpm2.png' width = '400'>
- J Wu, JB Tenenbaum, P Kohli. Neural scene de-rendering. CVPR'17
	- Problem setup: image to xml;\
		<img src = '/Generative/images/pm/derender1.png' width='350'>
	- Approach: add element one by one;\
		<img src = '/Generative/images/pm/derender2.png' width='500'>
- **Deep-Synth**: Kai Wang, Manolis Savva, Angel X. Chang, and Daniel Ritchie. Deep Convolutional Priors for Indoor Scene Synthesis. SIGGRAPH'18
	- https://github.com/brownvc/deep-synth
	- PM: add object one by one; BEV;\
		<img src = '/Generative/images/pm/indoor-prior.png' width = '400'>
- 3D-Aware Scene Manipulation via Inverse Graphics. NIPS'18
	- http://3dsdn.csail.mit.edu/
	- https://github.com/ysymyth/3D-SDN
- Kevin Ellis, Daniel Ritchie, Armando Solar-Lezama, Josh Tenenbaum. Learning to Infer Graphics Programs from Hand-Drawn Images, NIPS 2018
	- Noisy input (data augmentation)
	- Combining NGPM [4] and Attend-Infer-Repeat [5]
	- Learn a loss function?
	- DSL [11]
	- Prefer shorter program (with explicit reward)
	- Sketch-tool [1] to refine program
- Daniel Ritchie, Kai Wang, and Yu-an Lin. Fast and Flexible Indoor Scene Synthesis via Deep Convolutional Generative Models. CVPR'19
- Kai Wang, Yu-an Lin, Ben Weissmann, Manolis Savva, Angel X. Chang, and Daniel Ritchie. PlanIT: Planning and Instantiating Indoor Scenes with Relation Graph and Spatial Prior Networks. SIGGRAPH'19
- **PGIM**: Jiayuan Mao, Xiuming Zhang, Yikai Li, William T. Freeman, Joshua B. Tenenbaum, Jiajun Wu. Program-Guided Image Manipulators. ICCV'19
	- http://pgim.csail.mit.edu
- Reasoning, VQA:
	- Kexin Yi, Jiajun Wu, Chuang Gan, Antonio Torralba, Pushmeet Kohli and Joshua B. Tenenbaum. Neural-Symbolic VQA: Disentangling Reasoning from Vision and Language Understanding, NIPS 2018
		- An interpretable VQA model that disentangles language reasoning from visual understanding
		- For visual understanding, first perform objects segmentation and then learn to obtain structural scene representation (with supervision) such as color, size, shape, position.
		- For language reasoning, they learn to translate natural language question into a deterministic program such as filter_shape(scene, large) or count(scene). 
		- Finally, they execute the program on the structural scene representation to obtain the final answer
		- 99.8% on CLEVR
	- Yunchao Liu, Zheng Wu, Daniel Ritchie, William T. Freeman, Joshua B. Tenenbaum, and Jiajun Wu. Learning to describe scenes with programs. ICLR'19

## Unclassified
- GRAINS: Generative recursive autoencoders for indoor scenes. 2019
- Scenic: a language for scenario specification and scene generation. 2019
- A learning approach to evaluate the quality of 3D city models
- Gopal Sharma Rishabh Goyal Difan Liu Evangelos Kalogerakis Subhransu Maji. CSGNet: Neural Shape Parser for Constructive Solid Geometry. 2018
- Yaroslav Ganin, Tejas Kulkarni, Igor Babuschkin, S.M. Ali Eslami, Oriol Vinyals. Synthesizing programs for images using reinforced adversarial learning. 2018
- InverseCSG: automatic conversion of 3D models to CSG trees. 2018
- Learning elementary structures for 3D shape generation and matching
- Lingxiao Li, Minhyuk Sung, Anastasia Dubrovina, Li Yi, Leonidas Guibas. Supervised fitting of geometric primitives to 3d point clouds. CVPR'19
