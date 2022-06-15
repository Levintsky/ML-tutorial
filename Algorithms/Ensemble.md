# Boosting, Ensemble Learning

## Adaptive Basis Function Models (Kevin-Murphy-Chap-16)
- 16.1 Introduction
	- f(x) = w0 + Σwmφm(x)
- 16.2 CART (Classification and regression trees)
	- axis parallel splits
	- f(x) = E[y|x] = Σm wm I(x∈Rm) = Σm wmφ(x; vm)
	- 16.2.2 Growing a tree
		- Choose best feature and best value for that feature;
		- (j∗, t∗) = argmin_j min_t cost({xi, yi: xij≤t}) + cost({xi, yi : xij>t})
		- Gain: ∆ := cost(D) − (|DL|cost(DL)+|DR|cost(DR))
		- Regression cost: L2
		- Classification cost: misclassification rate, entropy deviance, Gini-index;
			- Gini-index: Q(T) = Σ p(1-p)
	- 16.2.3 Pruning a tree
	- 16.2.4 Pros and cons of trees
		- Easy to interpret (+)
		- Unstable (-)
	- 16.2.5 Random forests
		- Bagging trees: f(x) = Σfm(x)
	- 16.2.6 CART compared to hierarchical mixture of experts
- 16.3 Generalized additive models
	- f(x) = α + f1(x1) + ... + fD(xD)
	- 16.3.1 Backfitting
	- 16.3.2 Computational efficiency
	- 16.3.3 Multivariate adaptive regression splines (MARS)
- 16.4 Boosting
	- 16.4.1 Forward stagewise additive modeling
		- min_f ΣL(yi, f(xi))
		- Loss:
			- Squared error (yi-f(xi))^2: L2Boosting
			- Absolute error |yi-f(xi)|: Gradient Boosting
			- Exponential loss exp(-yif(xi): AdaBoost
				- L(y, f) = exp(−yf)
				- ∂E[−exp(y(x)|x]/∂x = 0
				- f∗(x)=1/2log[p(y=1|x)/p(y=-1|x)]
			- Logloss log(1+exp(-yif(xi))): LogitBoost
			- H(x) = sgn(h1(x)+h2(x)+h3(x)+...)
		- More powerful model baseline (GLM): at each step m
			- (β, γ) = argmin_βγ ΣL(yi,fm-i(xi)+βφ(xi;γ)
			- fm(x) = fm-1(x) + βφm(xi;γm)
	- 16.4.2 L2boosting
		- L(yi, fm−1(xi)+βφ(xi; γ)) = (rim − φ(xi; γ))^2
	- 16.4.3 AdaBoost
		- Binary classification
		- Lm(φ) = Σ_i wim exp(-βyiφ(xi))
		- Optimal: φm = argmin_φ wi,mI(yi ≠ φ(xi))
		- β = 1/2 log(1-errm)/errm
	- 16.4.4 LogitBoost
	- 16.4.5 Boosting as functional gradient descent
		- f^ = argmin_f L(f) solved stagewise;
		- At each step, find gradient:
			- Gradient/residual: gim = [∂L(yi,f(xi))/∂f(xi)]|f=fm-1
			- For gd, we should: fm = fm-1 - ρmgm
			- We fit a weaker learner to approximate gm:
			- γm = argmin_γ E[(-gim-φ(xi;γ))^2]
	- 16.4.6 Sparse boosting
		- Similar to matching pursuit;
	- 16.4.7 Multivariate adaptive regression trees (MART)
		- Advisable: shallow tree (low variance, high bias)
		- Combine gradient boosting with regression tree;
		- Re-estimate the parameters after fitting tree;
	- 16.4.8 Why does boosting work so well?
		- Sparse
	- 16.4.9 A Bayesian view
		- Mixture of expert: p(y|x, θ) = Σπm p(y|x, γm)
		- where each expert p(y|x,γm) is like a weak learner
- 16.5 Feedforward neural networks (multilayer perceptrons)
	- 16.5.1 Convolutional neural networks
	- 16.5.2 Other kinds of neural networks
	- 16.5.3 A brief history of the field
	- 16.5.4 The backpropagation algorithm
	- 16.5.5 Identifiability
	- 16.5.6 Regularization
	- 16.5.7 Bayesian inference
- 16.6 Ensemble learning
	- p(y|x, π) = Σwm p(y|x)
	- 16.6.1 Stacking
		- w = argmin_w Σ_i L(yi, Σ_m wmfm^-i(x))
		- LOOCV for generalization;
	- 16.6.2 Error-correcting output codes
	- 16.6.3 Ensemble learning is not equivalent to Bayes model averaging (BMA)
		- p(y|x,D)= Σ p(y|x,m,D)p(m|D)
- 16.7 Experimental comparison
	- 16.7.1 Low-dimensional features
	- 16.7.2 High-dimensional features
- 16.8 Interpreting black-box models
- Mixture of Experts (PRML Chap 14):
	- Mixture of linear regression:\
		<img src="/Basic-ML/images/ensemble/mix-lr-1.png" alt="drawing" width="400"/>\
		<img src="/Basic-ML/images/ensemble/mix-lr-2.png" alt="drawing" width="400"/>
		- E-step:\
			<img src="/Basic-ML/images/ensemble/mix-lr-3.png" alt="drawing" width="400"/>
		- M-step:\
			<img src="/Basic-ML/images/ensemble/mix-lr-4.png" alt="drawing" width="400"/>
			<img src="/Basic-ML/images/ensemble/mix-lr-5.png" alt="drawing" width="400"/>
			<img src="/Basic-ML/images/ensemble/mix-lr-6.png" alt="drawing" width="400"/>
	- General: p(t|x) = Σπk(x)pk(t|x)

## Baseline Weak Leaners
- CART
	- Packages of split finding:
		- **scikit-learn**: Scikit-learn: Machine learning in Python. JMLR'11
		- **gbm**: G. Ridgeway. Generalized Boosted Models: A guide to the gbm package.
	- Split\
		<img src="/Basic-ML/images/ensemble/cart1.png" alt="drawing" width="600"/>
	- Exact optimal split finding of m dimension n instances: O(mn) + O(mlogn) sorting:\
		<img src="/Basic-ML/images/ensemble/cart2.png" alt="drawing" width="600"/>
	- Approximate optimal split finding: percentile. 1. global: propose candidates once at beginning; 2. local: recalculate everytime; **Weighted-Quantile sketch** to propose candidates;\ 
		<img src="/Basic-ML/images/ensemble/cart3.png" alt="drawing" width="600"/>
	- Sparsity-aware split finding:\
		<img src="/Basic-ML/images/ensemble/cart4.png" alt="drawing" width="550"/>

## Boosting
- **AdaBoost**: Freund, Yoav; Schapire, Robert E. A decision-theoretic generalization of on-line learning and an application to boosting". Journal of Computer and System Sciences. 1997
	- First paper on AdaBoost;
- J. Friedman. Greedy function approximation: a gradient boosting machine. Annals of Statistics. 2001
- J. Bennett and S. Lanning. The netflix prize. In Proceedings of the KDD Cup Workshop 2007
- P. Li. Robust Logitboost and adaptive base class (ABC) Logitboost. UAI'10
- **LambdaMART**: C. Burges. From ranknet to lambdarank to lambdamart: An overview. Learning'10
- X. He, J. Pan, O. Jin, T. Xu, B. Liu, T. Xu, Y. Shi, A. Atallah, R. Herbrich, S. Bowers, and J. Q. n. Candela. Practical lessons from predicting clicks on ads at facebook. ADKDD'14
- **XG-Boost**: Tianqi Chen, Carlos Guestrin. XGBoost: A Scalable Tree Boosting System, KDD 2016
	- https://github.com/dmlc/xgboost
	- y = Σfk(x), f ∈ F(CART)
	- Loss (regression + complexity):\
		<img src="/Basic-ML/images/ensemble/boosting1.png" alt="drawing" width="600"/>
	- Loss of adding a new tree:\
		<img src="/Basic-ML/images/ensemble/boosting2.png" alt="drawing" width="600"/>
	- Optimal weight and loss:\
		<img src="/Basic-ML/images/ensemble/boosting3.png" alt="drawing" width="600"/>
	- Split finding on-the-fly (check CART);
- Zhihua Zhou. Multi-Layered Gradient Boosting Decision Trees. NIPS'18

## NIPS'18
- Xiao Li, Yu Wang, Sumanta Basu, Karl Kumbier, Bin Yu. A Debiased MDI Feature Importance Measure for Random Forests
- Shen-Huan Lyu, Liang Yang, Zhi-Hua Zhou. A Refined Margin Distribution Analysis for Forest Representation Learning
- Julaiti Alafate, Yoav S Freund. Faster Boosting with Smaller Memory
- Allan Grønlund, Lior Kamma, Kasper Green Larsen, Alexander Mathiasen, Jelani Nelson. Margin-Based Generalization Lower Bounds for Boosted Classifiers
- Bulat Ibragimov, Gleb Gusev. Minimal Variance Sampling in Stochastic Gradient Boosting
- Igor Kuralenok, Vasilii Ershov, Igor Labutin. MonoForest framework for tree ensemble analysis
- Corinna Cortes, Mehryar Mohri, Dmitry Storcheus. Regularized Gradient Boosting
- Peilin Zhong, Yuchen Mo, Chang Xiao, Pengyu Chen, Changxi Zheng. Rethinking Generative Mode Coverage: A Pointwise Guaranteed Approach
