# Multi-Task/Transfer Learning

## Multi-Task
- Berkeley, Modular Multitask Reinforcement Learning with Policy Sketches

## Transfer
- Resources:
	- https://github.com/AI-ON/Multitask-and-Transfer-Learning
- Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World
- **OpenAI**:
	- **Retro Contest**: A Nichol, V Pfau, C Hesse, O Klimov, J Schulman. Gotta Learn Fast: A New Benchmark for Generalization in RL. 2018
		- https://contest.openai.com/2018-1/
		- https://github.com/openai/retro#gym-retro
		- Sonic benchmark
		- Classic video games to gym environment
	- **CoinRun**: K Cobbe, O Klimov, C Hesse, T Kim, J Schulman. Quantifying Generalization in Reinforcement Learning. ICML'19
		- https://openai.com/blog/quantifying-generalization-in-reinforcement-learning/
		- https://github.com/openai/coinrun
		- much simpler than traditional platformer games like Sonic the Hedgehog
		- Nature-CNN: 3-layer, PPO
		- IMPALA: better
		- Improve generalization: dropout, L2 regularization, data augmentation, environment stochasticity