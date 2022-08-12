# 3D-CV Basics

## Tutorials, Books
- Faugeras and Luong, The Geometry of Multiple Views, 2001
- Richard Hartley, Andrew Zisserman. Multiple view geometry in computer vision.
- Ma, Soatto, Kosecka, Sastry, An Invitation to 3D Vision, 2004.

## Linear Algebra, Lie-Algebra
- SVD:
	- A Geometric Interpretation of SVD: maps unit-sphere to ellipsoid
- Skew-symmetric Matrices
	- For vec [t1, t2, t3],
	- We define skew symmetric matrix [t] as:
		- [0, -t3, t2]
		- [t3, 0, -t1]
		- [-t2, t1, 0]
	- We have:
		- [t] = -[t]'
		- rank([t]) = 2 for t;
		- Null space of [t] is t, [t]t = 0
	- Cross product t x u = [t]u
	- Rigid body motion:
		- g: R3 to R3
		- Preserve norm and cross product
		- gt(x) = Rx + T
- Lie-Algebra
	- Lie group: R ∈ SO(3)
	- Lie algebra w ∈ so(3), infinitesimal rotation;
	- R(t)R(t)' = I
		- dR/dt R' + R dR'/dt = 0
		- dR/dt R' = -(dR/dt R')';
		- dR/dt R' is skew symmetric;
		- Let dR/dt R' = w(t), dR(t)/dt = wR(t)
	- Lie algebra to Lie group: exponential
		- R(0) = I, dR(0)/dt = w
		- w ∈ so(3)
	- Logrithm:
		- For any R, exist w s.t. R = exp(w), where w is skew-symmetric;
		- w = log(R)
		- One solution:
			- Angle: |w| = cos^(-1)(trace(R)-1/2)
			- Axis: w/|w| = 1/2sin(|w|) [r32-r23, r13-r31, r21-r12]
		- Not unique: +2π

## Camera
- Calibration:

## Single-View Geometry
- Vanishing Points and Lines
	- Parallel lines meets at v-point;
	- All v-points (by different direction lines) forms a van-line;
- Projection transformation P;
- w = [w1  0 w4]
-     [0  w1 w5]
-     [w4 w5 w6]
- Find w s.t. v1 * w * v2 = 0 always hold;

## Two Views
- Assume:
	- Static scene;
	- K known;
	- Solve: (R, T) 6-dof
- Two images:
	- o1, o2: camera centers
	- e1, e2: o2 on im1, o1 on im2;
	- e1, e2: epipoles
	- (o1, o2, X): epipolar plane
	- l1, l2: epipolar lines
- F := inv(K2)'[t]RK1, fundamental matrix;
	- q'Fq = 0; (b/c coplanar)
- If q', q already multiplied by K1^-1, K2^-1;
	- q'Eq = 0; essential matrix;
	- E = [T]R, x2'[T]Rx1 = x2'(T x Rx1) = 0;
	- o1X, o2o1, o2X coplane, volume=0;
- 8-pt algorithm
	- x2' E x1 = 0
	- Find null space;
	- Project onto essential space (satisify the eigen-value property)
		- E has only 5-DOF
		<img src="/CV-3D/images/trad/essential-matrix-8point.png" alt="drawing" width="600"/>
	- Structure Reconstruction: estimate X (3D-coord);
		<img src="/CV-3D/images/trad/epipolar-structure1.png" alt="drawing" width="600"/>
		<img src="/CV-3D/images/trad/epipolar-structure2.png" alt="drawing" width="600"/>
- 4-pt algorithm (Homography)
	<img src="/CV-3D/images/trad/epipolar-homography.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/trad/epipolar-4point1.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/trad/epipolar-4point2.png" alt="drawing" width="600"/>
	- Relation between Homography and Essential-Matrix
		<img src="/CV-3D/images/trad/essential-homography.png" alt="drawing" width="600"/>
- Uncalibrated camera
	- Fundamental matrix
	<img src="/CV-3D/images/trad/fundamental-matrix.png" alt="drawing" width="600"/>

## MVG
- Good resources:
	- Y. Furukawa, B. Curless, S. M. Seitz, and R. Szeliski. Towards internet-scale multi-view stereo. CVPR'10
- Many cameras, each Pi for each image;
- Trifocal Tensor
- SVD;
- Bundle adjustment;
- Preimage & Coimage from Multiple Views
- From Preimages to Rank Constraints
	<img src="/CV-3D/images/trad/mvg.png" alt="drawing" width="500"/>
- Geometric Interpretation
- The Multiple-view Matrix
- Relation to Epipolar Constraints
- Multiple-View Reconstruction Algorithms
- Multiple-View Reconstruction of Lines

## To estimate obj Geometry
- Space-carving (ray-tracing);

## Matching
- Photometry to Geometry
- Small Deformation, Optical Flow
	- Lucas/Kanade
	- Horn/Schunck
- Sparse: Feature Point Extraction
- Wide Baseline Matching
	- Accumulation of small errors: drift
	- NCC
	- Small number of feature points;

## Variational Methods
- Variational Methods
- Variational Image Smoothing
- Euler-Lagrange Equation:
	- E(u) = ∫L(u, u')dx
	- dE/du = ∂L/∂u - d/dx(∂L/∂u') = 0
- Gradient Descent
- Adaptive Smoothing
- Euler and Lagrange
- Variational 3D
	- Imposing Silhouette Consistency: Cremers, Kolev, PAMI 2011
	- Multi-view Texture Reconstruction: Goldlücke, Cremers, ICCV 2009, DAGM 2009