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
- Uniform randomization:
	- F Sadeghi, S Levine. CAD2RL: Real Single-Image Flight Without a Single Real Image. 2016
	- J Tobin, R Fong, A Ray, J Schneider, W Zaremba, P Abbeel. Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. 2017
		- A recurrent policy can adapt to different physical dynamics
		- Random: Mass and dimensions of objects; Mass and dimensions of robot bodies; Damping, kp, friction of the joints; Gains for the PID controller (P term); Joint limit; Action delay; Observation noise.
	- **Dactyl**: Marcin Andrychowicz et.al. Learning Dexterous In-Hand Manipulation, 2018
		- At first, barely survive 5 seconds without dropping
		- DR: evolved work surprisingly well;
- DR as optimization
	- Q Vuong, S Vikram, H Su, S Gao, H Christensen. How to pick the domain randomization parameters for sim-to-real transfer of reinforcement learning policies? 2019
		- Insight: domain randomization as an optimization problem; learn a distribution on of source domain which a policy is trained on can achieve maximal performance in real world;
		- https://github.com/quanvuong/domain_randomization
- Guided DR:
	- Optimization for Task Performance
		- N Ruiz, S Schulter, M Chandraker. Learning To Simulate. ICLR'19
			- NAS: considered the task feedback as reward in RL problem and proposed a RL-based method
			- Exp: Toy example (GMM) for binary classification;
			- Exp: CARLA;
			- Exp: Semantic Segmentation;
			<img src="/RL/images/transfer/learn-to-sim.png" alt="drawing" width="600"/>
		- W Yu, K Liu, G Turk. Policy Transfer with Strategy Optimization. ICLR'19
			- Evolution based; CMA-ES (covariance matrix adaptation evolution strategy)
		- **SDR**: A Prakash, S Boochoon, M Brophy, D Acuna, E Cameracci, G State, O Shapira, S Birchfield. Structured Domain Randomization: Bridging the Reality Gap by Context-Aware Synthetic Data.
		- **Meta-Sim**: A Kar, A Prakash, M Liu, E Cameracci, J Yuan, M Rusiniak, D Acuna, A Torralba, S Fidler. Meta-Sim: Learning to Generate Synthetic Datasets. ICCV'19
			- GAN to cover **appearance gap**;
			- The synthetic scenes are parameterized by a hierarchy of objects with properties (i.e., location, color) as well as relationships between objects;
			- The hierarchy is specified by a probabilistic scene grammar akin to structure domain randomization;
			- A model G is trained to augment the distribution of scene properties s by following:
				- Learn the prior first: pre-train G to learn the identity function G(s)=s.
				- Minimize MMD loss between the real and sim data distributions. This involves backpropagation through non-differentiable renderer. The paper computes it numerically by perturbing the attributes of G(s).
				- Minimize REINFORCE task loss when trained on synthetic data but evaluated on real data. Again, very similar to AutoAugment.
			<img src="/RL/images/transfer/meta-sim1.png" alt="drawing" width="500"/>
			<img src="/RL/images/transfer/meta-sim2.png" alt="drawing" width="500"/>
			<img src="/RL/images/transfer/meta-sim3.png" alt="drawing" width="600"/>
			<img src="/RL/images/transfer/meta-sim4.png" alt="drawing" width="500"/>
	- Match Real Data Distribution
		- **SimOpt**: Y Chebotar, A Handa, V Makoviychuk, M Macklin, J Issac, N Ratliff, D Fox. Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience. 2019
			- https://sites.google.com/view/simopt
			- trained under an initial randomization distribution Pϕ(ξ) first, getting a policy πθ,Pϕ.
			- Then this policy is deployed on both simulator and physical robot to collect trajectories τξ and τreal respectively.
			- The optimization objective is to minimize the discrepancy between sim and real trajectories
			- SimOpt also has to solve the **tricky problem** of how to propagate gradient through non-differentiable simulator
			<img src="/RL/images/transfer/simopt.png" alt="drawing" width="500"/>
		- **RCAN**: S James, P Wohlhart, M Kalakrishnan, D Kalashnikov, A Irpan, J Ibarz, S Levine, R Hadsell, K Bousmalis. Sim-to-Real via Sim-to-Sim: Data-efficient Robotic Grasping via Randomized-to-Canonical Adaptation Networks. 2019
			- a nice combination of DA and DR for end-to-end RL tasks.
			- An image-conditional GAN (cGAN) is trained in sim to translate a domain-randomized image into a non-randomized version (aka “canonical version”).
			- Later the same model is used to translate real images into corresponding simulated version so that the agent would consume consistent observation as what it has encountered in training.
			- Still, the underlying assumption is that the distribution of domain-randomized sim images is broad enough to cover real-world samples.
			<img src="/RL/images/transfer/rcan.png" alt="drawing" width="500"/>
	- Guided by Data in Simulator
		- S Zakharov, W Kehl, S Ilic. DeceptionNet: Network-Driven Domain Randomization. 2019
			- With the recognition network fixed, maximize the difference between the prediction and the labels by applying reversed gradients during backpropagation. So that the deception module can learn the most confusing tricks.
			- With the deception modules fixed, train the recognition network with input images altered.
			<img src="/RL/images/transfer/DeceptionNet.png" alt="drawing" width="500"/>
		- **ADR**: B Mehta, M Diaz, F Golemo, C Pal, L Paull. Active Domain Randomization. 2019
			- ADR searches for the most informative environment variations within the given randomization ranges,  measured as the discrepancies of policy rollouts in randomized and reference (original, non-randomized) environment instances. 
			- Sounds a bit like SimOpt? Well, noted that SimOpt measures the discrepancy between sim and real rollouts, while ADR measures between randomized and non-randomized sim, avoiding the expensive real data collection part.
			- 1. Given a policy, run it on both reference and randomized envs and collect two sets of trajectories respectively.
			- 2. Train a discriminator model to tell whether a rollout trajectory is randomized apart from reference run. The predicted logp (probability of being randomized) is used as reward. The more different randomized and reference rollouts, the easier the prediction, the higher the reward.
				- The intuition is that if an environment is easy, the same policy agent can produce similar trajectories as in the reference one. Then the model should reward and explore hard environments by encouraging different behaviors.
			- 3. The reward by discriminator is fed into Stein Variational Policy Gradient (SVPG) particles, outputting a diverse set of randomization configurations.
			<img src="/RL/images/transfer/adr.png" alt="drawing" width="500"/>

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