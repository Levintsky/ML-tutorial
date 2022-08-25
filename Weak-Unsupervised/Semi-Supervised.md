# Semi-supervised Learning

## Basics
- Task:
	- Model from labeled + unlabeled data;
- Assumption:
	- Smoothness: smooth label;
	- Cluster:
	- Low-density separation:
	- Manifold:
- Model:
	- Consistency regularization for unlabeled data;: 
		- Π-model: (also used in SimCLR, BYOL, SimCSE, ...)
		- Temporal ensembling: EMA-target;
		- Mean teachers: mean-teacher with EMA-parameter;
		- noisy samples as learning targets: adversarial, VAT, ICT, MixUp, UDA,
	- Pseudo Labeling:
		- Label propagation: similarity graph;
		- Self-Training; train a model, then convert most confident data into labeled ones;
		- Reducing confirmation bias: problem with wrong label from imperfect teacher;
			- Meta Pseudo Labels (Pham et al. 2021)
	- Pseudo Labeling with Consistency Regularization
		- MixMatch, ReMixMatch;
		- DivideMix: GMM to divide data;
		- FixMatch
	- Combined with Powerful Pre-Training
- Tutorial:
	- https://lilianweng.github.io/posts/2021-12-05-semi-supervised

## Evaluation
- Avital Oliver, Augustus Odena, Colin Raffel, Ekin D. Cubuk, Ian J. Goodfellow. Realistic Evaluation of Deep Semi-Supervised Learning Algorithms. NIPS'18

## Vision
- **ReMixMatch**: David Berthelot, Nicholas Carlini, Ekin D. Cubuk, Alex Kurakin, Han Zhang, Colin Raffel, Kihyuk Sohn. ReMixMatch: Semi-Supervised Learning with Distribution Alignment and Augmentation Anchoring. 2019
	- CTAugment
	- https://github.com/google-research/remixmatch
	- CIFAR: 93.73% with 4,000 labels; 84.9% with 40;
- **FixMatch**: Kihyuk Sohn, David Berthelot, Chun-Liang Li, Zizhao Zhang, Nicholas Carlini, Ekin D. Cubuk, Alex Kurakin, Han Zhang, Colin Raffel. FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence. 2020
	- https://github.com/google-research/fixmatch
	- CIFAR: 94.9% with 250 labels, 88.6% with 40 (4 per class);

## NIPS'18
- Xuanqing Liu, Si Si, Jerry Zhu, Yang Li, Cho-Jui Hsieh. A Unified Framework for Data Poisoning Attack to Graph-based Semi-supervised Learning
- Xiaobo Xia, Tongliang Liu, Nannan Wang, Bo Han, Chen Gong, Gang Niu, Masashi Sugiyama. Are Anchor Points Really Indispensable in Label-Noise Learning?
- Pedro Mercado, Francesco Tudisco, Matthias Hein. Generalized Matrix Means for Semi-Supervised Learning with Multilayer Graphs
- Otilia Stretcu, Krishnamurthy Viswanathan, Dana Movshovitz-Attias, Emmanouil Platanios, Sujith Ravi, Andrew Tomkins. Graph Agreement Models for Semi-Supervised Learning
- Fan Zhou, Tengfei Li, Haibo Zhou, Hongtu Zhu, Ye Jieping. Graph-Based Semi-Supervised Learning with Non-ignorable Non-response
- Leonidas J Guibas, Qixing Huang, Zhenxiao Liang. A Condition Number for Joint Optimization of Cycle-Consistent Networks
- David Berthelot, Nicholas Carlini, Ian Goodfellow, Nicolas Papernot, Avital Oliver, Colin A Raffel. MixMatch: A Holistic Approach to Semi-Supervised Learning
- Liyuan Xu, Junya Honda, Gang Niu, Masashi Sugiyama. Uncoupled Regression from Pairwise Comparison Data
- Yair Carmon, Aditi Raghunathan, Ludwig Schmidt, John Duchi, Percy Liang. Unlabeled Data Improves Adversarial Robustness
