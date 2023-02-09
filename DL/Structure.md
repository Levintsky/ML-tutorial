# Structured/Stuctural Inference

## Problem Definition
- A structured model to explain a scene/object/...

## DL Meet MRF/CRF
- Bi-level optimization:
	- Inner-loop: MRF inference (sampling/VI/...)
	- Outer-loop: gradient descent on net weight w;
- S. Wang, A. Schwing, and R. Urtasun. Efficient inference of continuous markov random fields with polynomial potentials. NIPS'14
- L Chen, G Papandreou, I Kokkinos, K Murphy, A Yuille. Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs. ICLR'15
	- DL + dense-mrf;
- L. Chen, A. Schwing, A. Yuille, and R. Urtasun. Learning deep structured models. ICML'15
	- Problem formulation:
		- min_w ∑(x,y)∈D [max{∑b(y)f(x,y;w)+∑H(b)}-F(x,y;w)]
	- Inner loop: inference of CRF;
		- Blended learning: 1-step inner only, then update w;
	- Outer loop: learning of NN parameters;
- A. Schwing and R. Urtasun. Fully connected deep structured networks. arxiv'15
- S. Zheng, S. Jayasumana, B. Romera-Paredes, V. Vineet, Z. Su, D. Du, C. Huang, and P. Torr. Conditional random fields as recurrent neural networks. ICCV'15
- G Papandreou, L Chen, K Murphy, and A Yuille. Weakly- and Semi-Supervised Learning of a Deep Convolutional Network for Semantic Image Segmentation. ICCV'15
- D Belanger and A McCallum. Structured prediction energy networks. ICML'16
- L Chen, J Barron, G Papandreou, K Murphy, and A Yuille. Semantic Image Segmentation with Task-Specific Edge Detection Using CNNs and a Discriminatively Trained Domain Transform. CVPR'16
- S Wang, S Fidler, R Urtasun. Proximal Deep Structured Models. NIPS'16
	- Problem setup:
		- E(x,y;w) = ∑gi(yi,x;wu) + ∑α hα(yα,x;wα)
	- Reformulation:
		- E(x,y;w) = ∑gi(yi,hi(x,wu)) - ∑α hα(x, w)g∗α(zα) + ∑α hα(x, w) ⟨wα†yα, x⟩
	- Algorithm (1-step of inner loop proximal):
		- z = prox(g; z + σ/h w'y^)
		- y = prox(gi,hi; yi - σ/h w'y)
		- yi^ = yi + σ(yt+1 - yt)
	- Application: image denoising; depth refinement; optical flow;
- L Chen, G Papandreou, I Kokkinos, K Murphy, and A Yuille. DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs. 2017

## Structure Inference Approaches
- Search based:
	- Kemp, C. and Tenenbaum, J. B. The discovery of structural form. PNAS'08
	- Grosse, R. B., Salakhutdinov, R., Freeman, W. T., and Tenenbaum, J. B. Exploiting compositionality to explore a large space of model structures. UAI'12
	- Duvenaud, D., Lloyd, J. R., Grosse, R., Tenenbaum, J. B., and Ghahramani, Z. Structure discovery in nonparametric regression through compositional kernel search. ICML'13
	- Lloyd, J. R., Duvenaud, D. K., Grosse, R. B., Tenenbaum, J. B., and Ghahramani, Z. Automatic construction and natural-language description of nonparametric regression models. AAAI'14
- Data driven (from annotation, NN):
	- Yih, W.-t., He, X., and Meek, C. Semantic parsing for single-relation question answering. ACL'14
		- pos-tagging
	- Ma, X. and Hovy, E. End-to-end sequence labeling via bi-directional lstm-cnns-crf. ACL'16
	- Dong, L. and Lapata, M. Language to logical form with neural attention. ACL'16
		- Sequence to tree

## Application
- N. Homayounfar, S. Fidler and R. Urtasun. Sports Field Localization via Deep Structured Models. CVPR'17