# Multiview Geometry

## Textbook
- R Hartley and A Zisserman. Multiple View Geometry in Computer Vision.
- O Faugeras and Q Luong. The Geometry from Multiple Images
- Mark Pollefeys:
	- http://www.cs.unc.edu/~marc/tutorial/

## Geometric primitives and transformations (Rick Szeliski, Chap 2.1)
- 2D:
	- Points: (x, y), or (x', y', w) = w(x, y, 1)
	- Lines: ax + by + c = 0. so (n, d), n is normal;
	- Conics: x^T Q x = 0
- 3D:
	- Points: (x, y, z, w);
	- Planes: ax + by + cz + d = 0;
	- Lines: (1-lambda)p + lambda q; L=pq-qp (Plucker coordinate);
	- Quadrics: x^T Q x = 0
- 2D-Transformation:\
	<img src="/CV-3D/images/mvg/2d-transform.png" alt="drawing" width="400"/>
- 2D-Transformation:\
	<img src="/CV-3D/images/mvg/3d-transform.png" alt="drawing" width="400"/>
- 3D rotation:
	- Euler Angle: x, y, z rotation or x, y, x rotation; gimbal lock;
		- Cross product in matrix form:\
			<img src="/CV-3D/images/mvg/cross-product.png" alt="drawing" width="400"/>
		- Rodriguez's formula:\
			<img src="/CV-3D/images/mvg/rodriguez.png" alt="drawing" width="400"/>
		- Exponential form:\
			<img src="/CV-3D/images/mvg/euler-exp.png" alt="drawing" width="400"/>
	- Quaternion (check math section);
- Camera matrix:
	- Intrinsic: K = [f,s,cx; 0,f,cy; 0,0,1]
		- Mapping camera coord to pix coord;
		- s: skew, always assumed 0;
		- Set the origin at image center; cx, cy = W/2, H/2
		- Distortion:
			- xc = xc(1 + k1 r^2 + k2 r^4)
			- yc = yc(1 + k1 r^2 + k2 r^4)
	- **3D to 2D** (world-to-screen):
		- P = K[R\|T]; x=PX=KEX;
		- T = -Rc, with c as the camera center;
		- R = [R-camx^T; R-camy^T; R-camz^T], row vector as the 
	- Screen to world: X ~ E(-1) K(-1) x;
	- Camera to camera (assume z known):\
		<img src="/CV-3D/images/mvg/cam-cam.png" alt="drawing" width="400"/>
	- Planar scene: homography: x1 = H x0

## Geometric intrinsic calibration (Rick Szeliski, Chap 6.3)
- Calibration patterns: one 3D, or moving 2D\
	<img src="/CV-3D/images/mvg/pattern.png" alt="drawing" width="400"/>
- Vanishing points: from a pair of orthogonal, we can estimate focal length\
	<img src="/CV-3D/images/mvg/vanish-1.png" alt="drawing" width="400"/>\
	<img src="/CV-3D/images/mvg/vanish-2.png" alt="drawing" width="400"/>

## Structure From Motion
- Rick Szeliski, Chap 7
	- Triangulation: determining a point's 3D position from a set of corresponding image locations and known camera positions is known as triangulation; Pj=Kj[Rj\|tj], where tj=-Rjcj and cj is ith camera center;
		<img src="/CV-3D/images/mvg/triangulate.png" alt="drawing" width="400"/>
	- Two-frame structure from motion:
		- Calibrated: essential matrix (rank deficient b/c Et=0), chirality (a positive distance along the viewing rays emanating from the camera)\
			<img src="/CV-3D/images/mvg/essential-1.png" alt="drawing" width="400"/>\
			<img src="/CV-3D/images/mvg/essential-2.png" alt="drawing" width="400"/>\
			<img src="/CV-3D/images/mvg/essential-3.png" alt="drawing" width="400"/>
		- Projective (uncalibrated) reconstruction: Fundamental matrix\
			<img src="/CV-3D/images/mvg/fundamental.png" alt="drawing" width="400"/>
	- Factorization:
- C. Wu. VisualSFM: A visual structure from motion system. http://ccwu.me/vsfm, 2011

## Misc
- Parameter estimation
- Algorithm evaluation

## Single View
- Rigid-body motion
	<img src="/CV-3D/images/mvg/rigid-body-summary.png" alt="drawing" width="600"/>

- Camera model
- Calibration
- Single View Geometry.

## Two Views
- Epipolar Geometry, Essential matrix
	<img src="/CV-3D/images/mvg/epipolar-constraint1.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/mvg/epipolar-constraint2.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/mvg/epipolar-constraint3.png" alt="drawing" width="600"/>

- Estimate essential matrix: 8-point linear algorithm
	<img src="/CV-3D/images/mvg/8point.png" alt="drawing" width="600"/>
	<img src="/CV-3D/images/mvg/8point-2.png" alt="drawing" width="600"/>

- 3D reconstruction
- Computing F, Computing structure, Plane and homographies.

## Three Views
- Trifocal Tensor, Computing T.

## More Views
- N-Linearities
- Multiple view reconstruction
- Bundle adjustment, auto-calibration, Dynamic SfM, Cheirality, Duality

## Theory, Minimal-Problems
- http://cmp.felk.cvut.cz/old_pages/mini/
- David Nister. An Efficient Solution to the Five-Point Relative Pose Problem. PAMI'05
- Joe Kileel. Minimal Problems for the Calibrated Trifocal Variety. 2016
	- https://math.berkeley.edu/~jkileel/CalibratedMinimalProblems.html
- Timothy Duff, Kathlen Kohn, Anton Leykin, Tomas Pajdla. PLMP- Point-Line Minimal Problems in Complete Multi-View Visibility. ICCV'19 best student paper award
