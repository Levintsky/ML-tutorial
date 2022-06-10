# Graphical Models

## Basics
- DGM:
	- Bayesian net:
	- Learning:
	- Inference:	
- UGM:
	- MRF, CRF;
	- Learning:
	- Inference:
- Inference:
	- Exact inference:
		- VE;
		- Factor graph;
		- Sum-product/max-product;
	- Variational inference (check VI);
- Markov:
	- HMM:
		- Inference:
			- Maginal each state: forward/backward, (message-passing)
			- Most likely whole sequence: Viterbi

## Directed Graphical Models
- PRML: Chap 8.1, 8.2
- Concepts
	- Markov blanket
- Bayesian network:
	- LR:\
		<img src="/Bayes/images/gm/gm-lr.png" alt="drawing" width="400"/>
	- Linear Gaussian Models:\
		<img src="/Bayes/images/gm/gm-lgm-1.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/gm-lgm-2.png" alt="drawing" width="400"/>
- Conditional Independence
	- Explain away;
		<img src="/Bayes/images/gm/gm-ind.png" alt="drawing" width="400"/>
	- d-separation: all paths are blocked; A ind B \| C;
		- blocked definition ((a) the arrows on the path meet either head-to-tail or tail-to-tail at the node, and the node is in the set C, or (b) the arrows meet head-to-head at the node, and neither the node, nor any of its descendants, is in the set C.)
- **Kevin Murphy, Chap 10**;
- Examples: Naive Bayes Classifier; HMM; QMR (quick medical reference); Gaussian Bayes Net;
- Inference:
	- p(x_h|x_v,θ) = p(x_h,x_v|θ)/p(x_v|θ) 
	- = p(x_h,x_v|θ) / Σx_h' p(x_h',x_v|θ); (normalize)
- Learning:
	- With complete data:
		- Assume prior factorizes: p(θ) = ∏t=1..V p(θt)
		- Posterior also factorizes: p(θ|D) = ∏t=1..V p(Dt|θt)p(θt)
	- With missing data/latent, not convex;\
		<img src="/Bayes/images/gm/d-sep.png" alt="drawing" width="400"/>

## Undirected Graphical Models
- PRML, Chap 8.3
	- MRF: p(x) = 1/Z ∏ ψc(xc)
	- CRF
	- M. Schmidt. UGM: A Matlab toolbox for probabilistic undirected graphical models.
		- http://www.cs.ubc.ca/~schmidtm/Software/UGM.html. 
- Kevin Murphy, Chap 19
	- Hammersley-Clifford Theorem; Gibbs distribution; energy-based model;
	- Examples: Ising; Hopfield networks; Potts model (generalized Ising to multiple states);
		- Gaussian MRF: 
	- Learning:
		- Exponential family:
			- p(y|θ) = 1/Z(θ) exp[Σ θ_c φ_c(y)]
			- l(θ) = 1/N Σlogp(yi|θ) = 1/N Σ_i[Σ_c θφ(y)-logZ(θ)]
			- ∂l/∂θc = [1/N Σ_i φ_c(yi)] - E[φ_c(yi)]
		- Pseudo-likelihood:\
			<img src="/Bayes/images/gm/pseudo-likelihood.png" alt="drawing" width="400"/>
		- Stochastic maximum likelihood:\
			<img src="/Bayes/images/gm/batch-ml.png" alt="drawing" width="400"/>

## Inference in Graphical Models (PRML, Chap 8.4)
- Exact inference:
	- Variable elimination;
	- Factor graph;
		<img src="/Bayes/images/gm/factor-graph-1.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-2.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-3.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/gm/factor-graph-4.png" alt="drawing" width="400"/>
	- **Sum-product** algorithm (same as **belief propagation**, variable elimination):
		- Used to find marginal of a node p(x):
		- Belief propagation (Pearl, 1988) is a special case; sum-product for a node x first does sum of neighbor xb, then x takes all sum and do product;\
			<img src="/Bayes/images/gm/sum-product.png" alt="drawing" width="400"/>
	- Max-product: 
		- Used to find x maximize the joint distribution;
			<img src="/Bayes/images/gm/max-product-1.png" alt="drawing" width="400"/>
			<img src="/Bayes/images/gm/max-product-2.png" alt="drawing" width="400"/>
- Exact inference:
	- Trunction tree: sum-product, max-product produces efficient, exact inference on tree, so make graph a tree;
- Loopy BP;
- Learning grah structure;

## CRF (Directed or Undirected)
- Inference Proposals
	- MAP inference:
		- alpha-expansion
		- TRW-S
	- M-Best-MAP:
		- D. Nilsson. An efficient algorithm for finding the m most probable configurations in probabilistic expert systems. Statistics and Computing, vol. 8, pp. 159–173, 1998.
		- C. Yanover and Y. Weiss, Finding the m most probable configurations using loopy belief propagation. NIPS'03
		- D. Batra. An Efficient Message-Passing Algorithm for the M-Best MAP Problem. UAI'12
	- Generate a diverse set of proposals:
		- D. Batra, P. Yadollahpour, A. Guzman-Rivera, and G. Shakhnarovich. Diverse M-Best Solutions in Markov Random Fields. ECCV'12
		- **PDivMAP**: F. Meier, A. Globerson, and F. Sha. The More the Merrier: Parameter Learning for Graphical Models with Multiple MAPs. in ICML Workshop on Inferning: Interactions between Inference and Learning, 2013
		- C. Chen, V. Kolmogorov, Y. Zhu, D. Metaxas, and C. H. Lampert. Computing the m most probable modes of a graphical model. AISTATS'13
- Dense CRF:
	- Philipp Krähenbühl, Vladlen Koltun. Efficient Inference in Fully Connected CRFs with Gaussian Edge Potentials. NIPS'12
	- DeepLab;
- Uncertainty measure:
	- G. Papandreou and A. L. Yuille, Perturb-and-map random fields: Using discrete optimization to learn and sample from energy models. ICCV'11
	- D. Tarlow, R. P. Adams, and R. S. Zemel. Randomized optimum models for structured prediction. AISTATS'12
	- **MAP-perturbation**: S. Maji, T. Hazan, and T. Jaakkola. Active boundary annotation using random map perturbations. AAAI'14

## Markov and HMM (Kevin Murphy Chap 17)
- 17.1 Intro;
- 17.2 Markov models:
	- p(X1:T) = p(X1) ∏p(Xt|Xt-1)
	- 2.1 Transition matrix A;
	- n-step: A(n), A(1)=A, A(m+n)=A(m)A(n);
	- 2.2 Language modeling:
		- p(Xt=k) unigram;
		- p(Xt=k|Xt-1=j): bigram;
		- p(Xt=k|Xt-1=j, Xt-2=i): trigram;
		- n-gram;
		- MLE: π^ = Nj/ΣNj, Ajk^ = Njk/Σ_k Njk;
		- Backoff smoothing: Dirichlet;
	- 2.3 stationary distribution
		- π=πA
- 17.3 HMM
	- Hidden state z1:T
	- p(z1:T,x1:T) = [p(z1)∏p(zt|zt-1)] [∏p(xt|zt)]
	- Obs model:
		- B(k,l) = p(xt=l|zt=k,θ); discrete
		- p(xt|z=k,θ) = N(xt|μk, Σk)
- 17.4 HMM inference
	- 17.4.2 Forward algorithm
		- p(zt=j|x1:t−1) = Σp(zt=j|zt−1=i)p(zt−1=i|x1:t−1)
		- Forward posterior:
			- αt(j) = p(zt=j|x1:t) = p(zt=j|xt, x1:t−1) 
			- = 1/Z p(xt|zt=j)p(zt=j|x1:t−1)
			- αt ∝ ψt ⊙ (Ψ αt−1)
			- with ψt(j) = p(xt|zt = j) as local evidence, Ψ(i,j) = p(zt = j|zt−1 = i)
	- 17.4.3 Forward-backward algorithm
		- Posterior of a state given all obs:
			- p(z=j|x1:T) ∝ p(zt=j,x_t+1:T|x1:t) 
			- ∝ p(zt=j|x1:t) p(x_t+1:T|zt=j)
		- First item: αt
		- Second item: βt(j) := p(xt+1:T|zt=j)
		- Posterior: γt(j) ∝ αt(j)βt(j)
		- βt−1 = Ψ(ψt ⊙ βt)
	- 17.4.4 Viterbi (most probable sequence)
		- z∗ = argmax_z2:T p(z1:T|x1:T)
		- Still forward-backward, but do dynamic programming;
		- Keep track of best so far up to t-1;
		- δt(j) = max δt−1(i)ψ(i, j)φt(j)
	- 17.4.5 Forwards filtering, backwards sampling
		- zs1:T ∼ p(z1:T|x1:T)
		- One-step back posterior:
			- p(zt=i|zt+1=j,x1:T)=φt+1(j)ψ(i,j)αt(i)/αt+1(j)
- 17.5 Learning for HMMs
	- 17.5.1 Training with fully obs data
	- 17.5.2 EM for HMMs (the Baum-Welch algorithm)
		- E-step: latent zt marginal:
			- γi,t(j) = p(zt=j|xi,1:Ti, θ)
			- ξi,t(j, k) = p(zt−1=j, zt=k|xi,1:Ti, θ)
		- M-step:
			- Transition for discrete: Ajk = E[N_jk]/ΣE_k'[N_jk']
			- μ, Σ for Gaussian;
	- 17.5.3 Bayesian fitting
		- VBEM: posterior rather than MAP
	- 17.5.4 Discriminative training
		- Implicit from generative model
	- 17.5.5 Model selection
		- Choosing the number of hidden states
		- Structure learning: learning a **sparse** transition matrix
- 17.6 Generalizations of HMMs
	- 17.6.1 Variable duration (semi-Markov) HMMs
		- 17.6.1.1 HSMM as augmented HMMs
	- 17.6.2 Hierarchical HMMs
	- 17.6.3 Input-output HMMs
	- 17.6.4 Auto-regressive and buried HMMs
	- 17.6.5 Factorial HMM
	- 17.6.6 Coupled HMM and the influence model
	- 17.6.7 Dynamic Bayesian networks (DBNs)

## 18 State space models
- 18.1 Introduction
	- zt = g(at, zt−1, εt)
	- ot = h(zt, at, δt)
	- Important special case: all linear-Gaussian (LG-SSM):
		- Transition: zt = Atzt−1 + Btat + εt
		- Observation: ot = Ctzt + Dtat + δt
		- εt ∼ N(0,Qt), δt ∼ N(0,Rt)
- 18.2 Applications of SSMs
	- 18.2.1 SSMs for object tracking
	- 18.2.2 Robotic SLAM
	- 18.2.3 Online parameter learning using recursive least squares
	- 18.2.4 SSM for time series forecasting
		- ARMA
- 18.3 Inference in LG-SSM
	- 18.3.1 The Kalman filtering algorithm

## NIPS'19
- Boxin Zhao, Y. Samuel Wang, Mladen Kolar. Direct Estimation of Differential Functional Graphical Models. NIPS'19
- Shanshan Wu, Sujay Sanghavi, Alexandros G. Dimakis. Sparse Logistic Regression Learns All Discrete Pairwise Graphical Models. NIPS'19
- Lingrui Gan, Xinming Yang, Naveen Narisetty, Feng Liang. Bayesian Joint Estimation of Multiple Graphical Models. NIPS'19
- Radu Marinescu, Rina Dechter. Counting the Optimal Solutions in Graphical Models. NIPS'19
- Firoozeh Sepehr, Donatello Materassi. An Algorithm to Learn Polytree Networks with Hidden Nodes
- Jonathan Kuck, Tri Dao, Hamid Rezatofighi, Ashish Sabharwal, Stefano Ermon. Approximating the Permanent by Sampling from Adaptive Partitions
- Lingrui Gan, Xinming Yang, Naveen Narisetty, Feng Liang. Bayesian Joint Estimation of Multiple Graphical Models
- Radu Marinescu, Rina Dechter. Counting the Optimal Solutions in Graphical Models
- Boxin Zhao, Y. Samuel Wang, Mladen Kolar. Direct Estimation of Differential Functional Graphical Models
- Pasha Khosravi, YooJung Choi, Yitao Liang, Antonio Vergari, Guy Van den Broeck. On Tractable Computation of Expected Predictions
- Andy Shih, Guy Van den Broeck, Paul Beame, Antoine Amarilli. Smoothing Structured Decomposable Circuits
- Shanshan Wu, Sujay Sanghavi, Alexandros Dimakis. Sparse Logistic Regression Learns All Discrete Pairwise Graphical Models
- Sandeep Kumar, Jiaxi Ying, Jose Vinicius de Miranda Cardoso, Daniel Palomar. Structured Graph Learning Via Laplacian Spectral Constraints
