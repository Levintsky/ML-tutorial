# Rendering

## Differntiable Renderer
<img src="/Graphics/images/diff_render.jpg" alt="drawing" width="400"/>
<img src="/Graphics/images/vision.jpg" alt="drawing" width="400"/>
<img src="/Graphics/images/diff_render2.jpg" alt="drawing" width="400"/>

- M Loper, M Black. OpenDR: An approximate differentiable renderer. ECCV'14
- Inverse Problems in Computer Vision Using Adversarial Imagination Priors. 2016
- Tung, H.-Y. F., Harley, A. W., Seto, W., and Fragkiadaki, K. Adversarial inverse graphics networks: Learning 2d-to3d lifting and image-to-image translation from unpaired supervision. ICCV'17.
- Differentiable Image Parameterizations. 2018
	- https://distill.pub/2018/differentiable-parameterizations/
- Single-Image SVBRDF Capture with a Rendering-Aware Deep Network. TOG'18
	- 4 outputs: diffuse albedo, specular albedo, roughness, normal
- Justin Johnson, Agrim Gupta, and Li Fei-Fei. Image generation from scene graphs. CVPR 2018
	- Step 1: Generate scene graph: S. Schuster, R. Krishna, A. Chang, L. Fei-Fei, and C. D. Manning. Generating semantically precise scene graphs from textual descriptions for improved image retrieval.
	- Step 2: generate image
<img src="/Graphics/images/scene_graph.png" alt="drawing" width="600"/>


## MIT
- **GPGP**:  Mansinghka, V. K., Kulkarni, T. D., Perov, Y. N., and Tenenbaum, J. Approximate bayesian image interpretation using generative probabilistic graphics programs. NIPS'13
- **Picture**: Kulkarni, T. D., Kohli, P., Tenenbaum, J. B., and Mansinghka, V. Picture: A probabilistic programming language for scene perception. CVPR'15
- **DC-IGN**: Kulkarni, T. D., Whitney, W. F., Kohli, P., and Tenenbaum, J. Deep convolutional inverse graphics network. NIPS'15
<img src="/Graphics/images/dc_ign.png" alt="drawing" width="600"/>

- J Wu, JB Tenenbaum, P Kohli. Neural scene de-rendering. CVPR'17

## Toolbox
- https://github.com/tensorflow/graphics
- Differentiable graphics layers:
	- Spatial transformer
	- 6dof
	- Intrinsic camera modeling
	- Material modeling: