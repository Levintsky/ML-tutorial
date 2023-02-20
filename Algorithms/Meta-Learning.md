# Meta-Learning

## Basics
- Approaches:
	- Bilevel:
		- Learn a meta-learner to control and guide basic learner;
			- GD by GD;
			- Directly predict some parameters;
		- Learn a initialization s.t. the basic learner can fast adapt;
			- HyperParameter learning: Bayes, R Adams;
			- Init: MAML;
			- Bayesian: BMAML, PMAML;
			- Implicit-iMAML;
	- Slow-fast update: 
- Summary:
	- https://github.com/floodsung/Meta-Learning-Papers
- Applications:
	- Low-shot learning;

## Unclassified
- F Hutter, H Hoos, and K Leyton-Brown. Sequential model-based optimization for general algorithm configuration. LION'05
- F Hutter, L Xu, H Hoos, and K Leyton-Brown. Algorithm runtime prediction: Methods and evaluation (extended abstract). IJCAI'15
- T Domhan, J Springenberg, F Hutter. Speeding up Automatic Hyperparameter Optimization of Deep Neural Networksby Extrapolation of Learning Curves. IJCAI 2015
	- https://github.com/automl/pylearningcurvepredictor
- D Ha, A Dai and Q Le. Hypernetworks. ICLR 2017.
- J. Bergstra, R. Bardenet, Y. Bengio, and B. Kegl. Algorithms for hyper-parameter optimization. NIPS'11
- E Hazan, A Klivans, Y Yuan. Hyperparameter Optimization: A Spectral Approach. NIPS DLTP Workshop 2017
	- https://github.com/callowbird/Harmonica
- Bayesian-Based Hyperparameter Learning
	- J Snoek, H Larochelle, and R Adams. Practical bayesian optimization of machine learning algorithms. NIPS'12
	- J Snoek, et. al. Scalable bayesian optimization using deep neural networks. NIPS'15
	- DeepMind. Taking the human out of the loop: A review of bayesian optimization. 2016
	- Gradient based hyper-parameter optimization:
		- D Maclaurin, D Duvenaud, R Adams. Gradient-based hyperparameter optimization through reversible learning. ICML'15
		- F Pedregosa. Hyperparameter optimization with approximate gradient. ICML'16

## Legacy
- J Schmidhuber. Evolutionary principles in self-referential learning. 1987
- Y Yoshua, S Bengio, and J Cloutier. Learning a synaptic learning rule. '91
- D Naik and R Mammone. Meta-neural networks that learn by learning. IJCNN'92
- S Thrun and L Pratt. Learning to learn. 1998

## Meta-RL
- L2RL: DeepMind. Learning to reinforcement learn. CogSci 2016
- RL2: OpenAI. RL2: Fast Reinforcement Learning via Slow Reinforcement Learning. 2016
	- Fast RL: learned "algorithm" performed by LSTM
	- Slow RL: algorithm used to train LSTM in outer loop
- DeepMind. Been There, Done That: Meta-Learning with Episodic Recall. ICML'18
- DeepMind. Meta-Gradient Reinforcement Learning. NIPS'18
- OpenAI. Model-Based Reinforcement Learning via Meta-Policy Optimization. CoRL'18
- OpenAI. On First-Order Meta-Learning Algorithms. 2018
- Berkeley. The Importance of Sampling in Meta-Reinforcement Learning. NIPS'18
- Sergey. Meta-Reinforcement Learning of Structured Exploration Strategies. NIPS'18
- Zero-Shot Transfer with Deictic Object-Oriented Representation in Reinforcement Learning. NIPS'18
- DeepMind. Reinforcement Learning, Fast and Slow. Trends in Cognitive Sciences'19
- MAML for RL: https://github.com/cbfinn/maml_rl
- SNAIL: A Simple Neural Attentive Meta-Learner, Mishra et al'18

## MAML, Bi-level Optimization
- Intuition:
	- Sharing parameters between tasks;
- D Maclaurin, D Duvenaud, and R Adams. Gradient-based hyperparameter optimization through reversible learning. ICML'15
- **MAML**: ICML'17
	- https://github.com/cbfinn/maml (tensorflow)
	- https://github.com/katerakelly/pytorch-maml (pytorch)
	- A bi-level optimization problem
		- θ = argminF(θ), where F(θ)=1/M ΣL(Alg(θ, Dtr), Dte)
	- Inner level: SGD
		- φi := Alg(θ, Dtr) = θ - α∇θ L(θ, Dtr)
	- Theory support: C Finn and S Levine. Meta-learning and universality: Deep representations and gradient descent can approximate any learning algorithm. 2017
- M Al-Shedivat, T Bansal, Y Burda, I Sutskever, I Mordatch, and P Abbeel. Continuous adaptation via meta-learning in nonstationary and competitive environments. 2017
- C Finn, T Yu, T Zhang, P Abbeel, and S Levine. One-shot visual imitation learning via meta-learning. 2017
- Shared parameters **reduce overfitting**:
	- N Mishra, M Rohaninejad, X Chen, and P Abbeel. A Simple Neural Attentive Meta-Learner. ICLR'18
	- Y Lee and S Choi. Meta-Learning with Adaptive Layerwise Metric and Subspace. ICLR'18
	- T Munkhdalai, X Yuan, S Mehri, T Wang and A Trischler. Learning rapid-temporal adaptations. ICML'18
- Shared parameters induce robust convergence:
	- Zintgraf, Luisa M., Shiarlis, Kyriacos, Kurin, Vitaly, Hofmann, Katja, and Whiteson, Shimon. Fast Context Adaptation via Meta-Learning. ICML'19
- Bayes for MAML parameters:
	- BMAML: T Kim, J Yoon, O Dia, Sungwoong Kim, Y Bengio, S Ahn. Bayesian Model-Agnostic Meta-Learning. NIPS'18
		- Add uncertainty on both initial model and update
		- Stein Variational Gradient Descent (SVGD)
		- Extend uncertainty-awareness to meta-update
	- PMAML: C Finn, K Xu, S Levine. Probabilistic Model-Agnostic Meta-Learning. NIPS'18
		- Uncertainty
		- A graphical model view;
- Latent variables for concept or task inference:
	- F Zhou, B Wu and Z Li. Deep meta-learning: Learning to learn in the concept space. arxiv'18
	- CNP: M Garnelo, D Rosenbaum, C Maddison, T Ramalho, D Saxton, M Shanahan, Y Teh, D Rezende, A Eslami. Conditional Neural Processes. ICML'18
	- B Oreshkin, A Lacoste and P Rodriguez, Tadam: Task dependent adaptive metric for improved few-shot learning. NIPS'18
	- A Rusu, D Rao, J Sygnowski, O Vinyals, R Pascanu, S Osindero and R Hadsell. Meta-learning with latent embedding optimization. ICLR'19
	- K Lee, S Maji, A Ravichandran and S Soatto. Meta-learning with differentiable convex optimization. CVPR'19
- Shared initialization:
	- S Flennerhag, H Yin, J Keane and M Elliot. Breaking the activation function bottleneck through adaptive parameterization. NIPS'18
	- A Nichol, J Achiam and J Schulman. On First-Order Meta-Learning Algorithms. arixv'18
	- S Flennerhag, P Moreno, N Lawrence and A Damianou. Transferring knowledge across learning processes. ICLR'19
- C Finn, A Rajeswaran, S Kakade, and S Levine. Online meta-learning. ICML'19
- **iMAML**: A Rajeswaran, C Finn, S Kakade, S Levine. Meta-Learning with Implicit Gradients. NIPS'19
	- θ∗ = argmin.θ F(θ), where F(θ) = 1/M ∑Li(Alg.i(θ))
		- Alg.i(θ) = argmin.φ Gi(φ′,θ) = Li(φ′) + λ/2 ∥φ′-φ∥^2
	- Total and Partial Derivatives of the nested function:
		- dL(Alg(θ))/dθ = dφ/dθ ∇.φ Li(φ)
	- dAlg(θ)/dθ memory heavy, intractable large graph;
		- Obtain task φi with iterative solver s.t. ∥φ-Alg(θ)∥^2
		- vi = ∇.φ Li(φ)
		- CG to solve gi s.t. ∥gi - (I+1/λ ∇2L(φi))^-1vi∥ ≤ δ
		- ∇.θ F(θ) := 1/B ∑gi; used for SGD;
- M Yin, G Tucker, M Zhou, S Levine, C Finn. Meta-Learning without Memorization. 2019
	- Problem definition: Complete memorization in meta-learning is when the learned model ignores the task training data s.t.
		- I(y∗; D|x∗, θ) = 0
		- (i.e., q(y∗|x∗, θ, D)=q(y∗|x∗, θ) = E D'|x∗ [q(y∗|x∗, θ, D')].
- **warpgrad**: DeepMind. Meta-Learning with Warped Gradient Descent. ICLR'20
	- https://github.com/flennerhag/warpgrad
	- Insight: learn a meta-preconditioner mimicing 2nd-order to accelerate;
- Applications of MAML:
	- F Mi, M Huang, J Zhang, and B Faltings. Meta-learning for low-resource natural language generation in task-oriented dialogue systems. 2019

## Gradient Descent-Based
- S Hochreiter, S Younger and P Conwell. Learning to learn using gradient descent. ICANN'01
- RNN:
	- M Andrychowicz, M Denil, S Gomez, M Hoffman, D Pfau, T Schaul, B Shillingford, and N Freitas. Learning to learn by gradient descent by gradient descent. NIPS'16
	- S. Ravi and H. Larochelle. Optimization as a model for fewshot learning. ICLR 2017

## Slow-Fast
- Intuition:
	- Separate parameters into slow and fast weights;
	- where the former captures meta-information and the latter encapsulates rapid adaptation;
- G Hinton and D Plaut. Using fast weights to deblur old memories. '87
- J Schmidhuber. Learning to control fast-weight memories: An alternative to dynamic recurrent networks. Neural Computation'92
- D Ha, A Dai, and Q Le. Hypernetworks. ICLR'16
	- Insight: embedding a neural network that dynamically adapts the parameters of a main architecture
- J Ba, G Hinton, V Mnih, J Leibo, and C Ionescu. Using fast weights to attend to the recent past. NIPS'16
- Low shot:
	- B Lake. Science'15
	- Matching networks: O Vinyals, et al. NIPS'16
	- SNAIL: P Abbeel, et. al. A Simple Neural Attentive Meta-Learner, ICLR 2018
		- Temporal 1D-Conv + Attention;
	- M Ren, E Triantafillou, S Ravi, J Snell, K Swersky, J Tenenbaum, H Larochelle and R Zemel. Meta-learning for semi-supervised few-shot classification. ICLR'18

## Directly Predict Parameters For Base Learner
- Intuition:
	- Directly predict the parameters of the task learner;
	- To scale, such methods typically pretrain a feature extractor and predict a small subset of the parameters.
- L. Bertinetto, J. F. Henriques, J. Valmadre, P. Torr, and A. Vedaldi. Learning feed-forward one-shot learners. NIPS'16
- H. Qi, M. Brown, and D. G. Lowe. Low-shot learning with imprinted weights. 2017
- T Munkhdalai, X Yuan, S Mehri, T Wang and A Trischler. Learning rapid-temporal adaptations. ICML'18
- S Gidaris and N Komodakis. Dynamic few-shot visual learning without forgetting. CVPR'18
- S Qiao, C Liu, W Shen and A Yuille. Few-shot image recognition by predicting parameters from activations. CVPR'18

## Memory-based
- A Santoro, S Bartunov, M Botvinick, D Wierstra, and T Lillicrap. Meta-learning with memory-augmented neural networks. ICML'16
- J Wang, Z Kurth-Nelson, D Tirumala, H Soyer, J Leibo, R Munos, C Blundell, D Kumaran, M Botvinick. Learning to reinforcement learn. CogSci'17

## Learn to Compare
- J Snell, K Swersky, R Zemel. Prototypical Networks for Few-shot Learning. NIPS'17
- F. Sung, Y. Yang, L. Zhang, T. Xiang, P. H. Torr, and T. M. Hospedales. Learning to compare: Relation network for fewshot learning. CVPR'18.

## Detection
- B Kang, Z Liu, X Wang, F Yu, J Feng, T Darrell. Few-shot Object Detection via Feature Reweighting. 2018
	- Built on YOLOv2
	- Assumptions: feature can be reused, different features play important roles in specific classes
	- Train a meta-conv module as weight, to reweight features
- Y.-X. Wang and M. Hebert. Model recommendation: Generating object detectors from few samples. CVPR 2015