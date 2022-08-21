# Active Learning

## Basics
- Problem Definition:
	- Find data most uncertain; how to measure uncertainty and generate MAP? check Bayes/CRF;
- Typical heuristics:
	- Start with a pool of unlabeled data
	- Pick a few points at random and get their labels
	- Repeat
		- Fit a classifier to the labels seen so far
		- Query the unlabeled point that is closest to the boundary
		- (or most uncertain, or most likely to decrease overall uncertainty,...)
- Techniques:
	- Adaptive query:
		- Case I: Exploiting (cluster) structure in data;
		- Case II: Efficient search through hypothesis space;
- Tutorial:
	- ICML'19: https://hunch.net/~active_learning/

## Legacy
- D. MacKay, Information-based objective functions for active data selection. Neural Computation'92
	- Expected informativeness
- Y. Freund, H. Seung, E. Shamir, and N. Tishby. Selective sampling using the query by committee algorithm. ML'97
	- A committee of classifiers;
- S. Tong and D. Koller, Support vector machine active learning with applications to text classification. JMLR'02
	- SVM;

## Cluster Based
- Basics:
	- Assume distance/neighborhood known, propagate labels;
- Xiaojin Zhu, John Lafferty and Zoubin Ghahramani, Combining active learning and semi-supervised learning using Gaussian fields and harmonic functions, ICML 2003 workshop
- Sanjoy Dasgupta and Daniel Hsu. Hierarchical sampling for active learning. ICML 2008.

## Efficient search through hypothesis space
- Basics:
	- Assume we have multiple classifier hypothesis, add new data+label, remove unsatisfied hypothesis;
	- Supervised: for misclassification error ≤ ε, need ≈ 1/ε labeled points.
- Separable data:
	- David Cohn, Les Atlas and Richard Ladner. Improving generalization with active learning, Machine Learning 15(2):201-221, 1994.
	- Yoav Freund, H. Sebastian Seung, Eli Shamir, and Naftali Tishby, Selective Sampling Using the Query by Committee Algorithm, Machine Learning, 28, 133-168, 1997.
	- Sanjoy Dasgupta, Coarse sample complexity bounds for active learning. NIPS 2005.
- General data:
	- Nina Balcan, Alina Beygelzimer, John Langford, Agnostic Active Learning. ICML 2006
	- Hanneke, S. A Bound on the Label Complexity of Agnostic Active Learning. ICML 2007.
	- Sanjoy Dasgupta, Daniel J. Hsu, and Claire Monteleoni. A general agnostic active learning algorithm. NIPS 2007.
	- Alina Beygelzimer, Sanjoy Dasgupta, and John Langford, Importance Weighted Active Learning, ICML 2009.
- Algorithms:
	- A^2 algorithm;

## Application in Computer Vision
- Scene classification:
	- G.-J. Qi, X.-S. Hua, Y. Rui, J. Tang, and H.-J. Zhang, Two-dimensional active learning for image classification. CVPR'08
- Object/image categorization:
	- A. Kapoor, K. Grauman, R. Urtasun, and T. Darrell, Active learning with gaussian processes for object categorization. ICCV'07
	- P. Jain and A. Kapoor, Active learning for large multi-class problems. CVPR'09
- Large scale image/video:
	- R. Yan, J. Yang, and A. Hauptmann. Automatically labeling video data using multi-class active learning. ICCV'03
	- B. Collins, J. Deng, K. Li, and L. Fei-Fei. Towards scalable dataset construction: An active learning approach. ECCV'08
	- A. Fathi, M. F. Balcan, X. Ren, and J. M. Rehg. Combining self training and active learning for video segmentation. BMVC'11
	- S. Vijayanarasimhan and K. Grauman. Active frame selection for label propagation in videos. ECCV'12
	- C. Vondrick, D. Patterson, and D. Ramanan, Efficiently scaling up crowdsourced video annotation. IJCV'13
- Structured:
	- B. Settles and M. Craven. An analysis of active learning strategies for sequence labeling tasks. EMNLP'08
		- Tree/chain
	- A. Culotta and A. McCallum, Reducing labeling effort for structured prediction tasks. AAAI'05
		- Tree/chain
	- W. Luo, A. G. Schwing, and R. Urtasun, Latent Structured Active Learning. NIPS'13
		- Latent structure with belief propagation; local entropy of the marginal distribution of each variable via convex belief propagation;
	- Qing Sun, Ankit Laddha, Dhruv Batra. Active Learning for Structured Probabilistic Models with Histogram Approximation. CVPR'15
		- Insight: a variational approach with Histogram Approximation for Gibbs distribution to approximate entropy;
			<img src="/Basic-ML/images/active/hist-approx.png" alt="drawing" width="400"/>
		- Assumption: CRF with unary and binary, S(y) = Σφ(yu) + Σφ(yu, yv), target: to learn weight w in the log-linear model s.t. (w, φ(x, y)); find the one with largest entropy to label:
			- H(p) = -E_p(y|x)[log(P(y|x))]
		- Approximate with sample entropy: with M-best proposals\
			<img src="/Basic-ML/images/active/sample-entropy.png" alt="drawing" width="400"/>\
			<img src="/Basic-ML/images/active/sample-entropy-2.png" alt="drawing" width="400"/>
		- This paper with histogram around MAP:\
			<img src="/Basic-ML/images/active/hist-entropy.png" alt="drawing" width="400"/>\
			<img src="/Basic-ML/images/active/hist-entropy-2.png" alt="drawing" width="400"/>
		- More details: circular or rings around MAP: solvable by Lagrange Dual\
			<img src="/Basic-ML/images/active/hist-entropy-3.png" alt="drawing" width="400"/>
		- Parameter Learning w: MLE, marginals via sum-product loop BP;
- Ask for labels:
	- S. Vijayanarasimhan and K. Grauman, What's it going to cost you? Predicting effort vs. informativeness for multilabel image annotations. CVPR'09
	- B. Siddiquie and A. Gupta, Beyond active noun tagging: Modeling contextual interactions for multi-class active learning. CVPR'10
	- A. Parkash and D. Parikh. Attributes for classifier feedback. ECCV'12

## Learning from Weak Annotations
- Segmenation from labels only:
	- J. Winn and N. Jojic. LOCUS: learning object classes with unsupervised segmentation. CVPR'05
	- H. Arora, N. Loeff, D. Forsyth, and N. Ahuja. Unsupervised segmentation of objects using efficient learning. CVPR'07
	- J. Xu, A. G. Schwing, and R. Urtasun. Tell me what you see and I will show you where it is. CVPR'14
- Segmentation from partial labeling (some pixel labels missing):
	- X. He and R. S. Zemel. Learning hybrid models for image annotation with partially labeled data. NIPS'08
	- J. Verbeek and W. Triggs. Scene Segmentation with CRFs Learned from Partially Labeled Images. NIPS'08
- From scribbles:
	- Y. Boykov and M.-P. Jolly. Interactive graph cuts for optimal boundary and region segmentation of objects in n-d images. ICCV'01
	- C. Rother, V. Kolmogorov, and A. Blake. GrabCut: interactive foreground extraction using iterated graph cuts. SIGGRAPH'04
	- D. Batra, R. Sukthankar, and T. Chen. Semi-supervised clustering via learnt codeword distances. BMVC'08
	- D. Batra, A. Kowdle, D. Parikh, J. Luo, and T. Chen. iCoseg: Interactive Co-segmentation with Intelligent Scribble Guidance. CVPR'10
- Propagation across images:
	- D. Küttel, M. Guillaumin, and V. Ferrari. Segmentation propagation in imagenet. ECCV'12

## NIPS'19
- Andreas Kirsch, Joost van Amersfoort, Yarin Gal. BatchBALD: Efficient and Diverse Batch Acquisition for Deep Bayesian Active Learning
- Robert Pinsler, Jonathan Gordon, Eric Nalisnick, José Miguel Hernández-Lobato. Bayesian Batch Active Learning as Sparse Subset Approximation
- Shali Jiang, Roman Garnett, Benjamin Moseley. Cost Effective Active Search
- Michal Derezinski, Daniele Calandriello, Michal Valko. Exact sampling of determinantal point processes with sublinear time preprocessing
- Fabio Vitale, Anand Rajagopalan, Claudio Gentile. Flattening a Hierarchical Clustering through Active Learning
- Weishi Shi, Qi Yu. Integrating Bayesian and Discriminative Sparse Kernel Machines for Multi-class Active Learning
- Blake Mason, Ardhendu Tripathy, Robert Nowak. Learning Nearest Neighbor Graphs from Noisy Distance Samples
- Tomi Peltola, Mustafa Mert Çelikok, Pedram Daee, Samuel Kaski. Machine Teaching of Active Sequential Learners
- Songbai Yan, Kamalika Chaudhuri, Tara Javidi. The Label Complexity of Active Learning from Observational Data
