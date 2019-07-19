# Exploration, Exploitation

## Sergey Levine
- lec-17, 18
- UCB
<img src="/RL/images/xx-ucb.png" alt="drawing" width="500"/>

- **Thompson Sampling**: O Chapelle, L Li. An Empirical Evaluation of Thompson Sampling, NIPS'11
- Information Gain: D Russo, B V Roy. Learning to Optimize via Information-Directed Sampling. NIPS'14
<img src="/RL/images/xx-ig.png" alt="drawing" width="500"/>
- Summary
<img src="/RL/images/xx-sum.png" alt="drawing" width="500"/>

- Deep UCB:
	- **Pseudo-Count**: M G. Bellemare, S Srinivasan, G Ostrovski, T Schaul, D Saxton, R Munos. Unifying Count-Based Exploration and Intrinsic Motivation, NIPS'16
	<img src="/RL/images/xx-pseudo.png" alt="drawing" width="500"/>

	- **Hash**: H Tang, R Houthooft, D Foote, A Stooke, X Chen, Y Duan, J Schulman, F D Turck, P Abbeel. #Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning. NIPS'17
	<img src="/RL/images/xx-hash.png" alt="drawing" width="600"/>
	
	- **Classifier for seen/unseen**: J Fu, J D. Co-Reyes, S Levine. EX2: Exploration with Exemplar Models for Deep Reinforcement Learning, NIPS'17
	<img src="/RL/images/xx-class.png" alt="drawing" width="600"/>
	<img src="/RL/images/xx-class2.png" alt="drawing" width="600"/>

- Thompson Sampling
	- I Osband, C Blundell, A Pritzel, B V Roy. Deep Exploration via Bootstrapped DQN, NIPS'16
	<img src="/RL/images/xx-bootstrap1.png" alt="drawing" width="600"/>
	<img src="/RL/images/xx-bootstrap2.png" alt="drawing" width="600"/>

## Multi-Arm Bandit
- http://iosband.github.io/2015/07/28/Beat-the-bandit.html
- https://github.com/bgalbraith/bandits

## SOA
- **VIME**: Houthooft, Chen, Duan, Schulman, De Turck, Abbeel. (2016). VIME: Variational Information Maximizing Exploration.
<img src="/RL/images/vime1.png" alt="drawing" width="600"/>
<img src="/RL/images/vime2.png" alt="drawing" width="600"/>

- Stadie, Levine, Abbeel (2015). Incentivizing Exploration in Reinforcement Learning with Deep Predictive Models.
- Skip Context Tree Switching
- **Go-Explore**: A Ecoffet, J Huizinga, J Lehman, K O. Stanley, J Clune. Go-Explore: a New Approach for Hard-Exploration
Problems. NIPS'19
	- Montezuma’s Revenge Solved by Go-Explore, a New Algorithm for Hard-Exploration Problems (Sets Records on Pitfall, Too)
	- https://eng.uber.com/go-explore/

## Curiosity
- Deepak Pathak: TensorFlow code for Curiosity-driven Exploration for Deep Reinforcement Learning, ICML 2017
	- https://github.com/pathak22/noreward-rl
- Imagination-Augmented Agents for Deep Reinforcement Learning

## Legacy
- Schmidhuber. A Possibility for Implementing Curiosity and Boredom in Model-Building Neural Controllers. 1992