# Adaptive Basis Function Models

## CART (Classification and regression trees)
- Packages of split finding:
	- **scikit-learn**: Scikit-learn: Machine learning in Python. JMLR'11
	- **gbm**: G. Ridgeway. Generalized Boosted Models: A guide to the gbm package.
- Split
<img src="/Basic-ML/images/cart1.png" alt="drawing" width="600"/>

- Exact optimal split finding of m dimension n instances: O(mn) + O(mlogn) sorting:
<img src="/Basic-ML/images/cart2.png" alt="drawing" width="600"/>

- Approximate optimal split finding: percentile. 1. global: propose candidates once at beginning; 2. local: recalculate everytime; **Weighted-Quantile sketch** to propose candidates; 
<img src="/Basic-ML/images/cart3.png" alt="drawing" width="600"/>

- Sparsity-aware split finding:
<img src="/Basic-ML/images/cart4.png" alt="drawing" width="550"/>

## Boosting
- SOA:
	- Tianqi Chen, Carlos Guestrin. XGBoost: A Scalable Tree Boosting System, KDD 2016
		- https://github.com/dmlc/xgboost
		- y = sum fk(x), f in F (CART)
		- Loss (regression + complexity):
<img src="/Basic-ML/images/boosting1.png" alt="drawing" width="600"/>

		- Loss of adding a new tree:
<img src="/Basic-ML/images/boosting2.png" alt="drawing" width="600"/>

		- Optimal weight and loss:
<img src="/Basic-ML/images/boosting3.png" alt="drawing" width="600"/>

		- Split finding on-the-fly (check CART);
- Squared error (yi-f(xi))^2: L2Boosting
- Absolute error |yi-f(xi)|: Gradient Boosting
- Exponential loss exp(-yif(xi)|: AdaBoost
- Logloss log(1+exp(-yif(xi))): LogitBoost
- H(x) = sgn(h1(x)+h2(x)+h3(x)+...)

## Legacy
- J. Friedman. Greedy function approximation: a gradient boosting machine. Annals of Statistics. 2001
- P. Li. Robust Logitboost and adaptive base class (ABC) Logitboost. UAI'10
- **LambdaMART**: C. Burges. From ranknet to lambdarank to lambdamart: An overview. Learning'10
- X. He, J. Pan, O. Jin, T. Xu, B. Liu, T. Xu, Y. Shi,
A. Atallah, R. Herbrich, S. Bowers, and J. Q. n. Candela. Practical lessons from predicting clicks on ads at facebook. ADKDD'14
- J. Bennett and S. Lanning. The netflix prize. In Proceedings of the KDD Cup Workshop 2007

## Ensemble Learning