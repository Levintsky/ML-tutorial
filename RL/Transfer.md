# Multi-Task/Transfer Learning

## From Spinningups
- Progressive, uvfa; UNREAL; IU Agent; PathNet; MATL; learning an embedding space; HER;...

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
- **UVFA**: Schaul, T., Horgan, D., Gregor, K., and Silver, D. (2015a). Universal value function approximators. ICML'15
	- Multi-task Q-learning, Vg(s;theta) with g as the goal; 
	- 1+ goal we may try to achieve;
	- Every episode sample state goal pair (s0, g);
	- Different model architecture to represent goal and state\
		<img src="/RL/images/transfer/uvfa1.png" alt="drawing" width="450"/>
	- RL algorithm: Q-learning\
		<img src="/RL/images/transfer/uvfa2.png" alt="drawing" width="400"/>
- **Progressive-Nets**:
	- A Rusu, N Rabinowitz, G Desjardins, H Soyer, James Kirkpatrick, Koray Kavukcuoglu, Razvan Pascanu, Raia Hadsell. Progressive Neural Networks. 2016
		- They are schemes that can train NN's in an ensemble individually in a sequential fashion where an output of all trained NN's are stored and updated in an information center. The communication among NN’s is maintained indirectly through IC (information center), which ultimately reduces the interaction among the NNs
		- RL Alg: A3C
		- Everytime freeze previous learned knowledge;\
			<img src="/RL/images/transfer/progressive.png" alt="drawing" width="450"/>
	- Andrei A. Rusu, Mel Vecerik, Thomas Rothörl, Nicolas Heess, Razvan Pascanu, Raia Hadsell. Sim-to-Real Robot Learning from Pixels with Progressive Nets. CoRL'17
- **UNREAL**: Max Jaderberg, Volodymyr Mnih, Wojciech Marian Czarnecki, Tom Schaul, Joel Z Leibo, David Silver, Koray Kavukcuoglu. Reinforcement Learning with Unsupervised Auxiliary Tasks. 2016
	- https://github.com/miyosuda/unreal
- **IU Agent**: Serkan Cabi, Sergio Gómez Colmenarejo, Matthew W. Hoffman, Misha Denil, Ziyu Wang, Nando de Freitas. The Intentional Unintentional Agent: Learning to Solve Many Continuous Control Tasks Simultaneously. CoRL'17
	- Insight: the agent perceives a stream of rewards rti, indexed by i at time t. To learn the actor neural network parameterized by θ, we are interested in simultaneously maximizing the expected value of all tasks;
	- RL Alg: DDPG
	- To learn an intentional task, one will learn multiple unintentional (has to be off-policy);
		<img src="/RL/images/transfer/iu-agent.png" alt="drawing" width="450"/>
	- Experiments: Mujoco physics engine, stack object
	- When acting according to the policy associated with one of the hardest tasks, we are able to learn all other tasks off-policy
- **PathNet**: Chrisantha Fernando, Dylan Banarse, Charles Blundell, Yori Zwols, David Ha, Andrei A. Rusu, Alexander Pritzel, Daan Wierstra. PathNet: Evolution Channels Gradient Descent in Super Neural Networks. 2017
	-  Use agents embedded in the neural network whose task is to discover which parts of the network to re-use for new tasks;
	- MNIST, CIFAR, SVHN;
	- A3C on some games;
	- Algorithm from classification:
		- P genotypes (pathways) are initialized randomly, each genotype is at most a N by L matrix of integers, which describe the active modules in each layer in that pathway;
		- A binary tournament selection algorithm: A random genotype is chosen, and its pathway is trained for T epochs, its fitness being the negative classification error during that period of training;
		- A copy of the winning pathway’s genotype overwrites the losing pathways genotype.
	- A3C:
		- All 64 genotypes are evaluated in parallel;
		- Once the worker has finished T episodes, it chooses B other random genotypes and checks if any of those genotypes have returned a fitness of at least its own fitness
- J Andreas, D Klein, S Levine, Modular Multitask Reinforcement Learning with Policy Sketches. ICML'17
- **MATL**: Wulfmeier et al. Mutual Alignment Transfer Learning. 2017.
- Hausman et al, Learning an Embedding Space for Transferable Robot Skills. 2018.
- **HER**: Marcin Andrychowicz, Filip Wolski, Alex Ray, Jonas Schneider, Rachel Fong, Peter Welinder, Bob McGrew, Josh Tobin, Pieter Abbeel, Wojciech Zaremba. Hindsight Experience Replay. NIPS'17
	- Insight: if a goal is hard to achieve, then sparse reward impossible to train with; change goal to reachable make RL learn;
	- Multi-goal RL (similar to UVFA)
		<img src="/RL/images/algos/her.png" alt="drawing" width="500"/>

## Generalization, Overfitting
- Karl Cobbe, Oleg Klimov, Chris Hesse, Taehoon Kim, and John Schulman. Quantifying generalization in reinforcement learning. arxiv'18
- Jesse Farebrother, Marlos C. Machado, and Michael Bowling. Generalization and regularization in DQN. CoRR'18

## Domain Adaptation (DA)
- Resources:
	- https://github.com/AI-ON/Multitask-and-Transfer-Learning
- S Daftry, J. A Bagnell, M Hebert. Learning Transferable Policies for Monocular Reactive MAV Control. 2016
	- Task: AirDrone MAV flight, monocular reactive control
	- Deep domain adaptation
	- Dagger\
		<img src="/RL/images/transfer/mav.png" alt="drawing" width="500"/>
- Konstantinos Bousmalis, Alex Irpan, Paul Wohlhart, Yunfei Bai, Matthew Kelcey, Mrinal Kalakrishnan, Laura Downs, Julian Ibarz, Peter Pastor, Kurt Konolige, Sergey Levine, and Vincent Vanhoucke. Using simulation and domain adaptation to improve efficiency of deep robotic grasping. CoRR'17
- Shani Gamrian and Yoav Goldberg. Transfer learning for related reinforcement learning tasks via image-to-image translation. CoRR'18
- Stephen James, Paul Wohlhart, Mrinal Kalakrishnan, Dmitry Kalashnikov, Alex Irpan, Julian Ibarz, Sergey Levine, Raia Hadsell, and Konstantinos Bousmalis. Sim-to-real via sim-to-sim: Data-efficient robotic grasping via randomized-to-canonical adaptation networks. CoRR'18
- Transfer Value or Policy? A Value-centric Framework Towards Transferrable Continuous Reinforcement Learning. 2019

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