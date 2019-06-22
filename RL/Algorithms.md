# Strong Baselines

## Policy Gradient
- Sergey Levine:
	- PG
	<img src="/RL/images/pg.png" alt="drawing" width="600"/>

	- Baseline for variance reduction:
	<img src="/RL/images/pg-baseline.png" alt="drawing" width="600"/>

	- IS, off-policy PG
	<img src="/RL/images/pg-is.png" alt="drawing" width="600"/>

- Classic
	- On-Policy
	- Better Convergence
	- Effective in high-dimensional or continuous action spaces
	- Can learn **stochastic** policies
- Off-Policy
	- Importance-Sampling
- Legacy
	- Williams (1992). Simple statistical gradient-following algorithms for connectionist
reinforcement learning: introduces REINFORCE algorithm
	- Baxter & Bartlett (2001). Infinite-horizon policy-gradient estimation: temporally decomposed policy gradient (not the first paper on this! see actor-critic section later)
	- Peters & Schaal (2008). Reinforcement learning of motor skills with policy gradients: very accessible overview of optimal baselines and natural gradient
- SOA
	- Levine & Koltun (2013). Guided policy search: deep RL with importance sampled policy gradient (unrelated to later discussion of guided policy search)
	- **TRPO**: Schulman, L., Moritz, Jordan, Abbeel (2015). Trust region policy optimization: deep RL with natural policy gradient and adaptive step size
		- Theoretical Guarantee of monotonic improvement if KL constraint satisfied
		- Surrogate loss
		- Line search to make the best stepsize update;
		- Wojciech Zaremba: https://github.com/wojzaremba/trpo
		<img src="/RL/images/trpo1.png" alt="drawing" width="600"/>
		<img src="/RL/images/trpo2.png" alt="drawing" width="600"/>
		<img src="/RL/images/trpo3.png" alt="drawing" width="600"/>
		<img src="/RL/images/trpo4.png" alt="drawing" width="600"/>
		<img src="/RL/images/trpo5.png" alt="drawing" width="400"/>

	- **PPO** Schulman, Wolski, Dhariwal, Radford, Klimov (2017). Proximal policy optimization algorithms: deep RL with importance sampled policy gradient
	<img src="/RL/images/ppo.png" alt="drawing" width="400"/>

	- Trust region policy optimization with value function approximation

## Value + Policy, Actor-Critic
- Sergey Levine:
<img src="/RL/images/ac1.png" alt="drawing" width="500"/>
<img src="/RL/images/ac2.png" alt="drawing" width="500"/>

- Classic
	- Actor: the policy
	- Critic: value function
	- Reduce variance of policy gradient
- Legacy
	- Sutton, McAllester, Singh, Mansour (1999). Policy gradient methods for reinforcement learning with function approximation: actor-critic algorithms with value function approximation
- SOA
	- D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, and M. Riedmiller. Deterministic policy gradient algorithms. ICML, 2014.
	- **A3C**: V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. P. Lillicrap, T. Harley, D. Silver, and K. Kavukcuoglu. Asynchronous methods for deep reinforcement learning. ICML'16
		- Hogwild
	- **GAE**: J Schulman, P Moritz, S Levine, M I. Jordan and P Abbeel. High-dimensional continuous control with generalized advantage estimation. ICLR'16
	<img src="/RL/images/gae.png" alt="drawing" width="500"/>

	- **Q-Prop**: sample-efficient policy- gradient with an off-policy critic: policy gradient with Q-function control variate
	<img src="/RL/images/q-prop.png" alt="drawing" width="600"/>

	- **PCL**: O Nachum, M Norouzi, K Xu, D Schuurmans. Bridging the gap between value and policy based reinforcement learning, NIPS'17
		- combine the unbiasedness and stability of on-policy training with the data efficiency of off-policy approaches
		<img src="/RL/images/pcl.png" alt="drawing" width="600"/>

## Value Function
- Sergey Levine:
<img src="/RL/images/q-1.png" alt="drawing" width="500"/>
<img src="/RL/images/q-2.png" alt="drawing" width="500"/>
<img src="/RL/images/q-3.png" alt="drawing" width="500"/>

- Classic
	- Off-Policy
	- Experience Replay
	- Fixed Q-targets
	<img src="/RL/images/q-4.png" alt="drawing" width="500"/>

	- Multi-Step Returns: R Munos, T Stepleton, A Harutyunyan, M G. Bellemare. Safe and Efficient Off-Policy Reinforcement Learning. NIPS'16
	<img src="/RL/images/q-multistep.png" alt="drawing" width="500"/>

- Legacy
	- C. J. Watkins and P. Dayan. Q-learning. Machine learning, 1992.
- SOA
	- **DQN** Playing Atari with deep reinforcement learning, Mnih et al. ‘13
	- **DQN** V. Mnih, et.al. Human level control through deep reinforcement learning. Nature, 2015.
	- **Double Q-Learning**: H v Hasselt, A Guez, D Silver. Deep Reinforcement Learning with Double Q-learning. NIPS'15
		- Two network, one to choose action, the other to compute Q(s,a)
		<img src="/RL/images/double-q.png" alt="drawing" width="500"/>

	- T Schaul, J Quan, I Antonoglou and D Silver. Prioritized Experience Replay. ICLR'16
		- Prioritizing with TD-error
		- Implement with a heap
	- **Dueling network**: Z Wang, T Schaul, M Hessel, H v Hasselt, M Lanctot, N d Freitas. Dueling network architectures for deep reinforcement learning, ICML'16
	<img src="/RL/images/duel.png" alt="drawing" width="500"/>

	- **Distributional RL**: Bellemare, M. G.; Dabney, W.; and Munos, R. 2017. A distributional perspective on reinforcement learning. ICML'17

	- **Noisy Nets**: Fortunato, M.; Azar, M. G.; Piot, B.; Menick, J.; Osband, I.; Graves, A.; Mnih, V.; Munos, R.; Hassabis, D.; Pietquin, O.; Blundell, C.; and Legg, S. Noisy networks for exploration. ICLR'18

	- **Rainbow**: M Hessel, J Modayil, H v Hasselt, T Schaul, G Ostrovski, W Dabney, D Horgan, B Piot, M Azar, D Silver. Combining improvements in deep reinforcement learning, AAAI'18
		- Double Q-learning
		- Prioritized replay
		- Dueling network
		- Multi-step learning
		- Distributional RL
		- Noisy Nets (for Montezuma's Revenge)
	- **Non-delusional Q-learning and value iteration**, NIPS 2018 best paper award:
		- Delusion: parameter update inconsistent with following policy;
		- PCVI: Tabular (model-based MDP)
		- PCQL: Q-learning (model-free)
- Continuous:
	- S Gu, T Lillicrap, I Sutskever, S Levine. Continuous Deep Q-Learning with Model-based Acceleration. ICML'16
	- **DDPG**: T P. Lillicrap, J J. Hunt, A Pritzel, N Heess, T Erez, Y Tassa, D Silver, D Wierstra. Continuous control with deep reinforcement learning. ICLR'16
		- https://github.com/ghliu/pytorch-ddpg
		<img src="/RL/images/ddpg.png" alt="drawing" width="500"/>

	- D Kalashnikov, A Irpan, P Pastor, J Ibarz, A Herzog, E Jang, D Quillen, E Holly, M Kalakrishnan, V Vanhoucke, S Levine. QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation. CoRL'18

## Baselines
- Open-AI Baselines
	- https://github.com/openai/baselines
	- A2C, ACER, ACKTR
	- DDPG
	- DQN
	- GAIL
	- HER
	- PPO1 (Multi-CPU using MPI), PPO2 (Optimized for GPU), TRPO
- Pytorch libraries:
	- DQN Adventure: https://github.com/higgsfield/RL-Adventure
	- Ye Yuan (CMU): https://github.com/Khrylx/PyTorch-RL
	- Shangtong Zhang: https://github.com/ShangtongZhang/DeepRL
	- Ilya Kostrikov (NYU): https://github.com/ikostrikov
	- Rainbow: https://github.com/Kaixhin/Rainbow
	- A3C LSTM: https://github.com/dgriff777/rl_a3c_pytorch
- Tensorflow libraries:
	- https://github.com/brendanator/atari-rl
	- https://github.com/steveKapturowski/tensorflow-rl
	- https://github.com/tensorflow/agents
- Shane Gu:
	- https://github.com/shaneshixiang/rllabplusplus
- Berkeley RL:
	- https://github.com/rll/rllab
- GA3C:
	- https://github.com/NVlabs/GA3C
