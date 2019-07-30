# Multiview Geometry

## Textbook
- R Hartley and A Zisserman. Multiple View Geometry in Computer Vision.
- O Faugeras and Q Luong. The Geometry from Multiple Images

- Mark Pollefeys:
	- http://www.cs.unc.edu/~marc/tutorial/

## Background
- Projective geometry (2D, 3D)
	<img src="/CV-3D/images/mvg/transformation.png" alt="drawing" width="600"/>

- Parameter estimation
- Algorithm evaluation

## Single View
- Rigid-body motion
	<img src="/CV-3D/images/mvg/rigid-body-motion.png" alt="drawing" width="600"/>

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
