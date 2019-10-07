# Calibration

## Intrinsic
- K: mapping camera coord to pix coord;
- Intrinsic: K
```
[f,s,cx;
 0,f,cy;
 0,0,1]
```
- World to screen: x = KE p
- Screen to world: p ~ E(-1) K(-1) x
- s: skew, always assumed 0;
- Set the origin at image center; cx, cy = W/2, H/2

## Camera Matrix
- P = K[R|t], 3 x 4;

## Between Cameras
- x1 ~ K1 E1 p = K1 E1 E0(-1) K0(-1) x0

## Distortion
- xc = xc(1 + k1 r^2 + k2 r^4)
- yc = yc(1 + k1 r^2 + k2 r^4)

## Photometric formation
- BRDF (Bidirectional Reflectance Distribution Function)
- Diffuse reflection (Lambertian or matte reflection)
	- Scatter light uniformly
	- BRDF f(vi, vr, n, lambda) is constant;
- Specular reflection
	- Depends strongly on the direction of the outgoing light;
- Phong shading;
	- combined the diffuse and specular
- Di-chromatic reflection model
- Global illumination (ray tracing and radiosity)
- Optics:
	- Chromatic aberration: the index of refraction for glass varies slightly as a function of wavelength;
	- Vignetting: tendency for the brightness of the image to fall off towards the edge of the image;