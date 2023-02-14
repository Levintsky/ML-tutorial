# MDP, POMDP

## Stanford cs-234 (Lec-2)
- Assumption:
	- Dynamics and reward model available;
	- p(st+1|st, at) = p(st+1|ht, at)
- MDP + π(a|s) = MRP (Markov Reward Process)
	- V = R + γPV -> V = (I-γP)^-1 R
	- Bellman backup (iterative):
		- V(s;π) = Σ_a π(a|s)[r(s,a) + γΣ_s' p(s'|s,a)V(s';π)]
- Optimal: π∗(s) = argmax_π V(s;π)
	- Existance and unique;
- State-action: Q(s,a;π) = R(s,a) + γΣ_s' p(s'|s,a)V(s';π)]
	- Policy iteration (PI): iteratively do value-eval and policy improvement;
		- Policy improvement: take argmax, then follow π, always gets better;
		- π∗(s) = argmax_a Q(s,a;π)
	- Value iteration (VI):
		- V=BV, or V(s) = max_a[R(s,a)+γΣ_s' p(s'|s,a)V(s')]
- Policy evaluation:
	- MC: Gt = rt + γrt+1 + γ^2rt+2 + ... (high var, unbiased)
		- Incremental: G(s) += Gi,t, V(s;π)=G(s)/N(s)
	- TD(0): V(s) += α(r+γV(st+1)-V(st)), (low var, biased)
- Thompson Sampling for MDP:
	- Init prior p(Ras), p(T(s'|s,a))
	- Loop:
		- Sample: (s,a), T(s'|s,a), R(s,a)
		- Compute optimal Q;
		- at = argmaxQ(s,a)
		- Observe rt, st+1;
		- Update posterior p(Ras|rt), p(T|st+1) using Bayesian rule;
