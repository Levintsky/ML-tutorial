# Theory on Neural Net

## Basics
- Approximation theory:
	- Universal approximator, capacity;
- Statistical Generalization
	- More params does not lead to overfitting! (overparametrization)

## Unclassified
- Colin Wei, Tengyu Ma. Data-dependent Sample Complexity of Deep Neural Networks via Lipschitz Augmentation. NeurIPS'18
- Vaishnavh Nagarajan, J. Zico Kolter. Uniform convergence may be unable to explain generalization in deep learning. NIPS'18
- M. Belkin, D. Hsu, S. Ma, and S. Mandal. Reconciling modern machine-learning practice and the classical bias-variance trade-off. PNAS'19
	- Does not increase monotonically with intermediate dim m;
- Uniform convergence may be unable to explain generalization in deep learning. NIPS'19 oral
	- https://www.youtube.com/watch?v=o3GfnEjTdIQ
- Zeyuan Allen-Zhu, Yuanzhi Li. Can SGD Learn Recurrent Neural Networks with Provable Generalization? NIPS'19
- Mean field:
	- Ge Yang and Samuel Schoenholz. Mean field residual networks: On the edge of chaos. NeurIPS'17
	- Ryo Karakida, Shotaro Akaho, and Shun-ichi Amari. Universal statistics of fisher information in deep neural networks: mean field approach. 2018.
	- Mei, Song, Theodor Misiakiewicz, and Andrea Montanari. Mean-field theory of two-layers neural networks: dimension-free bounds and kernel limit. arXiv'19
	- Yaniv Blumenfeld, Dar Gilboa, and Daniel Soudry. A mean field theory of quantized deep networks: The quantization-depth trade-off. arXiv preprint arXiv:1906.00771, 2019.
	- Soufiane Hayou, Arnaud Doucet, and Judith Rousseau. Mean-field behaviour of neural tangent kernel for deep neural networks, 2019.
- Colin Wei, Jason D. Lee, Qiang Liu, and Tengyu Ma. Regularization matters: Generalization and optimization of neural nets v.s. their induced kernel, 2020
	- How finite-dim neural net approx infinite l1-network?
		- You need m=n+1;

## Universal Approximator
- Kurt Hornik. Approximation capabilities of multilayer feedforward networks. Neural networks, 4(2): 251–257, 1991.
- Hongzhou Lin, Stefanie Jegelka. ResNet with one-neuron hidden layers is a Universal Approximator. NIPS'18
- M. Leshno, V. Lin, A. Pinkus, and S. Schocken. Multilayer feedforward networks with a non- polynomial activation function can approximate any function. NN'93
- Ben Poole, Subhaneil Lahiri, Maithra Raghu, Jascha Sohl-Dickstein, and Surya Ganguli. Exponential expressivity in deep neural networks through transient chaos. NeurIPS'16
- Pierre Baldi. Neuronal Capacity. NIPS'18

## PAC-Bayes/Complexity/Generalization
- PL Bartlett, DJ Foster, MJ Telgarsky. Spectrally-normalized margin bounds for neural networks. NIPS'17
- N Golowich, A Rakhlin, O Shamir. Size-independent sample complexity of neural networks
- Behnam Neyshabur, Srinadh Bhojanapalli, Nathan Srebro. A pac-bayesian approach to spectrally-normalized margin bounds for neural networks. ICLR'18
	- Net: FF+ReLU
		- Tools: bound ∆output w.r.t. ∆weight, (bounding the sharpness);
		- Spectral norm of the layers and the Frobenius norm of the weights
	- Main result:
- Simon S Du, Jason D Lee, Haochuan Li, Liwei Wang, and Xiyu Zhai. Gradient descent finds global minima of deep neural networks. arXiv preprint arXiv:1811.03804, 2018a.
- Y Li, Y Liang. Learning overparameterized neural networks via stochastic gradient descent on structured data. NIPS'18
- R Novak, Y Bahri, DA Abolafia, J Pennington. Sensitivity and generalization in neural networks: an empirical study. arxiv'18
- Gaël Letarte, Pascal Germain, Benjamin Guedj, Francois Laviolette. Dichotomize and Generalize: PAC-Bayesian Binary Activated Deep Neural Networks. NIPS'18
- Vaishnavh Nagarajan and Zico Kolter. Deterministic PAC-bayesian generalization bounds for deep networks via generalizing noise-resilience. ICLR'19
- Wenda Zhou, Victor Veitch, Morgane Austern, Ryan P. Adams, and Peter Orbanz. Nonvacuous generalization bounds at the imagenet scale: a PAC-bayesian compression approach. ICLR'19
- Z Allen-Zhu, Y Li, Y Liang. Learning and generalization in overparameterized neural networks, going beyond two layers. NIPS'19
- Ping Li and Phan-Minh Nguyen. On random deep weight-tied autoencoders: Exact asymptotic analysis, phase transitions, and implications to training. ICLR'19
- Complexity:
	- Zi Yin, Yuanyuan Shen. On the Dimensionality of Word Embedding. NIPS'18
		- PIP loss, bias-variance trade-off
	- Simon Du. How Many Samples are Needed to Estimate a Convolutional Neural Network? NIPS'18
	- Léonard Blier, Yann Ollivier. The Description Length of Deep Learning models. NIPS'18
	- Chunyuan Li, Heerad Farkhoor, Rosanne Liu, Jason Yosinski. Measuring the Intrinsic Dimension of Objective Landscapes. ICLR'18
		- Insight: constrain the update in a subspace to recheck convergence;
- Behavior:
	- Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals. Understanding deep learning requires rethinking generalization. ICLR'17
		- **effective capacity**: successful neural network architectures is large enough to shatter the training data;

## Optimization/Convergence
- Initialization:
	- Amit Daniely, Roy Frostig, and Yoram Singer. Toward deeper understanding of neural networks: The power of initialization and a dual view on expressivity. NIPS'16
- Loss:
	- Anna Choromanska, Mikael Henaff, Michael Mathieu, Gérard Ben Arous, and Yann LeCun. The loss surfaces of multilayer networks. AISTATS'15
	- Daniel Soudry and Yair Carmon. No bad local minima: Data independent training error guarantees for multilayer neural networks. 2016
	- Nitish Shirish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping Tak Peter Tang. On large-batch training for deep learning: Generalization gap and sharp minima. arxiv'16
	- Itay Safran and Ohad Shamir. On the quality of the initial basin in overspecified neural networks. ICML'16
	- Quynh Nguyen and Matthias Hein. The loss surface of deep and wide neural networks. ICML'17
	- Janice Lan, Rosanne Liu, Hattie Zhou, Jason Yosinski. LCA: Loss Change Allocation for Neural Network Training. NIPS'19
		- Insight: module-wise training loss during iteration;
		<img src="/DL/images/empirical/lca-1.png" alt="drawing" width="450"/>\
		<img src="/DL/images/empirical/lca-2.png" alt="drawing" width="450"/>
	- Chiyuan Zhang, Samy Bengio, and Yoram Singer. Are all layers created equal? arxiv'19
- Over-Parametrization:
	- Zeyuan Allen-Zhu, Yuanzhi Li, and Zhao Song. A convergence theory for deep learning via over- parameterization. ICML'18
	- Francis Bach. On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport. NIPS'18
	- Behnam Neyshabur, Zhiyuan Li, Srinadh Bhojanapalli, Yann LeCun, Nathan Srebro. Towards Understanding the Role of Over-Parametrization in Generalization of Neural Networks, 2018
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
- Behavior:
	- Ian J Goodfellow, Oriol Vinyals, and Andrew M Saxe. Qualitatively characterizing neural network optimization problems. 2014
	- Hao Li, Zheng Xu, Gavin Taylor, Christoph Studer, and Tom Goldstein. Visualizing the Loss Landscape of Neural Nets. NIPS'18
	- **Double-Descent**: Preetum Nakkiran, Gal Kaplun, Yamini Bansal, Tristan Yang, Boaz Barak, Ilya Sutskever. Deep Double Descent: Where Bigger Models and More Data Hurt. ICLR'20
		- https://openai.com/blog/deep-double-descent/
		- Model-wise double descent: there is a regime where bigger models are worse;
			<img src="/DL/images/empirical/double-descent-1.png" alt="drawing" width="450"/>
		- Sample-wise non-monotonicity: there is a regime where more samples hurts;
			<img src="/DL/images/empirical/double-descent-2.png" alt="drawing" width="450"/>
		- Epoch-wise double descent;
		- Hypothesis: Our intuition is that, for models at the interpolation threshold, there is effectively only one model that fits the train data, and forcing it to fit even slightly noisy or misspecified labels will destroy its global structure. That is, there are no "good models" which both interpolate the train set and perform well on the test set. However, in the over-parameterized regime, there are many models that fit the train set and there exist such good models. Moreover, the implicit bias of stochastic gradient descent (SGD) leads it to such good models, for reasons we don't yet understand.

## Information Theory
- Samuel S Schoenholz, Justin Gilmer, Surya Ganguli, and Jascha Sohl-Dickstein. Deep information propagation. arXiv preprint arXiv:1611.01232, 2016.
