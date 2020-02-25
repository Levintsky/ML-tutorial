# Deep Learning Theories

## Another View
- Learning differential equation:
	- Rassi. Multistep neural networks for data-driven discovery of nonlinear dynamical systems. 2018
	- Rassi. Numerical Gaussian processes for time-dependent and nonlinear partial differential equations. 2018

## Approximator
- ResNet with one-neuron hidden layers is a Universal Approximator. NIPS'18

## Prediction Uncertainty, Probability Calibration
- Resources: https://treszkai.github.io/2019/09/26/overconfidence
- Niculescu-Mizil, Alexandru and Caruana, Rich. Predicting good probabilities with supervised learning. ICML'05
	- Well calibrated;
- Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger. On Calibration of Modern Neural Networks. ICML'17
	- Neural Networks are over confident;
- Balaji Lakshminarayanan, Alexander Pritzel, Charles Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. NIPS'17

## Convergence
- Preetum Nakkiran, Gal Kaplun, Yamini Bansal, Tristan Yang, Boaz Barak, Ilya Sutskever. Deep Double Descent: Where Bigger Models and More Data Hurt. ICLR'20
	- https://openai.com/blog/deep-double-descent/
	- Model-wise double descent: there is a regime where bigger models are worse;
		<img src="/DL/images/analysis/double-descent-1.png" alt="drawing" width="450"/>
	- Sample-wise non-monotonicity: there is a regime where more samples hurts;
		<img src="/DL/images/analysis/double-descent-2.png" alt="drawing" width="450"/>
	- Epoch-wise double descent;
	- Hypothesis: Our intuition is that, for models at the interpolation threshold, there is effectively only one model that fits the train data, and forcing it to fit even slightly noisy or misspecified labels will destroy its global structure. That is, there are no “good models” which both interpolate the train set and perform well on the test set. However, in the over-parameterized regime, there are many models that fit the train set and there exist such good models. Moreover, the implicit bias of stochastic gradient descent (SGD) leads it to such good models, for reasons we don't yet understand.
- Over-Parametrization:
	- Francis Bach. On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport. NIPS'18
	- Yuanzhi Li. Learning Overparameterized Neural Networks via Stochastic Gradient Descent on Structured Data. NIPS'18
	- How SGD Selects the Global Minima in Over-parameterized Learning: A Dynamical Stability Perspective. NIPS'18
	- Lili Su, Pengkun Yang. On Learning Over-parameterized Neural Networks: A Functional Approximation Perspective. NIPS'19
- SGD:
	- Which Neural Net Architectures Give Rise to Exploding and Vanishing Gradients. NIPS'18
	- Allen Zhu. Byzantine Stochastic Gradient Descent. NIPS'18
- Normalization:
	- How Does Batch Normalization Help Optimization? NIPS'18
	- Understanding Batch Normalizations. NIPS'18
	- Understanding Weight Normalized Deep Neural Networks with Rectified Linear Units. NIPS'18
- Paul Hand. Phase Retrieval Under a Generative Prior. NIPS'18
- Berkeley. On the Local Minima of the Empirical Risk. NIPS'18
- Allen Zhu. NEON2: Finding Local Minima via First-Order Oracles. NIPS'18
- Are ResNets Provably Better than Linear Predictors? NIPS'18
- Simon Du, Jason Lee. Algorithmic Regularization in Learning Deep Homogeneous Models: Layers are Automatically Balanced. NIPS'18

## Generalization
- PAC-Bayes:
	- John Langford and John Shawe-Taylor. Pac-bayes & margins. NIPS'02
	- David McAllester. Simplified pac-bayesian margin bounds. 2003
	- Vaishnavh Nagarajan and Zico Kolter. Deterministic PAC-bayesian generalization bounds for deep networks via generalizing noise-resilience. ICLR'19
	- Wenda Zhou, Victor Veitch, Morgane Austern, Ryan P. Adams, and Peter Orbanz. Nonvacuous generalization bounds at the imagenet scale: a PAC-bayesian compression approach. ICLR'19
- Behnam Neyshabur, Ryota Tomioka, Nathan Srebro. In Search of the Real Inductive Bias: On the Role of Implicit Regularization in Deep Learning. ICLR'15
- Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals. Understanding deep learning requires rethinking generalization. ICLR'17
- Behnam Neyshabur, Zhiyuan Li, Srinadh Bhojanapalli, Yann LeCun, Nathan Srebro. Towards Understanding the Role of Over-Parametrization in Generalization of Neural Networks, 2018
- NeurIPS 2019 orals:
	- Uniform convergence may be unable to explain generalization in deep learning. NIPS'19
		- https://www.youtube.com/watch?v=o3GfnEjTdIQ
- Zeyuan Allen-Zhu, Yuanzhi Li. Can SGD Learn Recurrent Neural Networks with Provable Generalization? NIPS'19

## Capacity
- Pierre Baldi. Neuronal Capacity. NIPS'18

## Dimensionality
- On the Dimensionality of Word Embedding (Stanford)
	- PIP loss, bias-variance trade-off

## Sample Complexity
- Simon Du. How Many Samples are Needed to Estimate a Convolutional Neural Network? NIPS'18

## Unclassified
- FAIR. The Description Length of Deep Learning models. NIPS'18
