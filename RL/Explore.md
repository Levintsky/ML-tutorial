# Exploration, Exploitation

## From spinningup
- Intrinsic motivation: VIME, CTS/PixelCNN/hash-based pseudo-count; EX2; ICM; Burda; RND;
- Unsupervised: VIC; DIAYN; VALOR;

## Classics
- lec-17, 18 (CS-294, Sergey Levine)
- Approach 1: **UCB** (Upper Confidence Bounds)
	- Intuition: try each arm until you are sure it's not great:
		- a = argmax μa + sqrt(2lnT/N(a))
		- Reg(T) ~ O(logT), provably as good as any algorithm
- Approach 2: **Thompson Sampling**:
	- An easy tutorial: https://github.com/andrecianflone/thompson/blob/master/thompson.ipynb
	- O Chapelle, L Li. An Empirical Evaluation of Thompson Sampling, NIPS'11
	- Russo, Daniel, Benjamin Van Roy, Abbas Kazerouni, and Ian Osband. A Tutorial on Thompson Sampling. 2017
- Approach 3: Information Gain:
	- D Russo, B V Roy. Learning to Optimize via Information-Directed Sampling. NIPS'14
		- IG(z,y|a) = E_y[H(p(z))-H(p(z)|y)|a], how much we learn about z from action a;
		- y = ra, z = θa (parameters of model p(ra))
		- g(a) = IG(θa,ra|a), information gain about a;
		- ∆a = E[r(a\*)-r(a)], expected suboptimality of a;
		- Choose a based on argmin_a ∆a^2/g(a),
			- Numerator ∆a^2: don't take suboptimal actions you know;
			- Denominator g(a): dont' take action you won't learn anything;
- In Q-learning:
	- ∆w = α(r(s)+γmaxQˆ(s',a';w)−Qˆ(s,a;w))∇wQˆ(s,a;w)
	- ∆w = α(r(s)+r(s,a)+γmaxQˆ(s',a';w)−Qˆ(s,a;w))∇wQˆ(s,a;w)
		- r(s,a): uncertainty;
- Summary\
	<img src="/RL/images/xx/xx-sum.png" alt="drawing" width="500"/>

## With NN
- A general framework:
```python
def process_reward(self, reward, frames):
    if self.config.exploration_bonus:
        reward += self.exploration_bonus.bonus(frames)
# where we have
def bonus(self, observation):
  frame = cv2.resize(observation[-1], self.frame_shape) // 32
  # Calculate pseudo count
  prob = self.update_density_model(frame)
  recoding_prob = self.density_model_probability(frame)
  pseudo_count = prob * (1 - recoding_prob) / (recoding_prob - prob)
  if pseudo_count < 0:
    pseudo_count = 0  # Occasionally happens at start of training
  # Return exploration bonus
  exploration_bonus = self.beta / math.sqrt(pseudo_count + 0.01)
  return exploration_bonus
```
- Pseudo-count:
	- **CTS**: M G. Bellemare, S Srinivasan, G Ostrovski, T Schaul, D Saxton, R Munos. Unifying Count-Based Exploration and Intrinsic Motivation, NIPS'16
		- CTS model (Bellemare, M., Veness, J., and Talvitie, E. (2014). Skip context tree switching. ICML'14);
		- Enhance the reward r with rareness of next state N(s), r'=r+β/sqrt(N(s)+ε):
			<img src="/RL/images/xx/xx-pseudo.png" alt="drawing" width="500"/>
	- **PixelCNN**: Georg Ostrovski, Marc G. Bellemare, Aaron van den Oord, Remi Munos. Count-Based Exploration with Neural Density Models. ICML'17
	- **Hash**: H Tang, R Houthooft, D Foote, A Stooke, X Chen, Y Duan, J Schulman, F D Turck, P Abbeel. #Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning. NIPS'17\
		<img src="/RL/images/xx/xx-hash.png" alt="drawing" width="400"/>
		<img src="/RL/images/xx/xx-hash2.png" alt="drawing" width="400"/>
- **EX2**: J Fu, J D. Co-Reyes, S Levine. EX2: Exploration with Exemplar Models for Deep Reinforcement Learning, NIPS'17
	- https://github.com/justinjfu/exemplar_models
	- Exemplar-classifier for seen/unseen:\
		<img src="/RL/images/xx/xx-ex2-1.png" alt="drawing" width="400"/>
	- Model archetecture (amortized rather than one each model)\
		<img src="/RL/images/xx/xx-ex2-2.png" alt="drawing" width="400"/>
	- Put together:\
		<img src="/RL/images/xx/xx-ex2-3.png" alt="drawing" width="400"/>
- Thompson Sampling:
	- Mandel, Liu, Brunskill, Popovic. Thompson sampling over representation & parameters. IJCAI'16
	- I Osband, C Blundell, A Pritzel, B V Roy. Deep Exploration via Bootstrapped DQN, NIPS'16
		- Train C DQN agents using bootstrapped samples; (expensive to train C nn);
		- Shared network Q with K outputs {Qk}k=1..K, masking distribution M:
			- Initial state s0;
			- k ~ Uniform(1,..,K); (choose a head)
			- for t=1..T do
				- Pick a = argmaxQk(st,a); (pick based on the head)
				- st+1, rt;
				- Sample bootstrap mask mt ~ M;
				- Add (st,at,rt+1,st+1,mt) to replay buffer;
  	- Azizzadenesheli, Anandkumar. Efficient Exploration through Bayesian Deep Q-Networks. NeurIPS workshop 2017
  		- Use deep NN with last layer as Bayesian linear regression;

## Unclassified
- Stadie, Levine, Abbeel (2015). Incentivizing Exploration in Reinforcement Learning with Deep Predictive Models.
- Skip Context Tree Switching
- **Go-Explore**: A Ecoffet, J Huizinga, J Lehman, K O. Stanley, J Clune. Go-Explore: a New Approach for Hard-Exploration Problems. NIPS'19
	- Montezuma's Revenge Solved by Go-Explore, a New Algorithm for Hard-Exploration Problems (Sets Records on Pitfall, Too)
	- https://eng.uber.com/go-explore/

## Curiosity, Intrinsic Reward
- J. Schmidhuber, Curious model-building control systems. IJCNN'91
- J. Schmidhuber, Formal theory of creativity, fun, and intrinsic motivation (1990–2010), IEEE Trans. Auton. Mental Develop'10
- Y. Sun, F. Gomez, and J. Schmidhuber, Planning to be surprised: Optimal Bayesian exploration in dynamic environments. AGI'11
- **VIME**: R Houthooft, X Chen, Y Duan, J Schulman, F De Turck, P Abbeel. VIME: Variational Information Maximizing Exploration. NIPS'16
	- Insight: MBRF with BNN on **dynamics uncertainty**;
	- Improve on e-greedy and adding Gaussian noise;
	- Trick 1: Maximization of information gain about the agent's belief of environment dynamics; KL() measure the diff prior and posterior (after the new (st, at, st+1)), s.t. r'(st, at, st+1) = r(st, at) + KL(prior|posterior)\
		<img src="/RL/images/xx/vime1.png" alt="drawing" width="500"/>\
	- Trick 2: Variational Bayes with BNN; assume the parameters observe factorized Gaussian;\
		<img src="/RL/images/xx/vime2.png" alt="drawing" width="500"/>\
	- Put all together: run an episdoe with current policy, save KL change;  update the policy with r'(s,a,st+1) with curiosity added in reward;\
		<img src="/RL/images/xx/vime3.png" alt="drawing" width="500"/>
- **ICM**: Deepak Pathak, Pulkit Agrawal, Alexei A. Efros, Trevor Darrell. for Curiosity-driven Exploration for Deep Reinforcement Learning, ICML 2017
	- Insight: given action, prediction next state? (can't model stochasticity or white noise);
	- Inverse model: given two states, guess what actions taken;
	- https://github.com/pathak22/noreward-rl (TensorFlow)\
	<img src="/RL/images/xx/xx-icm.png" alt="drawing" width="500"/>
- **I2A**: T Weber, S Racanière, D P. Reichert, L Buesing, A Guez, D J Rezende, A P Badia, O Vinyals, N Heess, Y Li, R Pascanu, P Battaglia, D Hassabis, D Silver, D Wierstra. Imagination-Augmented Agents for Deep Reinforcement Learning. NIPS'17
- Sainbayar Sukhbaatar, Zeming Lin, Ilya Kostrikov, Gabriel Synnaeve, Arthur Szlam, Rob Fergus. Intrinsic Motivation and Automatic Curricula via Asymmetric Self-Play. ICLR'18
- Sergey. Visual Reinforcement Learning with Imagined Goals. NIPS'18
- Learning to Play With Intrinsically-Motivated, Self-Aware Agents. NIPS'18
- Satinder Singh. On Learning Intrinsic Rewards for Policy Gradient Methods. NIPS'18
- Yuri Burda, Harri Edwards, Deepak Pathak, Amos Storkey, Trevor Darrell, Alexei A. Efros. Large-Scale Study of Curiosity-Driven Learning. ICLR'19
	- Contribution: Systematic analysis of how surprisal-based intrinsic motivation performs in a wide variety of environments.
- Yuri Burda, Harrison Edwards, Amos Storkey, Oleg Klimov. Exploration by Random Network Distillation. ICLR'19

## Unsupervised Option Discovery
- R Sutton, D Precup, and S Singh. Between mdps and semi-mdps: A framework for temporal abstraction in reinforcement learning. AI'99
- **Intrinsically motivated agent**
- Tobias Jung, Daniel Polani, and Peter Stone. Empowerment for continuous agent—environment systems. Adaptive Behavior, 19(1):16–39, 2011.
- Shakir Mohamed and Danilo Jimenez Rezende. Variational information maximisation for intrinsically motivated reinforcement learning. NIPS'15
- **VIC**: Karol Gregor, Danilo Rezende and Daan Wierstra. Variational Intrinsic Control. ICLR'17
	- Unsupervised RL, discover set of intrinsic options
	- Maximizing the number of different states an agent can reliably reach
	- Notation: option Omega, then associated policy pi(a|s,Omega) follows the option;
	- Different option should result in different result, if for two options Ω1 and Ω2, upon reaching state s(f1), we can infer it was option Ω1 that was executed rather than Ω2, and when reaching a state s(f2) we can infer it was option Ω2 rather than Ω1, then Ω1 and Ω2 can be said to be intrinsically different options:\
		<img src="/RL/images/hrl/vic1.png" alt="drawing" width="500"/>
	- p(sf|s0,Ω) is inherent to the environment, but obtaining Bayes' reverse p(Ω|s0,sf) is difficult. I-VB for approximate:\
		<img src="/RL/images/hrl/vic2.png" alt="drawing" width="500"/>
	- Put together to learn options Omega:\
		<img src="/RL/images/hrl/vic3.png" alt="drawing" width="400"/>
	- Intrinsic control with implicit options (action as options):\
		<img src="/RL/images/hrl/vic4.png" alt="drawing" width="400"/>
	- Experiments: grid world;
- Carlos Florensa, Yan Duan, and Pieter Abbeel. Stochastic neural networks for hierarchical reinforcement learning. 2017
	- Setting: with a single task reward;
- Roy Fox, Sanjay Krishnan, Ion Stoica, and Ken Goldberg. Multi-Level Discovery of Deep Options. 2017
- Karol Hausman, Jost Tobias Springenberg, Ziyu Wang, Nicolas Heess, and Martin Riedmiller. Learning an embedding space for transferable robot skills. ICLR'18
	- Insight: a discriminability objective is equivalent to maximizing the mutual information between the latent skill z and some aspect of the corresponding trajectory;
	- Setting: with many tasks and reward function
- **VALOR**: Joshua Achiam, Harrison Edwards, Dario Amodei, Pieter Abbeel. Variational Option Discovery Algorithms. 2018
	- https://github.com/Steven-Ho/VALOR (pytorch)
	- Option discovery based on variational inference
	- Trick 1: VAE style;
	- Trick 2: curriculum learning;
	- Context c sample from a noisy distribution G, decoder D decodes back to c, Cost function with 2nd term encourage exploratoin:\
		<img src="/RL/images/hrl/valor1.png" alt="drawing" width="300"/>
	- Algorithm:\
		<img src="/RL/images/hrl/valor2.png" alt="drawing" width="400"/>
	- Network architecture, notice the decoder does not see action, otherwise it will cheat and ignore environment;
		<img src="/RL/images/hrl/valor2.png" alt="drawing" width="400"/>
- **DIAYN**: Benjamin Eysenbach, Abhishek Gupta, Julian Ibarz, Sergey Levine. Diversity is All You Need: Learning Skills without a Reward Function. ICLR'19
	- **Unsupervised skill discovery**: Unsupervised emergence of diverse skills, such as walking and jumping; learn skills that not only are **distinguishable**, but also are as **diverse** as possible
	- Trick 1: max entropy polices to force skill diverse;
	- Trick 2: fix the prior distribution over skills, rather than learn it; (prevent collapsing to sampling only a handful of skills)
	- Trick 3: discriminator looks at every state (VIC only final state)\
		<img src="/RL/images/hrl/diayn.png" alt="drawing" width="400"/>
	- The utility:\
		<img src="/RL/images/hrl/diayn2.png" alt="drawing" width="400"/>

## Unclassified
- https://blog.openai.com/reinforcement-learning-with-prediction-based-rewards/
- https://blog.openai.com/learning-montezumas-revenge-from-a-single-demonstration/
- Exploration in Structured Reinforcement Learning. NIPS'18
- Improving Exploration in Evolution Strategies for Deep Reinforcement Learning via a Population of Novelty-Seeking Agents. NIPS'18
- Diversity-Driven Exploration Strategy for Deep Reinforcement Learning. NIPS'18

## Legacy
- Schmidhuber. A Possibility for Implementing Curiosity and Boredom in Model-Building Neural Controllers. 1992