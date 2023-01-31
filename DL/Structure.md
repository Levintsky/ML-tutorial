# Structured/Stuctural Inference

## Problem Definition
- A structured model to explain a scene/object/...

## Structural Inference Problems
- Matrix Factorization:
	- Mnih, A. and Salakhutdinov, R. R. Probabilistic matrix factorization. NIPS'08
- Clustering, co-clustering:
	- Kemp, C., Tenenbaum, J. B., Griffiths, T. L., Yamada, T., and Ueda, N. Learning systems of concepts with an infinite relational model. AAAI'06
- Binary latent factors:
	- Ghahramani, Z. and Griffiths, T. L. Infinite latent feature models and the indian buffet process. NIPS'06
- Sparse coding:
- Dependent GSM:
	- Karklin, Y. and Lewicki, M. S. Emergence of complex cell properties by learning to generalize in natural scenes. Nature'09
- Structure discovery (recursive search-based):
	- Kemp, C. and Tenenbaum, J. B. The discovery of structural form. PNAS'08
	- Grosse, R. B., Salakhutdinov, R., Freeman, W. T., and Tenenbaum, J. B. Exploiting compositionality to explore a large space of model structures. UAI'12

## MRF/CRF Style
- S. Wang, A. Schwing, and R. Urtasun. Efficient inference of continuous markov random fields with polynomial potentials. NIPS'14
- L. Chen, A. Schwing, A. Yuille, and R. Urtasun. Learning deep structured models. ICML'15
	- Problem formulation:
		- min_w ∑(x,y)∈D [max{∑b(y)f(x,y;w)+∑H(b)}-F(x,y;w)]
	- Inner loop: inference of CRF;
	- Outer loop: learning of NN parameters;
- A. Schwing and R. Urtasun. Fully connected deep structured networks. arxiv'15
- S. Zheng, S. Jayasumana, B. Romera-Paredes, V. Vineet, Z. Su, D. Du, C. Huang, and P. Torr. Conditional random fields as recurrent neural networks. ICCV'15
- George Papandreou, Liang-Chieh Chen, Kevin Murphy, and Alan L. Yuille. Weakly- and Semi-Supervised Learning of a Deep Convolutional Network for Semantic Image Segmentation. ICCV'15
- David Belanger and Andrew McCallum. Structured prediction energy networks. ICML'16
- Liang-Chieh Chen, Jonathan T. Barron, George Papandreou, Kevin Murphy, and Alan L. Yuille. Semantic Image Segmentation with Task-Specific Edge Detection Using CNNs and a Discriminatively Trained Domain Transform. CVPR'16
- Shenlong Wang, Sanja Fidler, Raquel Urtasun. Proximal Deep Structured Models. NIPS'16
	- Structured inference problem (energy minimization):
		- E(x,y;w) = ∑fi(yi,x;wu) + ∑α fα(yα,x;wα)>
	- Algorithm:
		- z = prox(g; z + σ/h w'y^)
		- y = prox(gi,hi; yi - σ/h w'y)
		- yi^ = yi + σ(yt+1 - yt)
	- Application: image denoising; depth refinement; optical flow;
- Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos, Kevin Murphy, and Alan L. Yuille. DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution,
and Fully Connected CRFs. 2017

## Structure Inference Approaches
- Search based:
	- Kemp, C. and Tenenbaum, J. B. The discovery of structural form. PNAS'08
	- Grosse, R. B., Salakhutdinov, R., Freeman, W. T., and Tenenbaum, J. B. Exploiting compositionality to explore a large space of model structures. UAI'12
	- Duvenaud, D., Lloyd, J. R., Grosse, R., Tenenbaum, J. B., and Ghahramani, Z. Structure discovery in nonparametric regression through compositional kernel search. ICML'13
	- Lloyd, J. R., Duvenaud, D. K., Grosse, R. B., Tenenbaum, J. B., and Ghahramani, Z. Automatic construction and natural-language description of nonparametric regression models. AAAI'14
- Data driven (from annotation, NN):
	- Yih, W.-t., He, X., and Meek, C. Semantic parsing for single-relation question answering. ACL'14
		- pos-tagging
	- Chen, D. and Manning, C. A fast and accurate dependency parser using neural networks. EMNLP'14
	- Ma, X. and Hovy, E. End-to-end sequence labeling via bi-directional lstm-cnns-crf. ACL'16
	- Dong, L. and Lapata, M. Language to logical form with neural attention. ACL'16
		- Sequence to tree
- (NN-based) guided search:
	- Beneš, B., Št’ava, O., Měch, R., and Miller, G. Guided procedural modeling. CGF'11
	- Menon, A., Tamuz, O., Gulwani, S., Lampson, B., and Kalai, A. A machine learning framework for programming by example. ICML'13
	- Osera, P.-M. and Zdancewic, S. Type-and-example-directed program synthesis. ACM SIGPLAN'15
	- Ritchie, D., Thomas, A., Hanrahan, P., and Goodman, N. Neurally-guided procedural models: Amortized inference for procedural graphics programs using neural networks. NIPS'16
	- Devlin, J., Uesato, J., Bhupatiraju, S., Singh, R., Mohamed, A.-r., and Kohli, P. Robustfill: Neural program learning under noisy i/o. ICML'17
	- Fox, R., Shin, R., Krishnan, S., Goldberg, K., Song, D., and Stoica, I. Parametrized hierarchical procedures for neural programming. ICLR'18
	- Sun, S.-H., Noh, H., Somasundaram, S., and Lim, J. Neural program synthesis from diverse demonstration videos. ICML'18
- Combined:
	- NGSI: S Lu, J Mao, J Tenenbaum, J Wu. Neurally-Guided Structure Inference. ICML'19
		- https://github.com/desire2020/NGSI
		- Key insight: search-based, exhaustive -> neural guided;
		- The algorithm builds the hierarchical structure by recursively choosing the production rule to expand a non-terminal symbol;
		- Application 1: Matrix decomposition. F = MG + G. M: selection; first G: Gaussian of cluster center; 2nd G: i.i.d Noise;
		- Application 2: Program parsing. Build on Xinyun 2018 with while loop.

## Application
- N. Homayounfar, S. Fidler and R. Urtasun. Sports Field Localization via Deep Structured Models. CVPR'17