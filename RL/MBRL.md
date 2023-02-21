# Model-based RL

## Basics
- Mordatch/Hamrick Tutorial (ICML'20)
- From Spinningup
	- Model learned: I2A, MBMF, MVE, STEVE, ME-TRPO, MB-MPO, world-models...
	- Model given: AlphaGo, Exit;
- https://zhuanlan.zhihu.com/p/72642285

## Unclassified
- A Strehl, L Li, M Littman. Incremental model-based learners with formal learning-time guarantees. UAI'06
- **MBIE-EB**: A Strehl, M Littman. An analysis of model-based interval estimation for Markov decision processes. JoCS'08
	- Init: ε, δ, m;
	- n(s,a,s')=0, rc(s,a)=0, n(s,a)=0, Q(s,a)=1/(1−γ);
	- Loop:
		- at = argmax Q(st,a);
		- Observe rt and state st+1;
		- Update stat n(s,a), n(s,a,s'), rc(s,a);
		- Update model: R(st,at) and T(s'|s,a)
		- Set Q(s, a) as exploration based reward by looping until convergence:
			- Q(s,a) = R(s,a) + γΣT(s'|s,a)maxQ(s',a) + β/√(n(s,a))
- **Recurrent World Models Facilitate Policy Evolution (Google Brain)**. NIPS'18

## Over-Optimistic
- Model-based Offline batch RL:
	- Learn a model penalize model uncertainty during planning;
	- Empirically very promising on D4RL tasks;
	- MOPO: T Yu, G Thomas, L Yu, S Ermon, J Zou, S Levine, C Finn, T Ma. MOPO: Model-based Offline Policy Optimization. NIPS'20
	- R Kidambi, A Rajeswaran, P Netrapalli, T Joachims. MOReL: Model-Based Offline Reinforcement Learning. NIPS'20

## Basics
- Version 0.5: collect random samples, train dynamics, plan
	- Pro: simple, no iterative procedure
	- Con: distribution mismatch problem
- Version 1.0: iteratively collect data, replan, collect data
	- Pro: simple, solves distribution mismatch
	- Con: open loop plan might perform poorly, esp. in stochastic domains
- Version 1.5: iteratively collect data using **MPC** (replan at each step)
	- Pro: robust to small model errors
	- Con: computationally expensive, but have a planning algorithm available
- Version 2.0: backpropagate directly into policy
	- Pro: computationally cheap at runtime
	- Con: can be numerically unstable, especially in stochastic domains (more on this later)
- Learn model and plan (without policy)
	- Iteratively collect more data to overcome distribution mismatch
	- Replan every time step (MPC) to mitigate small model errors
	- Learn policy
- Backpropagate into policy (e.g., PILCO) – simple but potentially unstable
	- Imitate optimal control in a constrained optimization framework (e.g., GPS)
	- Imitate optimal control via DAgger-like process (e.g., PLATO)
	- Use model-free algorithm with a model (Dyna, etc.)
- Efficiency:
	- gradient-free methods (e.g. NES, CMA, etc.)
	- fully online methods (e.g. A3C)
	- policy gradient methods (e.g. TRPO)
	- replay buffer value estimation methods (Q-learning, DDPG, NAF, SAC, etc.)
	- model-based deep RL (e.g. PETS, guided policy search)
	- model-based "shallow" RL (e.g. PILCO)
- Known dynamics (294, lec-11)\
	<img src="/RL/images/mbrl/mbrl1.png" alt="drawing" width="500"/>
- Linear case:
	- LQR: linear transition, quadratic cost\
		<img src="/RL/images/mbrl/mbrl2.png" alt="drawing" width="600"/>
	- Solved with backward recursion\
		<img src="/RL/images/mbrl/mbrl3.png" alt="drawing" width="550"/>
- Nonlinear case: DDP/iterative LQR
	- iLQR\
		<img src="/RL/images/mbrl/mbrl4.png" alt="drawing" width="550"/>
- Learn dynamics (294, lec-12)
	- Uncertainty-aware models
	- Aleatoric or statistical uncertainty
	- Epistemic or model uncertainty
	- Bayesian neural network
	- Bootstrap ensembles p(θ|D)
	- Moment matching (project to Gaussian)

## MDP/POMPD
- Stanford cs-234 (Lec-2)
- Assumption:
	- Dynamics and reward model available;
	- p(st+1|st, at) = p(st+1|ht, at)
- MDP + π(a|s) = MRP (Markov Reward Process)
	- V = R + γPV -> V = (I-γP)^-1 R
	- Bellman backup (iterative):
		- V(s;π) = Σ_a π(a|s)[r(s,a) + γΣ_s' p(s'|s,a)V(s';π)]
- Optimal: π∗(s) = argmax_π V(s;π)
	- Existance and unique;
- State-action: Q(s,a;π) = R(s,a) + γΣ_s' p(s'|s,a)V(s';π)]
	- Policy iteration (PI): iteratively do value-eval and policy improvement;
		- Policy improvement: take argmax, then follow π, always gets better;
		- π∗(s) = argmax_a Q(s,a;π)
	- Value iteration (VI):
		- V=BV, or V(s) = max_a[R(s,a)+γΣ_s' p(s'|s,a)V(s')]
- Policy evaluation:
	- MC: Gt = rt + γrt+1 + γ^2rt+2 + ... (high var, unbiased)
		- Incremental: G(s) += Gi,t, V(s;π)=G(s)/N(s)
	- TD(0): V(s) += α(r+γV(st+1)-V(st)), (low var, biased)
- Thompson Sampling for MDP:
	- Init prior p(Ras), p(T(s'|s,a))
	- Loop:
		- Sample: (s,a), T(s'|s,a), R(s,a)
		- Compute optimal Q;
		- at = argmaxQ(s,a)
		- Observe rt, st+1;
		- Update posterior p(Ras|rt), p(T|st+1) using Bayesian rule;

## Learn a Model for Data Generation
- S Gu, T Lillicrap, I Sutskever, S Levine. Continuous Deep Q-Learning with Model-based Acceleration. ICML'16
- G Kalweit, J Boedecker. Uncertainty-driven Imagination for Continuous Deep Reinforcement Learning CoRL2017.
	- Insight: model could be inaccurate!
	- Experience Replay Buffer divided into 2 categories:
		- traditional replay buffer
		- imaginary replay buffer
- **ME-TRPO**: Kurutach. Model-Ensemble Trust-Region Policy Optimization. ICLR'18

## Learn a Model for Planning
- Model for Better Value Estimation
	- **MVE**: V Feinberg, A Wan, I Stoica, M I. Jordan, J Gonzalez, S Levine. Model-Based Value Expansion for Efficient Model-Free Reinforcement Learning. ICML'18
		- Insight: approximate, few-step simulation of a reward- dense environment
		- Problem setup: continuous state and action;
		- RL: AC, on-policy; (IS not required)\
			<img src="/RL/images/mbrl/mve.png" alt="drawing" width="550"/>
	- **STEVE**: J Buckman, D Hafner, G Tucker, E Brevdo, H Lee. Sample-Efficient Reinforcement Learning with Stochastic Ensemble Value Expansion. NIPS'18
- Learn a model as context:
	- **I2A**: DeepMind. Imagination-Augmented Agents for Deep Reinforcement Learning. NIPS'17
		- Framework:\
			<img src="/RL/images/mbrl/i2a-1.png" alt="drawing" width="550"/>
			<img src="/RL/images/mbrl/i2a-2.png" alt="drawing" width="550"/>
		- Game: Sokoban;
	- **VPN**: V Feinberg, A Wan, I Stoica, M Jordan, J Gonzalez, Sergey Levine. Value Prediction Network. NIPS'17
		- https://github.com/junhyukoh/value-prediction-network
- MuZero: DeepMind. Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model. 2019
	- MuZero = VPN (learn abstract states + dynamics) + AlphaZero-planning (MCTS)

## Learn a Model
- World Model
	- **Navigation**: DeepMind. Neural Predictive Belief Representations, ICLR'19
		- 1-step frame prediction
		- Two variants of Contrastive-Predictive Coding (CPC), CPC|Action
		- DeepMind Lab\
			<img src="/RL/images/mbrl/cpc.png" alt="drawing" width="550"/>
- J. Oh, X. Guo, H. Lee, R. Lewis, and S.Singh. Action-conditional video prediction using deep networks in atari games. arxiv, 2015.
- D Ha, J Schmidhuber. Recurrent World Models Facilitate Policy Evolution， NIPS'18
	- VAE to encode frames for compression and regularization
	- RNN to Predict next step
	- Game: CarRacing, 
	- https://worldmodels.github.io \
		<img src="/RL/images/mbrl/r-world.png" alt="drawing" width="550"/>
- Ł Kaiser, M Babaeizadeh, P Miłos, B Osinski, R H Campbell, K Czechowski, D Erhan, C Finn, P Kozakowski, S Levine, R Sepassi, G Tucker, H Michalewski. Model Based Reinforcement Learning for Atari. ICLR'20
	- SimPLe\
		<img src="/RL/images/mbrl/mbrl-atari1.png" alt="drawing" width="550"/>
	- https://ai.googleblog.com/2019/03/simulated-policy-learning-in-video.html
	- Open sourced at https://github.com/tensorflow/tensor2tensor
	- Main loop:
		- The agent starts interacting with the real environment.
		- The collected observations are used to update the current world model.
		- The agent updates the policy by learning inside the world model.
	- World model: feed-forward CNN
		- Input 4 frames
		- Output: predicts next frame (256 softmax)
		- Output: Reward\
			<img src="/RL/images/mbrl/mbrl-atari2.png" alt="drawing" width="550"/>
	- RL: PPO
	- Experiment: 100k interactions;

## Continuous (MuJoCo, Robotics)
- Gaussian-Process Model (non-parametric):
	- C. E. Rasmussen and M. Kuss. Gaussian processes in reinforcement learning. NIPS'03
	- J Kocijan, R Murray-Smith, C Rasmussen, and A Girard. Gaussian process model based predictive control. ACC'04
	- . Ko, D Klein, D Fox, and D Haehnel. Gaussian processes and reinforcement learning for identification and control of an autonomous blimp. ICRA'07
	- D. Nguyen-Tuong, J. Peters, and M. Seeger. Local Gaussian process regression for real time online model learning. NIPS'08
	- A. Grancharova, J. Kocijan, and T. A. Johansen. Explicit stochastic predictive control of combustion plants based on Gaussian process models. Automatica'08
	- M Deisenroth, C Rasmussen, D Fox. Learning to Control a Low-Cost Manipulator using Data-Efficient Reinforcement Learning. RSS'11
		- Gaussian Process to learn the dynamics
	- M. Deisenroth, D. Fox, and C. Rasmussen. Gaussian processes for data-efficient learning in robotics and control. PAMI'14
	- S. Kamthe and M. P. Deisenroth. Data-efficient reinforcement learning with probabilistic model predictive control. AISTATS'18
- Bayesian Model:
	- E. Hernandaz and Y. Arkun. Neural network modeling and an extended DMC algorithm to control nonlinear systems. ACC'90
	- W. T. Miller, R. P. Hewes, F. H. Glanz, and L. G. Kraft. Real-time dynamic control of an industrial manipulator using a neural network-based learning controller. 1990
	- L.-J. Lin. Reinforcement Learning for Robots Using Neural Networks. 1992
	- A. Draeger, S. Engell, and H. Ranke. Model predictive control using neural networks. 1995
- Local NN (time-varying) Model:
	- Guided policy search (model-based RL) for image-based robotic manipulation
		- https://github.com/cbfinn/gps
	- S. Levine, C. Finn, T. Darrell, and P. Abbeel. End-to-end training of deep visuomotor policies. JMLR'16
	- C. Finn, X. Tan, Y. Duan, T. Darrell, S. Levine, and P. Abbeel. Deep spatial autoencoders for visuomotor learning. ICRA'16
	- Y. Chebotar, K. Hausman, M. Zhang, G. Sukhatme, S. Schaal, and S. Levine. Combining model-based and model-free updates for trajectory-centric reinforcement learning. ICML'17
- NN Model:
	- I. Lenz, R. Knepper, and A. Saxena. DeepMPC: Learning deep latent features for model predictive control. RSS'15
	- A. Punjani and P. Abbeel. Deep learning helicopter dynamics models. ICRA'15
	- J. Fu, S. Levine, and P. Abbeel. One-shot learning of manipulation skills with online dynamics adaptation and neural network priors. IROS'16
	- A. Baranes and P.-Y. Oudeyer. Active learning of inverse models with intrinsically motivated goal exploration in robots. 2016
	- I. Mordatch, N. Mishra, C. Eppner, and P. Abbeel. Combining model-based policy search with online model learning for control of physical humanoids. ICRA'16
	- S Depeweg, J. M. Hernández-Lobato, F. Doshi-Velez, and S. Udluft. Learning and policy search in stochastic dynamical systems with Bayesian neural networks. 2016
	- Y. Gal, R. McAllister, and C. Rasmussen. Improving PILCO with Bayesian neural network dynamics models. ICMLW'16
	- P. Agrawal, A. V. Nair, P. Abbeel, J. Malik, and S. Levine. Learning to poke by poking: Experiential learning of intuitive physics. NIPS'16
	- G. Williams, N. Wagener, B. Goldfain, P. Drews, J. M. Rehg, B. Boots, and E. A. Theodorou. Information theoretic MPC for model-based reinforcement learning. ICRA'17
	- A Nagabandi, G Kahn, R S. Fearing, S Levine. Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning. ICLR'18
		- At beginning: avoid overfitting (MBRL is better)
		- Later: avoid underfitting (MF-RL is better)
		- Mb-Mf best
- Bayesian-NN, Uncertainty-Aware:
	- Y. Gal, J. Hron, and A. Kendall. Concrete dropout. NIPS'16
	- I. Osband. Risk versus uncertainty in deep learning: Bayes, bootstrap and the dangers of dropout. NIPSW'16
	- I. Osband, C. Blundell, A. Pritzel, and B. Van Roy. Deep exploration via bootstrapped DQN. NIPS'16
	- C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger. On calibration of modern neural networks. ICML'17
- **MBMF**: S Bansal, R Calandra, K Chua, S Levine, C Tomlin. MBMF: Model-Based Priors for Model-Free Reinforcement Learning. NIPS'17
	- Learn a probabilistic dynamics model and leveraging it as a prior for the intertwined model-free optimization;\
		<img src="/RL/images/mbrl/mbmf.png" alt="drawing" width="550"/>
- **PETS**: K Chua, R Calandra, R McAllister, S Levine. Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models. NIPS'18
	- **SOA**!
	- https://github.com/kchua/handful-of-trials \
		<img src="/RL/images/mbrl/pets.png" alt="drawing" width="550"/>
- **MB-MPO**: Clavera. Model-Based Reinforcement Learning via Meta-Policy Optimization. 2018
- **SOLAR**: M Zhang, S Vikram, L Smith, P Abbeel, M Johnson, S Levine. SOLAR: Deep Structured Representations for Model-Based Reinforcement Learning. ICML'19
- **MBPO**: M Janner, J Fu, M Zhang, S Levine. When to Trust Your Model: Model-Based Policy Optimization. NeurIPS'19
	- https://zhuanlan.zhihu.com/p/105645139

## Legacy
- **PILCO**: M P Deisenroth, C E Rasmussen. PILCO: A Model-Based and Data-Efficient Approach to Policy Search. ICML'11
- **DDP**: Mayne, Jacobson. Differential dynamic programming. 1970
- **iLQR**: Tassa, Erez, Todorov.  Synthesis and Stabilization of Complex Behaviors through Online Trajectory Optimization. 2012
