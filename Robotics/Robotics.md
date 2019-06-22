# Robotics, Continuous Control

## Berkeley
- C. Finn, X. Y. Tan, Y. Duan, T. Darrell, S. Levine, and P. Abbeel. Learning visual feature spaces for robotic manipulation with deep spatial autoencoders. arxiv, 2015.
- Sim-to-Real Robot Learning from Pixels with Progressive Nets
- A Machine Learning Approach to Visual Perception of Forest Trails for Mobile Robots, 2015
- S. Levine, C. Finn, T. Darrell, P. Abbeel. End-to-End Training of Deep Visuomotor Policies, JMLR 2016
- Learning Hand-Eye Coordination for Robotic Grasping with Large-Scale Data Collection, 2016
- One-Shot Learning of Manipulation Skills with Online Dynamics Adaptation and Neural Network Priors
- Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates, ICRA 2017
- F. Sadeghi and S. Levine. CAD2RL: real single-image flight without a single real image. 2017
- Supersizing Self-supervision: Learning to Grasp from 50K Tries and 700 Robot Hours

## OpenAI
- Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. 2017
- Y Duan, M Andrychowicz, B C. Stadie, J Ho, J Schneider, I Sutskever, P Abbeel and W Zaremba. One-Shot Imitation Learning. 2017
- X. B. Peng, M. Andrychowicz, W. Zaremba, and P. Abbeel. Sim-to-real transfer of robotic control with dynamics randomization. CoRR'17
- **Dactyl**: Marcin Andrychowicz et.al. Learning Dexterous In-Hand Manipulation, 2018
	- https://blog.openai.com/learning-dexterity/
	- Train models:
		- A LSTM RL to predict action (control policy);
		- A CNN to predict object pose;
		- Combine pose estimation and control policy from multiple camera inputs;
		<img src="/Robotics/images/dexterity4.png" alt="drawing" width="400"/>

		- Trained with PPO;
		- **Policy actions**: correspond to desired joints angles relative to the current ones, **discrete action spaces work much better.**
		- **Reward**: at timestep t is r(t) = d(t) − d(t+1), desired and current object orientations. additional reward of 5 whenever a goal is achieved and a reward of −20.
		<img src="/Robotics/images/dexterity.png" alt="drawing" width="600"/>
		<img src="/Robotics/images/dexterity3.png" alt="drawing" width="600"/>

	- Problem setup: Manipulate objects using a Shaow Dexterous Hand
	- **Hardware**: a humanoid robotic hand with 24 degrees of freedom (DoF) actuated by 20 pairs of agonist–antagonist tendons
	<img src="/Robotics/images/dexterity2.png" alt="drawing" width="600"/>

	- **Simulator**: simulate the physical system with the MuJoCo physics engine; use Unity2 to render the images for training the vision based pose estimator.
	- modify the basic version of our simulation to a distribution over many simulations that foster transfer

	- Same distributed system as OpenAI Five;
	- Distributed workers collect experience at large scale;
	<img src="/Robotics/images/dexterity4.png" alt="drawing" width="600"/>

- OpenAI Robotics Symposium 2019 with a lot of talks:
	- https://openai.com/blog/symposium-2019/
	- Learning From Play, Pierre Sermanet, Google Brain
	- Doing for Our Robots What Nature Did for Us, Leslie Kaelbling, MIT
	- Treating People as Optimizers in Human-Robot Interaction, Anca Dragan, UC Berkeley
	- Social-Emotional Intelligence in Human-Robot Interactions, Jin Joo Lee, MIT / Amazon
	- What Should Be Learned, Chris Atkeson, CMU

## Dataset
- MuJoCo: A physics engine for model-based control, IROS 2012
- ShadowRobot. ShadowRobot Dexterous Hand. https://www.shadowrobot.com/products/dexterous-hand/, 2005.
	- five fingers with a total of 24 degrees of freedom
- Simulation only:
	- Y. Bai and C. K. Liu. Dexterous manipulation using both palm and fingers. ICLR'14
	- I. Mordatch, Z. Popovic, and E. Todorov. Contact-invariant optimization for hand manipulation. SCA'12

## Legacy
- L.-J. Lin. Reinforcement learning for robots using neural networks. No. CMU-CS-93-103. Carnegie-Mellon Univ Pittsburgh PA School of Computer Science, 1993.