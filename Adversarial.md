# Attack, Adversarial

## Classic
- Intriguing properties of neural networks. ICLR'14
- I J. Goodfellow, J Shlens, C Szegedy. Explaining and harnessing adversarial examples. ICLR'15
	- Key: apply sign of gradient rather than gradient itself;
- N Carlini and D Wagner. Towards Evaluating the Robustness of Neural Networks. IEEE Security and Privacy 2017 (Best Student Paper)
- Eykholt. Robust Physical-World Attacks on Deep Learning Visual Classification. CVPR'18
- **PGD**: A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu. Towards deep learning models resistant to adversarial attacks. ICLR'18
- C Xiang, C Qi, B Li. Generating 3D Adversarial Point Clouds, CVPR'19
	- https://github.com/xiangchong1/3d-adv-pc
	- adversarial point perturbation or adversarial point generation

## Robustness/Defense
- A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu. Towards deep learning models resistant to adversarial attacks. ICLR'18
- **ALP**: H. Kannan, A. Kurakin, and I. Goodfellow. Adversarial logit pairing. NIPS'18
- C Xie, Y Wu, L Maaten, A Yuille, and K He. Kaiming, Feature Denoising for Improving Adversarial Robustness. CVPR'19
	- CAAD defense champion;
	- https://github.com/facebookresearch/ImageNet-Adversarial-Training
	- Non-local means (best), mean-filter, median filter, bilateral filter;