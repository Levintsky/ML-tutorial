# Deep Learning based Recommendation

## Google
- **Wide-and-Deep**: Heng-Tze Cheng et. al. Wide & Deep Learning for Recommender Systems. 2016
	- Joint training;
	- **FTRL** algorithm: Flow-the-regularized-leader with L1
	- Ensemble of wide and deep, sigm(w-wide wide + w-deep deep + b)
	- Application: apps recommendation

## RL
- Deisenroth, M. P., Fox, D., and Rasmussen, C. E. Gaussian processes for data-efficient learning in robotics and control. PAMI'15
- Nagabandi, A., Kahn, G., Fearing, R. S., and Levine, S. Neural network dynamics for model-based deep reinforcement
learning with model-free fine-tuning. 2017
- Clavera, I., Nagabandi, A., Fearing, R. S., Abbeel, P., Levine, S., and Finn, C. Learning to adapt: Meta-learning for model-based control. 2018
- X Chen, S Li, H Li, S Jiang, Y Qi, L Song. Generative Adversarial User Model for Reinforcement Learning Based Recommendation System. ICML'19
	- Model-free: data-instensive, user gives up fast
	- Model-based: better
	- Minimax learning framework
	- GAN to simulate user behavior: better user model, better and simpler reward function than manual designed;
	- Cascade-DQN
<img src="/Recommendation/images/minimax.png" alt="drawing" width="500"/>
<img src="/Recommendation/images/cascade-dqn.png" alt="drawing" width="500"/>
