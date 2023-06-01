# Classification

## Fine-Grained Classification
- Basics
	- Granularity:
		- Y Cui, Z Gu, D Mahajan, L v d Maaten, S Belongie, S Lim. Measuring Dataset Granularity. 
			- the smaller, the more fine-grained;
- Benchmarks:
	- Most SOTA reports perf on CUB-bird, Stanford-cars and Aircraft;
	- Bird:
		- CUB-200-2011 (Caltech-UCSD Birds-200-2011) The caltech-ucsd birds-200-2011 dataset.
			- https://vision.cornell.edu/se3/caltech-ucsd-birds-200/
			- https://data.caltech.edu/records/20098
			- 11,788 images, 200 categories
			- Annotation: 15 part, 312 binary attributes, 1 bounding box;
	- Dogs:
		- Stanford dogs:  Novel dataset for Fine-Grained Image Categorization. CVPR'11 FGVC
		- http://vision.stanford.edu/aditya86/ImageNetDogs/
	- Plants:
		- Flower: Automated flower classification over a large number of classes. CVGIP'08
		- Leafsnap: A Computer Vision System for Automatic Plant Species Identification. ECCV'12
			- http://leafsnap.com/dataset/
			- 23147 images;
		- https://www.kaggle.com/c/herbarium-2020-fgvc7/
	- Cars:
		- Li Fei-Fei. 3d object representations for fine-grained categorization. In ICCVW'13
		- Stanford cars: 3D Object Representations for Fine-Grained Categorization
			- https://ai.stanford.edu/~jkrause/cars/car_dataset.html
			- 16,185 images (8,144 train/8,041 test), 196 classes;
			- Make/Model/year;
		- L Yang, P Luo, C C Loy, X Tang. A Large-Scale Car Dataset for Fine-Grained Categorization and Verification. CVPR'15
	- Aircraft:
		- A Vedaldi. Fine-grained visual classification of aircraft. arxiv'13
			- https://www.robots.ox.ac.uk/~vgg/data/fgvc-aircraft/
			- 10,200 images, 102 classes x 100/class;
			- 1/1/1 train/val/test;
	- Fish: https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring
	- Product: https://rpc-dataset.github.io/
	- G Horn, O Aodha, Y Song, Y Cui, C Sun, A Shepard, H Adam, P Perona, S Belongie. The iNaturalist Species Classification and Detection Dataset. CVPR'18
	- Insect: X Wu, C Zhan, Y Lai, M Cheng, J Yang. IP102: A Large-Scale Benchmark Dataset for Insect Pest Recognition. CVPR'19
	- Finer-grained: X Yu, Y Zhao, Y Gao, X Yuan, S Xiong. Benchmark Platform for Ultra-Fine-Grained Visual Categorization Beyond Human Performance. ICCV'21
		- 47,114 images, 3,526 categories;
		- https://github.com/XiaohanYu-GU/Ultra-FGVC
- Approaches:
	- Attribute-based;
	- Part-based;
- Resources
	- Tutorial in CVPR'21: https://fgva-cvpr21.github.io/

## Backbone
- Pooling/Feature-Integration
	- **Bilinear**: T Lin, A Roy Chowdhury, S Maji. Bilinear CNN Models for Fine-grained Visual Recognition. ICCV'15
		- https://github.com/HaoMood/bilinear-cnn
		- CUB-Bird: 84.1% 
	- L Wang, J Zhang, Lg Zhou, C Tang, W Li. Beyond Covariance: Feature Representation with Nonlinear Kernel Matrices. ICCV'15
	- T Lin, A  Chowdhury, S Maji. Bilinear CNNs for Fine-grained Visual Recognition. ICCV'15
	- T Lin, S Maji. Improved Bilinear Pooling with CNNs. BMVC'17
	- S. Kong, C. Fowlkes. Low-rank Bilinear Pooling for Fine-Grained Classification. CVPR'17
	- S Cai, W Zuo, L Zhang. Higher-Order Integration of Hierarchical Convolutional Activations for Fine-Grained Visual Categorization. ICCV'17
	- P Li, J Xie, Q Wang, W Zuo. Is Second-order Information Helpful for Large-scale Visual Recognition? ICCV'17
	- P Li, J Xie, Q Wang, Z Gao. Towards Faster Training of Global Covariance Pooling Networks by Iterative Matrix Square Root Normalization. CVPR'18
		- CUB-Bird: 88.7%
		- https://github.com/jiangtaoxie/fast-MPN-COV
		- https://github.com/osmr/imgclsmob
	- CAP: A Behera, Z Wharton, P Hewage, A Bera. Context-aware Attentional Pooling (CAP) for Fine-grained Visual Classification. AAAI'21
		- CUB-Bird: 91.8%
		- https://github.com/ArdhenduBehera/cap
- Part-based
	- N Zhang, J Donahue, R Girshick, T Darrell. Part-based R-CNNs for Fine-grained Category Detection. ECCV'14
	- S Huang, Z Xu, D Tao, Y Zhang. Part-Stacked CNN for Fine-Grained Visual Categorization. CVPR'16
	- X Wei, C Xie, J Wu. Mask-CNN: Localizing Parts and Selecting Descriptors for Fine-Grained Image Recognition. CVPR'16
	- J Fu, H Zheng, T Mei. Look Closer to See Better: Recurrent Attention Convolutional Neural Network for Fine-Grained Image Recognition. CVPR'17
	- M Lam, B Mahasseni, S Todorovic. Fine-Grained Recognition as HSnet Search for Informative Image Parts. CVPR'17
	- **MACNN**: Learning Multi-Attention Convolutional Neural Network for Fine-Grained Image Recognition. ICCV'17
		- https://github.com/Jianlong-Fu/Multi-Attention-CNN
		- Part supervision;
		- CUB: 86.5%;
	- Y Wang, V Morariu, L Davis. Learning a Discriminative Filter Bank within a CNN for Fine-grained Recognition. CVPR'18
		- https://github.com/jobinkv/Ongoing
		- CUB: 87.4%;
	- Z Yang, T Luo, D Wang, Z Hu, J Gao, Liwei Wang. Learning to Navigate for Fine-grained Classification. ECCV'18
	- J Han, X Yao, G Cheng, X Feng, D Xu. P-CNN: Part-Based Convolutional Neural Networks for Fine-Grained Visual Categorization. PAMI'19
- Attention
	- H Zheng, J Fu, Z Zha, J Luo. Looking for the Devil in the Details: Learning Trilinear Attention Sampling Network for Fine-grained Image Recognition. CVPR'19
		- https://github.com/researchmm/tasn
		- CUB: 87.9%
	- LIO: M Zhou, Y Bai, W zhang, T Zhao, T Mei. Look-into-Object: Self-supervised Structure Modeling for Object Recognition. CVPR'20
		- https://github.com/JDAI-CV/LIO
	- J Wang, X Yu, Y Gao. FFVT: Feature Fusion Vision Transformer for Fine-Grained Visual Categorization. '21
		- https://github.com/Markin-Wang/FFVT
		- 91.6%
	- CAL: Y Rao, G Chen, J Lu, J Zhou. Counterfactual Attention Learning for Fine-Grained Visual Categorization and Re-identification. ICCV'21
		- Insight: a counterfactual attention for FG classification;
			- What if we attend to something else? Y_effect = E[Y(A,X)-Y(A',X)]
			- Loss = Lce(Y_effect, y) + L-old;
		- https://github.com/raoyongming/cal
		- CUB: 90.6%
	- J He, J Chen, S Liu, A Kortylewski, C Yang, Y Bai, C Wang. TransFG: A Transformer Architecture for Fine-grained Recognition. AAAI'22
		- https://github.com/TACJu/TransFG
		- CUB: 91.7%

## Weakly-supervised/Data
- PIM: P Chou, C Lin, and W Kao. A Novel Plug-in Module for Fine-Grained Visual Classification. 2022
	- https://github.com/chou141253/FGVC-PIM
	- CUB-200: 92.8%
- SWAG: M Singh, L Gustafson, A Adcock, V Reis, B Gedik, R Kosaraju, D Mahajan, R Girshick, P Dollar, L Maaten.  Revisiting Weakly Supervised Pre-Training of Visual Perception Models
	- https://github.com/facebookresearch/SWAG
	- Hashtag weak supervision;
- Text data:
	- Are These Birds Similar: Learning Branched Networks for Fine-grained Representations. 2020
		- 87.5%
- A Imran, V Athitsos. DATL: Domain Adaptive Transfer Learning on Visual Attention Aware Data Augmentation for Fine-grained Visual Categorization. 20
	- 91.2%

## Loss-Design
- Metric Learning:
	- Abhimanyu Dubey, Otkrist Gupta, Pei Guo, Ramesh Raskar, Ryan Farrell, Nikhil Naik. Pairwise Confusion for Fine-Grained Visual Classification. ECCV'18
		- https://github.com/abhimanyudubey/confusion
		- CUB: 86.9%

## Approaches
- Webly-supervised fine-grained visual categorization via deep domain adaptation. PAMI'16
- J Deng, J Krause, M Stark, L Fei-Fei. Leveraging the Wisdom of the Crowd for Fine-Grained Recognition. PAMI'16
- Y Cui, F Zhou, J Wang, X Liu, Y Lin, S Belongie. Kernel pooling for convolutional neural networks. CVPR'17
- B Zhao, X Wu, J Feng, Q Peng, and S Yan. Diversified Visual Attention Networks for Fine-Grained Object Classification. TMM'17
- Y Cui, Y Song, C Sun, A Howard, S Belongie. Large Scale Fine-Grained Categorization and Domain-Specific Transfer Learning. CVPR'18
- M Engin, L Wang, L Zhou, X Liu. DeepKSPD: Learning Kernel-matrix-based SPD Representation for Fine-grained Image Recognition. ECCV'18
- Y Chen, Y Bai, W Zhang, T Mei. Destruction and Construction Learning for Fine-grained Image Recognition. CVPR'19
- O M Aodha, E Cole, P Perona. Presence-Only Geographical Priors for Fine-Grained Image Classification. ICCV'19
- W Luo, X Yang, X Mo, Y Lu, L Davis, J Li, J Yang, S Lim. Cross-X Learning for Fine-Grained Visual Categorization. ICCV'19
- L Zhang, S Huang, W Liu, and D Tao. Learning a Mixture of Granularity-Specific Experts for Fine-Grained Categorization. ICCV'19
- Hierarchical Deep Click Feature Prediction for Fine-Grained Image Recognition. PAMI'19
- MaskCOV: A random mask covariance network for ultra-fine-grained visual categorization. PR'21

## Misc
- K Yue, M Sun, Y Yuan, F Zhou, E Ding, F Xu. Compact Generalized Non-local Network. NIPS'18
	- https://github.com/KaiyuYue/cgnl-network.pytorch

## Localization-classification
- Branson et al., BMVC 2014
- Zhang et al., ECCV 2014
- Ren et al., TPAMI 2016
- Long et al., CVPR 2015
- SPDA-CNN. CVPR'16
- co-segmentation for weakly-supervised recognition
	- Krause et al., CVPR 2015
- Interdependence between parts;
	- Lam et al., CVPR 2017
	- Graph-based: Wang et al., AAAI 2020
- Deep filters as part detector: (clustering?)
	- Xiao CVPR'15
- Attention

## High Order Pooling
- Power normalisation;
- Simon, Koniusz, Nock, Harandi, Projective Subspace Networks For Few-Shot Learning. CVPR'20
