# Monte Carlo inference

## Latest
- A Golinski, Yee Whye Teh, F Wood, T Rainforth. Amortized Monte Carlo Integration. ICML'19 best paper honorable mention

## Sampling
- Sampling from Standard Distributions
	- Using **cdf**, u ~ U(0,1), invF(u) ~ F
- **Rejection Sampling**
	- Especially if p(x) hard to evaluate due to normalization factor, maybe the true p'(x)=p(x)/Z
	- Mq(x) > p(x)
	- x ~ q(x), u ~ U(0, 1), accept x if u > p(x)/Mq(x)
- **Importance Sampling** (especially when we want to sample more from a rare event)
	- Evaluate E(f(x)), where x ~ p(x), empirical: (f(x1) + f(x2) + ... + f(xN)) / N;
	- Sample x ~ q(x), evaluate E[f(x)p(x)/q(x)]
- **Particle filtering**:
	- Sequential importance sampling for p(z1:t|y1:t)
	- A set of weighted particles w(ts)
	- Weight: w(ts) = p(z1:t|y1:t) / q(z1:t|y1:t)
	- p(z1:t|y1:t) = p(yt|zt)p(zt|zt-1)p(z1:t-1|y1:t-1)
	- For proposal q, we restrict as: q(z1:t|y1:t)=q(zt|z1:t-1,y1:t)q(z1:t-1|y1:t-1)
	- Weight: w(ts) = w(ts-1) p(yt|zts)p(zts|zt-1s)/q(zts|zs1:t-1,y1:t)
	- For degeneration, do resampling

## MCMC (Kevin Murphy Chap 24)
- Gibbs sampling:
	- Basic idea: p(x1|x2, x3), then x2, x3
	- Save all samples, evaluate probability
	- Discard some initial points until **burn-in**
- Collapsed Gibbs sampling:
	- analytically integrate out some of the unknown quantities, and just sample the rest
- **Metropolis Hastings** algorithm
	- At each step, propose to move from the current state x to a new state x' with probability q(x'|x)
	- If symmetric q(x'|x)=q(x|x'), accept with r = min(1, p(x')/p(x))
	- Assymetric r = min(1, p(x')q(x|x')/p(x)q('x|x))
	- Gibbs sampling is a special case of MH
		<img src="/Basic-ML/images/mc/mh.png" alt="drawing" width="400"/>
	- Data-driven MCMC (Tu, Zhu)
		- Proposal also data-driven
		- q(x'|x,D) = pi0 q0(x'|x) + sum pik qk(xk'|fk(D))
		- q0: a standard data-independent proposal (random walk)
		- qk proposes changes to kth part
- Speed and accuracy
	- Burn-in phase: when more stable
- Auxiliary variable MCMC: Sometimes we can dramatically improve the efficiency of sampling by introducing dummy z, p(x)=sum_z(p(x,z))
	- Slice-sampling: introduce auxiliary height h;
		<img src="/Basic-ML/images/mc/slice-mc.png" alt="drawing" width="400"/>
	- Swendsen-Wang;
	- HMC: exp(-E(x)), introduce velocity v, exp(-E(x)-K(v)), i.e., exp(-H(x,v));
		<img src="/Basic-ML/images/mc/hmc.png" alt="drawing" width="400"/>
	- Gibbs sampling velocity;

## Unclassified
- Graphical model inference: Sequential Monte Carlo meets deterministic approximations. NIPS'18
- On Markov Chain Gradient Descent. NIPS'18
- On Learning Markov Chains. NIPS'18
