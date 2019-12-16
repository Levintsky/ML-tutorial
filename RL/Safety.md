# Safe, Robust RL

## Safe RL
- Amodei et al. Concrete Problems in AI Safety, 2016. 
	- Contribution: establishes a taxonomy of safety problems, serving as an important jumping-off point for future research. We need to solve these!
- **LFP**: Christiano et al. Deep Reinforcement Learning From Human Preferences, 2017.
- **CPO**: Achiam et al. Constrained Policy Optimization. 2017.
- **HIRL**: Saunders et al. Trial without Error: Towards Safe Reinforcement Learning via Human Intervention, 2017.
	- Algorithm: HIRL
- **Leave-No-Trace**: Eysenbach et al. Leave No Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning, 2017.
	- Algorithm: Leave No Trace.
- **Safety-Layer**: Dalal et al. Safe Exploration in Continuous Action Spaces. 2018. 
	- Algorithm: DDPG+Safety Layer.
- Y Chow, O Nachum, E Duenez-Guzman, M Ghavamzadeh. A Lyapunov-based Approach to Safe Reinforcement Learning. NIPS'18
	- CMDP (Constrained MDP), with upper-bound cost we should satisfy;
	- safe policy iteration (SPI) and safe value iteration (SVI);
	- safe DQN, safe DPI;

## Robust Control
- **LQG-Robust**: Sarah Dean, Nikolai Matni, Benjamin Recht, and Vickie Ye. Robust Guarantees for Perception-Based Control. 2019
	- https://github.com/modestyachts/robust-control-from-vision
	- Affine error-profile model;
	- Model: MBRL (LQR)
	- Evaluated on synthetic example CARLA