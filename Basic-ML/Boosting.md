# Adaptive Basis Function Models

## CART (Classification and regression trees)

## Generalized Additive Model

## Boosting
- SOA:
	- Tianqi Chen, Carlos Guestrin. XGBoost: A Scalable Tree Boosting System, KDD 2016
- Squared error (yi-f(xi))^2: L2Boosting
- Absolute error |yi-f(xi)|: Gradient Boosting
- Exponential loss exp(-yif(xi)|: AdaBoost
- Logloss log(1+exp(-yif(xi))): LogitBoost
- H(x) = sgn(h1(x)+h2(x)+h3(x)+...)

## Ensemble Learning