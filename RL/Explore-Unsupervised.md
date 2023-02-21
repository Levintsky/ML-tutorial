# Reinforcement Learning

## Basics
- Auxiliary tasks/reward to speed up RL;
- Classical:
	- Tabular/Linear; ε-greedy;
	- UCB;
	- MCTS;
	- Q-ensemble, Thompson sampling;
- Reward-Free Pre-Training (RFPT);
	- HER; Go-Explore;
- RL Tasks + Unsupervised Learning Supervision:
	- UL-Generative: density (PixelCNN, GPT-x, Bigan); MAE (BERT, Electra)
	- UL-Contrastive: CPC, SimCLR, MoCo, AMDIM, BYOL, SimSiam, DINO, Barlow Twins
	- RL + AE/VAE: UNREAL, world model, dreamer;
	- RL + Contrastive
- Intrinsic reward: Three types;
	- Knowledge-based: Surprise/unpredictability
		- ICM/VIME/plan-to-explore/disagreement/...;
	- Competence-based: Empowerment/Skills
		- MI: SSN4HRL, VIC, DIAYN, VALOR, DISCERN, DADS, VISR;
		- Asymmetric Self-Play (ASP);
	- Data-based: Entropy (i.e. coverage) of data collected;
		- Pseudo-count: CTS, PixelCNN, Hash, RND;
		- Entropy: MEPO, particle-based, ...
- Theory:
	- E Hazan, S Kakade, K Singh, A Soest. Provably Efficient Maximum Entropy Exploration. ICML'19
	- D Misra, M Henaff, A Krishnamurthy, J Langford. Kinematic State Abstraction and Provably Efficient Rich-Observation Reinforcement Learning. ICML'20
- Tutorials/Survey
	- C Colas, T Karch, O Sigaud, Ps Oudeyer. Autotelic Agents with Intrinsically Motivated Goal-Conditioned Reinforcement Learning: a Short Survey. 2020
	- ICML'21: A Srinivas, P Abbeel. Unsupervised Learning for Reinforcement Learning.
- https://blog.openai.com/reinforcement-learning-with-prediction-based-rewards/
- https://blog.openai.com/learning-montezumas-revenge-from-a-single-demonstration/

## Algorithmic Exploration (Complement RFPT)
- lec-17, 18 (CS-294, Sergey Levine)
- Insight: Optimism in Face of Uncertainty
	- Assume high reward for unvisitd states;
- Classic: Tabular/linear
	- Lai and Robbins’ Upper Confidence Bounds (UCB) 1985;
	- Sutton’s Dyna, 1990;
	- Schmidhuber’s Curiosity 1991;
	- Kaelbling’s Interval Exploration 1993;
	- Moore & Atkeson’s Prioritized Sweeping 1993;
	- Kaelbling, et al, RL Survey 1996;
	- Kearns and Singh, E3 2002;
	- Brafman and Tennenholtz, RMax 2002
	- Peter Auer’s UCB regret bounds, 2002;
	- Strehl and Littman, Model-based Interval Estimation (MBIE), 2008
- MCTS: check control-planning.md;
- UCB: (Upper Confidence Bounds)
    - a = argmax μa + √(2lnT/N(a))
    - Reg(T) ~ O(logT), provably as good as any algorithm
- Q Ensembles, Thompson Sampling: directly model posterior;
	- If conjugate prior/posterior: directly update;
	- Otherwise, approximate posterior θˆ:
		- Gibbs Sampling: θˆ0 init, change one θˆk at a time;
		- Laplace Approximation: approx around mode;
		- Langevin MC: dφt = ∇ln(g(φˆt))dt + √2 dBt
			- Iterate until stationary; (Euler discretization in practice)
		- Bootstrapping: resample from hypothetical history H=((x1,y1), ...) uniformly with replacement;
    - O Chapelle, L Li. An Empirical Evaluation of Thompson Sampling, NIPS'11
    - I Osband, C Blundell, A Pritzel, B V Roy. Deep Exploration via Bootstrapped DQN, NIPS'16
    	- Build C DQN agents using bootstrapped samples;
    		- Expensive, shared backbone with multi-heads Q(s, a) in practice;
    	- st, at=argmaxQ(s,a) from a random head; sample mask mt ~ M;
    	- (st, at, rt, st+1, mt) to replay buffer for learning;
	- Chen, Sidor, Abbeel, Schulman Q-UCB, 2017
		- a ∈ μ(st, a) + λσ(st, a), mean, std across ensembles;
    - D Russo, B V Roy, A Kazerouni, and I Osband. A Tutorial on Thompson Sampling. 2017
    - Mandel, Liu, Brunskill, Popovic. Thompson sampling over representation & parameters. IJCAI'16
    - Efficient Exploration through Bayesian Deep Q-Networks. NeurIPS workshop 2017
        - Use deep NN with last layer as Bayesian linear regression;
	- POLO: Lowrey, Rajeswaran, Kakade, Todorov, Mordatch. 2019
		- V(s) = log(∑.k exp(κV(s;θk)))
	- Lee, Laskin, Srinivas, Abbeel, SUNRISE 2020
		- Q(st, at) := rt + γmax.a Q(st+1, a)
			- if unseen (s, a), target Q inaccurate;
			- Weight |Q-Qt| with confidence score;
- Information Gain: bonus reward for reward uncertainty;
    - D Russo, B V Roy. Learning to Optimize via Information-Directed Sampling. NIPS'14
        - IG(z,y|a) = E_y[H(p(z))-H(p(z)|y)|a], how much we learn about z from action a;
        - y = ra, z = θa (parameters of model p(ra))
        - g(a) = IG(θa,ra|a), information gain about a;
        - ∆a = E[r(a∗)-r(a)], expected suboptimality of a;
        - Choose a based on argmin_a ∆a^2/g(a),
            - Numerator ∆a^2: avoid known suboptimal actions;
            - Denominator g(a): prefer uncertain actions;
- In Q-learning:
    - ∆w = α(Q-tgt − Qˆ(s,a;w))∇wQˆ(s,a;w)
    - ∆w = α(r(s,a) + Q-tgt − Qˆ(s,a;w))∇wQˆ(s,a;w)
        - r(s,a): uncertainty;

## RFPT
- HER [NeurIPS'17]:
	- Reward based on goal: R(s,a,g)
	- highsight relabel replay buffer to match final state;
- Go-Explore: UberAI. [NeurIPS'19]
    - Visiting a low count state -> revisit again in future;
    - Assume deterministic, divide states into cells (low-res img)
    - https://eng.uber.com/go-explore/
- SelfPlayer: Laskin, Rudes, Cang, Abbeel, 2021
	- ASP + GoExplore

## UL- 1. Generative (AE/VAE)
- Insight: Predict pixel color;
- UNREAL: M. Jaderberg et. al., Reinforcement Learning with Unsupervised Auxiliary Tasks. (2016)
	- Pixel control: maximizse change in pixel intensity
	- Reward prediction
- Higgins. DARLA: Improving Zero-Shot Transfer in RL. ICML'17
- World Models (Ha & Schmidhuber, 2018)
	- DeepMind. Unsupervised Predictive Memory in a Goal-Directed Agent.
- D Hafner, T Lillicrap, J Ba, M Norouzi. Dream to Control: Learning behaviors by latent imagination. 2019
- OpenAI. Learning to summarize from human feedback. NeurIPS'20
- SCAN: Learning Abstract Hierarchical Compositional Visual Concepts (DeepMind Blog)

## UL- 2. Contrastive
- Basics: RL + contrastive loss;
- P Sermanet, C Lynch, Y Chebotar, J Hsu, E Jang, S Schaal, S Levine. Time-Contrastive Networks: Self-Supervised Learning from Video. '17
- A Srinivas, M Laskin, P Abbeel. CURL: Contrastive Unsupervised Representations for Reinforcement Learning. ICML'20
- M Schwarzer, A Anand, R Goel, R Hjelm, A Courville, P Bachman. Data-Efficient Reinforcement Learning with Self-Predictive Representations. ICLR'21
	- BYOL fashion- with stop gradient;
	- Significant improvement
- Laskin, Lee, Stooke, Pinto, Abbeel, Srinivas. RAD: Reinforcement Learning with Augmented Data. NeurIPS'20
- DRQ: D Yarats, I Kostrikov, R Fergus. Image Augmentation Is All You Need: Regularizing Deep Reinforcement Learning from Pixels. ICLR'21
- A Stooke, K Lee, P Abbeel, M Laskin. Decoupling Representation Learning from Reinforcement Learning. ICML'21
	- Stop gradient for contrastive stream;
- SWAV+DRQ: D Yarats, R Fergus, A Lazaric, L Pinto.  Reinforcement Learning with Prototypical Representations. ICML'21
- FERM: A Zhan, R Zhao, L Pinto, P Abbeel, M Laskin. Learning Visual Robotic Control Efficiently with Contrastive Pre-training and Data Augmentation. NeurIPS Workshop'21
- Pre-training representations for data-efficient RL (Schwarzer & Rajkumar et al 2021)
	- Significant improvement

## UL- 3. Other Supervision
- ToMnet: Machine Theory of Mind. ICML'18
	- Task: Predict other agent
		- 1. next action (policy); 
		- 2. goal;
		- 3. trajectory.
	- VAE on character embedding: generate mean and variance;
	- DVIB for supervision;
- Applications (in robotics)
	- Deep Spatial Autoencoders for Visuomotor Learning (Finn et al 2015)

## Reward-Free-RL 1. Knowledge-based
- Error in Learned Dynamics Model:
	- Surprise/unpredictability/curiosity
	- Dynamics: p(st+1|st, at)
	- Inverse dynamics: p(at|st, st+1) ICM [Pathak, ICML'17]
- Legacy:
	- J Schmidhuber, Curious model-building control systems. IJCNN'91
	- Oudeyer and Kaplan. What is Intrinsic Motivation? A Typology of Computational Approaches. 2007
- Stadie, Levine, Abbeel. Incentivizing Exploration in Reinforcement Learning with Deep Predictive Models. 2015
- Achiam, Sastry, 2017
- ICM. Pathak. Curiosity-driven Exploration by Self-supervised Prediction. ICML'17
- Y Burda, H Edwards, D Pathak, A Storkey, T Darrell, A Efros. Large-Scale Study of Curiosity-Driven Learning. ICLR'19
	- Deeper dive on feature space?
	- https://pathak22.github.io/large-scale-curiosity/
- Intrinsic reward ~ Reduction in Epistemic Uncertainty 
	- Planning to be Surprised [Sun, Gomez, Schmidhuber, 2011]
	- VIME: [OpenAI, NIPS'16]
		- Bayesian-NN for dynamics;
		- r = H(Θ|ξt, at) - H(Θ|st+1, ξt, at)
		- 1. Eval: collect (st,at,st+1), KL, r′=r+ηKL;
		- 2. Update posterior by minimizing KL(q(θ|φ),q(θ));
		- 3. Standard RL to train policy with (s,a,s′,r′);
	- D Pathak, D Gandhi, A Gupta. Self-Supervised Exploration via Disagreement. ICML'19
	- R Sekar, O Rybkin, K Daniilidis, P Abbeel, D Hafner, D Pathak. Planning to Explore via Self-Supervised World Models. ICML'20
		- Planning in the Latent Space, Intrinsic Reward := Latent Disagreement
- I2A: DeepMind. Imagination-Augmented Agents for Deep Reinforcement Learning. NeurIPS'17
- Aleatoric Uncertainty?
- Legacy:
	- J Schmidhuber, Curious model-building control systems. IJCNN'91
	- J Schmidhuber. A Possibility for Implementing Curiosity and Boredom in Model-Building Neural Controllers. 1992
	- J. Schmidhuber, Formal theory of creativity, fun, and intrinsic motivation. 2010
	- Y. Sun, F. Gomez, and J. Schmidhuber, Planning to be surprised: Optimal Bayesian exploration in dynamic environments. AGI'11

## Reward-Free-RL 2. Competence
- Empowerment:
	- Measures the optionality a (perfect) agent can create over its future;
	- r = max.p(a.tn) I(A.tn; St+n)
- Designs: MI(z;τ) = H(z) - H(z|τ)
	- Which RL algorithm is used?
	- State-based or image-based (only DISCERN is image based)
	- Termination conditions of episodes affect learning signal
	- When state-based, which variables to include in τ?
- Maximize MI: 
	- SSN4HRL: r = logq(z|st; φ) - logp(z)
	- VIC: r = logq(z|sH; φ) - logp(z)
	- DIAYN: r = logq(z|st; φ) - logp(z)
	- VALOR: r = logq(z|s1:H; φ) - logp(z)
	- DISCERN: r = logq(z|s1:H; φ) - logp(z)
	- relative-VIC: r = logq(Ω|sT,s0;φ) - logq(Ω|s0;φ)
	- DADS: r = logq(st+1|st,z;φ) - logq(st+1|st;φ)
	- VISR: r = DIAYN + successor features;
- Asymmetric Self-Play (ASP)
	- Key Idea: two-player game, Alice challenges Bob, which encourages Alice to try new things (explore) and Bob to acquire skill
	- Alice set goal to Bob, Bob acts;
	- Alice intrinsic reward: max(0, tB-tA)
	- Bob reward: -tB
	- tA, tB: completion time;
- Klyubin, Polani, Nehaniv. Empowerment: A Universal Agent-Centric Measure of Control. '05
- T Jung, D Polani, and P Stone. Empowerment for continuous agent—environment systems. 2011.
- Salge, Glackin, Polani, Empowerment: An Introduction. 2013
- S Mohamed and D J Rezende. Variational information maximisation for intrinsically motivated reinforcement learning. NIPS'15
- VIC: DeepMind. Variational Intrinsic Control. ICLR'17
	- HRL: intermediate option set Ω, with π(a|s,Ω); final state sf1, sf2, ...
	- Loss-diversity: intrinsically different options I(Ω,sf|s0)
	- MI(sf; Ω|s0)
- SSN4HRL: C Florensa, Y Duan, P Abbeel. Stochastic Neural Networks for Hierarchical Reinforcement Learning. ICLR'17
- VALOR: J Achiam, H Edwards, D Amodei, P Abbeel. Variational Option Discovery Algorithms. 2018
- A Gupta, B Eysenbach, C Finn, S Levine. Unsupervised Meta-Learning for Reinforcement Learning. '18
	- Train with DIAYN;
	- logq(z|s) as reward;
- ASP: FAIR. Intrinsic Motivation and Automatic Curricula via Asymmetric Self-Play. ICLR'18
- DeepMind. Learning an embedding space for transferable robot skills. ICLR'18
	- MI(z; τ); latent skill z and trajectory τ;
- DIAYN: B Eysenbach, A Gupta, J Ibarz, S Levine. Diversity is All You Need: Learning Skills without a Reward Function. ICLR'19
- DISCERN: DeepMind. Unsupervised Control Through Non-Parametric Discriminative Rewards. ICLR'19
- VISR: DeepMind. Fast Task Inference with Variational Intrinsic Successor Features. ICLR'20
- DADS: A Sharma, S Gu, S Levine, V Kumar, K Hausman. Dynamics-Aware Unsupervised Discovery of Skills. 2020
- Scaled-ASP: OpenAI. Asymmetric Self-Play for Automatic Goal Discovery in Robotic Manipulation. '21
- MUSIC: Zhao, Gao, Abbeel, Tresp, Xu. MUSIC: Mutual Info State Intrinsic Control. 2021
	 - MI(s-agent; s-env);
	 - Incentivize the agent to visit agent states that affect the environment
- Relative VIC. DeepMind. Relative Variational Intrinsic Control. AAAI'21

## Reward-Free-RL 3. Data-based
- Entropy (i.e. coverage) of data collected
- Tabular MDPs: Count-based Exploration Bonus. [Strehl & Littman, 2008]
	- V(s) = max.a[R(s,a) + γV(s′) + βN(s,a)^-1/2]
- CTS: DeepMind. Skip Context Tree Switching. ICML'14
- Pseudo-count:
	- CTS [NeurIPS'16]: Unifying Count-based Exploration and Intrinsic Motivation.
		- learn p(s), change in P(s) as pseudo-count
		- Fitting: old p(si;θ), new p(si;θ′) with si added;
		- p(si;θ) = N(si)/n; p(si;θ′) = N(si)+1/n+1;
		- Solve N(si), n; (two unknowns, two equations)
		- r' = r + β/√(N(s)+ε)
	- Ostrovski [ICML'17]: Count-Based Exploration with Neural Density Models
		- Better perf with density model (PixelCNN);
	- Tang [NeurIPS'17]: #exploration
		- Hash to low-dimension space and count there;
	- J Fu, J D. Co-Reyes, S Levine. EX2: Exploration with Exemplar Models for Deep Reinforcement Learning, NeurIPS'17
	    - https://github.com/justinjfu/exemplar_models
	    - Exemplar-classifier for seen/unseen, classifier error to obtain density:
	        - p(s;θ) = (1-D(s))/D(s)
	        - Extra reward f(D(s))
	- RND [ICLR'19]: Burda. Exploration by Random Network Distillation.
		- Train a classifier for seen/new state;
- Directly Optimizing Entropy of Data Collected
	- Nearest neighbor: Singh, H., et al., 2003
		- H(s) ∝ ∑log(∥si-si.k∥)
	- MEPOL – Mutti, Pratissoli, Restelli, 2020
		- State entropy: r = H(s) = -E.s[logp(s)]
	- H Liu & P Abbeel. APT: Active Pre-Training. 2020
		- Particle based entropy reward;
	- Badia et al. Never Give Up: Learning Directed Exploration Strategies, 2020
		- Short-term exploration through particle-based entropy
		- Long-term exploration through RND
	- Reinforcement Learning with Prototypical Representations, Yarats, Fergus, Lazaric, Pinto, 2021
		- replay buffer for entropy estimates

## Intrinsic Reward
- Curious Agent
	- W Huang, I Mordatch, D Pathak. One Policy to Control Them All: Shared Modular Policies for Agent-Agnostic Control. ICML'20
		- https://github.com/huangwl18/modular-rl/
- Baldi et. al., Bayesian Surprise Attracts Human Attention. (2005)
- Driven by Compression Progress: A Simple Principle Explains Essential Aspects of Subjective Beauty, Novelty, Surprise, Interestingness, Attention, Curiosity, Creativity, Art, Science, Music, Jokes, Schmidhuber, 2008
- Complexity Gain: Graves et. al. Automated Curriculum learning For Neural Networks. (2017)
- Wang, J.X. et al. Evolving intrinsic motivations for altruistic behavior. 2018
- Sergey. Visual Reinforcement Learning with Imagined Goals. NIPS'18
- Learning to Play With Intrinsically-Motivated, Self-Aware Agents. NIPS'18
- S Singh. On Learning Intrinsic Rewards for Policy Gradient Methods. NIPS'18