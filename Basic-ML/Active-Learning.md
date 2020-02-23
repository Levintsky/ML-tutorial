# Active Learning

## Active Learning
- Basics:
	- Find data most uncertain; how to measure uncertainty and generate MAP? check Bayes/CRF;
- Legacy:
	- D. MacKay, Information-based objective functions for active data selection,” Neural Computation. Neural Computation'92
		- Expected informativeness
	- Y. Freund, H. Seung, E. Shamir, and N. Tishby, Selective sampling using the query by committee algorithm. ML'97
		- A committee of classifiers;
	- S. Tong and D. Koller, Support vector machine active learning with applications to text classification. JMLR'02
		- SVM;

## Application in Computer Vision
- Scene classification:
	- G.-J. Qi, X.-S. Hua, Y. Rui, J. Tang, and H.-J. Zhang, Two-dimensional active learning for image classification. CVPR'08
- Object/image categorization:
	- A. Kapoor, K. Grauman, R. Urtasun, and T. Darrell, Active learning with gaussian processes for object categorization. ICCV'07
	- P. Jain and A. Kapoor, Active learning for large multi-class problems. CVPR'09
- Large scale image/video:
	- R. Yan, J. Yang, and A. Hauptmann. Automatically labeling video data using multi-class active learning. ICCV'03
	- B. Collins, J. Deng, K. Li, and L. Fei-Fei, Towards scalable dataset construction: An active learning approach. ECCV'08
	- A. Fathi, M. F. Balcan, X. Ren, and J. M. Rehg, Combining self training and active learning for video segmentation. BMVC'11
	- S. Vijayanarasimhan and K. Grauman. Active frame selection for label propagation in videos. ECCV'12
	- C. Vondrick, D. Patterson, and D. Ramanan, Efficiently scaling up crowdsourced video annotation. IJCV'13
- Structured:
	- B. Settles and M. Craven, An analysis of active learning strategies for sequence labeling tasks. EMNLP'08
		- Tree/chain
	- A. Culotta and A. McCallum, Reducing labeling effort for structured prediction tasks. AAAI'05
		- Tree/chain
	- W. Luo, A. G. Schwing, and R. Urtasun, Latent Structured Active Learning. NIPS'13
		- Latent structure with belief propagation; local entropy of the marginal distribution of each variable via convex belief propagation;
	- Qing Sun, Ankit Laddha, Dhruv Batra. Active Learning for Structured Probabilistic Models with Histogram Approximation. CVPR'15
		- Insight: a variational approach with Histogram Approximation for Gibbs distribution to approximate entropy;
			<img src="/Basic-ML/images/active/hist-approx.png" alt="drawing" width="400"/>
		- Assumption: CRF with unary and binary, S(y) = sum phi(yu) + sum phi(yu, yv), target: to learn weight w in the log-linear model s.t. (w, phi(x, y)); find the one with largest entropy to label:\
			<img src="/Basic-ML/images/active/crf-entropy.png" alt="drawing" width="350"/>
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
	- S. Vijayanarasimhan and K. Grauman, What’s it going to cost you? Predicting effort vs. informativeness for multilabel image annotations. CVPR'09
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