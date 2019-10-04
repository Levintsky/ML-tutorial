# Calibration

## Intrinsic
- K: mapping pix coord to camera coord
- Intrinsic: K
```
[f,s,cx;
 0,f,cy]
 0,0,1]
```
- World to screen: x = KE p
- Screen to world: p ~ E(-1) K(-1) x
- s: skew, always assumed 0;
- Set the origin at image center; cx, cy = W/2, H/2

## Between Cameras
- x1 ~ K1 E1 p = K1 E1 E0(-1) K0(-1) x0

## Photometric formation
- BRDF (Bidirectional Reflectance Distribution Function)
- Phong shading;