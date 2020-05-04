# Meta-Learning

## Summary
- https://github.com/floodsung/Meta-Learning-Papers
- LSTM Learner:
	
## Unclassified
- Probabilistic Matrix Factorization for Automated Machine Learning. NIPS'18
- Yoshua Bengio. MetaGAN: An Adversarial Approach to Few-Shot Learning. NIPS'18
- Delta-encoder: an effective sample synthesis method for few-shot object recognition. NIPS'18

## NIPS'19
- Mikhail Khodak, Maria-Florina Balcan, Ameet Talwalkar. Adaptive Gradient-Based Meta-Learning Methods
- Russell Mendonca, Abhishek Gupta, Rosen Kralev, Pieter Abbeel, Sergey Levine, Chelsea Finn. Guided Meta-Policy Search
- LU LIU, Tianyi Zhou, Guodong Long, Jing Jiang, Chengqi Zhang. Learning to Propagate for Graph Meta-Learning
- Yujia Xie, Haoming Jiang, Feng Liu, Tuo Zhao, Hongyuan Zha. Meta Learning with Relational Information for Short Sequences
- Eunbyung Park, Junier Oliva. Meta-Curvature
- Khurram Javed, Martha White. Meta-Learning Representations for Continual Learning
- Aravind Rajeswaran, Chelsea Finn, Sham Kakade, Sergey Levine. Meta-Learning with Implicit Gradients
- Jun Shu, Qi Xie, Lixuan Yi, Qian Zhao, Sanping Zhou, Zongben Xu, Deyu Meng. Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting
- Shikun Liu, Andrew Davison, Edward Johns. Self-Supervised Generalisation with Meta Auxiliary Learning

## Legacy
- Jurgen Schmidhuber. Evolutionary principles in self-referential learning. 1987
- Bengio, Yoshua, Bengio, Samy, and Cloutier, Jocelyn. Learning a synaptic learning rule. Université
de Montréal, Département d’informatique et de recherche opérationnelle, 1991.
- Devang K Naik and RJ Mammone. Meta-neural networks that learn by learning. IJCNN'92
- Sebastian Thrun and Lorien Pratt. Learning to learn. 1998

## MAML, Bi-level Optimization
- Intuition:
	- Sharing parameters between tasks;
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
- Shared parameters **reduce overfitting**:
	- Mishra, Nikhil, Rohaninejad, Mostafa, Chen, Xi, and Abbeel, Pieter. A Simple Neural Attentive Meta-Learner. ICLR'18
	- Lee, Yoonho and Choi, Seungjin. Meta-Learning with Adaptive Layerwise Metric and Subspace. ICLR'18
	- Munkhdalai, Tsendsuren, Yuan, Xingdi, Mehri, Soroush, Wang, Tong, and Trischler, Adam. Learning rapid-temporal adaptations. ICML'18
- Shared parameters induce robust convergence:
	- Zintgraf, Luisa M., Shiarlis, Kyriacos, Kurin, Vitaly, Hofmann, Katja, and Whiteson, Shimon. Fast Context Adaptation via Meta-Learning. ICML'19
- Bayes for MAML parameters:
	- **BMAML**: Taesup Kim, Jaesik Yoon, Ousmane Dia, Sungwoong Kim, Yoshua Bengio, Sungjin Ahn.  Bayesian Model-Agnostic Meta-Learning. NIPS'18
		- BMAML
		- Add uncertainty on both initial model and update
		- Stein Variational Gradient Descent (SVGD)
		- Extend uncertainty-awareness to meta-update
	- **PMAML**: Chelsea Finn, Kelvin Xu, Sergey Levine. Probabilistic Model-Agnostic Meta-Learning. NIPS'18
		- Uncertainty
		- A graphical model view;
- Latent variables for concept or task inference:
	- Zhou, Fengwei, Wu, Bin, and Li, Zhenguo. Deep meta-learning: Learning to learn in the concept space. arxiv'18
	- **CNP**: Marta Garnelo, Dan Rosenbaum, Chris J. Maddison, Tiago Ramalho, David Saxton, Murray Shanahan, Yee Whye Teh, Danilo J. Rezende, S. M. Ali Eslami. Conditional Neural Processes. ICML'18
	- Oreshkin, Boris N, Lacoste, Alexandre, and Rodriguez, Paul. Tadam: Task dependent adaptive metric for improved few-shot learning. NIPS'18
	- Rusu, Andrei A., Rao, Dushyant, Sygnowski, Jakub, Vinyals, Oriol, Pascanu, Razvan, Osindero, Simon, and Hadsell, Raia. Meta-learning with latent embedding optimization. ICLR'19
	- Lee, Kwonjoon, Maji, Subhransu, Ravichandran, Avinash, and Soatto, Stefano. Meta-learning with differentiable convex optimization. CVPR'19
- Shared initialization:
	- Flennerhag, Sebastian, Yin, Hujun, Keane, John, and Elliot, Mark. Breaking the activation function bottleneck through adaptive parameterization. NIPS'18
	- Nichol, Alex, Achiam, Joshua, and Schulman, John. On First-Order Meta-Learning Algorithms. arixv'18
	- Flennerhag, Sebastian, Moreno, Pablo G., Lawrence, Neil D., and Damianou, Andreas. Transferring knowledge across learning processes. ICLR'19
- Chelsea Finn, Aravind Rajeswaran, Sham Kakade, and Sergey Levine. Online meta-learning. ICML'19
- **iMAML**: Aravind Rajeswaran, Chelsea Finn, Sham Kakade, Sergey Levine. Meta-Learning with Implicit Gradients. NIPS'19
	- Notice the regularization:\
		<img src = '/AutoML-Meta/images/iMAML1.png' width='400'>
	- Total and Partial Derivatives of the nested function:\
		<img src = '/AutoML-Meta/images/iMAML2.png' width='400'>
	- dAlg(theta)/dtheta memory heavy, intractable large graph;\
		<img src = '/AutoML-Meta/images/iMAML3.png' width='400'>
- Mingzhang Yin, George Tucker, Mingyuan Zhou, Sergey Levine, Chelsea Finn. Meta-Learning without Memorization. 2019
	- Problem definition: Complete memorization in meta-learning is when the learned model ignores the task training data such that I(y\*; D|x\*, θ) = 0 (i.e., q(y\*|x\*, θ, D)=q(y\* | x\*, θ) = E D'|x\* [q( y \* | x\*, θ, D')].
- **warpgrad**: Sebastian Flennerhag, Andrei A. Rusu, Razvan Pascanu, Francesco Visin, Hujun Yin, Raia Hadsell. Meta-Learning with Warped Gradient Descent. ICLR'20
	- https://github.com/flennerhag/warpgrad
	- Insight: learn a meta-preconditioner mimicing 2nd-order to accelerate;
- Applications of MAML:
	- Fei Mi, Minlie Huang, Jiyong Zhang, and Boi Faltings. Meta-learning for low-resource natural language generation in task-oriented dialogue systems. 2019

## Gradient Descent-Based
- Hochreiter, Sepp, Younger, A. Steven, and Conwell, Peter R. Learning to learn using gradient descent. ICANN'01
- RNN:
	- Andrychowicz, Marcin, Denil, Misha, Gomez, Sergio, Hoffman, Matthew W, Pfau, David, Schaul, Tom, Shillingford, Brendan, and De Freitas, Nando. Learning to learn by gradient descent by gradient descent. NIPS'16
	- S. Ravi and H. Larochelle. Optimization as a model for fewshot learning. ICLR 2017

## Slow-Fast
- Intuition:
	- Separate parameters into slow and fast weights;
	- where the former captures meta-information and the latter encapsulates rapid adaptation;
- Hinton, Geoffrey E and Plaut, David C. Using fast weights to deblur old memories. In 9th Annual
Conference of the Cognitive Science Society, 1987.
- Schmidhuber, Jürgen. Learning to control fast-weight memories: An alternative to dynamic recurrent
networks. Neural Computation, 4(1):131–139, 1992.
- Ha, David, Dai, Andrew M., and Le, Quoc V. Hypernetworks. ICLR'16
	- Insight: embedding a neural network that dynamically adapts the parameters of a main architecture
- Ba, Jimmy, Hinton, Geoffrey E, Mnih, Volodymyr, Leibo, Joel Z, and Ionescu, Catalin. Using fast weights to attend to the recent past. NIPS'16
- Low shot:
	- Lake, Brenden M., Salakhutdinov, Ruslan, and Tenenbaum, Joshua B. Human-level concept learning through probabilistic program induction. Science'15
	- Oriol Vinyals, Charles Blundell, Tim Lillicrap, Daan Wierstra, et al. Matching networks for one shot learning. NIPS'16
	- **SNAIL**: Pieter Abbeel, et. al. A Simple Neural Attentive Meta-Learner, ICLR 2018
		- Temporal 1D-Conv + Attention;
	- Ren, Mengye, Triantafillou, Eleni, Ravi, Sachin, Snell, Jake, Swersky, Kevin, Tenenbaum, Joshua B., Larochelle, Hugo, and Zemel, Richard S. Meta-learning for semi-supervised few-shot classification. ICLR'18

## Directly Predict
- Intuition:
	- Directly predict the parameters of the task learner;
	- To scale, such methods typically pretrain a feature extractor and predict a small subset of the parameters.
- L. Bertinetto, J. F. Henriques, J. Valmadre, P. Torr, and A. Vedaldi. Learning feed-forward one-shot learners. NIPS 2016
- H. Qi, M. Brown, and D. G. Lowe. Low-shot learning with imprinted weights. 2017
- Munkhdalai, Tsendsuren, Yuan, Xingdi, Mehri, Soroush, Wang, Tong, and Trischler, Adam. Learning rapid-temporal adaptations. ICML'18
- Gidaris, Spyros and Komodakis, Nikos. Dynamic few-shot visual learning without forgetting. CVPR'18
- Qiao, Siyuan, Liu, Chenxi, Shen, Wei, and Yuille, Alan L. Few-shot image recognition by predict- ing parameters from activations. CVPR'18

## Memory-based
- Adam Santoro, Sergey Bartunov, Matthew Botvinick, Daan Wierstra, and Timothy Lillicrap.
Meta-learning with memory-augmented neural networks. ICML'16
- Jane X Wang, Zeb Kurth-Nelson, Dhruva Tirumala, Hubert Soyer, Joel Z Leibo, Remi Munos, Charles Blundell, Dharshan Kumaran, Matt Botvinick. Learning to reinforcement learn. CogSci'17

## Learn to Compare
- Jake Snell, Kevin Swersky, Richard S. Zemel. Prototypical Networks for Few-shot Learning. NIPS'17
- F. Sung, Y. Yang, L. Zhang, T. Xiang, P. H. Torr, and T. M. Hospedales. Learning to compare: Relation network for fewshot learning. CVPR'18.

## Detection
- Bingyi Kang, Zhuang Liu, Xin Wang, Fisher Yu, Jiashi Feng, Trevor Darrell. Few-shot Object Detection via Feature Reweighting. 2018
	- Built on YOLOv2
	- Assumptions: feature can be reused, different features play important roles in specific classes
	- Train a meta-conv module as weight, to reweight features
- Y.-X. Wang and M. Hebert. Model recommendation: Generating object detectors from few samples. CVPR 2015