# RL-Basics

## Resources
- Courses
	- DeepMind/UCL: David Silver
	- Berkeley cs294: Sergey Levine
	- From OR point of view
		- http://www.columbia.edu/~sa3305/
	- Standord cs234;
- Good Summaries
	- Algorithms: https://github.com/tigerneil/awesome-deep-rl
	- L. P. Kaelbling, M. L. Littman, and A. W. Moore. Reinforcement learning: A survey. JAIR, 1996.
- Books
	- Reinforcement Learning: An Introduction
		- Assignment: https://github.com/ShangtongZhang/reinforcement-learning-an-introduction
	- Richard Bellman. Dynamic Programming. Princeton University Press, 1957.
- https://spinningup.openai.com/en/latest/spinningup/keypapers.html
- https://github.com/navneet-nmk/pytorch-rl
- https://github.com/sweetice/Deep-reinforcement-learning-with-pytorch
- Chinese:
	- https://zhuanlan.zhihu.com/sharerl
	- https://zhuanlan.zhihu.com/p/68205048
- Open-AI Baselines:
	- https://github.com/openai/baselines
	- A2C, ACER, ACKTR / DDPG / DQN / GAIL / HER
	- PPO1 (Multi-CPU using MPI), PPO2 (Optimized for GPU), TRPO
- **rlkit**
	- https://github.com/vitchyr/rlkit
	- RIG, TDMs, HER, DQN, SAC, TD3
- Pytorch libraries:
	- DQN Adventure: https://github.com/higgsfield/RL-Adventure
	- Ye Yuan (CMU): https://github.com/Khrylx/PyTorch-RL
	- Shangtong Zhang: https://github.com/ShangtongZhang/DeepRL
	- Ilya Kostrikov (NYU): https://github.com/ikostrikov
	- Rainbow: https://github.com/Kaixhin/Rainbow
	- A3C LSTM: https://github.com/dgriff777/rl_a3c_pytorch
- Tensorflow libraries:
	- https://github.com/brendanator/atari-rl
	- https://github.com/steveKapturowski/tensorflow-rl
	- https://github.com/tensorflow/agents
- Shane Gu: https://github.com/shaneshixiang/rllabplusplus
- Berkeley RL: https://github.com/rll/rllab
- GA3C: https://github.com/NVlabs/GA3C
- Model-free RL from Spinningup:
	- DQN: DQN, DRQN; Duel DQN; PER; Rainbow;
	- PG: A3C, TRPO, GAE, PPO, ACKTR, ACER, SAC;
	- DPG: DPG, DDPG, TD3;
	- Distributional: C51, QR-DQN, IQN, Dopamine;
	- Action-dependent: Q-prop, Stein control, mirage;
	- PCL: PCL, Trust-PCL;
	- Other continuous combine pg and q: PGQL, Reactor, IPG, equivalence between...;
	- Evolutionary: ES;

## Misc
- Visual Memory for Robust Path Following (Sergey Levine, Jitendra Malik). NIPS'18
- Fast deep reinforcement learning using online adjustments from the past (DeepMind). NIPS'18
- **Randomized Prior Functions for Deep Reinforcement Learning**. NIPS'18
- **Approximate Knowledge Compilation by Online Collapsed Importance Sampling**. NIPS'18
- **Randomized Prior Functions for Deep Reinforcement Learning**. NIPS'18
- UD-RL
	- Jurgen Schmidhuber. Reinforcement Learning Upside Down: Don’t Predict Rewards - Just Map Them to Actions. 2019
	- Rupesh Kumar Srivastava, Pranav Shyam, Filipe Mutz, Wojciech Jaśkowski, Jürgen Schmidhuber. Training Agents using Upside-Down Reinforcement Learning. 2019

## Applications on RL
- System Optimization
	- E. Ipek, O. Mutlu, José, and R. Caruana. Self-optimizing memory controllers: A reinforcement learning approach. ISCA, 2008.
- Web Browse
	- E Z Liu, K Guu, P Pasupat, T Shi, P Liang. Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration. ICLR'18
- Computer Vision (Attention)
	- V Mnih, N Heess, A Graves, K Kavukcuoglu. Recurrent Models of Visual Attention. NIPS'14
	- J. L. Ba, V. Mnih, and K. Kavukcuoglu. Multiple object recognition with visual attention. ICLR, 2015.
	- P. Sermanet, A. Frome, and E. Real. Attention for fine-grained categorization. ICLR'15
	- D Jayaraman, K Grauman. Learning to look around: Intelligently Exploring Unseen Environments for Unknown Tasks. CVPR'18
- NTM
	- W. Zaremba and I. Sutskever. Reinforcement learning neural turing machines. arxiv, 2015.
- Recommendation
	- Lihong Li, Wei Chu, John Langford, Robert E. Schapire. A Contextual-Bandit Approach to Personalized News Article Recommendation, WWW'10
	- Fighting Boredom in Recommender Systems with Linear Reinforcement Learning. NIPS'18
	- **Horizon**: Jason Gauci, Edoardo Conti, Yitao Liang, Kittipat Virochsiri, Yuchen He, Zachary Kaden, Vivek Narayanan, Xiaohui Ye, Zhengxing Chen, Scott Fujimoto. Horizon: Facebook's Open Source Applied Reinforcement Learning Platform. 2019
- Misc
	- Data center cooling using model-predictive control. NIPS'18 Tutorial
- Unclassified
	- Learning Temporal Point Processes via Reinforcement Learning. NIPS'18
	- Reinforcement Learning of Theorem Proving. NIPS'18

## Poker/Chess
- Chess
	- Chess:
		- M. Campbell, A. J. Hoane, and F. hsiung Hsu. Deep blue. Artificial intelligence, 2002.
	- Go
		- Legacy:
			- M. Enzenberger. The integration of a priori knowledge into a go playing neural network. URL: http://www.markus-enzenberger.de/neurogo.html, 1996.
			- M. Enzenberger. an open-source framework for board games and go engine based on monte carlo tree search. IEEE Transactions on Computational Intelligence and AI in Games, 2010.
			- **Pachi**: P. Baudis and J. loup Gailly. Pachi: State of the art open source go program. Advances in Computer Games, 2012.
			- D. Silver, Temporal-Difference Search in Computer Go, 2012
			- C. Maddison, A. Huang, I. Sutskever, and D. Silver. Move evaluation in go using deep convolutional neural networks. arxiv, 2014.
			- C. Clark and A. Storkey. Teaching deep convolutional neural networks to play go. ICML'15.
		- Y. Tian and Y. Zhu. Better computer go player with neural network and long- term prediction. arxiv, 2015.
		- **AlphaGo**: D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. van den Driessche, J. Schrittwieser, I. Antonoglou, V. Panneershelvam, M. Lanctot, S. Dieleman, J. Nham, N. Kalchbrenner, I. Sutskever, T. Lillicrap, M. Leach, K. Kavukcuoglu, T. Graepel, and D. Hassabis. Mastering the game of go with deep neural networks and tree search. Nature'14
		- **AlphaGo Zero**: D Silver, J Schrittwieser, K Simonyan, I Antonoglou, A Huang, A Guez, T Hubert, L Baker, M Lai, A Bolton, Y Chen, T Lillicrap, F Hui, L Sifre, G v d Driessche, T Graepel, D Hassabis. Mastering the game of Go without human knowledge. Nature'17
		- The system:\
			<img src="/RL/images/chess/agz1.png" alt="drawing" width="600"/>
		- MCTS:\
			<img src="/RL/images/chess/agz2.png" alt="drawing" width="600"/>
			<img src="/RL/images/chess/agz3.png" alt="drawing" width="400"/>
		- **AlphaZero**: D Silver, T Hubert, J Schrittwieser, I Antonoglou, M Lai, A Guez, M Lanctot, L Sifre, D Kumaran, T Graepel, T Lillicrap, K Simonyan, D Hassabis. A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play. Science'19
		- PhoenixGo: https://github.com/Tencent/PhoenixGo
		- MuGo: https://github.com/brilee/MuGo
		- Leela: https://github.com/gcp/leela-zero
		- MiniGo: https://github.com/tensorflow/minigo
		- Y Tian, J Ma, Q Gong, S Sengupta, Z Chen, J Pinkerton, L Zitnick. ELF OpenGo: an analysis and open reimplementation of AlphaZero. ICML'19
	- Gammon: Gerald Tesauro. Temporal difference learning and td-gammon. Communications of the ACM, 38(3):58–68, 1995.
- Poker (Texas Hod'em)
	- Check Game Theory;
- Rubik's Cube
	- Basics:
		- How to solve the rubik's cube - beginners method. https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/.
	- Mathematics:
		- Daniel Kunkle and Gene Cooperman. Twenty-six moves suffice for rubik’s cube. ISSAC'07
		- Silviu Radu. Rubik’s cube can be solved in 34 quarter turns. http://cubezzz.dyndns.org/drupal/?q=node/view/92, Jul 2007.
		- Michael Reid. Superflip requires 20 face turns. http://www.math.rwth-aachen.de/~Martin.Schoenert/Cube-Lovers/michael_reid__superflip_requires_20_face_turns.html, Jan 1995.
		- Tomas Rokicki. Twenty-two moves suffice for rubik’s cubeR. The Mathematical Intelligencer, 32(1):33–40, 2010.
		- Tomas Rokicki. God’s number is 26 in the quarter-turn metric. http://www.cube20.org/qtm/, Aug 2014
		- Tomas Rokicki, Herbert Kociemba, Morley Davidson, and John Dethridge. The diameter of the rubik’s cube group is twenty. SIAM Review, 56(4):645–670, 2014.
		-  Morwen Thistlethwaite. Thistlethwaite’s 52-move algorithm. https://www.jaapsch.net/puzzles/thistle.htm, Jul 1981.
	- Legacy:
		- Peter Lichodzijewski and Malcolm Heywood. The rubik cube and gp temporal sequence learning: an initial study. In Genetic Programming Theory and Practice VIII, pages 35–54. Springer, 2011.
	-  **Korf**:
		- Andrew Brown. Rubik’s cube solver. https://github.com/brownan/Rubiks-Cube-Solver, 2017.
		- Deepening A* search.
		- Richard E. Korf. Finding optimal solutions to rubik’s cube using pattern databases. AAAI’97/IAAI’97, pages 700–705. AAAI
	- **Kociemba**:
		- Two-phase algorithm details. http://kociemba.org/math/imptwophase.htm.
		- Maxim Tsoy. Kociemba. https://github.com/muodov/kociemba, 2018.
	- Deep-learning:
		- Robert Brunetto and Otakar Trunda. Deep heuristic-learning in the rubik’s cube domain: an experimental evaluation. 2017.

## HRL
- From Spinningup
	- STRAW, FUN, HIRO;
- Legacy
	- Hierarchical Learning in Stochastic Domains: Preliminary Results
	- Amy McGovern and Andrew G Barto. Automatic discovery of subgoals in reinforcement learning
	using diverse density. 2001.
	- Martin Stolle and Doina Precup. Learning options in reinforcement learning. In International Symposium on Abstraction, Reformulation, and Approximation, pp. 212–223. Springer, 2002.
	- A Tutorial on Bayesian Optimization of Expensive Cost Functions, with Application to Active User Modeling and Hierarchical Reinforcement Learning 2010
	- David Silver and Kamil Ciosek. Compositional planning using optimal option models.
- HRL
	- A summary: https://thegradient.pub/the-promise-of-hierarchical-reinforcement-learning/
	- A Deep Hierarchical Approach to Lifelong Learning in Minecraft, AAAI'17
	- T Shu, C Xiong, R Socher. Hierarchical and Interpretable Skill Acquisition in Multi-task Reinforcement Learning. ICLR'18
	- Tejas D Kulkarni, Karthik R Narasimhan, Ardavan Saeedi, and Joshua B Tenenbaum. Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation. NIPS'16
	- S Zheng, Y Yue and P Lucey. Generating long-term trajectories using deep hierarchical networks. NIPS'16.
		- Long-term planning;
	- Kulkarni, Tejas D, Narasimhan, Karthik, Saeedi, Ardavan, and Tenenbaum, Josh. Hierarchical deep reinforcement learning: Integrating temporal abstraction and intrinsic motivation. NIPS'16
	- E Zhan, Stephan Zheng, Generative Multi-Agent Behavioral Cloning
	- **HIRO**: Ofir Nachum, Shixiang Gu, Honglak Lee, Sergey Levine. Data-Efficient Hierarchical Reinforcement Learning. NIPS'18
	- Honglak Lee. Hierarchical Reinforcement Learning for Zero-shot Generalization with Subtask Dependencies. NIPS'18
	- Andrew Levy, George Konidaris, Robert Platt, Kate Saenko. Learning Multi-Level Hierarchies with Hindsight. ICLR'19
	- Zhen-Jia Pang, Ruo-Ze Liu, Zhou-Yu Meng, Yi Zhang, Yang Yu, Tong Lu. On Reinforcement Learning for Full-length Game of StarCraft. 2019
	- **MPH**: Alexander Pashevich, Danijar Hafner, James Davidson, Rahul Sukthankar, Cordelia Schmid. Modulated Policy Hierarchies. 2019
- Joint Skills and Meta-Controller
	- P Dayan, Peter and G Hinton. Feudal reinforcement learning. NIPS'93.
	- Pierre-Luc Bacon and Doina Precup. The option-critic architecture. NIPSW'15
	- Pierre-Luc Bacon, Jean Harb, and Doina Precup. The Option-Critic Architecture, AAAI 2017
	- Nicolas Heess, Greg Wayne, Yuval Tassa, Timothy Lillicrap, Martin Riedmiller, and David Silver. Learning and transfer of modulated locomotor controllers. 2016
	- **STRAW**: Alexander Vezhnevets, Volodymyr Mnih, John Agapiou, Simon Osindero, A Graves, O Vinyals, K Kavukcuoglu. Strategic Attentive Writer for Learning Macro-Actions. NIPS'16
		- Stick to the plan (commit)\
			<img src="/RL/images/hrl/straw1.png" alt="drawing" width="500"/>
		- Attention model:\
			<img src="/RL/images/hrl/straw2.png" alt="drawing" width="500"/>
		- Algorithm:\
			<img src="/RL/images/hrl/straw3.png" alt="drawing" width="400"/>
		- Experiments: 2D-maze; Atari;
	- **FUN**: A S Vezhnevets, S Osindero, T Schaul, N Heess, M Jaderberg, D Silver, K Kavukcuoglu. Feudal Network for Hierarchical Reinforcement Learning. ICML'17
		- https://github.com/dmakian/feudal_networks
		<img src="/RL/images/hrl/fun.png" alt="drawing" width="500"/>
	- Sanjay Krishnan, Roy Fox, Ion Stoica, and Ken Goldberg. Ddco: Discovery of deep continuous options for robot learning from demonstrations. ICLR'17
	- Carlos Florensa, Yan Duan, and Pieter Abbeel. Stochastic neural networks for hierarchical reinforcement learning. 2017
	- K Frans, J Ho, X Chen, P Abbeel, J Schulman. Meta Learning Shared Hierarchies. ICLR'18
	- Main problem:
		- the meta-policy does not select "bad" options, so these options do not receive any reward signal to improve.
		- Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. 2017
- Options
	- Daniel J Mankowitz, Timothy A Mann, and Shie Mannor. Time-regularized interrupting options. ICML'14
	- Marlos C. Machado, Clemens Rosenbaum, Xiaoxiao Guo, Miao Liu, Gerald Tesauro, Murray Campbell. Eigenoption Discovery through the Deep Successor Representation, ICLR'18

## Interpretable RL
- A Mott, D Zoran, M Chrzanowski, D Wierstra, D Rezende. Towards Interpretable Reinforcement Learning Using Attention Augmented Agents. NIPS'19
	<img src="/RL/images/interpretable/interp-rl.png" alt="drawing" width="500"/>

## Memory
- From OpenAI spinning-up:
	- **MFEC**: Blundell et al. Model-Free Episodic Control. 2016
	- **NEC**: Pritzel et al. Neural Episodic Control. 2017
	- **Neural Map**: Parisotto and Salakhutdinov. Neural Map: Structured Memory for Deep Reinforcement Learning. 2017
	- **MERLIN**: Wayne et al. Unsupervised Predictive Memory in a Goal-Directed Agent. 2018
	- **RMC**: Santoro et al. Relational Recurrent Neural Networks. 2018

## Safety RL
- Legacy:
	- **CMDP**: Altman, Eitan. Constrained Markov Decision Processes. 1999
	- Uchibe, Eiji and Doya, Kenji. Constrained reinforcement learning from intrinsic and extrinsic rewards. ICDL'07
		- Heuristic CMDP: gradient projection
	- Moldovan, Teodor Mihai and Abbeel, Pieter. Safe Exploration in Markov Decision Processes. ICML'12
- Chow, Yinlam, Ghavamzadeh, Mohammad, Janson, Lucas, and Pavone, Marco. Risk-Constrained Reinforcement Learning with Percentile Risk Criteria. JMLR'15
	- **Primal-dual** subgradient method for risk-constrained reinforcement learning 
	- Takes policy gradient steps on an objective that trades off return with risk
	- Simultaneously learning the trade-off coefficients (dual variables).
- Bou Ammar, Haitham, Tutunov, Rasul, and Eaton, Eric. Safe Policy Search for Lifelong Reinforcement Learning with Sublinear Regret. ICML'15
	- Theoretic
- Amodei et al. Concrete Problems in AI Safety, 2016. 
	- Contribution: establishes a taxonomy of safety problems, serving as an important jumping-off point for future research. We need to solve these!
	- 1. Avoiding Negative Side Effects;
	- 2. Avoiding Reward Hacking;
	- 3. Scalable Oversight;
	- 4. Safe Exploration;
	- 5. Robustness to Distribution Shift;
- Shalev-Shwartz, Shai, Shammah, Shaked, and Shashua, Amnon. Safe, Multi-Agent, Reinforcement Learning for Autonomous Driving. 2016
	- avoid the problem of enforcing constraints on parametrized policies by decomposing 'desires' from trajectory planning;
	- the neural network policy learns desires for behavior
	- while the trajectory planning algorithm (which is not learned) selects final behavior and enforces safety constraints;
- **LFP**: Christiano et al. Deep Reinforcement Learning From Human Preferences, 2017.
- **CPO**: Achiam et al. Constrained Policy Optimization. 2017.
	- near-constraint satisfaction at each iteration\
		<img src="/RL/images/safety/cpo.png" alt="drawing" width="400"/>
- Held, David, Mccarthy, Zoe, Zhang, Michael, Shentu, Fred, and Abbeel, Pieter. Probabilistically Safe Policy Transfer. ICRA'17
- **HIRL**: Saunders et al. Trial without Error: Towards Safe Reinforcement Learning via Human Intervention, 2017.
- **Intrinsic-fear**: Lipton, Zachary C., Gao, Jianfeng, Li, Lihong, Chen, Jianshu, and Deng, Li. Combating Deep Reinforcement Learning’s Sisyphean Curse with Intrinsic Fear.
- **Leave-No-Trace**: Eysenbach et al. Leave No Trace: Learning to Reset for Safe and Autonomous Reinforcement Learning, 2017.
- Chow, Y., Ghavamzadeh, M., Janson, L., and Pavone, M. Risk-constrained reinforcement learning with percentile risk criteria. JMLR'17
- **Safety-Layer**: Dalal et al. Safe Exploration in Continuous Action Spaces. ICML'18. 
	- Algorithm: DDPG+Safety Layer.
	- Problem setup: bounded CMDP, safe control in physical systems\
		<img src="/RL/images/safety/safety-layer1.png" alt="drawing" width="400"/>
	- Plug-in for DDPG:\
		<img src="/RL/images/safety/safety-layer2.png" alt="drawing" width="400"/>
	- The safety layer;\
		<img src="/RL/images/safety/safety-layer3.png" alt="drawing" width="400"/>
- Y Chow, O Nachum, E Duenez-Guzman, M Ghavamzadeh. A Lyapunov-based Approach to Safe Reinforcement Learning. NIPS'18
	- CMDP (Constrained MDP), with upper-bound cost we should satisfy;
	- safe policy iteration (SPI) and safe value iteration (SVI);
	- safe DQN, safe DPI;
- Constrained Cross-Entropy Method for Safe Reinforcement Learning. NIPS'18
- Yinlam Chow, Ofir Nachum, Aleksandra Faust, Edgar Duenez-Guzman, Mohammad Ghavamzadeh. Lyapunov-based Safe Policy Optimization for Continuous Control. ICML'19
	- Lagrange method: max_theta min_lambda c(xt,at) + lambda (D(xt|pi,x0)-d)
	- Lyapunov constraint: feasibility set;
- Robust Control
	- **LQG-Robust**: Sarah Dean, Nikolai Matni, Benjamin Recht, and Vickie Ye. Robust Guarantees for Perception-Based Control. 2019
		- https://github.com/modestyachts/robust-control-from-vision
		- Affine error-profile model;
		- Model: MBRL (LQR)
		- Evaluated on synthetic example CARLA

## Reproducibility, Analysis, and Critique
- Continuous control: Y Duan, X Chen, R Houthooft, J Schulman, P Abbeel. Benchmarking Deep Reinforcement Learning for Continuous Control. ICML'16
	- https://github.com/rll/rllab
- Islam et al. Reproducibility of Benchmarked Deep Reinforcement Learning Tasks for Continuous Control. 2017.
- Henderson et al. Deep Reinforcement Learning that Matters. 2017.
- Henderson et al. Where Did My Optimum Go?: An Empirical Analysis of Gradient Descent Optimization in Policy Gradient Methods. 2018.
- Ilyas et al. Are Deep Policy Gradient Algorithms Truly Policy Gradient Algorithms? 2018.
- Mania et al. Simple Random Search Provides a Competitive Approach to Reinforcement Learning. 2018.
- Wang et al. Benchmarking Model-Based Reinforcement Learning. 2019.

## RTS
- Starcraft
	- https://github.com/TorchCraft/TorchCraft
	- Starcraft II:
		- https://deepmind.com/blog/alphastar-mastering-real-time-strategy-game-starcraft-ii/
		- https://github.com/deepmind/pysc2
		- Challenge
			- Game theory: StarCraft is a game where, just like rock-paper-scissors, there is no single best strategy.
			- Imperfect information
			- Long term planning
			- Real time
			- Large action space
		- Network
			- Transformer Torso (Deep reinforcement learning with relational inductive biases, ICLR'19)
			- Deep LSTM core
			- Auto-regressive policy head with a pointer network
			- a centralised value baseline (Counterfactual Multi-Agent Policy Gradients AAAI'18)
			- Warm-start: supervised learning with human data
			- Population-based training;
	- FAIR: Forward Modeling for Partial Observation Strategy Games - A StarCraft Defogger. NIPS'18
		- **POMDP**
	- Jonas Gehring (FAIR)
		- Starcraft
		- LSTM for each unit;
		- Train stage I: off-policy;
		- Stage II: on-policy;		
- Dota
	- **OpenAI Five**:
		- https://openai.com/blog/openai-five/
		- **Long time horizons**: Dota games run at 30 frames per second for an average of 45 minutes, resulting in 80,000 ticks per game. OpenAI Five observes every fourth frame, yielding 20,000 moves;
		- **Partially-observed state**: Units and buildings can only see the area around them. The rest of the map is covered in a fog hiding enemies and their strategies.
		- **High-dimensional, continuous action space**: In Dota, each hero can take dozens of actions, and many actions target either another unit or a position on the ground. 170,000 possible actions per hero (not all valid each tick, such as using a spell on cooldown)
		- **High-dimensional, continuous observation space**: Dota is played on a large continuous map containing ten heroes, dozens of buildings, dozens of NPC units, and a long tail of game features such as runes, trees, and wards. Valve’s Bot API as 20,000 (mostly floating-point) numbers representing all information a human is allowed to access
		- Pure from selfplay.\
			<img src="/RL/images/rts/openai-five.png" alt="drawing" width="600"/>
		- **Model structure**: Each of OpenAI Five’s networks contain a single-layer, 1024-unit LSTM that sees the current game state (extracted from Valve’s Bot API) and emits actions through several possible action heads.
		- **Exploration**
		- **Coordination**
		- Distributed training system: **Rapid**, could be applied to any gym environment
			- Workers **push** data of game play
			- Optimizer: P100 GPU, PPO with Adam, batch size 4096, BPTT 16 time steps, NCCL to average gradients (previously with MPI allreduce)
			- Eval workers: 2500 CPUs, v.s. hardcoded scripted bots and self\
				<img src="/RL/images/rts/openai-five-rapid.png" alt="drawing" width="600"/>
		- **Difference versus humans**: 150-170 actions per minute;
		- **Binary rewards can give good performance.**
		- **Creep blocking can be learned from scratch.**
		- **We’re still fixing bugs**

## Navigation
- GA3C: https://github.com/tgangwani/GA3C-DeepNavigation
- pycolab: https://github.com/deepmind/pycolab
- Platform, Challenge and Benchmark:
	- VizDoom 2016
	- DeepMind Lab 2016
	- HoME 2017
	- House 3D: Y Wu, Y Wu, G Gkioxari, Y Tian. Building generalizable agents with a realistic and rich 3D environment. 2018
		- https://github.com/facebookresearch/House3D
		- https://github.com/jxwuyi/HouseNavAgent
	- Chalet 2018
	- AI2-THOR 2017
	- **DeepMind-Lab**: Learning to navigate in complex environments. ICLR'17
	- Realistic: Matterport, AdobeIndoorNav, Stanford 2D-3D-S, Scannet, Gibson, MINOS
	- **StreetLearn**: P Mirowski, A Banki-Horvath, K Anderson, D Teplyashin, K Hermann, M Malinowski, M Grimes, K Simonyan, K Kavukcuoglu, A Zisserman, R Hadsell. The StreetLearn Environment and Dataset. 2019
		- Google Street View;
		- http://streetlearn.cc
	- Baidu XWorld (Zihang Dai): https://github.com/zihangdai/pytorch_xworld
- Language:
	- Speaker-Follower Models for Vision-and-Language Navigation. NIPS'18
- VIN
	- Good summaries:
		- https://zhuanlan.zhihu.com/p/25515755
		- https://zhuanlan.zhihu.com/p/24478944
	- **VIN**: Aviv Tamar, Yi Wu, Garrett Thomas, Sergey Levine, Pieter Abbeel. Value Iteration Network. NIPS'16
		<img src="/RL/images/navigation/vin1.png" alt="drawing" width="600"/>
		<img src="/RL/images/navigation/vin2.png" alt="drawing" width="600"/>
	- **GVIN**: S Niu, S Chen, H Guo, C Targonski, M Smith, J Kovačević. Generalized Value Iteration Networks: Life Beyond Lattices. AAAI'18
		<img src="/RL/images/navigation/gvin.png" alt="drawing" width="600"/>
	- Sources:
		- https://github.com/kentsommer/pytorch-value-iteration-networks
- **Learning to Act by Predicting the Future**, ICLR 2017
	- Alexey Dosovitskiy, Vladlen Koltun
	- Win the 2nd Vizdoom competition
- Y Wu, Y Tian. Training Agent for First-Person Shooter Game with Actor-Critic Curriculum Learning. ICLR'17
	- VizDoom, known map;
	- Batch A3C;
- A Banino, C Barry, B Uria, C Blundell, T Lillicrap, P Mirowski, A Pritzel, M Chadwick, T Degris, J Modayil, G Wayne, H Soyer, F Viola, B Zhang, R Goroshin, N Rabinowitz, R Pascanu, C Beattie, S Petersen, A Sadik, S Gaffney, H King, K Kavukcuoglu, D Hassabis, R Hadsell, D Kumaran. Vector-based Navigation using Grid-like Representations in Artificial Agents. Nature'18
- P Mirowski. et.al. Learning to navigate in cities without a map. NIPS'18
- T Chen, S Gupta, and A Gupta. Learning exploration policies for navigation. 2019
- Devendra Singh Chaplot, Saurabh Gupta, A Gupta, R Salakhutdinov. Modular Visual Navigation using Active Neural Mapping. ICLR'19
- Devendra Singh Chaplot, Dhiraj Gandhi, Saurabh Gupta, Abhinav Gupta, Ruslan Salakhutdinov. Learning to Explore using Active Neural SLAM. ICLR'20
	- https://github.com/devendrachaplot/Neural-SLAM
	- https://www.cs.cmu.edu/~dchaplot/projects/neural-slam.html
	- Insight: combination of classics and deep learning, analytical path planners with learned SLAM module;
	- Winner of the CVPR 2019 Habitat PointGoal Navigation Challenge;
- K Hermann, M Malinowski, P Mirowski, A Banki-Horvath, K Anderson, R Hadsell. Learning to Follow Directions in Street View. AAAI'20
	- Input: front-view images (Google street-view), instructions; output: policy;
	- CNN-RNN;
