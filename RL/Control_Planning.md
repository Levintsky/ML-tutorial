# Optimal Control and Planning

## Basics
- Discrete MCTS (EECS-294, lec-10)
	- UCT
- Linear case: LQR
	- Linear known dynamics, quadratic cost function;
	- DDP backward;
	- iLQR: locally approximate via Taylor expansion;
- Control as an Inference (lec-15)

## Monte-Carlo Tree Search
- Approach:
	- Find a leaf sl using TreePolicy(s1)
	- Evaluate the leaf using DefaultPolicy(sl)
	- Update all values in tree between s1 and sl, take best action from s1;
	- UCT: Score(st) = Q(st)/N(st) + 2C √(2lnN(st-1)/N(st))
- Legacy
	- G. Tesauro and G. R. Galperin. On-line policy improvement using monte-carlo search. NIPS'96.
	- L. Kocsis and C. Szepesvàri. Bandit based monte-carlo planning. ECML'06.
	- S. Gelly and D. Silver. Combining online and offline knowledge in uct. ICML'07.
	- R Coulom. Efficient selectivity and backup operators in monte-carlo tree search. 2008
- Survey:
	- C. Browne, et. al. A survey of monte carlo tree search methods. 2012
- New, SOA
	- X. Guo, S. Singh, H. Lee, R. Lewis, and X. Wang. Deep learning for real-time atari game play using offline monte-carlo tree search planning. NIPS'14
		- Imitation learning from MCTS
	- T Anthony, Z Tian, and D Barber. Thinking fast and slow with deep learning and tree search, 2017.

## Control as Inference
- Problem setup:
	- State x, action u; Minimize cost:
	- C(x0,u0.T) = ∑.x p(x1:T|x0,u0.T-1) ∑t R(xt,ut,xt+1)
	- Imagine a free form Markov process qt(xt+1|xt)
		- Optimal: ψ(x1:T|x0) = q(x1:T|x0)exp(-∑R(xt,t))
	- Goal: minimize KL(p|ψ)
		- Loss: KL(p|q) + ⟨R⟩
- Basic idea: planning as inference;
	- A graphical model: p(Ot|st,at) ∝ exp(r(st,at))
	- Check HMM forward-backward algorithm (message-passing);
- Forward message:
	- Posterior αt = p(st|O1:t-1)
	- Given optimality before, where I am in state space;
- Backward message:
	- Given what will happen after t, what is the optimality if we should take (st at).
	- p(Ot=1|st,aT) := exp(r(st,at))
	- β(st) = p(O.t:T|st)
	- β(st,at) = p(O.t:T|st,at)
	- π(at|st) ∝ β(st,at)/β(st)
	- for t=T-1 to 1:
		- β(st,at) = p(Ot|st,at)E_st+1[β(st+1)]
		- β(st) = E_at[β(st,at)]
- Generalized/Soft Q-learning:
	- Q(s, a) := log[β(st, at)]
		- := logβ(st,at) = r(st, at) + logE.st+1|st,at[exp(V(st+1))]
	- V(st) := logβ(st) 
		- := log∫exp(Q(st,at))dat
	- Policy: π(at|st, O1:T) = β(st,at)/β(st)
- Forward message: αt(st) = p(st) given O1:t-1;
	- p(st|O1:T) ∝ αt(st)βt(st)
- Variational lower bound:
	- logp(x) >= Eq(z)[logp(x,z)-logq(z)]
		- gap is KL(q(z)|p(z))
	- Let observation: x=O1:T, z=(s1:T, a1:T)
	- logp(O1:T) >= Eq(s,a)[Σr(st,at)-logq(at|st)], (b/c r(st,at)=logp(Ot|st,at))
	-  = Σt Eq(st,at)[r(st,at)+H(q(at|st))] (max-entropy)
- Q-learning with soft optimality
	- Take ai and observe (si,ai,si',ri), add to buffer R;
	- Sample minibatch {sj,aj,sj',rj} from R;
	- Target yj = rj + γsoftmax_aj'Q(sj',aj';φ') with target network Q(;φ')
	- Regression bp: φ -= αΣ_j dQ(sj,aj;φ)/dφ (Q(sj,aj;φ)-yj)
	- Update target net φ' every N-step or Polyak;
- Policy gradient with soft optimality:
	- J(θ) = Σt Eπ[r(st,at)]+Eπ[H(π(at|st))]
- Graphical models:
	- Ziebart, B. D., Maas, A. L., Bagnell, J. A., and Dey, A. K. Maximum entropy inverse reinforcement learning. AAAI'08
	- Toussaint, M. Robot trajectory optimization using approximate inference. ICML'09
	- Ziebart. Modeling interaction via the principle of maximal causal entropy: connection between soft optimality and maximum entropy modeling. 2010
	- Rawlik, Toussaint, Vijaykumar. On stochastic optimal control and reinforcement learning by approximate inference: temporal difference style algorithm with soft optimality. RSS'12
	- H Kappen, V Gomez, M Opper. Optimal control as a graphical model inference problem: frames control as an inference problem in a graphical model. AAAI'13
- Modern soft optimality
	- O'Donoghue, B., Munos, R., Kavukcuoglu, K., and Mnih, V. PGQ: Combining policy gradient and Q-learning. 2016
	- Fox, R., Pakman, A., and Tishby, N. Taming the noise in reinforcement learning via soft updates. UAI'16
	- Haarnoja, Tang, Abbeel, L., Reinforcement Learning with Deep Energy-Based Policies. ICML'17
	- **PCL**: Nachum, Norouzi, Xu, Schuurmans. Bridging the gap between value and policy based reinforcement learning. NIPS'17
		- soft q-learning; n-step as path-consistent;
	- Schulman, Abbeel, Chen. Equivalence between policy gradients and soft Q-learning. 2017
	- **Trust-PCL**: O Nachum, M Norouzi, K Xu, D Schuurmans. Trust-PCL: An Off-Policy Trust Region Method for Continuous Control. ICLR'18
	- Levine. Reinforcement Learning and Control as Probabilistic Inference: Tutorial and Review. 18

## Legacy
- Proto-value Functions: A Laplacian Framework for Learning Representation and Control in Markov Decision Processes, 2007

## Unclassified
- DeepMind. Memory-based control with recurrent neural networks. NIPS'15
- DeepMind. Model-Free Episodic Control
- M Moczulski, K Xu, A Courville, K Cho. A Controller-Recognizer Framework: How necessary is recognition for control? ICML'16
- Y Chebotar, K Hausman, M Zhang, G Sukhatme, S Schaal, S Levine. Combining Model-Based and Model-Free Updates for Trajectory-Centric Reinforcement Learning. ICML'17
- DeepMind. The Predictron: End-To-End Learning and Planning, ICML'17
- **OptNet**: B Amos and Z Kolter. OptNet: Differentiable Optimization as a Layer in Neural Networks. ICML'17
- G Farquhar, T Rocktäschel, M Igl, Sh Whiteson. TreeQN and ATreeC: Differentiable Tree-Structured Models for Deep Reinforcement Learning. ICLR'18
- P Abbeel. Learning Plannable Representations with Causal InfoGAN. NIPS'18
- Berkeley. Variational Inverse Control with Events: A General Framework for Data-Driven Reward Definition. NIPS'18
- **MPC**: B Amos, I Rodriguez, J Sacks, B Boots, Z Kolter. Differentiable MPC for End-to-end Planning and Control. 2019
	- https://locuslab.github.io/mpc.pytorch/
