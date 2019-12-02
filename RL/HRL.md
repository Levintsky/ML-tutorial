# Hierarchical RL, Options

## HRL
- A summary: https://thegradient.pub/the-promise-of-hierarchical-reinforcement-learning/
- **FUN**: A S Vezhnevets, S Osindero, T Schaul, N Heess, M Jaderberg, D Silver, K Kavukcuoglu. Feudal Network for Hierarchical Reinforcement Learning. ICML'17
	- https://github.com/dmakian/feudal_networks
	<img src="/RL/images/hrl/fun.png" alt="drawing" width="500"/>
- A Deep Hierarchical Approach to Lifelong Learning in Minecraft, AAAI'17
- T Shu, C Xiong, R Socher. Hierarchical and Interpretable Skill Acquisition in Multi-task Reinforcement Learning. ICLR'18
- Tejas D Kulkarni, Karthik R Narasimhan, Ardavan Saeedi, and Joshua B Tenenbaum. Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation. NIPS'16
- **STRAW**: Alexander Vezhnevets, Volodymyr Mnih, John Agapiou, Simon Osindero, A Graves, O Vinyals, K Kavukcuoglu. Strategic Attentive Writer for Learning Macro-Actions. 2016
- S Zheng, Y Yue and P Lucey. Generating long-term trajectories using deep hierarchical networks. NIPS'16.
	- Long-term planning;
- Kulkarni, Tejas D, Narasimhan, Karthik, Saeedi, Ardavan, and Tenenbaum, Josh. Hierarchical deep reinforcement learning: Integrating temporal abstraction and intrinsic motivation. NIPS'16
- E Zhan, Stephan Zheng, Generative Multi-Agent Behavioral Cloning
- K Frans, J Ho, X Chen, P Abbeel, J Schulman. Meta Learning Shared Hierarchies. ICLR'18
- Ofir Nachum, Shixiang Gu, Honglak Lee, Sergey Levine. Data-Efficient Hierarchical Reinforcement Learning. NIPS'18
- Andrew Levy, George Konidaris, Robert Platt, Kate Saenko. Learning Multi-Level Hierarchies with Hindsight. ICLR'19
- Zhen-Jia Pang, Ruo-Ze Liu, Zhou-Yu Meng, Yi Zhang, Yang Yu, Tong Lu. On Reinforcement Learning for Full-length Game of StarCraft. 2019
- **MPH**: Alexander Pashevich, Danijar Hafner, James Davidson, Rahul Sukthankar, Cordelia Schmid. Modulated Policy Hierarchies. 2019

## Options
- Daniel J Mankowitz, Timothy A Mann, and Shie Mannor. Time-regularized interrupting options. ICML'14
- Pierre-Luc Bacon and Doina Precup. The option-critic architecture. NIPSW'15
- **VIC**: Karol Gregor, Danilo Rezende and Daan Wierstra. Variational Intrinsic Control. ICLR'17
	- Unsupervised RL, discover set of intrinsic options
	- Maximizing the number of different states an agent can reliably reach
	- Notation: option Omega, then associated policy pi(a|s,Omega) follows the option;
	- Different option should result in different result, if for two options Ω1 and Ω2, upon reaching state sf1 , we can infer it was option Ω1 that was executed rather than Ω 2 , and when reaching a state sf2 we can infer it was option Ω2 rather than Ω1 , then Ω 1 and Ω 2 can be said to be intrinsically different options:\
		<img src="/RL/images/hrl/vic1.png" alt="drawing" width="500"/>
	- p(sf|s0,Ω) is inherent to the environment, but obtaining Bayes' reverse p(Ω|s0,sf) is difficult. I-VB for approximate:\
		<img src="/RL/images/hrl/vic2.png" alt="drawing" width="500"/>
	- Put together to learn options Omega:
		<img src="/RL/images/hrl/vic3.png" alt="drawing" width="400"/>
	- Instrinsic control with implicit options (action as options):
		<img src="/RL/images/hrl/vic4.png" alt="drawing" width="400"/>
	- Experiments: grid world;
- The Option-Critic Architecture, AAAI 2017
- Marlos C. Machado, Clemens Rosenbaum, Xiaoxiao Guo, Miao Liu, Gerald Tesauro, Murray Campbell. Eigenoption Discovery through the Deep Successor Representation, ICLR'18

## Legacy
- P Dayan, Peter and G Hinton. Feudal reinforcement learning. NIPS'93.
- R Sutton, D Precup, and S Singh. Between mdps and semi-mdps: A framework for temporal abstraction in reinforcement learning. AI'99
- Hierarchical Learning in Stochastic Domains: Preliminary Results
- Amy McGovern and Andrew G Barto. Automatic discovery of subgoals in reinforcement learning
using diverse density. 2001.
- Martin Stolle and Doina Precup. Learning options in reinforcement learning. In International
Symposium on Abstraction, Reformulation, and Approximation, pp. 212–223. Springer, 2002.
- A Tutorial on Bayesian Optimization of Expensive Cost Functions, with Application to Active User Modeling and Hierarchical Reinforcement Learning 2010
- David Silver and Kamil Ciosek. Compositional planning using optimal option models.