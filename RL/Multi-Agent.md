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