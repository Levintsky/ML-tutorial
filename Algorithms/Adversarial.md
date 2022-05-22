# Attack, Adversarial

## Tutorial
- B Biggio, F Roli. Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning. 2018
- https://zhuanlan.zhihu.com/p/32037178
- https://www.jiqizhixin.com/articles/2018-03-05-4
- https://zhuanlan.zhihu.com/p/57733228
- https://medium.com/onfido-tech/adversarial-attacks-and-defences-for-convolutional-neural-networks-66915ece52e7

## Basic Concepts
- White-box attack
- Poison attack (add poison data in training)
- Defense:
	- Reactive
	- Proactive

## Unclassified
- Ke Li, Tianhao Zhang, Jitendra Malik. Approximate Feature Collisions in Neural Nets. NIPS'19

# Adversarial Learning
- Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Logan Engstrom, Brandon Tran, Aleksander Madry. Adversarial Examples Are Not Bugs, They Are Features. NeurIPS'19
	- Some features are robust, some are non-robust
	- Imagine binary classifcation: f(x) and y (+/-1)
	- Insight: create a new dataset, manipulate x (originally cat), s.t., turns it into a dog with cat-looking with dog-robust-feature and labled it as a dog in the new dataset;
- A Game Theoretic Approach to Class-wise Selective Rationalization. NIPS'19
- Donahue, J., Krahenbuhl, P., and Darrell, T. Adversarial feature learning.

## Attack
- Optimization-based:
	- **SOA**: N Carlini and D Wagner. Towards Evaluating the Robustness of Neural Networks. IEEE Security and Privacy 2017 (Best Student Paper)
	- Y Liu, X Chen, C Liu, and D Song. Delving into transferable adversarial examples and black-box attacks. ICLR'17
	-  I Evtimov, K Eykholt, E Fernandes, T Kohno, B Li, A Prakash, A Rahmati, and D Song. Robust physical-world attacks on machine learning models. 2017
	- C Xiao, J Zhu, B Li, W He, M Liu, and D Song. Spatially transformed adversarial examples. 2018
- D Lowd, C Meek. Adversarial Learning. KDD'05
- C Szegedy, W Zaremba, I Sutskever, J Bruna, D Erhan, I Goodfellow, R Fergus. Intriguing properties of neural networks. ICLR'14
- **FGSM**: I J. Goodfellow, J Shlens, C Szegedy. Explaining and harnessing adversarial examples. ICLR'15
	- Key: apply sign of gradient rather than gradient itself;
	- https://pytorch.org/tutorials/beginner/fgsm_tutorial.html
- A Nguyen, J Yosinski, J Clune. Deep Neural Networks are Easily Fooled: High Confidence Predictions for Unrecognizable Images. CVPR'15
	- Evolutionary; MAP-Elite; (keep best found so far)
- S Moosavi-Dezfooli, A Fawzi, P Frossard. DeepFool: a simple and accurate method to fool deep neural networks. 2016
- N Papernot, P McDaniel, I Goodfellow, S Jha, Z Celik, A Swami. Practical Black-Box Attacks against Machine Learning. 2017
	- Black box (no-access to parameter and net structure)
	- Adversarial exmaples are transferrable
- Y Dong, F Liao, T Pang, H Su, J Zhu, X Hu, J Li. Boosting Adversarial Attacks with Momentum. CVPR'18
	- 2017 winner;
- Eykholt. Robust Physical-World Attacks on Deep Learning Visual Classification. CVPR'18
- **PGD**: A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu. Towards deep learning models resistant to adversarial attacks. ICLR'18
- Unrestricted (no Lp norm constraint):
	- Y Song et al. Constructing unrestricted adversarial examples with generative models. 2018.
	- C Xiao, J Zhu, B Li, W He, M Liu, and D Song. Spatially transformed adversarial examples. 2018
	- H Hosseini and R Poovendran. Semantic adversarial examples. CVPRW'18
	- **UAE**: Unrestricted Adversarial Examples via Semantic Manipulation. ICLR'20
		- Problem: Colorization (cAdv); image to LAB space, input L (h x w x 1), sparse color hint (ab, h x w x 2), binary mask;
			- Per-pixel distribution from [Zhang 2017]
			- Only change high entropy region;
		- Problem: Texture Attck (tAdv); with Gram matrix;
		- Caption attack;
		- AMT study for naturalness;
	- G Shen, C Mao, J Yang, B Ray. Unrestricted Adversarial Attacks for Semantic Segmentation. ICLR'20
		- based on SPADE [Semantic image synthesis with spatially-adaptive normalization, 2019]
	- L Jain, W Wu, S Chen, U Jang, V Chandrasekaran, S Seshia, S Jha. Generating Semantic Adversarial Examples with Differentiable Rendering. ICLR'20 reject
	- H Qiu, C Xiao, L Yang, X Yan, H Lee, B Li. SemanticAdv: Generating Adversarial Examples via Attribute-Conditional Image Editing. ICLR'20 reject
	- Ameya Joshi, Amitangshu Mukherjee, Soumik Sarkar, Chinmay Hegde. Semantic Adversarial Attacks: Parametric Transformations That Fool Deep Classifiers. ICLR'20

## 3D
- Attack:
	- C Xiang, C Qi, B Li. Generating 3D Adversarial Point Clouds, CVPR'19
		- https://github.com/xiangchong1/3d-adv-pc
		- adversarial point perturbation or adversarial point generation
- Defense:
	- H Zhou, K Chen, W Zhang, H Fang, W Zhou, N Yu. DUP-Net: Denoiser and Upsampler Network for 3D Adversarial Point Clouds Defense. ICCV'19
		- 1. Remove outlier by local filtering;
		- 2. Upsampling: L Yu, X Li, C Fu, D Cohen-Or, P Heng. PU-Net: Point Cloud Upsampling Network. CVPR'18

## Robustness/Defense
- N Papernot, P McDaniel, X Wu, S Jha, A Swami. Distillation as a Defense to Adversarial Perturbations against Deep Neural Networks. 2016
- A Kurakin, I Goodfellow, and S Bengio. Adversarial machine learning at scale. ICLR'17
- A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu. Towards deep learning models resistant to adversarial attacks. ICLR'18
- **ALP**: H. Kannan, A. Kurakin, and I. Goodfellow. Adversarial logit pairing. NIPS'18
- Adversarially Robust Optimization with Gaussian Processes. NIPS'18
- C Xie, Y Wu, L Maaten, A Yuille, and K He. Feature Denoising for Improving Adversarial Robustness. CVPR'19
	- CAAD defense champion;
	- https://github.com/facebookresearch/ImageNet-Adversarial-Training
	- Non-local means (best), mean-filter, median filter, bilateral filter;
