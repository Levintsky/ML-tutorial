# Linear Classifier

## Basics
- Fisher
- Logistic Regression

## Linear Classifier (Bishop, Chapter 4)
- Fisher:
	- m1, m2 as class mean, get direction w (mapping to 1-dim) such that the between class have high variance and within class has low variance:\
		<img src="/Bayes/images/lr/logistic1.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/lr/logistic2.png" alt="drawing" width="250"/>
	- Relation to linear regression: target class 1 to N/N1, class 2 to N/N2;
	- Multiple class: J(W) = Tr{sw^(−1)sB}
	- **Perceptron**: (Frank Rosenblatt) check f(.) >0 or <0. The perceptron convergence theorem states that if there exists an exact solution (in other words, if the training data set is linearly separable), then the perceptron learning algorithm is guaranteed to find an exact solution in a finite number of steps\
		<img src="/Bayes/images/lr/perceptron.png" alt="drawing" width="400"/>
- Probabilistic Generative Models;
	- Continuous;
	- Discrete features (naive bayes assumption);
	- Exponential family;
- Probabilistic Discriminative Models;
	- Logistic regression
	- IRLS: just Newton's method with a diagonal weight Rnn=yn(1-yn);
		<img src="/Bayes/images/lr/irls.png" alt="drawing" width="500"/>
	- Multiclass: cross-entropy loss;
- Laplacian approximation:
	- Find a Gaussian approximation q(z) which is centred on a **mode** of the distribution p(z);
- Bayesian Logistic Regression:
	- Prior p(w) ~ N(m0, S0), posterior N(w_MAP, SN)
		<img src="/Bayes/images/lr/logistic-bayes-1.png" alt="drawing" width="500"/>
	- First get w_MAP (maximum posterior), then SN;
		<img src="/Bayes/images/lr/logistic-bayes-2.png" alt="drawing" width="500"/>
	- Predict: variational q(w) to approximate p(t|w), with a = w \* phi, we have:
		<img src="/Bayes/images/lr/logistic-bayes-3.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/lr/logistic-bayes-4.png" alt="drawing" width="400"/>
		<img src="/Bayes/images/lr/logistic-bayes-5.png" alt="drawing" width="400"/>

## Logistic Regression (Kevin Murphy, Chap 8)
- p(y\|x, w) = Ber(y\|wx)
- Suppose y in [-1, 1], we have the model, gradient and Hessian as\
	<img src="/Bayes/images/lr/logistic1.png" alt="drawing" width="250"/>\
	<img src="/Bayes/images/lr/logistic2.png" alt="drawing" width="300"/>
- Avoid zigzag: momentum
- Newton's method
- IRLS (Iterated reweighted Least Square)\
	<img src="/Bayes/images/lr/irls-alg.png" alt="drawing" width="250"/>
- Quasi-Newton: BFGS; (Assumption: Hessian as Diagonal + low-rank approx);
	<img src="/Bayes/images/lr/bfgs-1.png" alt="drawing" width="300"/>\
	<img src="/Bayes/images/lr/bfgs-2.png" alt="drawing" width="400"/>
- Multiclass: softmax
- Online learning, regret minimization;
	- Regret:\
		<img src="/Bayes/images/lr/online-1.png" alt="drawing" width="300"/>
	- SGD:\
		<img src="/Bayes/images/lr/online-2.png" alt="drawing" width="400"/>\
		<img src="/Bayes/images/lr/online-3.png" alt="drawing" width="400"/>
	- Sufficient converge condition (Robbins-Monroe):\
		<img src="/Bayes/images/lr/robins-monroe.png" alt="drawing" width="400"/>
	- Per-parameter: adagrad:\
		<img src="/Bayes/images/lr/adagrad.png" alt="drawing" width="400"/>
	- Perceptron:\
		<img src="/Bayes/images/lr/perceptron-2.png" alt="drawing" width="350"/>
- Generative v.s. discriminative models
	- D: p(y\|x, w)
	- G: p(x, y\|w)

## Generalized Linear Models, Exponential Family (Kevin Murphy, Chap 9)
- Exponential Family:\
	<img src="/Bayes/images/lr/glinear.png" alt="drawing" width="400"/>
- Log-Partition function:\
	<img src="/Bayes/images/lr/log-partition-1.png" alt="drawing" width="400"/>\
	<img src="/Bayes/images/lr/log-partition-2.png" alt="drawing" width="400"/>
- 􏰁**Pitman-Koopman-Darmois theorem** states that, under certain regularity conditions, the exponential family is the only family of distributions with finite sufficient statistics. 
- **Maxent**: The principle of maximum entropy or maxent says we should pick the distribution with maximum entropy (closest to uniform), subject to the constraints that the moments of the distribution match the empirical moments of the specified functions\
	<img src="/Bayes/images/lr/maxent-1.png" alt="drawing" width="200"/>\
	<img src="/Bayes/images/lr/maxent-2.png" alt="drawing" width="300"/>
- Probit regression:\
	<img src="/Bayes/images/lr/probit.png" alt="drawing" width="400"/>
- Multi-task learning; different tasks with own parameters share a same prior. Model trained on fewer data could borrow from group with more data;\
	<img src="/Bayes/images/lr/mtl.png" alt="drawing" width="450"/>

## Unclassified
- Alexander Munteanu, Chris Schwiegelshohn, Christian Sohler, David P. Woodruff. On Coresets for Logistic Regression. NIPS'18
