# Bayesian Statistics

## Unclassified
- NBC (Naive Bayes): Kevin Murphy 3.5
	- Assumption: the features are conditionally **independent** given the class label;
		- p(x|y=c,θ)=Πp(xj|y=c,θjc)
	- The log-sum-exp trick: minus the baseline;

## Bayesian Statistics (Kevin Murphy Chap 5)
- MAP estimation is not invariant to reparameterization
- Credible intervals:
	- Cα(D)=(l,u): P(l≤θ≤u|D)=1-α
- Bayesian model selection:
	- p(m|D) = p(D|m)p(m)/Σp(D|m)p(m)
- Bayesian Occam:
	- P(D) = p(y1)p(y2|y1)p(y3|y1:2)...p(yN|y1:N-1)
- BIC approximation to log marginal likelihood: also closed to MDL and AIC;
	- BIC := logp(D|θ^) - dof(θ)/2 logN ~ logp(D)
	- Penalized for complexity (dof);
- Priors:
	- Jeffreys priors: uniformative under reparametrization:
		- pθ(θ)=pφ(φ)|dφ/dθ|, (prior will generally change)
		- Pick pφ(φ) ∝ (I(φ))^1/2, with I(φ) as the Fisher;
		- I(φ) := -E[(dlogp(X|φ)/dφ)^2]
- Hierarchical Bayes: multi-level model:
	- η -> θ -> D
	- p(D,θ,η) = p(η) ∏i=1..N Bin(xi|Ni,θi)Beta(θi|η)
- Summary:
	- ML: θ^ = argmaxθ p(D|θ)
	- MAP: θ^ = argmaxθ p(D|θ)p(θ|η)
	- ML-II (Empirical): η^ = argmaxη∫p(D|θ)p(θ|η)dθ = argmaxηp(D|η)
	- MAP-II: η^ = argmaxηp(D|η)p(η)
	- Full Bayes: p(θ, η|D) ∝ p(D|θ)p(θ|η)p(η)	
- Bayesian decision theory:
	- Maximum expected utility principle:
		- δ(x) = argmin_a E[L(y,a)]
		- Utility U(y,a) = -L(y,a)
		- ρ(a|x) := E_p(y|x)[L(y,a)]
	- The false positive vs false negative tradeoff;
	- ROC curve;
		- fp v.s. fn;
		- ROC curve (receiver operating characteristic): true positive v.s. false positive:
		- Measured by **AUC** (area under the curve): the larger the better;
	- Precision recall: left ROC, right PR;
		<img src="/Probabilistic/images/basics/roc.png" alt="drawing" width="400"/>
	- F-score (F1-score):
		- F1 = 2/(1/P+1/R) = 2PR/R+P = 2Σyy^/(Σy+Σy^)
	- Multi-arm bandit: UCB, Thompson Sampling;
	- Utility theory;

## Frequentist Statistics (Kevin Murphy Chap 6)
- The parameter is viewed as fixed and the data as random, which is the exact opposite of the Bayesian approach;
- Sampling distribution:
	- θ^ = θ^mle(D), D ~ θ\*.
	- θ^ -> N(θ\*, I(θ\*)^-1) as N -> ∞
- Frequentist decision theory:
	- ρ(a|D, π) := E_p(θ|D,π)[L(θ,a)] = ∫L(θ,a)p(θ|D,π)dθ
- Not only is the frequentist definition unnatural, it cannot even be computed, because true θ is unknown. Consequently, we cannot compare different estimators in terms of their frequentist risk. We discuss various solutions to this below.
	- Option 1: Bayes risk;
	- Option 2: Minimax risk;
	- Admissible estimator: An estimator is said to be admissible if it is not strictly dominated by any other estimator;