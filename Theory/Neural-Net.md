# Theory on Neural Net

## Basics
- Approximation theory:
	- Universal approximator, capacity;
- Statistical Generalization
	- overparametrization: more params does not lead to overfitting!
	- Complexity/expressiveness;
- Optimization:
	- Initialization:
	- Implicit regularization; (SGD, initialization)
	- Behavior: double-descent
	- Behavior: NTK
	- Batch size;
	- Loss surface;
- VI:
	- Mean field:
- Information Theory
- Connection with other:
	- Gaussian Process

## Unclassified
- M. Belkin, D. Hsu, S. Ma, and S. Mandal. Reconciling modern machine-learning practice and the classical bias-variance trade-off. PNAS'19
	- Does not increase monotonically with intermediate dim m;
- NIPS'19
	- D Elbrächter, J Berner, P Grohs. How degenerate is the parametrization of neural networks with the ReLU activation function?
	- S Arora, N Cohen, W Hu, Y Luo. Implicit Regularization in Deep Matrix Factorization
	- F Salehi, E Abbasi, B Hassibi. The Impact of Regularization on High-dimensional Logistic Regression
	- Q Qian, X Qian. The Implicit Bias of AdaGrad on Separable Data
	- A Golatkar, A Achille, S Soatto. Time Matters in Regularizing Deep Networks: Weight Decay and Data Augmentation Affect Early Learning Dynamics, Matter Little Near Convergence

## Universal Approximator
- M. Leshno, V. Lin, A. Pinkus, and S. Schocken. Multilayer feedforward networks with a non-polynomial activation function can approximate any function. NN'93
- K Hornik. Approximation capabilities of multilayer feedforward networks. Neural networks'91
- H Lin, S Jegelka. ResNet with one-neuron hidden layers is a Universal Approximator. NIPS'18
- Pierre Baldi. Neuronal Capacity. NIPS'18

## PAC-Bayes/Complexity/Generalization
- Complexity/Expressiveness:
	- B Poole, S Lahiri, M Raghu, J Sohl-Dickstein, and S Ganguli. Exponential expressivity in deep neural networks through transient chaos. NeurIPS'16
	- Z Yin, Y Shen. On the Dimensionality of Word Embedding. NIPS'18
		- PIP loss, bias-variance trade-off
	- S Du. How Many Samples are Needed to Estimate a Convolutional Neural Network? NIPS'18
	- L Blier, Y Ollivier. The Description Length of Deep Learning models. NIPS'18
	- C Li, H Farkhoor, R Liu, J Yosinski. Measuring the Intrinsic Dimension of Objective Landscapes. ICLR'18
		- Insight: constrain the update in a subspace to recheck convergence;
	- C Wei, T Ma. Data-dependent Sample Complexity of Deep Neural Networks via Lipschitz Augmentation. NeurIPS'19
	- N Golowich, A Rakhlin, O Shamir. Size-independent sample complexity of neural networks
- Empirical behavior:
	- C Zhang, S Bengio, M Hardt, B Recht, O Vinyals. Understanding deep learning requires rethinking generalization. ICLR'17
		- Neural-net large enough to shatter the training data;
	- R Novak, Y Bahri, DA Abolafia, J Pennington. Sensitivity and generalization in neural networks: an empirical study. arxiv'18
	- P Li and P Nguyen. On random deep weight-tied autoencoders: Exact asymptotic analysis, phase transitions, and implications to training. ICLR'19
- PAC-Bayes Generalization Bound:
	- PL Bartlett, DJ Foster, MJ Telgarsky. Spectrally-normalized margin bounds for neural networks. NIPS'17
	- B Neyshabur, S Bhojanapalli, N Srebro. A pac-bayesian approach to spectrally-normalized margin bounds for neural networks. ICLR'18
		- Net: FF+ReLU
			- Tools: bound ∆output w.r.t. ∆weight, (bounding the sharpness);
			- Spectral norm of the layers and the Frobenius norm of the weights
		- Main result:
	- V Nagarajan, Z Kolter. Uniform convergence may be unable to explain generalization in deep learning. NIPS'18
		- https://www.youtube.com/watch?v=o3GfnEjTdIQ
	- G Letarte, P Germain, B Guedj, F Laviolette. Dichotomize and Generalize: PAC-Bayesian Binary Activated Deep Neural Networks. NIPS'18
	- W Zhou, V Veitch, M Austern, R Adams, and P Orbanz. Nonvacuous generalization bounds at the imagenet scale: a PAC-bayesian compression approach. ICLR'19
	- V Nagarajan and Z Kolter. Deterministic PAC-bayesian generalization bounds for deep networks via generalizing noise-resilience. ICLR'19
	- Z Allen-Zhu, Y Li, Y Liang. Learning and generalization in overparameterized neural networks, going beyond two layers. NIPS'19
- Overparametrization:
	- L. Sagun, U. Evci, V. U. Guney, Y. Dauphin, and L. Bottou. Empirical analysis of the hessian of over-parametrized neural networks. CoRR'17
	- Y Li, Y Liang. Learning overparameterized neural networks via stochastic gradient descent on structured data. NIPS'18
	- Z Allen-Zhu, Y Li, and Z Song. A convergence theory for deep learning via over-parameterization. ICML'18
	- B Neyshabur, Z Li, S Bhojanapalli, Y LeCun, N Srebro. Towards Understanding the Role of Over-Parametrization in Generalization of Neural Networks, 2018
	- S Du, X Zhai, B Poczos, and A Singh. Gradient descent provably optimizes over-parameterized neural networks. arXiv preprint arXiv:1810.02054, 2018b
	- L Su, P Yang. On Learning Over-parameterized Neural Networks: A Functional Approximation Perspective. NIPS'19
- D Arpit, S Jastrzebski, N Ballas, D Krueger, E Bengio, M Kanwal, T Maharaj, A Fischer, A Courville, Y Bengio, and S Lacoste-Julien. A closer look at memorization in deep networks. ICML'17
	- Over-parametrized → memorize whole dataset with 0 error;

## Optimization/Convergence
- Initialization:
	- I Safran and O Shamir. On the quality of the initial basin in overspecified neural networks. ICML'16
	- A Daniely, R Frostig, and Y Singer. Toward deeper understanding of neural networks: The power of initialization and a dual view on expressivity. NIPS'16
- NTK:
	- Good resources:
		- https://lilianweng.github.io/posts/2022-09-08-ntk/
	- Insight: K(x, x') what sgd on x will influence f(x'); 
	- L(θ) = 1/N ∑.i l(f(xi;θ), yi)
	- ∇L(θ) = 1/N ∑.i ∇f(xi;θ) ∇l(f, yi)
	- Infinitesimal step GD: dθ/dt = -∇L(θ)
	- Prediction of new x:
		- df(x;θ)/dt = -1/N ∑.i ∇f(x)†∇f(xi) ∇l(f, yi)
		- NTK: ∇f(x)†∇f(xi)
	- Main result: infinite width, NTK converges to
		- Deterministic at initialization;
		- Stays constant during training;
	- Proof: by inducition. check NNGP.
	- Linearized model:
		- df(θ)/dt = -ηK∇L(f), (since K constant)
		- e.g. MSE loss: ∇L(f) = f(X;θ) - y; let 
			- ODE gives: f(θ) - y = C exp[-ηKt]
	- Lazy training with NTK:
		- Change in θ: Δθ ~ ∥y-f(θ0)∥/∥∇f(θ0)∥
		- Change in ∇θ: Δ∇θ ~ ∥y-f(θ0)∥∇2f(θ0) / ∥∇f(θ0)∥
		- Let κ(θ) = Δ∇θ/∥∇θ∥, E[κ(θ)] → 0;
	- A Jacot, F Gabriel, C Hongler. Neural Tangent Kernel: Convergence and Generalization in Neural Networks. NeurIPS'18
	- Y Li. Learning Overparameterized Neural Networks via Stochastic Gradient Descent on Structured Data. NIPS'18
	- L Chizat, E Oyallon, F Bach. On Lazy Training in Differentiable Programming. NeurIPS'19
	- S Du, K Hou, R Salakhutdinov, B Poczos, R Wang, and K Xu. Graph neural tangent kernel: Fusing graph neural networks with graph kernels. NeurIPS'19
	- G Yang. Scaling limits of wide neural networks with weight sharing: Gaussian process behavior, gradient independence, and neural tangent kernel derivation. arxiv'19
	- S Hayou, A Doucet, and J Rousseau. Mean-field behaviour of neural tangent kernel for deep neural networks, 2019
- Regularization:
	- C Wei, J Lee, Q Liu, and T Ma. Regularization matters: Generalization and optimization of neural nets v.s. their induced kernel, 2020
	- How finite-dim neural net approx infinite l1-network?
		- You need m=n+1;
- SGD:
	- SGD prefers flatter minimia, which generalizes better:
		- S. Hochreiter and J. Schmidhuber. Flat minima. NC'97
		- N. S. Keskar, D. Mudigere, J. Nocedal, M. Smelyanskiy, and P. T. P. Tang. On large-batch training for deep learning: Generalization gap and sharp minima. ICLR'17
		- L Wu, Z Zhu, and W E. Towards understanding generalization of deep learning: Perspective of loss landscapes. arxiv'17
		- S Jastrzebski, Z Kenton, D Arpit, N Ballas, A Fischer, Y Bengio, and A Storkey. Three factors influencing minima in sgd. arxiv'17
	- S Du, J D Lee, H Li, L Wang, and X Zhai. Gradient descent finds global minima of deep neural networks. arXiv'18
	- F Bach. On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport. NIPS'18
	- B Hanin. Which Neural Net Architectures Give Rise to Exploding and Vanishing Gradients. NIPS'18
	- Z Zhu, J Wu, B Yu, L Wu, and J Ma. The anisotropic noise in stochastic gradient descent: Its behavior of escaping from minima and regularization effects. arxiv'18
		- the specific non-isotropic structure of the noise is important for SGD to find flat minima;
		- minima found by GD (gradient decent) can be unstable for SGD;
	- A Zhu. Byzantine Stochastic Gradient Descent. NIPS'18
	- L Wu, C Ma, W E. How SGD Selects the Global Minima in Over-parameterized Learning: A Dynamical Stability Perspective. NIPS'18
		- GD to SGD: escape from minimum and converge to another;
		- Def3. Sharpness, non-uniformity. Let H = 1/nΣHi, Σ=1/nΣi=1..n Hi^2-H^2, We define a = max(H) to be the sharpness, and s = max(Σ^1/2) to be the non-uniformity, respectively.
	- U Şimşekli，L Sagun, M Gürbüzbalaban. A Tail-Index Analysis of Stochastic Gradient Noise in Deep Neural Networks. ICML'19 best paper honorable mention
	- Z Zhu, Y Li. Can SGD Learn Recurrent Neural Networks with Provable Generalization? NIPS'19
- Batchsize:
	- N Keskar, D Mudigere, J Nocedal, M Smelyanskiy, and P Tak P Tang. On large-batch training for deep learning: Generalization gap and sharp minima. arxiv'16
	- P Goyal, et. al. Accurate, large minibatch sgd: training imagenet in 1 hour. arxiv'17
	- E Hoffer, I Hubara, and D Soudry. Train longer, generalize better: closing the generalization gap in large batch training of neural networks. NIPS'17
		- the ratio between the learning rate and the batch size η/B is a key factor for flatness;
	- F He, T Liu, D Tao. Control Batch Size and Learning Rate to Generalize Well: Theoretical and Empirical Evidence. NIPS'18
- Loss surface:
	- A Choromanska, M Henaff, M Mathieu, G Arous, and Y LeCun. The loss surfaces of multilayer networks. AISTATS'15
	- D Soudry and Y Carmon. No bad local minima: Data independent training error guarantees for multilayer neural networks. 2016
	- J. Pennington and Y. Bahri. Geometry of neural network loss surfaces via random matrix theory. ICML'16
	- Q Nguyen and M Hein. The loss surface of deep and wide neural networks. ICML'17
	- S Mei, A Montanari, and P Nguyen. A mean field view of the landscape of two-layer neural networks. PNAS'18
	- J Lan, R Liu, H Zhou, J Yosinski. LCA: Loss Change Allocation for Neural Network Training. NeurIPS'19
		- Insight: module-wise training loss during iteration;
		<img src="/DL/images/empirical/lca-1.png" alt="drawing" width="450"/>\
		<img src="/DL/images/empirical/lca-2.png" alt="drawing" width="450"/>
	- C Zhang, S Bengio, and Y Singer. Are all layers created equal? arxiv'19
	- SAM: P Foret, A Kleiner, H Mobahi, and B Neyshabur. Sharpness-Aware Minimization for Efficiently Improving Generalization. ICLR'21
		- https://github.com/google-research/sam
		- Insight: loss function: seeks parameters that lie in neighborhoods having uniformly low loss
- Normalization:
	- S Santurkar, D Tsipras, A Ilyas, A Madry. How Does Batch Normalization Help Optimization? NeurIPS'18
	- N Bjorck, C Gomes, B Selman, K Weinberger. Understanding Batch Normalizations. NeurIPS'18
	- Y Xu, X Wang. Understanding Weight Normalized Deep Neural Networks with Rectified Linear Units. NIPS'18
- P Hand. Phase Retrieval Under a Generative Prior. NIPS'18
- A Zhu. NEON2: Finding Local Minima via First-Order Oracles. NIPS'18
- Are ResNets Provably Better than Linear Predictors? NIPS'18
- S Du, J Lee. Algorithmic Regularization in Learning Deep Homogeneous Models: Layers are Automatically Balanced. NIPS'18
- Behavior:
	- I Goodfellow, O Vinyals, and A Saxe. Qualitatively characterizing neural network optimization problems. 2014
	- H Li, Z Xu, G Taylor, C Studer, and T Goldstein. Visualizing the Loss Landscape of Neural Nets. NIPS'18
	- **Double-Descent**: P Nakkiran, G Kaplun, Y Bansal, T Yang, B Barak, I Sutskever. Deep Double Descent: Where Bigger Models and More Data Hurt. ICLR'20
		- https://openai.com/blog/deep-double-descent/
		- Model-wise double descent: there is a regime where bigger models are worse, then the bigger the better;
		- Sample-wise non-monotonicity: there is a regime where more samples hurts, then the more the better;
		- Epoch-wise double descent;
		- Hypothesis (intuition):
			- At the **interpolation threshold** regime, only 1 model fitting train, (slight noisy or misspecified labels will destroy)
				- i.e., no "good models" which both interpolate the train set and perform well on the test set. 
			- Over-parameterized regime, many models fitting train set. Implicit bias of SGD leads it to such good models.

## Variational Inference
- Mean field:
	- G Yang and S Schoenholz. Mean field residual networks: On the edge of chaos. NeurIPS'17
	- R Karakida, S Akaho, and S Amari. Universal statistics of fisher information in deep neural networks: mean field approach. 2018.
	- S Mei, T Misiakiewicz, and A Montanari. Mean-field theory of two-layers neural networks: dimension-free bounds and kernel limit. arXiv'19
	- Y Blumenfeld, D Gilboa, and D Soudry. A mean field theory of quantized deep networks: The quantization-depth trade-off. arXiv preprint arXiv:1906.00771, 2019.
	- S Hayou, A Doucet, and J Rousseau. Mean-field behaviour of neural tangent kernel for deep neural networks, 2019.

## Information Theory
- S Schoenholz, J Gilmer, S Ganguli, and J Sohl-Dickstein. Deep information propagation. arXiv preprint arXiv:1611.01232, 2016.

## NN as Gaussian Process
- R Neal. Prior for Infinite Networks. 94
- NNGP: J Lee, Y Bahri, R Novak, S Schoenholz, J Pennington, J Sohl-Dickstein. Deep Neural Networks as Gaussian Processes. ICLR'18
	- Infinite width:
		- ∑l+1(x, x') = E.f~N(0,Λl)[σ(f(x))†σ(f(x'))] + β^2
