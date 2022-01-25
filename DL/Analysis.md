# Empirical Analysis of Deep Learning

## Prediction Uncertainty, Probability Calibration
- Resources: https://treszkai.github.io/2019/09/26/overconfidence
- Niculescu-Mizil, Alexandru and Caruana, Rich. Predicting good probabilities with supervised learning. ICML'05
	- Well calibrated;
- Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger. On Calibration of Modern Neural Networks. ICML'17
	- Neural Networks are over confident;
- Balaji Lakshminarayanan, Alexander Pritzel, Charles Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. NIPS'17

## Convergence
- **Double-Descent**: Preetum Nakkiran, Gal Kaplun, Yamini Bansal, Tristan Yang, Boaz Barak, Ilya Sutskever. Deep Double Descent: Where Bigger Models and More Data Hurt. ICLR'20
	- https://openai.com/blog/deep-double-descent/
	- Model-wise double descent: there is a regime where bigger models are worse;
		<img src="/DL/images/empirical/double-descent-1.png" alt="drawing" width="450"/>
	- Sample-wise non-monotonicity: there is a regime where more samples hurts;
		<img src="/DL/images/empirical/double-descent-2.png" alt="drawing" width="450"/>
	- Epoch-wise double descent;
	- Hypothesis: Our intuition is that, for models at the interpolation threshold, there is effectively only one model that fits the train data, and forcing it to fit even slightly noisy or misspecified labels will destroy its global structure. That is, there are no “good models” which both interpolate the train set and perform well on the test set. However, in the over-parameterized regime, there are many models that fit the train set and there exist such good models. Moreover, the implicit bias of stochastic gradient descent (SGD) leads it to such good models, for reasons we don't yet understand.

## Generalization
- Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals. Understanding deep learning requires rethinking generalization. ICLR'17

## Dimensionality
- Chunyuan Li, Heerad Farkhoor, Rosanne Liu, Jason Yosinski. Measuring the Intrinsic Dimension of Objective Landscapes. ICLR'18
	- Insight: constrain the update in a subspace to recheck convergence;

## Geometry of Loss Design
- Ian J Goodfellow, Oriol Vinyals, and Andrew M Saxe. Qualitatively characterizing neural network optimization problems. 2014
- Daniel Soudry and Yair Carmon. No bad local minima: Data independent training error guarantees for multilayer neural networks. 2016
- Itay Safran and Ohad Shamir. On the quality of the initial basin in overspecified neural networks. ICML'16
- Quynh Nguyen and Matthias Hein. The loss surface of deep and wide neural networks. ICML'17
- Hao Li, Zheng Xu, Gavin Taylor, Christoph Studer, and Tom Goldstein. Visualizing the Loss Landscape of Neural Nets. NIPS'18
- Janice Lan, Rosanne Liu, Hattie Zhou, Jason Yosinski. LCA: Loss Change Allocation for Neural Network Training. NIPS'19
	- Insight: module-wise training loss during iteration;
		<img src="/DL/images/empirical/lca-1.png" alt="drawing" width="450"/>\
		<img src="/DL/images/empirical/lca-2.png" alt="drawing" width="450"/>

## Property at Convergence
- Anna Choromanska, Mikael Henaff, Michael Mathieu, Gérard Ben Arous, and Yann LeCun. The loss surfaces of multilayer networks. AISTATS'15
- Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping Tak Peter Tang. On large-batch training for deep learning: Generalization gap and sharp minima. arxiv'16
- Chiyuan Zhang, Samy Bengio, and Yoram Singer. Are all layers created equal? arxiv'19

## Property During Iteration