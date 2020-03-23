# Differentiable Rendering

## Basics
<img src="/CV-3D/images/dr/diff_render.jpg" alt="drawing" width="400"/>
<img src="/CV-3D/images/dr/vision.jpg" alt="drawing" width="400"/>
<img src="/CV-3D/images/dr/diff_render2.jpg" alt="drawing" width="400"/>

## Legacy
- A. Fitzgibbon, Y. Wexler, and A. Zisserman. Image-based rendering using image-based priors. IJCV'05
- P. E. Debevec, C. J. Taylor, and J. Malik. Modeling and rendering architecture from photographs: A hybrid geometry- and image-based approach. 1996

## Classics
- Problem definition: reconstruting 3D model, textures and lighting from the rendered image;
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
- **DIB-R**: Wenzheng Chen, Jun Gao, Huan Ling, Edward Smith, Jaakko Lehtinen, Alec Jacobson, and Sanja Fidler. Learning to predict 3d objects with an interpolation-based differentiable renderer. NIPS'19
	- https://nv-tlabs.github.io/DIB-R/ \
		<img src="/CV-3D/images/dr/dib-r.png" alt="drawing" width="500"/>
- Shichen Liu, Tianye Li, Weikai Chen, and Hao Li. Soft rasterizer: A differentiable renderer for image-based 3d reasoning. ICCV'19

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
