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
- J Andreas, D Klein, S Levine, Modular Multitask Reinforcement Learning with Policy Sketches. ICML'17

## Transfer
- Resources:
	- https://github.com/AI-ON/Multitask-and-Transfer-Learning
- S Daftry, J. A Bagnell, M Hebert. Learning Transferable Policies for Monocular Reactive MAV Control. 2016
	- Task: AirDrone MAV flight, monocular reactive control
	- Deep domain adaptation
	- Dagger
	<img src="/RL/images/transfer/mav.png" alt="drawing" width="500"/>

## Domain Randomization
- https://lilianweng.github.io/lil-log/2019/05/05/domain-randomization.html
- CAD2RL: Real Single-Image Flight Without a Single Real Image. 2016
- Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba, Pieter Abbeel. Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. 2017
- How to pick the domain randomization parameters for sim-to-real transfer of reinforcement learning policies?

## OpenAI
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

## Misc
- K Kansky, T Silver, D A. Mély, M Eldawy, M Lázaro-Gredilla, X Lou, N Dorfman, S Sidor, S Phoenix, D George. Schema Networks: Zero-shot Transfer with a Generative Causal Model of Intuitive Physics. 2017