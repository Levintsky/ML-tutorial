# Image/Video Inpainting

## Problem Definition
- Hole filling;
- Legacy: generally an engergy minimization problem:
- Formulation: patch not masked for inpainting should be consistent \
	<img src="/Generative/images/inpaint/inpaint-energy.png" alt="drawing" width="400"/>
- Geometry-aware: 2nd term same as above, first term for gemoetry reprojection error; \
	<img src="/Generative/images/inpaint/inpaint-energy-2.png" alt="drawing" width="400"/>
- Key trick: To preserve structure, patch priority computation specifies the patch filling order;

## Unclassified
- Z. Yan, X. Li, M. Li, W. Zuo, and S. Shan. Shift-net: Image inpainting via deep feature rearrangement. arxiv'18
	- U-Net;
- R. Mechrez, I. Talmi, F. Shama, and L. Zelnik-Manor. Learning to maintain natural image statistics. arxiv'18
	- relative distance measure
- R. Mechrez, I. Talmi, and L. Zelnik-Manor. The contextual loss for image transformation with non-aligned data. arxiv'18
	- relative distance measure
- I. Talmi, R. Mechrez, and L. Zelnik-Manor. Template matching with deformable diversity similarity. CVPR'17
	- relative distance measure

## Legacy
- **ZNCC**: Dirk Padfield. Masked object registration in the fourier domain. TIP'12
	- masked zero-normalized cross correlation;
- Progressive fill holes on the boundary by patch similarity:
	- Alexei A Efros and Thomas K Leung. Texture synthesis by non-parametric sampling. ICCV'99
	- Denis Simakov, Yaron Caspi, Eli Shechtman, and Michal Irani. Summarizing visual data using bidirectional similarity. CVPR'08
	- C. Barnes, E. Shechtman, A. Finkelstein, and D. B. Goldman. Patchmatch: A randomized correspondence algorithm for structural image editing. TOG'09
	- Soheil Darabi, Eli Shechtman, Connelly Barnes, Dan Goldman, and Pradeep Sen. Image melding: Combining inconsistent images using patch-based synthesis. TOG'12
	- Kaiming He and Jian Sun. Image completion approaches using the statistics of similar patches. PAMI'14
- Image gradient statistics:
	- Coloma Ballester, Marcelo Bertalmio, Vicent Caselles, Guillermo Sapiro, and Joan Verdera. Filling-in by joint interpolation of vector fields and gray levels. TIP'01
	- Patrick Perez, Michel Gangnet, and Andrew Blake. Poisson image editing. TOG'03
	- Shai Avidan and Ariel Shamir. Seam carving for content-aware image resizing. TOG'07
- Texture synthesis:
	- A. A. Efros and W. T. Freeman. Image quilting for texture synthesis and transfer. SIGGRAPH'01
	- A. Criminisi, P. Perez, and K. Toyama. Object removal by exemplar-based inpainting. CVPR'03
	- I. Drori, D. Cohen-Or, and H. Yeshurun. Fragment-based image completion. TOG'03
	- V. Kwatra, I. Essa, A. Bobick, and N. Kwatra. Texture optimization for example-based synthesis. TOG'05
	- M. Wilczkowiak, G. Brostow, B. Tordoff, and R. Cipolla. Hole fill through photomontage. BMVC'05
	- N. Komodakis. Image completion using global optimization. CVPR'06
	- N. Komodakis and G. Tziritas. Image completion using efficient belief propagation via priority scheduling and dynamic pruning. TIP'07
- Exemplar-based:
	- A. Criminisi, P. Pérez, and K. Toyama. Region filling and object removal by exemplar-based image inpainting. TIP'04
	- J. Jia and C.-K. Tang. Image repairing: Robust image synthesis by adaptive nd tensor voting. In CVPR'03
	- J. Jia and C.-K. Tang. Inference of segmented color and texture description by tensor voting. PAMI'04
	- J. Sun, L. Yuan, J. Jia, and H.-Y. Shum. Image completion with structure propagation. TOG'05

## Inpainting
- **Context-encoder**: Deepak Pathak, Philipp Krahenbuhl, Jeff Donahue, Trevor Darrell, and Alexei A Efros. Context encoders: Feature learning by inpainting. CVPR'16
	- Inpaint from surrounding context;
	- Insight: inpainting auto-encoder; loss: L2;
	- Problem: fixed size (resolution), fixed mask; \
	<img src="/Generative/images/inpaint/context-encoder.png" alt="drawing" width="400"/>
- Emily Denton, Sam Gross, and Rob Fergus. Semi-supervised learning with context-conditional generative adversarial networks. arxiv'16 (ICLR'17 reject)
	- Generalized from context encoder, with GAN loss; \
	<img src="/Generative/images/inpaint/ssl-gan.png" alt="drawing" width="400"/>
- Y Li, S Liu, J Yang, and M Yang. Generative Face Completion. CVPR'17
	- Problem setup: Face inpainting; 3 supervision!
	- Insight: denoise/inpainting autoencoder;
	- **Supervision**: local+global GAN; part parsing output; \
		<img src="/Generative/images/inpaint/face-inpaint.png" alt="drawing" width="400"/>
- Chao Yang, Xin Lu, Zhe Lin, Eli Shechtman, Oliver Wang, and Hao Li. High-resolution image inpainting using multi-scale neural patch synthesis. CVPR'17
	- Key insight: Deep PatchMatch (nearest + neighbor); MRF post-processing;
	- https://github.com/leehomyc/Faster-High-Res-Neural-Inpainting
	- Insight: 1. Pretrain a loss; 2. AE framework; 3. iterative;
	- Supervision loss: pretrained content loss and texture loss Ec and Et; content: with ground-truth + adv-loss; texture: nearest neighbor with VGG relu3 and relu4; \
		<img src="/Generative/images/inpaint/neural-inpaint-1.png" alt="drawing" width="400"/>
	- Generative model: \
		<img src="/Generative/images/inpaint/neural-inpaint-2.png" alt="drawing" width="400"/>
	- Start from infilling mean color x0, iteratively optimize: \
		<img src="/Generative/images/inpaint/neural-inpaint-3.png" alt="drawing" width="250"/>
- Raymond A Yeh, Chen Chen, Teck Yian Lim, Alexander Schwing, Mark Hasegawa-Johnson, and Minh N Do. Semantic image inpainting with deep generative models. CVPR'17
	- https://github.com/moodoki/semantic_image_inpainting
	- Key insight: manipulate z; \
		<img src="/Generative/images/inpaint/semantic-inpaint.png" alt="drawing" width="400"/>
- **Global-Local-GAN**: S Iizuka, E Simo-Serra, and H Ishikawa. Globally and locally consistent image completion. TOG'17
	- https://github.com/satoshiiizuka/siggraph2017_inpainting
	- Fully-Conv CNN;
	- Rely heavily on post-processing (Poisson blending, MRF, Kaiming's)
	- Supervision: GAN loss; \
		<img src="/Generative/images/inpaint/global-local.png" alt="drawing" width="400"/>
- **Deep-Prior**: D Ulyanov, A Vedaldi, V Lempitsky. Deep Image Prior. CVPR'18
	- https://dmitryulyanov.github.io/deep_image_prior
	- Insight: prior comes from the network structure and net parameter initialization;
	- Deep energy based, natural image should have low cost;
	- Optimize image iteration by iteration;
- Jiahui Yu, Zhe Lin, Jimei Yang, Xiaohui Shen, Xin Lu, and Thomas S Huang. Generative Image Inpainting with Contextual Attention. CVPR'18
	- Key insight: Contextual attention; deep nearest neighbor;
	- https://github.com/JiahuiYu/generative_inpainting \
		<img src="/Generative/images/inpaint/gen-inpaint-1.png" alt="drawing" width="500"/>
	- Contextual attention: foreground (missing pixels) and background attention;
		<img src="/Generative/images/inpaint/gen-inpaint-2.png" alt="drawing" width="400"/>
- W. Xian, P. Sangkloy, J. Lu, C. Fang, F. Yu, and J. Hays. Texturegan: Controlling deep image synthesis with texture patches. CVPR'18
	- https://github.com/janesjanes/Pytorch-TextureGAN
	- http://texturegan.eye.gatech.edu/ \
		<img src="/Generative/images/inpaint/texturegan.png" alt="drawing" width="400"/>
- **Partial-Conv**: G Liu, F Reda, K J Shih, T Wang, A Tao, and B Catanzaro. Image Inpainting for Irregular Holes Using Partial Convolutions. ECCV'18
	- Insight: Convolution is masked and re-normalized to utilize valid pixels only;
	- https://github.com/NVIDIA/partialconv
- **GMCNN**: Yi Wang, Xin Tao, Xiaojuan Qi, Xiaoyong Shen, Jiaya Jia. Image Inpainting via Generative Multi-column Convolutional Neural Networks. NIPS'18
	- https://github.com/shepnerd/inpainting_gmcnn \
	- 3 submodules: a generator to produce results, global local discriminators for adversarial training, and a pretrained VGG network [20] to calculate ID-MRF loss. In the testing phase, only the generator network is used. \
		<img src="/Generative/images/inpaint/gmcnn.png" alt="drawing" width="500"/>
	- ID-MRF (implicit diversified Markov random fields): direct NN: over-smooth result; relative distance encourages different patch find different candidate (otherwise softmax loss will be large); \
		<img src="/Generative/images/inpaint/gmcnn-1.png" alt="drawing" width="500"/>
	- Information fusion: spatial variant loss (close to the boundary are more constrained);  adversarial loss (WGAN);
- S Hong, X Yan, T Huang, H Lee. Learning Hierarchical Semantic Image Manipulation through Structured Representations. NIPS'18
	- Key insight: generate the semantic mask first;
	- https://github.com/xcyan/neurips18_hierchical_image_manipulation \
	<img src="/Generative/images/inpaint/hier-inpaint1.png" alt="drawing" width="500"/>
	<img src="/Generative/images/inpaint/hier-inpaint2.png" alt="drawing" width="500"/>
	<img src="/Generative/images/inpaint/hier-inpaint3.png" alt="drawing" width="500"/>
- Donghoon Lee, Sifei Liu, Jinwei Gu, Ming-Yu Liu, Ming-Hsuan Yang, and Jan Kautz. Context-aware synthesis and placement of object instances. NIPS'18
	- https://github.com/NVlabs/Instance_Insertion
- **SN-PatchGAN**: Yu, Z Lin, J Yang, X Shen, X Lu, T Huang. Free-Form Image Inpainting with Gated Convolution. ICCV'19
	- http://jiahuiyu.com/deepfill2
	- Input: sketches as guidance;
	- Improve on partial-conv on soft-gated conv;\
		<img src="/Generative/images/inpaint/sn-patchgan.png" alt="drawing" width="500"/>
- Tamar Rott Shaham, Tali Dekel, Tomer Michaeli. SinGAN: Learning a Generative Model from a Single Natural Image. ICCV'19 best paper

## User-Guided
- J.-Y. Zhu, P. Krähenbühl, E. Shechtman, and A. A. Efros. Generative visual manipulation on the natural image manifold. ECCV'16.
- R Zhang, J Zhu, P Isola, X Geng, A Lin, T Yu, and A Efros. Real-time user-guided image colorization with learned deep priors. 2017
- T Wang, M Liu, J Zhu, A Tao, J Kautz, and B Catanzaro. High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs. 2017
- **Scribbler network**: P Sangkloy, J Lu, C Fang, F Yu, and J Hays. 2017. Scribbler: Controlling Deep Image Synthesis With Sketch and Color. CVPR'17

## Video Inpainting
- V. Kwatra, A. Schodl, I. Essa, G. Turk, and A. Bobick. Graphcut textures: Image and video synthesis using graph cuts. SIGGRAPH'03
- Spatial temporal:
	- Eli Shechtman, Yaron Caspi, and Michal Irani. Space-time super-resolution. PAMI'05
	- Yonatan Wexler, Eli Shechtman, and Michal Irani. Space-time completion of video. PAMI'07
	- Alasdair Newson, Andres Almansa, Matthieu Fradet, Yann Gousseau, and Patrick Perez. Towards fast, generic video inpainting. ECVMP'13
- Optical flow:
	- Wei-Sheng Lai, Jia-Bin Huang, Oliver Wang, Eli Shechtman, Ersin Yumer, and Ming-Hsuan Yang. Learning blind video temporal consistency. ECCV'18
		- ConvLSTM;
	- Donghoon Lee, Tomas Pfister, and Ming-Hsuan Yang. Inserting videos into videos. CVPR'19
		- 1. optical flow;
		- 2. flow guided inpainting;
	- Rui Xu, Xiaoxiao Li, Bolei Zhou, and Chen Change Loy. Deep flow-guided video inpainting. CVPR'19
		- 1. optical flow;
		- 2. flow guided inpainting;
- Geometrically-Driven Dynamic Object Removal for Self-Driving Video Simulation. CVPR'20 submission
	- Problem setup: input: images, LiDAR, dynamic object mask (by detection/segmentation/label) and camera instrinsics, poses; 
	- 1. depth estimation;
		- 1.1 UPSNet for segmentation; 5 super-class: road, ground, vegetation, building, streetpole; 3d (depth?) interpolation; sky-mask: sky depth to infinity;
	- 2. correspondence on image; \
		<img src="/Generative/images/inpaint/dynamic-removal-align.png" alt="drawing" width="400"/>
	- 3. inpainting;
		- Rerun algorithm 1 from frames i' > i; (forward, backward) \
		<img src="/Generative/images/inpaint/dynamic-removal-inpaint.png" alt="drawing" width="400"/>
