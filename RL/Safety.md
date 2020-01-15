# Safe, Robust RL

## Safe RL
- Legacy:
	- **CMDP**: Altman, Eitan. Constrained Markov Decision Processes. 1999
	- Uchibe, Eiji and Doya, Kenji. Constrained reinforcement learning from intrinsic and extrinsic rewards. ICDL'07
		- Heuristic CMDP: gradient projection
	- Moldovan, Teodor Mihai and Abbeel, Pieter. Safe Exploration in Markov Decision Processes. ICML'12
- Chow, Yinlam, Ghavamzadeh, Mohammad, Janson, Lucas, and Pavone, Marco. Risk-Constrained Reinforcement Learning with Percentile Risk Criteria. JMLR'15
	- **Primal-dual** subgradient method for risk-constrained reinforcement learning 
	- Takes policy gradient steps on an objective that trades off return with risk
	- Simultaneously learning the trade-off coefficients (dual variables).
- Bou Ammar, Haitham, Tutunov, Rasul, and Eaton, Eric. Safe Policy Search for Lifelong Reinforcement Learning with Sublinear Regret. ICML'15
	- Theoretic
- Amodei et al. Concrete Problems in AI Safety, 2016. 
	- Contribution: establishes a taxonomy of safety problems, serving as an important jumping-off point for future research. We need to solve these!
	- 1. Avoiding Negative Side Effects;
	- 2. Avoiding Reward Hacking;
	- 3. Scalable Oversight;
	- 4. Safe Exploration;
	- 5. Robustness to Distribution Shift;
- Shalev-Shwartz, Shai, Shammah, Shaked, and Shashua, Amnon. Safe, Multi-Agent, Reinforcement Learning for Autonomous Driving. 2016
	- avoid the problem of enforcing constraints on parametrized policies by decomposing 'desires' from trajectory planning;
	- the neural network policy learns desires for behavior
	- while the trajectory planning algorithm (which is not learned) selects final behavior and enforces safety constraints;
- **LFP**: Christiano et al. Deep Reinforcement Learning From Human Preferences, 2017.
- **CPO**: Achiam et al. Constrained Policy Optimization. 2017.
	- near-constraint satisfaction at each iteration\
		<img src="/RL/images/safety/cpo.png" alt="drawing" width="400"/>
- Held, David, Mccarthy, Zoe, Zhang, Michael, Shentu, Fred, and Abbeel, Pieter. Probabilistically Safe Policy Transfer. ICRA'17
- **HIRL**: Saunders et al. Trial without Error: Towards Safe Reinforcement Learning via Human Intervention, 2017.
- **Intrinsic-fear**: Lipton, Zachary C., Gao, Jianfeng, Li, Lihong, Chen, Jianshu, and Deng, Li. Combating Deep Reinforcement Learning’s Sisyphean Curse with Intrinsic Fear.
- **Leave-No-Trace**: Eysenbach et al. Leave No Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning, 2017.
- Chow, Y., Ghavamzadeh, M., Janson, L., and Pavone, M. Risk-constrained reinforcement learning with percentile risk criteria. JMLR'17
- **Safety-Layer**: Dalal et al. Safe Exploration in Continuous Action Spaces. ICML'18. 
	- Algorithm: DDPG+Safety Layer.
	- Problem setup: bounded CMDP, safe control in physical systems\
		<img src="/RL/images/safety/safety-layer1.png" alt="drawing" width="400"/>
	- Plug-in for DDPG:\
		<img src="/RL/images/safety/safety-layer2.png" alt="drawing" width="400"/>
	- The safety layer;\
		<img src="/RL/images/safety/safety-layer3.png" alt="drawing" width="400"/>
- Y Chow, O Nachum, E Duenez-Guzman, M Ghavamzadeh. A Lyapunov-based Approach to Safe Reinforcement Learning. NIPS'18
	- CMDP (Constrained MDP), with upper-bound cost we should satisfy;
	- safe policy iteration (SPI) and safe value iteration (SVI);
	- safe DQN, safe DPI;
- Constrained Cross-Entropy Method for Safe Reinforcement Learning. NIPS'18
- Yinlam Chow, Ofir Nachum, Aleksandra Faust, Edgar Duenez-Guzman, Mohammad Ghavamzadeh. Lyapunov-based Safe Policy Optimization for Continuous Control. ICML'19
	- Lagrange method: max_theta min_lambda c(xt,at) + lambda (D(xt|pi,x0)-d)
	- Lyapunov constraint: feasibility set;

## Robust Control
- **LQG-Robust**: Sarah Dean, Nikolai Matni, Benjamin Recht, and Vickie Ye. Robust Guarantees for Perception-Based Control. 2019
	- https://github.com/modestyachts/robust-control-from-vision
	- Affine error-profile model;
	- Model: MBRL (LQR)
	- Evaluated on synthetic example CARLA