# Data Augmentation

## Unclassified
- **mixup**: Zhang, H., Cisse, M., Dauphin, Y. N., and Lopez-Paz, D. mixup: Beyond empirical risk minimization. arXiv'17

## Legacy
- Bellegarda, J. R., de Souza, P. V., Nadas, A. J., Nahamoo, D., Picheny, M. A., and Bahl, L. R. Robust speaker adaptation using a piecewise linear acoustic mapping. In ICASSP-92

## Vision
- AlexNet;
- **cutout**: DeVries, T. and Taylor, G. W. Improved regularization of convolutional neural networks with cutout. arxiv'17
	- useful on CIFAR-10 and not on ImageNet
- Ekin D Cubuk, Barret Zoph, Dandelion Mane, Vijay Vasudevan, and Quoc V Le. Autoaugment:
Learning augmentation policies from data. 2018
- Lopes, R. G., Yin, D., Poole, B., Gilmer, J., and Cubuk, E. D. Improving robustness without sacrificing accu- racy with patch gaussian augmentation. arXiv'19
- **RandAugment**: Ekin D. Cubuk, Barret Zoph, Jonathon Shlens, and Quoc V. Le. Randaugment: Practical automated data augmentation with a reduced search space. 2019
	- https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet
	- Transformation: identity, autoContrast, equalize, rotate, solarize, color, posterize, contrast, brightness, sharpness, shear-x, shear-y, translate-x, translate-y;
	- Scale 0 - 10 augmentation magnitude;\
		<img src = '/DL/images/augment/randaugment.png' width = '400'>
- Raphael Gontijo-Lopes, Sylvia J. Smullin, Ekin D. Cubuk, Ethan Dyer. Affinity and Diversity: Quantifying Mechanisms of Data Augmentation. 2020
	- Define Affinity and Diversity: affinity = accuracy gap on validation; diversity = training loss gap;\
		<img src = '/DL/images/augment/affinity.png' width = '400'>
		<img src = '/DL/images/augment/diversity.png' width = '400'>
	- Empiricaly study: the larger the affinity/diversity, the better\
		<img src = '/DL/images/augment/aff-div.png' width = '400'>

## NLP
- Adams Wei Yu, David Dohan, Minh-Thang Luong, Rui Zhao, Kai Chen, Mohammad Norouzi, and
Quoc V Le. Qanet: Combining local convolution with global self-attention for reading comprehension. 2018

## Speech
- Awni Hannun, Carl Case, Jared Casper, Bryan Catanzaro, Greg Diamos, Erich Elsen, Ryan Prenger, Sanjeev Satheesh, Shubho Sengupta, Adam Coates, et al. Deep speech: Scaling up end-to-end speech recognition. 2014
- **Specaugment**: Daniel S Park, William Chan, Yu Zhang, Chung-Cheng Chiu, Barret Zoph, Ekin D Cubuk, and
Quoc V Le. Specaugment: A simple data augmentation method for automatic speech recognition. 2019

## Dataset Reduction
- Tongzhou Wang, Jun-Yan Zhu, Antonio Torralba, Alexei A. Efros. Dataset Distillation. ICLR'19 reject
