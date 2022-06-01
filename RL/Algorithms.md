# RL Algorithms

## Basics
- PG:
	- Log-trick, IS
	- TRPO:
		- Bound distribution change;
		- Bound objective value;
		- Natural gradient to bound π(a|s) change;
- AC:
	- Loss := |Adv(s,a)|^2 - sum Adv(s,a)logπ(a|s)
	- Adv := r(s,a) + γV(s') - V(s)
	- GAE: 
- Q-learning
	- BV: Q(s,a) = r(s,a) + max_a' Q(s',a'), contraction by γ;
	- Non-tabular: V = πBV, with π(.) as NN fitting;
	- Exploration: ε, greedy, Boltzmann;
	- Target-network, replay buffer;
	- Over-estimate: Double-Q, multi-step;
- Continuous Q-learning:
	- Sampling: CEM, CMA-ES;
	- Easily to optimize: NAF (normalized advantage function);
	- Learn an optimizer: DDPG;

## Resources
- https://spinningup.openai.com/en/latest/spinningup/keypapers.html
- https://github.com/navneet-nmk/pytorch-rl
- https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch
- Chinese:
	- https://zhuanlan.zhihu.com/sharerl
	- https://zhuanlan.zhihu.com/p/68205048
- Open-AI Baselines:
	- https://github.com/openai/baselines
	- A2C, ACER, ACKTR / DDPG / DQN / GAIL / HER
	- PPO1 (Multi-CPU using MPI), PPO2 (Optimized for GPU), TRPO
- **rlkit**
	- https://github.com/vitchyr/rlkit
	- RIG, TDMs, HER, DQN, SAC, TD3
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
- Shane Gu: https://github.com/shaneshixiang/rllabplusplus
- Berkeley RL: https://github.com/rll/rllab
- GA3C: https://github.com/NVlabs/GA3C
- Model-free RL from Spinningup:
	- DQN: DQN, DRQN; Duel DQN; PER; Rainbow;
	- PG: A3C, TRPO, GAE, PPO, ACKTR, ACER, SAC;
	- DPG: DPG, DDPG, TD3;
	- Distributional: C51, QR-DQN, IQN, Dopamine;
	- Action-dependent: Q-prop, Stein control, mirage;
	- PCL: PCL, Trust-PCL;
	- Other continuous combine pg and q: PGQL, Reactor, IPG, equivalence between...;
	- Evolutionary: ES;

## Policy Gradient
- Basic PG (from Sergey Levine CS-294):
	- θ = argmax E..τ\~p(θ) Σr(st, at), maximize J(θ)
		- Insight: reward depends on trajectory;
	- Trick: π(τ;θ)∇logπ(τ;θ) = ∇π(τ;θ)
	- PG: ∇J(θ) = ∫ πlogπ(τ;θ)r(τ)dτ = E..τ\~p(θ) ∇logπ(τ;θ)r(τ)
		- Insight: increase the probability of high reward trajectory;
	- Baseline for variance reduction:
		- E ∇logπ(τ;θ)b = 0, with 0 mean, so we can use any b in ∇logπ(r-b);
		- Get the baseline b to minimize Var(∇J(θ)); dVar/db=0;
		- b = E(g(τ)^2 r(τ)) / E(g(τ)^2), with g(τ)=∇logπ(τ;θ);
	- IS, off-policy PG:
		- Insight: we have trajectory of τ ~ p(θ) and try to optimize J(θ');
		- Weight each trajectory τ ~ p(θ) with p(θ')/p(θ), which is also π(τ;θ')/π(τ;θ);
		- PG of θ' becomes: weighted(Σ∇logπ)(Σr(st,at)) under τ ~ p(θ);
		- Keep up-to t and ignore future, we get TRPO;
		- Σ∇logπ(τ;θ') (Πt'=1..t π(θ')/π(θ)) (Σt'=t..T r(st,at))
- Advantages:
	- On-Policy
	- Better Convergence
	- Effective in high-dimensional or continuous action spaces
	- Can learn **stochastic** policies
- Legacy:
	- **REINFORCE**: Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. 1992
	- Baxter & Bartlett (2001). Infinite-horizon policy-gradient estimation: temporally decomposed policy gradient (not the first paper on this! see actor-critic section later)
	- Peters & Schaal (2008). Reinforcement learning of motor skills with policy gradients: very accessible overview of optimal baselines and natural gradient
- Recent:
	- **GPS**: S, Levine & Koltun. Guided policy search: deep RL with importance sampled policy gradient.  ICML'13. (unrelated to later discussion of guided policy search)
	- **TRPO**: J Schulman, S Levine, P Moritz, M Jordan, P Abbeel. Trust region policy optimization. ICML'15
		- **Trick-1**: make new expectation as old plus Advantage; J(π')=J(π)+E(Adv(s,a)), notice the expectation is under new policy π';
			- J(θ')-J(θ) = E..τ\~p(;θ') (Σt=0..∞ γ^t Adv(st, at;πθ))
			- Utility diff: sample from new trajectory, expectation of old advantage function;
		- **Trick-2**: not able to get expectation under new policy? IS, Expectation under p[f(x)] versus Expecation under q(x) q[q/p f(x)]
		- **Trick-3**: bound the difference between π'(s) and π(s) to make p(st;θ) and p(st;θ') closed, |π'(s)-π(s)| < ε easier to bound with KL-divergence;
			- p(s;θ') = (1-ε)^t p(s;θ) + (1-ε)^t p(s;other); still takes the same action with θ';
			- |p(s;θ')-p(s;θ)| <= 2εt; (Taylor Expansion)
			- J(θ')-J(θ) Sample from old trajectory instead will result in at most Σ..t 2εtC loss, with constant C bounded by O(Trmax) or O(rmax/1-γ);
		- **Trick-4**: First order approx for utility J(.), natural gradient for update;
			- θ' = argmaxθ' Σt E..st\~p(st;θ)[E..at\~π(at|st;θ)[π(;θ')/π(;θ) γ^t A(st,at;πθ')]]; traj, policy all sampled from old, IS advantage for new;
			- s.t. KL(π(at|st;θ')||π(at|st;θ')) < ε; constrained optimization;
			- Utility approx: argmax ∇..θ A(θ)(θ'-θ), s.t. KL(π(θ'),π(θ)) < ε;
				- We know KL(π(θ'),π(θ)) ~ 1/2 (θ'-θ)F(θ'-θ), with F as Fisher;
			- θ' = θ + αF^(-1)∇..θ J(θ), with α=sqrt(2ε/∇J F ∇J), largest step within trust-region;
		- https://zhuanlan.zhihu.com/p/26308073
		- In summary: Theoretical Guarantee of monotonic improvement if KL constraint satisfied; Surrogate loss; Line search to make the best stepsize update;
		- Wojciech Zaremba: https://github.com/wojzaremba/trpo
	- **PPO**: J Schulman, P Wolski, P Dhariwal, A Radford and O Klimov. Proximal policy optimization algorithms: deep RL with importance sampled policy gradient. 2017\
		<img src="/RL/images/algos/ppo.png" alt="drawing" width="400"/>
	- **PPO-Penalty**: Nicolas Heess, Dhruva TB, Srinivasan Sriram, Jay Lemmon, Josh Merel, Greg Wayne, Yuval Tassa, Tom Erez, Ziyu Wang, S. M. Ali Eslami, Martin Riedmiller, David Silver. Emergence of Locomotion Behaviours in Rich Environments. NIPS'17\
		<img src="/RL/images/algos/ppo-dist.png" alt="drawing" width="400"/>

## Value + Policy, Actor-Critic
- Basics: (Sergey Levine, CS-294)
	- Actor: the policy π(st|at;θ)
	- Critic: value function, Advantage A(s,a)=Q(s,a)-V(s)
		- Value V can be supervised by V=E[Q]
	- Reduce variance of policy gradient: update with A(s,a)∇logπ
- A general framework (for Implementation):
	- Phase 1: collect data (act/sample, no gradient!)
		- Given input x, neural net to get V(x), π(a|x), entropy H(π), and intermediate value such as h of RNN;
		- If deterministic, take action a argmax π(a|x), otherwise sample;
	- 1.1 Environment step forward;
		- Take action a, get reward, observation;
	- Phase 2: Learning of both actor and critic (A2C/PPO/...): 
		- 2.1 Critic target: Estimated with (GAE/n-step) V(st+1)
		- 2.2 Loss function and Update: value-loss  + action-loss;
			- L = adv^2 - adv log π(a|s)
		- 2.3 After-update: update mask, observation, and RNN-state (optional);
- Legacy
	- Sutton, McAllester, Singh, Mansour (1999). Policy gradient methods for reinforcement learning with function approximation: actor-critic algorithms with value function approximation
- Recent:
	- **DPG**: D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, and M. Riedmiller. Deterministic policy gradient algorithms. ICML'14
		- ∇..φ J(φ)=E[∇..aQ(s,a;π) ∇..φπ(s;φ)]
		- where Q(s,a;π)=E[Rt|s,a]
	- **A3C**: V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. P. Lillicrap, T. Harley, D. Silver, and K. Kavukcuoglu. Asynchronous methods for deep reinforcement learning. ICML'16
		- Hogwild
	- **GAE**: J Schulman, P Moritz, S Levine, M I. Jordan and P Abbeel. High-dimensional continuous control with generalized advantage estimation. ICLR'16\
		<img src="/RL/images/algos/gae.png" alt="drawing" width="400"/>
	- **ACER**: Ziyu Wang, Victor Bapst, Nicolas Heess, Volodymyr Mnih, Remi Munos, Koray Kavukcuoglu, Nando de Freitas. Sample Efficient Actor-Critic with Experience Replay. ICLR'17
		- AC with off-policy, IS;
		- Available in OpenAI baselines;
	- **ACKTR**: Yuhuai Wu, Elman Mansimov, Shun Liao, Roger Grosse, Jimmy Ba. Scalable trust-region method for deep reinforcement learning using Kronecker-factored approximation. 2017
		- **K-FAC** (Kronecker-factored approximate curvature) for both actor and critic;
	- **SAC**: Haarnoja, T., Zhou, A., Abbeel, P., and Levine, S. Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor. ICML'18
		- Insight: succeed while as random as possible; 1. separate network for policy and value; 2. off-policy AC; 3. Entropy max;
		- Problem setup: Continuous control;
		- Algorithm: off-policy actor-critic;
		- https://github.com/vitchyr/rlkit
		- Formulation: J(π) = sum r(st,at) + α H(π(.|st))
		- Lemma 1: formulation equivalent with soft Bellman (converge when infinity);
		- Lemma 2: project back to π' = argmin KL(π'(.|st), exp(Q(π-old))/Z-old) guarantees improvement;
		- Theory 3: soft policy iteration + projection converge to optimal;
		- Policy update: policy-loss = α log(π) - Q(s, π(s))
		- Value update: target value = r + α q_target(s', π(s'))
		- With V(.;ψ), V(.;ψ') as value network (original and target), Q(s,a;theta), π(.|s,φ), SAC alg:\
			<img src="/RL/images/algos/sac.png" alt="drawing" width="400"/>

## Value Function, Q-learning
- Basics (Sergey Levine, CS-294):\
	<img src="/RL/images/algos/q-1.png" alt="drawing" width="400"/>
	<img src="/RL/images/algos/q-2.png" alt="drawing" width="500"/>
	<img src="/RL/images/algos/q-3.png" alt="drawing" width="500"/>
- On policy: SARSA\
	<img src="/RL/images/algos/sarsa.png" alt="drawing" width="450"/>
- Classic
	- Q-learning: Off-Policy
	- Experience Replay
	- Fixed Q-targets\
		<img src="/RL/images/algos/q-4.png" alt="drawing" width="500"/>
	- Multi-Step Returns: R Munos, T Stepleton, A Harutyunyan, M G. Bellemare. Safe and Efficient Off-Policy Reinforcement Learning. NIPS'16\
		<img src="/RL/images/q-multistep.png" alt="drawing" width="500"/>
- Legacy:
	- **TD**: Sutton, R. S. Learning to predict by the methods of temporal differences. Machine learning, 3(1):9–44, 1988.
	- C. J. Watkins and P. Dayan. Q-learning. Machine learning'92.
	- **Experience Replay**: Lin, L.-J. Self-improving reactive agents based on reinforcement learning, planning and teaching. ML'92
	- **SARSA**: Singh, S., Jaakkola, T., Littman, M. L., and Szepesvari, C. Convergence results for single-step on-policy reinforcement-learning algorithms. ML'00
	- Precup, D., Sutton, R. S., and Dasgupta, S. Off-policy temporal-difference learning with function approximation. ICML'01
- More modern techniques:
	- **DQN**: Playing Atari with deep reinforcement learning, Mnih et al. 2013
	- **DQN**: V. Mnih, et.al. Human level control through deep reinforcement learning. Nature, 2015.
	- **DRQN**: Matthew Hausknecht, Peter Stone. Deep Recurrent Q-Learning for Partially Observable MDPs. AAAI'15
		- Could bootstrap from start of the episode or random point;\
			<img src="/RL/images/algos/drqn.png" alt="drawing" width="400"/>
	- **PER**: T Schaul, J Quan, I Antonoglou and D Silver. Prioritized Experience Replay. ICLR'16
		- Prioritizing with TD-error
		- Implement with a heap\
			<img src="/RL/images/algos/per.png" alt="drawing" width="400"/>
	- **Dueling network**: Z Wang, T Schaul, M Hessel, H v Hasselt, M Lanctot, N d Freitas. Dueling network architectures for deep reinforcement learning, ICML'16
		- Two heads for value function;
		- One for state value;
		- One for state-dependent action advantage function;\
			<img src="/RL/images/algos/duel.png" alt="drawing" width="400"/>
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
	- **SVG**: N. Heess. Learning continuous control policies by stochastic value gradients. NIPS'15
		- SVG(0): model free\
			<img src="/RL/images/svg0.png" alt="drawing" width="500"/>
		- SVG(1): one-step dynamics\
			<img src="/RL/images/svg1.png" alt="drawing" width="500"/>
		- SVG(inf)\
			<img src="/RL/images/svg-inf.png" alt="drawing" width="500"/>
	- S Gu, T Lillicrap, I Sutskever, S Levine. Continuous Deep Q-Learning with Model-based Acceleration. ICML'16
	- **DDPG**: T P. Lillicrap, J J. Hunt, A Pritzel, N Heess, T Erez, Y Tassa, D Silver, D Wierstra. Continuous control with deep reinforcement learning. ICLR'16
		- https://github.com/ghliu/pytorch-ddpg
		- A deep variant of DPG\
			<img src="/RL/images/algos/ddpg.png" alt="drawing" width="500"/>
		- 1. ddpg class;
			- Actor, actor-target, actor optimizer
			- Critic, critic-target, critic optimizer
		- 2. Collect experience: record (s, a, s', r)
		- 3. Learning
			- value loss (critic): Q(s, a; theta1) with target r + gamma Q-target(s', actor-target(s'))
			- policy loss (actor): -Q(s, actor(s))
	- D Kalashnikov, A Irpan, P Pastor, J Ibarz, A Herzog, E Jang, D Quillen, E Holly, M Kalakrishnan, V Vanhoucke, S Levine. QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation. CoRL'18
- **Overestimation**:
	- Thrun, S. and Schwartz, A. Issues in using function approximation for reinforcement learning. In Proceedings of the 1993 Connectionist Models Summer School Hillsdale, NJ. Lawrence Erlbaum, 1993.
	- **Double Q-Learning**: Van Hasselt, H. Double q-learning. NIPS'10
	- **Double DQN**: H v Hasselt, A Guez, D Silver. Deep Reinforcement Learning with Double Q-learning. NIPS'15
		- Two networks, one to choose action, the other to compute Q(s,a)
		<img src="/RL/images/algos/double-q.png" alt="drawing" width="500"/>
	- **TD3**: S Fujimoto, H van Hoof, D Meger. Addressing Function Approximation Error in Actor-Critic Methods. ICML'18
		- https://github.com/sfujim/TD3
		- Clipped Double Q-learning: actor x1,  critic x2 (not the target), target also has two critic;
		- For value iteration: y = r + min(Q1(s', a'), Q2(s', a'))
		- Delayed Policy update: at lower frequency;
		- Sync actor/critic target with current at even lower frequency;\
			<img src="/RL/images/algos/TD3.png" alt="drawing" width="400"/>
- Bias:
	- **SBEED**: Bo Dai, Albert Shaw, Lihong Li, Lin Xiao, Niao He, Zhen Liu, Jianshu Chen, Le Song. SBEED: Convergent Reinforcement Learning with Nonlinear Function Approximation. ICML'18
		- Value iteration does not have a cost function to optimize, it is just a fixed point iteration;
		- Key idea: use conjugate of the square function to avoid the bias introduced in square function;
		- Tradeoff: introduce a mini-max formulation;
		<img src="/RL/images/algos/sbeed.png" alt="drawing" width="400"/>
	- Yihao Feng, Lihong Li, Qiang Liu. A Kernel Loss for Solving the Bellman Equation. NIPS'19

## Unclassified
- **HER**: Marcin Andrychowicz, Filip Wolski, Alex Ray, Jonas Schneider, Rachel Fong, Peter Welinder, Bob McGrew, Josh Tobin, Pieter Abbeel, Wojciech Zaremba. Hindsight Experience Replay. NIPS'17
	<img src="/RL/images/algos/her.png" alt="drawing" width="500"/>
- Paulo Rauber, Avinash Ummadisingu, Filipe Mutz, Juergen Schmidhuber. Hindsight policy gradients. ICLR'19
- O'Donoghue, B., Osband, I., Munos, R., and Mnih, V. The uncertainty bellman equation and exploration. 2017
- **Smoothed**: Nachum, O., Norouzi, M., Tucker, G., and Schuurmans, D. Smoothed action value functions for learning gaussian policies. 2018
- Distributional:
	- **C51**: Bellemare, M. G.; Dabney, W.; and Munos, R. 2017. A distributional perspective on reinforcement learning. ICML'17
		- Q(s, a) from scalar to a categorical 51 classes (linear between v-min to v-max)
		- Do KL divergence training between Q(st, at) and r(st, at) + max_a Q(st+1, a), when take argmax action, just calculate expectation (marginalize 51 categories);\
			<img src="/RL/images/algos/c51.png" alt="drawing" width="400"/>
	- **QR-DQN**: Will Dabney, Mark Rowland, Marc G. Bellemare, Rémi Munos. Distributional Reinforcement Learning with Quantile Regression. AAAI'18\
		<img src="/RL/images/algos/qr-dqn.png" alt="drawing" width="400"/>
	- **IQN**: Will Dabney, Georg Ostrovski, David Silver, Remi Munos. Implicit Quantile Networks for Distributional Reinforcement Learning. ICML'18
	- **dopamine**: Pablo Samuel Castro, Subhodeep Moitra, Carles Gelada, Saurabh Kumar, Marc G. Bellemare. Dopamine: A Research Framework for Deep Reinforcement Learning. 2018
		- https://github.com/google/dopamine
	- Barth-Maron, G., Hoffman, M. W., Budden, D., Dabney, W., Horgan, D., TB, D., Muldal, A., Heess, N., and Lillicrap, T. Distributional policy gradients. ICLR'18
- Variance-reduction:
	 - Anschel, O., Baram, N., and Shimkin, N. Averaged-dqn: Variance reduction and stabilization for deep reinforcement learning. ICML'17
- Max Entropy:
	- Ziebart, B. D., Maas, A. L., Bagnell, J. A., and Dey, A. K. Maximum entropy inverse reinforcement learning. AAAI'08
	- Toussaint, M. Robot trajectory optimization using approximate inference. ICML'09
	- Rawlik, K., Toussaint, M., and Vijayakumar, S. On stochastic optimal control and reinforcement learning by approximate inference. RSS'12
	- Fox, R., Pakman, A., and Tishby, N. Taming the noise in reinforcement learning via soft updates. UAI'16
	- Haarnoja, T., Tang, H., Abbeel, P., and Levine, S. Reinforcement learning with deep energy-based policies. ICML'17
	- O’Donoghue, B., Munos, R., Kavukcuoglu, K., and Mnih, V. PGQ: Combining policy gradient and Q-learning. 2016
	- Schulman, J., Abbeel, P., and Chen, X. Equivalence between policy gradients and soft Q-learning. 2017
	- PCL: NIPS'17
	- SAC: 2018
- Action Dependent: (in AC, value function should be state-dependent)
	- **Q-Prop**: S Gu, T Lillicrap, Z Ghahramani, R E. Turner, S Levine. Sample-efficient policy-gradient with an off-policy critic: policy gradient with Q-function control variate. ICLR'17
		- Taylor approx of DPG/DDPG for value function, mixture of DPG/DDPG
		- https://github.com/shaneshixiang/rllabplusplus
		<img src="/RL/images/q-prop.png" alt="drawing" width="600"/>
	- **Stein-Control-Variate**: Hao Liu, Yihao Feng, Yi Mao, Dengyong Zhou, Jian Peng, Qiang Liu. Action-depedent Control Variates for Policy Optimization via Stein’s Identity. ICLR'18
	- The Mirage of Action-Dependent Baselines in Reinforcement Learning.
		- Contribution: interestingly, critiques and reevaluates claims from earlier papers (including Q-Prop and stein control variates) and finds important methodological errors in them.
		- Claims V(s,a) style does not reduce variance
- PCL:
	- **PCL**: O Nachum, M Norouzi, K Xu, D Schuurmans. Bridging the gap between value and policy based reinforcement learning, NIPS'17
		- combine the unbiasedness and stability of on-policy training with the data efficiency of off-policy approaches:
		- Entropy O(s,π)=O-old(s,π) + H(s,π) with **discounted entropy regularizer**\
		- H(s, π) = entropy(π|s) - gamma \* entropy(π|s')
		- Theory: correctness with control inference;\
			<img src="/RL/images/algos/pcl.png" alt="drawing" width="600"/>
	- **Trust-PCL**: Ofir Nachum, Mohammad Norouzi, Kelvin Xu, Dale Schuurmans. Trust-PCL: An Off-Policy Trust Region Method for Continuous Control. ICLR'18
- PG + Q-Learning:
	- O’Donoghue, B., Munos, R., Kavukcuoglu, K., and Mnih, V. PGQ: Combining policy gradient and Q-learning. 2016
	- **Reactor**: Audrunas Gruslys, Will Dabney, Mohammad Gheshlaghi Azar, Bilal Piot, Marc Bellemare, Remi Munos. The Reactor: A Fast and Sample-Efficient Actor-Critic Agent for Reinforcement Learning. ICLR'18
	- **IPG**: 	Interpolated Policy Gradient: Merging On-Policy and Off-Policy Gradient Estimation for Deep Reinforcement Learning
	- Schulman, J., Abbeel, P., and Chen, X. Equivalence between policy gradients and soft Q-learning. 2017
		- Theoretical link;

## Evoluation Strategy
- https://lilianweng.github.io/lil-log/2019/09/05/evolution-strategies.html
- **CMA-ES**: Nikolaus Hansen and Andreas Ostermeier. Completely derandomized self-adaptation in evolution strategies. Evolutionary computation, 9(2):159–195, 2001
	- a population of parameter vectors (“genotypes”) is perturbed "mutated" 
	- and their objective function value (“fitness”) is evaluated.
	- The highest scoring parameter vectors are then recombined to form the population for the next generation, and this procedure is iterated until the objective is fully optimized;
	- Successful in optimization in low-medium dimension;
- **NES**:
	- Daan Wierstra, Tom Schaul, Jan Peters, and Juergen Schmidhuber. Natural evolution strategies. 2008
	- Daan Wierstra, Tom Schaul, Tobias Glasmachers, Yi Sun, Jan Peters, and Jürgen Schmidhuber. Natural evolution strategies. JMLR'14
- **ES**: Tim Salimans, Jonathan Ho, Xi Chen, Szymon Sidor, Ilya Sutskever. Evolution Strategies as a Scalable Alternative to Reinforcement Learning. 2017
	- ES and parallel version:
		<img src="/RL/images/algos/es1.png" alt="drawing" width="450"/>
		<img src="/RL/images/algos/es2.png" alt="drawing" width="450"/>
	- Adaptive stepsize does not help;
	- Comparison with PG:\
		<img src="/RL/images/algos/es3.png" alt="drawing" width="400"/>
	- Experiments: 3D humanoid walking in 10 minute, competitive on Atari;
- Legacy:
	- I. Rechenberg and M. Eigen. Evolutionsstrategie: Optimierung Technischer Systeme nach Prinzipien der Biologischen Evolution. 1973
	- H.-P. Schwefel. Numerische optimierung von computer-modellen mittels der evolutionsstrategie. 1977
	- Juergen Schmidhuber and Jieyu Zhao. Direct policy search and uncertain policy evaluation. 1998
	- Sebastian Risi and Julian Togelius. Neuroevolution in games: State of the art and open challenges. 2015
- **Evolved Policy Gradients (OpenAI)**
