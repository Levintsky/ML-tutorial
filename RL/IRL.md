# Inverse Reinforcement Learning

## Sergey Levine
- lec-16
- Legacy problem setup: feature mapping
<img src="/RL/images/irl1.png" alt="drawing" width="600"/>
<img src="/RL/images/irl2.png" alt="drawing" width="600"/>

- From control inference
<img src="/RL/images/irl3.png" alt="drawing" width="600"/>
<img src="/RL/images/irl4.png" alt="drawing" width="600"/>
<img src="/RL/images/irl5.png" alt="drawing" width="600"/>
<img src="/RL/images/irl6.png" alt="drawing" width="600"/>

- Max Ent IRL
<img src="/RL/images/irl7.png" alt="drawing" width="600"/>

## SOA
- M Wulfmeier, P Ondruska, I Posner. Maximum Entropy Deep Inverse Reinforcement Learning. ICML'16
- C Finn, S Levine, P Abbeel. Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization. ICML'16
- Wulfmeier et al. Deep Maximum Entropy Inverse Reinforcement Learning. MaxEnt inverse RL using deep reward functions. arXiv'16
- C Finn, P Christiano, P Abbeel, S Levine. A Connection Between Generative Adversarial Networks, Inverse Reinforcement Learning, and Energy-Based Models. 2016
<img src="/RL/images/irl-gan.png" alt="drawing" width="500"/>

- **GAIL**: Jonathan Ho, Stefano Ermon. Generative Adversarial Imitation Learning. NIPS'16
	<img src="/RL/images/irl-gail.png" alt="drawing" width="500"/>
	- Expert replay sample (s, a)
	- Policy sample (s', a')
	- Update discriminator D with gradient penalty
	- Update reward in rollouts with predicted reward from discrimator D as log(D(s',a'))
	- Update policy with the fake reward
	<img src="/RL/images/gail.png" alt="drawing" width="500"/>

- J Fu, K Luo, S Levine. Learning Robust Rewards with Adversarial Inverse Reinforcement Learning. ICLR'18

## Reward Shaping
- A. Y. Ng, D. Harada, and S. Russell. Policy invariance under reward transformations: Theory and application to reward shaping. ICML'99.
<img src="/RL/images/reward-shaping.png" alt="drawing" width="500"/>

- I. Mordatch, E. Todorov, and Z. Popovic. Discovery of complex behaviors through contact-invariant optimization. TOG'12
- Y. Tassa, T. Erez, and E. Todorov. Synthesis and stabilization of complex behaviors through online trajectory optimization. IROS'12

## Legacy
- P Abbeel, A Ng. Apprenticeship Learning via Inverse Reinforcement Learning. ICML'04
- B D. Ziebart, A Maas, J Bagnell, and A K. Dey. Maximum Entropy Inverse Reinforcement Learning. AAAI'08