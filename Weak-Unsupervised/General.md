# Unsupervised, Weak-Supervised, SSL

## Tutorials
- NIPS'18 Tutorial by M. A. Ranzato and A. Graves. Deep unsupervised learning.
	- https://media.neurips.cc/Conferences/NIPS2018/Slides/Visualization_for_ML.pdf
	- Edwards & Storkey, Towards a Neural Statistician, (2017)
		- one must take seriously the idea of working with datasets, rather than datapoints, as the key objects to model.
	- **Work**:
		- image translation
		- image generation in some domains
	- **Sort-of-Work**:
		- SSL in some applications
	- **Does-not-Work-yet**:
		- General feature learning
- **Tutorial**: ECCV'2020
	- Deepak Pathak: https://youtu.be/fUMpC_hoedA
		- RL: intrinsic motivation/curiosity;
			- Predict consequences of action;
			- Bad prediction: high curiosity;
	- Alexei Efros: https://youtu.be/iTbfEXFwDJc
		- Optimistic view: PASCAL VOC -> ImageNet -> MS COCO -> LVIS;
		- No-fixed dataset: data-augmentation?
		- Continual learning? Catastrophic forgetting?
		- **Test-time training (TTT)**
			- A Jabri, A Owens, A Efros. Space-Time Correspondence as a Contrastive Random Walk. NeurIPS'20
				- Task: play video forward then backward, should end at the same point;
				- https://ajabri.github.io/videowalk/
				- https://github.com/ajabri/videowalk
	- Stella Yu: https://youtu.be/F5mt4z-w_Mk
		- Metric learning?
		- Non-parametric softmax instance;
	- Ishan Misra: https://youtu.be/gbziPIn9uDI
		- Multi-view invariance, grouping;
		- **PIRL**: Ishan Misra, Laurens van der Maaten. Self-Supervised Learning of Pretext-Invariant Representations. CVPR'20
			- Invariant to pretext task;
		- AVID-CMA: Pedro Morgado, Nuno Vasconcelos, Ishan Misra. Audio-Visual Instance Discrimination with Cross-Modal Agreement. arxiv'20
			- Task: in same video, audio/video match in time?
			- https://github.com/facebookresearch/AVID-CMA
		- **SWAV**: Unsupervised Learning of Visual Features by Contrasting Cluster Assignments. NeurIPS'20
			- Task: same image, two augmentation zt, zs and their query codes qt, qs, loss as l(zt, qs) + l(zs, qt);
			- https://github.com/facebookresearch/swav
	- Carl Doersch: https://youtu.be/RWCc0nZOSBw
		- **BYOL**: Jean-Bastien Grill, Florian Strub, Florent Altché, Corentin Tallec, Pierre H. Richemond, Elena Buchatskaya, Carl Doersch, Bernardo Avila Pires, Zhaohan Daniel Guo, Mohammad Gheshlaghi Azar, Bilal Piot, Koray Kavukcuoglu, Rémi Munos, Michal Valko. Bootstrap your own latent: A new approach to self-supervised Learning. 2020
			- https://github.com/deepmind/deepmind-research/tree/master/byol
			- step 1: no-negative;
			- step 2: stop-gradient; (freeze target network)
				- import to avoid collapse;
			- step 3: prediction; **predict the other representation?**
		- **CrossTransformer**:
	- Paolo Favaro: https://youtu.be/APwHDZZcLuY
		- Short-cut: predict from local features;
		- Build global features: distinguish between objects;

## Augment Consistency
- **UDA**: Qizhe Xie, Zihang Dai, Eduard Hovy, Minh-Thang Luong, and Quoc V. Le. Unsupervised data augmentation for consistency training. 2019
	- https://github.com/google-research/uda
	<img src = '/Weak-Unsupervised/images/uda.png' width = '400px'>

## Google Brain
- F Locatello, S Bauer, M Lucic, G Rätsch, S Gelly, B Schölkopf, O Bachem. Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations. ICML'19
	- https://github.com/google-research/disentanglement_lib

## InfoNCE
- **CPC**: Aaron van den Oord, Yazhe Li, and Oriol Vinyals. Representation Learning with Contrastive Predictive Coding. NIPS'18
	- Insight: an encoder g_enc(x_t)=z_t, as well as c_t (info accumulated until t), given some {z_t+k, z_j1, z_j2, ...}, z_t+k as positive and others uniformly sampled as negative, do classification **InfoNCE**;
	- Architecture\
		<img src = '/Weak-Unsupervised/images/cpc.png' width = '400'>
	- Prediction\
		<img src = '/Weak-Unsupervised/images/cpc2.png' width = '400'>
	- Loss: InfoNCE\
		<img src = '/Weak-Unsupervised/images/cpc3.png' width = '400'>
	- Application in vision:
		- ResNet-101: g-enc\
			<img src = '/Weak-Unsupervised/images/cpc4.png' width = '500px'>
- **GIM (Greedy-InfoMax)**: Sindy Löwe, Peter O’Connor, Bastiaan S. Veeling. Putting An End to End-to-End: Gradient-Isolated Learning of Representations. NIPS'19 Honorable Mention Outstanding New Directions Paper Award
	- https://github.com/loeweX/Greedy_InfoMax
	- Key insight: layer-wise information preservation;
	- Algorithm: Divide CNN by depth into M modeules;\
		<img src = '/Weak-Unsupervised/images/gim1.png' width = '500px'>
	- Supervision: similar to CPC;\
		<img src = '/Weak-Unsupervised/images/gim2.png' width = '500px'>
	- Experiments:
		- Vision: STL-10;
		- Audio: LibriSpeech speaker recognition (100-hour);

## Unclassified
- Supervising Unsupervised Learning. NIPS'18

## NIPS'19
- Tam Nguyen, Maximilian Dax, Chaithanya Kumar Mummadi, Nhung Ngo, Thi Hoai Phuong Nguyen, Zhongyu Lou, Thomas Brox. DeepUSPS: Deep Robust Unsupervised Saliency Prediction via Self-supervision
- Adam Bielski, Paolo Favaro. Emergence of Object Segmentation in Perturbed Generative Models
- Christopher Beckham, Sina Honari, Alex Lamb, Vikas Verma, Farnoosh Ghadiri, R Devon Hjelm, Yoshua Bengio, Chris Pal. On Adversarial Mixup Resynthesis
- Iordanis Kerenidis, Jonas Landman, Alessandro Luongo, Anupam Prakash. q-means: A quantum algorithm for unsupervised machine learning
- Hongteng Xu, Dixin Luo, Lawrence Carin. Scalable Gromov-Wasserstein Learning for Graph Partitioning and Matching
- Hugo Caselles-Dupré, Michael Garcia Ortiz, David Filliat. Symmetry-Based Disentangled Representation Learning requires Interaction with Environments
