# Bayesian Statistics

## Basics
- Super-Gaussian distributions: kurt(z) > 0; natural signals (images) with filtering;
	- kurt(z) := μ4/σ^4 - 3
- Skewed distribution: skew(z) = μ3/σ^3
- Textbooks
	- Machine Learning: A Probabilistic Perspective
	- Foundations of Machine Learning
	- The Elements of Statistical Learning
	- PRML: Pattern Recognition and Machine Learning
- PKU: https://resource.pku.edu.cn/index.php?r=course%2Fdetail&id=381

## Basic Concepts (K-Murphy-3)
- 3.2 Bayesian concept learning
	- 3.2.1 Likelihood
	- 3.2.2 Prior
	- 3.2.3 Posterior
	- 3.2.4 Posterior predictive distribution
- 3.5 NBC (Naive Bayes)
	- Assumption: the features are conditionally **independent** given the class label;
		- p(x|y=c,θ)=Πp(xj|y=c,θjc)
	- The log-sum-exp trick: minus the baseline;

## Bayesian Statistics (K-Murphy-5)
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
	- Precision recall: ROC, PR;
		- TP (y) v.s. FP (x), AUC the larger the better, |-
		- Precision (y) v.s. Recall (x) curve, -|
	- F-score (F1-score):
		- F1 = 2/(1/P+1/R) = 2PR/R+P = 2Σyy^/(Σy+Σy^)
	- Multi-arm bandit: UCB, Thompson Sampling;
	- Utility theory;

## Frequentist Statistics (K-Murphy-6)
- The parameter is viewed as fixed and the data as random, which is the exact opposite of the Bayesian approach;
- Sampling distribution:
	- θ^ = θ^mle(D), D ~ θ∗.
	- θ^ -> N(θ∗, I(θ∗)^-1) as N -> ∞
- Frequentist decision theory:
	- ρ(a|D, π) := E_p(θ|D,π)[L(θ,a)] = ∫L(θ,a)p(θ|D,π)dθ
- Not only is the frequentist definition unnatural, it cannot even be computed, because true θ is unknown. Consequently, we cannot compare different estimators in terms of their frequentist risk. We discuss various solutions to this below.
	- Option 1: Bayes risk;
	- Option 2: Minimax risk;
	- Admissible estimator: An estimator is said to be admissible if it is not strictly dominated by any other estimator;

## SVM
- K-Murphy-14.5
- J(w, λ) = ΣL(yi, yˆi) + λ∥w∥2
- 14.5.1 SVMs for regression
	- Huber like regression loss: E(y(x)-t) = (|y(x)-t|-ε)+
	- J(w, λ) = Σ(ξi+, ξi-) + λ∥w∥2
	- Optimal solution has form: wˆ = Σ αi xi (Schoelkopf and Smola 2002)
	- yˆ(x) = wˆ0 + Σαi κ(xi, x)
- 14.5.2 SVMs for classification
	- L.nll(y, η) = −logp(y|x, w) = log[1+exp(−yη)]
	- L(y, η) = max(0, 1−yη) = (1−yη)+
	- J(w, λ) = 1/2∥w∥2 + CΣ(1−yη)+; equivalent to Σξ
	- yˆ(x) = sgn(wˆ0 + Σαi κ(xi, x))
	- Large margin learning: x=x⊥+rw/|w|, then f(x)=rw'w/|w|
	- ν-SVM classifier: CΣξ (C=1/(νN))
	- Probabilistic output
	- SVMs for multi-class classification
- 14.5.3 Choosing C
- 14.5.4 Summary of key points
- 14.5.5 A probabilistic interpretation of SVMs
- Latent-SVM (K-Murphy-19.7)
	- http://www.csc.kth.se/cvap/cvg/rg/materials/magnus_004_slides.pdf
	- Generalize classical SVM to structured output;
	- Learn linear weight w for the loss/utility ⟨w,φ(x, y)⟩
		- with desired loss δ(y, y')
		- min.w ∥w∥^2 + C max.y[δ(y, yˆ) + w(φ(x,y)-φ(x,yˆ))]
	- Lower/upper bound:
		- R(w) ~ E(w) + Σ.i[max.y{L(yi,y)+w†φ(x,yi)}]
	- Gaussian prior: ∥w∥^2 with binary classification, reduced to standard SVM;
	- Non-probabilistic view:
	- Cutting plane methods:
		- http://svmlight.joachims.org/svm_struct.html
		- Initial guess w and no constraints.
		- Each iteration:
			- for xi, we find the "most violated" constraint involving x and yˆ.
			- If L(yi, y) > ξ+ε, add yˆ to the working set;
			- solve the resulting new QP to find the new w, ξ.
	- The structured perceptron algorithm;
	- Stochastic subgradient descent;
- Latent-structural-SVMs: hidden h;
	- e.g. in machine translation x->y without word alignment;
		- R(w) = -logp(w) + Σ.i log[Σ.y,h exp[L(yi,y,h)] exp[w†φ(x,y,h)]/Z(x,w)]
		- p(y,h|x,w) = exp[w†φ(x,y,h)] / Z(x, w)
		- Z(x, w) = Σ.y,h exp[w†φ(x,y,h)]
	- CCCP (concave-convex procedure): check VI;