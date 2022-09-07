# Empirical Analysis of Deep Learning

## Prediction Uncertainty, Probability Calibration
- Resources: https://treszkai.github.io/2019/09/26/overconfidence
- Niculescu-Mizil, Alexandru and Caruana, Rich. Predicting good probabilities with supervised learning. ICML'05
	- Well calibrated;
- Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger. On Calibration of Modern Neural Networks. ICML'17
	- Neural Networks are over confident;
- Balaji Lakshminarayanan, Alexander Pritzel, Charles Blundell. Simple and scalable predictive uncertainty estimation using deep ensembles. NIPS'17

## Invert
- Theory:
	- Arora, S.; Liang, Y.; and Ma, T. Why are deep nets reversible: A simple theory, with implications for training. ICLR-Workshop'16
	- Gilbert, A. C.; Zhang, Y.; Lee, K.; Zhang, Y.; and Lee, H. Towards understanding the invertibility of convolutional neural networks. IJCAI'17
		- Theoretical connection between compressive sensing and neural network;
		- Model-based CS, MB-RIP; assume higher dimension observation and Gaussian kernel;
			<img src = '/DL/images/dynamic-system/mb-iht.png' width = '400'>
