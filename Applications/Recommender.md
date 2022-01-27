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

## NIPS'19
- Ruiyi Zhang, Tong Yu, Yilin Shen, Hongxia Jin, Changyou Chen. Reward Constrained Interactive Recommendation with Natural Language Feedback
- Xueying Bai, Jian Guan, Hongning Wang. Model-Based Reinforcement Learning with Adversarial Training for Online Recommendation
- Han Zhu, Daqing Chang, Ziru Xu, Pengye Zhang, Xiang Li, Jie He, Han Li, Jian Xu, Kun Gai. Joint Optimization of Tree-based Index and Deep Model for Recommender Systems

## Summaries
- https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2650760136&idx=2&sn=afc75d6bf614bc7929b6ea9cb1abb260&chksm=871aa7b6b06d2ea0129ec7b06bf7b2448c3a55d485d6b80a066d622709066242fe7c925160c3&scene=21#wechat_redirect
- https://zhuanlan.zhihu.com/p/64722876

## Summary
- Content based
- Collaborative Filtering
- Hybrid (Content + CF)
- Relation and Bucket
- Repetitive

## Design
- Text preprocessing: tf-idf, ...
- Text clustering: DBScan
