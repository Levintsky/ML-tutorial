# Unsupervised, Weak-Supervised, SSL

## Resources
- NIPS'18 Tutorial: https://media.neurips.cc/Conferences/NIPS2018/Slides/Visualization_for_ML.pdf

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
		<img src = '/Weak-Unsupervised/images/cpc.png' width = '400px'>
	- Prediction\
		<img src = '/Weak-Unsupervised/images/cpc2.png' width = '400px'>
	- Loss: InfoNCE\
		<img src = '/Weak-Unsupervised/images/cpc3.png' width = '500px'>
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