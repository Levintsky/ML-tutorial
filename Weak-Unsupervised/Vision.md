# Weakly-Supervsied Learning

## Tutorial
- **Tutorial**: M. A. Ranzato and A. Graves. Deep unsupervised learning. NIPS Tutorial, 2018
- Edwards & Storkey, Towards a Neural Statistician, (2017)
	- one must take seriously the idea of working with datasets, rather than datapoints, as the key objects to model.
- **Work**:
	- image translation
	- image generation in some domains
- **Sort-of-Work**:
	- SSL in some applications
- **Does-not-Work-yet**:
	- General feature learning

## Unclassified
- Tomas Jakab, Ankush Gupta, Hakan Bilen, Andrea Vedaldi. Unsupervised Learning of Object Landmarks through Conditional Image Generation. NIPS'18
- **ReMixMatch**: David Berthelot, Nicholas Carlini, Ekin D. Cubuk, Alex Kurakin, Han Zhang, Colin Raffel, Kihyuk Sohn. ReMixMatch: Semi-Supervised Learning with Distribution Alignment and Augmentation Anchoring. 2019
	- CTAugment
	- https://github.com/google-research/remixmatch
	- CIFAR: 93.73% with 4,000 labels; 84.9% with 40;
- **FixMatch**: Kihyuk Sohn, David Berthelot, Chun-Liang Li, Zizhao Zhang, Nicholas Carlini, Ekin D. Cubuk, Alex Kurakin, Han Zhang, Colin Raffel. FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence. 2020
	- https://github.com/google-research/fixmatch
	- CIFAR: 94.9% with 250 labels, 88.6% with 40 (4 per class);

## Images
- Summaries:
	- Alexander Kolesnikov, Xiaohua Zhai, Lucas Beyer. Revisiting Self-Supervised Visual Representation Learning. CVPR'19
		- https://github.com/google/revisiting-self-supervised
- Context prediction:
	- Unsupervised Visual Representation Learning by Context Prediction. ICCV 2015
	- D. Pathak, P. Krahenbuhl, J. Donahue, T. Darrell, and A. Efros. Context encoders: Feature learning by inpainting. CVPR'16
- Input two image patches, predict spatial relationship:
	- C. Doersch et al. Unsupervised Visual Representation Learning by Context Prediction, ICCV'15
- Predict color from gray scale values:
	- Richard Zhang, Phillip Isola, Alexei A. Efros. Colorful Image Colorization, ECCV'16
- Predict image rotation:
	- S. Gidaris et al. Unsupervised Representation Learning by Predicting Image Rotations. ICLR 2018
- Clustering (pseudo-labels):
	- **Pseudo-label**: Dong-Hyun Lee. Pseudo-label: The simple and efficient semi-supervised learning method for deep neural networks. ICMLW'13
		- Equivalent to  Entropy Regularization;
	- Mathilde Caron, Piotr Bojanowski, Armand Joulin, and Matthijs Douze. Deep clustering for unsupervised learning of visual features. ECCV'18
		- Extract CNN and run K-means
		- Train on cluster id;
	- X Ji, J Henriques, A Vedaldi. Invariant Information Clustering for Unsupervised Image Classification and Segmentation. ICCV'19
		- https://github.com/xu-ji/IIC
- Dictionary Learning:
	- Zhirong Wu, Yuanjun Xiong, Stella Yu, and Dahua Lin. Unsupervised feature learning via non-parametric instance discrimination. CVPR'18
		- https://github.com/zhirongw/lemniscate.pytorch
		- Constrastive estimation;
	- **AMDIM**: Philip Bachman, R Devon Hjelm, and William Buchwalter. Learning representations by maximizing mutual information. 2019
		- https://github.com/Philip-Bachman/amdim-public
	- R Devon Hjelm, Alex Fedorov, Samuel Lavoie-Marchildon, Karan Grewal, Adam Trischler, and Yoshua Bengio. Learning deep representations by mutual information estimation and maximization. ICLR'19
	- **LocalAggr**: Chengxu Zhuang, Alex Lin Zhai, and Daniel Yamins. Local aggregation for unsupervised learning of visual embeddings. ICCV'19
- Weak supervision:
	- **URU**: D Mahajan, R Girshick, V Ramanathan, K He, M Paluri, Y Li, A Bharambe, L van der Maaten. Exploring the Limits of Weakly Supervised Pretraining. ECCV 2018
		- **IG-1B** dataset: Instagram
		- Pretrain on a larger dataset (1.5 billion Instagram) + (1.5k, 8.5k, 17k hashtag classes);
		- Preprocessing: image-deduplication, hash-tags clean up (SynNet);
		- Model: ResNext;
		- Infra: Caffe2-1hr, synchronous-SGD; 42 Machine x 8 GPU/m = 336 GPU; 22 days;
		- Conclusion 1: hash-tags v.s. accuracy; (always a gain, fine-grained target needs a fine-grained source);
		- Conclusion 2: larger amount of pretrain -> better target domain accuracy;
		- Conclusion 3: the smaller the label noise (hashtags are noisy) -> better target accuracy;
	- A Joulin, L van der Maaten, A Jabri, N Vasilache. Learning Visual Features from Large Weakly Supervised Data. ECCV 2016
- Exemplar:
	- **MoCo**: K He, H Fan, Y Wu, S Xie, R Girshick. Momentum Contrast for Unsupervised Visual Representation Learning. CVPR'20
		- Contrastive learning; (1-positive + K-negative), InfoNCE applied with softmax-cross-entropy;
		- Dictionary as a queue; (>> batch-size, no gradients, only learn query-encoder)
		- Momentum update: slowly updating key encoder; theta-key = 0.999 theta-key + 0.001 theta-query;
		- Positive: random augmentation (with grayscale);
		- Shuffling-BN: train with multiple GPUs independently, the sample order of minibatch randomly shuffled;
		- Exp:
			- Linear protocol: 68% on ImageNet, similar to CMC, CPC and LocalAggr;
			- PASCAL VOC Faster-RCNN end-to-end [AP: 74.4 -> 75.6];
			- COCO end-to-end MaskRCNN [AP: 54.7 -> 55.4]
- Weak detetection (Zhenheng):
	- Image has only image level labeling (no bbox or segments);
	- Hundreds of candidate proposals (can't penalize bbox reg-loss or classification loss);
	- Max-pooling/top-k then direct classification;
	- Half mAP

## Videos
- Predict video forward or backward
	- D. Wei et al. Self-supervision using the arrow of time, CVPR 2018
	- I. Misra, C. L. Zitnick, and M. Hebert. Shuffle and Learn: Unsupervised Learning using Temporal Order Verification. ECCV'16
		- Predict shuffle;
- Predict motion/ego-motion/motion-mask:
	- P. Agrawal, J. Carreira, and J. Malik. Learning to see by moving. ICCV'15
	- D. Jayaraman and K. Grauman. Learning image representations tied to egomotion. ICCV'15
	- D. Pathak, R. Girshick, P. Dollar, T. Darrell, and B. Hariharan. Learning features by watching objects move. CVPR'17
- Tracking:
	- X. Wang and A. Gupta. Unsupervised learning of visual representations using videos. ICCV'15
- Coloring videos
	- C. Vondrik et al. Tracking emerges from colorizing videos, ECCV 2018
- Predict future frame
	- E. Denton et al. Unsupervised learning of disentangled representations from video, NIPS 2017
- Predict one modality from the other
	- V. de Sa, Learning classification from unlabeled data, NIPS 1994
	- R. Arandjelovic et al. Object that sound, ECCV 2018
- R. Goroshin, J. Bruna, J. Tompson, D. Eigen, and Y. LeCun. Unsupervised learning of spatiotemporally coherent metrics. ICCV'15
- Self-Supervised Video Representation Learning With Odd-One-Out Networks

## SOA
- **CPC**:
	- Olivier J Hénaff, Ali Razavi, Carl Doersch, SM Eslami, and Aaron van den Oord. Data-efficient image recognition with contrastive predictive coding. 2019
	- **CMC**: Yonglong Tian, Dilip Krishnan, and Phillip Isola. Contrastive multiview coding. ICLR'20 rejected

## Tasks
- Jigsaw:
	- Unsupervised Learning of Visual Representations by Solving Jigsaw Puzzles. ECCV 2016

## 3D
- Alexey Dosovitskiy. Unsupervised Learning of Shape and Pose with Differentiable Point Clouds. NIPS'18

## DeepMind
- Neural scene representation and rendering. Science 2018
	- https://deepmind.com/blog/neural-scene-representation-and-rendering/
	- Input: images and viewpoints; output: a query new image
	- **Generative Query Network (GQN)**: learns an internal representation
		- t-SNE
		- VAE will fail
		- Factorized-representation\
			<img src = '/Weak-Unsupervised/images/gqn.png' width = '500px'>
	- g(x|vq, r) = int g(x,z|vq, r)dz, z: latent variable
	- Env: rooms with multiple objects (DML?), allow agent to act, robotic-arm;

## Unclassified
- Andrea Vedaldi. Modelling and unsupervised learning of symmetric deformable object categories. NIPS'18