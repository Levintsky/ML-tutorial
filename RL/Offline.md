# Offline RL

## Basics
- Train with different sources of data (experts, agents, ...)
	- Learn without exploration
- Distribution shift: 

## Misc
- QT-Opt: Google-Brin.Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation, Kalashnikov et al, 2018
	- Offline QT-Opt: 87% success
	- Finetuned QT-Opt: 93% success
- A Kumar, J Fu, G Tucker, S Levine. Stabilizing Off-Policy Q-Learning via Bootstrapping Error Reduction. NeurIPS'19
	- Massive overestimation;

## Policy Constraint method
- Iteratively do:
	- Q(s, a) = r(s, a) + E.a′~ π-new[Q(s′,a′)]
	- π-new(a|s) = argmax.π E.a~ π(a|s)[Q(s, a)]
		- s.t. KL(π, πβ) ≤ ε
		- πβ: behavior policy;
- Problems:
	- behavior policy πβ from different source;
	- Over pessimistic or optimistic;
- Solution:
	- Avoid evaluating actions not in the dataset;
	- Train Q() s.t. OOD actions never have high values;
- Legacy:
	- Todorov: passive dynamics in linearly solvable MDPs;
	- Kappen: KL-divergence control;
	- trust-regions, covariant PG, natural PG;
- Fox: Taming the noise... [UAI'16]
- Fujimoto: Off-Policy '18
- Jaques: Way Off Policy '19
- Kumar: Stabilizing '19
- Wu: Behavior regularized '19
- I Kostrikov, A Nair, S Levine. Offline Reinforcement Learning with Implicit Q-Learning. '21
	- Expectile loss: assymetric MSE;
- A Singh, A Yu, J Yang, J Zhang, AKumar, S Levine. COG: Connecting New Skills to Past Experience with Offline Reinforcement Learning. CoRL'20