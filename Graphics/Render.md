# Rendering

## Basics
- Problem definition: reconstruting 3D model, textures and lighting from the rendered image;
<img src="/CV-3D/images/dr/diff_render.jpg" alt="drawing" width="400"/>
<img src="/CV-3D/images/dr/vision.jpg" alt="drawing" width="400"/>
<img src="/CV-3D/images/dr/diff_render2.jpg" alt="drawing" width="400"/>

## Classics
- Ray Casting;
- CSG:
	- Easy with ray casting;
	- Hard for explicit surface as a triangle mesh;
- Transformation:
	- Move the ray from World Space to Object Space, intersection, and then rotate back;
- Reflection, refraction:
	- Douglas Enright, Stephen Marschner, Ronald Fedkiw. Animation and Rendering of Complex Water Surfaces. SIGGRAPH'02
	- Glossy Reflection: multiple reflection rays; polished surface;
- Hierarchical (kd-tree):
	- Pros and cons of kd-tree:
		- Pros: Simple code, Efficient traversal, Can conform to data;
		- Cons: costly construction, not great if you work with moving objects;
	- Most people use the Surface Area Heuristic (SAH)
		- MacDonald and Booth. Heuristic for ray tracing using space subdivision. Visual Computer'90
	- Warren Hunt, William R. Mark, Gordon Stoll. Fast kd-tree Construction with an Adaptive Error-Bounded Heuristic. IRT'06
	- Kun Zhou, Qiming Hou, Rui Wang, Baining Guo. Real-Time KD-Tree Construction on Graphics Hardware. SIGGRAPH Asia'08
	- Hard core efficiency: Ingo Wald's PhD thesis: http://www.sci.utah.edu/~wald/PhD/
- **BRDF** (Bidirectional Reflectance Distribution Function):
	- Generally 3 ways:
		- 1. By measure: MERL database;
		- 2. Empirical (Phong);
		- 3. Physical-based (**Cook-Torrance**); used by current games and movies;
	- Resources:
		- Very nice summary: https://zhuanlan.zhihu.com/p/21376124
		- http://www.realtimerendering.com/
		- https://blog.selfshadow.com/publications/
	- MERL BRDF Database: Wojciech Matusik, Hanspeter Pfister, Matt Brand and Leonard McMillan. A Data-Driven Reflectance Model. TOG'03
		- Image-based acquisition;
		- https://www.merl.com/brdf/
		- http://people.csail.mit.edu/wojciech/BRDFDatabase/
		- **Disney brdf**:
			- https://github.com/wdas/brdf
			- http://www.disneyanimation.com/technology/brdf.html
	- **Microfacet**: water = tiny-mirros x n
		- K Torrance, E Sparrow. Theory for Off-Specular Reflection From Roughened Surfaces. 1967
		- James F. Blinn. Models of light reflection for computer synthesized pictures. 1977
		- **Cook-Torrance**: Robert L. Cook, Kenneth E. Torrance. A reflectance model for computer graphics. SIGGRAPH'81
		- Michael Ashikmin, Simon Premože, Peter S Shirley. A microfacet-based BRDF generator. SIGGRAPH'00

## Legacy
- A. Fitzgibbon, Y. Wexler, and A. Zisserman. Image-based rendering using image-based priors. IJCV'05
- P. E. Debevec, C. J. Taylor, and J. Malik. Modeling and rendering architecture from photographs: A hybrid geometry- and image-based approach. 1996

## Differentiable Rendering
- Resources:
	- **Kaolin**: https://github.com/NVIDIAGameWorks/kaolin
	- **Tensorflow**: https://www.tensorflow.org/graphics/api_docs/python/tfg/rendering
	- **pytorch3d**: https://github.com/facebookresearch/pytorch3d
- **Opendr**: Loper, M. M. and Black, M. J. Opendr: An approximate differentiable renderer. ECCV'14
	- General framework, not only for NN;
- **Neural-Renderer**: Hiroharu Kato, Yoshitaka Ushiku, and Tatsuya Harada. Neural 3D Mesh Renderer. CVPR'18
	- Problem: 1. single 2D image to mesh; 2. Mesh Editing;
	- Insight: differentiable; approximate GD; first mesh generative model;
	- http://hiroharu-kato.com/projects_en/neural_renderer.html
	- https://github.com/daniilidis-group/neural_renderer
	- Supervision: silhouette loss + smoothness loss;
	- Assumption: deform an existing mesh (not from scratch); preprocessed segmentation;
	- Evaluation: 13 classes from ShapeNet;\
		<img src="/CV-3D/images/dr/neural-dr.png" alt="drawing" width="500"/>
- T.-M. Li, M. Aittala, F. Durand, and J. Lehtinen. Differentiable monte carlo ray tracing through edge sampling. Siggraph Asia'18
- **DIB-R**: Wenzheng Chen, Jun Gao, Huan Ling, Edward Smith, Jaakko Lehtinen, Alec Jacobson, and Sanja Fidler. Learning to predict 3d objects with an interpolation-based differentiable renderer. NIPS'19
	- https://nv-tlabs.github.io/DIB-R/ \
		<img src="/CV-3D/images/dr/dib-r.png" alt="drawing" width="500"/>
- Shichen Liu, Tianye Li, Weikai Chen, and Hao Li. Soft rasterizer: A differentiable renderer for image-based 3d reasoning. ICCV'19
- Stephen Lombardi, Tomas Simon, Jason Saragih, Gabriel Schwartz, Andreas Lehrmann, Yaser Sheikh. Neural Volumes: Learning Dynamic Renderable Volumes From Images Paper Abstract Author Preprint Paper Video. SIGGRAPH'19
- Justus Thies, Michael Zollhofer Matthias Niessner. Deferred Neural Rendering: Image Synthesis using Neural Textures Paper Abstract Author Preprint Paper Video. SIGGRAPH'19
- Lingjie Liu, Weipeng Xu, Michael Zollhoefer, Hyeongwoo Kim, Florian Bernard, Marc Habermann, Wenping Wang, Christian Theobalt. Neural Rendering and Reenactment of Human Actor Videos. SIGGRAPH'19
- Shih-En Wei, Jason Saragih, Tomas Simon, Adam W. Harley, Stephen Lombardi, Michal Perdoch, Alexander Hypes, Dawei Wang, Hernan Badino, Yaser Sheikh. VR Facial Animation via Multiview Image Translation. SIGGRAPH'19
- Ohad Fried, Ayush Tewari, Michael Zollhofer, Adam Finkelstein, Eli Shechtman, Dan B Goldman, Kyle Genova, Zeyu Jin, Christian Theobalt, Maneesh Agrawala. Text-based Editing of Talking-head Video. SIGGRAPH'19

## Unclassified
- **GPGP**:  Mansinghka, V. K., Kulkarni, T. D., Perov, Y. N., and Tenenbaum, J. Approximate bayesian image interpretation using generative probabilistic graphics programs. NIPS'13
- Inverse Problems in Computer Vision Using Adversarial Imagination Priors. 2016
- Tung, H.-Y. F., Harley, A. W., Seto, W., and Fragkiadaki, K. Adversarial inverse graphics networks: Learning 2d-to3d lifting and image-to-image translation from unpaired supervision. ICCV'17.
- Differentiable Image Parameterizations. 2018
	- https://distill.pub/2018/differentiable-parameterizations/
- Single-Image SVBRDF Capture with a Rendering-Aware Deep Network. TOG'18
	- 4 outputs: diffuse albedo, specular albedo, roughness, normal
- H Kato, Y Ushiku, T Harada. Neural 3d mesh renderer. CVPR'18.
- T Li, M Aittala, F Durand, and J Lehtinen. Differentiable monte carlo ray tracing through edge sampling. SIGGRAPH'18
- Thu H. Nguyen-Phuoc, Chuan Li, Stephen Balaban, Yongliang Yang. RenderNet: A deep convolutional network for differentiable rendering from 3D shapes. NIPS'18
- Wang Yifan, Felice Serena, Shihao Wu, Cengiz Öztireli, and Olga Sorkine-Hornung. 1343 2019. Differentiable Surface Splatting for Point-based Geometry Processing. TOG'19
- L Jain, W Wu, S Chen, U Jang, V Chandrasekaran, S Seshia, S Jha. Generating Semantic Adversarial Examples with Differentiable Rendering. ICLR'20 reject

## Toolbox
- https://github.com/tensorflow/graphics
- Differentiable graphics layers:
	- Spatial transformer
	- 6dof
	- Intrinsic camera modeling
	- Material modeling:
- W. Jakob, Mitsuba renderer, 2010, http://www.mitsuba-renderer.org.
