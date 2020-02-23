# Bayesian Statistics

## Unclassified
- NBC (Naive Bayes):\
	<img src="/Bayes/images/basics/nbc.png" alt="drawing" width="400"/>

## Bayesian Statistics (Kevin Murphy Chap 5)
- MAP estimation is not invariant to reparameterization
- Credible intervals:\
	<img src="/Bayes/images/basics/cred-int.png" alt="drawing" width="400"/>
- Bayesian model selection:\
	<img src="/Bayes/images/basics/bayes-model-select.png" alt="drawing" width="400"/>
- Bayesian Occam:\
	<img src="/Bayes/images/basics/bayes-occam.png" alt="drawing" width="400"/>
- BIC approximation to log marginal likelihood: also closed to MDL and AIC;
	<img src="/Bayes/images/basics/bic.png" alt="drawing" width="400"/>
- Priors:
	- Jeffreys priors: uniformative under reparametrization:\
		<img src="/Bayes/images/basics/Jeffreys-prior.png" alt="drawing" width="400"/>
- Hierarchical Bayes: multi-level model\
	<img src="/Bayes/images/basics/h-bayes-1.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/basics/h-bayes-2.png" alt="drawing" width="400"/>
- Empirical Bayes:\
	<img src="/Bayes/images/basics/emp-bayes.png" alt="drawing" width="400"/>
- Bayesian decision theory:
	- Maximum expected utility principle:
		<img src="/Bayes/images/basics/bayes-decision-1.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/basics/bayes-decision-2.png" alt="drawing" width="400"/>
	- The false positive vs false negative tradeoff;
	- ROC curve;
		- fp v.s. fn;\
			<img src="/Bayes/images/basics/fpfn.png" alt="drawing" width="200"/>
		- ROC curve (receiver operating characteristic): true positive v.s. false positive:
		- Measured by **AUC** (area under the curve): the larger the better;
	- Precision recall: left ROC, right PR;
		<img src="/Bayes/images/basics/roc.png" alt="drawing" width="400"/>
	- F-score (F1-score):\
		<img src="/Bayes/images/basics/f-score.png" alt="drawing" width="350"/>
	- Multi-arm bandit: UCB, Thompson Sampling;
	- Utility theory;

## Frequentist Statistics (Kevin Murphy Chap 6)
- The parameter is viewed as fixed and the data as random, which is the exact opposite of the Bayesian approach;
- Sampling distribution:\
	<img src="/Bayes/images/basics/sample-dist.png" alt="drawing" width="400"/>
- Frequentist decision theory:
	<img src="/Bayes/images/basics/freq-decision.png" alt="drawing" width="400"/>
- Not only is the frequentist definition unnatural, it cannot even be computed, because true theta is unknown. Consequently, we cannot compare different estimators in terms of their frequentist risk. We discuss various solutions to this below.
	- Option 1: Bayes risk;
	- Option 2: Minimax risk;
	- Admissible estimator: An estimator is said to be admissible if it is not strictly dominated by any other estimator;