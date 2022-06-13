# Boosting, Ensemble Learning

## Combining Models (PRML Chap 14)
- AdaBoost: training and prediction\
	<img src="/Basic-ML/images/ensemble/adaboost-1.png" alt="drawing" width="400"/>\
	<img src="/Basic-ML/images/ensemble/adaboost-2.png" alt="drawing" width="400"/>
- Cost function:\
	<img src="/Basic-ML/images/ensemble/adaboost-3.png" alt="drawing" width="400"/>
- CART: grow + prune;
	- Regression:\
		<img src="/Basic-ML/images/ensemble/cart-reg.png" alt="drawing" width="400"/>
	- Classification:\
		<img src="/Basic-ML/images/ensemble/cart-cls.png" alt="drawing" width="400"/>
- Mixture of Experts:
	- Mixture of linear regression:\
		<img src="/Basic-ML/images/ensemble/mix-lr-1.png" alt="drawing" width="400"/>\
		<img src="/Basic-ML/images/ensemble/mix-lr-2.png" alt="drawing" width="400"/>
		- E-step:\
			<img src="/Basic-ML/images/ensemble/mix-lr-3.png" alt="drawing" width="400"/>
		- M-step:\
			<img src="/Basic-ML/images/ensemble/mix-lr-4.png" alt="drawing" width="400"/>
			<img src="/Basic-ML/images/ensemble/mix-lr-5.png" alt="drawing" width="400"/>
			<img src="/Basic-ML/images/ensemble/mix-lr-6.png" alt="drawing" width="400"/>
	- Mixture of logistic regression:\
	- General\
		<img src="/Basic-ML/images/ensemble/mix-expert.png" alt="drawing" width="400"/>

## Adaptive Basis Function Models
- CART (Classification and regression trees)
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
	- Squared error (yi-f(xi))^2: L2Boosting
	- Absolute error |yi-f(xi)|: Gradient Boosting
	- Exponential loss exp(-yif(xi)|: AdaBoost
	- Logloss log(1+exp(-yif(xi))): LogitBoost
	- H(x) = sgn(h1(x)+h2(x)+h3(x)+...)
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
