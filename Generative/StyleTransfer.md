# Style Transfer

## Tutorial
- Y Jing, Y Yang, Z Feng, J Ye, Y Yu, and M Song. Neural Style Transfer: A Review. TVCG 2018
	- https://www.jiqizhixin.com/articles/2018-05-15-5
	- https://github.com/ycjing/Neural-Style-Transfer-Papers
<img src="/Generative/images/style-transfer.png" alt="drawing" width="600"/>

- Style-Transfer in text: https://github.com/fuzhenxin/Style-Transfer-in-Text

## Classic
- **CRN**: Q Chen, V Koltun. Photographic Image Synthesis with Cascaded Refinement Networks. ICCV'17
- **Cycle-GAN**: Zhu, J.-Y., Park, T., Isola, P., and Efros, A. A. Unpaired image-to-image translation using cycle-consistent adversarial networks. CVPR 2017
<img src="/Generative/images/cycle-gan.png" alt="drawing" width="500"/>

	- https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
	- G: X -> Y; discriminator: D_Y;
	- F: Y -> X; discriminator: D_X;
	- Adversarial loss: E[logD_Y(y)] + E[log(1-D_Y(G(x)))]
	- Similar loss for D_X
	- Consistency loss: ||F(G(x))-x|| + ||G(F(y))-y|| with L1 norm
- **pix2pix**: Isola, P., Zhu, J.-Y., Zhou, T., and Efros, A. A. Image-to-image translation with conditional adversarial networks. CVPR, 2017.
<img src="/Generative/images/pix2pix1.png" alt="drawing" width="250"/>
<img src="/Generative/images/pix2pix2.png" alt="drawing" width="330"/>

## Image Optimization-based
- Parametric:
<img src="/Generative/images/neural-style1.png" alt="drawing" width="250"/>

	- L. A. Gatys, A. S. Ecker, and M. Bethge, Texture Synthesis Using Convolutional Neural Networks. NIPS'15
	- L. A. Gatys, A. S. Ecker, and M. Bethge, A neural algorithm of artistic style. 2015
	- L. A. Gatys, A. S. Ecker, and M. Bethge, Image style transfer using convolutional neural networks, CVPR'16
	- G. Berger and R. Memisevic, Incorporating long-range consistency in cnn-based texture generation, ICLR'17
	- A. Mahendran and A. Vedaldi, Understanding deep image representations by inverting them, CVPR'15
	- A. Mordvintsev, C. Olah, and M. Tyka, “Inceptionism: Going deeper into neural networks,” 2015 [Online]. Available: https://research.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html
	- Visualizing deep convolutional neural networks using natural pre-images, IJCV'16
	- Y. Li, N. Wang, J. Liu, and X. Hou, Demystifying neural style transfer. IJCAI'17
		- Theoretically, Gram is similar to minimize MMD (mean and variance matches)
	- S. Li, X. Xu, L. Nie, and T.-S. Chua, “Laplacian-steered neural style transfer, ACMMM'07
	- V. M. Patel, R. Gopalan, R. Li, and R. Chellappa, Visual domain adaptation: A survey of recent advances, SPM'15.
- Non-Parametric:
	-  C. Li and M. Wand, Combining markov random fields and convolutional neural networks for image synthesis, CVPR'16

## Model-based
- **PSPM** (Per-Style-Per-Model)
	- J. Johnson, A. Alahi, and L. Fei-Fei, Perceptual losses for realtime style transfer and super-resolution. ECCV'16
	- D. Ulyanov, V. Lebedev, A. Vedaldi, and V. Lempitsky, Texture networks: Feed-forward synthesis of textures and stylized images. ICML'16
	- D. Ulyanov, A. Vedaldi, and V. Lempitsky, Improved texture networks: Maximizing quality and diversity in feed-forward stylization and texture synthesis. CVPR'17
		- **Instance-Normalization**
	- C. Li and M. Wand, Precomputed real-time texture synthesis with markovian generative adversarial networks. ECCV'16
- **MSPM** (Multiple-Style-Per-Model):
	- **CIN**: V. Dumoulin, J. Shlens, and M. Kudlur, A learned representation for artistic style, ICLR'17
		- CIN (Conditional Instance Normalization)
	- D. Chen, L. Yuan, J. Liao, N. Yu, and G. Hua, Stylebank: An explicit representation for neural image style transfer, CVPR'17
	- Y. Li, F. Chen, J. Yang, Z. Wang, X. Lu, and M.-H. Yang, Diversified texture synthesis with feed-forward networks, CVPR'17
	-  H. Zhang and K. Dana, Multi-style generative network for realtime transfer, 2017
- **ASPM** (Arbitrary-Style-Per-Model):
	- T. Q. Chen and M. Schmidt, Fast patch-based style transfer of arbitrary style. NIPS Workshop'16
	- Xun Huang, Serge Belongie. Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization. ICCV'17
		- **Real-time ASPM**
		- Adaptive Instance Normalization (AdaIN)
	- G Ghiasi, H Lee, M Kudlur, V Dumoulin, J Shlens. Exploring the Structure of a Real-time, Arbitrary Neural Artistic Stylization Network. BMVC'17
	- Yijun Li, Chen Fang, Jimei Yang, Zhaowen Wang, Xin Lu, and Ming-Hsuan Yang. Universal Style Transfer via Feature Transforms. NIPS'17

## Legacy
- NPR (non-photorealistic rendering):
	- B. Gooch and A. Gooch, Non-photorealistic rendering. 2001
	- T. Strothotte and S. Schlechtweg, Non-photorealistic computer graphics: modeling, rendering, and animation. 2002
	- P. Rosin and J. Collomosse, Image and video-based artistic stylisation. 2012
- SBR (Stroke-based rendering):
	- A. Hertzmann, Painterly rendering with curved brush strokes of multiple sizes. SIGGRAPH'98
- Texture Transfer:
	- A. A. Efros and W. T. Freeman, Image quilting for texture synthesis and transfer. SIGGRAPH'01
	- I. Drori, D. Cohen-Or, and H. Yeshurun, Example-based style synthesis. CVPR'03
	- O. Frigo, N. Sabater, J. Delon, and P. Hellier, “Split and match: Example-based adaptive patch sampling for unsupervised style transfer, CVPR'16
	- M. Elad and P. Milanfar, Style transfer via texture synthesis. TIP'17
- EBR (Example-based):
	- **Image Analogy**: A. Hertzmann, C. E. Jacobs, N. Oliver, B. Curless, and D. H. Salesin, Image analogies. SIGGRAPH'01