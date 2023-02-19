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
- J Suarez, Y Du, P Isola, I Mordatch. Neural MMO: A Massively Multiagent Game Environment for Training and Evaluating Intelligent Agents. ICLR 2019 reject

## DeepMind
- DeepMind. Human-level performance in 3D multiplayer games with population-based reinforcement learning. Science'19
	- For The Win (FTW): CNN from pixels;\
		<img src="/RL/images/multi-agent/ftw.jpg" alt="drawing" width="500"/>
		<img src="/RL/images/multi-agent/ftw2.jpg" alt="drawing" width="500"/>

## Legacy
- M. Lauer and M. Riedmiller. An algorithm for distributed reinforcement learning in cooperative multi-agent systems. ICML'00
- L. Matignon, G. J. Laurent, and N. Le Fort-Piat. Hysteretic q-learning: an algorithm for decentralized reinforcement learning in cooperative multi-agent teams. IROS'07
- L. Busoniu, R. Babuska, and B. De Schutter. A comprehensive survey of multiagent reinforcement learning. 2008
- L. Panait and S. Luke. Cooperative multi-agent learning: The state of the art. AAMAS'05
