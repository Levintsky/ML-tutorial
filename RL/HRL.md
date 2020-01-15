# Hierarchical RL, Options

## From Spinningup
- STRAW, FUN, HIRO;

## HRL
- A summary: https://thegradient.pub/the-promise-of-hierarchical-reinforcement-learning/
- A Deep Hierarchical Approach to Lifelong Learning in Minecraft, AAAI'17
- T Shu, C Xiong, R Socher. Hierarchical and Interpretable Skill Acquisition in Multi-task Reinforcement Learning. ICLR'18
- Tejas D Kulkarni, Karthik R Narasimhan, Ardavan Saeedi, and Joshua B Tenenbaum. Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation. NIPS'16
- S Zheng, Y Yue and P Lucey. Generating long-term trajectories using deep hierarchical networks. NIPS'16.
	- Long-term planning;
- Kulkarni, Tejas D, Narasimhan, Karthik, Saeedi, Ardavan, and Tenenbaum, Josh. Hierarchical deep reinforcement learning: Integrating temporal abstraction and intrinsic motivation. NIPS'16
- E Zhan, Stephan Zheng, Generative Multi-Agent Behavioral Cloning
- **HIRO**: Ofir Nachum, Shixiang Gu, Honglak Lee, Sergey Levine. Data-Efficient Hierarchical Reinforcement Learning. NIPS'18
- Honglak Lee. Hierarchical Reinforcement Learning for Zero-shot Generalization with Subtask Dependencies. NIPS'18
- Andrew Levy, George Konidaris, Robert Platt, Kate Saenko. Learning Multi-Level Hierarchies with Hindsight. ICLR'19
- Zhen-Jia Pang, Ruo-Ze Liu, Zhou-Yu Meng, Yi Zhang, Yang Yu, Tong Lu. On Reinforcement Learning for Full-length Game of StarCraft. 2019
- **MPH**: Alexander Pashevich, Danijar Hafner, James Davidson, Rahul Sukthankar, Cordelia Schmid. Modulated Policy Hierarchies. 2019

## Joint Skills and Meta-Controller
- P Dayan, Peter and G Hinton. Feudal reinforcement learning. NIPS'93.
- Pierre-Luc Bacon and Doina Precup. The option-critic architecture. NIPSW'15
- Pierre-Luc Bacon, Jean Harb, and Doina Precup. The Option-Critic Architecture, AAAI 2017
- Nicolas Heess, Greg Wayne, Yuval Tassa, Timothy Lillicrap, Martin Riedmiller, and David Silver. Learning and transfer of modulated locomotor controllers. 2016
- **STRAW**: Alexander Vezhnevets, Volodymyr Mnih, John Agapiou, Simon Osindero, A Graves, O Vinyals, K Kavukcuoglu. Strategic Attentive Writer for Learning Macro-Actions. NIPS'16
	- Stick to the plan (commit)\
		<img src="/RL/images/hrl/straw1.png" alt="drawing" width="500"/>
	- Attention model:\
		<img src="/RL/images/hrl/straw2.png" alt="drawing" width="500"/>
	- Algorithm:\
		<img src="/RL/images/hrl/straw3.png" alt="drawing" width="400"/>
	- Experiments: 2D-maze; Atari;
- **FUN**: A S Vezhnevets, S Osindero, T Schaul, N Heess, M Jaderberg, D Silver, K Kavukcuoglu. Feudal Network for Hierarchical Reinforcement Learning. ICML'17
	- https://github.com/dmakian/feudal_networks
	<img src="/RL/images/hrl/fun.png" alt="drawing" width="500"/>
- Sanjay Krishnan, Roy Fox, Ion Stoica, and Ken Goldberg. Ddco: Discovery of deep continuous options for robot learning from demonstrations. ICLR'17
- Carlos Florensa, Yan Duan, and Pieter Abbeel. Stochastic neural networks for hierarchical reinforcement learning. 2017
- K Frans, J Ho, X Chen, P Abbeel, J Schulman. Meta Learning Shared Hierarchies. ICLR'18
- Main problem:
	- the meta-policy does not select "bad" options, so these options do not receive any reward signal to improve.
	- Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. 2017

## Options
- Daniel J Mankowitz, Timothy A Mann, and Shie Mannor. Time-regularized interrupting options. ICML'14
- Marlos C. Machado, Clemens Rosenbaum, Xiaoxiao Guo, Miao Liu, Gerald Tesauro, Murray Campbell. Eigenoption Discovery through the Deep Successor Representation, ICLR'18

## Legacy
- Hierarchical Learning in Stochastic Domains: Preliminary Results
- Amy McGovern and Andrew G Barto. Automatic discovery of subgoals in reinforcement learning
using diverse density. 2001.
- Martin Stolle and Doina Precup. Learning options in reinforcement learning. In International Symposium on Abstraction, Reformulation, and Approximation, pp. 212–223. Springer, 2002.
- A Tutorial on Bayesian Optimization of Expensive Cost Functions, with Application to Active User Modeling and Hierarchical Reinforcement Learning 2010
- David Silver and Kamil Ciosek. Compositional planning using optimal option models.