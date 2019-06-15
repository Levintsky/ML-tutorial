# Model-based RL

## Sergey Levine
- Known dynamics (lec-11)
<img src="/RL/images/mbrl1.png" alt="drawing" width="500"/>

- Linear case:
	- LQR: linear transition, quadratic cost
	<img src="/RL/images/mbrl2.png" alt="drawing" width="600"/>

	- Solved with backward recursion
	<img src="/RL/images/mbrl3.png" alt="drawing" width="550"/>

- Nonlinear case: DDP/iterative LQR
	- iLQR
	<img src="/RL/images/mbrl4.png" alt="drawing" width="550"/>

- Learn dynamics (lec-12)
	- Uncertainty-aware models
	- Aleatoric or statistical uncertainty
	- Epistemic or model uncertainty
	- Bayesian neural network
	- Bootstrap ensembles p(theta|D)
	- Moment matching (project to Gaussian)

## Learn a Model
-  World Model:
	- DeepMind
		- Neural Predictive Belief Representations, ICLR 2019
			- Contrastive-Predictive Coding (CPC)
		- Representation Learning with Contrastive Predictive Coding (NIPS 2018)		

## Atari
- J. Oh, X. Guo, H. Lee, R. Lewis, and S.Singh. Action-conditional video prediction using deep networks in atari games. arxiv, 2015.
- Recurrent World Models Facilitate Policy Evolution， NIPS 2018
	- VAE for compression and regularization
	- Predict next step
	- https://worldmodels.github.io
- Łukasz Kaiser, Mohammad Babaeizadeh, Piotr Miłos, Błazej Osinski, Roy H Campbell, Konrad Czechowski, Dumitru Erhan, Chelsea Finn, Piotr Kozakowski, Sergey Levine, Ryan Sepassi, George Tucker, Henryk Michalewski. Model Based Reinforcement Learning for Atari. 2019
	- SimPLe
	- https://ai.googleblog.com/2019/03/simulated-policy-learning-in-video.html
	- Open sourced at https://github.com/tensorflow/tensor2tensor
	- Main loop:
		- The agent starts interacting with the real environment.
		- The collected observations are used to update the current world model.
		- The agent updates the policy by learning inside the world model.
	- World model: feed-forward CNN
		- Input 4 frames
		- Output: predicts next frame (256 softmax)
		- Output: Reward
	- RL:
		- PPO
	- Experiment: 100k interactions;

## Continuous (MuJoCo, Robotics)
- M P Deisenroth, C E Rasmussen, D Fox. Learning to Control a Low-Cost Manipulator using Data-Efficient Reinforcement Learning. RSS'11
	- Gaussian Process to learn the dynamics
- Guided policy search (model-based RL) for image-based robotic manipulation https://github.com/cbfinn/gps
- End-to-end training of deep visuomotor policies, L, Finn ’16
- A Nagabandi, G Kahn, R S. Fearing, S Levine. Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning. ICLR'18
	- At beginning: avoid overfitting (MBRL is better)
	- Later: avoid underfitting (MF-RL is better)
	- Mb-Mf best
- V Feinberg, A Wan, I Stoica, M I. Jordan, J E. Gonzalez, S Levine. Model-Based Value Expansion for Efficient Model-Free Reinforcement Learning. ICML'18
- K Chua, R Calandra, R McAllister, S Levine. Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models. NIPS'18
- J Buckman, D Hafner, G Tucker, E Brevdo, H Lee. Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion. NIPS'18
- **SOLAR**: M Zhang, S Vikram, L Smith, P Abbeel, M J. Johnson, S Levine. SOLAR: Deep Structured Representations for Model-Based Reinforcement Learning. ICML'19

## Legacy
- **PILCO**: M P Deisenroth, C E Rasmussen. PILCO: A Model-Based and Data-Efficient Approach to Policy Search. ICML'11
- **DDP**: Mayne, Jacobson. Differential dynamic programming. 1970
- **iLQR**: Tassa, Erez, Todorov.  Synthesis and Stabilization of Complex
Behaviors through Online Trajectory Optimization. 2012