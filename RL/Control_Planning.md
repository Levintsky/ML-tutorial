# Optimal Control and Planning

## Basics
- Discrete MCTS (EECS-294, lec-10)
	- UCT
- Linear case: LQR
	- Linear known dynamics, quadratic cost function;
	- DDP backward;
	- iLQR: locally approximate via Taylor expansion;
- Control as an Inference (lec-15)

## Monte-Carlo Tree Search
- Approach:
	- Find a leaf sl using TreePolicy(s1)
	- Evaluate the leaf using DefaultPolicy(sl)
	- Update all values in tree between s1 and sl, take best action from s1;
	- UCT: Score(st) = Q(st)/N(st) + 2C sqrt(2lnN(st-1)/N(st))
- Legacy
	- C. Browne, E. Powley, D. Whitehouse, S. Lucas, P. I. Cowling, P. Rohlfshagen, D. P. Stephen Tavener, S. Samothrakis, and S. Colton. A survey of monte carlo tree search methods. IEEE Transactions on Computational Intelligence and AI in Games, 2012
	- S. Gelly and D. Silver. Combining online and offline knowledge in uct. ICML, 2007.
	- L. Kocsis and C. Szepesvàri. Bandit based monte-carlo planning. ECML, 2006.
	- Rémi Coulom. Efficient selectivity and backup operators in monte-carlo tree search. In International conference on computers and games, pages 72–83. Springer, 2006.
	- G. Tesauro and G. R. Galperin. On-line policy improvement using monte-carlo search. NIPS'96.
- New, SOA
	- X. Guo, S. Singh, H. Lee, R. Lewis, and X. Wang. Deep learning for real-time atari game play using offline monte-carlo tree search planning. NIPS'14
		- Imitation learning from MCTS
	- Thomas Anthony, Zheng Tian, and David Barber. Thinking fast and slow with deep learning and tree search, 2017.

## Control as Inference
- A graphical model\
	<img src="/RL/images/control/control-infer1.png" alt="drawing" width="500"/>
- Forward message: p(st\|O 1:t-1)
	- Given optimality before, where I am in state space;
- Backward message:
	- soft Q(s, a) or beta(st, at) = p(Ot:T\|st, at).
	- soft V(s) or beta(st): marginalize at with some p(at\|st) action prior;
	- Then Q(st, at) = r(st, at) + log E_st+1(exp(V(st+1)))
	- Given what will happen after t, what is the optimality if we should take (st at).\
	<img src="/RL/images/control/control-infer2.png" alt="drawing" width="600"/>
	<img src="/RL/images/control/control-infer3.png" alt="drawing" width="600"/>
	<img src="/RL/images/control/control-infer4.png" alt="drawing" width="600"/>
- Forward message: alpha(st) = p(st) given O1:t-1\
	<img src="/RL/images/control/control-infer5.png" alt="drawing" width="600"/>
	<img src="/RL/images/control/control-infer6.png" alt="drawing" width="600"/>
- Q-learning with soft optimality\
	<img src="/RL/images/control/soft-q.png" alt="drawing" width="600"/>
- Policy gradient with soft optimality\
	<img src="/RL/images/control/soft-pg.png" alt="drawing" width="600"/>
- Graphical models:
	- Ziebart. (2010). Modeling interaction via the principle of maximal causal entropy: connection between soft optimality and maximum entropy modeling.
	- H Kappen, V Gomez, M Opper. Optimal control as a graphical model inference problem: frames control as an inference problem in a graphical model. AAAI'13
	- Rawlik, Toussaint, Vijaykumar. On stochastic optimal control and reinforcement learning by approximate inference: temporal difference style algorithm with soft optimality. RSS'12
- Modern soft optimality
	- Haarnoja, Tang, Abbeel, L., Reinforcement Learning with Deep Energy-Based Policies. ICML'17
	- Nachum, Norouzi, Xu, Schuurmans. (2017). Bridging the gap between value and policy based reinforcement learning.
	- Schulman, Abbeel, Chen. (2017). Equivalence between policy gradients and soft Q-learning.
 	- Haarnoja, Zhou, Abbeel, L. (2018). Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor.
	- Levine. (2018). Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review

## Legacy
- Proto-value Functions: A Laplacian Framework for Learning Representation and Control in Markov Decision Processes, 2007

## Unclassified
- N Heess, J J Hunt, T P Lillicrap, D Silver. Memory-based control with recurrent neural networks. NIPS'15
- C Blundell, B Uria, A Pritzel, Y Li, A Ruderman, J Z Leibo, J Rae, D Wierstra, D Hassabis. Model-Free Episodic Control
- G Farquhar, T Rocktäschel, M Igl, Sh Whiteson. TreeQN and ATreeC: Differentiable Tree-Structured Models for Deep Reinforcement Learning. ICLR'18
- M Moczulski, K Xu, A Courville, K Cho. A Controller-Recognizer Framework: How necessary is recognition for control? ICML'16
- Y Chebotar, K Hausman, M Zhang, G Sukhatme, S Schaal, S Levine. Combining Model-Based and Model-Free Updates for Trajectory-Centric Reinforcement Learning. ICML'17
- D Silver, H v Hasselt, M Hessel, T Schaul, A Guez, T Harley, G Dulac-Arnold, D Reichert, N Rabinowitz, A Barreto, T Degris. The Predictron: End-To-End Learning and Planning, ICML'17
- **OptNet**: B Amos and Z Kolter. OptNet: Differentiable Optimization as a Layer in Neural Networks. ICML'17
- **MPC**: B Amos, I Rodriguez, J Sacks, B Boots, Z Kolter. Differentiable MPC for End-to-end Planning and Control. 2019
	- https://locuslab.github.io/mpc.pytorch/
- Pieter Abbeel. Learning Plannable Representations with Causal InfoGAN. NIPS'18
- Berkeley. Variational Inverse Control with Events: A General Framework for Data-Driven Reward Definition. NIPS'18

## Theory
- On the Sample Complexity of the Linear Quadratic Regulator

## NIPS'19
- Shangtong Zhang, Wendelin Boehmer, Shimon Whiteson. Generalized Off-Policy Actor-Critic
- Sebastian Tschiatschek, Ahana Ghosh, Luis Haug, Rati Devidze, Adish Singla. Learner-aware Teaching: Inverse Reinforcement Learning with Preferences and Constraints
- Naman Agarwal, Elad Hazan, Karan Singh. Logarithmic Regret for Online Control
- Xingyu Lin, Harjatin Baweja, George Kantor, David Held. Adaptive Auxiliary Task Weighting for Reinforcement Learning
- Pim de Haan, Dinesh Jayaraman, Sergey Levine. Causal Confusion in Imitation Learning
- Hengyuan Hu, Denis Yarats, Qucheng Gong, Yuandong Tian, Mike Lewis. Hierarchical Decision Making by Generating and Following Natural Language Instructions
- Xiangyuan Zhang, Kaiqing Zhang, Erik Miehling, Tamer Basar. Non-Cooperative Inverse Reinforcement Learning
- Jack Umenberger, Mina Ferizbegovic, Thomas Schön, Håkan Hjalmarsson. Robust exploration in linear quadratic reinforcement learning
- Francisco Garcia, Philip Thomas. A Meta-MDP Approach to Exploration for Lifelong Reinforcement Learning
- Andrea Zanette, Alessandro Lazaric, Mykel J Kochenderfer, Emma Brunskill. Limiting Extrapolation in Linear Approximate Value Iteration
- Alberto Maria Metelli, Amarildo Likmeta, Marcello Restelli. Propagating Uncertainty in Reinforcement Learning via Wasserstein Barycenters
- Yu Bai, Tengyang Xie, Nan Jiang, Yu-Xiang Wang. Provably Efficient Q-Learning with Low Switching Cost
- Ronald Ortner, Matteo Pirotta, Alessandro Lazaric, Ronan Fruit, Odalric-Ambrym Maillard. Regret Bounds for Learning State Representations in Reinforcement Learning
- Matteo Turchetta, Felix Berkenkamp, Andreas Krause. Safe Exploration for Interactive Machine Learning
- David Janz, Jiri Hron, Przemysław Mazur, Katja Hofmann, José Miguel Hernández-Lobato, Sebastian Tschiatschek. Successor Uncertainties: Exploration and Uncertainty in Temporal Difference Learning
- Andrea Zanette, Mykel J Kochenderfer, Emma Brunskill. Almost Horizon-Free Structure-Aware Best Policy Identification with a Generative Model
- Kamil Ciosek, Quan Vuong, Robert Loftin, Katja Hofmann. Better Exploration with Optimistic Actor Critic
- Simon Du, Yuping Luo, Ruosong Wang, Hanrui Zhang. Provably Efficient Q-learning with Function Approximation via Distribution Shift Error Checking Oracle
- Liangpeng Zhang, Ke Tang, Xin Yao. Explicit Planning for Efficient Exploration in Reinforcement Learning
- Jian QIAN, Ronan Fruit, Matteo Pirotta, Alessandro Lazaric. Exploration Bonus for Regret Minimization in Discrete and Continuous Average Reward MDPs
- Xiuyuan Lu, Benjamin Van Roy. Information-Theoretic Confidence Bounds for Reinforcement Learning
