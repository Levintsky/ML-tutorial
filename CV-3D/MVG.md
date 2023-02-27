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
	- Conics: x†Qx = 0
- 3D:
	- Points: (x, y, z, w);
	- Planes: ax + by + cz + d = 0;
	- Lines: (1-λ)p + λ q; L=pq-qp (Plucker coordinate);
	- Quadrics: x†Qx = 0
- 2D-Transformation:\
	- Translation: [I|t]; 2-dof
	- Rigit: [R|t]; 3
	- similarity: [sR|t]; 4
	- Affine: [A]2x3; 6
	- Projective: [H]3x3; 8
- 3D-Transformation:
	- Translation: [I|t]; 3-dof
	- Rigit: [R|t]; 6
	- similarity: [sR|t]; 7
	- Affine: [A]3x4; 12
	- Projective: [H]4x4; 15
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
	- 3D to 2D (world-to-screen):
		- P = K[R|T]; x=PX=KEX;
		- T = -Rc, with c as the camera center;
		- R = [R-camx†; R-camy†; R-camz†], row vector as the
	- Screen to world: X ~ E(-1) K(-1) x;
	- Camera to camera (assume z known):\
		<img src="/CV-3D/images/mvg/cam-cam.png" alt="drawing" width="400"/>
	- Planar scene: homography: x1 = H x0

## Geometric intrinsic calibration (Rick Szeliski, Chap 6.3)
- Calibration patterns: one 3D, or moving 2D
- Vanishing points: from a pair of orthogonal, we can estimate focal length

## Structure From Motion
- Rick Szeliski, Chap 7
	- Triangulation: determining a point's (x,y, z) from multi-images with known camera pose;
	- Pj=Kj[Rj|tj], where tj=-Rjcj and cj is ith camera center;
	- Two-frame structure from motion:
		- Calibrated: essential matrix (rank deficient b/c Et=0), chirality (a positive distance along the viewing rays emanating from the camera)
		- t=c1-c0, p-c1, p-c0 co-plane;
		- x1† E x0 = 0;
		- E = [t]R
		- E = U∑V†; (rank-2)
			- ∑ = [1 0 0]
			-     [0 1 0]
			-     [0 0 0]
		- Projective (uncalibrated) reconstruction: Fundamental matrix
	- Factorization: M is 2M × 3 and the structure matrix S is 3 × N; SVD of rank 3;
		<img src="/CV-3D/images/mvg/factor-1.png" alt="drawing" width="400"/>
	- Bundle adjustment;
- C. Wu. VisualSFM: A visual structure from motion system. http://ccwu.me/vsfm, 2011

## Stereo
- Rick Szeliski, Chap 11
	- Epipolar geometry;
		- Rectification: make the epipolar line horizontal;
		- Rectified geometry: x'=x+fB/Z; y'=y; B: baseline;
		- Plane sweep: assume calibrated; depth proposals + robust matching;
			<img src="/CV-3D/images/mvg/plane-sweep-1.png" alt="drawing" width="400"/>\
			<img src="/CV-3D/images/mvg/plane-sweep-2.png" alt="drawing" width="400"/>
		- Sparse correspondence;
		- Dense correspondence;
			- Cost: SSD, SAD, MSE, MAD;
		- Local methods:
		- Global methods: MRF;
		- Multi-view stereo;
			- Volumetric and 3D surface reconstruction;
			- Shape from silhouettes;

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
	- x2† TR x1 = 0 (vectors coplane)
	- E = TR
- Estimate essential matrix: 8-point linear algorithm
	- x2† E x1 = 0
	- a = [x1x2, x1y2, x1z2, y1x2, y1y2, y1z2, z1x2, z1y2, z1z2]
	- a† E = 0
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
- D Nister. An Efficient Solution to the Five-Point Relative Pose Problem. PAMI'05
- J Kileel. Minimal Problems for the Calibrated Trifocal Variety. 2016
	- https://math.berkeley.edu/~jkileel/CalibratedMinimalProblems.html
- T Duff, K Kohn, A Leykin, T Pajdla. PLMP-Point-Line Minimal Problems in Complete Multi-View Visibility. ICCV'19 best student paper award
