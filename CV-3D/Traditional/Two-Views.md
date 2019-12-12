# Reconstruction from Two Views

## The Reconstruction Problem
- Assume static scene;
- Intrinsic camera (calibration) parameters are known;
- Recover 6 paras (R, T)

## The Epipolar Constraint
- Two image planes parallel: e, e' infinity;
	- o1, o2: camera centers
	- e1, e2: epipoles
	- (o1, o2, X): epipolar plane
	- l1, l2: epipolar lines
	<img src="/CV-3D/images/trad/epipolar.png" alt="drawing" width="600"/>

- Essential matrix; (for canonical cameras)
	<img src="/CV-3D/images/trad/essential-matrix.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/trad/essential-matrix2.png" alt="drawing" width="600"/>

## Eight-Point Algorithm
- x2^T E x1 = 0
- Find null space;
- Project onto essential space (satisify the eigen-value property)
	- E has only 5-DOF
	<img src="/CV-3D/images/trad/essential-matrix-8point.png" alt="drawing" width="600"/>

## Structure Reconstruction
<img src="/CV-3D/images/trad/epipolar-structure1.png" alt="drawing" width="600"/>
<img src="/CV-3D/images/trad/epipolar-structure2.png" alt="drawing" width="600"/>

## Four-Point Algorithm
- Homography
<img src="/CV-3D/images/trad/epipolar-homography.png" alt="drawing" width="600"/>

- Assume **all points lie on a plane**
<img src="/CV-3D/images/trad/epipolar-4point1.png" alt="drawing" width="600"/>
<img src="/CV-3D/images/trad/epipolar-4point2.png" alt="drawing" width="600"/>

- Relation between Homography and Essential-Matrix
<img src="/CV-3D/images/trad/essential-homography.png" alt="drawing" width="600"/>

## The Uncalibrated Case
- Uncalibrated camera
- Fundamental matrix
<img src="/CV-3D/images/trad/fundamental-matrix.png" alt="drawing" width="600"/>