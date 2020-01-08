# Image Inpainting

## Inpainting
- **Deep-Prior**: D Ulyanov, A Vedaldi, V Lempitsky. Deep Image Prior. 
	- https://dmitryulyanov.github.io/deep_image_prior
	- Deep energy based, natural image should have low cost;
	- Optimize image iteration by iteration;
- **SN-PatchGAN**: Yu, Z Lin, J Yang, X Shen, X Lu, T Huang. Free-Form Image Inpainting with Gated Convolution
	- http://jiahuiyu.com/deepfill2
	- Input: sketches as guidance;
	- Improve on partial-conv on soft-gated conv;\
		<img src="/Graphics/images/sn-patchgan.png" alt="drawing" width="600"/>
- S Hong, X Yan, T Huang, H Lee. Learning Hierarchical Semantic Image Manipulation through Structured Representations. NIPS'18
	<img src="/Graphics/images/hier-inpaint1.png" alt="drawing" width="600"/>
	<img src="/Graphics/images/hier-inpaint2.png" alt="drawing" width="600"/>
	<img src="/Graphics/images/hier-inpaint3.png" alt="drawing" width="600"/>
- See and Think: Disentangling Semantic Scene Completion. NIPS'18
- Image Inpainting via Generative Multi-column Convolutional Neural Networks (Jiaya Jia). NIPS'18
- **Partial-Conv**: G Liu, F Reda, K J Shih, T Wang, A Tao, and B Catanzaro. 2018. Image Inpainting for Irregular Holes Using Partial Convolutions. 2018
	- Convolution is masked and re-normalized to utilize valid pixels only
- **Global-Local-GAN**: S Iizuka, E Simo-Serra, and H Ishikawa. 2017. Globally and locally consistent image completion. TOG'17
	- Fully-Conv CNN
	- Rely heavily on post-processing (Poisson blending, MRF, Kaiming's)
- Jiahui Yu, Zhe Lin, Jimei Yang, Xiaohui Shen, Xin Lu, and Thomas S Huang. 2018. Generative Image Inpainting with Contextual Attention. 2018
- W. Xian, P. Sangkloy, J. Lu, C. Fang, F. Yu, and J. Hays. Texturegan: Controlling deep image synthesis with texture patches. CVPR'18

## User-Guided
- J.-Y. Zhu, P. Krähenbühl, E. Shechtman, and A. A. Efros. Generative visual manipulation on the natural image manifold. ECCV'16.
- R Zhang, J Zhu, P Isola, X Geng, A Lin, T Yu, and A Efros. Real-time user-guided image colorization with learned deep priors. 2017
- T Wang, M Liu, J Zhu, A Tao, J Kautz, and B Catanzaro. High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs. 2017
- **Scribbler network**: P Sangkloy, J Lu, C Fang, F Yu, and J Hays. 2017. Scribbler: Controlling Deep Image Synthesis With Sketch and Color. CVPR'17

## Specific Category
- Y Li, S Liu, J Yang, and M Yang. Generative Face Completion. 2017

## Legacy
- C. Barnes, E. Shechtman, A. Finkelstein, and D. B. Goldman. Patchmatch: A randomized correspondence algorithm for structural image editing. TOG'09