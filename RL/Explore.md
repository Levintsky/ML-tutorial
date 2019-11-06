# Exploration, Exploitation

## Sergey Levine
- lec-17, 18
- UCB
<img src="/RL/images/xx/xx-ucb.png" alt="drawing" width="500"/>

- **Thompson Sampling**: O Chapelle, L Li. An Empirical Evaluation of Thompson Sampling, NIPS'11
- Information Gain: D Russo, B V Roy. Learning to Optimize via Information-Directed Sampling. NIPS'14
<img src="/RL/images/xx/xx-ig.png" alt="drawing" width="500"/>
- Summary
<img src="/RL/images/xx/xx-sum.png" alt="drawing" width="500"/>

- Deep UCB:
	- **Pseudo-Count**: M G. Bellemare, S Srinivasan, G Ostrovski, T Schaul, D Saxton, R Munos. Unifying Count-Based Exploration and Intrinsic Motivation, NIPS'16
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
	<img src="/RL/images/xx/xx-pseudo.png" alt="drawing" width="500"/>

	- **Hash**: H Tang, R Houthooft, D Foote, A Stooke, X Chen, Y Duan, J Schulman, F D Turck, P Abbeel. #Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning. NIPS'17
	<img src="/RL/images/xx/xx-hash.png" alt="drawing" width="600"/>
	
	- **Classifier for seen/unseen**: J Fu, J D. Co-Reyes, S Levine. EX2: Exploration with Exemplar Models for Deep Reinforcement Learning, NIPS'17
	<img src="/RL/images/xx/xx-class.png" alt="drawing" width="600"/>
	<img src="/RL/images/xx/xx-class2.png" alt="drawing" width="600"/>

- Thompson Sampling
	- I Osband, C Blundell, A Pritzel, B V Roy. Deep Exploration via Bootstrapped DQN, NIPS'16
	<img src="/RL/images/xx/xx-bootstrap1.png" alt="drawing" width="600"/>
	<img src="/RL/images/xx/xx-bootstrap2.png" alt="drawing" width="600"/>

## Multi-Arm Bandit
- http://iosband.github.io/2015/07/28/Beat-the-bandit.html
- https://github.com/bgalbraith/bandits

## SOA
- Stadie, Levine, Abbeel (2015). Incentivizing Exploration in Reinforcement Learning with Deep Predictive Models.
- Skip Context Tree Switching
- **Go-Explore**: A Ecoffet, J Huizinga, J Lehman, K O. Stanley, J Clune. Go-Explore: a New Approach for Hard-Exploration
Problems. NIPS'19
	- Montezuma’s Revenge Solved by Go-Explore, a New Algorithm for Hard-Exploration Problems (Sets Records on Pitfall, Too)
	- https://eng.uber.com/go-explore/

## Curiosity
- J. Schmidhuber, Curious model-building control systems. IJCNN'91
- Y. Sun, F. Gomez, and J. Schmidhuber, Planning to be surprised: Optimal Bayesian exploration in
dynamic environments. AGI'11
- **VIME**: R Houthooft, X Chen, Y Duan, J Schulman, F De Turck, P Abbeel. VIME: Variational Information Maximizing Exploration. NIPS'16
	- Improve on e-greedy and adding Gaussian noise;
	- Maximization of information gain about the agent's belief of environment dynamics;
	- **MBRL?**: Model the dynamics with a model theta,
	<img src="/RL/images/xx/vime1.png" alt="drawing" width="600"/>
	<img src="/RL/images/xx/vime2.png" alt="drawing" width="600"/>

- Deepak Pathak: TensorFlow code for Curiosity-driven Exploration for Deep Reinforcement Learning, ICML 2017
	- https://github.com/pathak22/noreward-rl
- **I2A**T Weber, S Racanière, D P. Reichert, L Buesing, A Guez, D J Rezende, A P Badia, O Vinyals, N Heess, Y Li, R Pascanu, P Battaglia, D Hassabis, D Silver, D Wierstra. Imagination-Augmented Agents for Deep Reinforcement Learning. NIPS'17
- Sainbayar Sukhbaatar, Zeming Lin, Ilya Kostrikov, Gabriel Synnaeve, Arthur Szlam, Rob Fergus. Intrinsic Motivation and Automatic Curricula via Asymmetric Self-Play. ICLR'18

## Legacy
- Schmidhuber. A Possibility for Implementing Curiosity and Boredom in Model-Building Neural Controllers. 1992