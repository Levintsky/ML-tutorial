# Implicit Functions for Templates

## Legacy
- Antonio Ricci. A constructive geometry for computer graphics. The Computer Journal'73
- **MetaBalls**: J. F. Blinn. A generalization of algebraic surface drawing. TOG'82
- **Soft-object**: Geoff Wyvill, Craig McPheeters, and Brian Wyvill. Data structure for soft objects. In Advanced Computer Graphics'86
- **Conv-surface**: Jules Bloomenthal and Ken Shoemake. Convolution surfaces. SIGGRAPH'91
- **Blobby-model**: Shigeru Muraki. Volumetric shape description of range data using blobby model. SIGGRAPH'91
- **Unity-implicit**: Yutaka Ohtake, Alexander Belyaev, Marc Alexa, Greg Turk, and Hans-Peter Seidel. Multi-level partition of unity implicits, volume 22. ACM, 2003

## Template as Implicit Functions
- **SIF**: Kyle Genova, Forrester Cole, Daniel Vlasic, Aaron Sarna, William T. Freeman, Thomas Funkhouser. Learning Shape Templates with Structured Implicit Functions. ICCV'19
	- Primitives: 3D Gaussian, with level-set c=-0.07;\
		<img src = '/Composition/images/3d/sif.png' width = '450'>
	- Compact: 7N for N blobs; (1 c + 3 mean + 3 variance for each Gaussian)
- **DSIF**: Kyle Genova, Forrester Cole, Avneesh Sud, Aaron Sarna, Thomas Funkhouser. Deep Structured Implicit Functions. 2020
	- Insight: similar to SIF, with another implicit NN to get better surfaces;
	- Improve on SIF 7 parameters to 10 (plus);
	- Algorithm framework:\
		<img src = '/Composition/images/3d/dsif.png' width = '500'>
- Boyang Deng, Kyle Genova, Soroosh Yazdani, Sofien Bouaziz, Geoffrey Hinton, Andrea Tagliasacchi. CvxNet: Learnable Convex Decomposition. 2020
	- Problem setup: a set of convex implicit functions by NN;
		<img src = '/Composition/images/3d/cvx-net-1.png' width = '400'>
	- Formulation: a set of classifier:\
		<img src = '/Composition/images/3d/cvx-net-2.png' width = '400'>\
		<img src = '/Composition/images/3d/cvx-net-3.png' width = '400'>
	- Multiple convex: a set of things + composition;
	- Decomposition loss (auxiliary):\
		<img src = '/Composition/images/3d/cvx-net-4.png' width = '400'>
	- Unique parameterization loss (auxiliary):\
		<img src = '/Composition/images/3d/cvx-net-5.png' width = '400'>
	- Guidance loss (auxiliary):\
		<img src = '/Composition/images/3d/cvx-net-6.png' width = '400'>
