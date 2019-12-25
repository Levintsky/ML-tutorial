# Distributed RL

## From Spinningup
- Adam Stooke, Pieter Abbeel. Accelerated Methods for Deep Reinforcement Learning, Stooke and Abbeel, 2018.
	- Contribution: Systematic analysis of parallelization in deep RL across algorithms.
	- https://github.com/astooke/accel_rl
- IMPALA, Ape-X, R2D2, RLlib;

## Distributed RL Platforms
- A summary:\
	<img src="/RL/images/dist/dist-rl-history.png" alt="drawing" width="600"/>
- 2013/2015: DQN\
	<img src="/RL/images/dist/dist-rl-dqn.png" alt="drawing" width="600"/>
- **Gorila**: A. Nair, P. Srinivasan, S. Blackwell, C. Alcicek, R. Fearon, V. Alessandro De Maria, Panneershelvam, M. Suleyman, C. Beattie, S. Petersen, S. Legg, V. Mnih, K. Kavukcuoglu, and D. Silver. Massively parallel methods for deep reinforcement learning view publication. ICML, 2015.\
	<img src="/RL/images/dist/dist-rl-gorila.png" alt="drawing" width="600"/>
- **A3C**: V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. P. Lillicrap, T. Harley, D. Silver, and K. Kavukcuoglu. Asynchronous methods for deep reinforcement learning. ICML'16\
	<img src="/RL/images/dist/a3c.png" alt="drawing" width="600"/>
- **Ape-X**: D Horgan, J Quan, D Budden, G Barth-Maron, M Hessel, H v Hasselt, D Silver. Distributed Prioritized Experience Replay. ICLR'18\
	<img src="/RL/images/dist/dist-rl-ape-x.png" alt="drawing" width="600"/>
- **AlphaZero**\
	<img src="/RL/images/dist/dist-rl-agz.png" alt="drawing" width="600"/>
- **IMPALA**: L Espeholt, H Soyer, R Munos, K Simonyan, V Mnih, T Ward, Y Doron, V Firoiu, T Harley, I Dunning, S Legg, K Kavukcuoglu. IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor-Learner Architectures. ICML'18
	- https://github.com/deepmind/scalable_agent \
		<img src="/RL/images/dist/impala.png" alt="drawing" width="700"/>
	- V-trace: old policy mu (generated the trajectory), new policy pi\
		<img src="/RL/images/dist/impala2.png" alt="drawing" width="600"/>
- T Salimans, J Ho, X Chen, S Sidor, I Sutskever. Evolution Strategies as a Scalable Alternative to Reinforcement Learning. 2017
	<img src="/RL/images/dist/dist-rl-evo.png" alt="drawing" width="600"/>
- **RLlib**: E Liang, R Liaw, P Moritz, R Nishihara, R Fox, K Goldberg, J E. Gonzalez, M I. Jordan, I Stoica. RLlib: Abstractions for Distributed Reinforcement Learning. ICML'18
	- https://ray.readthedocs.io/en/latest/rllib.html \
		<img src="/RL/images/dist/rllib.png" alt="drawing" width="600"/>
- **R2D2**: Steven Kapturowski, Georg Ostrovski, John Quan, Remi Munos, Will Dabney. Recurrent Experience Replay in Distributed Reinforcement Learning. ICLR'19
- Dopamine: https://github.com/google/dopamine

## Algorithms
- Y. Li and D. Schuurmans. Mapreduce for parallel reinforcement learning. Recent advances in reinforcement learning, 2011.
- Popov, I., Heess, N., Lillicrap, T., Hafner, R., BarthMaron, G., Vecerik, M., Lampe, T., Tassa, Y., Erez, T., and Riedmiller, M. Data-efficient deep reinforcement learning for dexterous manipulation. 2017
- Horgan, D., Quan, J., Budden, D., Barth-Maron, G., Hessel, M., van Hasselt, H., and Silver, D. Distributed prioritized experience replay. ICLR'18