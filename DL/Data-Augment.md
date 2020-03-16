# Data Augmentation

## Vision
- AlexNet;
- Ekin D Cubuk, Barret Zoph, Dandelion Mane, Vijay Vasudevan, and Quoc V Le. Autoaugment:
Learning augmentation policies from data. 2018
- **RandAugment**: Ekin D. Cubuk, Barret Zoph, Jonathon Shlens, and Quoc V. Le. Randaugment: Practical automated data augmentation with a reduced search space. 2019
	- https://github.com/tensorflow/tpu/tree/master/models/official/efficientnet
	- Transformation: identity, autoContrast, equalize, rotate, solarize, color, posterize, contrast, brightness, sharpness, shear-x, shear-y, translate-x, translate-y;
	- Scale 0 - 10 augmentation magnitude;

## NLP
- Adams Wei Yu, David Dohan, Minh-Thang Luong, Rui Zhao, Kai Chen, Mohammad Norouzi, and
Quoc V Le. Qanet: Combining local convolution with global self-attention for reading comprehension. 2018

## Speech
- Awni Hannun, Carl Case, Jared Casper, Bryan Catanzaro, Greg Diamos, Erich Elsen, Ryan Prenger, Sanjeev Satheesh, Shubho Sengupta, Adam Coates, et al. Deep speech: Scaling up end-to-end speech recognition. 2014
- Daniel S Park, William Chan, Yu Zhang, Chung-Cheng Chiu, Barret Zoph, Ekin D Cubuk, and
Quoc V Le. Specaugment: A simple data augmentation method for automatic speech recognition. 2019