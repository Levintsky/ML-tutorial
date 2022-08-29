# Data Augmentation/Generation

## Basics
- Augment or generate new data;
- Goal:
	- Not enough data;
- Data Augmentation
	- Image Augmentation
		- Basic Image Processing Operations
		- Task-Specific Augmentation Strategies:
			- AutoAugment (RL), RandAugment (reduced search space, magnitude only), Population based (evolutionary), UDA;
		- Image Mixture:
			- Mixup, Cutmix (cut paste), MoCHi (HNM)
	- Text Augmentation
		- Lexical Edits: synomym replacement, random swap/delete words;
		- Back-translation: translate to another language, then back;
			- CERT (Contrastive self-supervised Encoder Representations from Transformers; Fang et al. (2020);
		- Mix-up: Guo'19 on embedding space; adding adversarial;
	- Audio Augmentation
		- Wang & van den Oord (2021): mixup, masking, frequency masking, frequency shift;
	- Architectural Augmentation: dropout, SimCSE (Guo'21), cutoff (Shen'20)
- Data Synthesis
	- Language Model as Noisy Annotator: GPT-3 as a weak annotator (Wang'21)
	- Language Model as Data Generator: LAMBADA (Anaby-Tavor et al. 2019), Kumar et al. 2021
- How to Quantify Generated Data Quality? Gontijo-Lopes et al. (2020)
	- Affinity: distribution shift; KL(p(y|x), p(y|x')) model sensitive;
	- Diversity:
- Training with Noisy Data
	- Survey: Learning from Noisy Labels with Deep Neural Networks: A Survey. '21
	- Regularization and Robust Architecture: noisy adaptation layer;
	- Robust Learning Objective: L1 > L2;
	- Label Correction: F-correction (Patrini et al. 2017);
	- Sample Reweighting and Selection
- Tutorial: https://lilianweng.github.io/posts/2022-04-15-data-gen/

## Data Augmentation
- Legacy
	- Bellegarda, J. R., de Souza, P. V., Nadas, A. J., Nahamoo, D., Picheny, M. A., and Bahl, L. R. Robust speaker adaptation using a piecewise linear acoustic mapping. ICASSP'92
- Mixup:
	- Insight: convex linear combination:
		- x˜ = λxi + (1−λ)xj 
		- y˜ = λyi + (1−λ)yj 
	- **mixup**: Zhang, H., Cisse, M., Dauphin, Y. N., and Lopez-Paz, D. mixup: Beyond empirical risk minimization. ICLR'18
		- https://github.com/facebookresearch/mixup-cifar10
	- Guo, H., Mao, Y., and Zhang, R. Augmenting data with
	mixup for sentence classification: An empirical study. arxiv'19
		- Two strategy proposed: Interpolate on word or sentence embedding;
	- Guo, H., Mao, Y., and Zhang, R. Mixup as locally linear out-of-manifold regularization. AAAI'19
		- H := argmin{LD(H) + LD′(H)}
	- Verma, V., Lamb, A., Beckham, C., Najafi, A., Mitliagkas, I., Lopez-Paz, D., and Bengio, Y. Manifold mixup: Better representations by interpolating hidden states. ICLR'19
		- Predict less confidently on interpolations of hidden representations.
		- https://github.com/vikasverma1077/manifold_mixup
		- 1. Select a random layer k (could be input);
		- 2. Two minibatches (x,y), (x', y')
		- 3. Input mixup from layer k, mixing λ ∼ Beta(α, α);
		- 4. Forwarded (g˜k(x), y˜) used as output;
	- Guo, H. Nonlinear mixup: Out-of-manifold data augmentation for text classification. AAAI'20
		- Nonlinear interpolation for both data and label;
	- Zhang, L., Deng, Z., Kawaguchi, K., Ghorbani, A., and Zou, J. How does mixup help with robustness and generalization? ICLR'21
		- Insight: prove adversarial robustness and generalization;
- Vision
	- AlexNet;
	- **cutout**: DeVries, T. and Taylor, G. W. Improved regularization of convolutional neural networks with cutout. arxiv'17
		- useful on CIFAR-10 and not on ImageNet
	- **AutoAugment**: Ekin D. Cubuk, Barret Zoph, Dandelion Mane, Vijay Vasudevan, Quoc V. Le. AutoAugment: Learning Augmentation Policies from Data. CVPR'19
	- Lopes, R. G., Yin, D., Poole, B., Gilmer, J., and Cubuk, E. D. Improving robustness without sacrificing accuracy with patch gaussian augmentation. arXiv'19
	- **RandAugment**: Ekin D. Cubuk, Barret Zoph, Jonathon Shlens, and Quoc V. Le. Randaugment: Practical automated data augmentation with a reduced search space. 2019
		- https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet
		- Transformation: identity, autoContrast, equalize, rotate, solarize, color, posterize, contrast, brightness, sharpness, shear-x, shear-y, translate-x, translate-y;
		- Scale 0 - 10 augmentation magnitude;
	- Raphael Gontijo-Lopes, Sylvia J. Smullin, Ekin D. Cubuk, Ethan Dyer. Affinity and Diversity: Quantifying Mechanisms of Data Augmentation. 2020
		- Define Affinity and Diversity: affinity = accuracy gap on validation; diversity = training loss gap;\
			<img src = '/DL/images/augment/affinity.png' width = '400'>
			<img src = '/DL/images/augment/diversity.png' width = '400'>
		- Empiricaly study: the larger the affinity/diversity, the better\
			<img src = '/DL/images/augment/aff-div.png' width = '400'>
- NLP
	- Adams Wei Yu, David Dohan, Minh-Thang Luong, Rui Zhao, Kai Chen, Mohammad Norouzi, and Quoc V Le. Qanet: Combining local convolution with global self-attention for reading comprehension. 2018
- Speech
	- Awni Hannun, Carl Case, Jared Casper, Bryan Catanzaro, Greg Diamos, Erich Elsen, Ryan Prenger, Sanjeev Satheesh, Shubho Sengupta, Adam Coates, et al. Deep speech: Scaling up end-to-end speech recognition. 2014
	- **Specaugment**: Daniel S Park, William Chan, Yu Zhang, Chung-Cheng Chiu, Barret Zoph, Ekin D Cubuk, and
	Quoc V Le. Specaugment: A simple data augmentation method for automatic speech recognition. 2019
- Dataset Reduction
	- Tongzhou Wang, Jun-Yan Zhu, Antonio Torralba, Alexei A. Efros. Dataset Distillation. ICLR'19 reject
