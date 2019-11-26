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
- Legacy
	- **REINFORCE**: Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. 1992
	- Baxter & Bartlett (2001). Infinite-horizon policy-gradient estimation: temporally decomposed policy gradient (not the first paper on this! see actor-critic section later)
	- Peters & Schaal (2008). Reinforcement learning of motor skills with policy gradients: very accessible overview of optimal baselines and natural gradient
- SOA
	- About **Natural Gradient**:
		- https://www.zhihu.com/question/266846405
		- https://zhuanlan.zhihu.com/p/82934100
	- Levine & Koltun (2013). Guided policy search: deep RL with importance sampled policy gradient (unrelated to later discussion of guided policy search)
	- **TRPO**: J Schulman, S Levine, P Moritz, M Jordan, P Abbeel. Trust region policy optimization. ICML'15
		- **Trick-1**: make new expectation as old plus Advantage; J(pi')=J(pi)+E(Adv(s,a)), notice the expectation is under new policy pi';
		- **Trick-2**: not able to get expectation under new policy? IS, Ex~p[f(x)]=Ex~q[q/p f(x)]
		- **Trick-3**: bound the difference between pi'(s) and pi(s), |pi'(s)-pi(s)| < eps easier to bound; 
		- **Trick-4**: First order approx for J, natural gradient for update;
		- https://zhuanlan.zhihu.com/p/26308073
		- Theoretical Guarantee of monotonic improvement if KL constraint satisfied
		- Surrogate loss
		- Line search to make the best stepsize update;
		- Wojciech Zaremba: https://github.com/wojzaremba/trpo
		<img src="/RL/images/trpo1.png" alt="drawing" width="600"/>
		<img src="/RL/images/trpo2.png" alt="drawing" width="600"/>
		<img src="/RL/images/trpo3.png" alt="drawing" width="600"/>
		<img src="/RL/images/trpo4.png" alt="drawing" width="600"/>
		<img src="/RL/images/trpo5.png" alt="drawing" width="400"/>

	- **PPO** J Schulman, P Wolski, P Dhariwal, A Radford and O Klimov. Proximal policy optimization algorithms: deep RL with importance sampled policy gradient. 2017
	<img src="/RL/images/ppo.png" alt="drawing" width="400"/>

	- Trust region policy optimization with value function approximation

## Value + Policy, Actor-Critic
- Sergey Levine:
<img src="/RL/images/ac1.png" alt="drawing" width="500"/>
<img src="/RL/images/ac2.png" alt="drawing" width="500"/>

- Implementation loops:
	- 1: act/sample, no gradient!
	```python
	def act(self, inputs, rnn_hxs, masks, deterministic=False):
		value, actor_features, rnn_hxs = self.base(inputs, rnn_hxs, masks)
		# Discrete if discrete; Diag-Gaussian if continuous
		dist = self.dist(actor_features)
		if deterministic:
			action = dist.mode()
		else:
			action = dist.sample()
		action_log_probs = dist.log_probs(action)
		dist_entropy = dist.entropy().mean()
		return value, action, action_log_probs, rnn_hxs
	```
	- 1.1 Env step
	```python 
	obs, reward, done, infos = envs.step(action)
	# st, at, st+1, vt, rt, mt
	rollouts.insert(obs, recurrent_hidden_states, action,
					action_log_prob, value, reward, masks, bad_masks)
	```
	- 2: A2C/PPO/...
	- 2.1 Estimate target value (GAE/n-step)
	```python
	next_value = actor_critic.get_value(
		rollouts.obs[-1], rollouts.recurrent_hidden_states[-1],
		rollouts.masks[-1]).detach()
	rollouts.compute_returns(next_value, args.use_gae, args.gamma,
		args.gae_lambda, args.use_proper_time_limits)
	```
	- 2.2 Update
	```python
	def update(self, rollouts):
		values = values.view(num_steps, num_processes, 1)
		action_log_probs = action_log_probs.view(num_steps, num_processes, 1)
		advantages = rollouts.returns[:-1] - values
		value_loss = advantages.pow(2).mean()
		action_loss = -(advantages.detach() * action_log_probs).mean()
	```
	- 2.3 After-update:
	```python
	def after_update(self):
		self.obs[0].copy_(self.obs[-1])
		self.recurrent_hidden_states[0].copy_(self.recurrent_hidden_states[-1])
		self.masks[0].copy_(self.masks[-1])
		self.bad_masks[0].copy_(self.bad_masks[-1])
	```

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
	<img src="/RL/images/gae.png" alt="drawing" width="600"/>

	- **Q-Prop**: S Gu, T Lillicrap, Z Ghahramani, R E. Turner, S Levine. Sample-efficient policy-gradient with an off-policy critic: policy gradient with Q-function control variate. ICLR'17
		- https://github.com/shaneshixiang/rllabplusplus
	<img src="/RL/images/q-prop.png" alt="drawing" width="600"/>

	- **PCL**: O Nachum, M Norouzi, K Xu, D Schuurmans. Bridging the gap between value and policy based reinforcement learning, NIPS'17
		- combine the unbiasedness and stability of on-policy training with the data efficiency of off-policy approaches
		<img src="/RL/images/pcl.png" alt="drawing" width="600"/>

## Value Function
- Sergey Levine:
<img src="/RL/images/q-1.png" alt="drawing" width="500"/>
<img src="/RL/images/q-2.png" alt="drawing" width="500"/>
<img src="/RL/images/q-3.png" alt="drawing" width="500"/>

- DDPG (Cont) design:
	- 1. ddpg class;
	```python
	class DDPG(object):
		def __init__(self, gamma, tau, hidden_size, num_inputs, action_space):
			self.actor = Actor(hidden_size, self.num_inputs, self.action_space)
			self.actor_target = Actor(hidden_size, self.num_inputs, self.action_space)
			self.actor_perturbed = Actor(hidden_size, self.num_inputs, self.action_space)
			self.actor_optim = Adam(self.actor.parameters(), lr=1e-4)
			self.critic = Critic(hidden_size, self.num_inputs, self.action_space)
			self.critic_target = Critic(hidden_size, self.num_inputs, self.action_space)
			self.critic_optim = Adam(self.critic.parameters(), lr=1e-3)
			self.gamma = gamma
			self.tau = tau
			hard_update(self.actor_target, self.actor)  # Make sure target is with the same weight
			hard_update(self.critic_target, self.critic)
	```
	- 2. Collect experience
	```python
	def select_action(self, state):
		self.actor.eval()
        if param_noise is not None: 
            mu = self.actor_perturbed((Variable(state)))
        else:
            mu = self.actor((Variable(state)))
        self.actor.train()
        mu = mu.data
        if action_noise is not None:
            mu += torch.Tensor(action_noise.noise())
        return mu.clamp(-1, 1)
	action = agent.select_action(state, ounoise, param_noise)
    next_state, reward, done, _ = env.step(action.numpy()[0])
    total_numsteps += 1
    episode_reward += reward
    action = torch.Tensor(action)
    mask = torch.Tensor([not done])
    next_state = torch.Tensor([next_state])
    reward = torch.Tensor([reward])
    memory.push(state, action, mask, next_state, reward)
	```
	- 3. Learning
		- value loss: (s, a) -> critic(theta1) -> v-predict with v-target for theta1
		- policy loss: (s, actor(s, theta2)) -> critic -> v for theta2
	```python
	# value learning
	next_action_batch = self.actor_target(next_state_batch)
    next_state_action_values = self.critic_target(next_state_batch, next_action_batch)
    reward_batch = reward_batch.unsqueeze(1)
    mask_batch = mask_batch.unsqueeze(1)
    expected_state_action_batch = reward_batch + (self.gamma * mask_batch * next_state_action_values)
    self.critic_optim.zero_grad()
    state_action_batch = self.critic((state_batch), (action_batch))
    value_loss = F.mse_loss(state_action_batch, expected_state_action_batch)
    value_loss.backward()
    self.critic_optim.step()
    # actor learning
    self.actor_optim.zero_grad()
    policy_loss = -self.critic((state_batch),self.actor((state_batch)))
    policy_loss = policy_loss.mean()
    policy_loss.backward()
    self.actor_optim.step()
	```
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
	- **DQN** Playing Atari with deep reinforcement learning, Mnih et al. 2013
	- **DQN** V. Mnih, et.al. Human level control through deep reinforcement learning. Nature, 2015.
	- **Double Q-Learning**: H v Hasselt, A Guez, D Silver. Deep Reinforcement Learning with Double Q-learning. NIPS'15
		- Two network, one to choose action, the other to compute Q(s,a)
		<img src="/RL/images/double-q.png" alt="drawing" width="500"/>

	- T Schaul, J Quan, I Antonoglou and D Silver. Prioritized Experience Replay. ICLR'16
		- Prioritizing with TD-error
		- Implement with a heap
	- **Dueling network**: Z Wang, T Schaul, M Hessel, H v Hasselt, M Lanctot, N d Freitas. Dueling network architectures for deep reinforcement learning, ICML'16
		- Two heads for value function;
		- One for state value;
		- One for state-dependent action advantage function;
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
	- **SVG**: N. Heess. Learning continuous control policies by stochastic value gradients. NIPS'15
		- SVG(0): model free
		<img src="/RL/images/svg0.png" alt="drawing" width="500"/>

		- SVG(1): one-step dynamics
		<img src="/RL/images/svg1.png" alt="drawing" width="500"/>

		- SVG(inf)
		<img src="/RL/images/svg-inf.png" alt="drawing" width="500"/>

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
