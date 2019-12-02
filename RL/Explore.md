# Exploration, Exploitation

## Classics
- lec-17, 18 (CS-294, Sergey Levine)
- Approach 1: UCB\
	<img src="/RL/images/xx/xx-ucb.png" alt="drawing" width="500"/>
- Approach 2: **Thompson Sampling**: O Chapelle, L Li. An Empirical Evaluation of Thompson Sampling, NIPS'11
	<img src="/RL/images/xx/thompson-sampling.png" alt="drawing" width="500"/>
	- Information Gain: D Russo, B V Roy. Learning to Optimize via Information-Directed Sampling. NIPS'14\
	<img src="/RL/images/xx/xx-ig.png" alt="drawing" width="500"/>
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
- **CTS-Pseudocounts**: M G. Bellemare, S Srinivasan, G Ostrovski, T Schaul, D Saxton, R Munos. Unifying Count-Based Exploration and Intrinsic Motivation, NIPS'16
	- CTS model (Bellemare, M., Veness, J., and Talvitie, E. (2014). Skip context tree switching. ICML'14);
	- Enhance the reward r with rareness of next state N(s), r'=r+beta/sqrt(N(s)+eps):
		<img src="/RL/images/xx/xx-pseudo.png" alt="drawing" width="500"/>
- **PixelCNN-Pseudocounts**: Georg Ostrovski, Marc G. Bellemare, Aaron van den Oord, Remi Munos. Count-Based Exploration with Neural Density Models. ICML'17
- **Hash-Pseudocounts**: H Tang, R Houthooft, D Foote, A Stooke, X Chen, Y Duan, J Schulman, F D Turck, P Abbeel. #Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning. NIPS'17
	<img src="/RL/images/xx/xx-hash.png" alt="drawing" width="400"/>
	<img src="/RL/images/xx/xx-hash2.png" alt="drawing" width="400"/>
- **EX2**: J Fu, J D. Co-Reyes, S Levine. EX2: Exploration with Exemplar Models for Deep Reinforcement Learning, NIPS'17
	- https://github.com/justinjfu/exemplar_models
	- Exemplar-classifier for seen/unseen:
	<img src="/RL/images/xx/xx-ex2-1.png" alt="drawing" width="400"/>
	- Model archetecture (amortized rather than one each model)
	<img src="/RL/images/xx/xx-ex2-2.png" alt="drawing" width="400"/>
	- Put together:
	<img src="/RL/images/xx/xx-ex2-3.png" alt="drawing" width="400"/>
- Thompson Sampling
	- I Osband, C Blundell, A Pritzel, B V Roy. Deep Exploration via Bootstrapped DQN, NIPS'16
	<img src="/RL/images/xx/xx-bootstrap1.png" alt="drawing" width="600"/>
	<img src="/RL/images/xx/xx-bootstrap2.png" alt="drawing" width="600"/>

## Multi-Arm Bandit
- http://iosband.github.io/2015/07/28/Beat-the-bandit.html
- https://github.com/bgalbraith/bandits

## Unclassified
- Stadie, Levine, Abbeel (2015). Incentivizing Exploration in Reinforcement Learning with Deep Predictive Models.
- Skip Context Tree Switching
- **Go-Explore**: A Ecoffet, J Huizinga, J Lehman, K O. Stanley, J Clune. Go-Explore: a New Approach for Hard-Exploration Problems. NIPS'19
	- Montezuma's Revenge Solved by Go-Explore, a New Algorithm for Hard-Exploration Problems (Sets Records on Pitfall, Too)
	- https://eng.uber.com/go-explore/

## Curiosity
- J. Schmidhuber, Curious model-building control systems. IJCNN'91
- J. Schmidhuber, Formal theory of creativity, fun, and intrinsic motivation (1990–2010), IEEE Trans. Auton. Mental Develop'10
- Y. Sun, F. Gomez, and J. Schmidhuber, Planning to be surprised: Optimal Bayesian exploration in dynamic environments. AGI'11
- **VIME**: R Houthooft, X Chen, Y Duan, J Schulman, F De Turck, P Abbeel. VIME: Variational Information Maximizing Exploration. NIPS'16
	- Insight: MBRF with BNN on **dynamics uncertainty**;
	- Improve on e-greedy and adding Gaussian noise;
	- Trick 1: Maximization of information gain about the agent's belief of environment dynamics; KL() measure the diff prior and posterior (after the new (st, at, st+1)), s.t. r'(st, at, st+1) = r(st, at) + KL(prior|posterior)\
	<img src="/RL/images/xx/vime1.png" alt="drawing" width="500"/>
	- Trick 2: Variational Bayes with BNN; assume the parameters observe factorized Gaussian;\
	<img src="/RL/images/xx/vime2.png" alt="drawing" width="500"/>
	- Put all together: run an episdoe with current policy, save KL change;  update the policy with r'(s,a,st+1) with curiosity added in reward;\
	<img src="/RL/images/xx/vime3.png" alt="drawing" width="500"/>
- **ICM**: Deepak Pathak, Pulkit Agrawal, Alexei A. Efros, Trevor Darrell. for Curiosity-driven Exploration for Deep Reinforcement Learning, ICML 2017
	- Insight: given action, prediction next state? (can't model stochasticity or white noise);
	- Inverse model: given two states, guess what actions taken;
	- https://github.com/pathak22/noreward-rl (TensorFlow)\
	<img src="/RL/images/xx/xx-icm.png" alt="drawing" width="500"/>
- **I2A**: T Weber, S Racanière, D P. Reichert, L Buesing, A Guez, D J Rezende, A P Badia, O Vinyals, N Heess, Y Li, R Pascanu, P Battaglia, D Hassabis, D Silver, D Wierstra. Imagination-Augmented Agents for Deep Reinforcement Learning. NIPS'17
- Sainbayar Sukhbaatar, Zeming Lin, Ilya Kostrikov, Gabriel Synnaeve, Arthur Szlam, Rob Fergus. Intrinsic Motivation and Automatic Curricula via Asymmetric Self-Play. ICLR'18
- Yuri Burda, Harri Edwards, Deepak Pathak, Amos Storkey, Trevor Darrell, Alexei A. Efros. Large-Scale Study of Curiosity-Driven Learning. ICLR'19
	- Contribution: Systematic analysis of how surprisal-based intrinsic motivation performs in a wide variety of environments.
- Yuri Burda, Harrison Edwards, Amos Storkey, Oleg Klimov. Exploration by Random Network Distillation. ICLR'19

## Legacy
- Schmidhuber. A Possibility for Implementing Curiosity and Boredom in Model-Building Neural Controllers. 1992