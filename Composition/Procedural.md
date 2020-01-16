## Procedural Modeling

## Brief Overview
- Problem Definition: Generate something with grammars/programs/templates/compositional model to explain/modify/generate an object
- Surveys and books:
	- DS Ebert, FK Musgrave, D Peachey, K Perlin, S Worley. Texturing & Modeling, a Procedural Approach, 3rd ed. Elsevier, 2003.
	- Lagae, Ares; Lefebvre, Sylvain; Cook, Rob; DeRose, Tony; Drettakis, George; Ebert, DS; Lewis, JP ; Perlin, Ken ; Zwicker, Matthias. State of the art in procedural noise function. EG'10
	- Ruben M. Smelik, Tim Tutenel, Rafael Bidarra, and Bedrich Benes. 2014. A Survey on Procedural Modelling for Virtual Worlds. Computer Graphics Forum'14\
		<img src = '/Composition/images/survey.png' width = '600'>

## Legacy
- **L-System**: Aristid Lindenmayer. Mathematical models for cellular interactions in development. Journal of theoretical biology 1968
	- First PM paper;
- K Perlin. An image synthesizer. SIGGRAPH'85
- Przemyslaw Prusinkiewicz. Graphical applications of L-systems. In Proceedings of graphics interface. 1986

## Terrain
- Noise-based, physics-based;
- Fractal: BB Mandelbrot. The Fractal Geometry of Nature. W. H. Freeman, 1982
	- Height (limitation: can't handle overhangs and caves)
- FK Musgrave, CE Kolb, RS Mace. The synthesis and rendering of eroded fractal terrains. SIGGRAPH'89
	- Physics-based: Erosion;
- B Benes, R Forsbach. Layered data representation for visual simulation of terrain erosion. SCCG'01
- RL Saunders. Terrainosaurus: Realistic Terrain Synthesis Using Genetic Algorithms. 06
	- AI-based? DEM-based
- A Peytavie, E Galin, J Grosjean. Arches: a framework for modeling complex terrains. CGF'09

## Vegetation, Plant
- Problem: individual plant organs, plants, complete plant ecosystems;
- Przemyslaw Prusinkiewicz and Aristid Lindenmayer. The Algorithmic Beauty of Plants. 1990
- Przemyslaw Prusinkiewicz, Mark James, and Radomir Mech. Synthetic topiary. SIGGRAPH'94
- Radomir Mech and Przemyslaw Prusinkiewicz. Visual models of plants interacting with their environment. SIGGRAPH'96
- Michael T. Wong, Douglas E. Zongker, and David H. Salesin. Computer-generated Floral Ornament. SIGGRAPH'98
- **Xfrog**: D Lintermann, O Deussen. Interactive Modeling of Plants. CGA'99
- T Ijiri, S Owada, T Igarashi. Seamless integration of initial sketching and subsequent detail editing in flower modeling. CGF'06 
- S Longay, A Runions, F Boudon, Przemyslaw Prusinkiewicz. Treesketch: Interactive modeling of trees on a tablet. EG'12
- T Ijiri, S Owada, T Igarashi. The sketch L-System: Global control of tree modeling using free-form strokes. Smart Graphics'06
- Yotam Livny, Feilong Yan, Matt Olson, Baoquan Chen, Hao Zhang, Jihad El-Sana. Automatic reconstruction of tree skeletal structures from point clouds. TOG'10
- **SpeedTree**: Interactive Data Visualization, Inc. SpeedTree. 13
	- http://www.speedtree.com/
- **plastic trees**: Pirk, Sören; Stava, Ondrej; Kratt, Julian; Massih Said, Michel Abdul; Neubert, Boris; Mech, Randomir; Benes, Bedrich; Deussen, Oliver. Plastic trees: interactive self-adapting botanical tree models. SIGGRAPH'12

## Water bodies: 
- Problem setup: rivers, lakes, streams, oceans, waterfalls...

## Roads
- Problem: in the context of procedural cities;
	- a) user-assisted, where road 3D splines that minimize local elevation changes are fitted in between sketch strokes or control points;
	- b) based on path finding techniques from AI research, such as A\*
- **DEM**: E Bruneton, F Neyret. Real-time rendering and editing of vector-based terrains. CGF'08
- J McCrae, K Singh. Sketch-based path design. GI'09: Proceedings of Graphics Interface 2009

## City
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
- Jerry O. Talton, Yu Lou, Jared Duke, Steve Lesser, Radomir Mech, and Vladlen Koltun.  Metropolis Procedural Modeling. TOG'11
	- http://vladlen.info/publications/metropolis-procedural-modeling/
	- https://code.google.com/archive/p/metropolis-procedural-modeling/source
- CityEngine;

## Buildings
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

## Furniture, building interior:
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
- Houdini: Side Effects Software. Available from http://www.sidefx.com/

## Light
- Michael Schwarz and Peter Wonka. Procedural Design of Exterior Lighting for Buildings with Complex Constraints. TOG'2014

## Inverse Procedural Modeling
- City:
	- Carlos A Vanegas, Ignacio Garcia-Dorado, Daniel G Aliaga, Bedrich Benes, and Paul Waddell. Inverse design of urban procedural model. TOG'12
	- Gen Nishida, Ignacio Garcia-Dorado, Daniel G. Aliaga, Bedrich Benes, Adrien Bousseau. Interactive Sketching of Urban Procedural Models. TOG'16
		- Inverse PM: Our interactive sketching tool allows the user to quickly and easily author procedural 3D building models.
		- The user only performs interactive sketching and our system automatically generates the procedural model and its parameters yielding the sketched shape.
- Tree:
	- O Stava, S Pirk, J Kratt, B Chen, R Mech, O Deussen, and B Benes. Inverse Procedural Modelling of Trees. CGF'14
- Bedrich Beneš, Ondrej Štava, Radomir Mech, and Gavin Miller. Guided Procedural Modeling. EG'11
