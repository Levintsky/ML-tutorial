# Logistic Regression

## Model
- p(y\|x, w) = Ber(y\|wx)
- Suppose y in [-1, 1], we have the model, gradient and Hessian as\
	<img src="/Basic-ML/images/lr/logistic1.png" alt="drawing" width="150"/>
	<img src="/Basic-ML/images/lr/logistic2.png" alt="drawing" width="300"/>
- Avoid zigzag: momentum
- Newton's method
- IRLS (Iterated reweighted Least Square)
<img src="/Basic-ML/images/lr/logistic2.png" alt="drawing" width="500"/>

- Multiclass: softmax
- Generative v.s. discriminative models
	- D: p(y\|x, w)
	- G: p(x, y\|w)

## Generalized Linear Models
- Exponential Family:
	<img src="/Basic-ML/images/glinear.png" alt="drawing" width="500"/>