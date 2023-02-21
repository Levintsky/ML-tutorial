# Imitation Learning

## Basics
- Problem setup:
	- Given expert demonstration, guess reward functions;
- Two approaches:
	- BC
	- IRL
- IRL:
	- Bi-level optimization: expensive;
		- Learn reward;
		- RL with learned reward;
	- Linear case:
		- Feature matching;
		- SVM learning;
- Sergey Levine (294 lec-16)

## Basics
- Legacy problem setup: feature mapping
	- Linear reward: r(s,a;ψ) = ∑ψi fi(s,a) = ψ†fi(s,a)
	- Pick ψ s.t. E.πrψ[f(s,a)] = E.π∗[f(s,a)]
- SVM trick: demonstration better than other trajectory by a margin
	- min∥ψ∥^2 s.t. ψ†E.π∗[f(s,a)] ≥ ψ†E.π[f(s,a)] + D(π, π∗)
- From control inference: policy probability
	- p(τ|O1:T) ∝ p(τ)exp[∑.t r(st,at)]
- MLE with parition function:
	- max.ψ 1/N ∑.i logp(τi|O1:T) = max.ψ 1/N ∑.i r(τi;ψ) - logZ
		- Z = ∫p(τ)exp(r(τ;ψ))dτ
	- ∇.ψ L = E.π∗[∇.ψ r] - E.π[∇.ψ r]
	- Let μt(st,at) ∝ β(st,at)α(st), we have:
	- ∇.ψ L = ∑μt ∇.ψr
- Max Ent IRL: r(st,at;ψ) = ψ†E[f] actually:
	- max.ψ H(π) s.t. E.πrψ[f(s,a)] = E.π∗[f(s,a)]

## Spinning Up
- Ziebart. Modeling Purposeful Adaptive Behavior with the Principle of Maximum Causal Entropy, 2010.
	- Contributions: Crisp formulation of maximum entropy IRL.
- Finn et al. Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization, 2016.
	- Algorithm: GCL.
- GAIL
- DeepMimic
- Variational Discriminator Bottleneck: Improving Imitation Learning, Inverse RL, and GANs by Constraining Information Flow, Peng et al, 2018.
	- Algorithm: VAIL.
- One-Shot High-Fidelity Imitation: Training Large-Scale Deep Nets with RL, Le Paine et al, 2018.
	- Algorithm: MetaMimic.

## Misc
- P Sharma, D Pathak, A Gupta. Third-Person Visual Imitation Learning via Decoupled Hierarchical Controller. NeurIPS'19

## IL
- Behavior Cloning: naive supervised;
	- Two notable success stories:
		- Pomerleau, NIPS'89: ALVINN;
		- Summut et al., ICML'92: Learning to fly in flight simulator;
	- Problem: distribution mismatch; (always pretty well in practice)
		- Compounding error; ∝ ε^T2
	- S Ross, A Bagnell. Efficient Reductions for Imitation Learning. AISTATS'10
	- J Schmidhuber, et. al. A Machine Learning Approach to Visual Perception of Forest Trails for Mobile Robots. 2015
	- Stanford. What Matters in Learning from Offline Human Demonstrations for Robot Manipulation. CoRL'21
- DAgger
	- Interactive from expert;
	- S Ross, G J Gordon, and D Bagnell. A reduction of imitation learning and structured prediction to no-regret online learning. AISTATS'11
	- X. Guo, S. Singh, H. Lee. Deep Learning for Real-Time Atari Game Play Using Offline MCTS Planning. NIPS'14
		- Imitation learning from MCTS
- Meta, One-Shot
	- Y Duan, M Andrychowicz, B Stadie, J Ho, J Schneider, I Sutskever, P Abbeel, W Zaremba, One-Shot Imitation Learning, NIPS'17
		- Task: 7-DOF Fetch robotic arm to stack; B on A, C on B, ...
		- Training: pairs of demonstrations for a subset of all tasks, watch first, perform on second from initial
		- Test time: one demonstration
		- pi(a|o, d), d: demonstration, d: (o1, a1), (o2, a2), ...
		- Temporal dropout: throw away 95%
		- **Attention** model on demonstration: salient frame;
		- **Attention** model and current task;
			<img src="/RL/images/imitation/1shot-il1.png" alt="drawing" width="500"/>
			<img src="/RL/images/imitation/1shot-il2.png" alt="drawing" width="600"/>
	- C Finn, T Yu, T Zhang, P Abbeel, S Levine, One-Shot Visual Imitation Learning. CoRL'17
		- MAML on RL, cost: directly map state to action;
		- http://rail.eecs.berkeley.edu/nips_demo.html
		- https://github.com/tianheyu927/mil \
			<img src="/RL/images/imitation/maml1.png" alt="drawing" width="500"/>
			<img src="/RL/images/imitation/maml2.png" alt="drawing" width="400"/>
			<img src="/RL/images/imitation/maml3.png" alt="drawing" width="600"/>
	- T Yu, C Finn, A Xie, S Dasari, T Zhang, P Abbeel, S Levine. One-Shot Imitation from Observing Humans via Domain-Adaptive Meta-Learning.
		- https://sites.google.com/view/daml
		- https://github.com/tianheyu927/mil
			<img src="/RL/images/imitation/daml.png" alt="drawing" width="500"/>
	- D Pathak, P Mahmoudieh, G Luo, P Agrawal, D Chen, Y Shentu, E Shelhamer, J Malik, A A. Efros, T Darrell. Zero-Shot Visual Imitation. ICLR'18
		- https://pathak22.github.io/zeroshot-imitation/
		- Tasks: 1. complex rope manipulation with a Baxter robot; 2. navigation in previously unseen office environments with a TurtleBot;
			<img src="/RL/images/imitation/0shot-il1.png" alt="drawing" width="500"/>
- Hard Atari Games
	- Y Aytar, T Pfaff, D Budden, T L Paine, Z Wang, N Freitas. Playing hard exploration games by watching YouTube (DeepMind), NIPS'18
		- Task: MONTEZUMA’S REVENGE, PITFALL! and PRIVATE EYE
		- Input: unaligned videos from multiple sources
		- Map to common representation using self-supervised objectives constructed over both time and modality (vision, sound, ...);\
			<img src="/RL/images/imitation/youtube-il1.png" alt="drawing" width="600"/>
		- Embed a **single YouTube video** in this representation to construct a **reward function** that encourages an agent to **imitate human gameplay**
		- TDC (Temporal Distance Classification): predict temporal difference y given two frames v, w: dt [0],[1],[2],[3−4],[5−20],[21−200]
		- CMC (Cross-Model Classification): audio a, video frame v, (v, a, y)\
			<img src="/RL/images/imitation/youtube-il2.png" alt="drawing" width="600"/>

		- Cycle GAN (cross domain of different sequences): two sequences (v1, v2, ...), (w1, w2, ...), for vi, find NN wj, then find NN vk, |i-k| should be small;\
			<img src="/RL/images/imitation/youtube-il3.png" alt="drawing" width="600"/>
		- 1-shot imitation: Give positive reward in imitation learning if sequences are within some threshold after 16 frames;\
			<img src="/RL/images/imitation/youtube-il4.png" alt="drawing" width="300"/>
		- System: IMPALA
- Structured Prediction
	- Mohanmmad Norouzi
- Teacher
	- Teacher-Student Curriculum Learning, NIPS 2017
- Demonstration
	- **DeepMimic**: X B Peng, P Abbeel, S Levine, M v d Panne. DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills. SIGRAPH'18
		- Problem setup: goal-directed reinforcement learning with data
		- Input: a character model, a corresponding set of kinematic reference motions (target poses {qt}), and a task defined by a reward function;
		- Output: controller for imitation pi(at|st, gt);
		- State: the relative positions of each link with respect to the root (designated to be the pelvis), their rotations expressed in quaternions, and their linear and angular velocities. All features are computed in the character’s local coordinate frame;
		- Action: PD controller (proportional-derivative);
		- Network: Gaussian\
			<img src="/RL/images/imitation/deepmimic1.png" alt="drawing" width="450"/>
			<img src="/RL/images/imitation/deepmimic2.png" alt="drawing" width="450"/>
	- A Rajeswaran, V Kumar, A Gupta, G Vezzani, J Schulman, E Todorov, S Levine. Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations
	- Deep Q-learning from Demonstrations. RSS'18
	- Leveraging Demonstrations for Deep Reinforcement Learning on Robotics Problems with Sparse Rewards
	- **NAC**: Y Gao, H Xu, J Lin, F Yu, S Levine, T Darrell. Reinforcement Learning from Imperfect Demonstrations. ICML'18
		- An auxiliary pool of D (demonstration) to warm up, then AC;
		- NAC: Normalized Actor-Critic; similar to soft policy gradient (with max-entropy term);
		- Normalizing the Q-function over the actions
		- Previously, PCL (bridging the gap...) learns Q from demonstration;\
			<img src="/RL/images/imitation/nac1.png" alt="drawing" width="400"/>
			<img src="/RL/images/imitation/nac2.png" alt="drawing" width="400"/>
	- Y Wu, N Charoenphakdee, H Bao, V Tangkaratt, M Sugiyama. Imitation Learning from Imperfect Demonstration. ICML'19
- Multi-Agent IL:
	- Legacy:
		- Chernova, Sonia and Veloso, Manuela. Multiagent collaborative task learning through imitation.
	- H M Le, Y Yue, P Carr, and P Lucey. Coordinated multi-agent imitation learning. ICML'17
		- https://github.com/hoangminhle/MultiAgent-ImitationLearning
		- Entropy regularized cost:\
			<img src="/RL/images/imitation/cmail1.png" alt="drawing" width="500"/>
		- Alternating policy and latent structure model;\
			<img src="/RL/images/imitation/cmail2.png" alt="drawing" width="500"/>
		- Line 3-5: Learn (core part)\
			<img src="/RL/images/imitation/cmail3.png" alt="drawing" width="500"/>
		- Line 6: Structure-learning\
			<img src="/RL/images/imitation/cmail4.png" alt="drawing" width="500"/>
		- Line 2: Role-assignment\
			<img src="/RL/images/imitation/cmail4.png" alt="drawing" width="500"/>
	- E Zhan, S Zheng, Y Yue, P Lucey. Generative Multi-Agent Behavioral Cloning. ICML'18
		<img src="/RL/images/imitation/gmabc.png" alt="drawing" width="500"/>
		
		- Novel problem setting: K-agents, U=[U1,...,UK] K demonstrations, C: context;
		- [pi1, pi2, ... piK], each has a specific role;
		- Role based indexing: the roles are undefined, unobserved, and could change dynamically within the same sequence;
		- Variational-RNN;	
- Papers
	- LSTM
		- R. Rahmatizadeh, P. Abolghasemi, A. Behal, and L. Bölöni. Learning real manipulation tasks from virtual demonstrations using LSTM. arxiv'16
		- A A. Rusu, M Vecerik, T Rothörl, N Heess, R Pascanu, R Hadsell. Sim-to-Real Robot Learning from Pixels with Progressive Nets. CoRL'17
	- J Ho, J K. Gupta, S Ermon. Model-Free Imitation Learning with Policy Optimization. ICML'16
	- I Mordatch, K Lowrey, G Andrew, Z Popovic, E V. Todorov. Interactive Control of Diverse Complex Characters. NIPS'15
	- K Nyuyen. Imitation Learning with Recurrent Neural Networks, arxiv'16 
- Codes
	- Deepak: TensorFlow code for zero-shot visual imitation by self-supervised exploration, ICLR 2018,
		- https://github.com/pathak22/zeroshot-imitation

## Inverse Reinforcement Learning
- Basics:
	- Given expert demonstration, infer reward function;
	- Linear case:
		- R(s)=wx(s)
		- V(s0;π) = E[Σ_t γ^tR(st)|s0] = wμ(π), with μ(π) discounted weighted frequency of states;
		- Expert optimal, so: wμ(π∗) >= wμ(π) for other policies;
- Legacy:
	- P Abbeel, A Ng. Apprenticeship Learning via Inverse Reinforcement Learning. ICML'04
	- B D. Ziebart, A Maas, J Bagnell, and A K. Dey. Maximum Entropy Inverse Reinforcement Learning. AAAI'08
- Unclassified:
	- M Wulfmeier, P Ondruska, I Posner. Maximum Entropy Deep Inverse Reinforcement Learning. ICML'16
	- **GCL**: C Finn, S Levine, P Abbeel. Guided Cost Learning: Deep Inverse Optimal Control via Policy Optimization. ICML'16
		- Many costs can explain same demo: 1. max-margin; 2. probabilistic (GCL);
		- Solving inner loop control: 1. inner-loop MDP (requires dynamics); 2. sampling (GCL);
		- Build on IOC [Ziebart'08]
		- Framework:\
			<img src="/RL/images/irl/gcl1.png" alt="drawing" width="500"/>
		- Algorithm: the sampling q(tau) is critical:\
			<img src="/RL/images/irl/gcl2.png" alt="drawing" width="500"/>
	- Wulfmeier et al. Deep Maximum Entropy Inverse Reinforcement Learning. MaxEnt inverse RL using deep reward functions. arXiv'16
	- Lifelong Inverse Reinforcement Learning. NIPS'18
- Adversarial
	- C Finn, P Christiano, P Abbeel, S Levine. A Connection Between Generative Adversarial Networks, Inverse Reinforcement Learning, and Energy-Based Models. 2016
		- Generator: sample; data: demonstration
		- Discriminator:\
			<img src="/RL/images/irl/irl-gan.png" alt="drawing" width="500"/>
	- **GAIL**: J Ho, S Ermon. Generative Adversarial Imitation Learning. NIPS'16
		<img src="/RL/images/irl/irl-gail.png" alt="drawing" width="500"/>
		<img src="/RL/images/irl/gail.png" alt="drawing" width="500"/>
		- Implementation on Mujoco (main-loop):
		- 1. Agent collect samples -> batch; (st, at, mt, st+1, rt) with customized reward as -log(D(s',a'))
		- 2. Update parameters
		- 2.1 (reward, action, state, mask) from batch (step 1);
		- 2.2 Estimate advantage;
		- 2.3 Update discriminator D with gradient penalty: 1 iteration
			- Input: [state, action] of expert, sample
		- 2.4 Minibatch PPO;
		- 2.4.1 Estimate advantage: Adv=Q(s,a)-V(s), enhanced with GAE;
		- 2.4.2 PPO:
			- Value loss: L = E[|V(s)-R|^2]
			- Policy loss: L = E[-Surr logπ(s,a)], with surrogate clamped advantage as in PPO;
	- J. Ho, J. K. Gupta, and S. Ermon. Model-free imitation learning with policy optimization. ICML'16.
	- **InfoGAIL**: Y Li, J Song, S Ermon. InfoGAIL: Interpretable Imitation Learning from Visual Demonstrations. NIPS'17
		- Multimodal, assign each demonstration to each expert (fixed number)
	- **MGAIL**: N Baram, O Anschel, I Caspi, S Mannor. End-to-End Differentiable Adversarial Imitation Learning. ICML'17
	- J Fu, K Luo, S Levine. Learning Robust Rewards with Adversarial Inverse Reinforcement Learning. ICLR'18
- Reward Shaping
	- A. Y. Ng, D. Harada, and S. Russell. Policy invariance under reward transformations: Theory and application to reward shaping. ICML'99\
		<img src="/RL/images/reward-shaping.png" alt="drawing" width="500"/>
	- I. Mordatch, E. Todorov, and Z. Popovic. Discovery of complex behaviors through contact-invariant optimization. TOG'12
	- Y. Tassa, T. Erez, and E. Todorov. Synthesis and stabilization of complex behaviors through online trajectory optimization. IROS'12