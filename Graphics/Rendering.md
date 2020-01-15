# Rendering

## Differntiable Renderer
<img src="/Graphics/images/diff_render.jpg" alt="drawing" width="400"/>
<img src="/Graphics/images/vision.jpg" alt="drawing" width="400"/>
<img src="/Graphics/images/diff_render2.jpg" alt="drawing" width="400"/>

- Inverse Problems in Computer Vision Using Adversarial Imagination Priors. 2016
- Tung, H.-Y. F., Harley, A. W., Seto, W., and Fragkiadaki, K. Adversarial inverse graphics networks: Learning 2d-to3d lifting and image-to-image translation from unpaired supervision. ICCV'17.
- Differentiable Image Parameterizations. 2018
	- https://distill.pub/2018/differentiable-parameterizations/
- Single-Image SVBRDF Capture with a Rendering-Aware Deep Network. TOG'18
	- 4 outputs: diffuse albedo, specular albedo, roughness, normal
- Justin Johnson, Agrim Gupta, and Li Fei-Fei. Image generation from scene graphs. CVPR 2018
	- Step 1: Generate scene graph: S. Schuster, R. Krishna, A. Chang, L. Fei-Fei, and C. D. Manning. Generating semantically precise scene graphs from textual descriptions for improved image retrieval.
	- Step 2: generate image
- H Kato, Y Ushiku, T Harada. Neural 3d mesh renderer. CVPR'18.
- T Li, M Aittala, F Durand, and J Lehtinen. Differentiable monte carlo ray tracing through edge sampling. SIGGRAPH'18

## MIT
- **GPGP**:  Mansinghka, V. K., Kulkarni, T. D., Perov, Y. N., and Tenenbaum, J. Approximate bayesian image interpretation using generative probabilistic graphics programs. NIPS'13
- S Yao, T M H Hsu, J Zhu, J Wu, A Torralba, W T. Freeman, J B. Tenenbaum. 3D-Aware Scene Manipulation via Inverse Graphics, NIPS'18

## Toolbox
- https://github.com/tensorflow/graphics
- Differentiable graphics layers:
	- Spatial transformer
	- 6dof
	- Intrinsic camera modeling
	- Material modeling:

## Legacy
- A. Fitzgibbon, Y. Wexler, and A. Zisserman. Image-based rendering using image-based priors. IJCV'05
- P. E. Debevec, C. J. Taylor, and J. Malik. Modeling and rendering architecture from photographs: A hybrid geometry- and image-based approach. 1996