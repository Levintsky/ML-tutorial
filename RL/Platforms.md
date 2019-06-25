# Platforms and Systems

## Platforms
- **ALE**: Bellemare, M. G.; Naddaf, Y.; Veness, J.; and Bowling, M. The arcade learning environment: An evaluation platform for general agents. JAIR'13'
- **FAIR**:
	- ELF: https://github.com/pytorch/ELF
	- House3D: https://github.com/facebookresearch/House3D
- **OpenAI**:
	- Open-AI gym: https://github.com/openai/gym
	- Robo-School: https://github.com/openai/roboschool
	- Mujoco: https://github.com/openai/mujoco-py
	- Continuous control: Y Duan, X Chen, R Houthooft, J Schulman, P Abbeel. Benchmarking Deep Reinforcement Learning for Continuous Control. ICML'16
		- https://github.com/rll/rllab
	- Retro Contest: A Nichol, V Pfau, C Hesse, O Klimov, J Schulman. Gotta Learn Fast: A New Benchmark for Generalization in RL. 2018
		- https://contest.openai.com/2018-1/
		- https://github.com/openai/retro#gym-retro
		- Classic video games to gym environment
- **DeepMind**:
	- DeepMind-Lab
		- 3D, first-person
		- Built on Quake III arena (1999)
		- Agent receives RGB(D) and reward, as well as velocity
		- Action: jump, crouch, 8 directions (left, right, 45deg, ...)
- **VizDoom**: ViZDoom: A Doom-based AI research platform for visual reinforcement learning. CIG 2016
	- Poland Team.
- **Minecraft**:
	- **Malmo**: Johnson M., Hofmann K., Hutton T., Bignell D. The Malmo Platform for Artificial Intelligence Experimentation. IJCAI'16
- **Retro**: N Bhonker, S Rozenberg and I Hubara. Playing SNES in the Retro Learning Environment. ICLR'17

## Distributed RL
- A summary:
<img src="/RL/images/dist-rl-history.png" alt="drawing" width="600"/>

- 2013/2015: DQN
<img src="/RL/images/dist-rl-dqn.png" alt="drawing" width="600"/>

- **Gorila**: A. Nair, P. Srinivasan, S. Blackwell, C. Alcicek, R. Fearon, V. Alessandro De Maria, Panneershelvam, M. Suleyman, C. Beattie, S. Petersen, S. Legg, V. Mnih, K. Kavukcuoglu, and D. Silver. Massively parallel methods for deep reinforcement learning view publication. ICML, 2015.
<img src="/RL/images/dist-rl-gorila.png" alt="drawing" width="600"/>

- **A3C**: V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. P. Lillicrap, T. Harley, D. Silver, and K. Kavukcuoglu. Asynchronous methods for deep reinforcement learning. ICML'16
<img src="/RL/images/a3c.png" alt="drawing" width="600"/>

- **Ape-X**: D Horgan, J Quan, D Budden, G Barth-Maron, M Hessel, H v Hasselt, D Silver. Distributed Prioritized Experience Replay. ICLR'18
<img src="/RL/images/dist-rl-ape-x.png" alt="drawing" width="600"/>

- **AlphaZero**
<img src="/RL/images/dist-rl-agz.png" alt="drawing" width="600"/>

- **IMPALA**: L Espeholt, H Soyer, R Munos, K Simonyan, V Mnih, T Ward, Y Doron, V Firoiu, T Harley, I Dunning, S Legg, K Kavukcuoglu. IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures. ICML'18
	- https://github.com/deepmind/scalable_agent
	<img src="/RL/images/impala.png" alt="drawing" width="700"/>

- T Salimans, J Ho, X Chen, S Sidor, I Sutskever. Evolution Strategies as a Scalable Alternative to Reinforcement Learning. 2017
<img src="/RL/images/dist-rl-evo.png" alt="drawing" width="600"/>

- **RLlib**: E Liang, R Liaw, P Moritz, R Nishihara, R Fox, K Goldberg, J E. Gonzalez, M I. Jordan, I Stoica. RLlib: Abstractions for Distributed Reinforcement Learning. ICML'18
	- https://ray.readthedocs.io/en/latest/rllib.html
	<img src="/RL/images/rllib.png" alt="drawing" width="600"/>

- Dopamine: https://github.com/google/dopamine

## Algorithms
- Y. Li and D. Schuurmans. Mapreduce for parallel reinforcement learning. Recent advances in reinforcement learning, 2011.