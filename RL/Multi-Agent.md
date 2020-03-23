# Multi-Agent

## OpenAI
- **Particle-World**: Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments, 2018
	- **MADDPG**
	- https://github.com/openai/multiagent-particle-envs
	- Discrete case:\
		<img src = '/RL/images/multi-agent/maddpg1.png' width = '600'>
	- Continuous case:\
		<img src = '/RL/images/multi-agent/maddpg2.png' width = '600'>
- S Liu, G Lever, N Heess, J Merel, S Tunyasuvunakool, and T Graepel. Emergent coordination through competition. ICLR'19
- B Baker, I Kanitscheider, T Markov, Y Wu, G Powell, B McGrew, I Mordatch.Emergent Tool Use From Multi-Agent Autocurricula. 2019
	- http://openai.com/blog/emergent-tool-use
	- http://github.com/openai/multi-agent-emergence-environments
	- Key insight: six emergent phases in agent strategy in our environment, each of which creates a new pressure for the opposing team to adapt
	- Policy: PPO + GAE;
	- Platform: rapid;
	- Entity centric and attention based to capture object-level info;
	- Net structure: CNN-RNN;\
		<img src="/RL/images/multi-agent/hide-seek.png" alt="drawing" width="500"/>
- Joseph Suarez, Yilun Du, Phillip Isola, Igor Mordatch. Neural MMO: A Massively Multiagent Game Environment for Training and Evaluating Intelligent Agents. ICLR 2019 reject

## DeepMind
- M Jaderberg, W Czarnecki, I Dunning, L Marris, G Lever, A G Castañeda, C Beattie, N C. Rabinowitz, Ari S. Morcos, A Ruderman, N Sonnerat, T Green, L Deason, Joel Z. Leibo, D Silver, D Hassabis, K Kavukcuoglu, T Graepel. Human-level performance in 3D multiplayer games with population-based reinforcement learning. Science'19
	- For The Win (FTW): CNN from pixels;\
		<img src="/RL/images/multi-agent/ftw.jpg" alt="drawing" width="500"/>
		<img src="/RL/images/multi-agent/ftw2.jpg" alt="drawing" width="500"/>

## Unclassified
- A multi-agent reinforcement learning model of common-pool resource appropriation
- S. Omidshafiei, J. Pazis, C. Amato, J. P. How, and J. Vian. Deep decentralized multi-task multi-agent reinforcement learning under partial observability. CoRR 2017
- J. K. Gupta, M. Egorov, and M. Kochenderfer. Cooperative multi-agent control using deep reinforcement learning. 2017.
- Actor-Critic Policy Optimization in Partially Observable Multiagent Environments. NIPS'18
- Credit Assignment For Collective Multiagent RL With Global Rewards. NIPS'18
- Multi-Agent Reinforcement Learning via Double Averaging Primal-Dual Optimization. NIPS'18
- Learning Others' Intentional Models in Multi-Agent Settings Using Interactive POMDPs. NIPS'18

## Legacy
- M. Lauer and M. Riedmiller. An algorithm for distributed reinforcement learning in cooperative multi-agent systems. ICML'00
- L. Matignon, G. J. Laurent, and N. Le Fort-Piat. Hysteretic q-learning: an algorithm for decentralized reinforcement learning in cooperative multi-agent teams. IROS'07
- L. Busoniu, R. Babuska, and B. De Schutter. A comprehensive survey of multiagent reinforce- ment learning. 2008
- L. Panait and S. Luke. Cooperative multi-agent learning: The state of the art. AAMAS'05

## NIPS'19
- Nicolas Carion, Nicolas Usunier, Gabriel Synnaeve, Alessandro Lazaric. A Structured Prediction Approach for Generalization in Cooperative Multi-Agent Reinforcement Learning
- Sai Qian Zhang, Qi Zhang, Jieyu Lin. Efficient Communication in Multi-Agent Reinforcement Learning via Variance Based Control
- Xin Guo, Anran Hu, Renyuan Xu, Junzi Zhang. Learning Mean-Field Games
- Deepak Pathak, Christopher Lu, Trevor Darrell, Phillip Isola, Alexei Efros. Learning to Control Self-Assembling Morphologies: A Study of Generalization via Modularity
- Yali Du, Lei Han, Meng Fang, Ji Liu, Tianhong Dai, Dacheng Tao. LIIR: Learning Individual Intrinsic Reward in Multi-Agent Reinforcement Learning
- Micah Carroll, Rohin Shah, Mark Ho, Tom Griffiths, Sanjit Seshia, Pieter Abbeel, Anca Dragan. On the Utility of Learning about Humans for Human-AI Coordination
- Chao Qu, Shie Mannor, Huan Xu, Yuan Qi, Le Song, Junwu Xiong. Value Propagation for Decentralized Networked Deep Multi-agent Reinforcement Learning
- Tom Eccles, Yoram Bachrach, Guy Lever, Angeliki Lazaridou, Thore Graepel. Biases for Emergent Communication in Multi-agent Reinforcement Learning
- Fushan Li, Michael Bowling. Ease-of-Teaching and Language Structure from Emergent Communication
- Jack Serrino, Max Kleiman-Weiner, David Parkes, Josh Tenenbaum. Finding Friend and Foe in Multi-Agent Games
- Jiechuan Jiang, Zongqing Lu. Learning Fairness in Multi-Agent Systems
- Anuj Mahajan, Tabish Rashid, Mikayel Samvelyan, Shimon Whiteson. MAVEN: Multi-Agent Variational Exploration
- Shuyue Hu, Chin-wing Leung, Ho-fung Leung. Modelling the Dynamics of Multiagent Q-Learning in Repeated Symmetric Games: a Mean Field Theoretic Approach
- Christian Schroeder de Witt, Jakob Foerster, Gregory Farquhar, Philip Torr, Wendelin Boehmer, Shimon Whiteson. Multi-Agent Common Knowledge Reinforcement Learning
