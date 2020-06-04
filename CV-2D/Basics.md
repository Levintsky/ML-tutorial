# Basics

## Courses
- http://www.cs.washington.edu/education/courses/455/
- http://www.cs.washington.edu/education/courses/576/
- http://vision.stanford.edu/teaching/cs223b/
- http://www.cs.washington.edu/education/courses/558/06sp/ 14 http://graphics.cs.cmu.edu/courses/15-463/

## Textbooks
- Richard Hartley, Andrew Zisserman. Multiple view geometry in computer vision.
- Richard Szeliski. Computer Vision: Algorithms and Applications. 2010

## Image Formation
- Rick Szeliski, Chap 2.2;
- BRDF (Bidirectional Reflectance Distribution Function)
	- Incident: vi; reflected: vr; most surfaces: isotropic;
		<img src="/CV-2D/images/basics/brdf-1.png" alt="drawing" width="400"/>
	- http://www1.cs.columbia.edu/CAVE/software/curet/
- Diffuse (Lambertian or matte reflection):
	- scatters light uniformly in all directions; most normally associate with shading;
		<img src="/CV-2D/images/basics/diffuse-1.png" alt="drawing" width="350"/>\
		<img src="/CV-2D/images/basics/diffuse-2.png" alt="drawing" width="400"/>
- Specular reflection: specular (gloss or highlight) reflection;
	<img src="/CV-2D/images/basics/reflect-1.png" alt="drawing" width="400"/>\
	<img src="/CV-2D/images/basics/reflect-2.png" alt="drawing" width="400"/>\
	<img src="/CV-2D/images/basics/reflect-3.png" alt="drawing" width="400"/>
- Phong shading: ambient + diffuse + reflect;\
	<img src="/CV-2D/images/basics/phong.jpg" alt="drawing" width="400"/>
- Optics:
	- Chromatic aberration;
	- Vignetting;
	- Shutter speed;
	- Sampling pitch;
	- Fill factor;
	- Chip size;
	- Analog gain;
	<img src="/CV/images/basics/optics.png" alt="drawing" width="400"/>

## Image Processing
- Rick Szeliski, Chap 3;
- Point operators
	- Pixel transforms
	- Color transforms
	- Compositing and matting
	- Histogram equalization
	- Application: Tonal adjustmen
- Linear filtering
	- Separable filtering
	- Examples of linear filtering
	- Band-pass and steerable filters
- More neighborhood operators
	- Non-linear filtering: median, bilateral; Iterated adaptive smoothing and anisotropic diffusion;
	- Morphology: dilation, erosion, majority, opening, closing;
	- Distance transforms
	- Connected components
- Fourier transforms
	- Fourier transform pairs
	- Two-dimensional Fourier transforms
	- Wiener filtering
	- Application: Sharpening, blur, and noise removal
- Pyramids and wavelets
	- Interpolation
	- Decimation
	- Multi-resolution representations
	- Wavelets
	- Application: Image blending
- Geometric transformations
	- Parametric transformations 
	- Application: Feature-based morphing
- Global optimization
	- Regularization
	- Markov random fields
	- Application: Image restoration

## Feature Detection, Matching
- Rick Szeliski, Chap 4;
- Points and patches;
	- Feature detectors: Harris; DoG;
	- Feature descriptors: MOPS, SIFT, PCA-SIFT, GLOH;
	- Feature matching;
	- Feature tracking;
	- Application: Performance-driven animation;
- Edges:
	- Edge detection;
	- Edge linking;
	- Application: Edge editing and enhancement
- Lines;
	- Successive approximation;
	- Hough transforms;
	- Vanishing points;
	- Application: Rectangle detection;
