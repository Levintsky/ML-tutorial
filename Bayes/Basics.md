# Bayesian Statistics

## Unclassified
- NBC (Naive Bayes):\
	<img src="/Bayes/images/basics/nbc.png" alt="drawing" width="400"/>

## Kevin Murphy (Chap 5)
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
