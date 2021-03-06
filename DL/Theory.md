# Deep Learning Theories

## Unclassified
- Samuel S Schoenholz, Justin Gilmer, Surya Ganguli, and Jascha Sohl-Dickstein. Deep information propagation. arXiv preprint arXiv:1611.01232, 2016.
- Ben Poole, Subhaneil Lahiri, Maithra Raghu, Jascha Sohl-Dickstein, and Surya Ganguli. Exponential expressivity in deep neural networks through transient chaos. NeurIPS'16
- Ge Yang and Samuel Schoenholz. Mean field residual networks: On the edge of chaos. NeurIPS'17
- Léonard Blier, Yann Ollivier. The Description Length of Deep Learning models. NIPS'18
- Simon S Du, Jason D Lee, Haochuan Li, Liwei Wang, and Xiyu Zhai. Gradient descent finds global minima of deep neural networks. arXiv preprint arXiv:1811.03804, 2018a.
- Ping Li and Phan-Minh Nguyen. On random deep weight-tied autoencoders: Exact asymptotic analysis, phase transitions, and implications to training. ICLR'19

## Universal Approximator
- Kurt Hornik. Approximation capabilities of multilayer feedforward networks. Neural networks, 4(2): 251–257, 1991.
- Hongzhou Lin, Stefanie Jegelka. ResNet with one-neuron hidden layers is a Universal Approximator. NIPS'18
- M. Leshno, V. Lin, A. Pinkus, and S. Schocken. Multilayer feedforward networks with a non- polynomial activation function can approximate any function. NN'93

## Mean-Field/Optimal-Transport Theory
- Ryo Karakida, Shotaro Akaho, and Shun-ichi Amari. Universal statistics of fisher information in deep neural networks: mean field approach. 2018.
- Chizat, Lenaic, and Francis Bach. On the global convergence of gradient descent for over-parameterized models using optimal transport. NIPS'18
- Mei, Song, Theodor Misiakiewicz, and Andrea Montanari. Mean-field theory of two-layers neural networks: dimension-free bounds and kernel limit. arXiv'19
- Yaniv Blumenfeld, Dar Gilboa, and Daniel Soudry. A mean field theory of quantized deep networks: The quantization-depth trade-off. arXiv preprint arXiv:1906.00771, 2019.
- Soufiane Hayou, Arnaud Doucet, and Judith Rousseau. Mean-field behaviour of neural tangent kernel for deep neural networks, 2019.

## Initialization
- Amit Daniely, Roy Frostig, and Yoram Singer. Toward deeper understanding of neural networks: The power of initialization and a dual view on expressivity. NIPS'16

## Convergence
- Over-Parametrization:
	- Zeyuan Allen-Zhu, Yuanzhi Li, and Zhao Song. A convergence theory for deep learning via over- parameterization. ICML'18
	- Francis Bach. On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport. NIPS'18
	- Simon S Du, Xiyu Zhai, Barnabas Poczos, and Aarti Singh. Gradient descent provably optimizes over-parameterized neural networks. arXiv preprint arXiv:1810.02054, 2018b
	- Yuanzhi Li. Learning Overparameterized Neural Networks via Stochastic Gradient Descent on Structured Data. NIPS'18
		- Empirical
	- Lili Su, Pengkun Yang. On Learning Over-parameterized Neural Networks: A Functional Approximation Perspective. NIPS'19
- SGD:
	- Boris Hanin. Which Neural Net Architectures Give Rise to Exploding and Vanishing Gradients. NIPS'18
	- Allen Zhu. Byzantine Stochastic Gradient Descent. NIPS'18
- Normalization:
	- Shibani Santurkar, Dimitris Tsipras, Andrew Ilyas, Aleksander Madry. How Does Batch Normalization Help Optimization? NIPS'18
	- Nils Bjorck, Carla P. Gomes, Bart Selman, Kilian Q. Weinberger. Understanding Batch Normalizations. NIPS'18
	- Yixi Xu, Xiao Wang. Understanding Weight Normalized Deep Neural Networks with Rectified Linear Units. NIPS'18
- Paul Hand. Phase Retrieval Under a Generative Prior. NIPS'18
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
- Behnam Neyshabur, Zhiyuan Li, Srinadh Bhojanapalli, Yann LeCun, Nathan Srebro. Towards Understanding the Role of Over-Parametrization in Generalization of Neural Networks, 2018
- NeurIPS 2019 orals:
	- Uniform convergence may be unable to explain generalization in deep learning. NIPS'19
		- https://www.youtube.com/watch?v=o3GfnEjTdIQ
- Zeyuan Allen-Zhu, Yuanzhi Li. Can SGD Learn Recurrent Neural Networks with Provable Generalization? NIPS'19

## Capacity
- Pierre Baldi. Neuronal Capacity. NIPS'18

## Dimensionality
- Zi Yin, Yuanyuan Shen. On the Dimensionality of Word Embedding. NIPS'18
	- PIP loss, bias-variance trade-off

## Sample Complexity
- Simon Du. How Many Samples are Needed to Estimate a Convolutional Neural Network? NIPS'18
