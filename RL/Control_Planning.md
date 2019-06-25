# Control and Planning

## Sergey Levine
- MCTS (lec-10)
- Control as an Inference (lec-15)

## Monte-Carlo Tree Search
- Approach
<img src="/RL/images/mcts.png" alt="drawing" width="500"/>

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
- A graphical model
<img src="/RL/images/control-infer1.png" alt="drawing" width="500"/>

- Backward message: beta(st, at) = p(Ot:T) given (st, at). i.e., given what will happen after t, what is the optimality if we should take (st at).
<img src="/RL/images/control-infer2.png" alt="drawing" width="600"/>
<img src="/RL/images/control-infer3.png" alt="drawing" width="600"/>
<img src="/RL/images/control-infer4.png" alt="drawing" width="600"/>

- Forward message: alpha(st) = p(st) given O1:t-1
<img src="/RL/images/control-infer5.png" alt="drawing" width="600"/>
<img src="/RL/images/control-infer6.png" alt="drawing" width="600"/>

- Q-learning with soft optimality
<img src="/RL/images/soft-q.png" alt="drawing" width="600"/>

- Policy gradient with soft optimality
<img src="/RL/images/soft-pg.png" alt="drawing" width="600"/>

- Graphical models:
	- Kappen. (2009). Optimal control as a graphical model inference problem: frames control as an inference problem in a graphical model.
	- Ziebart. (2010). Modeling interaction via the principle of maximal causal entropy: connection between soft optimality and maximum entropy modeling.
	- Rawlik, Toussaint, Vijaykumar. (2013). On stochastic optimal control and reinforcement learning by approximate inference: temporal difference style algorithm with soft optimality.
- Modern soft optimality
	- Haarnoja, Tang, Abbeel, L., Reinforcement Learning with Deep Energy-Based Policies. ICML'17
	- Nachum, Norouzi, Xu, Schuurmans. (2017). Bridging the gap between value and policy based reinforcement learning.
	- Schulman, Abbeel, Chen. (2017). Equivalence between policy gradients and soft Q-learning.
 	- Haarnoja, Zhou, Abbeel, L. (2018). Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor.
	- Levine. (2018). Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review

## SOA
- Memory-based control with recurrent neural networks
- Model-Free Episodic Control
- TREEQN AND ATREEC: DIFFERENTIABLE TREE PLANNING FOR DEEP REINFORCEMENT LEARNING
- A Controller-Recognizer Framework: How necessary is recognition for control?
- Combining Model-Based and Model-Free Updates for Trajectory-Centric Reinforcement Learning

## Planning
- The Predictron: End-To-End Learning and Planning, ICML 2017

## Physics
- Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics

## Theory
- On the Sample Complexity of the Linear Quadratic Regulator

## Legacy
- Proto-value Functions: A Laplacian Framework for Learning Representation and Control in Markov Decision Processes, 2007
