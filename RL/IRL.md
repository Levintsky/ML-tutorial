# Inverse Reinforcement Learning

## Basics
- Sergey Levine (294 lec-16)
- Legacy problem setup: feature mapping\
	<img src="/RL/images/irl/irl1.png" alt="drawing" width="600"/>
- SVM trick: demonstration better than other trajectory by a margin\
	<img src="/RL/images/irl/irl2.png" alt="drawing" width="600"/>
- From control inference: policy probability\
	<img src="/RL/images/irl/irl3.png" alt="drawing" width="600"/>
- MLE with parition function:\
	<img src="/RL/images/irl/irl4.png" alt="drawing" width="500"/>
	<img src="/RL/images/irl/irl5.png" alt="drawing" width="600"/>
	<img src="/RL/images/irl/irl6.png" alt="drawing" width="600"/>
- Max Ent IRL\
	<img src="/RL/images/irl/irl7.png" alt="drawing" width="600"/>

## Unclassified
- M Wulfmeier, P Ondruska, I Posner. Maximum Entropy Deep Inverse Reinforcement Learning. ICML'16
- **GCL**: C Finn, S Levine, P Abbeel. Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization. ICML'16
	- Many costs can explain same demo: 1. max-margin; 2. probabilistic (GCL);
	- Solving inner loop control: 1. inner-loop MDP (requires dynamics); 2. sampling (GCL);
	- Build on IOC [Ziebart'08]
	- Framework:\
		<img src="/RL/images/irl/gcl1.png" alt="drawing" width="500"/>
	- Algorithm: the sampling q(tau) is critical:\
		<img src="/RL/images/irl/gcl2.png" alt="drawing" width="500"/>
- Wulfmeier et al. Deep Maximum Entropy Inverse Reinforcement Learning. MaxEnt inverse RL using deep reward functions. arXiv'16
- Lifelong Inverse Reinforcement Learning. NIPS'18

## Adversarial
- C Finn, P Christiano, P Abbeel, S Levine. A Connection Between Generative Adversarial Networks, Inverse Reinforcement Learning, and Energy-Based Models. 2016
	- Generator: sample; data: demonstration
	- Discriminator:\
		<img src="/RL/images/irl/irl-gan.png" alt="drawing" width="500"/>
- **GAIL**: J Ho, S Ermon. Generative Adversarial Imitation Learning. NIPS'16
	<img src="/RL/images/irl/irl-gail.png" alt="drawing" width="500"/>
	<img src="/RL/images/irl/gail.png" alt="drawing" width="500"/>
	- Implementation on Mujoco (main-loop):
	- 1. Agent collect samples -> batch; (st, at, mt, st+1, rt) with customized reward as log(D(s',a'))
```python
def expert_reward(state, action):
    return -math.log(discrim_net(state_action)[0].item())
reward = custom_reward(state, action)
memory.push(state, action, mask, next_state, reward)
```
	- 2. Update parameters
	- 2.1 (reward, action, state, mask) from batch (step 1);
	- 2.2 Estimate advantage;
	- 2.3 Update discriminator D with gradient penalty: 1 iteration
		- Input: [state, action] of expert, sample
	- 2.4 Minibatch PPO;
	- 2.4.1 Estimate advantage;
```python
# actor-critic
values = value_net(states) # (B, 1)
fixed_log_probs = policy_net.get_log_prob(states, actions) # (B, 1)
# GAE with rollouts
def estimate_advantages():
    for i in reversed(range(rewards.size(0))):
    deltas[i] = rewards[i] + gamma * prev_value * masks[i] - values[i]
    advantages[i] = deltas[i] + gamma * tau * prev_advantage * masks[i]
    prev_value = values[i, 0]
    prev_advantage = advantages[i, 0]
returns = values + advantages
advantages = (advantages - advantages.mean()) / advantages.std()
return advantages, returns
```
	- 2.4.2 PPO:
```python
# critic
values_pred = value_net(states)
value_loss = (values_pred - returns).pow(2).mean()
# weight decay
for param in value_net.parameters():
    value_loss += param.pow(2).sum() * l2_reg
optimizer_value.zero_grad()
value_loss.backward()
optimizer_value.step()
# policy
log_probs = policy_net.get_log_prob(states, actions)
ratio = torch.exp(log_probs - fixed_log_probs)
surr1 = ratio * advantages
surr2 = torch.clamp(ratio, 1.0 - clip_epsilon, 1.0 + clip_epsilon) * advantages
policy_surr = -torch.min(surr1, surr2).mean()
optimizer_policy.zero_grad()
policy_surr.backward()
torch.nn.utils.clip_grad_norm_(policy_net.parameters(), 40)
optimizer_policy.step()
```
- J. Ho, J. K. Gupta, and S. Ermon. Model-free imitation learning with policy optimization. ICML'16.
- **InfoGAIL**: Y Li, J Song, S Ermon. InfoGAIL: Interpretable Imitation Learning from Visual Demonstrations. NIPS'17
	- Multimodal, assign each demonstration to each expert (fixed number)
- **MGAIL**: N Baram, O Anschel, I Caspi, S Mannor. End-to-End Differentiable Adversarial Imitation Learning. ICML'17
- J Fu, K Luo, S Levine. Learning Robust Rewards with Adversarial Inverse Reinforcement Learning. ICLR'18

## Reward Shaping
- A. Y. Ng, D. Harada, and S. Russell. Policy invariance under reward transformations: Theory and application to reward shaping. ICML'99\
	<img src="/RL/images/reward-shaping.png" alt="drawing" width="500"/>
- I. Mordatch, E. Todorov, and Z. Popovic. Discovery of complex behaviors through contact-invariant optimization. TOG'12
- Y. Tassa, T. Erez, and E. Todorov. Synthesis and stabilization of complex behaviors through online trajectory optimization. IROS'12

## Legacy
- P Abbeel, A Ng. Apprenticeship Learning via Inverse Reinforcement Learning. ICML'04
- B D. Ziebart, A Maas, J Bagnell, and A K. Dey. Maximum Entropy Inverse Reinforcement Learning. AAAI'08