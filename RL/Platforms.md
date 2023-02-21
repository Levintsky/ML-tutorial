# Platforms

## Game-Engine
- Atari (rts):
	- **ALE**: Bellemare, M. G.; Naddaf, Y.; Veness, J.; and Bowling, M. The arcade learning environment: An evaluation platform for general agents. JAIR'13'
	- ELF: https://github.com/pytorch/ELF
- Navigation with auxiliary (e.g. shooting, QA, ...)
	- **VizDoom**: ViZDoom: A Doom-based AI research platform for visual reinforcement learning. CIG'16
		- Poland Team.
	- DeepMind-Lab
		- 3D, first-person
		- Built on Quake III arena (1999)
		- Agent receives RGB(D) and reward, as well as velocity
		- Action: jump, crouch, 8 directions (left, right, 45deg, ...)
	- House3D: https://github.com/facebookresearch/House3D
	- **Malmo**: Johnson M., Hofmann K., Hutton T., Bignell D. The Malmo Platform for Artificial Intelligence Experimentation. IJCAI'16
- General:
	- Open-AI gym: https://github.com/openai/gym
	- Retro Contest: A Nichol, V Pfau, C Hesse, O Klimov, J Schulman. Gotta Learn Fast: A New Benchmark for Generalization in RL. 2018
		- https://contest.openai.com/2018-1/
		- https://github.com/openai/retro#gym-retro
		- Classic video games to gym environment
	- **Retro**: N Bhonker, S Rozenberg and I Hubara. Playing SNES in the Retro Learning Environment. ICLR'17
- Robotics:
	- Robo-School: https://github.com/openai/roboschool
	- Mujoco: https://github.com/openai/mujoco-py

## Distributed RL Platforms
- From Spinningup
	- A Stooke, P Abbeel. Accelerated Methods for Deep Reinforcement Learning. 2018.
		- Contribution: Systematic analysis of parallelization in deep RL across algorithms.
		- https://github.com/astooke/accel_rl
	- IMPALA, Ape-X, R2D2, RLlib;
- A summary:\
	<img src="/RL/images/dist/dist-rl-history.png" alt="drawing" width="600"/>
- 2013/2015: DQN\
	<img src="/RL/images/dist/dist-rl-dqn.png" alt="drawing" width="600"/>
- **Gorila**: DeepMind. Massively parallel methods for deep reinforcement learning view publication. ICML, 2015.\
	<img src="/RL/images/dist/dist-rl-gorila.png" alt="drawing" width="600"/>
- **A3C**: DeepMind. Asynchronous methods for deep reinforcement learning. ICML'16\
	<img src="/RL/images/dist/a3c.png" alt="drawing" width="600"/>
- **Ape-X**: DeepMind. Distributed Prioritized Experience Replay. ICLR'18\
	<img src="/RL/images/dist/dist-rl-ape-x.png" alt="drawing" width="600"/>
- **AlphaZero**\
	<img src="/RL/images/dist/dist-rl-agz.png" alt="drawing" width="600"/>
- **IMPALA**: DeepMind. IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures. ICML'18
	- https://github.com/deepmind/scalable_agent \
		<img src="/RL/images/dist/impala.png" alt="drawing" width="700"/>
	- V-trace: old policy mu (generated the trajectory), new policy pi\
		<img src="/RL/images/dist/impala2.png" alt="drawing" width="600"/>
- T Salimans, J Ho, X Chen, S Sidor, I Sutskever. Evolution Strategies as a Scalable Alternative to Reinforcement Learning. 2017
	<img src="/RL/images/dist/dist-rl-evo.png" alt="drawing" width="600"/>
- **RLlib**: E Liang, R Liaw, P Moritz, R Nishihara, R Fox, K Goldberg, J E. Gonzalez, M I. Jordan, I Stoica. RLlib: Abstractions for Distributed Reinforcement Learning. ICML'18
	- https://ray.readthedocs.io/en/latest/rllib.html \
		<img src="/RL/images/dist/rllib.png" alt="drawing" width="600"/>
- **R2D2**: S Kapturowski, G Ostrovski, J Quan, R Munos, W Dabney. Recurrent Experience Replay in Distributed Reinforcement Learning. ICLR'19
- **dopamine**: DeepMind. Dopamine: A Research Framework for Deep Reinforcement Learning. 2018
		- https://github.com/google/dopamine
- Algorithms
	- Y. Li and D. Schuurmans. Mapreduce for parallel reinforcement learning. Recent advances in reinforcement learning, 2011.
	- DeepMind. Data-efficient deep reinforcement learning for dexterous manipulation. 2017
	- DeepMind. Distributed prioritized experience replay. ICLR'18