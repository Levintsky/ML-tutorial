# Control and Planning

## Sergey Levine
- MCTS (lec-10)
- Control as an Inference (lec-15)

## Monte-Carlo Tree Search
- Approach\
	<img src="/RL/images/mcts/mcts.png" alt="drawing" width="400"/>
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
- Backward message: beta(st, at) = p(Ot:T) given (st, at). i.e., given what will happen after t, what is the optimality if we should take (st at).\
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
	- H Kappen, V Gomez, M Opper. Optimal control as a graphical model inference problem: frames control as an inference problem in a graphical model. AAAI'13
	- Ziebart. (2010). Modeling interaction via the principle of maximal causal entropy: connection between soft optimality and maximum entropy modeling.
	- Rawlik, Toussaint, Vijaykumar. (2013). On stochastic optimal control and reinforcement learning by approximate inference: temporal difference style algorithm with soft optimality.
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

## Applications
- Data center cooling using model-predictive control. NIPS'18 Tutorial

