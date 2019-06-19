# Imitation Learning

## Behavior Cloning
- Problem: distribution mismatch
- A Giusti, J Guzzi, D C. Ciresan, F He, J P. Rodríguez, F Fontana, M Faessler, C Forster,
J Schmidhuber, G Di Caro, D Scaramuzza, L M. Gambardella. A Machine Learning Approach to Visual Perception of Forest Trails for Mobile Robots. 2015

## DAgger
- Interactive

## Meta, One-Shot
- Rocky Duan, One-Shot Imitation Learning, NIPS 2017
- Chelsea Finn, One-Shot Visual Imitation Learning
	- One-Shot Visual Imitation Learning via Meta-Learning: https://github.com/tianheyu927/mil
- Chelsea Finn, http://rail.eecs.berkeley.edu/nips_demo.html, MAML on RL
- Berkeley, One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning
- D Pathak, P Mahmoudieh, G Luo, P Agrawal, D Chen, Y Shentu, E Shelhamer, J Malik, A A. Efros, T Darrell. Zero-Shot Visual Imitation. ICLR'18

## Hard Atari Games
- Y Aytar, T Pfaff, D Budden, T L Paine, Z Wang, N Freitas. **Playing hard exploration games by watching YouTube (DeepMind)**, NIPS 2018
	- TDC (Temporal Distance Classification): predict temporal difference given two frames
	- CMC (Cross-Model Classification)
	- Cycle GAN (cross domain of different sequences)
	- Give positive reward in imitation learning if sequences are within some threshold after 16 frames

## Structured Prediction
- Mohanmmad Norouzi

## Teacher
- Teacher-Student Curriculum Learning, NIPS 2017

## Autonomous Driving
- End-to-end Driving via Conditional Imitation Learning

## Demonstration
- Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations
- Deep Q-learning from Demonstrations
- Leveraging Demonstrations for Deep Reinforcement Learning on Robotics Problems with Sparse Rewards
- Yueh-Hua Wu, Nontawat Charoenphakdee, Han Bao, Voot Tangkaratt, Masashi Sugiyama. Imitation Learning from Imperfect Demonstration. ICML'19

## Adversarial
- **GAIL**: Jonathan Ho, Stefano Ermon. Generative Adversarial Imitation Learning
	- Expert replay sample (s, a)
	- Policy sample (s', a')
	- Update discriminator D with gradient penalty
	- Update reward in rollouts with predicted reward from discrimator D as log(D(s',a'))
	- Update policy with the fake reward
	<img src="/RL/images/gail.png" alt="drawing" width="500"/>

- InfoGAIL: Interpretable Imitation Learning from Visual Demonstrations
- End-to-End Differentiable Adversarial Imitation Learning
- J. Ho, J. K. Gupta, and S. Ermon. Model-free imitation learning with policy optimization.
ICML 2016.

## Papers
- DAgger
	- Learning Transferable Policies for Monocular Reactive MAV Control
	- X. Guo, S. Singh, H. Lee. Deep Learning for Real-Time Atari Game Play Using Offline MCTS Planning.
- LSTM
	- Learning real manipulation tasks from virtual demonstrations using LSTM
	- Sim-to-Real Robot Learning from Pixels with Progressive Nets
- Model-Free Imitation Learning with Policy Optimization
- Interactive Control of Diverse Complex Characters
- Imitation Learning with Recurrent Neural Networks, Nyuyen 2016 

## Codes
- Deepak: TensorFlow code for zero-shot visual imitation by self-supervised exploration, ICLR 2018, https://github.com/pathak22/zeroshot-imitation