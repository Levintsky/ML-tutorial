# Attack, Adversarial

## Tutorial
- B Biggio, F Roli. Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning. 2018
- https://zhuanlan.zhihu.com/p/32037178

## Basic Concepts
- White-box attack
- Poison attack (add poison data in training)
- Defense:
	- Reactive
	- Proactive

## Classic
- D Lowd, C Meek. Adversarial Learning. KDD'05
- C Szegedy, W Zaremba, I Sutskever, J Bruna, D Erhan, I Goodfellow, R Fergus	. Intriguing properties of neural networks. ICLR'14
- **FGSM**: I J. Goodfellow, J Shlens, C Szegedy. Explaining and harnessing adversarial examples. ICLR'15
	- Key: apply sign of gradient rather than gradient itself;
- A Nguyen, J Yosinski, J Clune. Deep Neural Networks are Easily Fooled: High Confidence Predictions for Unrecognizable Images. CVPR'15
	- Evolutionary; MAP-Elite; (keep best found so far)
- S Moosavi-Dezfooli, A Fawzi, P Frossard. DeepFool: a simple and accurate method to fool deep neural networks. 2016
- N Papernot, P McDaniel, I Goodfellow, S Jha, Z Celik, A Swami. Practical Black-Box Attacks against Machine Learning. 2017
	- Black box (no-access to parameter and net structure)
	- Adversarial exmaples are transferrable
- N Carlini and D Wagner. Towards Evaluating the Robustness of Neural Networks. IEEE Security and Privacy 2017 (Best Student Paper)
- Y Dong, F Liao, T Pang, H Su, J Zhu, X Hu, J Li. Boosting Adversarial Attacks with Momentum. CVPR'18
	- 2017 winner;
- Eykholt. Robust Physical-World Attacks on Deep Learning Visual Classification. CVPR'18
- **PGD**: A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu. Towards deep learning models resistant to adversarial attacks. ICLR'18
- C Xiang, C Qi, B Li. Generating 3D Adversarial Point Clouds, CVPR'19
	- https://github.com/xiangchong1/3d-adv-pc
	- adversarial point perturbation or adversarial point generation

## Robustness/Defense
- A Kurakin, I Goodfellow, and S Bengio. Adversarial machine learning at scale. ICLR'17
- A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu. Towards deep learning models resistant to adversarial attacks. ICLR'18
- **ALP**: H. Kannan, A. Kurakin, and I. Goodfellow. Adversarial logit pairing. NIPS'18
- C Xie, Y Wu, L Maaten, A Yuille, and K He. Kaiming, Feature Denoising for Improving Adversarial Robustness. CVPR'19
	- CAAD defense champion;
	- https://github.com/facebookresearch/ImageNet-Adversarial-Training
	- Non-local means (best), mean-filter, median filter, bilateral filter;