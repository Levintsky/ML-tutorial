# Multi-Task/Transfer Learning

## Sergey Levine
- lec-17, 18
- **Forward** transfer: train on one task, transfer to a new task
	- Just try it and hope for the best
	- Architectures for transfer: progressive networks
	- Finetune on the new task
- Multi-task transfer: train on many tasks, transfer to a new task
	- Generate highly randomized source domains
	- Model-based reinforcement learning
	- Model distillation
	- Contextual policies
	- Modular policy networks
- Multi-task meta-learning: learn to learn from many tasks
	- RNN-based meta-learning
	- Gradient-based meta-learning

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
- K Kansky, T Silver, D A. Mély, M Eldawy, M Lázaro-Gredilla, X Lou, N Dorfman, S Sidor, S Phoenix, D George. Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics. 2017