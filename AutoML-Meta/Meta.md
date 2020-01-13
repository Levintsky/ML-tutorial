# Meta-Learning

## Summary
- https://github.com/floodsung/Meta-Learning-Papers
- LSTM Learner:
- Parameter Prediction
	- L. Bertinetto, J. F. Henriques, J. Valmadre, P. Torr, and A. Vedaldi. Learning feed-forward one-shot learners. NIPS 2016
	- H. Qi, M. Brown, and D. G. Lowe. Low-shot learning with imprinted weights. 2017

## Unclassified
- Probabilistic Matrix Factorization for Automated Machine Learning. NIPS'18
- Yoshua Bengio. MetaGAN: An Adversarial Approach to Few-Shot Learning. NIPS'18
- Delta-encoder: an effective sample synthesis method for few-shot object recognition. NIPS'18

## Legacy
- Jurgen Schmidhuber. Evolutionary principles in self-referential learning. 1987
- Devang K Naik and RJ Mammone. Meta-neural networks that learn by learning. IJCNN'92
- Sebastian Thrun and Lorien Pratt. Learning to learn. 1998

## Attention
- Oriol Vinyals, Charles Blundell, Tim Lillicrap, Daan Wierstra, et al. Matching networks for
one shot learning. NIPS'16
- **SNAIL**: Pieter Abbeel, et. al. A Simple Neural Attentive Meta-Learner, ICLR 2018
	- Temporal 1D-Conv + Attention;

## Recurrent
- Sepp Hochreiter, A Steven Younger, and Peter R Conwell. Learning to learn using gradient
descent. ICANN'01
- Adam Santoro, Sergey Bartunov, Matthew Botvinick, Daan Wierstra, and Timothy Lillicrap.
Meta-learning with memory-augmented neural networks. ICML'16
- S. Ravi and H. Larochelle. Optimization as a model for fewshot learning. ICLR 2017

## MAML, Bi-level Optimization
- Dougal Maclaurin, David Duvenaud, and Ryan Adams. Gradient-based hyperparameter optimization through reversible learning. ICML'15
- **MAML**: Chelsea Finn, Pieter Abbeel, and Sergey Levine. Model-agnostic meta-learning for fast adaptation of deep networks. ICML'17
	- https://github.com/cbfinn/maml (tensorflow)
	- https://github.com/katerakelly/pytorch-maml (pytorch)
	- A bi-level optimization problem\
		<img src = '/AutoML-Meta/images/maml1.png' width='400'>
	- Inner level: SGD\
		<img src = '/AutoML-Meta/images/maml2.png' width='400'>
- Chelsea Finn and Sergey Levine. Meta-learning and universality: Deep representations and
gradient descent can approximate any learning algorithm. 2017
- Maruan Al-Shedivat, Trapit Bansal, Yuri Burda, Ilya Sutskever, Igor Mordatch, and Pieter
Abbeel. Continuous adaptation via meta-learning in nonstationary and competitive environments. 2017
- Chelsea Finn, Tianhe Yu, Tianhao Zhang, Pieter Abbeel, and Sergey Levine. One-shot visual
imitation learning via meta-learning. 2017
- **BMAML**: Taesup Kim, Jaesik Yoon, Ousmane Dia, Sungwoong Kim, Yoshua Bengio, Sungjin Ahn.  Bayesian Model-Agnostic Meta-Learning. NIPS'18
	- BMAML
	- Add uncertainty on both initial model and update
	- Stein Variational Gradient Descent (SVGD)
	- Extend uncertainty-awareness to meta-update
- **PMAML**: Chelsea Finn, Kelvin Xu, Sergey Levine. Probabilistic Model-Agnostic Meta-Learning. NIPS'18
	- Uncertainty
	- A graphical model view
- Chelsea Finn, Aravind Rajeswaran, Sham Kakade, and Sergey Levine. Online meta-learning. ICML'19
- **iMAML**: Aravind Rajeswaran, Chelsea Finn, Sham Kakade, Sergey Levine. Meta-Learning with Implicit Gradients. NIPS'19
	- Notice the regularization:\
		<img src = '/AutoML-Meta/images/iMAML1.png' width='400'>
	- Total and Partial Derivatives of the nested function:\
		<img src = '/AutoML-Meta/images/iMAML2.png' width='400'>
	- dAlg(theta)/dtheta memory heavy, intractable large graph;\
		<img src = '/AutoML-Meta/images/iMAML3.png' width='400'>
- Applications of MAML:
	- Fei Mi, Minlie Huang, Jiyong Zhang, and Boi Faltings. Meta-learning for low-resource natural language generation in task-oriented dialogue systems. 2019

## General Low-Shot Learning
- F. Sung, Y. Yang, L. Zhang, T. Xiang, P. H. Torr, and T. M. Hospedales. Learning to compare: Relation network for fewshot learning. CVPR, 2018.

## Detection
- Bingyi Kang, Zhuang Liu, Xin Wang, Fisher Yu, Jiashi Feng, Trevor Darrell. Few-shot Object Detection via Feature Reweighting. 2018
	- Built on YOLOv2
	- Assumptions: feature can be reused, different features play important roles in specific classes
	- Train a meta-conv module as weight, to reweight features
- Y.-X. Wang and M. Hebert. Model recommendation: Generating object detectors from few samples. CVPR 2015