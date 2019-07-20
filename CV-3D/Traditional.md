# Traditional 3D

## Camera
- Intrinsic K: camera matrix; (skewness, distortion); extrinsic
	<img src="/CV-3D/images/tra-eqn1.png" alt="drawing" width="300"/>
	<img src="/CV-3D/images/tra-eqn2.png" alt="drawing" width="300"/>

- Calibration:

## Single-View Geometry
- Vanishing Points and Lines
- Find w s.t. v1 * w * v2 = 0 always hold;
	<img src="/CV-3D/images/van1.png" alt="drawing" width="400"/>
	<img src="/CV-3D/images/van2.png" alt="drawing" width="300"/>

## Epipolar Geometry
- Baseline, epipolar plane,
- Two image planes parallel: e, e' infinity;
	<img src="/CV-3D/images/epipolar.png" alt="drawing" width="600"/>

- Essential matrix; (for canonical cameras)
- Fundamental matrix;

## MVS, Structure from Motion
- Many cameras, each Mi for each image;
- SVD;
- Bundle adjustment;

## Active Volumetric Stereo
- Space carving;
<img src="/CV-3D/images/space-carving.png" alt="drawing" width="500"/>
