# Rendering

## Classics
- CSG:
	- Easy with ray casting;
	- Hard for explicit surface as a triangle mesh;
- Transformation:
	- Move the ray from World Space to Object Space, intersection, and then rotate back;
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
- Texture mapping and shaders:
	- Two approaches: texture mapping; procedural (shader);
	- Texture mapping:
		- Barycentric, uv-coordinate, lookup;
		- Kai Hormann, Bruno Lévy and Alla Sheffer. Mesh Parameterization: Theory and Practice. ACM SIGGRAPH Course Notes, 2007
			- http://alice.loria.fr/index.php/publications.html?redirect=0&Paper=SigCourseParam@2007&Author=Levy
		- Normal mapping;
	- Procedural:
		- **Perlin noise**: Ken Perlin. An image synthesizer. SIGGRAPH'85
		- https://mrl.nyu.edu/~perlin/noise/
		- Ken Perlin. Improving Noise. SIGGRAPH'02

## Differentiable Rendering
- I. Gkioulekas, S. Zhao, K. Bala, T. Zickler, and A. Levin. Inverse volume rendering with material dictionaries. TOG'13
- **Opendr**: Loper, M. M. and Black, M. J. Opendr: An approximate differentiable renderer. ECCV'14
	- General framework, not only for NN;
- I. Gkioulekas, A. Levin, and T. Zickler. An evaluation of computational imaging techniques for heterogeneous inverse scattering. ECCV'16
- T.-M. Li, M. Aittala, F. Durand, and J. Lehtinen. Differentiable monte carlo ray tracing through edge sampling. Siggraph Asia'18
	- https://github.com/BachiLi/redner
	- https://people.csail.mit.edu/tzumao/diffrt/
- **3d-rcnn**: Abhijit Kundu, Yin Li, and James M. Rehg. 3d-rcnn: Instance-level 3d object reconstruction via render-and-compare. CVPR'18
	- https://abhijitkundu.info/projects/3D-RCNN/
	- Input: 2D image;
	- Output: 3D scene;
	- Supervision: differentiable rendering loss;
- Stephen Lombardi, Tomas Simon, Jason Saragih, Gabriel Schwartz, Andreas Lehrmann, Yaser Sheikh. Neural Volumes: Learning Dynamic Renderable Volumes From Images Paper Abstract Author Preprint Paper Video. SIGGRAPH'19
- Justus Thies, Michael Zollhofer, Matthias Niessner. Deferred Neural Rendering: Image Synthesis using Neural Textures. SIGGRAPH'19
- Lingjie Liu, Weipeng Xu, Michael Zollhoefer, Hyeongwoo Kim, Florian Bernard, Marc Habermann, Wenping Wang, Christian Theobalt. Neural Rendering and Reenactment of Human Actor Videos. SIGGRAPH'19
- Shih-En Wei, Jason Saragih, Tomas Simon, Adam W. Harley, Stephen Lombardi, Michal Perdoch, Alexander Hypes, Dawei Wang, Hernan Badino, Yaser Sheikh. VR Facial Animation via Multiview Image Translation. SIGGRAPH'19
- Ohad Fried, Ayush Tewari, Michael Zollhofer, Adam Finkelstein, Eli Shechtman, Dan B Goldman, Kyle Genova, Zeyu Jin, Christian Theobalt, Maneesh Agrawala. Text-based Editing of Talking-head Video. SIGGRAPH'19
- Yuxuan Zhang, Wenzheng Chen, Huan Ling, Jun Gao, Yinan Zhang, Antonio Torralba, Sanja Fidler. Image gans meet differentiable rendering for inverse graphics and interpretable 3d neural rendering. 2020

## Applications
- 3D face reconstruction:
	- E. Richardson, M. Sela, R. Or-El, and R. Kimmel. Learning detailed face reconstruction from a single image. CVPR'17
	- A. Tewari, M. Zollhofer, P. Garrido, F. Bernard, H. Kim, P. Perez, and C. Theobalt. Self-supervised multi-level face model learning for monocular reconstruction at over 250 hz. CVPR'18
	- A. Tewari, M. Zollhofer, H. Kim, P. Garrido, F. Bernard, P. Perez, and C. Theobalt. Mofa: Model-based deep convolutional face autoencoder for unsupervised monocular reconstruction. ICCV'17
	- L. Tran and X. Liu. Nonlinear 3d face morphable model. CVPR'18
	- K. Genova, F. Cole, A. Maschinot, A. Sarna, D. Vlasic, and W. T. Freeman. Unsupervised training for 3d morphable model regression. CVPR'18
- Material inference:
	- V. Deschaintre, M. Aittala, F. Durand, G. Drettakis, and A. Bousseau. Single-image svbrdf capture with a renderingaware deep network. TOG'18
	- G. Liu, D. Ceylan, E. Yumer, J. Yang, and J.-M. Lien. Material editing using a physically based rendering network. ICCV'17
- 3D reconstruction:
	- D. J. Rezende, S. A. Eslami, S. Mohamed, P. Battaglia, M. Jaderberg, and N. Heess. Unsupervised learning of 3d structure from images. NIPS'16
	- O. Nalbach, E. Arabadzhiyska, D. Mehta, H.-P. Seidel, and T. Ritschel. Deep shading: convolutional neural networks for screen space shading. CGF'17
	- P. Henderson and V. Ferrari. Learning to generate and reconstruct 3d meshes with only 2d supervision. BMVC'18
	- A. Kundu, Y. Li, and J. M. Rehg. 3d-rcnn: Instance-level 3d object reconstruction via render-and-compare. CVPR'18
	- T. Nguyen-Phuoc, C. Li, S. Balaban, and Y. Yang. Rendernet: A deep convolutional network for differentiable rendering from 3d shapes. arxiv'18

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
