# 3D Generative and Synthesis

## 3D-Aware 2D Generation
- M Tatarchenko, A Dosovitskiy, T Brox. Multi-view 3D Models from Single Images with a Convolutional Network. ECCV'16
	- Encoder/Decoder
	- Input RGB, output RGB/D conditioned on any shape input (angle, ...)
	- https://github.com/lmb-freiburg/mv3d
- A Dosovitskiy, J Springenberg, M Tatarchenko, T Brox. Learning to Generate Chairs, Tables and Cars with Convolutional Networks. PAMI'17
	- Input: class c, view v, transfrom param theta;
	- Output: image;
	- Conv, deconv, upsampling;
- Johanna Delanoy, Mathieu Aubry, Phillip Isola, Alexei A. Efros, Adrien Bousseau. 3D Sketching using Multi-View Deep Volumetric Prediction. CGIT'18

## Template-Based
- Haibin Huang, Evangelos Kalogerakis, Benjamin Marlin. Analysis and synthesis of 3D shape families via deep-learned generative models of surfaces. Eurographics 2015
- Li Yi, Haibin Huang, Difan Liu, Evangelos Kalogerakis, Hao Su, Leonidas Guibas. Deep Part Induction from Articulated Object Pairs. SIGGRAPH Asia 2018
	- Deep Matching (Point Net)
	- Motion Discovery, Part Co-segmentation

## Conditional
- Text to 3D:
	- A. X. Chang, M. Savva, and C. D. Manning. Learning spatial knowledge for text to 3d scene generation. EMNLP'14
	- A. Chang, W. Monroe, M. Savva, C. Potts, and C. D. Manning. Text to 3d scene generation with rich lexical grounding. ACL'15

## Generation
- Haibin Huang, Evangelos Kalogerakis, and Benjamin Marlin. Analysis and synthesis of 3d shape families via deep-learned generative models of surfaces. CGF, 34(5):25–38, 2015.
- Interactive 3D modeling with a generative adversarial network, 3D Vision 2017
- Amir Arsalan Soltani, Haibin Huang, Jiajun Wu, Tejas D. Kulkarni, Joshua B. Tenenbaum. Synthesizing 3D Shapes via Modeling Multi-View Depth Maps and Silhouettes with Deep Generative Networks. CVPR 2017
	- https://github.com/Amir-Arsalan/Synthesize3DviaDepthOrSil

## Completion
- A. Dai, C. R. Qi, and M. Nießner. Shape completion using 3D-encoder-predictor CNNs and shape synthesis. CVPR'17
- L. Ladicky, O. Saurer, S. Jeong, F. Maninchedda, and M. Pollefeys. From point clouds to mesh using regression. ICCV'17
- G. Riegler, A. O. Ulusoy, H. Bischof, and A. Geiger. OctNetFusion: Learning depth fusion from data. 3DV'17

## 3D-Reconstruction, Render
- W. Jakob, Mitsuba renderer, 2010, http://www.mitsuba-renderer.org.

## Shape Editing
- A. Jain, T. Thormahlen, T. Ritschel, and H.-P. Seidel. Exploring shape variations by 3d-model decomposition and partbased recombination. CGF 2012

## PC Upsampling
- Wang Yifan, Shihao Wu, Hui Huang, Daniel Cohen-Or, and Olga Sorkine-Hornung. Patch-based progressive 3d point set upsampling. arXiv preprint arXiv:1811.11286, 2018
- Lequan Yu, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. Ec-net: an edge-aware point set consolidation network. ECCV'18
- Lequan Yu, Xianzhi Li, Chi-Wing Fu, Daniel Cohen-Or, and Pheng-Ann Heng. Pu-net: Point cloud upsampling network. CVPR'18